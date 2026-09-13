"""Key structural fact: I is numerically rank-deficient (rank ~55-68 of 97)!
Why? Power-sum monomials with total degree<=9 at k=50: are there EXACT linear dependencies?
p_j for j>=1: no algebraic relation at k=50 (need k+1 vars for Newton identities... relations among
p_1..p_9 as functions on R^50: none of degree<=9? Newton: e_{10} expressed via p_1..p_10 — but that's
e, not a relation among p's. Power sums p_1..p_50 algebraically independent; p_1..p_9 certainly
independent as POLYNOMIALS. So I should be EXACTLY PD. Tiny eigenvalues (~1e-13 scaled) = genuine
near-degeneracy: high-degree power-sum monomials (e.g., p_9 vs p_1^9-ish combos?) nearly collinear
on the simplex? Hmm, or is small-k... The scaled min-eig -2.6e-13 ~ rounding level: TRUE min eig could be
small-positive (like 1e-14?) — ill-conditioned but PD. That kills Cholesky certificate for 4I-J AND
casts doubt on float max (3.44 vs 3.6 across thresholds: the top modes live in the ill-conditioned tail!).
DANGER: the 'top' eigenvalue may be a numerical artifact of dividing by near-zero I-modes. The TRUE max
might be much lower (or higher?). Need reliable computation: work in EXACT arithmetic or high precision.
Options: mpmath high-precision full pipeline (DP 1.6M states at dps=50: SLOW in Python, maybe 10+ min per run;
but vectorizable? mpmath doesn't vectorize. Use numpy longdouble? not supported for linalg; but DP itself
in longdouble (float128, 64-bit mantissa) IS supported elementwise! Redo DP bottom-up in float128: values get
~1e-19 rel accuracy; then I,J in float128; then eigensolve... linalg lacks float128. Hmm.
Alternative: REDUCE basis to well-conditioned subset: drop near-dependent monomials. The max over a subspace is a
LOWER bound (fine for existence, but we need UPPER bound <4 — restriction gives wrong direction!).
For upper bound with singular-ish I: M <= lambda means J - lambda I <= 0 (PSD). Equivalent: for all c.
Since I PD (exactly), fine in theory; numerics need care.
BETTER IDEA — change basis to well-conditioned one: use ORTHOGONAL-ish symmetric polynomials? E.g., basis of
monomial symmetric functions m_lambda or Schur, still ill-conditioned on simplex?
Hmm. Actually reconsider: is I REALLY PD exactly? Basis = {Q_e : W(e)<=9}, Q_e = prod p_j^{e_j} as functions on
R^50 restricted to simplex Dx_50(1). Polynomial identity: if sum c_e Q_e = 0 on open set, then as formal polynomial
sum c_e prod P_j^{e_j} = 0 where P_j = sum t_i^j. Since P_1..P_9 algebraically independent (subset of independent
P_1..P_50), all c_e=0. YES exactly independent => I exactly PD. True min-eig > 0 but possibly tiny.
STRATEGY for rigorous UPPER bound avoiding ill-conditioning: prove J <= 4I - DELTA via SUM-OF-SQUARES-free
analytic argument? OR: exact arithmetic ONLY on the ill-conditioned tail complement...
PRAGMATIC ALTERNATIVE: pick a well-conditioned SUB-basis (e.g., total degree <= 5? dim smaller) for a clean
certified upper bound on THAT subspace (lower-dim, Cholesky works), PLUS bound the tail contribution analytically?
Tail bound: M(full) <= max(M(sub), ...) no clean decomposition.
COMPLETELY DIFFERENT, ROBUST PLAN: bound M(F) analytically for ALL symmetric deg<=9 F:
M(F) = 50 J_1/I. Write F in t_1-fiber form and apply Cauchy-Schwarz with OPTIMAL fiber weight?
J_1 = int (int_0^u F)^2 <= int [int_0^u F^2 w / int w ...]. Equality-optimizing gives back eigenvalue problem. no.
Hmm, what about a direct pointwise-to-integral bound: (int_0^u F(t_1) dt_1)^2 <= (int_0^u F^2 dt_1) * u.
So J_1 <= int_{Dx} u F^2 where u=1-S' (S' = sum_{i>=2}). Then M <= 50 * int uF^2/int F^2 <= 50*max(u)=50. weak.
Weighted: (int F)^2 = (int F v^{1/2} v^{-1/2})^2 <= (int F^2 v)(int v^{-1}). Choose v(t_1) to minimize ratio
globally... For upper bound valid for our CLASS, take v = u - t_1 (tent): int_0^u v^{-1} = infty. no.
OK here's another thought — REDUCE k EFFECTIVELY: symmetric F of degree<=9 in 50 vars: dep on power sums.
I and J entries are RATIONAL functions of k (k=50): each entry = (poly in k)/(k+..)! style. Could compute
exact rationals via k-SYMBOLIC DP? Same cost.
COST REALITY CHECK for exact Fractions DP on 1.6M states: actually values at level k have denominators dividing
(k + stuff)!-ish; numerators big. Let me just TIME a single-state exact eval + extrapolate. Also alternative:
exact via longdouble DP (fast, vectorized) + RATIONAL reconstruction? no.
Actually, BEST PRACTICAL RIGOROUS ROUTE: mpmath dps=80 DP but VECTORIZED differently — the DP transitions are
linear: v_k = T_k v_{k-1} with sparse T_k (40k nnz). 50 levels x 20 r-values... the needed-set dict version did 1.6M
states in ~2 min float. In mpmath scalar Python: 1.6M states x ~25 subs = 40M mpmath ops ~ 1-2 HOURS. Too slow.
BUT we don't need all 1.6M for an UPPER bound on a REDUCED basis... circular again.
RESOLUTION: use Fractions but ONLY for the 97x97 I,J entries via MEMOIZED recursion (each entry triggers needed
children; total distinct still 1.6M). Same cost. Hmm.
WAIT — much better: FLINT-style exact via integers mod PRIMES + reconstruction? Overkill.
SIMPLEST SOUND MOVE given lane clock: the float max is ~3.3-3.6, well below 4, but certification is blocked by
ill-conditioning. Consider REDUCED DEGREE certificate: deg<=9 contains deg<=d subspaces. If I certify (rigorously,
well-conditioned) that max over deg<=9 RESTRICTED... no, need full.
Hmm, actually, let me reconsider the conditioning: scaled-Is min eig -2.9e-13 with 29 eigs <1e-12. What if TRUE
min-eig is like 1e-16 and the top generalized eig is HUGE (like >4) carried by tail modes, with float just misfiring?
Must check with higher precision eigensolve: implement power/generalized iteration in float128 for the DP + use
mpmath ONLY for the 97x97 generalized EVP (cheap! eigh on 97x97 in mpmath = fast). The expensive part is DP (1.6M),
but float128 DP via numpy vectorization is FAST (same speed ~2-4 min). Then mpmath 80-digit generalized eigensolve
on 97x97 (trivial cost). The DP rel-error ~1e-18 (float128) >> needed to resolve min-eig 1e-14? Values accurate to
1e-18 relative; I entries ~1e-65 absolute err ~1e-83; min-eig of scaled A ~1e-13*s0-ish... absolute err in A entries
1e-83 vs A min-eig 1e-13*3e-65=3e-78: MARGINAL (err comparable to smallest eig). Hmm. But generalized top eig depends
on INVERSE of small eigs — garbage-prone regardless. The top-3.44 might be PURE ARTIFACT.
Robust approach: exact DP for the QUADRATIC FORMS ONLY along carefully chosen directions? For UPPER bound need global.
Let me think about what TRUE max could be: try well-conditioned subspace max (thr=1e-8 kept 41 modes: 3.33). The tail
adds 3.33->3.6 as threshold loosens — suspicious monotonic creep = artifact signature. TRUE max might be ~3.0-3.3.
ALL below 4 regardless! For a rigorous <4 certificate, use EXACT arithmetic with a SMART basis: choose basis where I
is WELL-conditioned AND spans the same space: e.g., orthonormalize in float then ROUND to rationals? Certificate via
congruence: A=4I-J PSD iff Q'AQ PSD for any nonsingular Q. Take Q = float whitener (inverse Cholesky factor of Is on
kept subspace...). Still leaves tail.
FRESH IDEA — split certificate: A = 4I - J. Write A = A_keep + A_tail? Use eigenvalue interlacing/block argument:
order basis as [well-conditioned 41 modes | tail 56 modes]. A = [A11 A12; A12' A22]. PSD iff A11>0 and Schur
S = A22 - A12'A11^{-1}A12 >= 0. A11 (41x41, well-cond: min-eig of scaled A ~? A=4I-J on kept subspace: mineig ~ (4-3.33)*avg... small ~0.1*s0?) — Cholesky-able with interval verification. Schur complement 56x56 still needs certificate. Recursion doesn't terminate the pain.
DIFFERENT TACK — prove M<4 ANALYTICALLY with a clever majorant: It suffices: 4I(F) - sum_m J_m(F) >= 0 for all symmetric deg<=9 F.
4I - 50 J_1 (by symmetry). Consider identity: 4 int F^2 - 50 int_{fibers}(int F)^2. Hmm 50 vs 4: per-fiber need
(int_0^u F)^2 <= (4/50) int F^2-ish... fiber length u<=1: (int_0^u F)^2 <= u int_0^u F^2 <= int_0^u F^2. That gives
J_1 <= I_fiber-integrated = ... J_1 <= int_R F^2 * 1?? then M<=50. To get 4 need avg fiber factor 4/50=0.08?? Only if
F concentrates where u small... not true for all F. So NO universal fiberwise bound gives 4; the bound must use
DEGREE<=9 + SYMMETRY globally. I.e., certificate inherently needs the matrix computation. OK so exact computation it is.
DECISION: exact rational DP is too slow in pure Python Fractions; instead do EXACT INTEGER arithmetic with numpy object
arrays? Same speed issue. ALTERNATIVE: use 'longdouble DP + mpmath EVP + interval bound' to get a RIGOROUS upper bound
via the following theorem: M* <= tildeM + kappa * eps where... M* = max generalized eig; if I_tilde,J_tilde within
entrywise rel err eta of exact, then M* <= tildeM_true... the error propagation through ill-conditioned I is unbounded
without a lower bound on min-eig(I). DEAD END without min-eig bound. And min-eig(I) lower bound IS a PSD certificate
on I - mu*D... same difficulty but I is EXACTLY PD with integer entries (scaled): I entries = rationals; I - mu*D PSD
for small mu... still PSD cert.
FINAL PRACTICAL OPTION: exact Cholesky/LDL of A=4I-J with entries as EXACT Fractions, using the REDUCED well-conditioned
41-dim subspace for the BULK + ... no. Hmm, actually, why not just TRY sympy/Fraction LDL on the full 97x97 with
entries scaled to small integers? Entry sizes: I entries ~ p/60! — as Fractions with 60!-scale denominators, LDL
intermediate bit-length grows ~ O(n * log) — 97 steps: maybe 1000s of digits; Python big-int ops at that size ~ms;
1M ops -> 1000s+. Too slow, BUT Bareiss (fraction-free) keeps sizes smaller: Bareiss on 97x97 integer matrix with
200-digit entries: O(n^3) ops, intermediate sizes bounded (~ (n) * entrybits ~ 97*700 bits ~ 68k bits ~ 20k digits):
each mult ~ tens of us; 300k mults -> ~10-60s!! BAREISS IS THE ANSWER for exact PSD: A PSD iff all leading principal
minors >= 0 (need >0 for the nonsingular... >=0 with exact-zero handling: semidefinite needs all principal minors, but
for PROOF of 4I-J >= 0 suffices?? No — leading principal minors >=0 does NOT imply PSD (needs >0 for definite; for
semidefinite need ALL principal minors >=0). Hmm! But we can certify A - eps*D > 0 STRICTLY via Bareiss (leading minors
>0 => PD => A >= eps*D >= ... wait A-epsD PD => A >= epsD > 0 => M <= 4-eps' — STRONGER than needed, and if TRUE min eig
is tiny-positive, choose eps tiny: Bareiss with exact integers handles it as long as strictly positive! The TRUE min-eig
of (4I-J)/s0: float says ~-2.6e-13 (rounding noise) — TRUE value unknown sign?! If TRUE 4I-J is INDEFINITE (M*>4),
Bareiss fails and target answer flips to EXISTENCE! Either way Bareiss/exact tells the truth. But exact needs EXACT A
entries as integers: scale A by exact common denominator — entries are Fractions; get exact Fractions from DP first
(1.6M states Fractions — the SLOW part again!). ARGH.
Reduce exact-DP cost: needed states for I: (g,0) seeds only + J seeds (h,s<=20). Hmm 1.6M total. BUT exact Fractions:
can use DYNAMIC common-denominator per (k) level with numpy object-int vectorization! At level k, all values share
denominator L_k = lcm(1..~70)^k-ish? L_k = product... define D_k recursively: transition multiplies by Beta(A+1,r+1) =
A!r!/(A+r+1)! and adds. With per-level denominator D_k = D_{k-1} * L where L = lcm of all (A+r+1)!/(A!r!)... L = lcm of
C(A+r+1, A)*(A+... hmm Beta = 1/[(A+r+1) C(A+r, A)]: denominator divides (A+r+1)*C(A+r,A) | L0=lcm over all (A,r) pairs:
A<=18, r<=~70: L0 = lcm{1..89} ~ e^89 ~ 1e38 (39 digits). D_k = L0^k: at k=50, 2000-digit denominators; numerators similar.
Numpy object arrays of Python ints, vectorized over 5701 states x 50 levels with sparse matvec (40k nnz x 50 = 2M bigint
mults of ~1000-digit numbers ~ us each) -> ~seconds-minutes!! FEASIBLE. Then Bareiss on 97x97 with 2000-digit entries:
intermediate ~ 97*7000 bits?? Bareiss keeps |entries| <= ... Hadamard-ish bound: intermediates <= (max entry)^... roughly
n^{n/2} M^n bits ~ 97*... ~ 97*log2(97)*... ~ 97*6.6 + 97*6600?? no: Bareiss intermediate <= det-based: ~ n! M^n-ish worst case
but typically ~ (entrybits * n) = 2000digits*97?? = 200k digits = 660k bits per entry; 300k mults of 660k-bit ints (~ms each
with Karatsuba... Python uses Karatsuba/FFT for big: 660k-bit ~ 20k 30-bit limbs: mult ~ 0.5-5ms) -> 300k*2ms = 600s. SLOW.
Reduce: use SMALLER exact problem: certify on well-conditioned subspace?? For UPPER bound need full space. ALTERNATIVELY
certify M <= 3.9 (< 4) — same PSD shape. Hmm.
STOP. Clock check: lane is 60 min; already deep. PRAGMATIC RE-FRAME: maybe aim lower — the target allows EITHER direction.
Float says max ~3.3-3.6 <4 i.e. NONEXISTENCE, but rigorous cert is heavy. Reconsider EXISTENCE?? max<4 means no.
What CAN be completed rigorously in remaining time? A REDUCED but complete result? The target demands the FULL deg<=9 answer.
Given constraints, best path: (i) longdouble-DP + mpmath-EVP for a SOLID high-precision max (~reliable to ~1e-6 if conditioning
allows via truncated-SVD subspace + RIGOROUS tail bound?); (ii) attempt Bareiss exact certificate in background; (iii) if exact
fails to finish, file target_exit_request (BLOCKED: certification of the ill-conditioned 97-dim PSD) or EMERGENT?
Hmm — but wait: decision_phase_status is PENDING; instructions say work only on target; exit-request if blocked.
Let me first try the float128-DP + careful subspace analysis to see TRUE max, then decide.
IMMEDIATE: float128 DP rebuild (vectorized, fast) + mpmath EVP.
"""
print("noted")
