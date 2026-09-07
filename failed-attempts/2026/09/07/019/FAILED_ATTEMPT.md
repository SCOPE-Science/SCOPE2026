# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Seeded dot-product census at order 26: hypohamiltonian status and extremal symmetry among Blanusa x Petersen descendants
- **Round:** 2026-09-07-first-light-01
- **Lane:** 23
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Graph Theory
- **Method:** canonical augmentation generation with nauty hashing and exact Hamiltonicity-cycle filtering with witness logs

## Problem

Close one seeded order-subfamily: enumerate up to isomorphism (nauty canonical-hash dedup) all distinct cubic bridgeless graphs of order 26 obtainable as a single Isaacs dot product B18_i . P10 (both orientations; B18_i in {both Blanusa 18-vertex snarks}, P10 = Petersen), over Aut-representative independent edge-pairs in the edge-factor and adjacent vertex-pairs in the vertex-factor; for each descendant compute girth, |Aut|, and snark status and decide hypohamiltonicity by exact Hamiltonicity testing (G non-Hamiltonian plus all 26 G-v Hamiltonian with explicit witness cycles; every non-witness gets a named obstruction). Screen hypotraceability secondarily. Order 26 is the unique single-dot-product order in {22,24,26} from seeds {10,18,20} by n1+n2-2 arithmetic; orders 18-20 and general existence to 36 are already censused, so this is the precise gap subfamily closable by constrained generation in two hours.

## Attempted claim

At least one explicit order-26 cubic hypohamiltonian descendant of Blanusa-18 x Petersen-10 dot products with a within-family extremal parameter (minimal or maximal |Aut|, with confirmed girth-5 invariant tuple distinguishing it from Petersen, both Blanusas, and Flower J5), delivered as an explicit adjacency list with nauty canonical hash, girth/|Aut|/snark certificate, proof of non-Hamiltonicity of G via exhaustive search log, and 26 explicit Hamiltonian cycles (one per G-v).

## Research outcome

Closed the Blanusa x Petersen order-26 dot-product subfamily: 1280 orbit candidates -> 109 non-isomorphic cubic bridgeless girth-5 snarks, 87 hypohamiltonian, with explicit minimal-symmetry (|Aut|=1) hypohamiltonian snark witness (rep 8) carrying 26 verified G-v cycles and triple-checked non-Hamiltonicity, plus full obstruction list for 22 non-witnesses. All decisions dual-solver verified and replayable in seconds.

## Why this attempt failed

Failed axes: value.

value: Correct and narrowly new but not independently worth finding later. (a) Snark status for all 109 is an Isaacs-theorem corollary (dot product of snarks is a snark), not a discovery. (b) Girth is universally 5, identical to all seeds (P10/B18_1/B18_2/J5 all girth 5), no record; global smallest girth-6 hypo is order 25 and no-girth>=7-to-42 constraint is respected but yields no record. (c) Claimed within-family extremal Aut=1 is modal (65/109 ~=60%), not rare or surprising; trivial Aut is generic for cubics. Maximal Aut=8 (2 reps) equals seed B18_2 Aut=8, so not distinguishing. No global symmetry/girth extremality. (d) Draft explicitly admits order-26 hypohamiltonian-snark existence per se was already known, so W26 is not an existence breakthrough, only a provenance instance. (e) 87-vs-22 hypo split is presented without structural explanation: no theorem predicting which edge/vertex/wiring choices preserve hypohamiltonicity, no Fiorini-condition analysis, just brute-force table plus first-non-Ham-v list. This is the paradigmatic unexplained enumeration. (f) Seeded-pair slice defined by n1+n2-2 arithmetic (18+10-2=26 as unique single-product order in 22-26 window) is an artificial parameter substitution, not a natural class like all order-26 cubics/snarks (explicitly out of scope). Regeneration takes seconds-minutes with published scripts, so archival value as dataset is minimal and lacks theoretical payoff comparable to SCOPE successes (sharp bounds, records, coupling proofs). Falls under mere parameter substitution / tiny unmotivated gain / unexplained enumeration, which must be rejected even if correct and new.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: No nauty: used WL (collides on cubics, disclosed) + custom invariant bucketing + explicit isomorphism, not nauty hashes. Hamiltonian non-existence certificates are solver statistics + replayable exhaustive code, not full exponential transcripts. Edge-colouring uses single solver path (Hamiltonicity uses dual+naive). Aut enumeration is worst-case exponential (fast here). Blanusa seeds defined as P.P types (theorem-backed) without external LCF import; B1/B2 label swap possible but pair-as-set is…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
