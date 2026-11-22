"""Reproducible algebra and finite diagnostics for the memristive critical slice.
Not a substitute for the infinite-dimensional monotone iteration or asymptotic proof.
"""
import sympy as sp
import mpmath as mp

x,y,z,w,a,b=sp.symbols('x y z w a b', real=True)
f=lambda t:1-t*t/2
x1=a*y**2
y1=b*f(w)*y*(1-z)
z1=1-x
w1=w+y
y2=b*f(w1)*y1*(1-z1)
w2=w1+y1
y3=b*f(w2)*y2*(1-(1-x1))
assert sp.simplify(y3-a*b*f(w2)*y2*y**2)==0
P=sp.Symbol('p')
root1=sorted(sp.nroots(P**3-P**2-2),key=lambda t:-sp.re(t))[0]
root2=sorted(sp.nroots(P**3-2*P**2-2),key=lambda t:-sp.re(t))[0]
rho=float(sp.re(root1));beta=float(sp.re(root2))
assert 1.69<rho<1.70 and 2.35<beta<2.37
assert (2/rho)**0.5>1 and (2/beta)**0.5<1
print('exact scalar reduction: PASS; Perron roots',rho,beta)

mp.mp.dps=110
s=mp.mpf('0.1');A=mp.mpf(1);N=8
upper=[s,s**3,s**7]
while len(upper)<N:
    n=len(upper)-1
    upper.append(2*mp.sqrt(2)*A*upper[n]**2*upper[n-2]**2)
assert all(upper[n+1]<upper[n]/2 for n in range(2,N-1))
ys=[s,s**3,s**7]+[mp.mpf(0)]*(N-3)
for _ in range(N+5):
    new=ys[:3]
    for n in range(2,N-1):
        d=mp.fsum(ys[n:]); F=mp.sqrt(2)*d-d*d/2
        new.append(A*F*ys[n]*ys[n-2]**2)
    assert all(0<=new[j]<=upper[j] for j in range(N))
    assert all(new[j]>=ys[j] for j in range(N))
    ys=new
assert all(v>0 for v in ys)
w2=mp.sqrt(2)-mp.fsum(ys[2:]);w1=w2-ys[1];w0=w1-ys[0]
F=lambda t:1-t*t/2
x0=ys[2]/(F(w1)*ys[1]);z0=1-ys[1]/(F(w0)*ys[0])
assert 0<x0<1 and 0<z0<1 and 0<w0<w1<w2<mp.sqrt(2)
X,Y,Z,W=x0,ys[0],z0,w0
for n in range(4):
    X,Y,Z,W=Y**2,F(W)*Y*(1-Z),1-X,W+Y
    assert abs(Y-ys[n+1])<=mp.mpf('1e-85')*ys[n+1]
print('monotone tail bounds and finite direct-map consistency: PASS')
print('positive initial state:',*[mp.nstr(t,12) for t in (x0,ys[0],z0,w0)])
print('boundary sample y3:',mp.nstr(ys[3],18),'y4:',mp.nstr(ys[4],18))
