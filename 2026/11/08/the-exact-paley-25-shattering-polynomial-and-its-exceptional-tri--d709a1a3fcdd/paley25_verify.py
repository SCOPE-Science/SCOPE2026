#!/usr/bin/env python3
"""Exact arithmetic check of open-neighborhood VC shattering for the first Paley fields.
The field F_25 is F_5[t]/(t^2-2), x=a+5*b represents a+b*t.
No external dependencies required. """
from itertools import combinations
from math import comb

class Field:
    def __init__(self,p,quadratic=False):
        self.p=p;self.quadratic=quadratic;self.q=p*p if quadratic else p
        self.c=2 if quadratic else None
        if quadratic:
            assert pow(self.c,(p-1)//2,p)==p-1
        self.residues={self.mul(x,x) for x in range(1,self.q)}
        assert len(self.residues)==(self.q-1)//2
    def add(self,x,y):
        if not self.quadratic:return (x+y)%self.p
        p=self.p;return (x%p+y%p)%p + p*((x//p+y//p)%p)
    def sub(self,x,y):
        if not self.quadratic:return (x-y)%self.p
        p=self.p;return (x%p-y%p)%p + p*((x//p-y//p)%p)
    def mul(self,x,y):
        if not self.quadratic:return x*y%self.p
        p=self.p;c=self.c
        a,b=x%p,x//p;d,e=y%p,y//p
        return (a*d+c*b*e)%p+p*((a*e+b*d)%p)
    def frobenius(self,x):
        if not self.quadratic:return x
        return x%self.p + self.p*((-(x//self.p))%self.p)
    def adjacency(self,u,v):return self.sub(u,v) in self.residues

def trace_mask(field, support, y):
    return sum(1<<i for i,x in enumerate(support) if field.adjacency(x,y))

def shattered_direct(field,support):
    return len({trace_mask(field,support,y) for y in range(field.q)})==(1<<len(support))

def get_masks(field):
    return [sum(1<<y for y in range(field.q) if field.adjacency(x,y)) for x in range(field.q)]

def shattered_bitset(field,masks,support):
    traces=[(1<<field.q)-1]
    for s in support:
        n=masks[s]
        traces=[v & ~n for v in traces]+[v & n for v in traces]
        if not all(traces):return False
    return all(traces)

def profile(field):
    masks=get_masks(field)
    counts=[1]; failures={}; shattered={}
    for k in range(1,5):
        ngood=0
        miss=[]; good=[]
        # translation automorphisms let us pin one support vertex at 0.
        for t in combinations(range(1,field.q),k-1):
            s=(0,)+t
            b=shattered_bitset(field,masks,s)
            d=shattered_direct(field,s)
            assert b==d, ('independent-check disagree',field.q,s)
            (good if b else miss).append(s)
            ngood+=b
        assert (ngood*field.q)%k==0
        counts.append(ngood*field.q//k)
        shattered[k]=good
        failures[k]=miss
    return counts,shattered,failures

def orbit_partition(field, supports, k):
    good=set(supports)
    sq=field.residues
    orbits=[]
    while good:
        s=min(good)
        orbit={tuple(sorted(field.add(field.mul(a,field.frobenius(x) if f else x),b) for x in s))
               for f in (False,True) for a in sq for b in range(field.q)}
        assert orbit <= good, ('orbit invariance error',s,next(iter(orbit-good),None))
        orbits.append((s,len(orbit)))
        good-=orbit
    assert sum(t for s,t in orbits)==len(supports)
    return orbits

def run():
    fields=[Field(5),Field(3,True),Field(13),Field(17),Field(5,True)]
    results=[]
    for f in fields:
        counts,good,miss=profile(f)
        print('q',f.q, 'profile',counts, 'VCdim', max(i for i,c in enumerate(counts) if c))
        results.append((f.q,counts))
        if f.q==25:
            assert counts==[1,25,300,2200,3600]
            # Check every 4-subset directly, not relying on translation reduction.
            full_four={s for s in combinations(range(f.q),4) if shattered_direct(f,s)}
            assert len(full_four)==3600
            good_orbits=orbit_partition(f,full_four,4)
            print('q25 four-support orbits:',good_orbits)
            missing_three={s for s in combinations(range(f.q),3) if not shattered_direct(f,s)}
            assert len(missing_three)==comb(25,3)-2200==100
            # The only missing triples are equilateral triangles for the
            # quadratic-root lambda of lambda^2-lambda+1=0, with square side.
            roots=[z for z in range(25) if f.add(f.sub(f.mul(z,z),z),1)==0]
            assert roots==[13,18]
            equilateral={tuple(sorted((u,f.add(u,d),f.add(u,f.mul(d,z)))))
                         for u in range(25) for d in f.residues for z in roots}
            assert len(equilateral)==100 and equilateral==missing_three
            print('q25 missing triples = square-equilateral',len(equilateral),'roots',roots)
            print('q25 unshattered 3-support orbits:',orbit_partition(f,missing_three,3))
            s=(0,2,5,10)
            assert shattered_direct(f,s)
            witness={mask:next(y for y in range(f.q) if trace_mask(f,s,y)==mask) for mask in range(16)}
            print('witness 4-support',s,'centres',witness)
    assert results==[(5,[1,5,5,0,0]),(9,[1,9,36,0,0]),(13,[1,13,78,182,0]),(17,[1,17,136,612,0]),(25,[1,25,300,2200,3600])]
    print('PALEY25_SHATTERING_PASS',results)
if __name__=='__main__':run()
