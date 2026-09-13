import numpy as np
A1=np.array([[-2.,0.],[0.,-0.9]]); Ab1=np.array([[-1.,0.],[-0.5,-1.]])
A2=np.array([[-1.,0.5],[0.,-1.]]); Ab2=np.array([[-1.,0.],[0.1,-1.]])
h=0.6; d=0.0; gam=0.8
eg=np.exp(-gam*h)
def build(P,Q,R,S12,A,Ab):
    phi11=A.T@P+P@A+Q-eg*R
    phi13=P@Ab+eg*R-S12
    phi23=eg*R-S12.T
    phi33=-(1-d)*eg*Q-2*eg*R+S12+S12.T
    Z=np.zeros((2,2))
    M=np.block([[phi11,S12,phi13,h*A.T@R],[S12.T,-eg*R,phi23,Z],[phi13.T,phi23.T,phi33,h*Ab.T@R],[h*R@A,Z,h*R@Ab,-R]])
    psi=np.block([[R,S12],[S12.T,R]])
    return M,psi
def maxeig(M):
    M=(M+M.T)/2
    w=np.linalg.eigvalsh(M)
    return w[-1]
rng=np.random.default_rng(0)
def unpack(v):
    p=v[0:3]; q=v[3:6]; r=v[6:9]; s=v[9:13]
    P=np.array([[p[0],p[1]],[p[1],p[2]]]); Q=np.array([[q[0],q[1]],[q[1],q[2]]]); R=np.array([[r[0],r[1]],[r[1],r[2]]])
    S=np.array([[s[0],s[1]],[s[2],s[3]]])
    return P,Q,R,S
def cost(v):
    P,Q,R,S=unpack(v)
    eP=np.linalg.eigvalsh((P+P.T)/2)[0]; eQ=np.linalg.eigvalsh((Q+Q.T)/2)[0]; eR=np.linalg.eigvalsh((R+R.T)/2)[0]
    M1,ps1=build(P,Q,R,S,A1,Ab1); M2,ps2=build(P,Q,R,S,A2,Ab2)
    m1=maxeig(M1); m2=maxeig(M2)
    q1=maxeig(-ps1); q2=maxeig(-ps2)
    return max(m1,m2,q1,q2,-eP,-eQ,-eR),(m1,m2,q1,q2,eP,eQ,eR)
v=np.array([2.,0.,2., 1.,0.,1., 0.5,0.,0.5, 0.05,0.,0.,0.05])
c,info=cost(v); print("init",c,info)
best=c; bv=v.copy()
for it in range(300000):
    step=0.03*(0.99999**it)+2e-4
    prop=bv+rng.normal(0,step,size=bv.shape)
    c2,info2=cost(prop)
    if c2<best:
        best=c2; bv=prop
        print(it,round(best,5),[round(x,4) for x in info2])
print("BEST",best)
P,Q,R,S=unpack(bv)
print("P=",P.tolist()); print("Q=",Q.tolist()); print("R=",R.tolist()); print("S=",S.tolist())
M1,ps1=build(P,Q,R,S,A1,Ab1); M2,ps2=build(P,Q,R,S,A2,Ab2)
print("M1eig",np.linalg.eigvalsh((M1+M1.T)/2).tolist())
print("M2eig",np.linalg.eigvalsh((M2+M2.T)/2).tolist())
print("ps1",np.linalg.eigvalsh((ps1+ps1.T)/2).tolist(),"ps2",np.linalg.eigvalsh((ps2+ps2.T)/2).tolist())
