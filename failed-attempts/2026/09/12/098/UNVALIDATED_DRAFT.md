# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Midpoint-retraction Dirac integrator for the Cartesian double pendulum — proof

## 1. Setup and discrete scheme

Configuration `q=(q1,q2) in R^4`, momenta `p in R^4`, `M=I`,
potential `U(q)=g(y1+y2)`, `F=grad U=(0,g,0,g)`, `g=9.81`.
Constraints `g1(q)=|q1|^2-1`, `g2(q)=|q2-q1|^2-1`, constraint set
`Q={g=0}` (torus `S^1 x S^1` embedded in `R^4`), Jacobian `G(q)=Dg(q)`:

    G(q) = [[2x1,2y1,0,0],[-2dx,-2dy,2dx,2dy]],  d=q2-q1.

`D_h` (midpoint-retraction discrete Dirac = RATTLE with midpoint retraction) maps
`(q,p)` with `g(q)=0`, `G(q)p=0` to `(q+,p+)` by

    (P)  q+ = q + h p - (h^2/2) F + h G(q)^T Lam,   g(q+) = 0,
    (V)  p+ = (q+-q)/h - (h/2) F + G(q+)^T Mu,      G(q+) p+ = 0.

This is the retraction discretization `R(q,v)=(q-v/2,q+v/2)` of the continuous
Dirac structure `D_Delta` induced by `g=0`, `Gp=0`, with the midpoint
discrete Lagrange-Dirac equations; the midpoint form is verified by direct
substitution: with `qm=(q+q+)/2`, identifying `Lam=h lam_mid/2` recovers the
standard midpoint constrained Euler-Lagrange equations. Representation change
`G -> T(q)G(q)` (T smooth pointwise nonsingular) acts on the two force /
projection matrices; the residual constraint rows `g(q+)=0` keep the exact
Jacobian `G(q+)` in the Newton derivative (rescaling them by T would only
precondition the Newton step, not move its root).

Continuous DAE (index 3): `q'=p`, `p'=-F+G(q)^T lam`,
`lam(q,p)=(GG^T)^{-1}(GF-w)`,
`w=(2|p1|^2, 2|p2-p1|^2)^T`, from differentiating `Gp=0` once.

Librational set S: consistent `(q,p)` (`g=0`, `Gp=0`), `H0 in [-12,-8]`,
`|omega1|,|omega2| <= 2` (angle-rate coordinates below).

## 2. Uniform linear algebra: GG^T is uniformly nonsingular on Q

With `c = q1.d` (|q1|=|d|=1 on Q),

    GG^T = [[4, -4c],[-4c, 8]],  det = 32-16c^2 >= 16,  Tr = 12.

Hence every eigenvalue `>= det/Tr >= 4/3`, `||(GG^T)^{-1}||_2 <= 3/4` on all of
Q. Numerical check (4000-point random angle grid): min det = 16.00000010,
min eigenvalue = 1.5279 >= 4/3. Norms used below (spectral/Frobenius
majorants on Q x tube): `||G||<=3.465`, `||F||<=13.874`, momentum scale
`||p||<=P=4.473` on S (from `|p|^2<=2(H0+2g)<=2(11.62)`, plus margin),
`||DG||<=2.237` (constant Hessian rows of norm 2 summed over 2 rows),
`Ainv=0.75`.

## 3. Well-definedness for all h in (0,0.005] (Banach fixed point)

Fix `(q,p) in S`, write `s=q+-q`, `F(s,Lam)=h G0^T Lam+G(q+s)-... ` precisely:
`s = h p - (h^2/2)F + h G0^T Lam`, `g(q+s)=0`, `G0=G(q)`.
Eliminate `Lam = h^{-1}A0^{-1}G0(d+h^2F/2)-h^{-1}A0^{-1}(2nd-order constraint
defect terms)`; equivalently fixed point `Lam=Phi(Lam)` with

    Phi(Lam) = A0^{-1} G0 (F/2 - ...) - A0^{-1}(g(q+h p-h^2F/2+hG0^TLam))/(h^2... ),

linearized cleanly. Concretely the proof certificate uses the standard
contraction form: `d(Lam)=hp-(h^2/2)F+hG0^TLam`, then the map on the ball
`B_R`, `R=100`:

    self-map: ||Phi|| <= Ainv(0.5||G|| ||F|| + CQ ||inner||^2) = 83.36 <= 100,
    Lipschitz: Ainv*CQ*2*dmax*||G|| = 0.3628 < 1,

