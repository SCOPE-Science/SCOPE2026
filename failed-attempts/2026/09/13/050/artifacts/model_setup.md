# Model setup (finite-state stationary discounted vs ergodic MFG)

States: [d]={1..d}, d>=3. Simplex S_d={m>=0,sum m=1}.
For x in [d], differences: (Delta u)(x,y)=u(y)-u(x), vector in R^{d-1}~R^d with zero x-slot.

Data class D(d,c,L,A):
- Admissible rates: compact set A of matrices gamma(x,y)>=a_min>0 for x!=y,
  gamma(x,x)=-sum_{y!=x}gamma(x,y), with 0<a_min<=gamma<=a_max.
  Controlled via feedback: gamma(x,y)=gamma^*(x,y,p) where p=Delta u(x,·).
- Hamiltonian H(x,p) smooth, uniformly convex in p:
  H(x,p)=sup_{a in A_x}[ -a·p - L(x,a) ], L smooth strictly convex.
  So D_p H = -a^*, D^2_{pp}H in [1/L_H, L_H] on bounded p-sets,
  gamma^*=-D_p H bounded in [a_min,a_max], Lipschitz in p.
- Coupling F:S_d->R^d smooth, L_F-Lipschitz, Lasry-Lions strictly monotone:
  (F(m)-F(m'))·(m-m') >= c|m-m'|^2, c>0.

Stationary discounted equilibrium (r in (0,1]):
  (D)  r V_r(x) + H(x,Delta V_r(x)) + F(x,m_r) = 0,  x in [d],
       sum_y m_r(y) gamma^*_x(y,Delta V_r(y)) = 0 (i.e. m_r^T G_r=0),
       m_r in S_d, V_r in R^d.
  G_r(y,x)=gamma^*(y,x,Delta V_r(y)) generator.

Stationary ergodic triple (ubar,mbar,lambdabar):
  (E)  lambdabar + H(x,Delta ubar(x)) + F(x,mbar) = 0,
       mbar^T Gbar = 0, Gbar from Delta ubar,
       normalization sum_x ubar(x)=0, lambdabar in R.

Known well-posedness (assumed as background, verified by standard fixed-point
+ irreducibility): under strict monotonicity and a_min>0, (D) has a unique
solution; (E) has a unique triple with normalization. Invariant measures are
strictly positive: m_r(x),mbar(x) >= m_min>0 depending only on d,a_min,a_max
(Doeblin minorization: every chain with rates in [a_min,a_max] has uniform
spectral gap and uniform stationary lower bound).

Targets: with |·| Euclidean on R^d:
  |r V_r - lambdabar 1| + |m_r - mbar| <= C r^alpha, 0<r<=r_0,
  C,r_0,alpha>0 depending only on (d,c,L-bounds,a_min,a_max).

Decomposition: V_r = (rho_r/r) 1 + u_r, sum u_r=0, rho_r=<r V_r> average.
Then Delta V_r = Delta u_r. Goal: sup_r|u_r|<infty, |rho_r 1-lambdabar 1|=O(r),
|m_r-mbar|=O(r). Duality identity (checked symbolically in check_duality.py):
for any u1,u2,m1,m2 with generators G1,G2 from Delta u1,Delta u2:
  sum_x (H(x,Du1)-H(x,Du2)+F(x,m1)-F(x,m2))(m1(x)-m2(x))
  + sum_x (u1-u2)(x) [(G1^T m1)(x)-(G2^T m2)(x)]  (zero at equilibria)
  = sum_x [H(x,Du1)-H(x,Du2)-D_pH(x,Du2)·D(u1-u2)](m2)
  + sum_x [H(x,Du2)-H(x,Du1)-D_pH(x,Du1)·D(u2-u1)](m1)
  + (F(m1)-F(m2))·(m1-m2).
Convexity+monotonicity make RHS >= c|m1-m2|^2 + convexity gaps >=0.
At equilibria LHS reduces to discount/coupling residuals (Lemma 2).
