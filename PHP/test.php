<?php
header("Content-Type:application/json");
$hello = '[{"key1": "value1"},{"key2": "value2"},{"key3": "value3"},{"key4": "value4"}]';
response($hello);

function response($data){	
	$json_response = json_encode($data);
  echo $json_response;
}
?>