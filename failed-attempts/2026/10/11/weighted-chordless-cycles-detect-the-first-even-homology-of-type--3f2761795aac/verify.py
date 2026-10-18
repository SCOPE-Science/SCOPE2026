from itertools import permutations,combinations
from math import comb

def graph_c4_plus_isolates(indices,r):
    seq=list(indices)
    return {tuple(sorted((seq[i],seq[(i+1)%4]))) for i in range(4)}

def gf2rank(cols):
    piv={}
    for v in cols:
        while v:
            k=v.bit_length()-1
            if k in piv: v^=piv[k]
            else: piv[k]=v;break
    return len(piv)

def bettis_clique(r, edges, submask):
    verts=[i for i in range(r) if submask>>i&1]
    if not verts:return {-1:1}
    faces={}
    for l in range(1,len(verts)+1):
        f=[s for s in combinations(verts,l) if all((u,v) in edges for u,v in combinations(s,2))]
        if f:faces[l-1]=f
    ranks={}
    for dim in range(1,max(faces)+1):
        lower={f:i for i,f in enumerate(faces[dim-1])}
        cols=[]
        for f in faces[dim]:
            v=0
            for face in combinations(f,dim):v^=1<<lower[face]
            cols.append(v)
        ranks[dim]=gf2rank(cols)
    b={}
    for dim in faces:
        val=len(faces[dim])-ranks.get(dim,0)-ranks.get(dim+1,0)-(1 if dim==0 else 0)
        if val:b[dim]=val
    return b

def run_cost(mask,r):
    cost=0;pos=0
    while pos<r:
        if not (mask>>pos&1):pos+=1;continue
        end=pos
        while end<r and mask>>end&1:end+=1
        l=end-pos
        cost+=l*(l+1)//2;pos=end
    return cost

def calc_degrees(r,edges):
    betti={mask:bettis_clique(r,edges,mask) for mask in range(1<<r)}
    total={}
    lengthsmin={}
    for p in permutations(range(r+1)):
        m=sum((p[i]>p[j]) for i in range(r+1) for j in range(i+1,r+1))
        D=sum((1<<i) for i in range(r) if p[i]>p[i+1])
        lengthsmin[D]=min(lengthsmin.get(D,10**9),m)
        for j,rank in betti[D].items():
            n=2*m+1+j
            total[n]=total.get(n,0)+rank
    return total, lengthsmin,betti

def test():
    for r in range(2,8):
        em=set()
        for p in permutations(range(r+1)):
            mask=sum((1<<i) for i in range(r) if p[i]>p[i+1])
            length=sum(p[i]>p[j] for i in range(r+1) for j in range(i+1,r+1))
            em.add((mask,length))
        for mask in range(1<<r):
            assert min(l for D,l in em if D==mask)==run_cost(mask,r)
    print('MIN_INV_VERIFIED for all subsets r=2..7')
    for r,d in [(7,[0,1,2,3]),(7,[0,2,4,6]),(6,[0,1,3,5]),(5,[0,1,2,3])]:
        edges=graph_c4_plus_isolates(d,r)
        ranks,mins,b=calc_degrees(r,edges)
        earliest=min((n for n,val in ranks.items() if n>0 and n%2==0 and val>0),default=None)
        target=2*run_cost(sum(1<<v for v in d),r)+2
        print('r=',r,'cycle=',d,'target=',target,'first_even=',earliest,'rank=',ranks.get(earliest),'odd_nonzero=',sum(v for n,v in ranks.items() if n%2),'even_nonzero=',sum(v for n,v in ranks.items() if n>0 and n%2==0))
        assert earliest==target
    for r in [4,5,6]:
        for edges in [{(i,i+1) for i in range(r-1)}, {tuple(p) for p in combinations(range(r),2)}, {(0,1),(1,2),(2,3),(0,2)}]:
            ranks,_,_=calc_degrees(r,edges)
            assert not any(n>0 and n%2==0 for n in ranks)
    print('CHORDAL_TESTS_VERIFIED')
    print('VERIFY_OK')
if __name__=='__main__':test()

def chordless_masks(r,edges):
    found=[]
    for mask in range(1<<r):
        v=[i for i in range(r) if mask>>i&1]
        if len(v)<4:continue
        if any(sum(tuple(sorted((u,w))) in edges for w in v if w!=u)!=2 for u in v):continue
        seen={v[0]}; stack=[v[0]]
        while stack:
            z=stack.pop()
            for w in v:
                if w not in seen and tuple(sorted((z,w))) in edges:
                    seen.add(w);stack.append(w)
        if len(seen)==len(v):found.append(mask)
    return found

def test_cycle_cost_rank():
    # Independent construction of the least weighted chordless cycles,
    # compared with every permutation/induced-clique homology contribution.
    for r in (4,5,6):
        complete=list(combinations(range(r),2))
        graphs=[]
        graphs.append(set(complete))
        graphs.append({(i,i+1) for i in range(r-1)})
        graphs.append(set(graph_c4_plus_isolates(range(4),r)))
        graphs.append({(i,j) for i,j in complete if (3*i+5*j+r)%4!=0})
        graphs.append({(i,j) for i,j in complete if (7*i+3*j+r)%5 in (0,1)})
        for edges in graphs:
            cycles=chordless_masks(r,edges)
            hom,_,_=calc_degrees(r,edges)
            ev=[q for q,v in hom.items() if q>0 and q%2==0 and v>0]
            if not cycles:
                assert not ev
            else:
                m=min(run_cost(d,r) for d in cycles)
                q=2*m+2
                assert min(ev)==q and hom[q]==sum(run_cost(d,r)==m for d in cycles)
    print('INDEPENDENT_CYCLE_MINIMUM_AND_RANK_VERIFIED')

if __name__=='__main__':test_cycle_cost_rank()
