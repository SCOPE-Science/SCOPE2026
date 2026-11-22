"""Exact checks of the three-regime stationary-load example (standard library only)."""
from fractions import Fraction as F
from math import sqrt

def add(a,b):
    c=[F(0)]*max(len(a),len(b))
    for i,v in enumerate(a):c[i]+=v
    for i,v in enumerate(b):c[i]+=v
    return trim(c)
def neg(a):return [-z for z in a]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)
def trim(a):
    while len(a)>1 and not a[-1]:a.pop()
    return a
def det(a):
    return add(sub(mul(a[0][0],sub(mul(a[1][1],a[2][2]),mul(a[1][2],a[2][1]))),mul(a[0][1],sub(mul(a[1][0],a[2][2]),mul(a[1][2],a[2][0])))),mul(a[0][2],sub(mul(a[1][0],a[2][1]),mul(a[1][1],a[2][0]))))
def deriv(a):return [F(i)*a[i] for i in range(1,len(a))] or [F(0)]
def evalp(a,x):
    r=F(0)
    for z in a[::-1]:r=r*x+z
    return r

def example():
    # Flows/loss q=(1,10,100), pollutant loading u=(1,40,50);
    # environmental transitions i<->i+1 at rate k, all 3 equally likely.
    k=[F(0),F(1)];z=[F(0)]
    M=[[[F(1),F(1)],neg(k),z], [neg(k),[F(10),F(2)],neg(k)], [z,neg(k),[F(100),F(1)]]]
    rhs=[[F(1,3)],[F(40,3)],[F(50,3)]]
    den=det(M)
    num=[F(0)]
    for j in range(3):
        mm=[[M[r][c] if c!=j else rhs[r] for c in range(3)] for r in range(3)]
        num=add(num,det(mm))
    assert den==[F(1000),F(1210),F(111)], (den, 'den')
    assert num==[F(5500,3),F(9040,3),F(273,3)], (num, 'num')
    dnum=sub(mul(deriv(num),den),mul(num,deriv(den)))
    # C' = -30(7479 k^2 +7500 k -26500) /[(k+10)^2(111k+100)^2]
    assert dnum == [F(795000),F(-225000),F(-224370)],dnum
    # The derivative is dnum/den^2, with a strictly positive denominator.
    for x in [F(0), F(1,10),F(1,2),F(1),F(2),F(3),F(10),F(100)]:
        assert evalp(dnum,x)==-F(30)*(F(7479)*x*x+F(7500)*x-F(26500))
        assert evalp(den,x)>0
        assert evalp(num,x)>0
    c0=num[0]/den[0]
    assert c0==F(11,6)
    cfast=num[-1]/den[-1]
    assert cfast==F(91,111)
    a,b,c=7479,7500,-26500
    star=(-b+sqrt(b*b-4*a*c))/(2*a)
    assert 1.4<star<1.5
    C=lambda t:float(evalp(num,F(t))/evalp(den,F(t))) if isinstance(t,int) else (273*t*t+9040*t+5500)/(3*(t+10)*(111*t+100))
    crest=C(star)
    assert crest>float(c0)*1.16
    assert crest>float(cfast)
    assert C(0)<C(1)<crest and crest>C(2)>C(10)>C(100)
    assert (a*0*0+b*0+c)<0 and (a*10*10+b*10+c)>0
    # Fractional stationary balance for 38 deterministic switching intensities.
    xs=[F(0)]+[F(i,7) for i in range(1,38)]
    for x in xs:
        MX=[[evalp(v,x) for v in row] for row in M]
        matden=evalp(den,x)
        m=[]
        for j in range(3):
            mm=[[M[r][cc] if cc!=j else rhs[r] for cc in range(3)] for r in range(3)]
            m.append(evalp(det(mm),x)/matden)
        for i in range(3):assert sum(MX[i][j]*m[j] for j in range(3))==F([1,40,50][i],3)
        assert sum(m)==evalp(num,x)/matden
    print('EXACT example polynomial, derivative, and 38 balance systems: PASS')
    print('k_star:',format(star,'.12f'))
    print('mean_at_max:',format(crest,'.12f'))
    print('slow_limit:',c0,'fast_limit:',cfast,'relative_gain_slow:',format(crest/float(c0)-1,'.8f'))

if __name__=='__main__':example()
