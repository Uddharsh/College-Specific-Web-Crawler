import json

f=open('document.json')
my_data=json.load(f)
fileout = open("doc_table.html", "w",encoding="utf-8")
table="<html>\n"
table+="<head>\n"
table+="	<title>Bootstrap Example</title>\n"
table+="	<meta charset='utf-8'>\n"
table+="	<meta name='viewport' content='width=device-width, initial-scale=1'>\n"
table+="	<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css'>\n"
table+="  	<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js'></script>\n"
table+="  	<script src='https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js'></script>\n"
table+="  	<script src='https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js'></script>\n"
table+="	<link rel='stylesheet' type='text/css' href='https://cdn.datatables.net/1.10.21/css/jquery.dataTables.css'>\n"
table+="	<script type='text/javascript' charset='utf8' src='https://cdn.datatables.net/1.10.21/js/jquery.dataTables.js'></script>\n"
table+="</head>\n"
table+="<body>\n"		
table+="<div class='container-fluid table-responsive'>\n"
table+= "<table class='table table-striped table-bordered table-hover' cellspacing='0' width='100%' id='doctableid'>\n"

# Create the table's column headers
table+="	<thead class='thead-dark'>\n"
header = "Document Heading,Document Link".split(",")
table += "		<tr>\n"
for column in header:
    table += "			<th>{0}</th>\n".format(column.strip())
table += "		</tr>\n"
table+="	</thead>\n"
table+='	<tbody id="doctab">\n'
# Create the table's row data
for x,y in my_data.items():
    table += "		<tr>\n"
    table += "			<td>{0}</td>\n".format(x.strip())
    table += "			<td>{0}</td>\n".format('<a href='+'"'+y.strip()+'"'+' target="_blank"'+'>'+y.strip()+'</a>')
    table += "		</tr>\n"
table+="	</tbody>\n"
table += "</table>\n"
table+="</div>"
table+="<script >$(document).ready( function () { $('#doctableid').DataTable();} );</script>\n"
table+="</body>\n"
table+="</html>"
fileout.writelines(table)
fileout.close()