function dret()
{
  var x = document.getElementById("document_retriever");
  if (x.style.display === "none") 
  {
    x.style.display = "block";
  }
  else
  {
  	x.style.display = "block";
  }
  xdret();
}
function xdret()
{
  var x = document.getElementById("webpage_retriever");
  if (x.style.display === "block") 
  {
    x.style.display = "none";
  }
}
function wpret()
{
  var x = document.getElementById("webpage_retriever");
  if (x.style.display === "none") 
  {
    x.style.display = "block";
  }
  else
  {
    x.style.display = "block";
  }
  xwpret();
}
function xwpret()
{
  var x = document.getElementById("document_retriever");
  if (x.style.display === "block") 
  {
    x.style.display = "none";
  }
}

			