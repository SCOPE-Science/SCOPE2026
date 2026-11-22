#!/usr/bin/env python3
"""Direct small-case check of matching-complex homology on spider trees."""
from itertools import product,combinations

def matching_faces(lengths):
    edges=[]
    for i,L in enumerate(lengths):
        vs=[0]+[(i,j) for j in range(1,L+1)]
        edges.extend((vs[j-1],vs[j]) for j in range(1,L+1))
    out={0:[0]}
    def rec(pos, used, mask):
        if pos==len(edges):
            out.setdefault(mask.bit_count(),[]).append(mask)
            return
        rec(pos+1,used,mask)
        u,v=edges[pos]
        if u not in used and v not in used:
            rec(pos+1,used|{u,v},mask|(1<<pos))
    out={}
    rec(0,set(),0)
    return out

def rank2(cols):
    pivots={}
    for c in cols:
        while c:
            p=c.bit_length()-1
            if p in pivots:c^=pivots[p]
            else:
                pivots[p]=c
                break
    return len(pivots)

def reduced_betti(lengths):
    faces=matching_faces(lengths)
    grades=sorted(faces)
    ranks={0:1}
    for d in grades[1:]:
        below={m:i for i,m in enumerate(faces[d-1])}
        cols=[]
        for m in faces[d]:
            col=0
            x=m
            while x:
                bit=x&-x
                col ^= 1<<below[m^bit]
                x-=bit
            cols.append(col)
        ranks[d]=rank2(cols)
    return {d-1:len(faces[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in grades[1:] if len(faces[d])-ranks.get(d,0)-ranks.get(d+1,0)}

def formula(lengths):
    s=sum(L//3 for L in lengths)
    q=sum(L%3==2 for L in lengths)
    r=sum(L%3==1 for L in lengths)
    if q>=2 or (q==0 and r==1):return {}
    if q==1:return {s:1}
    if r==0:return {s-1:1} if s>=1 else {}  # impossible s0 for q=r=0
    return {s:r-1} if r>1 else {}

def test():
    tests=0; max_faces=0
    for a in range(1,5):
      for ls in product(range(1,6),repeat=a):
        if sum(ls)>17:continue
        actual=reduced_betti(ls)
        pred=formula(ls)
        assert actual==pred,(ls,actual,pred)
        tests+=1
        max_faces=max(max_faces,sum(map(len,matching_faces(ls).values())))
    print('PASS',tests,'spider length profiles; max face count',max_faces)
if __name__=='__main__':test()
