# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Heegner 17-indivisibility input for 11a1 over Q(sqrt(-19))
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1196
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Heegner points and Kolyvagin systems
- **Method:** explicit point with height bound and mod-17 Kummer reduction check

## Problem

Let E/Q be the elliptic curve 11a1 given by y^2+y=x^3-x^2-10x+20 of conductor 11, let K=Q(sqrt(-19)) of discriminant -19, and let p=17. Preliminary gate (failure is NO_RESULT, not disproof): verify p is good ordinary for E by counting E(F_17), verify every prime dividing 11 splits in K by Kronecker symbols, and verify the mod-17 representation is irreducible via two explicit Frobenius trace witnesses. Decided claim (base-layer Kolyvagin input for the anticyclotomic mu-vanishing program, no tower layers): decide, with a complete certificate, whether the conductor-1 Heegner point y_K on E(K) has infinite order and is 17-indivisible in E(K)/17E(K), witnessed by an explicit point, a nonzero canonical-height lower bound, and a nonzero mod-17 Kummer class checked against the 17-division polynomial and the local Kummer conditions at the split primes above 17. A complete answer proves indivisibility with that witness set, or rigorously disproves it by certifying y_K torsion or 17-divisible with an explicit division preimage or a height-zero plus 17-descent certificate that pins the obstruction in Sha(E/K)[17].

## Attempted claim

Let E/Q be the elliptic curve 11a1 given by y^2+y=x^3-x^2-10x+20 of conductor 11, let K=Q(sqrt(-19)) of discriminant -19, and let p=17. Preliminary gate (failure is NO_RESULT, not disproof): verify p is good ordinary for E by counting E(F_17), verify every prime dividing 11 splits in K by Kronecker symbols, and verify the mod-17 representation is irreducible via two explicit Frobenius trace witnesses. Decided claim (base-layer Kolyvagin input for the anticyclotomic mu-vanishing program, no tower layers): decide, with a complete certificate, whether the conductor-1 Heegner point y_K on E(K) has infinite order and is 17-indivisible in E(K)/17E(K), witnessed by an explicit point, a nonzero canonical-height lower bound, and a nonzero mod-17 Kummer class checked against the 17-division polynomial and the local Kummer conditions at the split primes above 17. A complete answer proves indivisibility with that witness set, or rigorously disproves it by certifying y_K torsion or 17-divisible with an explicit division preimage or a height-zero plus 17-descent certificate that pins the obstruction in Sha(E/K)[17].

## Research outcome

Target blocked by a conductor obstruction: the stated equation has conductor 51931, not 11, so it is not 11a1; reported as an emergent finding with certified mod-17 irreducibility, an infinite-order point, and a split-prime Kummer certificate.

## Why this attempt failed

Failed axes: originality, value.

originality: EMERGENT_FINDING genuinely arose from the target investigation, so absence from topic.json is not adverse. Substantively, however, the core mathematical facts are already recorded or implied by the official database and a stronger known theorem. LMFDB 51931.a1 lists verbatim the same minimal equation y^2+y=x^3-x^2-10x+20 with conductor 51931=11*4721, discriminant -51931, j=-122023936/51931, rank 1 with generator (0,4) and height 1.38274, and states the l-adic Galois representation has maximal image for all l, which strictly implies the claimed mod-17 irreducibility. Hence the conductor/discriminant/j, the infinite-order point identity, and irreducibility are database recomputation or corollary of a stronger fact, not new claims. The only computationally novel fragment (order-85 Kummer check at the arbitrarily chosen split prime 83) is a mechanical finite-field enumeration with no prior motivation. A timestamp or in-lane derivation does not establish priority over this coverage. value: As an EMERGENT_FINDING it is judged under the ordinary full value standard with no presumption. The headline is essentially the negative resolution of the admitted target via a single-sign +20/-20 normalization typo plus routine certifications of the resulting arbitrary typo curve: discriminant via textbook b-formulas, point counts by brute force, a standard two-reduction infinite-order argument for the already-catalogued generator (0,4), Borel/Dedekind-style irreducibility checks, and a local 17-indivisibility check at an arbitrarily selected split prime 83 (with four more arbitrary primes). The object was not motivated before computation, the exact values were already in LMFDB 51931.a1, the chosen prime 83 has no independent motivation, and certification/replayability alone does not create value under the shared STANDARD. Internal protective use (stopping a mistyped input from entering level-11 Kolyvagin arguments) is useful workflow hygiene but not an independently retrievable public-record result; it is the classic cheap type/normalization-error plus direct-lookup plus arbitrary-parameter-fact pattern the STANDARD rejects even when correct.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The report does not decide Heegner 17-indivisibility for either model: no canonical-height lower bound, no 17-division-polynomial Kummer comparison, and no CM fiber identification were completed. It makes no claim about the true 11a1 curve beyond using its newform coefficients to diagnose the typo, and no claim about Sha(E/K)[17], BSD, anticyclotomic towers, or mu-invariants. The O_K search was bounded (|a|,|b|<=4) and evidences only that no second tiny generator exists. All computations assume…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
