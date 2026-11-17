"""Exact finite-field checks for threefold convolution on the split torus.

Run: python3 check_hyperbola.py
Only integer arithmetic is used. The general point-count estimate is a theorem,
not an empirical inference from this checker.
"""
from collections import Counter


class Field:
    def __init__(self, p, modulus=None):
        self.p = p
        self.modulus = modulus or [0, 1]
        self.k = len(self.modulus) - 1
        self.q = p ** self.k
        assert self.modulus[-1] == 1
        self.coeff = [self._digits(x) for x in range(self.q)]
        self.mul_table = [[self._mul0(x, y) for y in range(self.q)] for x in range(self.q)]
        self.inv_table = [None] + [self.pow(x, self.q-2) for x in range(1,self.q)]
        for x in range(1,self.q):
            assert self.mul(x, self.inv_table[x]) == 1

    def _digits(self,x):
        v=[]
        for _ in range(self.k):
            v.append(x%self.p)
            x//=self.p
        return v

    def _code(self, ds):
        return sum((x%self.p)*self.p**i for i,x in enumerate(ds))

    def add(self,a,b):
        return self._code([x+y for x,y in zip(self.coeff[a], self.coeff[b])])

    def neg(self,a):
        return self._code([-x for x in self.coeff[a]])

    def sub(self,a,b):
        return self.add(a,self.neg(b))

    def _mul0(self,a,b):
        va=self.coeff[a];vb=self.coeff[b]
        arr=[0]*(2*self.k-1)
        for i,x in enumerate(va):
            for j,y in enumerate(vb): arr[i+j]+=x*y
        for i in range(2*self.k-2,self.k-1,-1):
            c=arr[i]%self.p
            for j in range(self.k):arr[i-self.k+j]-=c*self.modulus[j]
        return self._code(arr[:self.k])

    def mul(self,a,b):return self.mul_table[a][b]

    def pow(self,a,n):
        r=1
        while n:
            if n&1:r=self.mul(r,a)
            a=self.mul(a,a)
            n>>=1
        return r

    def inv(self,a):return self.inv_table[a]

    def val(self,n):return n%self.p

    def chi(self,x):
        return 0 if x==0 else (1 if self.pow(x,(self.q-1)//2)==1 else -1)


def verify(p, modulus=None, expected_diameter=None, missing_products=None):
    F=Field(p,modulus);q=F.q
    add,sub,mul,chi=F.add,F.sub,F.mul,F.chi
    one=1
    S=[(t,F.inv(t)) for t in range(1,q)]
    D2=Counter((add(x,u),add(y,v)) for x,y in S for u,v in S)
    D3=Counter()
    for (a,b),n in D2.items():
        for x,y in S:D3[(add(a,x),add(b,y))]+=n
    assert sum(D2.values())==(q-1)**2
    assert sum(D3.values())==(q-1)**3
    def poly(c,t):
        f1=sub(one,t)
        qt=sub(sub(mul(sub(c,F.val(3)),t),mul(c,mul(t,t))),one)
        f2=sub(mul(c,t),one)
        return mul(mul(f1,qt),f2)
    def r3_from_formula(a,b):
        if a==b==0:return (q-1)*(1+chi(F.neg(F.val(3))))
        if a==0 or b==0:return q-3-chi(F.neg(F.val(3)))
        c=mul(a,b)
        if c==one:return 3*q-6
        sigma=sum(chi(poly(c,t)) for t in range(q))
        ans=q-4+sigma
        if c!=F.val(9):
            assert abs(sigma+1)<=2*q**0.5+1e-8  # Weil estimate, sample sanity only
            assert ans+6==q+2+sigma
        else:
            assert ans==q-5-chi(F.neg(F.val(3)))
        return ans
    for a in range(q):
        for b in range(q):
            assert D3[(a,b)] == r3_from_formula(a,b), (q,a,b,D3[(a,b)],r3_from_formula(a,b))
    # Independently verify twofold convolutions, including axial restrictions.
    for a in range(q):
        for b in range(q):
            if a==b==0: n=q-1
            elif a==0 or b==0: n=0
            else:
                c=mul(a,b)
                disc=sub(one,mul(F.val(4),F.inv(c)))
                n=1+chi(disc)
            assert D2[(a,b)]==n,(q,a,b,D2[(a,b)],n)
    visited={(0,0)};layer={(0,0)};diameter=None
    for step in range(1,7):
        layer={(add(a,x),add(b,y)) for a,b in layer for x,y in S}
        visited|=layer
        if len(visited)==q*q:
            diameter=step;break
    if expected_diameter is None:assert diameter is None,(q,diameter)
    else:assert diameter==expected_diameter,(q,diameter,expected_diameter)
    zeros={c for c in range(1,q) if D3[(1,c)]==0}
    if missing_products is not None:assert zeros==set(missing_products),(q,zeros,missing_products)
    result={'q':q,'diameter':diameter,'nonzero_target_missing_products':sorted(zeros),'origin_3steps':D3[(0,0)],'axis_nonzero_3steps':D3[(0,1)],'three_step_support':len(D3)}
    print(result)
    return result


def main():
    for p,mod,diam,zero in [
       (3,None,None,{2}),
       (5,None,4,{2,3}),
       (7,None,4,{5,6}),
       (3,[1,0,1],4,{4,7}),
       (11,None,3,{6}),
       (13,None,3,set()),
       (17,None,3,set()),
       (19,None,3,set()),
       (5,[3,0,1],3,set()),  # u^2=2 mod 5
       (3,[2,2,0,1],3,set()),  # u^3=u+1 mod 3
    ]:
        verify(p,mod,diam,zero)
    # q=3: S={(1,1),(-1,-1)} lies in the proper diagonal subgroup.
    F=Field(3)
    assert {(t,F.inv(t)) for t in range(1,3)}=={(1,1),(2,2)}
    print('SPLIT_HYPERBOLA_THREE_STEP_CHECKS_PASS')


if __name__=='__main__':main()
