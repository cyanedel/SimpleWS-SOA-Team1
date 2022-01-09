package main

import (
	"context"
	"time"
	"fmt"
	"log"
	"net/http"
	"encoding/json"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

type Movie struct {
	Title    string   `bson:"title,omitempty"`
	Id       int      `bson:"id,omitempty"`
	Genre    string   `bson:"genre,omitempty"`
	Year     string   `bson:"year,omitempty"`
}

var movielist []Movie

const uri = "mongodb://localhost:27017/?maxPoolSize=20&w=majority"

func handleRequests() {
	http.HandleFunc("/", homePage)
	http.HandleFunc("/getmovielist", returnMovieList)
	log.Fatal(http.ListenAndServe(":3300", nil))
}

func main() {
	client, err := mongo.NewClient(options.Client().ApplyURI(uri))
	if err != nil {
		log.Fatal(err)
	}
	ctx, _ := context.WithTimeout(context.Background(), 10*time.Second)
	err = client.Connect(ctx)
	if err != nil {
		log.Fatal(err)
	}
	defer client.Disconnect(ctx)

	collection := client.Database("soa").Collection("movielist")
	cur, currErr := collection.Find(ctx, bson.D{})

	if currErr != nil { panic(currErr) }
	defer cur.Close(ctx)

	if err = cur.All(ctx, &movielist); err != nil {
		panic(err)
	}

	// fmt.Println(movielist)

	handleRequests()
}

func homePage(w http.ResponseWriter, r *http.Request){
	fmt.Fprintf(w, "Welcome to go(lang) HomePage!")
}

func returnMovieList(w http.ResponseWriter, r *http.Request){
	json.NewEncoder(w).Encode(movielist)
}