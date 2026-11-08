from fractions import Fraction as F

def norm(z):
    u,v=z
    return max(abs(u),abs(v),abs(u-v))

def add(a,b): return a[0]+b[0],a[1]+b[1]
def mul(a,b): return a*b[0],a*b[1]
def sub(a,b): return a[0]-b[0],a[1]-b[1]
def R(z): u,v=z; return u-v,u
def Q(z): u,v=z; return u,u-v
V=[(F(1),F(0)),(F(1),F(1)),(F(0),F(1)),(F(-1),F(0)),(F(-1),F(-1)),(F(0),F(-1))]
assert all(norm(R(z))==norm(z) and norm(Q(z))==norm(z) for z in V)
assert all(R(V[j])==V[(j+1)%6] for j in range(6))
for tau in [F(0),F(1,10),F(1,3),F(1,2),F(1),F(2),F(7,2),F(10)]:
    D=1+tau+tau*tau
    goal=tau+1/D
    x=(F(1),1/D); y=(tau*tau/D,F(1))
    assert norm(x)==norm(y)==1
    assert norm(add(x,mul(tau,y)))==goal
    assert norm(sub(mul(tau,x),y))==goal
    for s in [F(0),F(1,7),F(1,2),F(1)]:
        for t in [F(0),F(2,7),F(1)]:
            xx=(F(1),s)
            for yy in [(F(1),t),(1-t,F(1)),(-t,1-t),(-F(1),-t)]:
                z=max(norm(add(xx,mul(tau,yy))),norm(sub(mul(tau,xx),yy)))
                assert z>=goal
    assert ((1+tau)+tau*tau*tau+tau*tau)/D==goal
print('HEXAGON_SKEW_SCHAFFER_RATIONAL_CHECK_OK')
