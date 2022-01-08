package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
)

type Country struct {
	Name              string `json:name`
	CountryCode       string `json:countryCode`
	CountryCodeAlpha3 string `json:countryCodeAlpha3`
	Phone             string `json:phone`
	Currency          string `json:currency`
	StateProvinces    []StateProvince `json:stateProvinces`
}

type StateProvince struct {
	Name string `json:name`
}

var countries []Country

type Movie struct {
	Id    int `json:id`
	Title string `json:movie_title`
	Genre string `json:movie_genre`
	Year  string `json:release_year`
}

var movies []Movie

func handleRequests() {
	http.HandleFunc("/", homePage)
	http.HandleFunc("/getcountrylist", returnCountryList)
	http.HandleFunc("/getmovielist", returnMovieList)
	log.Fatal(http.ListenAndServe(":3300", nil))
}

func init() {
	getCountryList()
	getMovieList()
}

func main() {
	handleRequests()
}

func homePage(w http.ResponseWriter, r *http.Request){
	fmt.Fprintf(w, "Welcome to the HomePage!")
	fmt.Println("Endpoint Hit: homePage")
}

func returnCountryList(w http.ResponseWriter, r *http.Request){
	json.NewEncoder(w).Encode(countries)
}

func returnMovieList(w http.ResponseWriter, r *http.Request){
	json.NewEncoder(w).Encode(movies)
}

func getCountryList() {
	// Open our jsonFile
	jsonFile, err := os.Open("countryList.json")
	// if we os.Open returns an error then handle it
	if err != nil {
			fmt.Println(err)
	}

	fmt.Println("Successfully Opened countryList.json")
	// defer the closing of our jsonFile so that we can parse it later on
	defer jsonFile.Close()

	byteValue, _ := ioutil.ReadAll(jsonFile)
	// var result map[string]interface{}
  json.Unmarshal([]byte(byteValue), &countries)
	// fmt.Printf("Country : %+v", countries)
}

func getMovieList() {
	jsonFile, err := os.Open("movieList.json")
	if err != nil {
			fmt.Println(err)
	}

	fmt.Println("Successfully Opened movieList.json")
	defer jsonFile.Close()

	byteValue, _ := ioutil.ReadAll(jsonFile)
  json.Unmarshal([]byte(byteValue), &movies)
}