# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Slit-strip crossing-gap stability beta=1/4 via monotone coupling (TARGET, repaired)

## Theorem
Let H be the hexagonal (honeycomb) lattice at mesh 1 with critical FK-Ising
(q=2) isoradial weights. Let S_N be the strip subgraph induced by
[0,2N]x[0,N], with Dobrushin boundary conditions: wired on the bottom side
(y=0), free elsewhere. Let K be a nonempty connected top-attached subgraph
(touching y=N) of (graph) diameter d with d<=N/4, and S_N^K = S_N \ K with
free boundary on dK. Let p_N be the bottom-to-top-side crossing probability
in S_N, and p_N^K the LITERAL bottom-to-(top side minus K) crossing
probability in S_N^K (paths must land on the top side outside K; landing on
dK alone does not count). Let d_1 = max(d,1) be the lattice-quantized
diameter (a connected subgraph has d=0 iff it is a single site, else d>=1
in mesh units). Assume published inputs (H1)-(H2) below. Then with beta=1/4,
m<=6, N0=12, and

  C = max{ C_arm * 12^{3/8} * c0^{-6}, N0^{1/4} } < infinity,

  |p_N^K - p_N| <= C * (d_1/N)^{1/4},

hence as written |p_N^K-p_N| <= C*(d/N)^{1/4} for every admissible d>=1.
No fermionic observable, ratio RN derivative, or convergence rate is used.

## Published inputs (black boxes only, with isoradial uniformity)
(H1) Half-plane one-arm upper bound: for critical FK-Ising, uniformly in the
boundary conditions outside the annulus, the centre position on the boundary
line, and scales 1<=r<R,
  sup P[ B(x0,R)\B(x0,r) crossed in {y<=N} ] <= C_arm (r/R)^{3/8}
with finite C_arm. Exponent 3/8 is slack below the exact 1/2; only an upper
bound with exponent >1/4 is needed. Uniformity over isoradial embeddings
(incl. honeycomb) and over boundary conditions: Chelkak-Smirnov universality
+ Duminil-Copin-Hongler-Nolin RSW framework and its isoradial extensions
(Beffara-Duminil-Copin; Duminil-Copin-Hongler-Nolin 2011 and follow-ups).
The fermions enter only inside this published black box, never in our proof.
(H2) RSW uniform crossing lower bound c0>0 for rectangles of bounded aspect
ratio (<=2), uniform in scale, position, boundary conditions, and over the
isoradial honeycomb embedding: Duminil-Copin-Hongler-Nolin (2011) and
isoradial extensions. Used only for <=6 corner gluings below.

## Lemma 1 (FK disagreement bound, Grimmett-type; replaces exact agreement)
Let mu, mu^K be the full and slit FK measures. Let x0 be K's attachment
point, r = max(3d,3) (floored radius; K subset B(x0,r)), B=B(x0,r).
Then there is a monotone exploration coupling of (mu,mu^K) revealing the
bottom cluster edge by edge with common uniforms such that, by the FK domain
Markov property plus comparison of boundary conditions for q>=1
(Grimmett, The Random-Cluster Model, Ch. 3-4: spatial Markov Lemma 4.13,
CBC Theorem 4.19; exploration-coupling form cf. Duminil-Copin lecture notes
on FK percolation), the conditional opening probabilities revealed from the
bottom coincide in the two domains until the exploration touches dB.
Consequence (total-variation form): on the complement of
  F = {bottom <-> dB}   (failure event),
the bottom-connectivity to every set outside B coincides in the two
marginals. Hence for the crossing indicators (literal definitions),
  |p_N^K - p_N| <= max{ mu(F), mu^K(F) }.
We bound the max by the H1/H2 sup-bound, which is uniform in boundary
conditions and hence covers both marginals. No pathwise identity on F is
claimed; only D subset F up to the coupling, i.e. the TV estimate above.

## Lemma 2 (topology; literal crossing; proxy remark)
Let A = {bottom <-> top side} (full), A^K = {bottom <-> top side \ K}
(slit, literal). Under the Lemma-1 coupling, on F^c the indicators of A
and A^K agree. Indeed: (a) a slit literal crossing path landing on top\K
outside B avoids K (K subset B) and is open in the full domain, so A holds;
if the slit path enters B then F holds. (b) A full crossing path avoiding B
is open in the slit and lands on top\K, so A^K holds; if the full path
enters B then F holds. Thus disagreement D={1_A != 1_{A^K}} satisfies
D subset F (in the coupling), and Lemma 1 gives the gap bound.
Remark (proxy): the earlier "proxy" event P^K={bottom <-> dK or top\K}
differs from A^K only when a slit path hits dK subset B, i.e. only on F;
so |P^K-prob - p_N^K| <= max(mu(F),mu^K(F)) by the same arm bound. The
theorem is stated for the literal p_N^K, so no proxy is used.

