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






Feel free to modify and clear up.I might try an interactive CLI browser at some point too.
Thx,







