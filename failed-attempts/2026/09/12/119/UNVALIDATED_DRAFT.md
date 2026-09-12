# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Disproof of the split-p finite cuspidal criterion at (K, p) = (Q(i), 5)

## Theorem (TARGET resolution)

Let K = Q(i), p = 5, T the places above {2, 5}, and H = UT_3(Z/25) the finite
Heisenberg exponent-25 quotient with centre Z ≅ Z/25, pushed out to
1 → H → E_H → G_{K,T} → 1 as in the topic. Read x_v, y_v as lifts to H of a
(Z/25)^2-basis of V = H/Z (the standard non-central Heisenberg generators;
the only reading under which the commutator test is non-vacuous — see §5).
Then the stated equivalence is **false**: there exist cuspidal sections
s_cusp : G_{K,T} → E_H which violate the local Heisenberg inertia commutator
relation. In fact the local relation is unsatisfiable by *any* section on the
full inertia group I_v (for either v | 5), indeed already on tame inertia
alone. The cyclotomic-descent half of the criterion is therefore moot.

## 1. Local cyclotomy at v | 5

5 = 2^2 + 1^2 splits in K = Q(i), so each completion K_v ≅ Q_5 has residue
field F_5. Since x^25 − 1 = (x−1)^25 in F_5[x] (all C(25,k), 0<k<25, vanish mod
5), no nontrivial 5-power roots of unity are visible mod 5: the residue degree
of K_v(μ_25)/K_v is 1 and the extension is totally ramified of degree
φ(25) = 20. Hence the mod-25 cyclotomic character satisfies

  χ : I_v ↠ (Z/25)^× ≅ C_20   (surjective, full inertia — v ∈ T is allowed
  to ramify, so I_v ⊂ G_{K,T} is the full local inertia).

Consequently χ(I_v) contains elements ≠ 1 mod 25 from *both* ramification
layers: wild elements 1 + 5t (e.g. u = 6 of order 5) and tame elements of
order 4 (e.g. u = 7; the tame image is the prime-to-5 subgroup
{1, 7, 18, 24} ⊂ (Z/25)^×, which is nontrivial). Globally [K(μ_25):K] = 20
(local degree already 20), ramified only above 5, so K(μ_25)/K factors via
G_{K,T}. All unit-group facts are certified by brute force in
`output/artifacts/verify_heisenberg_local.py` (§A–D of its log).

## 2. Heisenberg group facts (certified by exhaustive enumeration)

Write H = {(a,b,c) : a,b,c ∈ Z/25} with (a,b,c)(a′,b′,c′) =
(a+a′, b+b′, c+c′+ab′). Then |H| = 25^3, centre Z(H) = {(0,0,c)} of order 25,
V = H/Z ≅ (Z/25)^2, commutator [(a,b,c),(a′,b′,c′)] = (0,0,ab′−a′b), and for
the standard generators X = (1,0,0), Y = (0,1,0):

  C_H(X) ∩ C_H(Y) = Z(H).

The script verifies this by exhausting all 15625 elements, plus the
commutator formula on a deterministic subsample. The Galois action on V is
scalar via χ (both Kummer coordinates have weight 1), modelled by
φ_u(a,b,c) = (ua, ub, u^2c); the script checks φ_u is an automorphism and that
inner conjugation preserves V-classes, so for every h ∈ H,
φ_u(hXh^{−1}) has V-class u·(1,0) ≠ (1,0) whenever u ≠ 1 mod 25 (checked for
all h ∈ H with u ∈ {6, 7}).

## 3. The local condition is unsatisfiable

Let s : G_{K,T} → E_H be *any* section and σ ∈ I_v with u := χ(σ) ≠ 1
(e.g. any lift of a wild element with u = 6, or tame with u = 7 — both exist
by §1). Suppose [s(σ), X] = [s(σ), Y] = 1 in E_H. Projecting to E_H/Z, which
is split as V ⋊ G_{K,T} by the section induced from s, centrality in an
abelian-kernel semidirect product gives σ·X̄ = X̄ and σ·Ȳ = Ȳ in V, i.e.
(u−1)·(1,0) = 0 and (u−1)·(0,1) = 0 in (Z/25)^2, forcing u = 1 mod 25 —
contradiction. Hence s(σ) fails to centralize at least one of X, Y. Since such
σ exist in both wild and tame inertia, **no** section satisfies
[s_v(I_v), x_v] = [s_v(I_v), y_v] = 1, even with I_v replaced by tame inertia.

## 4. A cuspidal section exists over G_{K,T} — and therefore violates the test

The three cusps {0, 1, ∞} are K-rational, so Deligne tangential basepoints give
cuspidal sections G_K → π_1^geom ⋊ G_K, pushed to the H-quotient E_H. The
tangential Galois action is ramified only where μ_25 ramifies (P^1 with the
divisor {0,1,∞} has good reduction at every finite place — the three sections
stay disjoint mod any prime — so no extra ramification occurs), i.e. only
above 5, and 5 ∈ T. Thus a cuspidal section descends to
s_cusp : G_{K,T} → E_H. By §3, s_cusp violates the local commutator relation at
each v | 5. This is exactly the third admitted resolution mode: a cuspidal
section violating one of the two conditions (we make no claim about its Kummer
pair's descent status, which is unnecessary for the refutation).

## 5. Conclusion and remarks on scope

The "only-if" direction (cuspidal ⇒ local + descent) is false, so the iff is
false. (The "if" direction is vacuously true since the antecedent never holds;
we do not claim it as a positive result.) The refutation uses the literal
reading of the local test with x_v, y_v lifting a V-basis — the standard
Heisenberg-generator reading, and the only one under which the test has teeth:
had x_v, y_v been central, every section would pass trivially and the
criterion would have to be judged on descent alone, a case the topic text
("Heisenberg inertia commutators" with two generators) excludes. The argument
is robust: it kills the test on tame inertia already, so no weakening of I_v
to tame inertia, and no H-conjugacy (conjugating the section preserves the
V-class argument), can rescue the criterion.

## 6. Reproduction

Run `python3 output/artifacts/verify_heisenberg_local.py` (pure standard
library; ~15k-element group exhausted in seconds). Expected: ALL CHECKS PASSED
with (Z/25)^× = ⟨2⟩ of order 20, wild {1,6,11,16,21}, tame {1,7,18,24},
|Z(H)| = 25, C(X)∩C(Y) = centre, and V-class displacement by φ_6, φ_7 for all
h ∈ H. Full output is stored in
`output/artifacts/verify_heisenberg_local.log`.
