#!/usr/bin/env python3
"""Independent finite enumeration of right-Engel word fibers in affine groups.
No external packages are required. Execute: python3 verify.py
"""
from collections import Counter
from itertools import product

class Ring:
    def __init__(self, q, m, model):
        self.q, self.m, self.model = q, m, model
        self.p = 2 if q == 4 else q
        self.N = q**m
        self.elements = range(self.N)
        if model == 'cyclic':
            self.add = lambda a, b: (a+b) % self.N
            self.neg = lambda a: (-a) % self.N
            self.mul = lambda a, b: (a*b) % self.N
        else:
            def fadd(a,b):
                return a ^ b if q == 4 else (a+b)%q
            def fneg(a):
                return a if q == 4 else (-a)%q
            def fmul(a,b):
                if q != 4: return a*b%q
                # F_4 = F_2[z]/(z^2+z+1).
                result = 0
                for i in range(2):
                    for j in range(2):
                        if (a>>i)&1 and (b>>j)&1:
                            result ^= [1,2,3][i+j]
                return result
            def digits(a):
                z=[]
                for _ in range(m): z.append(a%q); a//=q
                return z
            def enc(ds):return sum(d*q**i for i,d in enumerate(ds))
            self.add = lambda a,b: enc([fadd(x,y) for x,y in zip(digits(a),digits(b))])
            self.neg = lambda a: enc([fneg(x) for x in digits(a)])
            def mul(a,b):
                x=digits(a);y=digits(b);z=[0]*m
                for i in range(m):
                    for j in range(m-i): z[i+j]=fadd(z[i+j],fmul(x[i],y[j]))
                return enc(z)
            self.mul=mul
        self.one=1
        self.unit_inv={a:next((b for b in self.elements if self.mul(a,b)==1),None) for a in self.elements}
        self.units=[a for a in self.elements if self.unit_inv[a] is not None]
        self.pi=self.p if model=='cyclic' else q
        self.powers=[self.pi**j if model=='cyclic' else q**j for j in range(m)]
    def val(self,a):
        if a == 0:return self.m
        if self.model=='cyclic':
            r=0
            while a%self.p==0:r+=1;a//=self.p
            return r
        r=0
        while a%self.q==0:r+=1;a//=self.q
        return r


def audit(q,m,model):
    R=Ring(q,m,model)
    assert len(R.units)==(q-1)*q**(m-1)
    cm=Counter(R.val(R.add(u,R.neg(1))) for u in R.units)
    assert cm[0]==(q-2)*q**(m-1)
    assert cm[m]==1
    for j in range(1,m):assert cm[j]==(q-1)*q**(m-j-1)
    # independent direct group operations
    def times(g,h):
        b,u=g; d,v=h
        return (R.add(b,R.mul(u,d)),R.mul(u,v))
    def inverse(g):
        b,u=g; v=R.unit_inv[u]
        return (R.neg(R.mul(v,b)),v)
    def bracket(g,h):
        return times(times(inverse(g),inverse(h)),times(g,h))
    group=list(product(R.elements,R.units))
    # Evaluate all prescribed translation target fibers.
    K=min(m+2,5)
    actual=[Counter() for _ in range(K)]
    fixed_by_y=[Counter() for _ in range(K)]
    for x in group:
        for y in group:
            z=x
            for k in range(K):
                z=bracket(z,y)
                actual[k][z]+=1
                if z==(0,1): fixed_by_y[k][y]+=1
    for k in range(1,K+1):
        expected={}
        for t in R.elements:
            v=R.val(t); s=0
            for i in range(m+1):
                for j in range(m+1):
                    rho=min(m,(k-1)*i+min(i,j))
                    if v>=rho:s+=cm[i]*cm[j]*q**(m+rho)
            expected[(t,1)]=s
        assert set(actual[k-1]).issubset(set(expected)),(q,m,model,k,'nontranslation')
        for out,n in expected.items():
            assert actual[k-1][out]==n,(q,m,model,k,out,actual[k-1][out],n)
        assert sum(expected.values())==len(group)**2,(q,m,model,k,'mass')
        for (b,v) in group:
            i=R.val(R.add(v,R.neg(1)))
            h=R.val(b)
            s=min(m,(k-1)*i)
            d=min(m,k*i)
            threshold=max(0,min(i,m-s)-h)
            H=len(R.units) if threshold==0 else q**(m-threshold)
            predicted=q**d*H
            assert fixed_by_y[k-1][(b,v)]==predicted, (q,m,model,k,(b,v),'eng',fixed_by_y[k-1][(b,v)],predicted)
        support={R.val(out[0]) for out,count in actual[k-1].items() if count>0}
        if q==2:
            assert min(support)==min(k,m)
        else:
            assert 0 in support
        if k >= m+1:
            expected_zero=len(group)**2*(1/(q-1)+(q-2)/((q-1)*q**m))
            assert abs(actual[k-1][(0,1)]-expected_zero)<1e-6
    if q==2 and K>=m:
        assert len(actual[m-1])==1
    if q>2 and K>=m+1:
        assert actual[m]==actual[m+1] if K>=m+2 else True
    if q>2 and m>=2 and K>=m+1:
        p_nonzero_delta=sum(actual[m-1][(t,1)]-actual[m][(t,1)] for t in R.elements if t)
        assert p_nonzero_delta*q*q==(q-2)*len(group)**2,(q,m,model,'sharp jump')
    print('PASS',f'R={model}({q},{m})',f'|G|={len(group)}',f'depths=1..{K}',f'pairs={len(group)**2}')

if __name__=='__main__':
    for q,m,model in [(2,1,'poly'),(2,2,'poly'),(2,3,'poly'),(2,4,'poly'),
                      (2,2,'cyclic'),(2,3,'cyclic'),(2,4,'cyclic'),
                      (3,1,'poly'),(3,2,'poly'),(3,3,'poly'),
                      (3,2,'cyclic'),(3,3,'cyclic'),(4,1,'poly'),(4,2,'poly'),
                      (5,1,'poly'),(5,2,'cyclic')]:
        audit(q,m,model)
    print('VERIFY_OK')