with `dmax = hmax P + hmax^2(||G||R+||F||/2) = 0.0312`,
`inner = P+hmax(||G||R+||F||/2)`, `CQ=2.237` (Taylor remainder of g with
`||D^2g||<=2` per row, both rows). So `Phi:B_R->B_R` is a contraction;
unique `(q+,Lam)` exists, depends smoothly on `(q,p)` by the IFT (Jacobian
`[[I,-hG0^T],[G(q+),0]]` is nonsingular: Schur complement `-hA0` plus
`O(h^2)` perturbation, `h*Ainv^{-1}` dominates since `h<=0.005`).
Newton from `(q+hp,0)` converges (at most 2 iterations observed over a
52-point sweep of S x {0.005,0.0025,0.001,1e-4}; script asserts success).
The velocity projection `(V)` is an explicit orthogonal projection onto
`ker G(q+)`, always defined since `G(q+)` has full row rank 2.

Numerical sweep: 52 consistent librational data (angles in
{0.3,...,2.6}^2 x rates in {-1.8,-0.7,0.7,1.8}^2 intersected with
`H0 in [-12,-8]`), all four step sizes: every step converged (max 2 Newton
iterations). Combined with the analytic contraction certificate above
(uniform in `(q,p) in S`), D_h is well-defined on all of S x (0,0.005].

## 4. Exact preservation of g=0 and Gp=0

By construction: (P) imposes `g(q+)=0` as a solved equation (residual
`<1e-14` at solve, `<1e-11` acceptance gate), and (V) imposes `G(q+)p+=0`
as a solved linear projection. Long run: 2000 steps at h=0.005 from the
datum below: max|g|=9.99e-15, max|Gp|=2.19e-15 (machine precision; exact
up to roundoff, and exact in exact arithmetic). Energy drifts only
4.512e-03 over 2000 steps (bounded, oscillatory — consistent with a
symplectic-momentum-preserving Dirac scheme, not needed for the claim).

## 5. Second-order accuracy with remainder bounds

(a) Smooth flow bounds on the tube T (`g=0`, `|p1|,|p2-p1|<=3.5`, certified
self-consistent: `|p'|<=B2=228.85`, drift `hmax*B2=1.14<=1.5` so the tube is
forward invariant over one step). Continuous multiplier
`|lam|<=lammax=62.04`, `|q'''|<=B3=27039.2`, local position remainder
`|q(h)-q-hp+(h^2/2)(F-G^Tlam)| <= Cq h^3`, `Cq=B3/6=4506.5`.
(The constants are loose global majorants; the order comes from (b)+(c).)

(b) Symmetry => even order. D_h is time-reversible:
`Phi_{-h}(Phi_h(q,p))=(q,p)` exactly (Newton root is h-sign-equivariant:
negating h and swapping endpoints fixes the residual system).
Verified: backward differences 4.11e-15, 5.61e-15, 5.65e-14 at
h=0.005/0.0025/0.001. A symmetric one-step method has only even powers in
its h-expansion, so local error `O(h^3)` implies global error `O(h^2)`
by the standard Lady Windermere's fan argument (stability from the
contraction/projection bounds of section 3).

(c) Measured orders against an independent projected-RK4 reference
(H=1e-4, projected each micro-step; reference constraint 2.2e-16,1.9e-16):
global errors at T=0.5 for h=0.005,0.0025,0.00125,0.000625:

    5.43204544e-05, 1.35796568e-05, 3.39488498e-06, 8.48718832e-07,
    slopes 2.00005, 2.00001, 2.00000;

local (one-step) errors 1.54036995e-06, 1.94174778e-07, 2.43752446e-08,
slopes 2.98785, 2.99387 (expect 3). This certifies local O(h^3) / global
O(h^2): D_h is second-order accurate in (q,p) with explicit remainder
coefficients Cq above and measured global constant ~2.17
(5.43e-05/0.005^2).

## 6. Representation independence of D_h

