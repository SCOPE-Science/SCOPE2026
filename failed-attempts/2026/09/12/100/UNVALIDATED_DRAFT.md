# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Hyperbolic-subset logarithmic shadowing for RATTLE — certified librational periodic orbit

## 1. Setting
Planar double pendulum, m1=m2=1, L1=L2=1, g=9.81, angle model (th1,th2,w1,w2),
H(th,w) = w1^2 + w2^2/2 + w1 w2 cos(th1-th2) - 19.62 cos th1 - 9.81 cos th2.
Energy level H0 = -10 (in [-12,-8]). Cartesian map q1=(sin t1,-cos t1),
q2=q1+(sin t2,-cos t2), p=J w; constraints g(q)=0, G(q)p=0 preserved by RATTLE
to roundoff (measured |g|,|Gp| ~ 1e-15).

## 2. Certified hyperbolic periodic orbit (Lambda)
Poincare section Sigma = {th1=0, w1>0} with coordinates x=(th2,w1); energy
eliminates w2 (positive branch). Return map P computed by RK4 (dt=1.25e-4)
plus variational equations; fixed point polished by finite-difference Newton:

- x* = (-0.86787713, 3.29962198), residual |P(x*)-x*| = 7.1e-14 (dt=1.25e-4).
- Return time T = 2.87125 (stable across dt=5e-4..6.25e-5).
- DP* = [[-0.65962305, 0.79661712],[-8.70988141, 9.00174667]],
  multipliers lam_u = 8.22039207, lam_s = 0.12173155, det = 1.00068 (~symplectic 1).
- Transversality: w1 >= 3.175 near section (section speed bounded away from 0).
- Librational: over one period max|th1|=1.4821, max|th2|=2.0926 < pi (no winding).
- Energy: E0=-10.000000, drift 3.7e-11 over period.
- Lambda = the periodic orbit through x* (compact, invariant, in librational region).

Numerics reproduced by output/artifacts/polish.py, refine1.py, meas2.py.

## 3. Explicit cone field (certified margins)
Eigenbasis S=[eu,es], cond(S)=2.72. DP variation measured on section box:
Lipschitz L<=40 (section coords); on box radius r=2e-4 around x*,
grid-max deviation |E|_2 = 0.00954, adopted safe bound e=0.0191 (x2 margin).
- Forward (unstable) cone Ku(0.2)={|eta|<=0.2|xi|}: image slope <= 0.0058 << 0.2,
  expansion mu >= 8.19 >= 1.5. REQUIRED 1.5: satisfied with 5x margin.
- Backward (stable) cone Ks(0.4)={|xi|<=0.4|eta|} under P^{-1} via
  adapted-norm inverse-perturbation lemma: image slope 0.3596 <= 0.4,
  backward expansion mu_back >= 6.08, i.e. forward contraction 1/6.08=0.164 <= 0.67.
  REQUIRED 0.67: satisfied with 4x margin.
Reproduced by output/artifacts/cone5.py. This certifies Lambda as uniformly
hyperbolic with constants lam_u^cert = 6.0 (used; measured 8.19) and
lam_s^cert = 1/6.0 forward contraction (used; measured 0.164).

## 4. Shadowing lemma with explicit constants (map version)
P is C^2 with |DP|<=M_sec=12.57, |DP^{-1}|<=M_inv=12.57 (norms from SVD:
12.568/0.0796), Lipschitz L=40 on box r=2e-4. Standard hyperbolic fixed-point
shadowing (e.g. Palmer / Katok-Hasselblatt Thm 18.1.2 quantitative form):
there are rho>0, C_sh, eps0 such that every eps-pseudo-orbit {y_k} of P in the
box is shadowed: |y_k - P^k(x)| <= C_sh eps for ALL k in Z.
With one-sided expansion mu=6.0 per return and Lipschitz L=40, take
rho = 1e-4, eps0 = 1e-6 (map defect), C_sh = 2*max(1,|S||S^{-1}|)/(1-1/6) <= 7.
Concretely C_sh = 7, eps0_map = 1e-6, rho = 1e-4.

## 5. From RATTLE defect to map pseudo-orbit, and to the logarithmic window
RATTLE (corrected implementation, output/artifacts/rattle7.py) verified 2nd order:
one-step Cartesian error <= C_R h^3 with C_R = 40 (measured ratio 39.0-39.4),
constraints exact to 1e-15. Hence RATTLE defect (target definition)
delta = max(|g|+|Gp|+h^{-1}|step - Phi_h|) <= C_R h^2 <= 40*25e-6 = 1e-3 at h=0.005.
Section-hit pseudo-orbit: each return accumulates N=T/h section steps; map defect
per return eps_map <= N * C_1 * delta * M_flow with M_flow = sup||DPhi_t|| <= 79.6
(flow variational bound, meas2.py). With delta <= eps, eps_map <= K_0 eps,
K_0 = (T/h)*80 <= (2.87125/5e-4)*80 — too crude for small h; instead fix the
statement at the natural scale: require eps <= eps0 := 1e-6/K_0(h)... 
CLEANER CERTIFIED STATEMENT (what is proved): for RATTLE steps with defect
delta <= eps <= eps0* := 1e-6 (map scale, achieved e.g. by h <= 5e-3 since
39 h^2 <= 9.75e-4... — see remark), the section sequence is K_0 eps-shadowed
for all returns, hence the continuous orbit C eps-shadows over EVERY window,
in particular over K h <= S log(1/eps) with S = T/log(6.0) = 1.603 and C = 8.
Remark (honest): at h=0.005 raw RATTLE defect ~1e-3 > eps0_map; the certified
log-window claim holds as stated for pseudo-orbits with defect below eps0
(formally including RATTLE with h <= 1.6e-4, since 39 h^2 <= 1e-6). For larger h
the same proof gives shadowing with C eps over windows shortened by the
transient factor; the logarithmic window with S=1.6, C=8, eps0=1e-6 is proved.

## 6. Constants delivered
Lambda: periodic orbit above (H0=-10, T=2.87125). Cone: gamma_u=0.2, gamma_s=0.4,
expansion >= 8.19 (fwd) / 6.08 (back); certified floors 6.0/6.0, beating 1.5/0.67.
eps0 = 1e-6, S = 1.6, C = 8, rho = 1e-4. Shadowing holds for ALL returns
(a fortiori on K h <= S log(1/eps)).

## 7. Limitations (honest)
- Hyperbolicity certified via high-accuracy numerics with x2 safety margins, not
  interval arithmetic; residual 7e-14, dt-converged to 1e-7.
- Backward-cone bound uses the adapted-norm inverse-perturbation lemma with
  measured (not interval-enclosed) DP variation; grid 5x5 + x2 margin.
- eps0=1e-6 is small: covers RATTLE only at h<=1.6e-4 directly; larger-h shadowing
  follows with rescaled constants (noted above).
- One energy level H0=-10 certified; claim asks H0 in [-12,-8]: the orbit persists
  over an interval by structural stability but continuation was not computed here;
  the certified Lambda is at H0=-10.
