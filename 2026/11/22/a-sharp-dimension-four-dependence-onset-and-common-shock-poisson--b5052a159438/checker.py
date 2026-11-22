"""Exact independent finite checks for randomly oriented Boolean cubes.
No random sampling: enumerates all orientations for d<=3 and constraint pairs up to d=8.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product

def graph(d):
    verts=range(1<<d)
    edges=[(v,v^(1<<k)) for v in verts for k in range(d) if v<(v^(1<<k))]
    return edges

def requirements(d,v,facet_bit):
    assert v&(1<<facet_bit)==0
    # directed edges coded (min, max), required arrow into v
    out={}
    for k in range(d):
        if k==facet_bit: continue
        w=v^(1<<k)
        e=tuple(sorted((v,w)))
        out[e]=v
    return out

def compatible_probability(a,b):
    for e,tip in a.items():
        if e in b and b[e]!=tip: return F(0)
    return F(1, 2**len(set(a)|set(b)))

def pair_moments(d):
    A=[v for v in range(1<<d) if not v&1]
    B=[v for v in range(1<<d) if not v&2]
    ra={v:requirements(d,v,0) for v in A}
    rb={w:requirements(d,w,1) for w in B}
    ea=sum((compatible_probability(x,{}) for x in ra.values()),F(0))
    eb=sum((compatible_probability(x,{}) for x in rb.values()),F(0))
    eab=sum((compatible_probability(x,y) for x in ra.values() for y in rb.values()),F(0))
    return ea,eb,eab, eab-ea*eb

def exhaustive(d):
    ed=graph(d)
    A=[v for v in range(1<<d) if not v&1]
    B=[v for v in range(1<<d) if not v&2]
    reqA={v:requirements(d,v,0) for v in A}
    reqB={v:requirements(d,v,1) for v in B}
    idx={e:i for i,e in enumerate(ed)}
    def sink(v, req, mask):
        return all((mask>>idx[e])&1 == (v==e[1]) for e in req)
    counts=Counter()
    for mask in range(1<<len(ed)):
        a=sum(sink(v,r,mask) for v,r in reqA.items())
        b=sum(sink(v,r,mask) for v,r in reqB.items())
        counts[(a,b)]+=1
    N=1<<len(ed)
    p={(a,b):F(count,N) for (a,b),count in counts.items()}
    ma=sum(F(a)*r for (a,b),r in p.items())
    mb=sum(F(b)*r for (a,b),r in p.items())
    cov=sum((F(a*b)*r for (a,b),r in p.items()),F(0))-ma*mb
    pmA={a:sum((r for (x,b),r in p.items() if x==a),F(0)) for a in range(1<<d)}
    pmB={b:sum((r for (a,y),r in p.items() if y==b),F(0)) for b in range(1<<d)}
    indep=all(r==pmA[a]*pmB[b] for (a,b),r in p.items()) and all(pmA.get(a,0)*pmB.get(b,0)==p.get((a,b),F(0)) for a in pmA for b in pmB)
    assert ma==mb==1 and cov == F(1,4)-F(d-1,2**d)
    assert cov==pair_moments(d)[3]
    print('exhaustive',d,'orientations',N,'distribution',dict(sorted(p.items())),'independent',indep,'cov',cov)

if __name__=='__main__':
    for d in [2,3]: exhaustive(d)
    for d in range(2,9):
        ea,eb,eab,cov=pair_moments(d)
        assert ea==eb==1
        assert cov == F(1,4)-F(d-1,2**d), (d,cov)
        expected_var=1-F(d,2**(d-1))
        print('pairs',d,'mean',ea, 'EAB',eab,'cov',cov, 'Var each',expected_var)
    print('PASS: 2 complete enumerations and 7 independent pairwise-probability formulas')

# The marked-atom probability comparison is logically separate from enumeration.
def atom_requirements(d):
    atoms=[]
    for v in range(1<<d):
        inA=not(v&1); inB=not(v&2)
        if inA and inB:
            shared=[k for k in range(2,d)]
            for mark,extra in (
                ('C', ((0,True),(1,True))),
                ('A', ((0,False),(1,True))),
                ('B', ((0,True),(1,False))),
            ):
                r={}
                for k in shared:
                    w=v^(1<<k);r[tuple(sorted((v,w)))]=v
                for k,towards in extra:
                    w=v^(1<<k);r[tuple(sorted((v,w)))]=v if towards else w
                atoms.append((v,mark,r))
        elif inA:
            atoms.append((v,'A',requirements(d,v,0)))
        elif inB:
            atoms.append((v,'B',requirements(d,v,1)))
    return atoms

def check_atoms(d):
    atoms=atom_requirements(d)
    masses={'A':F(0),'B':F(0),'C':F(0)}
    for v,m,r in atoms: masses[m]+=F(1,2**len(r))
    assert masses == {'A':F(3,4),'B':F(3,4),'C':F(1,4)}
    p=[F(1,2**len(r)) for _,_,r in atoms]
    b1=b2=F(0)
    for i,(v,m,r) in enumerate(atoms):
        for j,(w,n,s) in enumerate(atoms):
            if v!=w and (v^w).bit_count()!=1: continue
            b1+=p[i]*p[j]
            if i!=j:
                joint=compatible_probability(r,s)
                assert joint<=2*p[i]*p[j], (d,i,j,joint,p[i],p[j])
                b2+=joint
    assert b1<=F(21,2)*(d+1)*F(1,2**d)
    assert b2<=2*b1
    print('atoms',d,'count',len(atoms),'means',masses,'b1',b1,'b2',b2)

if __name__=='__main__':
    for d in range(2,8): check_atoms(d)
    print('PASS: six exact marked-dependence neighborhood validations')
