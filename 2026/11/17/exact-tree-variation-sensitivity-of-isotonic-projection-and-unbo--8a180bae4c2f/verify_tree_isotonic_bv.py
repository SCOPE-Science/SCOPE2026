"""Exact finite-tree variation/isotonic-block certificate, standard library only.
Public research reproducibility code. Run: python verify_tree_isotonic_bv.py.
"""
from fractions import Fraction
from itertools import combinations, product

def edges_path(n): return [(i,i+1) for i in range(n-1)]
def edges_star(m): return [(0,i) for i in range(1,m+1)]
def edges_caterpillar(k):
    return [(i,i+1) for i in range(k-1)]+[(i,k+i) for i in range(k)]

def components(n,edges,exclude=set()):
    adj=[[] for _ in range(n)]
    for idx,(a,b) in enumerate(edges):
        if idx not in exclude: adj[a].append(b);adj[b].append(a)
    labels=[-1]*n;comps=[]
    for i in range(n):
        if labels[i]!=-1: continue
        st=[i];labels[i]=len(comps);comp=[]
        while st:
            v=st.pop();comp.append(v)
            for w in adj[v]:
                if labels[w]<0: labels[w]=len(comps);st.append(w)
        comps.append(comp)
    return labels,comps

def by_subtree(n,edges):
    best=Fraction(1);arg=None;ne=len(edges)
    for mask in range(1,1<<n):
        S={i for i in range(n) if (mask>>i)&1}
        if len(S)<2:continue
        inside=[i for i,(u,v) in enumerate(edges) if u in S and v in S]
        if len(inside)!=len(S)-1:continue
        for ei in inside:
            (u,v)=edges[ei]
            adj={x:[] for x in S}
            for j in inside:
                if j==ei:continue
                a,b=edges[j];adj[a].append(b);adj[b].append(a)
            A={u};todo=[u]
            while todo:
                for w in adj[todo.pop()]:
                    if w not in A:A.add(w);todo.append(w)
            B=S-A
            a,b=len(A),len(B)
            p=sum(x in A and y not in S or y in A and x not in S for x,y in edges)
            q=sum(x in B and y not in S or y in B and x not in S for x,y in edges)
            gain=Fraction(b*p+a*q,a+b)
            if gain>best:best,arg=gain,(tuple(sorted(S)),ei,a,b,p,q)
    return best,arg

def block_norm(n,edges):
    best=Fraction(1);arg=None
    for mask in range(1<<len(edges)):
        excluded={i for i in range(len(edges)) if not(mask>>i&1)}
        lab,blocks=components(n,edges,excluded)
        for ei in range(len(edges)):
            labels,cut=components(n,edges,{ei})
            assert len(cut)==2
            y=[Fraction(labels[v]) for v in range(n)]
            avg=[sum(y[v] for v in blk)/len(blk) for blk in blocks]
            z=[avg[lab[v]] for v in range(n)]
            tv=sum(abs(z[u]-z[v]) for u,v in edges)
            if tv>best:best,arg=tv,(mask,ei)
    return best,arg

