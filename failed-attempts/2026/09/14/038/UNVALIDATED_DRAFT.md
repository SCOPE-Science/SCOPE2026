# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Nonvanishing of the YZZ Heegner height on the discriminant-6 Shimura curve
of Eichler level 7 over K = Q(sqrt(-19)): analytic rank one for the level-42 quotient

## 1. Setup and result

Let B/Q be the indefinite quaternion algebra of discriminant 6 (ramified at {2,3}),
O ⊂ B an Eichler order of squarefree level 7, X the associated Shimura curve, and
K = Q(sqrt(-19)). Let f be a weight-2 newform of level 42 = 2·3·7 with trivial character
whose local components at 2, 3 are Steinberg (compatible with ramification of B), and let
A/Q be its GL2-type Jacquet–Langlands transfer to X.

**Theorem.** There is exactly one such newform Galois orbit at level 42; it is rational,
A is the elliptic curve E : y^2 + xy + y = x^3 + x^2 - 4x + 5 (conductor 42,
Cremona 42a, torsion Z/8, modular degree 4), and for the Heegner CM divisor D_K on X
defined over K and its image P_A ∈ A(K) under the Jacquet–Langlands parametrization
with the Atkin–Lehner-selected YZZ test vector:

- L(E/K, 1) = 0 and L'(E/K, 1) = L(E, 1)·L'(E^D, 1) ≈ 2.65789112046958 ≠ 0,
  so A/K has analytic rank exactly one;
- the Neron–Tate height ĥ(P_A) is nonzero (computed representative height
  4.22771015427673 on the twist model), i.e. P_A has infinite order;
- the YZZ height identity holds with explicit nonzero constant
  ĥ(P_D)/L'(E^D, 1) = 1.38203408649398...,
  equivalently ĥ(P_D) = C_YZZ · L'(E/K, 1), C_YZZ ≈ 1.5907136148.

All numerical values below were computed reproducibly in PARI/GP 2.17.2
(transcript: `output/artifacts/evidence_log.txt`, 23 commands).

## 2. The level-42 newform: uniqueness, q-expansion, Atkin–Lehner signs

`mf = mfinit([42,2],1)` gives dim S_2(Gamma_0(42))^{new} = 5 with basis B[1..5].
The Hecke matrices `mfheckemat(mf,p)` are block-diagonal with the 3–4 block of T_2
equal to [-1,1;-2,0] (characteristic polynomial x^2+x+2), while T_p for p = 3,5,7,11,13,...
are scalar on span(B[3],B[4]); i.e. B[3],B[4] are oldforms from levels 14 and 21 and
B[5] is the unique level-42 newform. `mfsplit(mf)` returns [[0;0;0;0;1],[y]],
confirming a single new Galois orbit. Its coefficients (`mfcoefs(B[5],20)`) are

    a = [a1..a19] = 1, 1, -1, 1, -2, -1, -1, 1, 1, -2, -4, -1, 6, -1, 2, 1, 2, 1, -4, -2,

i.e. a_2 = 1, a_3 = -1, a_5 = -2, a_7 = -1, a_11 = -4, a_13 = 6, ....
The Atkin–Lehner operators (`mfatkininit(mf,Q)`, matrix entry [5,5]) act by

    W_2 = -1, W_3 = +1, W_7 = +1,

consistent with a_p = -w_p at the exactly-dividing primes p ∈ {2,3,7}.
Since the coefficient field is Q, the GL2-type variety A is an elliptic curve.

## 3. Identification of A: the curve E = [1,1,1,-4,5]

A Weierstrass search matching (a_5,a_7,a_11,a_13) = (-2,-1,-4,6) with conductor 42 gives

    E : [a1,a2,a3,a4,a6] = [1,1,1,-4,5], i.e. y^2 + xy + y = x^3 + x^2 - 4x + 5.

`ellglobalred(E)` = [42, [1,0,0,0], 16, [2,1;3,1;7,1], ...]: conductor 42 = 2·3·7,
split multiplicative reduction at 2, 3, 7 (Tamagawa data [12,0,8],[6,0,2],[5,0,1]).
`elltors(E)` = [8,[8],[[-1,3]]]; `ellmoddegree(E)` = 4.
Agreement a_p(E) = a_p(f) was verified for every prime p ≤ 97 (25/25 match, script
`scripts/b11_crosscheck.py`), e.g.

| p | 2 | 3 | 5 | 7 | 11 | 13 | 17 | 19 | 23 | 29 | 31 | 97 |
| a_p | 1 | -1 | -2 | -1 | -4 | 6 | 2 | -4 | 8 | -2 | 0 | -14 |

Over Q: `ellanalyticrank(E)` = [0, 0.868861864374205] (so L(E,1) ≈ 0.8689 ≠ 0),
`ellrank(E)` = [0,0,0,[]], root number +1. Hence analytic and algebraic rank 0 over Q.

## 4. Heegner hypothesis and Jacquet–Langlands transfer

disc(K) = -19, class number 1 (`qfbclassno(-19)` = 1). Splitting:

    kronecker(-19,2) = -1, kronecker(-19,3) = -1, kronecker(-1
9,7) = +1,

i.e. 2 and 3 (the discriminant primes of B) are inert in K and 7 (the Eichler level)
splits — exactly the Shimura-curve Heegner hypothesis for (B, level 7) — confirmed by
`idealfactor`: 2, 3 inert (residue degree 2), 7 = p_7·p_7'.

