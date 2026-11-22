"""Validate independent full-state graph counts and geometric cycle census."""
from collections import Counter

def parse(filename):
    shells=Counter();basin=Counter();meta={}
    for line in open(filename,encoding='utf-8'):
        a=line.split()
        if not a: continue
        if a[0]=='SHELL': shells[tuple(map(int,a[1:3]))]=int(a[3])
        if a[0]=='BASIN': basin[tuple(map(int,a[1:3]))]=int(a[3])
        if a[0]=='TOTAL':meta['total']=int(a[1]);meta['extra']=a
    return shells,basin,meta
A=parse('clebsch_threshold2_a.log');B=parse('clebsch_threshold2_b.log')
assert A[0]==B[0] and A[1]==B[1], (A[0]-B[0],B[0]-A[0])
assert A[2]['total']==B[2]['total']==3**16
expected_shells={
    (0,1):1,(0,4):360,(1,1):65535,(1,4):5400,
    (2,1):3178531,(2,4):53160,(3,1):10245950,
    (4,1):15448184,(5,1):10086320,(6,1):3812880,(7,1):150400}
assert dict(A[0])==expected_shells
expected_basins={(1,42987801):1,(4,644):60,(4,676):30}
assert dict(A[1])==expected_basins
assert sum(A[0].values())==3**16
assert sum(size*count for (_,size),count in A[1].items())==3**16
assert sum(x for (d,p),x in A[0].items() if p==4)==58920
assert sum(x for (d,p),x in A[0].items() if p==1)==42987801
assert max(d for d,p in A[0])==7
print('CROSSCHECK OK: all 43,046,721 states; two independent full-state algorithms; 91 temporal cycles, 90 period-four; 7-step sharp entry.')
