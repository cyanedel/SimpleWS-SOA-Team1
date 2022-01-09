<?php
header("Content-Type:application/json;charset=utf-8");
fetchData();
function fetchData(){
  require 'dblink.properties.php';
  $myArray = array();
  $sql = "select * from animals";
  $result = mysqli_query($dblink, $sql) or die("Error in Selecting " . mysqli_error($dblink));
  while($row = mysqli_fetch_assoc($result)){
    $myArray[] = $row;
  }
  
  echo json_encode($myArray,JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
  mysqli_close($dblink);
}
?>