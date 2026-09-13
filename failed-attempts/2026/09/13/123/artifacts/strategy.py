"""High-precision recomputation with mpmath (dps=80): rebuild DP values and I,J in
mpmath, then Rayleigh quotient of candidate + power iteration for true max.
To keep runtime sane, reuse float transition STRUCTURE but evaluate in mpmath only
the needed (h,r) values bottom-up. 1.6M states x avg branching(~25?) in Python/mpmath
is too slow. Better: recompute in EXACT rational arithmetic the QUADRATIC FORMS
num=c'Jc, den=c'Ic for a ROUNDED candidate vector c (small integers): only need
v50[g] for g in span of support (97x97 pairs -> but support small if we round c to
few dominant components) and v49 entries for J. Exact via Fractions with Beta as
Fraction(A! r!/(A+r+1)!): factorials small (<= ~70). Feasible: per (h,r) state exact
value as Fraction; but full 1.6M states exact = heavy. Instead DIRECT formula:
V entries via Dirichlet sums: int_{Dx_k} Q^h u^r = coefficient extraction:
Q^h u^r with u=1-S: expand u^r = sum_b C(r,b)(-S)^b... still messy.
Cleanest exact route: t-monomial expansion! Each power-sum monomial Q_e = prod_j (sum_i t_i^j)^{e_j}
expands into t-monomials; integrals are Dirichlet (factorials). Number of t-monomials per Q_e
at k=50: huge (50^9). NOT feasible directly.
Alternative: symmetric reduction — power sums -> monomial symmetric functions m_lambda^{(k)};
integrals of m_lambda over Dx_k(1) have closed forms via fattorizations... still complex.
PRAGMATIC rigorous path: (a) float max ~3.4-3.6 with shaky tail; (b) for the CERTIFICATE,
prove upper bound <4 via exact arithmetic on 4I-J with entries computed EXACTLY as Fractions
through the DP (only needed states: 1.6M — each a Fraction with big numerator/denominator;
Python Fractions 1.6M states x 25-branch sums = maybe 10-30 min. Risky but let's estimate size first).
Cheaper rigorous alternative: interval arithmetic (mpmath iv?) — not available. Implement simple
[lo,hi] interval DP in float (directed rounding via numpy nextafter scaling): overestimation factor
per level tiny; 50 levels fine. Then interval I,J -> interval certificate 4I-J PSD?
Interval PSD check: sufficient condition via Gershgorin on interval matrix: need
underline(diag) > sum overline(|offdiag|) per row — usually FAILS for dense Gram matrices.
Better: compute approximate LDL (float) of A=4I-J, then RIGOROUSLY verify via interval residual:
find float L,D with D>0, compute interval E = A - LDL', bound ||E||_2 <= eps, and min(D) - eps'>0...
Standard verify: if A - LDL' interval has small entries and DDiag min > rowsum(E), PSD holds.
Fejér-style: A = LDL' + E with |E_ij|<=e: A PSD if D_min * ... hmm need L nonsingular accounting.
Simplest classical certificate: INT-CHOLESKY: run Cholesky with intervals; if all pivots stay >0
with rigorous rounding control, A is PSD. Implement careful interval Cholesky with outward rounding
using float + explicit error bounds (Higham-style): do float Cholesky of scaled A; a posteriori bound
via ||A-LL'||_F <= c*u*||A||-ish is circular (assumes success) — but there is a rigorous theorem:
if computed L satisfies ||A-LL'|| small RELATIVE to min pivot growth... Use the Demmel/Kahan style?
TIME CHECK: this is getting deep. Given one-hour lane, better plan:
- The float evidence says max in [3.3, 3.6]-ish, needs <4 certificate.
- FAST rigorous upper bound: restrict-negation is wrong direction... we need GLOBAL upper bound.
- Alternative: exact PSD via sympy? 97x97 Fractions Cholesky: entries are rationals with denominators
dividing 70!-ish (astronomical). Cholesky Fractions will blow up. Use scaled INTEGER matrix:
multiply A by L=lcm... entries ~1e-65 scale; scale by 1e0/s0 first (float, inexact) — breaks exactness.
Hmm: exactness requires exact I,J entries as Fractions. DP with Fractions: denominators divide products
of (A+r+1) and Beta denominators: (A+r+1)!/(A!r!): values like p/50!-ish with 1.6M states; each Fraction
op = big-int gcd. Est: intermediates have ~100-300 digit numbers; 40M ops -> way too slow in Python.
REDESIGN: choose SMALLER but rigorous certificate:
Observe J-identity: M(F) = k J_1/I. Try analytic upper bound: J_1(F) <= C * I(F) with C from Cauchy-Schwarz
along fibers: (int_0^u F dt_m)^2 <= u * int_0^u F^2 dt_m. So J_m <= int_{R^{(m)}} u * int_0^u F^2 = int_R (1-S+t_m) F^2.
Sum over m: sum_m J_m <= int_R (k(1-S) + S) F^2 = int_R (k - (k-1)S) F^2 <= k*I(F) (since S>=0)!
So M <= k = 50. Useless alone (need 4).
Sharpen: weight (1-S+t_m) is small where F^2 concentrates? For UPPER bound need reverse: F^2 could
concentrate at S~0 where weight ~k=50?? That gives M up to 50?? But float says 3.4. The fiber-CS bound is loose.
Alternative analytic: expand in symmetric basis, bound each J_1 entry vs I entries? Meh.
DIFFERENT rigorous certificate idea — EXACT arithmetic in a SMALLER exact ring:
Note all DP operations are +-*/ on rationals starting from integers (C, Beta with factorial ratios).
Use modulular/exact via Python integers with a SINGLE common denominator per level? Denominators divide
D_k = lcm stuff... could use np exact with dtype object ints but same cost.
Actually, reconsider cost: needed states 1.6M is for WMAX=18 FULL + r<=~68. But I,J only need:
I: v50[(g,0)] for g=e_i+e_j (W<=18): 1410-dim DP... bottom-up needed from these: children (f,A+1) with r=A+1<=19:
need[k] for k<50 = {(f,r): r<=19ish, W(f)+r<=19}: MUCH smaller! The 1.6M came from ALSO seeding need[49] with
r=2..20 for ALL h (for J). J needs v49[(h,s)] for h=f+g of SUBTERMS (W<=18) and s=a+b+2<=20: same reduced set!
Wait — need[49] seeds: (h,s) for h with W<=18 (1410 of them) x s in 2..20 (19 values) = 27k seeds, each spawning
children. Total 1.6M. Exact Fractions on 1.6M states: each state = sum over subs (avg ~25 terms) of c*beta*child:
~40M Fraction mults/adds. Each with ~50-200-digit ints: ~microseconds*10 each -> 400-4000s. Too slow for lane.
Better: REDUCE basis first! Float shows top vector concentrated; but upper bound needs ALL 97.
Hmm, but do we need WMAX=18 for J? J entries: h=f+g where f,g are SUBTERMS of basis elements: W(f)<=9 each so
W(h)<=18 yes. r=a+b+2<=20. OK.
PIVOT to interval arithmetic in FLOAT (fast, vectorized) + interval-Cholesky certificate attempt:
- Redo DP bottom-up with numpy float intervals [lo,hi] (2 arrays per r... memory: needed sets as dict; vectorize
by (h,r) index arrays). Outward rounding: multiply bounds by (1+2^-52 *slack) each op — use Higham gamma_n style
global bound instead: track relative error symbolically! DP is all POSITIVE additions/multiplications (no cancellation):
relative error per level <= (1+u)^{ops} — clean forward bound. All DP values have small RELATIVE error (no subtraction
anywhere in values!). I,J entries likewise (positive sums). So I,J known to high RELATIVE accuracy (~1e-13?).
- Then A=4I-J has CANCELLATION (subtraction!) — relative bounds blow up, but ABSOLUTE bounds: |A-tildeA| entrywise
<= small absolute (since I,J entries ~1e-65, errors ~1e-78). Then rigorous PSD: Gershgorin won't work (dense),
but LDL' residual method: float-Cholesky A_tilde... A_tilde itself: is 4I-J even PSD in float? Its min eigenvalue:
4-3.6=0.4 gap scaled... A/s0 has min eig ~ (4-3.44)*lambda_min-ish... fine, Cholesky should succeed; then verify
A - L L' small in norm + min pivot argument via standard a-posteriori theorem (e.g., Rump/Wiedlandt: if
||I - L^{-1} A L^{-T}|| < 1-ish... needs inversion bounds).
Simplest implementable rigorous PSD test: exact-ish LDL with Fractions on the SCALED matrix? entries ~O(1) rationals
with huge denominators — still big-int blowup, but only 97x97=9409 entries; LDL Fractions O(n^3)=1M Fraction ops on
numbers GROWING exponentially (bits double per step -> thousands of digits). Estimated slow (minutes-tens of minutes)
but maybe OK?? Risky.
ALTERNATIVE certificate avoiding PSD entirely: UPPER-bound M via TRACE/REGRESSION-free analytic bound per basis vector?
M <= sum over... no, Rayleigh max <= max row sum ratio? M <= max_i (sum_j |J_ij| v_j)/(sum_j I_ij v_j)... 
Johansson-style: M <= max generalized eigenvalue <= ||I^{-1}|| ||J||: computable rigorous upper bounds on NORMS via
interval arithmetic (no cancellation! norms of I,J separately: ||J||_F and ||I^{-1}|| via min-eig lower bound of I...
min-eig of I needs PSD-type certificate again. Circular.
PRAGMATIC DECISION: implement (1) mpmath 50-digit verification of the TOP Rayleigh quotient (<4, rigorous up to
controlled precision — present as high-precision evidence, honest about certification level); (2) attempt interval-DP +
Rump-style PSD certificate for 4I-J; if it closes, full proof; else report best justified route.
Actually WAIT — much better certificate idea: DIRECT SOS/SDP-free upper bound via COMPLETING THE SQUARE in exact arithmetic
on a COARSE subspace + analytic tail? Still complex.
EVEN SIMPLER rigorous upper bound: M = max_c c'Jc/c'Ic <= max_c c'Jc/c'Dc * max_c c'Dc/c'Ic for D=diag(I):
= (max generalized eig of (J,D)) * (max eig of (D,I))... second factor = max over... c'Dc/c'Ic <= max_{ij} ... 
c'Dc/c'Ic for PSD I: = lambda_max(D^{1/2} I^{-1} D^{1/2}) — again needs I^{-1}. no.
Let me just try: float LDL of A=4I-J succeeds? then interval residual certificate. GO.
"""
print("strategy noted")
