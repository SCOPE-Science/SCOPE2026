from fractions import Fraction as F
from math import factorial

# Polynomials are dict degree -> exact rational coefficient.
def add(a,b):
    out=dict(a)
    for k,v in b.items(): out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}

def mul(a,b,maxdeg=20):
    out={}
    for i,x in a.items():
        for j,y in b.items():
            if i+j<=maxdeg: out[i+j]=out.get(i+j,F(0))+x*y
    return {k:v for k,v in out.items() if v}

def scale(a,c): return {k:v*c for k,v in a.items() if v*c}

def shift(a,d): return {k+d:v for k,v in a.items()}

# E[(X+t)^r] for X~N(0,1), as polynomial in t.
def normal_raw_moment(r):
    p={}
    for j in range(r+1):
        # choose j powers from X; odd centered moments vanish
        if j%2: continue
        if j==0: cm=F(1)
        else:
            cm=F(factorial(j), (2**(j//2))*factorial(j//2))
        from math import comb
        p[r-j]=p.get(r-j,F(0))+F(comb(r,j))*cm
    return p

assert normal_raw_moment(2)=={2:F(1),0:F(1)}
assert normal_raw_moment(4)=={4:F(1),2:F(6),0:F(3)}
assert normal_raw_moment(6)=={6:F(1),4:F(15),2:F(45),0:F(15)}
assert normal_raw_moment(8)=={8:F(1),6:F(28),4:F(210),2:F(420),0:F(105)}

# E log cosh(t Z), Z~N(t,1), through degree 8.
logcosh_coeff={2:F(1,2),4:F(-1,12),6:F(1,45),8:F(-17,2520)}
Elog={}
for power,c in logcosh_coeff.items():
    # t^power * E[Z^power]
    Elog=add(Elog, scale(shift(normal_raw_moment(power),power),c))
Elog={k:v for k,v in Elog.items() if k<=8}
expected_Elog={2:F(1,2),4:F(1,4),6:F(-1,6),8:F(5,24)}
assert Elog==expected_Elog, (Elog,expected_Elog)

# a(t)=t^2-E log cosh(tZ)
a=add({2:F(1)},scale(Elog,F(-1)))
expected_a={2:F(1,2),4:F(-1,4),6:F(1,6),8:F(-5,24)}
assert a==expected_a, (a,expected_a)

# q(t)=t E[Z]-t^2 E[Z^2]/2, exactly.
q={2:F(1,2),4:F(-1,2)}

# Check reciprocal Laurent series by shifting t^2 a^{-1} into ordinary polynomial.
# Candidate inv_a=2 t^-2 +1-t^2/6+5t^4/12.
inv_a_shifted={0:F(2),2:F(1),4:F(-1,6),6:F(5,12)}  # t^2 * inv_a
# a * inv_a = (a/t^2)*(t^2 inv_a).
a_over={k-2:v for k,v in a.items()}
prod_a=mul(a_over,inv_a_shifted,maxdeg=6)
assert prod_a.get(0)==1
assert prod_a.get(2,F(0))==0
assert prod_a.get(4,F(0))==0
assert prod_a.get(6,F(0))==0

inv_q_shifted={0:F(2),2:F(2),4:F(2),6:F(2)}
q_over={k-2:v for k,v in q.items()}
prod_q=mul(q_over,inv_q_shifted,maxdeg=6)
assert prod_q.get(0)==1
assert prod_q.get(2,F(0))==0
assert prod_q.get(4,F(0))==0
assert prod_q.get(6,F(0))==0

# Difference inv_q - inv_a through t^4.
# Laurent t^-2 coefficients cancel.
assert F(2)-F(1)==F(1)
assert F(2)-F(-1,6)==F(13,6)
assert F(2)-F(5,12)==F(19,12)

print('VERIFY_OK')
