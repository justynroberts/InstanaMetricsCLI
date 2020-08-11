# Metric Calculator

Simple **CLI** for querying metrics with the Instana API. Written for Python 3.x

# Installation Instructions

You will need Python 3.x in your path.
You will also need to install the pip module `requests`

    pip3 install `requests`

## Format 
The main runtime is queryinstana.py which accepts the following commands :-
 

     queryinstana.py [Attribute|count] from|ascsv [Plugin] where [Dynamic Focus Query]

`Attribute` can be any field name returned in the API, but generally `label` will be used for this example
`count` returns the number of records for the value of Attribute


    from|ascsv|count


`From` denotes a line delimited return  of the value of Attribute (useful in a bash For/Each scenario) 
`ascsv` denotes a csv delimited return of the value of Attribute



    [Dynamic focus Query]

Add a query to refine your search criteria



## Sample



## Sample Cost Calculator

All your files and folders are presented as a tree in the file explorer. You can switch from one to another by clicking a file in the tree.

## Rename a file

You can rename the current file by clicking the file name in the navigation bar or by clicking the **Rename** button in the file explorer.

## Delete a file

You can delete the current file by clicking the **Remove** button in the file explorer. The file will be moved into the **Trash** folder and automatically deleted after 7 days of inactivity.

## Export a file

You can export the current file by clicking **Export to disk** in the menu. You can choose to export the file as plain Markdown, as HTML using a Handlebars template or as a PDF.


# Getting started

You will need to make two modifications to the `instanaquery.py` to get started :-

`APItoken =` "Your API Token" - Generated in the Instana UI

`Instance =` "demoeu-instana" - The name of your Instance (Please note you do not need the .instana.io, just the environment/tenant name)



# Sample

1. A simple query for Kubernetes Namespaces :-

> python3 queryinstana.py label from KubernetesCluster where
> 'entity.selfType:kubernetesCluster'

Will return all labels (names) for each K8s cluster you have deployed.


# Advanced
Putting this all together, its easy to iterate and parse in a bash script.

sampleusage.sh creates an output CSV of Clusters,Namespaces, Pods and Deployments.





Feel free to modify and clear up.






