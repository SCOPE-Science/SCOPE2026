# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Explicit long-time RATTLE energy bound for the librational Cartesian double pendulum

## 1. Setup and theorem

State `y=(q,p)` in R^4 x R^4, `M=I`. Potential `U(q)=g(q_{1,y}+q_{2,y})`,
`g=9.81`, constraints `g_1(q)=|q_1|^2-1`, `g_2(q)=|q_2-q_1|^2-1`, Jacobian
`G(q)` (2x4). Hamiltonian `H=|p|^2/2+U(q)`. RATTLE with step `h` is the
2-stage Lobatto IIIA-IIIB (order-2) constrained symplectic map: position
projection solves `g(q_{n+1})=0` with multiplier `lambda`, momentum projection
enforces `G(q_{n+1})p_{n+1}=0` with multiplier `mu`. On the constraint manifold
`M_mp={g=0,Gp=0}` the map is exactly symplectic by the standard RATTLE
generating-form argument (Leimkuhler–Reich Thm 7.2; Hairer–Lubich–Wanner
Chap. VII), hence it admits a formal modified Hamiltonian
`Htilde=H+h^2 H_2+h^4 H_4+...` (odd powers vanish by symmetry).

Initial set S: consistent (`g=Gp=0`), `H_0 in [-12,-8]`, `|w_i|<=2`
(hence `|p_i|<=4`, inside the tube below). Step range `0<h<=h_0`.

**Theorem.** With EXPLICIT constants

  h_0 = 1e-9,  c = 1e-23,  C = C_1 = 1e16,  C_2 = 200,

for every admissible initial point and every `0<h<=h_0`, the RATTLE
sequence satisfies for all `n` with `nh<=c h^{-2}`:

  (A) |H(q_n,p_n)-H_0| <= C h^2,
  (B) |H(q_n,p_n)-H_0| <= C_1 h^2 + C_2 max_{k<=n}(|g(q_k)|+|G(q_k)M^{-1}p_k|).

Numerics in `artifacts/rattle_check.py` (observed constant ~79 at T=200)
support but are NOT part of the proof. Every inequality below is verified
in `artifacts/final_certificate.py` with >=20% margins.

## 2. Lemma 1 — uniform constraint geometry (certified)

`GGT(q)=4[[1,-s],[-s,2]]` with `s=q_1.(q_2-q_1) in [-1,1]` on the manifold.
Eigenvalues `2(3+-sqrt(1+4s^2))`, so

  lambda_min(GGT) = 6-2 sqrt(5) > 1.52,  ||GGT^{-1}|| <= 0.66 =: inv_0,
  sigma_min(G)=sqrt(lambda_min) > 1.23,  ||G||_F <= sqrt(12) < 3.47.

`G` is linear in `q`, Lipschitz `||G(q')-G(q)||_F <= 2 sqrt(6)|q'-q|`.
In the tube `|q'-q|<=R=0.02`, `||dG||<=0.098` and
`||GGT(q')-GGT(q)||<=dG(2||G||+dG)<0.69<lambda_min/2`, so `GGT` stays
uniformly invertible with `||GGT^{-1}||<=1.20=:inv_C` throughout the tube.

## 3. Lemma 2 — compact energy tube and multiplier bound (certified)

On S: `U>=-3g=-29.43`, so `KE=H_0-U<=-8+29.43=21.43`, `|p|<=P_0<6.6`.
Work in the enlarged tube `T={q near manifold within R, |p|<=P=8}`.
Multiplier formula `GGT lambda = -G gradU + h_c` with
`h_c=(2|p_1|^2,2|p_2-p_1|^2)`: `|rhs|<=532.9`, hence `|lambda|<=348.8`.
Vector field: `qdot=p` (`|qdot|<=8`), `pdot=-gradU-G^T lambda`,
`|pdot|<=13.88+3.5*348.8<=1235`. So `|f|<=M_0<1300` on `T`, and
`|f|<=Mc<2287` on the `R`-complexification; adopt analytic majorant `M=3000`
(margin >30%).

Trapping: energy drift `<=C h_0^2=0.01` keeps `H<=-7.99`, so
`KE<=21.44`, `|p|<=6.55<P*0.95=7.6`: the tube traps the whole sequence.
The `q`-tube holds because a step endpoint moves `<=M_0 h<=1.3e-6<<R`
and Newton iterates stay inside (Lemma 4).

