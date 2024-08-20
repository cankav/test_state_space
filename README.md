# test_state_space
Test performance of LabelEncoder with large state space

Results from a i7-1355U

```
python3  run_test.py 10
state_space generation took 0.00 seconds
number of states: 1024
first state: 0000000000
last state: 1111111111

le generation took 0.00 seconds
LabelEncoder classes preview:
['0000000000' '0000000001' '0000000010' ... '1111111101' '1111111110'
 '1111111111']


total time 0.00 seconds
```


```
python3  run_test.py 20
state_space generation took 0.15 seconds
number of states: 1048576
first state: 00000000000000000000
last state: 11111111111111111111

le generation took 0.18 seconds
LabelEncoder classes preview:
['00000000000000000000' '00000000000000000001' '00000000000000000010' ...
 '11111111111111111101' '11111111111111111110' '11111111111111111111']


total time 0.33 seconds
```

```
python3  run_test.py 25
state_space generation took 6.24 seconds
number of states: 33554432
first state: 0000000000000000000000000
last state: 1111111111111111111111111

le generation took 7.56 seconds
LabelEncoder classes preview:
['0000000000000000000000000' '0000000000000000000000001'
 '0000000000000000000000010' ... '1111111111111111111111101'
 '1111111111111111111111110' '1111111111111111111111111']


total time 13.80 seconds
```