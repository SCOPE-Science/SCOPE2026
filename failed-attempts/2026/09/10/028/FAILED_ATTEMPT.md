# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Formality dichotomy for the triple-2-sphere wedge plus one 5-cell: a Massey witness versus a Steenrod-forced vanishing theorem
- **Round:** 2026-09-07-first-light-01
- **Lane:** 561
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Homotopy Theory
- **Method:** Postnikov k-invariant analysis with Steenrod-operation constraints and Massey-product formality transfer

## Problem

Decide formality versus non-formality for the named simply-connected 2-stage complex X_1 = (S^2_1 vee S^2_2 vee S^2_3) union_{w} e^5, where w = 1 times w0 and w0 generates the distinguished infinite-cyclic Whitehead summand W ~= Z in pi_4(vee^3 S^2)/torsion. Rational cohomology truncated at degree 5 is fixed: H^2(X_1;Q) = span{x1,x2,x3}, xi xj = 0, H^5(X_1;Q) = span{z}. Either prove all Massey triple products vanish via a Steenrod-operation constraint on the k-invariant (formality horn) or exhibit the Massey witness <x1,x2,x3> = +/-z with explicit defining-system cochains (non-formality horn).

## Attempted claim

For X_1 = (S^2_1 vee S^2_2 vee S^2_3) union_{1*w0} e^5 as fixed above, the rational Massey triple product <x1,x2,x3> is defined (x1 x2 = x2 x3 = 0) and equals +/-z, a generator of H^5(X_1;Q), modulo the indeterminacy ideal (x1,x3) = 0; hence X_1 is non-formal over Q, and the mod-2 reduction of its k-invariant satisfies the explicit Sq^2 identity stated in the record.

## Research outcome

Proved the target: explicit Sullivan defining system gives strictly defined Massey <x1,x2,x3>=+/-z on X1 (pairing constant via Hilton transgression + primitivity), hence rational non-formality, plus vanishing mod-2 Sq table through degree 6 with Sq^2 line in ker (free-Whitehead). Exact-arithmetic replay VERIFY_OK.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: Cellular cohomology dims (1,0,3,0,0,1,0), cup-triviality (H^4=0), definedness (x1x2=x2x3=0) and zero indeterminacy (H^3=0) are correct and replayed. Sullivan linear algebra (d3 6x6 iso, delta 10x18 rank 10 ker 8, m closed in ker, mod-7 cross-check) replays VERIFY_OK. Mod-2 dims and vanishing Sq<=6 by degree/instability are correct but vacuous (all relevant sources/targets zero). ESSENTIAL GAP: the headline identity <x1,x2,x3>=+/-z (c=+/-1, m spans H^5(X1), m=d(v0) for v0 dual to w0=[[i1,i2],i3]) is NOT proved. verify_target.py constructs an ARBITRARY 7-dim hyperplane of ker missing m (ext=ker minus one vector), not the SPECIFIC hyperplane annihilating w0. No code encodes w0 Hilton coordinates or Sullivan differential coefficients d(v). The bridge cites Hilton Hopf-Hilton evaluation + Porter/Massey-Whitehead transgression with pages explicitly unchecked (DRAFT Sec Separation: live retrieval rate-limited, pages unchecked). No Andrews-Arkowitz differential formula is computed. Hence pairing constant +/-1 is assertion, not proof/computation. Moreover ordering analysis indicates likely misidentification: Dranishnikov-Rudyak Thm 3 / Uehara-Massey Lemma 7 pairs [i1,[i2,i3]] with <a1,a2,a3>; w0=[[i1,i2],i3]=+/-[i3,[i1,i2]] pairs with <a3,a1,a2>=(0,1,-1), not m=(1,0,-1). Draft provides no coefficient matrix distinguishing these two independent directions in the 2-dim distinct-index plane, so survival of the CLAIMED ordering is unestablished and may be false (the surviving Massey on X1 may be the cyclic permute). Proof vs computation not separated for the decisive step. originality: TARGET route: audited normally, no preset presumption. Headline normalized to (a) literal triple-wedge-plus-5-cell Massey +/-z, (b) equivalents: Sullivan-differential / Whitehead-bracket / Massey-Whitehead duality forms, permuted labelings, [[,],] vs [, [,]] parenthesizations, (c) dominance: general k-stage/2-stage formality, higher Whitehead-Massey duality, k=general theorems. Searches via SerpBase (3 forms) + OpenAlex/Crossref auxiliaries found decisive priors that substantively imply the phenomenon: Uehara-Massey (1957) Lemma 7 (Jacobi identity for Whitehead products) + Dranishnikov-Rudyak (2003) Theorem 3: for K=S^{k1}vS^{k2}vS^{k3}, f=[i1,[i2,i3]], X=cone(f), <a1,a2,a3> has zero indeterminacy and equals (-1)^{k1} generator. Setting k1=k2=k3=2 gives EXACTLY a triple-2-sphere wedge plus one 5-cell with strict Massey generating H^5 and hence non-formality. Up to wedge-permutation automorphism (S3), DR's attaching line [i1,[i2,i3]] maps to [i3,[i1,i2]]=+/-w0, and DR's Massey <a1,a2,a3> maps to <a3,a1,a2> on X1. Labels 1,2,3 are arbitrary; claiming <x1,x2,x3> vs <x3,x1,x2> is relabeling within same isomorphism type, not a new cell. Andrews-Arkowitz (1978) Thm 6.1 (Sullivan minimal-model differential encodes higher Whiteheads) + Porter Higher Products duality provide the general Massey-Whitehead correspondence of which the computation is a k=2 instance. Denham-Suci…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Sign +/- is ordering/orientation convention. Page-level citations (Hilton/Sullivan/DGMS/Porter) recalled from standard statements; live retrieval rate-limited (429) so exact pages unchecked. The pairing-constant step cites Hilton's Hopf-invariant evaluation (standard) rather than a machine singular-cochain check.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