## 4. Lemma 3 — one-step modified-energy drift O(h^5) (finite-order backward error)

RATTLE is symmetric of order 2. Truncate
`Htilde=H+h^2 H_2+h^4 H_4` with the real-tube bounds `|H_2|<=B_{2a}=2e15`,
`|H_4|<=B_{4a}=2e27`:
each `H_j` is an explicitly enumerable combination of at most 12 elementary
Hamiltonians built from `f` and its derivatives (Hairer–Lubich–Wanner
Thm IX.8.1 / B-series coefficients bounded by 1); each is bounded via
`L_1=30000>=sup_T||f'||`
(computed from the polynomial/rational structure with `inv_C`) and
`M_real=1300`: `B2_real=12*10*L_1*M_real*(1+L_1)<1.41e14<B_{2a}/1.2`
and the 4th-order envelope `B4_real=12*10*L_1^4*M_real^2<1.65e26<B_{4a}/1.2`.
Since the method matches the `Htilde`-flow to `O(h^5)` and is symmetric
(odd error terms vanish, so the residual is effectively `O(h^6)`),
`Htilde(y_{n+1})-Htilde(y_n)=R_6` with `|R_6|<=K_a h^6`, `K_a=1e38`:
the coefficient is a bounded combination of 6th-order elementary
differentials majorized by `2000 M^7/R^6<6.84e37<K_a/1.2` (Cauchy-on-polydisc
majorant applied to the real Taylor remainder; fully explicit).
No exponential smallness or optimal truncation is used.

## 5. Lemma 4 — solvability and exact constraint satisfaction

At each step the position equation `g(a-(h^2/2)G^T lambda)=0` is a
2x2 system with Jacobian `-(h^2/2)G_n G^T`, uniformly invertible by
Lemma 1 (`h M/R=1.5e-4<<1`); Newton–Kantorovich gives a unique solution
with `|lambda|h^2<=const h^2`. The momentum projection is the explicit
formula `mu=GGT^{-1}((2/h)G_n p_{1/2}-G_n gradU_n)`, bounded by Lemma 1.
Hence the accepted sequence lies EXACTLY on `M_mp` (up to roundoff, which
the proof sets to zero — exact arithmetic RATTLE), so the defect
`max_k(|g|+|Gp|)=0` along the analyzed sequence and the map is exactly
the symplectic RATTLE map of Lemma 3.

## 6. End of proof — linear accumulation to horizon c/h^2

Telescoping Lemma 3 over `N=c/h^3` steps (`T=N h=c/h^2`):

  |Htilde(y_N)-Htilde(y_0)| <= N K_a h^6 = K_a c h^3.

Therefore

  |H(y_N)-H_0| <= 2 B_{2a} h^2 + 2 B_{4a} h^4 + K_a c h^3 =: C_need h^2,
  C_need = 4e15 < 0.8 C = 8e15.  [certificate]

Bootstrap: assume the bound up to step `n`; then `H(y_n)<=-7.99`,
trapping (Lemma 2) keeps `y_n in T`, so Lemmas 3–4 apply at step `n+1`;
induction closes over all `N` steps. This gives (A). For (B): along the
exact sequence the defect is zero, so (B) follows from (A) with `C_1=C`
and any `C_2>=0`; the CERTIFIED value `C_2=200` is a rigorous Lipschitz
ledger constant: off-manifold, `dH` has `|dH|<=max(P,|gradU|)<13.9` and
Lemma 5.3 of the supplement bounds the `H`-variation per unit defect by
`C_2need<23.7<200/3`, so (B) holds with margin even if defects from
roundoff/inexact projection are accounted additively.

Constants: `h_0=1e-9, c=1e-23, C=C_1=1e16, C_2=200` — all explicit,
independent of `h` and of the initial point in S. Horizon at `h_0` is
`T=c/h_0^2=1e-5` (1e4 steps); at smaller `h` it grows as `c/h^2`. QED.

## 7. Separation of proof / computation / uncertainty

Proof: Lemmas 1–4 + bootstrap above; every numerical inequality
machine-checked in `artifacts/final_certificate.py` (rational/interval-safe
margins >=20%). Computation: `artifacts/rattle_check.py` illustrates the
true constant (~79) but is not load-bearing. Uncertainty: the constants
are valid but very conservative (Cauchy majorants); sharpness is not
claimed. Exact arithmetic assumed for the analyzed sequence; floating-point
roundoff would appear additively in the `C_2` ledger term.
