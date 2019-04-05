from datetime import datetime
from biocommons.seqrepo import SeqRepo

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
#SEQUENCES = {
#    "id": {
#        "name": "NC_000001.11", 
#        "timestamp": get_timestamp()
#    }
#}

# Create a handler for our read (GET) people
def read():
    # Create the list of people from our data
    sr = SeqRepo("/usr/local/share/seqrepo/latest")
    return sr["NC_000001.11"][780000:780020]
    #return [SEQUENCES[key] for key in sorted(SEQUENCES.keys())]
