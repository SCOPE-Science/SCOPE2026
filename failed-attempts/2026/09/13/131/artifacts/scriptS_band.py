"""Script S: CERTIFIED essential-radius strip via cone-adapted Finsler norm.
Anisotropic norm: ||v||_* = max(|s|/t, |y|_2), t = cone width parameter.
Block bounds from Script K: |m11|<=A11=0.2161, |r|<=R=0.0198, |c|<=C=0.4756,
sigmin(B)>=S=1.3713 (grid+pad certificate). For v in cone |s|<=kap|y|:
  |s'|<= (A11*kap+R)|y|, |y'|>=(S-kap*C)|y|.
Finsler norm with t: ||Mv||_*/||v||_* <= max over cone of
  max(|s'|/t,|y'|)/max(|s|/t,|y|). Take t=kap: ratio <= max((A11*kap+R)/kap, H)
  in strong norm... For Lasota-Yorke essential radius use Gouzel-Liverani factor:
  rho_ess <= max(Lambda_s^{alpha}, lambda_w^{-beta}) style. Evaluate: with
  Lambda_s=0.2206 (stable contraction), lambda_w=1.1332 (weak expansion):
  choices alpha,beta in (0,1): max(0.2206^alpha, 1.1332^{-beta}).
  alpha=0.3: 0.635; beta=1: 0.882?? Need <=0.7: take alpha small? 0.2206^0.3=0.635 OK
  but weak factor 1.1332^{-beta} with beta<=1-p... For smooth 2-unstable case use
  beta close to 1: 1/1.1332=0.8825 > 0.7! PROBLEM: weak expansion 1.133 too small
  for 0.7 via this crude factor. Use higher iterate: lambda_w^N grows: N=6:
  1.1332^6 = 2.094 => factor 0.4775 <= 0.7. So take N=6 iterate: rho_ess(P^6)<=0.7
  hmm but target needs rho_ess(P)<=0.7, i.e. rho_ess(P^6)<=0.7^6=0.1176. Gap!
Refine: use TRUE weak expansion ~1.55 (linear value; nonlinear per-vector min over
cone measured 1.43 in sampling, Script C). The certified 1.133 lost much to crude
|c| padding (0.4756 includes |E|corners double counted). Improve: certify sigmin
of FULL 2x2 B on finer grid with derivative-based Lipschitz (not triangle) to get
sigmin>=1.43+, and bound |c| by sampling+Lipschitz (true max ~0.2?). Then
lambda_w >= 1.43-0.5*0.25 = 1.3 => 1/1.3 = 0.77 still >0.7. N=2: 1.3^2=1.69,
rho_ess(P^2)<=0.77^2? no: factor per 2 steps 1/1.69=0.59<=0.7?? But again
rho_ess(P)<=0.7 needs per-step factor 0.7.
Honest conclusion: essential<=0.7 needs lambda_w^{beta}>=1/0.7=1.4286 with
beta<1 (regularity ceiling, beta<=1): lambda_w>=1.43 at beta=1, or the strong
direction (3.24) compensates in determinant-based (Baladi-Tsujii) spaces where
rho_ess ~ max(lambda_w^{-1}... involving BOTH unstable directions via volume:
for volume-preserving 2D unstable, weight ~ (det Df|_u)^{-1/p}... = (lambda_w*lambda_s_u)^{-1}.
With lambda_u_strong=3.24: det_u >= 1.43*2.9 ~ 4.1 => rho factor tiny. THAT is the
route: essential radius bound via unstable Jacobian determinant (transfer operator
on densities for volume-preserving map: LY inequality contracts with
(det_u)^{-1}-type factor, not weak-only). Compute certified det_u >= ? and report.
"""
import numpy as np, math
A=np.array([[2.,1.,0.],[1.,2.,1.],[0.,1.,1.]])
w,P=np.linalg.eigh(A)
alp,bet=2*math.pi*0.03,2*math.pi*0.02
C=P.T@A@P
E2=P.T@(A@np.array([[0.,1.,0.],[0.,0.,0.],[0.,0.,0.]]))@P*alp
E3=P.T@(A@np.array([[0.,0.,0.],[0.,0.,1.],[0.,0.,0.]]))@P*bet
def Bmat(c2,c3): return (C+c2*E2+c3*E3)[1:,1:]
n=10; dmin=1e9
for i in range(n+1):
    for j in range(n+1):
        dmin=min(dmin,abs(np.linalg.det(Bmat(-1+2*i/n,-1+2*j/n))))
from itertools import product
nE2=np.linalg.norm(E2[1:,1:],2); nE3=np.linalg.norm(E3[1:,1:],2)
# d det <= 2*max||B||*(lip): crude pad
Bmax=max(np.linalg.norm(Bmat(c2,c3),2) for c2 in (-1,1) for c3 in (-1,1))
pad=2*Bmax*(nE2+nE3)/n
print(f"grid det_u min={dmin:.4f} pad={pad:.4f} => certified det(Df|_u-plane)>={dmin-pad-1e-9:.4f}")
print("true linear det_u = 1.555*3.247 =",1.55495813*3.24697960)
