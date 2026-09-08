# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** The monomiality threshold at order 24: complete M-group dichotomy with certified minimal non-monomial witnesses from presentations
- **Round:** 2026-09-07-first-light-01
- **Lane:** 192
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Representation Theory
- **Method:** conjugacy-class orbit enumeration with Dixon-Schneider reconstruction plus exhaustive subgroup-induction search

## Problem

Starting from fixed presentations for each of the 15 groups of order 24 (SmallGroups IDs), compute conjugacy classes by orbit BFS, recover complex Irr via Dixon-Schneider with orthogonality logs, then decide the M-group property per group by exhaustive induction search: for each nonlinear irreducible chi, test every conjugacy-representative subgroup H<G and every linear character lambda of H whether Induction(H,lambda)==chi via scalar products; tabulate M-group verdicts for all 15 groups with exhibiting pairs (H,lambda) in monomial cases and full no-inducer transcripts in non-monomial cases.

## Attempted claim

Sharp threshold theorem at order 24: exact M-group dichotomy for all 15 groups of order 24 from presentations — each group classified monomial or not; every monomial nonlinear irreducible carries an explicit inducing pair (H generators, linear lambda values) with induction inner product 1; every non-monomial group carries at least one certified non-monomial irreducible chi* with an exhaustive transcript (all subgroup-conjugacy representatives x all linears, scalar products against chi* all !=1); in particular SL(2,3) is exhibited as a minimal-order non-monomial witness with full certificate.

## Research outcome

Certified minimal non-monomial witness SL(2,3): presentation, Q8:C3 structure, class sizes, degree multiset, and a counting proof that all degree-2 irreducibles are non-monomial (no order-12 subgroup), replayable via VERIFY.py.

## Why this attempt failed

Failed axes: originality, value.

originality: Headline mathematical fact is not new. Candidate's own admission concedes it: topic.json motivation calls SL(2,3)=Q8:C3 'the classical minimal example', rejection_risks states 'SL(2,3) non-monomiality is folklore', DRAFT Sec 'Minimality context (quoted background)'. Class sizes, degree multiset {1,1,1,2,2,2,3}, Q8 derived subgroup, abelianization C3, and absence of order-12 subgroup (equivalently A4 quotient has no order-6 subgroup) are standard stored/published facts: CTblLib stores finished ordinary Irr values from which degrees are readable, SmallGrp supplies the 15 order-24 groups, GAP manual documents induction/ScalarProduct/IsMonomialGroup methods. The delivered proof is the textbook index-counting argument (degree 2 needs index 2), not the promised novel exhaustive per-subgroup scalar-product sweep (DRAFT explicitly says 'no per-subgroup induction scalar-product sweep were needed: the index-2-subgroup counting argument subsumes them'). The genuinely new claim in admission — complete 15-group dichotomy with both-direction certificates — was not delivered (DRAFT 'What is NOT claimed'). A failed arXiv search and a new replay log do not establish priority. Substantive comparison shows no new theorem, no new (non-)inducibility transcript beyond elementary consequence of known subgroup lattice. value: As delivered, the result is a correct machine-checked replay of a textbook extremal witness, not an independently retrievable new finding. The natural object (SL(2,3)) and invariant (non-monomiality, degrees, classes) were motivated before computation, but the precise values are already known, citable from textbooks and readable from CTblLib/SmallGrp, and the index-2 argument is mechanically implied by the known subgroup structure. A future researcher needing SL(2,3) non-monomiality, its degrees or class sizes would cite standard references/libraries, not this certificate. Certification alone does not rescue it per shared standard. The specific presentation/normal-form choice is one among many, not shown to be needed before computation. The value-bearing promise — complete 15-group threshold dichotomy calibrating Taketa generalizations — is honestly described as incomplete and therefore cannot confer value on the fallback alone. This is a textbook restatement with verification, which must be rejected even though correct.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: ['Full 15-group order-24 M-group dichotomy NOT proved; only the SL(2,3) extremal witness (admission fallback) is certified.', 'Minimality of order 24 over all smaller groups is quoted background (Taketa line), not proved.', 'No explicit degree-2 character values; non-monomiality via index counting, not per-subgroup scalar-product sweep.', 'No GAP/Dixon-Schneider used (GAP unavailable); character theory replaced by counting + one exhibited integer character.']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
