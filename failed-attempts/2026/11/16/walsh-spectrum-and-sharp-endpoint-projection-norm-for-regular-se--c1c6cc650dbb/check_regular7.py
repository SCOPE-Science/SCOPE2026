#!/usr/bin/env python3
"""Exact integer certificate for Walsh convolution by K7 regular-tournament indicator.
Run: python3 check_regular7.py [--write] from the directory with the CSV files.
No third-party packages are needed.
"""
from collections import Counter
from pathlib import Path
import csv, math, sys

N = 7
Q = 3
INNER = [(i,j) for i in range(1,N) for j in range(i+1,N)]
assert len(INNER)==15
INCIDENT = {v:sum(1<<k for k,(i,j) in enumerate(INNER) if i==v or j==v) for v in range(1,N)}


def is_regular(y):
    out = [0]*N
    for k,(i,j) in enumerate(INNER):
        if y & (1<<k): out[i]+=1
        else: out[j]+=1
    for j in range(1,N):
        s = (Q-j-(y&INCIDENT[j]).bit_count()) & 1
        out[0]+=s
        out[j]+=1-s
    return all(z==Q for z in out)


def fwht(a):
    a = list(a)
    d=len(a)
    h=1
    while h<d:
        for start in range(0,d,2*h):
            for i in range(start,start+h):
                x,y=a[i],a[i+h]
                a[i]=x+y
                a[i+h]=x-y
        h*=2
    return a


def csv_out(filename,values):
    with open(filename,'w',newline='',encoding='utf-8') as f:
        w=csv.writer(f,lineterminator='\n')
        w.writerow(('index','value'))
        w.writerows(enumerate(values))


def csv_check(filename,values):
    with open(filename,encoding='utf-8',newline='') as f:
        rows=csv.reader(f)
        assert next(rows)==['index','value']
        count=0
        for i,row in enumerate(rows):
            assert len(row)==2 and int(row[0])==i and int(row[1])==values[i], (filename,i)
            count+=1
        assert count==len(values), (filename,count)


def main():
    f=[int(is_regular(x)) for x in range(1<<15)]
    assert sum(f)==2640
    v=fwht(f)
    h=Counter(abs(x) for x in v)
    assert h=={0:24112,16:3780,32:420,48:1365,80:630,96:1260,112:360,176:630,240:105,528:105,2640:1},h
    assert sum(x*x for x in v)==(1<<15)*2640
    assert min(abs(x) for x in v if x)!=0
    assert min(abs(x) for x in v if x)==16 and max(abs(x) for x in v)==2640
    assert all(v[x]==0 for x in range(1<<15) if x.bit_count()&1)
    z=fwht([int(x!=0) for x in v])
    k=Counter(abs(x) for x in z)
    assert k=={0:5760,16:3360,32:6720,48:11760,64:1344,80:2730,208:560,240:420,496:112,8656:2},k
    assert sum(abs(x) for x in z)==1427840
    assert sum(x*x for x in z)==(1<<15)*8656
    # A character frequency on the 21-edge cube has one of 2^6 lifts
    # of each quotient frequency, with the same absolute coefficient.
    assert sum(int(x!=0) for x in v)*(1<<6)==553984
    # Direct sums for frequencies chosen without using the Walsh recursion.
    support=[i for i,a in enumerate(f) if a]
    for u in [0,1,3,7,0x7fff,0x5555,0x1234,0x432,0x7777,0x3456,0x6aaa]:
        direct=sum(1 if (u & y).bit_count()%2==0 else -1 for y in support)
        assert direct==v[u],(u,direct,v[u])
    if '--write' in sys.argv:
        csv_out('walsh_quotient.csv',v)
        csv_out('projection_kernel.csv',z)
    else:
        csv_check('walsh_quotient.csv',v)
        csv_check('projection_kernel.csv',z)
    assert (sum(abs(x) for x in z)//math.gcd(sum(abs(x) for x in z),1<<15),
            (1<<15)//math.gcd(sum(abs(x) for x in z),1<<15))==(11155,256)
    print('REGULAR7_WALSH_RANGE_PASS count=2640 quotient=32768 nonzero=8656 rank=553984 gap=16 projection=11155/256')

if __name__=='__main__': main()