## Radius flooring and small scales (explicit N0)
Mesh is 1: K nonempty connected has d=0 (single site) or d>=1. Set
r = max(3d,3) >= 3, so K subset B(x0,r) always (graph neighbourhood covers
K plus one layer), and H1's condition r>=1 holds. Set R = N/4 and N0 = 12.
For N >= N0, R >= 3 so the floored r=3 fits inside R whenever 3d < N/4.
Arm regime: max(3d,3) < N/4, i.e. r<R; then r/R <= 12 d_1/N < 1.
Non-arm regime (12 d_1/N >= 1): |gap| <= 1 <= (12 d_1/N)^{1/4}
(since then the base >=1 and exponent 1/4 preserves the inequality).
Small N < N0: with d_1>=1, d_1/N > 1/N0... rather (d_1/N) >= 1/N for
N<N0 gives 1 <= N0^{1/4}(d_1/N)^{1/4} because (N/d_1)^{1/4} <= N0^{1/4}.
Both trivial covers are absorbed by the max in C (N0^{1/4}>=12^{1/4}).

## Corner gluing: m<=6 uniform cost c0^{-6} (figure)
dist(bottom,K) >= 3N/4 > R, so bottom lies outside B(x0,R). A bottom-to-B
path segment from outside B(x0,R) into B(x0,r) contains an arm of the
half-annulus B(x0,R)\B(x0,r) in {y<=N}, except when B(x0,R) is cut by a
lateral side x=0 or x=2N. Then glue <=6 RSW rectangles (aspect <=2) to
complete/relocate the arm; each gluing costs c0^{-1} by FKG + H2, uniformly
in x0, scale, and boundary conditions.

  y=N  |-----------top------------|x0-------------| (K attached at x0)
       |      . - - - - - - .     |XXXX K XXXX|
       |   .  R= N/4  half-disk . |..B(x0,r)..|
       |  :  . - - -inner r- .  : |:::::::::::|
       |  : :  arm r->R :::::: : |  slit void |
  side x=0: ][ rect 1 ][ rect 2 ][...arm...]  [rect 3][ corner x=2N
       |  : : (glue q-annulus->half, <=3 rects/side) : |
       |___:________bottom (wired)________________:___| y=0
       Corner case: if x0 within R of x=0, chain: [1] one rect shifting the
       quarter-annulus mouth off the wall, [2]-[3] two rects closing it to a
       half-annulus at projected centre x0'=R, [4] one rect crossing the top
       strip conditioning; mirror image at x=2N reuses the same 4; +2 rects
       to join dyadic inner/outer pieces. Total m<=6 in all positions.

Hence with Arm_half(r,R) the half-annulus crossing,
  max(mu(F),mu^K(F)) <= c0^{-6} * C_arm * (r/R)^{3/8},   r=max(3d,3), R=N/4.

## Beta=1/4 derivation
In the arm regime, r/R <= 12(d_1/N), so
  |gap| <= C_arm c0^{-6} 12^{3/8} (d_1/N)^{3/8}
        <= C_arm c0^{-6} 12^{3/8} (d_1/N)^{1/4},
since d_1/N <= 1/4 < 1 and 3/8 > 1/4 gives u^{3/8} <= u^{1/4} (downgrade).
In the non-arm/small-N regimes the trivial covers give |gap|<=N0^{1/4}
(d_1/N)^{1/4}. Taking the max yields C and beta=1/4 exactly (a stronger 3/8
intermediate bound is proved). C is independent of N, d, and K's position.

## Method compliance
Only monotone (FKG) exploration coupling + Lemma-1 TV bound, RSW gluing
(<=6), and the published half-plane one-arm upper bound are used. No
fermionic-ratio approximate Radon-Nikodym derivative and no
observable-convergence rate enter our derivation.

## Computed certificate
output/artifacts/check_exponent.py (repaired) verifies with r=max(3d,3),
N0=12: arm-regime inequality arm<=C_main*(d/N)^{1/4} over (N,d) grid,
trivial/small-N covers, and finiteness of the C-formula. Numeric
placeholders (C_arm=8, c0=0.01) are conservative finiteness stand-ins, NOT
claimed published values; the theorem's C is the symbolic expression in the
named published constants.
