import itertools
import sys
from datetime import datetime
from sklearn.preprocessing import LabelEncoder
import pickle
import os

# This script tests to see if we can generate a LabelEncoder that
# has a large number of states.
# States are assumed to be binary strings

# number of bits in our state space
bit_count = sys.argv[1]
filename = sys.argv[2]

try:
    bit_count = int(bit_count)
except ValueError:
    raise Exception("Unexpecte bit_count value {bit_count}, value must be integer")

start = datetime.now()
state_space = list([ ''.join(x) for x in itertools.product(['0', '1'], repeat=bit_count)])
state_space_time = (datetime.now()-start).total_seconds()
print(f"state_space generation took {state_space_time:.2f} seconds")
print(f"number of states: {len(state_space)}")
print(f"first state: {state_space[0]}")
print(f"last state: {state_space[-1]}")

start = datetime.now()
le = LabelEncoder()
le.fit( state_space )
le_time = (datetime.now()-start).total_seconds()
print(f"\nle generation took {le_time:.2f} seconds")
print("LabelEncoder classes preview:")
print(le.classes_)

start = datetime.now()
with open(filename,'wb') as fp:
    pickle.dump(le,fp)
dump_time = (datetime.now()-start).total_seconds()
print(f"dumping took {dump_time:.2f} seconds")
cmd = f'du -sh {filename}'
print('dump size')
os.system(cmd)

print(f"\n\ntotal time {state_space_time+le_time+dump_time:.2f} seconds")
