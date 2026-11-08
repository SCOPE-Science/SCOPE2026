"""Independent enumeration of the ordered-configuration graph spine and its arm-orbit graph."""
from itertools import permutations, combinations
from math import factorial, comb
from collections import deque, defaultdict


def compositions(p,m):
    if m==1:
        yield (p,)
    else:
        for q in range(p+1):
            for c in compositions(p-q,m-1):yield (q,)+c

def placements(labels,m):
    for perm in permutations(labels):
        for comp in compositions(len(labels),m):
            a=[];j=0
            for count in comp:
                a.append(tuple(perm[j:j+count]));j+=count
            yield tuple(a)

def group(gens,m):
    ident=tuple(range(m));seen={ident};todo=[ident]
    for g in todo:
        for h in gens:
            x=tuple(g[h[i]] for i in range(m))
            if x not in seen:seen.add(x);todo.append(x)
    return todo

def act(A,g):
    B=[None]*len(A)
    for i,x in enumerate(A):B[g[i]]=x
    return tuple(B)

def orbit_map(states,G):
    states=set(states);visited=set();mp={};n=0
    for x in states:
        if x in visited:continue
        orb={act(x,g) for g in G}
        assert orb<=states
        for y in orb:mp[y]=n
        visited|=orb;n+=1
    return mp,n

def beta_burnside(p,G):
    def chi(f):
        rise=1
        for j in range(p-1):rise*=f+j
        return (2*p-1-(p-1)*f)*rise
    chi_avg=sum(chi(sum(g[i]==i for i in range(len(g)))) for g in G)
    assert chi_avg%len(G)==0
    return 1-chi_avg//len(G)

def run_case(m,p,gens,name):
    G=group(gens,m)
    A=list(placements(tuple(range(p)),m))
    B=[]
    for c in range(p):
        B.extend((c,a) for a in placements(tuple(x for x in range(p) if x!=c),m))
    # For B states, only the arm-placement component moves under arm permutations.
    mapA,va=orbit_map(A,G)
    mapsB={}; vb=0
    for c in range(p):
        states=[a for z,a in B if z==c]
        mpc,nc=orbit_map(states,G)
        for a,ix in mpc.items():mapsB[c,a]=ix+vb
        vb+=nc
    edge_orbs=set()
    incidence=[]
    for c,arr in B:
        for arm in range(m):
            changed=list(arr);changed[arm]=(c,)+changed[arm]
            end=(mapA[tuple(changed)],mapsB[c,arr])
            # An edge orbit is uniquely determined by B state and chosen arm,
            # not merely its quotient endpoints (parallel edges can occur).
            ed=(c,arr,arm)
            key=min((c,act(arr,g),g[arm]) for g in G)
            edge_orbs.add(key)
    # Every vertex in a connected finite quotient graph contributes to E-V+1.
    v=va+vb;e=len(edge_orbs);beta=e-v+1
    pred=beta_burnside(p,G)
    assert beta==pred, (m,p,name, v,e,beta,pred)
    if name=='trivial':
        known=1+(p*m-2*p-m+1)*factorial(p+m-2)//factorial(m-1)
        assert beta==known
    return {'m':m,'p':p,'group':name,'group_size':len(G),'vertex_orbits':v,'edge_orbits':e,'beta':beta}

if __name__=='__main__':
    cases=[]
    for m,p in [(3,2),(3,3),(3,4),(4,2),(4,3),(4,4),(5,2),(5,3),(5,4)]:
        cyc=tuple((i+1)%m for i in range(m))
        swap=tuple(1 if i==0 else 0 if i==1 else i for i in range(m))
        refl=tuple((-i)%m for i in range(m))
        variants={'trivial':[],'cyclic':[cyc],'dihedral':[cyc,refl],'symmetric':[cyc,swap]}
        if m>=4:
            tri=tuple([1,2,0]+list(range(3,m)))
            variants['alternating']=[cyc,tri] if m%2==1 else [tri,tuple([1,0,3,2]+list(range(4,m)))]
            # For m=4, generators are A4. For m=5, 3-cycle + double swap only A5? actually A5 needs 5-cycle.
            if m==5:variants['alternating']=[cyc,tri]
        for name,gens in variants.items():
            rec=run_case(m,p,gens,name)
            cases.append(rec)
            print(f"m={m} p={p} {name}: |H|={rec['group_size']} V={rec['vertex_orbits']} E={rec['edge_orbits']} beta={rec['beta']}")
    print('ALL_VERIFY_OK cases='+str(len(cases)))
