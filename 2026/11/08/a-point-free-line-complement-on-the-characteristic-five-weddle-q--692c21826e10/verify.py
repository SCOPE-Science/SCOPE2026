"""Reproduce finite-field rational points, lines and incidence of a Weddle quartic.

Pure Python 3, no nonstandard dependencies. The complete finite searches are:
156 projective points and 806 projective lines over F_5, and
16276 projective points over F_25 (u^2 = 2).
"""
from itertools import combinations, product
from collections import Counter

P = 5

def normalized(v):
    for a in v:
        if a % P:
            inv = pow(a % P, -1, P)
            return tuple((x * inv) % P for x in v)
    raise ValueError("zero projective vector")

def points5():
    return [((0,) * i + (1,) + suffix)
            for i in range(4)
            for suffix in product(range(5), repeat=3-i)]

def wedge_f(v):
    a,b,c,d = v
    return (a*a*b*d-a*a*c*c-a*b*b*c+a*c*d*d
            +b**4-b*b*d*d-b*c*c*d+c**4) % P

def line_through(p,q):
    return frozenset([q] + [normalized([(p[j]+t*q[j]) % P for j in range(4)])
                            for t in range(5)])

def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
        -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
        +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0])) % P

def plane_normal(p,q,r):
    mat=(p,q,r)
    v=[]
    for i in range(4):
        m=[[row[j] for j in range(4) if j!=i] for row in mat]
        v.append(((-1)**i)*det3(m)%P)
    assert any(v)
    return tuple(v)

def dot(n,p):
    return sum(x*y for x,y in zip(n,p)) % P

def secant_and_residual_lines(pts):
    six = [normalized((1,t,t*t,t*t*t)) for t in range(5)] + [(0,0,0,1)]
    assert len(set(six)) == 6
    secants = {line_through(p,q) for p,q in combinations(six,2)}
    residual = set()
    for triple in combinations(range(6),3):
        comp = tuple(i for i in range(6) if i not in triple)
        if triple > comp: continue
        n1 = plane_normal(*(six[i] for i in triple))
        n2 = plane_normal(*(six[i] for i in comp))
        line = frozenset(p for p in pts if dot(n1,p)==dot(n2,p)==0)
        assert len(line)==6
        residual.add(line)
    assert len(secants)==15 and len(residual)==10
    assert secants.isdisjoint(residual)
    return six,secants,residual

def fpadd(x,y): return ((x[0]+y[0])%5, (x[1]+y[1])%5)
def fpneg(x): return ((-x[0])%5, (-x[1])%5)
def fpsub(x,y): return fpadd(x,fpneg(y))
def fpmul(x,y):
    return ((x[0]*y[0]+2*x[1]*y[1])%5,
            (x[0]*y[1]+x[1]*y[0])%5)

def eval25(a,b,c,d):
    aa=fpmul(a,a); bb=fpmul(b,b); cc=fpmul(c,c); dd=fpmul(d,d)
    termspos=[fpmul(fpmul(aa,b),d),fpmul(fpmul(a,c),dd),fpmul(bb,bb),fpmul(cc,cc)]
    termsneg=[fpmul(aa,cc),fpmul(fpmul(a,bb),c),fpmul(bb,dd),fpmul(fpmul(b,cc),d)]
    y=(0,0)
    for z in termspos: y=fpadd(y,z)
    for z in termsneg: y=fpsub(y,z)
    return y

def count25():
    field=list(product(range(5),repeat=2))
    zero=(0,0);one=(1,0)
    count=0
    for i in range(4):
        for tail in product(field,repeat=3-i):
            v=[zero]*i+[one]+list(tail)
            count += eval25(*v)==zero
    return count

def fppow(x,n):
    result=(1,0)
    while n:
        if n&1: result=fpmul(result,x)
        x=fpmul(x,x);n//=2
    return result

def genus2_counts():
    f25=list(product(range(5),repeat=2))
    squares={fpmul(y,y) for y in f25}
    count=1
    for x in f25:
        y=fpsub(fppow(x,5),x)
        count+=1 if y==(0,0) else (2 if y in squares else 0)
    count5=1+sum(1 for x in range(5) if (pow(x,5,5)-x)%5==0)
    assert count5==6 and count==6
    return count5,count

def main():
    pts=points5()
    assert len(pts)==156 and len(set(pts))==156
    W={p for p in pts if wedge_f(p)==0}
    assert len(W)==66
    all_lines={line_through(a,b) for a,b in combinations(pts,2)}
    assert len(all_lines)==806
    contained={line for line in all_lines if line <= W}
    assert len(contained)==25
    nodes,secants,residual=secant_and_residual_lines(pts)
    assert contained==secants|residual
    assert set(nodes)<=W
    incid=Counter(sum(x in l for l in contained) for x in W)
    assert incid==Counter({2:60,5:6})
    for x in W:
        if x in nodes:
            assert sum(x in s for s in secants)==5
            assert sum(x in r for r in residual)==0
        else:
            assert sum(x in s for s in secants)==1
            assert sum(x in r for r in residual)==1
    assert len(set().union(*contained))==66
    g5,g25=genus2_counts()
    n25=count25()
    assert n25==1026
    assert 25*26 - (6*4+60)==566
    assert n25-566==460
    print('GENUS2_F5_POINTS=6; GENUS2_F25_POINTS=6')
    print('PROJECTIVE_F5_POINTS=156')
    print('PROJECTIVE_F5_LINES=806')
    print('WEDDLE_F5_POINTS=66')
    print('WEDDLE_F25_POINTS=1026')
    print('WEDDLE_F5_LINES=25')
    print('SECANTS=15; RESIDUAL_LINES=10')
    print('RATIONAL_POINT_LINE_INCIDENCE=6x5,60x2')
    print('COMPLEMENT_F5_POINTS=0')
    print('COMPLEMENT_F25_POINTS=460')
    print('VERIFY_OK')

if __name__=='__main__': main()
