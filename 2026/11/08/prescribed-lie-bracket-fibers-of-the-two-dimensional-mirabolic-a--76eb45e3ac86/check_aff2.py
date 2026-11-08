"""Direct finite-field checking of affine-plane Lie bracket fiber formulas.
Public mathematical reproducer; Python standard library only.
"""
from itertools import product
from collections import Counter

def predicted(q,Z,w):
    z00,z01,z10,z11=Z
    if (z00+z11)%q: return 0
    zero=not any(Z)
    if zero:
        return q**8+2*q**7+q**6-3*q**5-q**4+q**3 if w==(0,0) else q**3*(q*q-1)*(q**3+q**2+q-1)
    det=(z00*z11-z01*z10)%q
    if det!=0:
        return q**5*(q*q-1)
    # For rank-one nilpotent Z, image(Z) is one line: image of a nonzero column.
    col = (z00,z10) if (z00,z10)!=(0,0) else (z01,z11)
    on_line=(col[0]*w[1]-col[1]*w[0])%q == 0
    if on_line:
        return q**3*(q*q-1)*(q*q+q-1)
    return q**3*(q*q-1)*(q*q-1)

def direct(q):
    assert q in (2,3)
    all6=list(product(range(q),repeat=6))
    count=Counter()
    for a,b,c,d,u,v in all6:
        for e,f,g,h,s,t in all6:
            Z=((b*g-f*c)%q,(f*(a-d)+b*(h-e))%q,(c*(e-h)+g*(d-a))%q,(c*f-g*b)%q)
            w=((a*s+b*t-e*u-f*v)%q,(c*s+d*t-g*u-h*v)%q)
            count[Z,w]+=1
    counts=Counter()
    for Z in product(range(q),repeat=4):
        for w in product(range(q),repeat=2):
            actual=count.get((Z,w),0)
            expected=predicted(q,Z,w)
            if actual!=expected:
                raise AssertionError((q,Z,w,actual,expected))
            if expected: counts[expected]+=1
    assert sum(count.values())==q**12
    assert sum(k*v for k,v in counts.items())==q**12
    print(f'q={q}: examined {q**12} ordered pairs, {len(count)} nonempty targets, size-class distribution {sorted(counts.items())}')

if __name__=='__main__':
    direct(2); direct(3)
    print('AFF2_FULL_BRACKET_FIBERS_PASS')