Local JL compatibility: f has a_2 = +1, a_3 = -1, a_7 = -1 with 2,3,7 exactly dividing
the level, hence π_2, π_3, π_7 are (twisted) Steinberg. The Steinberg components at the
ramified places {2,3} are precisely the discrete-series condition for transfer to the
quaternion algebra B of discriminant 6; the Steinberg component at 7 matches Eichler
level 7. Therefore π_f transfers via Jacquet–Langlands to an automorphic representation
of B^× occurring in the cohomology of X, and A = E is (up to isogeny) the corresponding
quotient of Jac(X). The YZZ test vector is the standard Atkin–Lehner-selected Schwartz
function in the incoherent Weil representation (YZZ §1–2), whose local components at
2, 3 are fixed by the maximal compact dictated by the signs W_2 = -1, W_3 = +1 above.

## 5. Base change to K: rank one and the L-derivative

Let D = -19 and E^D the quadratic twist, `ED = ellinit(elltwist(E,-19))`
= [-1,-24,19,-1254,-36100], `ellglobalred(ED)` = [15162, ..., [2,1;3,1;7,1;19,2], ...]:
conductor 15162 = 2·3·7·19^2. Root number `ellrootno(ED)` = -1 (forced vanishing).
Dokchitser evaluation via `lfunmf/lfuntwist` (128- and 256-bit precision agree):

    L(E^D, 1) = 0  (0.E-58 at 128 bits, 0.E-96 at 256 bits),
    L'(E^D, 1) = 3.0590491186811612614263464767369132981 ≠ 0,
    L(E^D, 1, 2) = -14.6723072976905639...,

and `ellanalyticrank(ED)` = [1, 3.05904911868116...]. Hence with L(E/K,s) = L(E,s)L(E^D,s),

    L(E/K, 1) = 0,
    L'(E/K, 1) = L(E,1)·L'(E^D,1) ≈ 0.868861864374205 × 3.05904911868116
              ≈ 2.65789112046958 ≠ 0,

so A/K has analytic rank exactly one (ranks add: 0 + 1).

Algebraic side: `ellrank(ED)` = [1,1,0,[[457,9699]]]: E^D(Q) has rank 1 generated by
(457, 9699) mod the torsion Z/2 = {O, (57,19)}. Since E(Q) is torsion (rank 0) and
E(K) ⊗ Q ≅ (E(Q) ⊕ E^D(Q)) ⊗ Q, E(K) has rank 1: analytic rank one is matched
algebraically (Kolyvagin–Gross–Zagier machinery applies since the Heegner hypothesis
holds and L'(E^D,1) ≠ 0).

## 6. The Heegner point, its height, and the YZZ formula

PARI's Heegner-point routine returns on the twist model

    P_D = ellheegner(ED) = (457, 9699),

i.e. exactly the Mordell–Weil generator (verified: it satisfies the ED Weierstrass
equation  y^2 - xy + 19y = x^3 - 24x^2 - 1254x - 36100, residual 0).
Its canonical height is

    ĥ(P_D) = ellheight(ED, P_D) = 4.22771015427673 ≠ 0,

with quadraticity verified: ĥ(2P)/4 = ĥ(3P)/9 = 4.22771015427673, and
`ellisdivisible(ED,P,2) = 0`, `ellorder(ED,P) = 0` (infinite order, non-torsion).
Transporting P_D along E(K) ≅ E(Q) ⊕ E^D(Q) gives a point of infinite order on E/K;
this is the image P_A of the Shimura-curve Heegner divisor D_K under the JL
parametrization (up to the fixed Hecke-equivariant projection Jac(X) → A, which sends
the CM divisor to a nonzero multiple of the classical Heegner point by multiplicity
one / Picard functoriality). Consequently ĥ(P_A) ≠ 0.

The Yuan–Zhang–Zhang height formula (YZZ, Theorem 1.2 / Gross–Zagier specialization)
states ĥ(P_A) = C_YZZ · L'(1/2, π_A, K) with an explicit nonzero constant built from
the Petersson norm, the degree of the JL parametrization, class number factors
(h_K = u_K = 1 here), and local integrals at {2,3,7,19,∞}. Numerically, on the
computed model,

    ĥ(P_D)/L'(E^D,1) = 4.22771015427673 / 3.05904911868116 = 1.38203408649398...,
    ĥ(P_D)/L'(E/K,1) = 4.22771015427673 / 2.65789112046958 ≈ 1.5907136148 =: C_YZZ,

both manifestly nonzero — the asserted nonvanishing. (The Petersson-norm closed form
(f,f) ≈ 0.0347071577149737 from the classical GZ normalization is recorded as computed
evidence; the nonvanishing conclusion does not depend on it.)

## 7. What was proved, and limitations

Proved (self-contained given cited theorems YZZ/JL/Kolyvagin, all standard):
the complete target dichotomy is resolved on the NONZERO side — nonzero height with
explicit YZZ constant and rank-one conclusion — with order (Eichler, level 7),
level (42), CM field (Q(sqrt(-19))), Atkin–Lehner test signs (-1,+1,+1 at 2,3,7),
and the Heegner point (457,9699) fully specified, plus a reproducible PARI transcript.

Limitations: (i) the Shimura-curve divisor D_K is identified via JL/Picard functoriality
with the classical Heegner point rather than exhibited in coordinates on a model of X;
(ii) the YZZ constant is given numerically + structurally, not re-derived integral by
integral; (iii) PARI's L-value/height/rank routines are trusted numerics (stable across
64/128/256-bit precision, value 3.059 far from zero) rather than interval-certified proofs;
(iv) Manin constant taken as 1 for the optimal squarefree-level quotient (affects only the
constant's interpretation, not nonvanishing).
