# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Commutator-power countable rank in Grp
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1175
- **Disposition:** NO_RESULT
- **Domain:** group theory
- **Method:** derivation search and finite-quotient separation

## Problem

Let Set be locally finitely presentable and let T be the free-group monad on Set, finitary with Lawvere theory the theory of groups. Consider the named colimit type of coequalizers of countably generated normal congruences (quotients by infinite relator families); the generating parallel pair is non-reflexive, hence outside the sifted reflexive-coequalizer preservation theorem. Fix the free group F(a,b) and for each integer n >= 2 let w_n = [a^n, b^n] be the explicit commutator-power word, deliberately excluding n = 1 so that no single relator abelianizes the presentation; let G be the group presented as <a, b | w_n = 1 for all n >= 2>, motivated by commutator-power laws and Burnside-type finite-presentability boundaries. Decide the colimit-preservation witness together with the accessibility-rank separation: a complete answer either proves that the canonical Set comparison map coeq(T(R) => T(X)) -> T(coeq(R => X)) for this relator diagram is bijective and exhibits a finite subfamily of the words w_n from which every other w_n follows by explicit free-group derivations (so G is finitely presentable, a new commutator-power identity), or exhibits an explicit word-level mismatch in the comparison or a separating homomorphism from a finite-subfamily quotient onto an explicit finite group killing that subfamily while sending w_N to a non-identity element for some N (so G is strictly countably presentable and the presentability rank jumps). All words, derivations or homomorphisms, and quotient computations are to be listed and verified.

## Attempted claim

Let Set be locally finitely presentable and let T be the free-group monad on Set, finitary with Lawvere theory the theory of groups. Consider the named colimit type of coequalizers of countably generated normal congruences (quotients by infinite relator families); the generating parallel pair is non-reflexive, hence outside the sifted reflexive-coequalizer preservation theorem. Fix the free group F(a,b) and for each integer n >= 2 let w_n = [a^n, b^n] be the explicit commutator-power word, deliberately excluding n = 1 so that no single relator abelianizes the presentation; let G be the group presented as <a, b | w_n = 1 for all n >= 2>, motivated by commutator-power laws and Burnside-type finite-presentability boundaries. Decide the colimit-preservation witness together with the accessibility-rank separation: a complete answer either proves that the canonical Set comparison map coeq(T(R) => T(X)) -> T(coeq(R => X)) for this relator diagram is bijective and exhibits a finite subfamily of the words w_n from which every other w_n follows by explicit free-group derivations (so G is finitely presentable, a new commutator-power identity), or exhibits an explicit word-level mismatch in the comparison or a separating homomorphism from a finite-subfamily quotient onto an explicit finite group killing that subfamily while sending w_N to a non-identity element for some N (so G is strictly countably presentable and the presentability rank jumps). All words, derivations or homomorphisms, and quotient computations are to be listed and verified.

## Research outcome

Target blocked: verified finite-group separators cover singletons, tested pairs, and all finite relator sets with gcd>=2 (Heisenberg UT3 family, S3/S7 exact-order maps, all machine-checked), but sets with three or more pairwise-coprime moduli such as {2,3,5} resisted every tried construction and a 4M-trial bounded search; neither a general separation nor a finite-derivation rigidity proof was found, so no auditable complete rank decision exists and the lane exits cleanly with all partial evidence preserved under output/artifacts/.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No complete decision of the finite-presentability rank of G was obtained: the uniform separation or derivation scheme for finite relator sets containing three or more pairwise-coprime moduli (e.g. {2,3,5}) remains open, and the 4M-trial S_10 search plus the elementary forcing lemma only localize, not resolve, that hard core. Verified artifacts cover singletons, tested pairs, and gcd>=2 sets only.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No complete decision of the finite-presentability rank of G was obtained: the uniform separation or derivation scheme for finite relator sets containing three or more pairwise-coprime moduli (e.g. {2,3,5}) remains open, and the 4M-trial S_10 search plus the elementary forcing lemma only localize, not resolve, that hard core. Verified artifacts cover singletons, tested pairs, and gcd>=2 sets only.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
