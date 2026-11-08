"""Exact three-time history recurrence for synchronous binary majority on perfect cubic rooted trees."""
from itertools import product
from math import log
from sys import argv
HIST=list(product((0,1), repeat=3))
def majority(*xs): return int(sum(xs)>len(xs)//2)
def valid(v,p,a,b):
    return (v[1] == majority(p[0],a[0],b[0]) and
            v[2] == majority(p[1],a[1],b[1]) and
            v[1] == majority(p[2],a[2],b[2]))
def root_valid(v,a,b,c):
    return (v[1] == majority(a[0],b[0],c[0]) and
            v[2] == majority(a[1],b[1],c[1]) and
            v[1] == majority(a[2],b[2],c[2]))
D=[[int(v[1]==p[0] and v[2]==p[1] and v[1]==p[2]) for v in HIST] for p in HIST]
expected=[16,1024,3591360,44727123784320,7011368815622449172248037376,172073825280280505732279917684494237852672500611916959488]
for H in range(1,7):
  total=sum(D[vi][ai]*D[vi][bi]*D[vi][ci]
    for vi,v in enumerate(HIST)
    for ai,a in enumerate(HIST)
    for bi,b in enumerate(HIST)
    for ci,c in enumerate(HIST) if root_valid(v,a,b,c))
  assert total == expected[H-1],(H,total)
  print(f'H={H} vertices={3*2**H-2} first_entry_by_1={total} fraction={total/2**(3*2**H-2):.12g}')
  if H<6:
    new=[[sum(D[vi][ai]*D[vi][bi]
        for ai,a in enumerate(HIST) for bi,b in enumerate(HIST) if valid(v,p,a,b))
        for vi,v in enumerate(HIST)] for p in HIST]
    D=new
print('EXACT_RECURRENCE_OK')
