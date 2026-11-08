"""Independent finite verification of affine-line membership concept dimensions.
No external dependencies; run with Python 3.10+.
"""
from functools import lru_cache
from itertools import combinations, product
from math import comb

def concept_data(p, e):
    q=p**e
    points=list(product(range(q), repeat=2))
    directions=[]
    for s in range(q): directions.append((1,s))
    for s in range(q):
        if s%p==0: directions.append((s,1))
    lines=set()
    for a,b in directions:
        for x,y in points:
            line=0
            for t in range(q):
                pt=((x+t*a)%q,(y+t*b)%q)
                line|=1<<points.index(pt)
            lines.add(line)
    return points, sorted(lines)

def ldim(lines, npoints):
    masks=[]
    for x in range(npoints):
        masks.append(sum(1<<i for i,line in enumerate(lines) if (line>>x)&1))
    all_h=(1<<len(lines))-1
    @lru_cache(None)
    def solve(active):
        if active & (active-1)==0: return 0
        best=0
        for bit in masks:
            a=active&bit; b=active&(~bit)
            if not a or not b: continue
            candidate=1+min(solve(a),solve(b))
            if candidate>best: best=candidate
        return best
    rank=solve(all_h)
    return rank, solve.cache_info().currsize

def witness_tree_for_pencils(p,e,points,lines):
    q=p**e
    point_to_idx={xy:i for i,xy in enumerate(points)}
    root=point_to_idx[(0,0)]
    y=point_to_idx[(1,0)]
    pencil0=sum((1<<j) for j,ln in enumerate(lines) if ln&(1<<root))
    pencily=sum((1<<j) for j,ln in enumerate(lines) if ln&(1<<y) and not ln&(1<<root))
    queries=[sum((1<<j) for j,ln in enumerate(lines) if ln&(1<<i)) for i in range(len(points))]
    @lru_cache(None)
    def tree(active, depth):
        if depth==0:
            return ("leaf", (active&-active).bit_length()-1) if active else None
        if active.bit_count() < (1<<depth): return None
        for i,mask in enumerate(queries):
            pos=active&mask; neg=active&~mask
            if pos.bit_count() < (1<<(depth-1)) or neg.bit_count() < (1<<(depth-1)):continue
            pt=tree(pos,depth-1)
            if pt is None:continue
            nt=tree(neg,depth-1)
            if nt is not None:return (i,nt,pt)
        return None
    pos=tree(pencil0,e)
    neg=tree(pencily,e)
    assert pos is not None and neg is not None, (p,e)
    root_tree=(root,neg,pos)
    count=0
    def verify(node,trace):
        nonlocal count
        if node[0]=="leaf":
            j=node[1]
            assert all(bool(lines[j]&(1<<i))==bool(a) for i,a in trace)
            count+=1
            return
        i,n,pv=node
        verify(n,trace+[(i,0)])
        verify(pv,trace+[(i,1)])
    verify(root_tree,[])
    assert count==2**(e+1)
    print('WITNESS_TREE',p,e,'depth',e+1,'leaves',count,flush=True)
    return root_tree

def vcdim_sample(lines,npoints,maxk=3):
    def shattered(items):
        traces={sum((1<<j) for j,x in enumerate(items) if (line>>x)&1) for line in lines}
        return len(traces)==1<<len(items)
    for k in range(1,maxk+1):
        c=sum(shattered(S) for S in combinations(range(npoints),k))
        if k<=2: assert c==comb(npoints,k), (npoints,k,c)
        elif k==3: assert c==0,(npoints,k,c)
    return True

if __name__=='__main__':
    for p,e in [(2,1),(3,1),(5,1),(2,2),(3,2),(2,3)]:
        pts,lines=concept_data(p,e)
        q=p**e
        assert len(lines)==q*(q+q//p), (p,e,len(lines))
        print('CASE',p,e,'points',len(pts),'lines',len(lines),flush=True)
        assert vcdim_sample(lines,len(pts))
        witness_tree_for_pencils(p,e,pts,lines)
        if (p,e) in [(2,1),(3,1),(2,2)]:
            d,states=ldim(lines,len(pts))
            assert d==e+1,(p,e,d)
            print('LDIM',d,'states',states,flush=True)
        else:
            print('Ldim for this larger case follows from the general proof.',flush=True)
    print('ALL_AFFINE_CHAIN_LINE_CHECKS_PASS')
