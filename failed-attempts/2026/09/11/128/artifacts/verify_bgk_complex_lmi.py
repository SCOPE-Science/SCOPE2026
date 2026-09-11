"""Complex-field-correct BGK LMI (28x28) for lane-1018.
h = u+iv; T=iV. Re<ALh,h> (BGK) is SKEW in (u,v): = q_u'BM_v - q_v'BM_u.
Re<Ah,h> is pure (u,v)-cross. Stacked LMI [[Gd,K],[K',Gd']] with
Gd: A11=eps*Qmm-kap*I, A12=eps*(B-2FB)~ Jh, A22=(1-kap)I+eps Jh'QzJh.
K = K_D + K_H as derived in worklog analysis.
"""
import numpy as np
exec(open('scratch/lmi15.py').read().split("eps = ")[0])
B = np.linalg.inv(np.eye(5) + S)
def picoeffs(p):
    return np.array([pexpect(pmul(polys[c], p)) for c in range(5)])
V1 = {(1,0,0):1.0}; V1SQ = {(2,0,0):1.0}
ua=[pmul(V1,polys[a]) for a in [1,2,3,4]]; wa=[pmul(V1SQ,polys[a]) for a in range(5)]
Ca=np.array([picoeffs(p) for p in ua]); Cb=np.array([picoeffs(p) for p in wa])
def mgram(pa,pb,A,B_): return pexpect(pmul(pa,pb))-A@B_
Ju=np.zeros((4,4)); Jw=np.zeros((5,5)); Juw=np.zeros((4,5))
for i in range(4):
    for j in range(4): Ju[i,j]=mgram(ua[i],ua[j],Ca[i],Ca[j])
for i in range(5):
    for j in range(5): Jw[i,j]=mgram(wa[i],wa[j],Cb[i],Cb[j])
for i in range(4):
    for j in range(5): Juw[i,j]=mgram(ua[i],wa[j],Ca[i],Cb[j])
J=np.block([[Ju,Juw],[Juw.T,Jw]])
wJ,VJ=np.linalg.eigh(J+1e-12*np.eye(9))
Jh=VJ@np.diag(np.sqrt(np.maximum(wJ,0)))@VJ.T
eps=1/8; kap=1/120
BS=B@S; FBF=F@B@F
Qmm=((BS+BS.T)/2-((FBF+FBF.T)/2))
Eq=np.zeros((5,4)); Eq[1,0]=1; Eq[2,1]=1; Eq[3,2]=1; Eq[4,3]=1
Xd=(B-2*F@B)@Eq  # 5x4 diag cross M-q
Xr=B             # 5x5 diag cross M-r
X=np.hstack([Xd,Xr])
Qz=np.zeros((9,9)); Qz[:4,:4]=Eq.T@(-(B+B.T)/2)@Eq
A11=eps*Qmm-kap*np.eye(5)
A12=eps*X@Jh
A22=(1-kap)*np.eye(9)+eps*(Jh.T@Qz@Jh)
Gd=np.block([[A11,A12],[A12.T,A22]])
print("Gd min eig:", np.linalg.eigvalsh(Gd)[0])
# K blocks on (M5,y9)x(M5,y9): K_D: [Mu,qv]+eps*B/2 ... define K with
# stacked order (u;v): G=[[Gd,K],[K.T,Gd]]; contribution 2*u'K*v.
# D-skew: -eps*q_u'BM_v + eps*q_v'BM_u.
#  -eps*q_u'BM_v = -eps*qu'B'Mv -> K[Mv-part...]: 2*u'Kv with u=(Mu,yu),v=(Mv,yv):
#   term -eps*qu'B Mv: qu = Eq' z_u, z_u=Jh yu -> -eps*yu'Jh'Eq'B Mv -> K[yu,Mv] block: K[5:, :5] += -eps*Jh'Eq'B/2? 2*u'Kv: u'K v with K[yu,Mv]=C gives 2*yu'C Mv. Need 2C=-eps*Jh'Eq'B -> C=-eps/2*Jh'Eq'B.
#  +eps*q_v'BM_u -> K[yv,Mu]: by symmetry K.T[Mv...]: K[5:,:5] also gets? term eps*yv'Jh'Eq'B Mu = u'K v with u=Mu? No: u-part Mu, v-part yv: Mu'K[Mu,yv]yv: K[:5,5:]+=eps/2*B'EqJh = eps/2*B Eq Jh.
# H-cross: -kap*(M_v'FBM_u + M_u'FBM_v + q_v'BM_u + q_u'BM_v):
#  -kap*M_v'FBM_u -> K[Mu,Mv] += -kap/2*(FB+(FB)')? 2*Mu'K Mv with K=-kap/2*(FB+ B'F')/2... 2*Mu'C*Mv vs -kap*Mv'FBMu -kap*Mu'F'BMv = -kap*Mu'(FB+B'F')Mv... (FB sym? F,B sym but product not.) Mv'FBMu = Mu'B'FMv = Mu'BF Mv. So total -kap*Mu'(BF+FB)Mv. C= -kap/2*(BF+FB).
#  -kap*q_v'BM_u -> K[Mu,yv] += -kap/2*B Eq Jh.  -kap*q_u'BM_v -> K[yu,Mv] += -kap/2*Jh'Eq'B.
K=np.zeros((14,14))
Wq=np.hstack([np.eye(4),np.zeros((4,5))])@Jh  # 4x9: qu = Wq yu
K[5:,:5]+=(-eps/2)*Wq.T@Eq.T@B - (kap/2)*Wq.T@Eq.T@B  # K[yu,Mv]
K[:5,5:]+=(eps/2)*B@Eq@Wq - (kap/2)*B@Eq@Wq  # K[Mu,yv]
K[:5,:5]+=(-kap/2)*(B@F+F@B)  # K[Mu,Mv]
G28=np.block([[Gd,K],[K.T,Gd]])
ev=np.linalg.eigvalsh(G28)
print("G28 min eig:", ev[0])
print("G28 eigs:", np.round(ev,4))
print("COMPLEX BGK:", "CLOSE" if ev[0]>=0 else "OPEN")
print("||K||:", np.linalg.norm(K,ord=2))
