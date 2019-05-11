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
#def read():
#    # Create the list of people from our data
#    from biocommons.seqrepo import SeqRepo
#    sr = SeqRepo("/usr/local/share/seqrepo/latest")
#    #return sr["NC_000001.11"][780000:780020]
#    #return [sr[key] for key in sorted(sr.keys())]
#    #return sr.fetch('NM_000059.3', start=10, end=22)
#    #return [sr[seq_id] for seq_id in sorted(sr.seq_id())]
    
    
def search():    
    from biocommons.seqrepo import SeqRepo
    sr = SeqRepo("/usr/local/share/seqrepo/latest")
    #return [sr[key] for key in sorted(sr.keys())]
    return sr["NC_000001.11"][780000:780020]
    
