"""Clean robust chord-tangent on E_lam: x^3+y^3+z^3-3 lam xyz=0, O=(1:-1:0)."""
import numpy as np
lam = 2.0
def F(P):
    x,y,z=P; return x**3+y**3+z**3-3*lam*x*y*z
def grad(P):
    x,y,z=P
    return np.array([3*x**2-3*lam*y*z,3*y**2-3*lam*x*z,3*z**2-3*lam*x*y],dtype=complex)
O=np.array([1.0,-1.0,0.0],dtype=complex)
def line_points(L):
    u,s,vh=np.linalg.svd(L.reshape(1,3)); return vh[1,:],vh[2,:]
def third(P,Q):
    P=np.asarray(P,dtype=complex); Q=np.asarray(Q,dtype=complex)
    M=np.column_stack([P,Q]); _,s_,_=np.linalg.svd(M)
    if s_[-1]<1e-10: L=grad(P)       # tangent (doubling)
    else: L=np.cross(P,Q)
    A,B=line_points(L)
    ts=np.array([0,1,2,3],dtype=complex)
    vs=np.array([F(A*t+B) for t in ts])
    V=np.vander(ts,4,increasing=True); c=np.linalg.solve(V,vs)
    r=np.roots([c[3],c[2],c[1],c[0]])
    def pdist(u,R):
        C=A*u+B; M2=np.column_stack([C,R]); _,s2,_=np.linalg.svd(M2); return s2[-1]/ (np.linalg.norm(C)+1e-30)
    if s_[-1]<1e-10:
        dP=np.array([pdist(u,P) for u in r]); iP=int(np.argmin(dP)); assert dP[iP]<1e-4,(dP,r)
        cands=[i for i in range(3) if i!=iP]
        # tangent: root at P is double; third = remaining unless all equal (flex: return P)
        if min(abs(r[i]-r[iP]) for i in cands)<1e-6:
            return P/np.max(np.abs(P))
        j=max(cands,key=lambda i: abs(r[i]-r[iP])); C=A*r[j]+B; return C/np.max(np.abs(C))
    else:
        dP=np.array([pdist(u,P) for u in r]); dQ=np.array([pdist(u,Q) for u in r])
        iP,iQ=int(np.argmin(dP)),int(np.argmin(dQ))
        assert dP[iP]<1e-4 and dQ[iQ]<1e-4,(dP,dQ,r)
        if iP!=iQ: j=3-iP-iQ
        else: # numerically tangent case
            cands=[i for i in range(3) if i!=iP]
            if min(abs(r[i]-r[iP]) for i in cands)<1e-4: return P/np.max(np.abs(P))
            j=max(cands,key=lambda i: abs(r[i]-r[iP]))
        C=A*r[j]+B; return C/np.max(np.abs(C))
def add(P,Q):
    R=third(P,Q); S=third(O,R); return S/np.max(np.abs(S))
def neg(P): return third(O,P)
def mul(n,P):
    R=O.copy(); Q=np.array(P,dtype=complex); k=n
    while k:
        if k&1: R=add(R,Q)
        Q=add(Q,Q); k>>=1
    return R
def peq(P,Q):
    M=np.column_stack([P,Q]); _,s_,_=np.linalg.svd(M); return s_[-1]
if __name__=="__main__":
    P=np.array([1.0,2.0,3.0],dtype=complex)
    print("assoc test:", peq(add(add(P,O),P),add(P,add(O,P))))
    print("P-P==O:", peq(add(P,neg(P)),O))
    print("2P on curve:", F(add(P,P)))
    print("order map:", [float(peq(mul(k,P),O)) for k in [1,2,3,7]])
    import pickle
    print("OK grouplaw")