def theorem_examples():
    cnt=0
    for n in range(2,9):
        es=edges_path(n)
        a,_=by_subtree(n,es);b,_=block_norm(n,es)
        assert a==b==1,(n,a,b)
        cnt+=1
    for m in range(1,8):
        es=edges_star(m)
        a,_=by_subtree(m+1,es);b,_=block_norm(m+1,es)
        expected=max(Fraction(1),Fraction(m-1,2))
        assert a==b==expected,(m,a,b,expected)
        cnt+=1
    for k in range(2,6):
        es=edges_caterpillar(k)
        a,_=by_subtree(2*k,es)
        b,_=block_norm(2*k,es)
        lower=Fraction(2*(k//2)*((k+1)//2),k)
        assert a==b and a>=lower,(k,a,b,lower)
        cnt+=1
    # A nontrivial asymmetric example where blocks of more than two vertices matter.
    for es,n in [([(0,1),(1,2),(1,3),(3,4),(3,5),(5,6)],7),
                 ([(0,1),(1,2),(1,3),(2,4),(4,5),(4,6)],7)]:
        a,_=by_subtree(n,es);b,_=block_norm(n,es)
        assert a==b,(es,a,b)
        cnt+=1
    print('ALL_CONNECTED_SUBTREE_VS_INDEPENDENT_EDGE_PARTITION_CHECKS_PASSED',cnt)
    for m in (3,4,7):
        print('STAR_EXACT',m,str(by_subtree(m+1,edges_star(m))[0]))
    for k in (3,4,5,6):
        val,arg=by_subtree(2*k,edges_caterpillar(k))
        print('CATERPILLAR_EXACT',k,str(val),'BACKBONE_BOUND',str(Fraction(2*(k//2)*((k+1)//2),k)))
    print('ALL_ISOTONIC_TREE_VARIATION_DIAGNOSTICS_PASSED')

if __name__=='__main__':theorem_examples()

def side_profile(n,edges,root,cut):
    """Max number of outward boundary edges for each rooted-subtree size.
    The edge cut is excluded from the rooted side.
    """
    adj=[[] for _ in range(n)]
    for i,(u,v) in enumerate(edges):
        if i!=cut:adj[u].append(v);adj[v].append(u)
    def rec(v,parent):
        children=[w for w in adj[v] if w!=parent]
        dp={1:len(children)}
        for w in children:
            child=rec(w,v)
            new=dict(dp)
            for a,bb in dp.items():
                for k,cc in child.items():
                    z=bb+cc-1
                    if z>new.get(a+k,-1):new[a+k]=z
            dp=new
        return dp
    return rec(root,-1)

def via_knapsack(n,edges):
    best=Fraction(1);arg=None
    for ei,(u,v) in enumerate(edges):
        pa=side_profile(n,edges,u,ei)
        pb=side_profile(n,edges,v,ei)
        for a,aa in pa.items():
            for b,bb in pb.items():
                gain=Fraction(b*aa+a*bb,a+b)
                if gain>best:best=gain;arg=(ei,a,b,aa,bb)
    return best,arg

def strict_kkt_witness(n,edges,active,edge_step):
    """Exact rational verification of a local affine region with a chosen active forest."""
    labels,blocks=components(n,edges,set(range(len(edges)))-set(active))
    num=len(blocks);quot=[(labels[u],labels[v]) for i,(u,v) in enumerate(edges) if i not in active]
    assert all(a!=b for a,b in quot)
    level=[0]*num
    for _ in range(num):
        for a,b in quot:level[b]=max(level[b],level[a]+1)
    assert all(level[b]>level[a] for a,b in quot)
    xi=[Fraction(10*level[labels[i]]) for i in range(n)]
    y=list(xi)
    for ei in active:
        u,v=edges[ei];y[u]+=1;y[v]-=1 # y=xi-D^T lambda
    (u,v)=edges[edge_step];side,_=components(n,edges,{edge_step})
    h=[Fraction(s) for s in side];eps=Fraction(1,10000)
    z=[y[i]+eps*h[i] for i in range(n)]
    avg=[sum(z[v] for v in b)/len(b) for b in blocks]
    out=[avg[labels[i]] for i in range(n)]
    residual=[out[i]-z[i] for i in range(n)] # D^T lambda
    lam={}
    # solve tree divergence for internal active edges, independently in each block
    for block in blocks:
        adj={v:[] for v in block}
        for ei in active:
            u,v=edges[ei]
            if u in adj and v in adj:
                adj[u].append((v,ei));adj[v].append((u,ei))
        r={v:residual[v] for v in block}
        todo=set(block)
        while len(todo)>1:
            leaf=next((v for v in todo if sum(w in todo for w,_ in adj[v])==1),None)
            assert leaf is not None
            neighbor,ei=next((w,e) for w,e in adj[leaf] if w in todo)
            sign=1 if edges[ei][1]==leaf else -1
            val=r[leaf]/sign
            lam[ei]=val
            r[neighbor]+=r[leaf] # since opposite incidence at neighbor
            todo.remove(leaf)
        assert not r[next(iter(todo))]
    assert all(lam[e]>0 for e in active),(active,lam)
    assert all(out[v]>out[u] for i,(u,v) in enumerate(edges) if i not in active)
    assert all(out[v]==out[u] for i,(u,v) in enumerate(edges) if i in active)
    tv_in=sum(abs(h[v]-h[u]) for u,v in edges)
    assert tv_in==1
    tv_out=sum(abs(out[v]-out[u]-(xi[v]-xi[u])) for u,v in edges)/eps
    # Note xi is the base projection; exact quotient for perturbation.
    return tv_out

def extra_checks():
    cnt=0
    for n,es in [(5,edges_path(5)),(6,edges_star(5)),(8,edges_caterpillar(4)),
                  (7,[(0,1),(1,2),(1,3),(3,4),(3,5),(5,6)])]:
        a,_=by_subtree(n,es);d,_=via_knapsack(n,es)
        assert a==d,(es,a,d)
        for mask in range(1<<len(es)):
            active={i for i in range(len(es)) if mask>>i&1}
            labels,blocks=components(n,es,set(range(len(es)))-active)
            for ei in range(len(es)):
                kkt=strict_kkt_witness(n,es,active,ei)
                # Independent average matrix difference quotient equals KKT ratio.
                hlabel,_=components(n,es,{ei})
                h=[Fraction(t) for t in hlabel]
                avg=[sum(h[v] for v in block)/len(block) for block in blocks]
                out=[avg[labels[i]] for i in range(n)]
                tv=sum(abs(out[v]-out[u]) for u,v in es)
                assert kkt==tv,(n,mask,ei,kkt,tv)
                cnt+=1
    print('EXACT_KKT_ACTIVE_FOREST_AND_LOCAL_RATIO_WITNESSES_PASSED',cnt)
    print('TREE_SIDE_KNAPSACK_VS_SUBTREE_ENUMERATION_PASSED 4')

if __name__=='__main__':extra_checks()
