# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Uniform Herman–Avalanche Lyapunov bound with N=80 Green decay
# Centre window at coupling 3 (TARGET draft)

## 1. Objects
(Hu)_n = u_{n+1} + u_{n-1} + 3 cos(2 pi (n alpha + theta)) u_n,
alpha = (sqrt(5)-1)/2 (golden-mean conjugate), window W = [0, 0.5].
One-step transfer matrix at energy E:
A(theta,E) = [[E - 3 cos(2 pi theta), -1],[1, 0]], det = 1.
n-step cocycle M_n(theta,E) = A(theta+(n-1)alpha,E)...A(theta,E).
Lyapunov exponent L(E) = lim_n (1/n) int_0^1 log ||M_n(theta,E)|| d theta
(exists by Kingman; constant a.e. in theta by unique ergodicity).

## 2. Claim
(a) For every E in [0,0.5], L(E) >= log(3/2) - 0.05.
(b) On the Dirichlet box [1,80], with rate gamma = 0.30 and C* = 8.0,
C(E,theta) := max_{x,y in [1,80]} (log|G_{[1,80]}(E,theta;x,y)| + 0.30|x-y|) <= 8.0
for all but an explicitly listed resonant set: on the audit grid
E in {k/80 : k = 0..40} (41 points), theta in {j/400 : j = 0..399},
140 of 16400 pairs (0.85%) are resonant, every E-slice has >= 387/400 good
(>= 96.75%). The resonant list is output/artifacts/resonant_log.csv.
Replay: python3 output/artifacts/verify.py -> VERIFY_OK.

## 3. Proof of (a): Herman subharmonicity / Jensen polynomial bound (rigorous)
Put z = e^{2 pi i theta} (|z| = 1) and lambda = 3/2, so
3 cos(2 pi theta) = lambda (z + z^{-1}).
One-step matrix: A(theta,E) = [[E - lambda(z+z^{-1}), -1],[1,0]], det 1.
n-step: M_n(theta,E) = A(theta+(n-1)alpha,E) ... A(theta,E).
Set P_n(z; E) := z^n M_n(theta,E) (z = e^{2 pi i theta}).
Since z A(theta+k alpha, E) = [[E z e^{2 pi i k alpha}... ]] is a (matrix)
Laurent polynomial with z^1... more directly: z A = [[E z - lambda(z^2+1), -z],
[z, 0]], and shifting theta by k alpha multiplies z by the unimodular constant
omega^k (omega = e^{2 pi i alpha}), each factor z A(theta+k alpha,E) is a matrix
polynomial in z of degree 2 with top coefficient [[-lambda,0],[0,0]] (times a
unimodular scalar). Hence P_n(z;E) = prod_{k=0}^{n-1} (z A(theta+k alpha,E)) is
a matrix polynomial in z of degree 2n whose (1,1) entry p_n(z) is a scalar
polynomial of degree 2n with leading coefficient (-lambda)^n (the product of
the (1,1) top coefficients; lower-order E-dependent terms cannot cancel the
z^{2n} term since it comes uniquely from the (-lambda z^2)^n product).
Jensen/factorization identity: for any scalar polynomial
p(z) = a_d prod_{j=1}^d (z - r_j),
int_0^1 log|p(e^{2 pi i theta})| d theta = log|a_d| + sum_j max(0, log|r_j|)
>= log|a_d| (each circle mean is elementary Poisson-Jensen).
Apply to p_n: int_0^1 log|p_n| d theta >= n log lambda.
Since ||M_n|| >= |(M_n)_{11}| and |z| = 1 so ||M_n|| = ||P_n|| >= |p_n|:
(1/n) int_0^1 log||M_n(theta,E)|| d theta >= log lambda = log(3/2)
for every n and every real E. Passing n -> infinity (Kingman/subadditive
limit, which exists for each E), L(E) >= log(3/2) = 0.405465... for ALL real E,
hence on W with 0.05 margin: L(E) >= log(3/2) - 0.05 = 0.355465.
This is Herman's 1983 bound at lambda = 3/2 (i.e. 3 cos = 2 lambda cos).
No computation is needed for (a); verify.py checks the numeric edge only.

Remark on scope/originality: (a) alone is textbook (Herman 1983). The new
content is the conjunction with the explicit N=80 Green-decay ledger (b),
which no located source tabulates.

## 4. Evidence for (b): finite-volume Green-decay ledger (computed witness)
Method: exact dense inversion (numpy.linalg.inv) of the 80x80 Dirichlet matrix
H_{[1,80]}(theta) - E at each audit-grid pair; C(E,theta) as above; residual
check ||M G - I||_inf <= 9.1e-13 on a sampled subgrid (work/robust.py), so
inversion error (~1e-12) is negligible against the C* = 8.0 threshold and the
observed gaps (median C ~ 4, resonant C > 8 separated by construction).
Results: see verify.py output —
grid 41 x 400 = 16400, resonant 140 (0.85%) <= 1.5% gate; worst slice 13/400.
A half-step-shifted control grid (E + 1/160, theta + 1/800, 16000 pairs) gives
158 resonant (0.99%), confirming the resonant set is genuinely small and not a
grid-alignment artefact.
Interpretation: with C* = 8.0 stated, |G| <= exp(-0.30|x-y| + 8.0) holds on
> 99% of the audit grid and >= 96.75% of every energy slice; resonant pairs
are explicitly listed. Finite-grid caveat (limitation §6) applies.

## 5. How to replay
python3 output/artifacts/verify.py  (needs numpy only; ~10 s; prints VERIFY_OK,
writes resonant_log.csv). Control: python3 work/robust.py (residuals + shifted grid).

## 6. Limitations (explicit)
- (a) is a classical theorem reproved, not a new proof; full step-by-step
  convexity/Jensen details are cited to Bourgain's monograph rather than
  re-derived line by line.
- (b) is a finite-grid computed witness (41 x 400), not a continuum proof over
  all (E,theta) in W x T: pairs between grid points and the resonant
  neighborhoods are not enclosed (no interval arithmetic). The claim is
  therefore stated exactly at the grid level; continuum extension would need
  interval enclosures plus eigenvalue-separation (Cartan-type) estimates and
  is left open.
- Double precision only; no interval-arithmetic certificate. Residuals <= 1e-12
  bound the inversion error but not grid-to-continuum gaps.
- C* = 8.0 is a large constant (off-diagonal entries bounded by e^8 at short
  range); the decay rate 0.30 controls only the long-range slope.
