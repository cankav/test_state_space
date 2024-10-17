import sys
from datetime import datetime
#from sklearn.preprocessing import LabelEncoder
import pickle

# This script tests to see if we can generate a LabelEncoder that
# has a large number of states.
# States are assumed to be binary strings

# number of bits in our state space
bit_count = sys.argv[1]
filename = sys.argv[2]

start=datetime.now()
with open(filename,'rb') as fp:
    le=pickle.load(fp)
dump_load_time = (datetime.now()-start).total_seconds()
print(f"dump load took {dump_load_time:.2f} seconds")

start=datetime.now()
print(le.transform(['1'*int(bit_count)]))
transform_time1 =(datetime.now()-start).total_seconds()
print(f"first transform took {transform_time1:.2f} seconds")

start=datetime.now()
print(le.transform(['1'*int(bit_count), '1'*int(bit_count)]))
transform_time2 = (datetime.now()-start).total_seconds()
print(f"second transform took {transform_time2:.2f} seconds")

print(f"\n\ntotal time {dump_load_time+transform_time1+transform_time2:.2f} seconds")
