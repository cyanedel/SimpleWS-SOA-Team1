<?php
header("Content-Type:application/json;charset=utf-8");
if(isset($_GET["id"])){
  fetchData($_GET["id"]);
} else {
  fetchData("");
}

function fetchData($id){
  require 'dblink.properties.php';
  $myArray = array();
  $sql = "SELECT * FROM animals WHERE 1=1 ";
  if($id != ""){
    $sql .= " AND id=".$id;
  }
  
  $result = mysqli_query($dblink, $sql) or die("Error in Selecting " . mysqli_error($dblink));
  while($row = mysqli_fetch_assoc($result)){
    $myArray[] = $row;
  }
  
  echo json_encode($myArray,JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
  mysqli_close($dblink);
}
?>