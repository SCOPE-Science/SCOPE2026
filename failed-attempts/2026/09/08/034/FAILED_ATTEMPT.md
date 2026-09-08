# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** A certified finite extra-relator quotient in a small-exponent two-generator triangle window with coset-table witness
- **Round:** 2026-09-07-first-light-01
- **Lane:** 125
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Combinatorial Group Theory
- **Method:** Todd-Coxeter coset enumeration with Reidemeister-Schreier presentation replay

## Problem

Let T(l,m,n) = <a,b | a^l = b^m = (ab)^n = 1> be the two-generator ordinary triangle presentation. Let W be the natural small-exponent hyperbolic window W = {(l,m,n) : 3 <= l <= m <= n <= 6, 1/l+1/m+1/n < 1}. For each (l,m,n) in W the baseline T(l,m,n) is infinite (Fuchsian/hyperbolic). Consider the one-extra-relator family G(l,m,n;k,w) = <a,b | a^l = b^m = (ab)^n = w(a,b)^k = 1> with fixed short word w(a,b) = [a,b] = aba^{-1}b^{-1} and 2 <= k <= 5. Survey the finite window W x {2,3,4,5} via Todd-Coxeter coset enumeration over the trivial subgroup plus Reidemeister-Schreier replay: find at least one tuple (l,m,n;k) with a complete terminating coset table proving |G| = N finite, relator-check replay, and a separating invariant showing the certified finite G is a proper finite quotient distinct from the infinite baseline T(l,m,n) (e.g. order inequality against an infinite linear/symmetric quotient of T(l,m,n) or abelianization/PSL(2,p) image obstruction in the neighbor).

## Attempted claim

There exists at least one tuple (l,m,n;k) in W x {2,3,4,5} with w=[a,b] such that G(l,m,n;k,w) is finite of explicitly certified order N (complete coset table over 1 with all relators verified closed), cross-validated by a Reidemeister-Schreier presentation of a small-index subgroup consistent with order N, and separated from the infinite baseline T(l,m,n) by an explicit quotient invariant (e.g. T(l,m,n) surjects an infinite group while G has order N, or |G| does not divide any member of a known infinite-quotient family of the neighbor). The certificate consists of committed integer coset tables verifiable without trusting any group library.

## Research outcome

Certified finite extra-relator quotient G(3,4,5;2) of order 360 with closed coset-table witness, RS index cross-check, and separation from the infinite hyperbolic baseline, plus 5 sibling finite orders and an honest 76-case census table.

## Why this attempt failed

Failed axes: value.

value: Even taking correctness and narrow novelty as given, the contribution is an unexplained single-window enumeration, not an independently retrievable advance. The window (hyperbolic triples with entries <=6 crossed with k<=5; headline one of 76 presentations, 70 reported inconclusive at a 1500-coset cap with no infiniteness witnesses) is an arbitrary bounded box atop the closed textbook (l,m,n) trichotomy, and the method is routine bounded Todd-Coxeter reporting which cases terminate. No general finiteness criterion, no finite-vs-infinite boundary characterization, no extremal/structural theorem, and explicitly no isomorphism identification (the order-360 datum is left as a bare number; the class/order table in fact matches A6 but this is disclaimed as observation only). Sibling orders include the near-trivial C3 collapse and four more bare numbers with the same deficit. Downstream uses (residual finiteness, growth gaps, benchmarks, hypermap/Hurwitz/property-(T) quotients) are asserted, not demonstrated by any downstream theorem, example, or adopted benchmark. The fallback census also fails its own bar: 70/76 inconclusive is not a complete finite-vs-infinite census with extremal table. Under SCOPE value policy this is textbook-trichotomy-plus-parameter-substitution / unexplained enumeration / tiny unmotivated gain: correct and narrowly new but not worth finding later as mathematics.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: ['Remaining 70 tuples inconclusive at 1500-coset cap; no infiniteness witnesses computed.', 'Baseline T(3,4,5) infiniteness cited as classical trichotomy, not re-proved.', 'No isomorphism identification of the order-360 group claimed.', 'Literature novelty rests on admission triage; no further independent search in this pass.']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
