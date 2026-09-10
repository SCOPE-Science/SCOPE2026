# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Scalar-centrality divisibility defects are void for diagonal AH blocks,
# with the exact pullback-mass law for the Hilbert-cube-seed Villadsen system

## 1. Setup (fixed, auditable)

Let Q = [0,1]^N (Hilbert cube), B_k = M_{t_k}(C(Q)) with t_1 = 2 and
t_{k+1} = (k+2) t_k, so t_k = (k+1)! (t_1 = 2, t_2 = 6, t_3 = 24, ...).
Let phi_k : B_k -> B_{k+1} be Villadsen diagonal maps with (k+1)
pullback summands along coordinate-shift surjections sigma_j : Q -> Q
(e.g. sigma_j(x)_n = x_{n+j}) plus one point-evaluation summand at c_k,
{c_k} dense in Q, with B_Q = lim(B_k, phi_k) simple.
Write T(B) for the trace simplex. For a = (a_{pq}) in M_t(C(Q)) and a
Borel probability mu on Q, tau_{mu}(a) = int_Q (1/t)Tr(a(q)) dmu(q);
every trace on B_k is of this form.

The admitted fallback was the following literal claim (stage 3, t_3 = 24,
shifts sigma_1..sigma_4, point c_2, F = {z_1,z_2,z_3} the first three
coordinate functions viewed as diagonal scalars z_l I_{24} in B_3):

  (D) Every c.p.c. order-zero psi : M_2 -> B_3 with
      ||[psi(x), f]|| <= 1/16 for all matrix units x and all f in F
      satisfies max_{tau in T(B_3)} |tau(psi(e_11)) - tau(psi(e_22))| >= 1/16.

## 2. Result A (refutation): (D) is false

Define psi_0 : M_2 -> B_3 by psi_0(x) = x tensor I_{12} (constant
M_{24}-valued functions; i.e. the top-left 12x12 diagonal block carries
x_{11}, etc.). Then:

(i) psi_0 is a unital *-homomorphism, hence contractive, completely
positive, and order-zero (e_11 _|_ e_22 maps to orthogonal projections).
Verified as exact 24x24 rational-matrix identities in
`artifacts/prove_defect_void.py` (W1): e_11 e_12 = e_12, e_12 e_22 = e_12,
e_21 e_12 = e_22, psi_0(e_11)psi_0(e_22) = 0, psi_0(e_11)+psi_0(e_22) = I.

(ii) [psi_0(e_ij), z_l I_{24}] = 0 exactly, for every matrix unit e_ij
and every diagonal-scalar test function (any coordinate function, any
finite F, any threshold). Constants commute with scalars. Replayed on a
mesh in the script (W2); the identity is exact, mesh-independent.

(iii) tau(psi_0(e_11)) = tau(psi_0(e_22)) = 1/2 for EVERY trace
tau in T(B_3), because the matrix entries are constant so
tau = normalized matrix trace irrespective of the underlying measure mu
on Q. Hence max_tau |tau(psi_0(e_11)) - tau(psi_0(e_22))| = 0 < 1/16 (W3).

So psi_0 satisfies the hypothesis of (D) with centrality defect 0 and
violates its conclusion. (D) is false.

## 3. Result B (general voidness): no scalar-diagonal variant survives

At every stage k >= 1, t_k = (k+1)! is even, so
psi_k(x) = x tensor I_{t_k/2} is a unital *-homomorphism M_2 -> B_k,
exactly commuting with ALL diagonal scalars and with trace defect 0
(script W4). Structural cause: the constant matrix subalgebra
M_{t_k}(C) subset M_{t_k}(C(Q)) sits inside every diagonal block. Hence:

- Replacing 1/16 by any epsilon > 0, or F by any finite diagonal-scalar
  set, leaves psi_0 (resp. psi_k) a counterexample.
- No finite-stage approximately-scalar-central 2-divisibility defect lemma
  of this shape can hold for diagonal AH blocks. A repaired obstruction
  must test centrality against NON-scalar elements (matrix-valued or
  pullback-block-structure elements) -- a different claim from the literal
  (D), not pursued here.

## 4. Result C (positive companion): exact pullback-mass law

The finite-stage analysis that produced the refutation also yields the
exact law governing where a repaired obstruction must live. Paths from
level l to K are summand-choice sequences (coordinate or point at each
level i); there are M(l,K) = prod_{i=l}^{K-1}(i+2) = (K+1)!/(l+1)! of them,
and the pullback of tau_K evaluates a in B_l at the pasted functions with
equal weight 1/M(l,K) per path. Consequences (exact rational arithmetic,
brute-force verified in `artifacts/prove_mass_law.py`):

- All-coordinate path mass = (l+1)/(K+1) -> 0 as K -> infinity (gamma = 0).
- First-point-at-m class mass = (l+1)/((m+1)(m+2)), proved in closed form;
  classes partition all point-touching paths, e.g. at (l,K) = (1,4):
  24 + 20 + 10 + 6 = 60 paths (masses 2/5, 1/3, 1/6, 1/10).
- Correction to loose language: a first-point CLASS mass is spread over
  many distinct pasted threads (accumulated shifts); e.g. at (1,4) the
  first-point-at-2 class has 10 paths collapsing to 6 distinct atoms
  (multiplicities [1,1,2,2,2,2], atom masses mult/60).
- Single-path mass = 1/M(l,K) = (l+1)!/(K+1)!.

## 5. Result D (target-directed byproduct): unique-trace contraction + K0

For the limit trace system (`artifacts/prove_unique_trace.py`):
R(l,K) = prod_{i=l}^{K-1}(i+1)/(i+2) = (l+1)/(K+1) exactly (Fractions);
atomic class weights sum to 1 - R with total-variation bound
2(l+1)/(K+1) -> 0; K_0(B_Q) = colimit(Z, x(k+2)) = Q with [1] = 1 and
tau_*(n/t) = n/t consistent pairing; shift fixed point d = 0 coherent
(sigma_J(d) = d) while a generic dense enumeration is provably
decoherent (0/19 coherent steps at tol 0.125, max defect 1.0). This
documents the B_Q Elliott-invariant table but does NOT decide Z-stability:
neither target horn (strict comparison + Winter deformation, nor central
character + mean-dimension lower bound, with mdim ratios
(k+1+N)/(k+2)! -> 0) closed in-hour.

## 6. Reproduction

From `output/`:
  python3 artifacts/prove_defect_void.py   # -> REFUTATION_OK (Results A+B)
  python3 artifacts/prove_mass_law.py      # -> MASSLAW_OK (Result C)
  python3 artifacts/prove_unique_trace.py  # -> UNIQUE_TRACE_OK (Result D)
  python3 artifacts/verify_target.py       # -> VERIFY_TARGET_OK (stage data;
    # T2/T5 commentary atom-vs-class language superseded by Result C)

Probes for support spreads, Lemma-C bounds, and thread decoherence were
exploratory working notes (route assessment) and are not archived as claim
evidence; the four scripts above are the complete verification-critical set.

## 7. What is claimed and what is not

Claimed: (A) the literal 1/16 defect inequality is false, with explicit
witness; (B) the voidness generalizes to every stage and every
finite-diagonal-F/positive-threshold variant, with structural cause;
(C) the exact pullback-mass law above; (D) the unique-trace/K0 data above.
NOT claimed: Z-stability or non-Z-stability of B_Q (both target horns
remain open); any repaired matrix-valued-centrality defect bound; any
mean-dimension lower bound; strict comparison either way. Section 5 states
exactly how far the target evidence goes.
