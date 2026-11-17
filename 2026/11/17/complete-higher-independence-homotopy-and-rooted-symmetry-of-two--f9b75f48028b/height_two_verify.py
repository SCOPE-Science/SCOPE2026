"""Exact finite tests for higher-independence topology of rooted height-two trees."""
from itertools import permutations, product
from collections import deque, defaultdict
from math import comb


def structure(q):
    n=len(q)
    A=tuple(range(n)); B=tuple(range(n,n+sum(q)))
    groups=[]; z=n
    for t in q:
        groups.append(tuple(range(z,z+t)));z+=t
    return A,B,groups

def root_complex(q,r):
    A,B,groups=structure(q)
    N=1+len(A)+len(B)
    masks=[]
    for m in range(1<<N):
        # root absent: connected components are separate stars
        if not (m & 1):
            ok=all(((m>>(i+1))&1)==0 or 1+sum((m>>(1+j))&1 for j in groups[i])<=r for i in A)
        else:
            # root connected to each present branch vertex
            size=1+sum(((m>>(i+1))&1)*(1+sum((m>>(1+j))&1 for j in groups[i])) for i in A)
            ok=size<=r
        if ok:masks.append(m)
    return masks

def link_complex(q,r):
    A,B,groups=structure(q)
    N=len(A)+len(B)
    masks=[]
    for m in range(1<<N):
        w=sum(((m>>i)&1)*(1+sum((m>>j)&1 for j in groups[i])) for i in A)
        if w<=r-1:masks.append(m)
    return masks

def match_link(q,r):
    A,B,groups=structure(q)
    f=link_complex(q,r); S=set(f); rem=set(f); pairs={}
    for group in groups:
        b=1<<group[0]
        for x in sorted(rem):
            if x not in rem or x&b:continue
            y=x|b
            if y in rem:
                pairs[x]=y;rem.remove(x);rem.remove(y)
    # exactly one critical facet for every t-subset of all leaves except first leaf
    n=len(q);Q=sum(q);t=r-n-1
    expected=comb(Q-1,t) if 0<=t<=Q-1 else 0
    assert len(rem)==expected,(q,r,'critical',len(rem),expected)
    assert all(x.bit_count()==r-1 and all((x>>a)&1 for a in A) and not ((x>>groups[0][0])&1) for x in rem)
    # complete Hasse diagram with reversed matched pairs
    indeg={x:0 for x in S};adj={x:[] for x in S};E=0
    for x in S:
        for j in range(n+Q):
            y=x|(1<<j)
            if y==x or y not in S:continue
            if pairs.get(x)==y: u,v=y,x
            else:u,v=x,y
            adj[u].append(v);indeg[v]+=1;E+=1
    D=deque(x for x in S if indeg[x]==0);cnt=0
    while D:
        x=D.popleft();cnt+=1
        for y in adj[x]:
            indeg[y]-=1
            if indeg[y]==0:D.append(y)
    assert cnt==len(S),(q,r,'directed cycle')
    return len(S),E,len(rem)

def rank2(vectors):
    piv={}
    for x in vectors:
        while x:
            b=x.bit_length()-1
            if b not in piv:
                piv[b]=x;break
            x^=piv[b]
    return len(piv)

def homology_mod2(faces,nverts):
    bydim=defaultdict(list)
    for f in faces:bydim[f.bit_count()-1].append(f)
    rk={};dim=max(bydim)
    for d in range(0,dim+1):
        lower={f:i for i,f in enumerate(bydim[d-1])}
        cols=[]
        for f in bydim[d]:
            v=0
            for j in range(nverts):
                if (f>>j)&1:v^=1<<lower[f^(1<<j)]
            cols.append(v)
        rk[d]=rank2(cols)
    return {d:len(bydim[d])-rk[d]-rk.get(d+1,0) for d in range(-1,dim+1) if len(bydim[d])-rk.get(d,0)-rk.get(d+1,0)>0}

def rooted_actions(q):
    n=len(q);A,B,groups=structure(q);N=n+len(B)
    for pa in permutations(A):
        if any(q[i]!=q[pa[i]] for i in A):continue
        for reorders in product(*(tuple(permutations(groups[pa[i]])) for i in A)):
            p=[0]*N
            for i in A:
                p[i]=pa[i]
                for old,new in zip(groups[i],reorders[i]):p[old]=new
            yield tuple(p)

def signed_fixed_sum(faces,p):
    out=0
    for f in faces:
        verts=[i for i in range(len(p)) if f>>i&1]
        img=[p[i] for i in verts]
        if set(img)!=set(verts):continue
        inv=sum(img[i]>img[j] for i in range(len(img)) for j in range(i+1,len(img)))
        out+=(-1)**(len(verts)+inv)
    return out

def cyclic_lengths(p):
    seen=set();ls=[]
    for i in range(len(p)):
        if i in seen:continue
        j=i; k=0
        while j not in seen:
            seen.add(j);k+=1;j=p[j]
        ls.append(k)
    return ls

def expected_character(q,r,p):
    n=len(q);Q=sum(q);t=r-n-1
    if t<0 or t>Q-1:return 0
    cA=len(cyclic_lengths(p[:n])); sig=(-1)**(n-cA)
    leaf_perm=[p[n+j]-n for j in range(Q)]
    co=[1]+[0]*t
    for length in cyclic_lengths(leaf_perm):
        co=[co[j]-(co[j-length] if j>=length else 0) for j in range(t+1)]
    return sig*(-1)**t*sum(co)

def check():
    params=[(1,1),(1,1,1),(2,1),(2,2),(3,1),(2,1,1),(2,2,1),(3,2),(3,1,1),(3,3)]
    tests=inc=faces=characters=direct=0
    for q in params:
        n=len(q);Q=sum(q);m=max(q)
        acts=list(rooted_actions(q))
        for r in range(1,n+Q+2):
            nf,ne,nc=match_link(q,r)
            tests+=1;faces+=nf;inc+=ne
            graph_faces=root_complex(q,r)
            bet=homology_mod2(graph_faces,n+Q+1)
            t=r-n-1
            expected={}
            upper=1
            for qi in q:upper*=comb(qi-1,r-1) if 1<=r<=qi else 0
            if upper:expected[n*r-1]=upper
            if 0<=t<=Q-1:expected[r-1]=comb(Q-1,t)
            assert bet==expected,(q,r,'homology',bet,expected)
            direct+=1
            link=link_complex(q,r)
            for p in acts:
                # on link: reduced Euler fixed trace is -signed_fixed_sum;
                # single possible homology degree r-2
                trace=(-1)**(r-1)*signed_fixed_sum(link,p)
                expected_trace=expected_character(q,r,p)
                assert trace==expected_trace,(q,r,p,trace,expected_trace)
                characters+=1
        print('PROFILE',q,'r_range',(1,n+Q+1),'actions',len(acts))
    extra=homology_mod2(root_complex((4,4),3),11)
    assert extra=={2:1,5:9},extra
    print('MIXED_PROFILE_4_4_PASS',extra)
    print('HEIGHT_TWO_TREE_EXACT_PASS','cases',tests,'link_faces',faces,'face_incidences',inc,'mod2_graph_tests',direct,'signed_characters',characters)

if __name__=='__main__':check()
