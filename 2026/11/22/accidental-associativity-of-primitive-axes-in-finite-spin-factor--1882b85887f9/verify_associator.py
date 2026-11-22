"""Independent finite-field tests for primitive spin-factor associator counts.

Run: python3 spin_idempotent_associator_verify.py
Only standard-library Python is required. No external data are used.
"""
from itertools import product

class Field:
    def __init__(self, q):
        assert q in (3, 5, 7, 9)
        self.q = q
        self.p = 3 if q == 9 else q
        self.els = list(range(q))
        if q == 9:
            self.add = lambda a, b: ((a % 3 + b % 3) % 3) + 3 * ((a // 3 + b // 3) % 3)
            self.neg = lambda a: (-(a % 3) % 3) + 3 * (-(a // 3) % 3)
            self.mul = lambda a, b: (((a % 3)*(b % 3) - (a // 3)*(b // 3)) % 3) + 3 * (((a % 3)*(b // 3)+(a // 3)*(b % 3)) % 3)
            self.nonsquare = 4  # 1+t, t^2=-1, has multiplicative order eight
        else:
            self.add = lambda a,b: (a+b)%q
            self.neg = lambda a: (-a)%q
            self.mul = lambda a,b: (a*b)%q
            self.nonsquare = next(a for a in range(2,q) if a not in {(x*x)%q for x in range(1,q)})
        self.half = next(a for a in self.els if self.add(a,a) == 1)
    def chi(self, a):
        if a == 0: return 0
        return 1 if a in {self.mul(x,x) for x in self.els if x != 0} else -1


def dot(F, x, y, diag):
    result = 0
    for a,b,c in zip(x,y,diag):
        result = F.add(result, F.mul(c,F.mul(a,b)))
    return result


def mul_J(F, x, y, diag):
    a,u=x; b,v=y
    scalar=F.add(F.mul(a,b),dot(F,u,v,diag))
    out=tuple(F.add(F.mul(a,w),F.mul(b,t)) for w,t in zip(v,u))
    return (scalar,out)


def is_zero_associator(F,u,v,w,diag):
    e=lambda t:(F.half,tuple(F.mul(F.half,x) for x in t))
    x,y,z=e(u),e(v),e(w)
    left=mul_J(F,mul_J(F,x,y,diag),z,diag)
    right=mul_J(F,x,mul_J(F,y,z,diag),diag)
    return left==right


def predicted(F,d,diag):
    # The quadratic representation count over an odd finite field.
    determinant=1
    for x in diag: determinant=F.mul(determinant,x)
    minus_one=F.neg(1)
    def count_norm_one(n,det):
        sign=F.chi(F.mul(pow_field(F, minus_one, n//2), det))
        if n%2 == 0:
            return F.q**(n-1)-sign*F.q**(n//2-1)
        return F.q**(n-1)+sign*F.q**((n-1)//2)
    S=count_norm_one(d,determinant)
    T=count_norm_one(d-1,determinant)
    return S,T,S*(T*T+2*S-2*T),S*(T*T-2*T)


def pow_field(F,a,k):
    r=1
    for _ in range(k):r=F.mul(r,a)
    return r


def run(q,d,twist,full):
    F=Field(q)
    diag=(1,)*(d-1)+(F.nonsquare if twist else 1,)
    sphere=[v for v in product(F.els, repeat=d) if dot(F,v,v,diag)==1]
    S,T,expect,nontrivial=predicted(F,d,diag)
    assert len(sphere)==S,(q,d,twist,'S',len(sphere),S)
    middle=sphere if full else sphere[:min(4,len(sphere))]
    total=0
    for v in middle:
        got=0
        perpendicular=sum(dot(F,u,v,diag)==0 for u in sphere)
        assert perpendicular==T,(q,d,twist,'T',perpendicular,T)
        for u in sphere:
            for w in sphere:
                got+=is_zero_associator(F,u,v,w,diag)
        assert got==T*T+2*(S-T),(q,d,twist,'one-middle',got,T*T+2*(S-T))
        total+=got
    if full:
        assert total==expect,(q,d,twist,'total',total,expect)
    return f'q={q} d={d} twist={int(twist)} full={int(full)} S={S} T={T} total={expect} independent_outer={nontrivial}: PASS'


if __name__=='__main__':
    rows=[]
    for q in (3,5,9):
        for d in (2,3,4,5):
            if q == 9 and d>3: continue
            if q == 5 and d>4: continue
            for twist in (False,True):
                full=(q==3 and d<=5) or (q==5 and d<=3) or (q==9 and d==2)
                rows.append(run(q,d,twist,full))
    print('\n'.join(rows))
    print('VERIFY_OK',len(rows),'configurations')
