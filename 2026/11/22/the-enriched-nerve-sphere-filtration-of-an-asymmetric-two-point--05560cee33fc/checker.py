#!/usr/bin/env python3
"""Independent normalized-cell persistence checker for a finite two-point directed length nerve.
This checker enumerates ordered paths, takes signed simplicial faces, and filters by weights.
Finite tests support, but do not replace, the all-degree proof.
"""
from fractions import Fraction
from collections import Counter
from itertools import product

def path_cells(a,b,maxdim):
    cells=[]
    for d in range(maxdim+1):
        for start in (0,1):
            path=tuple((start+i)%2 for i in range(d+1))
            length=sum((a if (path[i],path[i+1])==(0,1) else b) for i in range(d))
            cells.append((length,d,path))
    return sorted(cells)

def reduced_boundary(path):
    faces=[]
    if len(path)<2: return faces
    for i in range(len(path)):
        face=path[:i]+path[i+1:]
        if any(face[j]==face[j+1] for j in range(len(face)-1)): continue
        faces.append((face, (-1)**i))
    return faces

def persistence(a,b,maxdim=10):
    cells=path_cells(a,b,maxdim)
    indices={p:i for i,(_,_,p) in enumerate(cells)}
    reduced={}; lows={}; paired_births=set()
    for j,(weight,d,p) in enumerate(cells):
        col=set()
        for face,coef in reduced_boundary(p):
            idx=indices[face]
            if idx in col: col.remove(idx)
            else: col.add(idx)
        while col:
            low=max(col)
            if low not in lows:break
            col.symmetric_difference_update(reduced[lows[low]])
        reduced[j]=col
        if col:
            lows[max(col)]=j
            paired_births.add(max(col))
    intervals=[]
    for birth,death in lows.items():
        bw,bd,_=cells[birth]; dw,_,_=cells[death]
        if bw<dw:intervals.append((bd,bw,dw))
    for i,(w,d,_) in enumerate(cells):
        if not reduced[i] and i not in paired_births:intervals.append((d,w,None))
    return Counter(intervals),cells

def expected(a,b,maxdim):
    s=a+b
    output=Counter({(0,Fraction(0),a):1,(0,Fraction(0),None):1})
    for d in range(1,maxdim):
        if d%2==1:
            m=(d-1)//2
            output[(d,m*s+b,(m+1)*s)]+=1
        else:
            m=d//2
            output[(d,m*s,m*s+a)]+=1
    return output

def check():
    attempts=0
    for ai,bi in product(range(1,9),repeat=2):
        a=Fraction(ai);b=Fraction(bi)
        actual,cells=persistence(a,b,maxdim=12)
        # The latest 12-cells are truncated. Exclude any intervals with birth dimension >=11
        actual=Counter({key:v for key,v in actual.items() if key[0]<=10})
        want=expected(min(a,b),max(a,b),11)
        assert actual==want,(a,b,actual-want,want-actual)
        # Integral signed boundaries, face by face, satisfy d^2=0.
        for _,dim,path in cells:
            if dim<=1: continue
            dd=Counter()
            for f,c in reduced_boundary(path):
                for ff,cc in reduced_boundary(f):dd[ff]+=c*cc
            assert all(v==0 for v in dd.values()),(a,b,path,dd)
        attempts+=1
    # Include rational asymmetric weights and near-tie to test exact thresholds.
    for a,b in [(Fraction(1,2),Fraction(3,2)),(Fraction(1,3),Fraction(2,3)),
                (Fraction(5,7),Fraction(5,7)),(Fraction(7,10),Fraction(9,10))]:
        actual,_=persistence(a,b,maxdim=12)
        actual=Counter({key:v for key,v in actual.items() if key[0]<=10})
        want=expected(min(a,b),max(a,b),11)
        assert actual==want,(a,b,actual-want,want-actual)
        attempts+=1
    print('PASS: %s exact-weight two-point instances; all reduced persistence bars through degree 10; integral d^2=0.'%attempts)
if __name__=='__main__':check()
