#!/usr/bin/env python3
"""Exact finite-field cross-checks for quadratic Fourier zeros on two-dimensional prime-field planes."""
from collections import Counter
from math import cos, sin, pi

class FiniteField:
    def __init__(self, p, poly):
        self.p=p;self.poly=list(poly);self.m=len(poly)-1;self.q=p**self.m
        assert poly[-1]==1
        self.digits=[]
        for x in range(self.q):
            y=x;d=[]
            for _ in range(self.m):d.append(y%p);y//=p
            self.digits.append(d)
        self.add=[[self.enc([(a+b)%p for a,b in zip(self.digits[x],self.digits[y])]) for y in range(self.q)] for x in range(self.q)]
        self.mul=[[self._mul(x,y) for y in range(self.q)] for x in range(self.q)]
        self.powp=[]
        for x in range(self.q):
            xp=x; ex=[]
            for i in range(self.m):
                ex.append(xp);xp=self.power(xp,p)
            self.powp.append(ex)
        self.trace=[]
        for x in range(self.q):
            s=0
            for t in self.powp[x]:s=self.add[s][t]
            assert all(z==0 for z in self.digits[s][1:]), (x,s)
            self.trace.append(self.digits[s][0])
        # Validate the displayed polynomial quotient really is a field.
        assert all(self.power(x,self.q-1)==1 for x in range(1,self.q))
        self.one=1
    def enc(self,d):return sum(int(z)*self.p**i for i,z in enumerate(d))
    def _mul(self,x,y):
        p=self.p;m=self.m;prod=[0]*(2*m-1)
        for i,a in enumerate(self.digits[x]):
            for j,b in enumerate(self.digits[y]):prod[i+j]=(prod[i+j]+a*b)%p
        for k in range(2*m-2,m-1,-1):
            c=prod[k]
            for j in range(m):prod[k-m+j]=(prod[k-m+j]-c*self.poly[j])%p
        return self.enc(prod[:m])
    def power(self,x,k):
        s=1
        while k:
            if k&1:s=self.mul[s][x]
            x=self.mul[x][x];k//=2
        return s
    def span(self,u,v):
        return sorted({self.add[self.mul[u][a]][self.mul[v][b]] for a in range(self.p) for b in range(self.p)})
    def rank_for_a(self,a,u,v):
        tr=self.trace;mul=self.mul;p=self.p
        A=tr[mul[a][mul[u][u]]]
        B=tr[mul[a][mul[u][v]]]
        C=tr[mul[a][mul[v][v]]]
        if A==B==C==0:return 0
        if (A*C-B*B)%p==0:return 1
        return 2
    def exact_zero_histogram(self,u,v):
        H=self.span(u,v);p=self.p;q=self.q;tr=self.trace;add=self.add;mul=self.mul
        assert len(H)==p*p
        XX=[mul[x][x] for x in H]
        counts=Counter()
        squared=Counter()
        roots=[complex(cos(2*pi*k/p),sin(2*pi*k/p)) for k in range(p)]
        for a in range(q):
            aXX=[mul[a][xx] for xx in XX]
            for b in range(q):
                bins=[0]*p
                for x,ax in zip(H,aXX):
                    phase=tr[add[ax][mul[b][x]]]
                    bins[phase]+=1
                z=sum(count*root for count,root in zip(bins,roots))
                sq=int(round(abs(z)**2))
                assert abs(abs(z)**2-sq)<1e-6,(a,b,z,sq)
                squared[sq]+=1
                if len(set(bins))==1:
                    assert sq==0
                    counts[a]+=1
                else:assert sq>0
        return Counter(counts.get(a,0) for a in range(q)), sum(counts.values()), squared

def test(p,poly,generic=True,special=False):
    F=FiniteField(p,poly);q=F.q;m=F.m
    candidates=[]
    for v in range(q):
        if v not in range(p) and v!=0:
            istwo=F.power(v,p*p)==v
            if istwo==special:
                candidates.append(v)
    if not candidates:return None
    v=candidates[0]
    actual_ranks=Counter(F.rank_for_a(a,1,v) for a in range(q))
    observed,zeros,hist=F.exact_zero_histogram(1,v)
    if special:
        expected_ranks={0:q//p**2,2:q-q//p**2}
        expected_profile={q-q//p**2:q//p**2,0:q-q//p**2}
        expected_zeros=q*q*(p*p-1)//p**4
        expected_hist={0:expected_zeros, p*p:q*q*(1-1/p**2),p**4:q*q//p**4}
    else:
        expected_ranks={0:q//p**3,1:q*(p*p-1)//p**3,2:q*(p**3-p*p)//p**3}
        expected_profile={q-q//p**2:q//p**3,q-q//p:q*(p*p-1)//p**3,0:q*(p**3-p*p)//p**3}
        expected_zeros=q*q*(p*p-1)*(p*p-p+1)//p**5
        expected_hist={0:expected_zeros,p*p:q*q*(p-1)//p,p**3:q*q*(p*p-1)//p**4,p**4:q*q//p**5}
    assert dict(actual_ranks)==expected_ranks,(p,m,special,actual_ranks,expected_ranks)
    assert dict(observed)==expected_profile,(p,m,special,observed,expected_profile)
    assert zeros==expected_zeros,(p,m,special,zeros,expected_zeros)
    assert dict(hist)=={k:int(v) for k,v in expected_hist.items()},(p,m,special,hist,expected_hist)
    assert sum(k*v for k,v in hist.items())==q*q*p*p # Exact Parseval.
    print('OK',p,m,'subfield' if special else 'generic', 'q',q,'plane', (1,v),'rank_counts',dict(actual_ranks),'zero_profile',dict(observed),'zeros',zeros,'squared_magnitude_hist',dict(hist))
    return True

def complete_plane_census(p, poly):
    F=FiniteField(p,poly);q=F.q;m=F.m
    planes=set()
    for u in range(1,q):
        line={F.mul[u][z] for z in range(p)}
        for v in range(1,q):
            if v not in line:
                planes.add(tuple(F.span(u,v)))
    total=(q-1)*(q-p)//((p*p-1)*(p*p-p))
    assert len(planes)==total,(p,m,len(planes),total)
    counts=Counter()
    for H in planes:
        u=next(x for x in H if x)
        ui=F.power(u,q-2)
        special=(m%2==0 and all(F.power(F.mul[ui][x],p*p)==F.mul[ui][x] for x in H))
        v=next(x for x in H if x not in {F.mul[u][k] for k in range(p)})
        ranks=Counter(F.rank_for_a(a,u,v) for a in range(q))
        if special:
            assert dict(ranks)=={0:q//(p*p),2:q-q//(p*p)}
        else:
            assert dict(ranks)=={0:q//p**3,1:q*(p*p-1)//p**3,2:q*(p**3-p*p)//p**3}
        counts['special' if special else 'generic']+=1
    expected_special=(q-1)//(p*p-1) if m%2==0 else 0
    assert counts['special']==expected_special,(p,m,counts,expected_special)
    assert counts['generic']==total-expected_special
    print('CENSUS_OK',p,m,'total',total,'generic',counts['generic'],'special',counts['special'])

if __name__=='__main__':
    assert test(3,[1,2,0,1],special=False)
    assert test(5,[1,1,0,1],special=False)
    assert test(3,[2,1,0,0,1],special=False)
    assert test(3,[2,1,0,0,1],special=True)
    complete_plane_census(3,[1,2,0,1])
    complete_plane_census(5,[1,1,0,1])
    complete_plane_census(3,[2,1,0,0,1])
    print('CHECK_OK four exact-field tests; all 174 planes classified')
