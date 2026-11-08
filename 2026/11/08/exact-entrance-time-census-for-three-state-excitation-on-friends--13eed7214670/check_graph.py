"""Independent brute-force labelled-graph checker for Greenberg--Hastings on a friendship graph.
Run: python3 check_graph.py. Uses only the Python 3 standard library.
"""
from collections import Counter
from itertools import product

COEFF = {
(0,1):{1:1},(0,3):{1:-3,3:3},(1,1):{1:-1,4:2},
(1,3):{1:1,3:-1,4:-1,6:1},(2,1):{7:1},
(2,3):{1:1,3:-1,7:-1,9:1},(3,1):{3:1,4:-1,7:1},
(3,3):{1:1,3:-1,7:-1,9:1},(4,1):{3:-1,4:-1,7:1},
(4,3):{4:1,6:-1,7:-1,9:1}}

def neighbors(r):
    v=2*r+1
    adj=[set() for _ in range(v)]
    for k in range(r):
        a,b=2*k+1,2*k+2
        for x,y in [(0,a),(0,b),(a,b)]:
            adj[x].add(y);adj[y].add(x)
    return tuple(tuple(sorted(a)) for a in adj)

def iterate(x,adj):
    y=[]
    for i,z in enumerate(x):
        if z==0:
            y.append(int(any(x[j]==1 for j in adj[i])))
        elif z==1:y.append(2)
        else:y.append(0)
    return tuple(y)

def entry(x,adj):
    found={};m=0
    while x not in found:
        found[x]=m;m+=1
        x=iterate(x,adj)
        assert m<=40
    return found[x],m-found[x]

if __name__=='__main__':
    count=0
    for r in range(1,6):
        adj=neighbors(r);classes=Counter()
        for x in product(range(3), repeat=2*r+1):
            classes[entry(tuple(x),adj)]+=1
            count+=1
        expected=Counter({key:sum(v*k**r for k,v in poly.items()) for key,poly in COEFF.items()})
        assert classes==expected,(r,classes,expected)
        print('GRAPH',r,'states',3**(2*r+1),'classes',dict(sorted(classes.items())))
    print('BRUTE_FORCE_OK',count)