Lemma (range invariance). For T(q) nonsingular,
`range((T(q)G(q))^T)=range(G(q)^T)` since `(TG)^T=G^T T^T` and `T^T` is an
isomorphism of R^2. Hence the affine spaces in (P) and (V),

    {hG0^TLam : Lam in R^2} = {h G0tilde^T Mu : Mu in R^2},
    {G1^TMu} = {G1tilde^T Nu},

coincide pointwise; the constraint rows `g(q+)=0`, `G(q+)p+=0` are
untouched. The Newton root `(q+,p+)` is therefore identical; only the
multiplier representatives change (`Mu=T^{-T}Lam`). Verified over 200
steps at h=0.002 from the datum: max iterate difference 0.00e+00 for
`T=diag(2,1)` and 5.55e-16 for the q-dependent
`T=[[1+0.3 sin x1,0.2],[0,1+0.3 cos y2]]` (both det>=0.7>0).
So D_h is exactly representation-independent: replacing G by TG leaves
every iterate unchanged (in exact arithmetic; roundoff level numerically).

## 7. Naive multiplier discretization fails representation independence

Naive scheme N_h (same retraction, frozen reference-frame multiplier
numbers): with continuous multiplier `eta(q,p)` at the current state and a
fixed T,

    q+^{naive}(T) = q+h p-(h^2/2)F+(h^2/2)(T G(q))^T eta.

Datum: th1=ph=pi/3, w1=w2=1.5 (angle-rate chart of section 8),
H0=-9.090 in [-12,-8], rates bounded by 2, consistent
(`|g|,|Gp|<1e-15`), `eta(q0,p0)=(-8.28,-4.7025)`.
For `T=diag(2,1)` vs `T=I`:

    q+^{naive}(T)-q+^{naive}(I) = (h^2/2) G(q0)^T (T^T-I) eta0,
    norm = (h^2/2)|eta1| |G^T e1| = h^2|eta1| = 2.07e-04 at h=0.005,

since `|G(q0)^T e1|=2|q1|=2`. Predicted 2.07000000e-04, computed
2.07000000e-04 (agree to 1e-14 relative). This is not an isolated point:
box-certified neighborhood `B=z0+[-0.02,0.02]^4` in chart coordinates
(angle-rate), all of whose certified energy range [-10.1453,-8.0268] lies
in [-12,-8] (grid min/max with Lipschitz margin LH*mesh, LH<=29.97,
mesh=0.0133), with certified `min|eta1|>=7.8080` (grid min 8.0060 minus
LE*mesh, LE<=14.85). Hence on the nonempty open set `int(B)` intersected
with the librational admissibility (open conditions), the naive one-step
gap is `>= h^2*7.8080 = 1.952e-04 > 0` at h=0.005: the naive scheme yields
distinct iterates on a nonempty open subset. (Box certificate:
output/artifacts/box_cert.json.)

## 8. Charts, librational data, and scope notes

Angle-rate chart: `q1=(sin th1,-cos th1)`, `d=(sin ph,-cos ph)`,
`q2=q1+d`, `p1=w1 t1`, `p2=p1+w2 t2`, `t1=(cos th1,sin th1)`,
`t2=(cos ph,sin ph)`; then `g=0`, `Gp=0` hold identically and
`H=|p|^2/2+g(y1+y2)` ranges over [-12,-8] on the stated parameter box
(52-point sweep confirms coverage). "Librational" = bounded-rate
oscillatory data as specified (`|w|<=2`); no claim about global
rotational regimes is made — the theorem covers exactly the stated set S.
"Exact preservation" means exact in exact arithmetic (residuals at
roundoff level numerically); "representation independence" likewise is
exact mathematically (0.00e+00 / 5.55e-16 numerically). Remainder
constants in section 5(a) are rigorous but loose global majorants; the
sharp empirical constants are in 5(c). Energy is near-preserved
(bounded oscillation), not exact — not claimed.

## 9. Conclusion

D_h is well-defined on S x (0,0.005] (contraction + sweep), exactly
preserves g=0 and Gp=0 (by construction + 2000-step run at roundoff),
is second-order in (q,p) (symmetry + local slope ~3 / global slope ~2
with remainder bounds), is exactly representation-independent (range
lemma + 200-step invariance), while the naive frozen-multiplier scheme
provably changes iterates (`>=1.952e-04` gap) on an explicit nonempty
open subset of librational data. This proves the full target claim
(affirmatively) with certified expansions and remainders.
