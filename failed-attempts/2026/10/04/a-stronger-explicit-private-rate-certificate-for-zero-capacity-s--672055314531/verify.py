from fractions import Fraction as F

N=48

def ln_pos(x):
    # rigorous interval for ln(x), x>0 rational
    assert x>0
    if x == 1:
        return F(0),F(0)
    if x < 1:
        lo,hi=ln_pos(1/x)
        return -hi,-lo
    # reduce x = 2^k y, y in [1,2)
    k=0
    y=x
    while y>=2:
        y/=2; k+=1
    while y<1:
        y*=2; k-=1
    def ln_unit(y):
        z=(y-1)/(y+1)
        s=F(0)
        zz=z
        for n in range(N+1):
            s += zz/F(2*n+1)
            zz *= z*z
        lo=2*s
        # first omitted exponent 2N+3
        tail = 2*zz/F(2*N+3)/(1-z*z)
        return lo, lo+tail
    l2lo,l2hi=ln_unit(F(2))
    ylo,yhi=ln_unit(y)
    if k>=0:
        return ylo+k*l2lo, yhi+k*l2hi
    else:
        return ylo+k*l2hi, yhi+k*l2lo

def h2_interval(x):
    assert F(0)<=x<=F(1)
    if x in (0,1): return F(0),F(0)
    lxlo,lxhi=ln_pos(x)
    lylo,lyhi=ln_pos(1-x)
    # numerator -x ln x -(1-x)ln(1-x)
    nlo= -x*lxhi -(1-x)*lyhi
    nhi= -x*lxlo -(1-x)*lylo
    l2lo,l2hi=ln_pos(F(2))
    return nlo/l2hi, nhi/l2lo

def J_upper(c,q,t):
    r0=1/c
    rt=(1+(c-1)*t)/c
    rb=(1+(c-1)*q*t)/c
    rb_lo,rb_hi=h2_interval(rb)
    r0_lo,r0_hi=h2_interval(r0)
    rt_lo,rt_hi=h2_interval(rt)
    return rb_hi-(1-q)*r0_lo-q*rt_lo

def bob_lower(p,q,t):
    a=(1-p)/7
    s=a*t
    hqs_lo,hqs_hi=h2_interval(q*s)
    hs_lo,hs_hi=h2_interval(s)
    return hqs_lo-q*hs_hi

p=F(1,2); q=F(39,200); t=F(4,299)
b=bob_lower(p,q,t)
e=p*J_upper(F(205,9),q,t)+(1-p)*J_upper(F(4),q,t)
r=b-e
target=F(2101,10_000_000) # 0.0002101
published=None
# interval for 3 ln2/10927
l2lo,l2hi=ln_pos(F(2))
published_hi=3*l2hi/F(10927)
print('bob_lower', float(b))
print('eve_upper', float(e))
print('rate_lower', float(r))
print('target', float(target))
print('published_upper', float(published_hi))
print('improvement_factor_lower', float(r/published_hi))
assert t <= F(1,2)
assert r > target
assert r*F(10,1) > published_hi*F(11,1)  # >10% improvement
print('VERIFY_OK')
