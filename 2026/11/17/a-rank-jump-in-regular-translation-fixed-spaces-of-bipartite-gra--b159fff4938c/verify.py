"""Direct finite checks for regular-translation fixed bipartite graph complexes.
Standard-library Python 3, no third-party packages.
"""
from itertools import product
from collections import defaultdict

def elements(moduli):
    return list(product(*(range(n) for n in moduli)))

def inverse(x, moduli):
    return tuple(-v % m for v,m in zip(x,moduli))

def reps_for_edge_orbits(moduli):
    zero=(0,)*len(moduli);seen=set();reps=[]
    for x in elements(moduli):
        if x==zero or x in seen:continue
        y=inverse(x,moduli);seen.add(x);seen.add(y);reps.append(x)
    return reps

def valuation(x,m):
    if x==0:return None
    j=0
    while x%2==0:x//=2;j+=1
    return j

def cayley_bipartite(moduli,reps,mask):
    # Construct connected components by actual graph search, never using characters.
    vals=elements(moduli); ix={x:i for i,x in enumerate(vals)}
    step=[reps[i] for i in range(len(reps)) if (mask>>i)&1]
    col=[-1]*len(vals)
    for root in range(len(vals)):
        if col[root]!=-1:continue
        col[root]=0; q=[root]
        for v in q:
            for s in step:
                w=ix[tuple((vals[v][j]+s[j])%moduli[j] for j in range(len(moduli)))]
                if col[w]<0:col[w]=1-col[v];q.append(w)
                elif col[w]==col[v]:return False
    return True

def faceted(a,reps,mask):
    for k in range(a):
        if all(((mask>>i)&1)==0 or (x!=0 and valuation(x,2**a)==k) for i,(x,b,*_) in enumerate(reps)):
            return True
    if all(((mask>>i)&1)==0 or b==1 for i,(x,b,*_) in enumerate(reps)):
        return True
    for k in range(a):
        if all(((mask>>i)&1)==0 or (x%(2**k)==0 and (x//(2**k)+b)%2==1) for i,(x,b,*_) in enumerate(reps)):
            return True
    return False

def nerve(a):
    # F_k=0..a-1, G_{-1}=a, G_k=a+k+1.
    facets=[]
    big=sum(1<<j for j in range(a,2*a+1));facets.append(big)
    for k in range(a):
        fk=1<<k
        less=sum(1<<j for j in range(a,a+k+1))
        facets.append(fk|less)
        facets.append(fk|(1<<(a+k+1)))
    return facets

def gf2_betti(facets,nv):
    faces={0}
    for f in facets:
        sub=f
        while sub:
            faces.add(sub);sub=(sub-1)&f
    layers=defaultdict(list)
    for face in faces:layers[face.bit_count()-1].append(face)
    def rank(vecs):
        piv={}
        for x in vecs:
            while x:
                k=x.bit_length()-1
                if k not in piv:piv[k]=x;break
                x^=piv[k]
        return len(piv)
    ranks={}
    for k in range(1,max(layers)+1):
        idx={v:i for i,v in enumerate(layers[k-1])}
        boundaries=[]
        for f in layers[k]:
            x=f;bitset=0
            while x:
                b=x&-x;bitset^=1<<idx[f^b];x-=b
            boundaries.append(bitset)
        ranks[k]=rank(boundaries)
    return {k:len(layers[k])-ranks.get(k,0)-ranks.get(k+1,0)-(k==0) for k in range(max(layers)+1)}

if __name__=='__main__':
    for a in range(1,5):
        mods=(2**a,2);reps=reps_for_edge_orbits(mods)
        passed=0
        for mask in range(1<<len(reps)):
            actual=cayley_bipartite(mods,reps,mask)
            expected=faceted(a,reps,mask)
            assert actual==expected,(mods,mask,actual,expected)
            passed+=1
        print(f'CYCLIC_BY_TWO a={a}: {len(reps)} edge-orbit vertices, {passed} selections tested; facet formula PASS')
        betti=gf2_betti(nerve(a),2*a+1)
        assert {k:v for k,v in betti.items() if v}=={1:a},(a,betti)
        print(f'NERVE a={a}: reduced mod-two Betti numbers {{1:{a}}} PASS')
    # Odd-part invariance checked via independent graph traversal and projected selection.
    for mods in [(4,2,3),(2,2,3),(4,2,5)]:
        reps=reps_for_edge_orbits(mods)
        if len(reps)>18:
            # A fixed, deterministic 12,000 subset check, plus all singletons and pairs.
            masks=[0]+[1<<i for i in range(len(reps))]+[(1<<i)|(1<<j) for i in range(len(reps)) for j in range(i+1,len(reps))]
            s=1729
            for _ in range(12000):
                s=(1664525*s+1013904223)&0xffffffff
                masks.append(s&((1<<len(reps))-1))
        else:masks=range(1<<len(reps))
        total=0
        for mask in masks:
            xs=[reps[i] for i in range(len(reps)) if (mask>>i)&1]
            if any(x==0 and b==0 for x,b,t in xs):expected=False
            else:
                p_reps=reps_for_edge_orbits(mods[:2]); ip={frozenset((p,inverse(p,mods[:2]))):j for j,p in enumerate(p_reps)}
                projection=0
                for x,b,t in xs:projection|=1<<ip[frozenset(((x,b),inverse((x,b),mods[:2])))]
                expected=cayley_bipartite(mods[:2],p_reps,projection)
            got=cayley_bipartite(mods,reps,mask)
            assert got==expected,(mods,mask,got,expected)
            total+=1
        print(f'ODD_PART moduli={mods}: {total} edge-orbit subsets, graph-traversal vs projected graph PASS')
    print('ALL_REGULAR_BIPARTITE_FIXED_SPACE_CHECKS_PASS')
