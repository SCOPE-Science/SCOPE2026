# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Sharp Schmidt-threshold interval for inhomogeneous Bad shift
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1064
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Diophantine Approximation
- **Method:** Schmidt game strategy plus explicit Bob cluster obstruction

## Problem

Let gamma=(e-2,sqrt(3)-1) and Bad^{gamma}_{1/2,1/2} be x in [0,1]^2 with liminf_{q->infty} q^1/2 max_i||q x_i-gamma_i||>0. Let alpha_low=(34 sqrt(2))^-1 and alpha_high=1/12 with beta0=1/2. Decide the conjoined sharp-interval claim: Bad is (alpha_low,beta)-winning for every beta in (0,1) via an explicit Alice tree, AND Bad is not (alpha_high,beta0)-winning via an explicit Bob 12-cluster counter-strategy on a logged scale window.

## Attempted claim

For shift gamma=(e-2,sqrt(3)-1), the equal-weight inhomogeneous Bad set Bad^{gamma}_{1/2,1/2} is (alpha_low,beta)-winning for every beta with alpha_low=(34 sqrt(2))^-1, and is not (1/12,1/2)-winning: Bob has an explicit 12-cluster strategy forcing the intersection point outside Bad, so the critical winning threshold satisfies alpha_low <= alpha_*(gamma) < 1/12.

## Research outcome

Disproved the sharp-interval target by refuting its upper half: Bad^gamma at shift (e-2,sqrt(3)-1) IS (1/12,1/2)-Schmidt-winning via Datta-Shao HAW plus an exact-rational transfer lemma.

## Why this attempt failed

Failed axes: originality, value.

originality: FAIL: Headline 'Bad^gamma IS (1/12,1/2)-winning for gamma=(e-2,sqrt(3)-1)' is substantively implied by a known stronger theorem, not new. Datta-Shao Theorem 1 proves HAW for ALL Lipschitz theta including every constant shift and every weight, hence covers this gamma and w=(1/2,1/2) as a strict special case; standard HAW=>Schmidt-winning plus the elementary 5-line transfer (C1-C4) mechanically yields (1/12,1/2). A prior source need not state the headline verbatim. No new strategy, constant, or census is contributed; certification does not create originality. ADMISSION_DEFECT: topic.audit_preflight decisive_checks claimed HAW gives only unspecified-alpha winning and the 1/12 upper half is logically independent of HAW; Lemma B refutes that preflight because HAW at 1/24 directly implies (1/12,1/2)-winning. value: FAIL: Even though literally false as a conjunction, the target is refuted only by direct lookup plus textbook transfer, which TARGET policy explicitly denies value. Plugging the named shift into Datta-Shao's all-shifts HAW theorem and applying elementary ball-avoidance geometry (move 11R/12, clearance 11/12>=1/8) is a mere parameter substitution / recomputation of a known stronger fact, with DRAFT itself stating 'no computation needed for the logic'. No shift-adapted separation, cluster analysis, or threshold computation decides the tail game; exploratory q=2..8000 statistics are unnecessary. ADMISSION_DEFECT: admission negative_resolution value case promised a threshold-crossing requiring new strategy-plus-counterstrategy computation, but the delivered refutation is a cheap lookup, so value fails per cheap-defect rule despite literal falsity.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The disproof refutes the conjoined target through its upper (U) half and takes no position on whether the lower Alice-at-An-constant conjunct (L) holds under shifting; the Datta-Shao HAW theorem is cited from the published paper (full text consulted) rather than re-proved; the HAW-to-Schmidt transfer lemma is proved here but is an elementary game comparison, claimed only as the refutation vehicle, not as an original theorem.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
