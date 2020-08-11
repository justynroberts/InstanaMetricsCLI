rm output.csv
#Remove Headers if you dont need
echo "Cluster","Namespace","Deployment Count","Pod Count" >> output.csv
for cluster in $(python3 queryinstana.py label FROM  KubernetesCluster where 'entity.selfType:kubernetesCluster' )
do
    for namespace in $(python3 queryinstana.py label FROM  KubernetesNamespace where entity.kubernetes.cluster.label:$cluster )
    do
        for deployment in $(python3 queryinstana.py count FROM  KubernetesDeployment where 'entity.kubernetes.cluster.label:'$cluster' AND entity.kubernetes.namespace:'$namespace )
        do 
            for pod in $(python3 queryinstana.py count FROM  KubernetesPod where 'entity.kubernetes.cluster.label:'$cluster' AND entity.kubernetes.namespace:'$namespace)
            do
                #Output everything
                echo "$cluster","$namespace","$deployment","$pod" 
                echo "$cluster","$namespace","$deployment","$pod" >> output.csv
           done
        done
    done
done