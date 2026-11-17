"""Exact simplicial Morse-certificate verifier for three seven-column multiple chessboard complexes."""
from collections import Counter, deque
from functools import lru_cache

N=7; CAPACITIES=((1,1,1,5),(1,1,2,4),(1,1,3,3))

def boundary(mask):
    m=mask; i=0
    while m:
        bit=m&-m; m-=bit
        yield mask-bit, (1 if not i%2 else -1)
        i+=1

def generate(cap):
    current=[(0,(0,0,0,0))]
    for c in range(N):
        nxt=[]
        for face,counts in current:
            nxt.append((face,counts))
            for r in range(4):
                if counts[r]<cap[r]:
                    new=list(counts);new[r]+=1
                    nxt.append((face|(1<<(c*4+r)),tuple(new)))
        current=nxt
    return {face for face,_ in current}

def matching(faces):
    remaining=set(faces)-{0}; pairs={}
    for v in range(4*N):
        for face in tuple(remaining):
            if face & (1<<v): continue
            other=face|(1<<v)
            if other in remaining:
                remaining.remove(face);remaining.remove(other)
                pairs[face]=other;pairs[other]=face
    return pairs,remaining

def acyclic(faces,pairs):
    nonempty=faces-{0}; indeg=dict.fromkeys(nonempty,0); outgoing={x:[] for x in nonempty}
    covers=0
    for higher in nonempty:
        for lower,_ in boundary(higher):
            if not lower:continue
            covers+=1
            if pairs.get(lower)==higher:
                a,b=lower,higher
            else:a,b=higher,lower
            outgoing[a].append(b);indeg[b]+=1
    todo=deque(x for x,d in indeg.items() if d==0);visited=0
    while todo:
        x=todo.popleft();visited+=1
        for y in outgoing[x]:
            indeg[y]-=1
            if indeg[y]==0:todo.append(y)
    assert visited==len(nonempty),('cycle',len(nonempty)-visited)
    return covers

def morse_boundary(k,crit,pairs):
    lower=sorted(x for x in crit if x.bit_count()==k)
    higher=sorted(x for x in crit if x.bit_count()==k+1)
    lookup={x:i for i,x in enumerate(lower)}
    active=set()
    @lru_cache(None)
    def expand(face):
        assert face not in active,'unexpected gradient cycle'
        active.add(face)
        if face in lookup:
            result={lookup[face]:1}
        elif face in pairs and pairs[face].bit_count()==k+1:
            up=pairs[face]
            pivot=next(v for x,v in boundary(up) if x==face)
            result={}
            for x,sgn in boundary(up):
                if x==face:continue
                for i,value in expand(x).items():
                    result[i]=result.get(i,0)-pivot*sgn*value
            result={i:v for i,v in result.items() if v}
        else:result={}
        active.remove(face)
        return result
    columns=[]
    for top in higher:
        col={}
        for face,sgn in boundary(top):
            for i,v in expand(face).items():col[i]=col.get(i,0)+sgn*v
        columns.append({i:v for i,v in col.items() if v})
    return len(lower),columns

def full_unit_rank(m,columns):
    """Greedy *integer* elementary Morse cancellations: every pivot is +/-1."""
    rows=[{j:v for j,col in enumerate(columns) if (v:=col.get(i,0))} for i in range(m)]
    remaining_rows=set(range(m));remaining_cols=set(range(len(columns)))
    number=0;maxentry=0
    while remaining_rows:
        candidates=[]
        for i in remaining_rows:
            options=[j for j,v in rows[i].items() if j in remaining_cols and abs(v)==1]
            if options:candidates.append((len(rows[i]),i,options[0]))
        if not candidates:break
        _,ri,cj=min(candidates)
        pivot=rows[ri][cj]
        active=dict(rows[ri]); active.pop(cj,None)
        for i in remaining_rows-{ri}:
            a=rows[i].pop(cj,0)
            if a:
                for j,v in active.items():
                    u=rows[i].get(j,0)-a*pivot*v
                    if u:rows[i][j]=u
                    else:rows[i].pop(j,None)
                    maxentry=max(maxentry,abs(u))
        remaining_rows.remove(ri);remaining_cols.remove(cj)
        number+=1
    return number,maxentry

def run(cap):
    faces=generate(cap)
    pairs,crit=matching(faces)
    covers=acyclic(faces,pairs)
    dims=Counter(f.bit_count()-1 for f in crit)
    b3,c4=morse_boundary(4,crit,pairs)
    b4,c5=morse_boundary(5,crit,pairs)
    assert b3==dims[3] and len(c4)==dims[4]
    assert b4==dims[4] and len(c5)==dims[5]
    for col in c5:
        d={}
        for row,coef in col.items():
            for i,v in c4[row].items():d[i]=d.get(i,0)+coef*v
        assert all(v==0 for v in d.values()),'d^2 failure'
    rank4,max4=full_unit_rank(b3,c4)
    rank5,max5=full_unit_rank(b4,c5)
    assert rank4==b3 and rank5==b4-rank4,(cap,rank4,rank5,b3,b4)
    top=len(c5)-rank5
    print(f'capacities={cap} faces_with_empty={len(faces)} covers={covers} pairs={len(pairs)//2} critical={dict(sorted(dims.items()))}')
    print(f'Morse_d4={b3}x{len(c4)} unit_pivots={rank4}; Morse_d5={b4}x{len(c5)} unit_pivots={rank5}; d4*d5=0; max_pivot_update={max(max4,max5)}')
    print(f'HOMOTOPY=wedges_of_{top}_S5')
    return top
if __name__=='__main__':
    answer=[run(x) for x in CAPACITIES]
    assert answer==[15,57,57],answer
    print('ALL_EXACT_CHECKS_PASSED')
