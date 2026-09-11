# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Distality decision for the three-variable translate-incidence cell in (R,<,+,alpha^Z) with transcendental alpha
- **Round:** 2026-09-07-first-light-01
- **Lane:** 704
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Mathematical Logic
- **Method:** distal cell decomposition with indiscernible-sequence shattering analysis

## Problem

Fix alpha_*=e (>1 transcendental) and G=alpha_*^Z as a unary predicate. Let M=(R,<,+,G). Decide distality of the partitioned three-variable translate-incidence formula phi(x1,x2;y) := G(x1-x2+y) (|x|=2,|y|=1) by producing a machine-checkable certificate: either a distal cell decomposition (strong honest definition with explicit bound) or a non-distal indiscernible-sequence obstruction. Uses only +,<,G; avoids Schreier-graph games, Tseitin restrictions, and number-field geometry.

## Attempted claim

For M=(R,<,+,G) with G=e^Z, decide the partitioned formula phi(x1,x2;y):=G(x1-x2+y): produce either (i) an explicit strong honest definition for phi with finite bound N and fiber-count log proving phi distal, or (ii) an explicit indiscernible sequence (a_i)_{i in I1+(c)+I2} with I1,I2 infinite without endpoints and parameter b such that (a_i)_{I1+I2} is b-indiscernible but phi-truth on increasing tuples through a_c differs, with combinatorial log (order-type, finite indiscernibility checks, truth table). Completion is binary: verifier replays the filed certificate and returns PASS/FAIL.

## Research outcome

phi(x1,x2;y)=G(x1-x2+y) in (R,<,+,e^Z) is distal: closed-form SHD with N=2 pairs via e-difference uniqueness; verifier replays PASS; phi0 corollary K=2, VC=2.

## Why this attempt failed

Failed axes: originality, value.

originality: Headline distal decision for phi(x1,x2;y)=G(x1-x2+y) in (R,<,+,e^Z) is substantively implied by prior broader field-distal theorem. Hieronymi-Nell Thm 3.1 proves T_disc distal for (Rtilde,lambda) with lambda for 2^Z; abstract claims general discrete multiplicative subgroup distal; HWX Thm A + survey remark states (Rbar,lambda^Z) NIP/distal for general lambda citing Hieronymi-Nell/Miller. Same proof works for lambda=e with reps 1,e,..,e^{p-1} and monomials e^t, i.e. mechanical 2->e substitution. (Rbar,e^Z) distal implies reduct (R,<,+,e^Z) distal (fewer formulas), hence phi distal. Explicit N=2 formulas/VC=2 are certificate/corollary of known stronger fact, not independent novelty under adversarial checklist. value: TARGET value was dividing-line distal-vs-nondistal decision for transcendental additive-reduct cell. That decision is already implied by broader field (Rbar,e^Z) distal + reduct, so standalone dividing-line payoff evaporates. Remaining explicit N=2/K=2 certificate and VC=2 corollary are certifications/corollaries of known distal fact, not independently motivated before computation in topic (VC not in admission target/fallback qualification as exact invariant goal) and do not meet exact-invariant retrieval clause which requires pre-motivated object+invariant; they are tiny gains/repackaging of known stronger distal theory. Hence no independent retrieval value as TARGET.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Proves formula-distality of phi (hence phi0), not distality of full Th(M) nor classification of all (R,<,+,alpha^Z); cites Hermite transcendence of e; A=empty case uses 0-parameter perp cell; verifier checks bounded exponent windows exactly with general case by proof.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
