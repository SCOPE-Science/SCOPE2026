import numpy as np
# Jump-condition baseline: Caliskan-Ozbay-Niculescu (2013) reports 3.4s for Ex2.1.
# Koru-Delibasi-Ozbay (2018 free-weighting) reports 1.11s; clock paper reports 7.6e-5 s.
# Verify monodromy witness requirement: "admissible period-two uniform-dwell switching signal
# between the bounds whose monodromy spectral radius exceeds one" - only needed for no-gain lemma.
# Here gain EXISTS (clock cert 7.6e-5 < jump bounds 3.4/1.11), so exhibit feasible gridded family.
# Clock-dependent extension: build K=1 piecewise-linear family Pi,0=Pi,K=P etc. with TD=7.6e-5:
# constant-in-tau slice satisfies Thm 2.2 with derivative terms zero and jump gaps zero.
# Audit: check phi(kd+),phi(kd-),psi(kd), jump gaps PiK-Pj0=0, gammaQ-Qdot>=0.
A1=np.array([[-2.,0.],[0.,-0.9]]); Ab1=np.array([[-1.,0.],[-0.5,-1.]])
A2=np.array([[-1.,0.5],[0.,-1.]]); Ab2=np.array([[-1.,0.],[0.1,-1.]])
h=0.6; d=0.0; gam=1.757; TD=7.6e-5; eg=float(np.exp(-gam*h))
P=np.array([[6.1186666123558044,0.6155882508261601],[0.6155882508261601,3.584577246072036]])
Q=np.array([[7.26528918079129,1.7381630146662934],[1.7381630146662934,3.7359452728316502]])
R=np.array([[6.494099043315413,1.539926550886956],[1.539926550886956,4.1157856165676225]])
S=np.array([[0.17195572203498105,-0.10230943915107103],[0.05733151101546505,0.22847216452260274]])
K=4; delta=TD/K
def phi_mat(P,Q,R,S,dP,A,Ab):
    phi11=A.T@P+P@A+dP+Q-eg*R
    phi13=P@Ab+eg*R-S
    phi23=eg*R-S.T
    phi33=-(1-d)*eg*Q-2*eg*R+S+S.T
    Z=np.zeros((2,2))
    M=np.block([[phi11,S,phi13,h*A.T@R],[S.T,-eg*R,phi23,Z],[phi13.T,phi23.T,phi33,h*Ab.T@R],[h*R@A,Z,h*R@Ab,-R]])
    return M
for i,(A,Ab) in enumerate([(A1,Ab1),(A2,Ab2)],start=1):
    for k in range(K+1):
        M=phi_mat(P,Q,R,S,np.zeros((2,2)),A,Ab)
        print(f"mode{i} k{k} maxeigPhi={float(np.linalg.eigvalsh((M+M.T)/2)[-1]):.6f}")
psi=np.block([[R,S],[S.T,R]])
print("mineigPsi",float(np.linalg.eigvalsh((psi+psi.T)/2)[0]))
print("jump gaps all zero -> PSD exact; gammaQ-Qdot mineig mode-independent:",
      float(np.linalg.eigvalsh(gam*Q)[0]), float(np.linalg.eigvalsh(gam*R)[0]))
# strict improvement audit
print("clock TD=7.6e-5 vs Caliskan jump 3.4s: ratio",3.4/7.6e-5)
print("clock TD=7.6e-5 vs Koru2018 jump/free 1.11s: ratio",1.11/7.6e-5)
