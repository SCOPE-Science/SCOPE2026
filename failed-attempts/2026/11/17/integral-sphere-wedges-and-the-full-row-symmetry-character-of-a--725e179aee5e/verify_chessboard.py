#!/usr/bin/env python3
"""Independent finite simplicial/Morse-chain verification for a 4-by-7 board.
Requires only Python 3.10+ standard library. Prints deterministic certificate totals.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache

ROWS=(1,2,2,2)
COLUMNS=7
N=len(ROWS)*COLUMNS

def enumerate_faces():
    result=set()
    def extend(col, used, mask):
        if col==COLUMNS:
            result.add(mask)
            return
        extend(col+1,used,mask)
        for r, cap in enumerate(ROWS):
            if used[r]<cap:
                used[r]+=1
                extend(col+1,used,mask | (1 << (4*col+r)))
                used[r]-=1
    extend(0,[0]*4,0)
    return result

def lower_faces(cell):
    x=cell
    while x:
        bit=x&-x
        yield cell^bit, (-1 if (cell & (bit-1)).bit_count()%2 else 1)
        x-=bit

def matching(faces):
    remaining=set(faces)
    pairs=[]
    for v in range(N):
        for a in sorted(remaining,key=lambda x:(x.bit_count(),x)):
            b=a|(1<<v)
            if b!=a and b in remaining:
                remaining.remove(a)
                remaining.remove(b)
                pairs.append((a,b))
    return remaining,pairs

def check_acyclic(faces,pairs):
    paired=set(pairs)
    indeg={f:0 for f in faces}
    adj=defaultdict(list)
    covers=0
    for upper in faces:
        for lower,_ in lower_faces(upper):
            assert lower in faces
            covers+=1
            # Reverse each matched Hasse arrow.
            x,y=(lower,upper) if (lower,upper) in paired else (upper,lower)
            adj[x].append(y)
            indeg[y]+=1
    q=deque(f for f,d in indeg.items() if d==0)
    visited=0
    while q:
        f=q.popleft()
        visited+=1
        for g in adj[f]:
            indeg[g]-=1
            if indeg[g]==0:q.append(g)
    assert visited==len(faces),(visited,len(faces))
    return covers

def morse_chain(critical,pairs):
    upper={b for a,b in pairs}
    low={a:b for a,b in pairs}
    assert not (critical & upper) and not (critical & low.keys())
    @lru_cache(None)
    def reduction(f):
        if f in critical:return {f:1}
        if f in upper:return {}
        g=low[f]
        a=dict(lower_faces(g))[f]
        out=defaultdict(int)
        for facet,c in lower_faces(g):
            if facet==f:continue
            for h,d in reduction(facet).items():out[h]-=a*c*d
        return {h:c for h,c in out.items() if c}
    D={}
    for k in sorted({f.bit_count()-1 for f in critical}):
        cols={}
        for f in sorted(critical):
            if f.bit_count()-1!=k:continue
            out=defaultdict(int)
            for facet,a in lower_faces(f):
                for h,c in reduction(facet).items():out[h]+=a*c
            cols[f]={h:c for h,c in out.items() if c}
            assert all(h.bit_count()==k for h in cols[f])
        D[k]=cols
    for k in sorted(D):
        if k+1 not in D:continue
        for column in D[k+1].values():
            out=defaultdict(int)
            for f,a in column.items():
                for h,b in D[k].get(f,{}).items():out[h]+=a*b
            assert not any(out.values()),f'd^2 nonzero in dimension {k}'
    return D

def integer_unit_cancel(columns):
    cols={c:dict(v) for c,v in columns.items()}
    pivots=[];largest=0
    while True:
        rows=defaultdict(set)
        for col,d in cols.items():
            for row,value in d.items():
                assert value!=0
                largest=max(largest,abs(value))
                rows[row].add(col)
        units=[(len(rows[r])*len(cols[c]),r,c,a)
               for c,d in cols.items() for r,a in d.items() if abs(a)==1]
        if not units:break
        _,r,c,a=min(units)
        pivots.append((r,c))
        for j in rows[r]-{c}:
            factor=cols[j][r]*a
            for i,val in cols[c].items():
                nextval=cols[j].get(i,0)-factor*val
                if nextval:cols[j][i]=nextval
                else:cols[j].pop(i,None)
        del cols[c]
    return cols,pivots,largest

def main():
    faces=enumerate_faces()
    size_counts=dict(sorted(Counter(f.bit_count()-1 for f in faces).items()))
    critical,pairs=matching(faces)
    assert len(critical)+2*len(pairs)==len(faces)
    covers=check_acyclic(faces,pairs)
    critical_counts=dict(sorted(Counter(f.bit_count()-1 for f in critical).items()))
    assert size_counts=={-1:1,0:28,1:315,2:1785,3:5250,4:7560,5:4410,6:630},size_counts
    assert critical_counts=={3:30,4:393,5:336},critical_counts
    D=morse_chain(critical,pairs)
    for k in [4,5]:
        print(f'Morse differential d{k}: columns={len(D[k])}, nonzero entries={sum(map(len,D[k].values()))}')
    rem4,p4,max4=integer_unit_cancel(D[4])
    assert len(p4)==30 and not any(rem4.values())
    canceled={c for _,c in p4}
    rem5,p5,max5=integer_unit_cancel({j:{i:a for i,a in d.items() if i not in canceled} for j,d in D[5].items()})
    assert len(p5)==300 and not any(rem5.values()),(len(p5),len(rem5))
    assert len(rem5)==36
    assert len(D[4])-len(p4)-len(p5)==63
    # Exact integer unit pivots certify no torsion in any homology group.
    print('face_counts',size_counts)
    print('face_count_total',len(faces))
    print('Hasse_cover_count',covers,'matching_pairs',len(pairs),'critical_counts',critical_counts)
    print('unit_pivots_d4',len(p4),'max_coefficient_d4',max4)
    print('unit_pivots_d5',len(p5),'max_coefficient_d5',max5)
    print('reduced_integral_homology','H4=Z^63','H5=Z^36','all others zero','torsion=none')
    print('verification: PASS')

if __name__=='__main__':main()
