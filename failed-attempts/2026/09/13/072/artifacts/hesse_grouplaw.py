"""Correct exact-polarization Hesse group law over C. O=(1:-1:0). Fixed tangent case."""
import numpy as np
def pol(P,Q,R,a,b,c):
    A=-(a*b*c); B=(a**3+b**3+c**3)
    s=sum(6*A*P[i]*Q[i]*R[i] for i in range(3))
    s+=B*(P[0]*(Q[1]*R[2]+Q[2]*R[1])+P[1]*(Q[0]*R[2]+Q[2]*R[0])+P[2]*(Q[0]*R[1]+Q[1]*R[0]))
    return s
def pnorm(P):
    P=np.array(P,dtype=complex); m=np.max(np.abs(P)); return P/m
def F(P,a,b,c):
    x,y,z=P; return -(a*b*c)*(x**3+y**3+z**3)+(a**3+b**3+c**3)*x*y*z
def grad(P,a,b,c):
    x,y,z=P; A=-(a*b*c); B=(a**3+b**3+c**3)
    return np.array([3*A*x**2+B*y*z, 3*A*y**2+B*x*z, 3*A*z**2+B*x*y])
O=np.array([1.0,-1.0,0.0],dtype=complex)
def _third_on_line(A_,B_,s0,t0,a,b,c):
    # line {s A_ + t0 B_}, P at s=s0 is a double root (tangent). residual via exact Taylor:
    # G(s)=FA s^3+(pAAB/2)s^2 t0+(pABB/2)s t0^2+FB t0^3; u3 = -cc2/cc3, cc2=G''(s0)/2, cc3=G'''(s0)/6=FA.
    FA=F(A_,a,b,c)
    if abs(FA)<1e-30:  # A_ on curve: swap basis
        A_,B_=B_,A_; s0,t0=t0,s0; FA=F(A_,a,b,c)
        if abs(FA)<1e-30: return pnorm(A_)  # degenerate; bail
    pAAB=pol(A_,A_,B_,a,b,c)/2; pABB=pol(A_,B_,B_,a,b,c)/2
    Gpp = lambda s: 6*FA*s+2*pAAB*t0
    cc2=Gpp(s0)/2; cc3=FA
    if abs(cc3)<1e-30 and abs(cc2)<1e-30: return pnorm(s0*A_+t0*B_)  # flex/triple
    return pnorm((s0+(-cc2/cc3))*A_+t0*B_)
def third(P,Q,a,b,c):
    P=pnorm(P); Q=pnorm(Q)
    M=np.column_stack([P,Q]); _,s,_=np.linalg.svd(M)
    if s[-1]>1e-12:
        C2=pol(P,P,Q,a,b,c)/2; C1=pol(P,Q,Q,a,b,c)/2; C0=F(Q,a,b,c)
        if abs(C0)<1e-12 and abs(C1)+abs(C2)>1e-30:
            return pnorm(C1*P-C2*Q)
    L=grad(P,a,b,c); L=L/np.max(np.abs(L))
    _,_,vh=np.linalg.svd(L.reshape(1,3)); A_,B_=vh[1,:].conj(),vh[2,:].conj()
    # project P onto basis: solve [A_ B_][s,t]^T = P (least squares; exact since P on line)
    G=np.column_stack([A_,B_]); st,_,_,_=np.linalg.lstsq(G,P,rcond=None)
    return _third_on_line(A_,B_,st[0],st[1],a,b,c)
def add(P,Q,a,b,c): return pnorm(third(pnorm(third(pnorm(P),pnorm(Q),a,b,c)),O,a,b,c))
def mul(n,P,a,b,c):
    R=O.copy(); Q=pnorm(P); k=n
    while k:
        if k&1: R=add(R,Q,a,b,c)
        Q=add(Q,Q,a,b,c); k>>=1
    return R
def peq(P,Q):
    M=np.column_stack([pnorm(P),pnorm(Q)]); _,s,_=np.linalg.svd(M); return s[-1]
if __name__=="__main__":
    for abc in [(0.5+0.1j,-0.3+0.2j,1.0),(1.0,2.0,3.0)]:
        a,b,c=abc
        P=pnorm([a,b,c])
        print("abc=",abc)
        print("  assoc:",peq(add(add(P,O,a,b,c),P,a,b,c),add(P,add(O,P,a,b,c),a,b,c)))
        print("  P-P==O:",peq(add(P,third(O,P,a,b,c),a,b,c),O))
        print("  orders:",[round(float(peq(mul(k,P,a,b,c),O)),6) for k in range(1,9)])
