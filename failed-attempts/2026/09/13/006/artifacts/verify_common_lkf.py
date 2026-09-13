import numpy as np, json
# Target: reproduce Koru Ex 2.1 cert: h=0.6,d=0,gam=1.757, TD~0 + jump-bound comparison.
# Check 1: common LKF (P,Q,R,S) feasibility at gam=1.757 (clock-constant slice of Thm 2.2).
A1=np.array([[-2.,0.],[0.,-0.9]]); Ab1=np.array([[-1.,0.],[-0.5,-1.]])
A2=np.array([[-1.,0.5],[0.,-1.]]); Ab2=np.array([[-1.,0.],[0.1,-1.]])
h=0.6; d=0.0; gam=1.757; eg=float(np.exp(-gam*h))
P=np.array([[6.1186666123558044,0.6155882508261601],[0.6155882508261601,3.584577246072036]])
Q=np.array([[7.26528918079129,1.7381630146662934],[1.7381630146662934,3.7359452728316502]])
R=np.array([[6.494099043315413,1.539926550886956],[1.539926550886956,4.1157856165676225]])
S=np.array([[0.17195572203498105,-0.10230943915107103],[0.05733151101546505,0.22847216452260274]])
def build(P,Q,R,S,A,Ab):
    phi11=A.T@P+P@A+Q-eg*R
    phi13=P@Ab+eg*R-S
    phi23=eg*R-S.T
    phi33=-(1-d)*eg*Q-2*eg*R+S+S.T
    Z=np.zeros((2,2))
    M=np.block([[phi11,S,phi13,h*A.T@R],[S.T,-eg*R,phi23,Z],[phi13.T,phi23.T,phi33,h*Ab.T@R],[h*R@A,Z,h*R@Ab,-R]])
    psi=np.block([[R,S],[S.T,R]])
    return M,psi
for name,A,Ab in [("m1",A1,Ab1),("m2",A2,Ab2)]:
    M,psi=build(P,Q,R,S,A,Ab)
    print(name,"maxeigM",float(np.linalg.eigvalsh((M+M.T)/2)[-1]),"mineigPsi",float(np.linalg.eigvalsh((psi+psi.T)/2)[0]))
print("eigP",np.linalg.eigvalsh(P).tolist(),"eigQ",np.linalg.eigvalsh(Q).tolist(),"eigR",np.linalg.eigvalsh(R).tolist())
# Check 2: jump-condition (Morse/Geromel-Colaneri-type) bound baseline.
# Common LKF exists => jump bound can certify TD=0 (arbitrary switching) in the delay-aware
# Geromel-Colaneri form e^{A TD}P e^{A TD}-P<=0 limit. So no strict clock improvement possible below 0.
# Check 3: monodromy witness math: for constant delay h, mode flows are Phi_i(t)=expm of DDE generator;
# at TD->0 fast switching averages vector fields; both A_i+Abar_i Hurwitz? check.
print("A1+Ab1 eig",np.linalg.eigvals(A1+Ab1).tolist())
print("A2+Ab2 eig",np.linalg.eigvals(A2+Ab2).tolist())
print("avg eig",np.linalg.eigvals(0.5*(A1+Ab1+A2+Ab2)).tolist())
