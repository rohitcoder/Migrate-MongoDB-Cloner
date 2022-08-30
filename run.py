from pymongo import MongoClient

sourceCluster = MongoClient("Connection_STRING_HERE")
sourcedb = sourceCluster["source_cluster_name_here"]

targetCluster = MongoClient("Connection_STRING_HERE")
targetdb = targetCluster["source_cluster_name_here"]


# list all collections and copy it to target cluster one by one
for collection in sourcedb.list_collection_names():
    print("Copying collection: " + collection)
    ## DOWNLOAD IN grouping of 5000 documents to avoid memory error and use insert_many()
    for doc in sourcedb[collection].find({}).batch_size(5000):
        targetdb[collection].insert_one(doc)
    print("\nCollection: " + collection + " copied to target cluster")