# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Schmidt-winning fiber of Bad on the explicit rational line
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1005
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Diophantine Approximation
- **Method:** Schmidt interval-game strategy versus resonant-cover analysis

## Problem

Decide whether the fiber Bad(1/2,1/2) intersected with the explicit rational line L0={(x,x/2+1/3): x in R} is 1/2-Schmidt-winning when played on L0: Alice has a strategy guaranteeing the limit point x* satisfies (x*,x*/2+1/3) in Bad(1/2,1/2) with some uniform constant c>0 independent of the play, equivalently the restricted HAW property on this slice.

## Attempted claim

Bad(1/2,1/2) cap L0 with L0: y=x/2+1/3 is 1/2-Schmidt-winning in the line topology: there exists an Alice strategy whose limit points all lie in Bad(1/2,1/2) with a uniform constant, certifying the rational-line fiber as game-abundant rather than exceptional.

## Research outcome

Disproved the target: Bad(1/2,1/2) cap L0 is empty via the q=6m resonance plus Dirichlet, hence not 1/2-Schmidt-winning.

## Why this attempt failed

Failed axes: originality, value.

originality: FAIL: the headline emptiness is substantively implied by a known stronger theorem, not new. An-Beresnevich-Velani arXiv:1409.0064 Remark 4 Eq (1.5) proves Bad(i,j) cap L_{a,b}=EMPTY if liminf q^{1/sigma} max(||qa||,||qb||)=0 with sigma=min(i,j), with full dual-form proof in the paper. For i=j=1/2, sigma=1/2, and for rational a=1/2,b=1/3, q=6k gives max=0 so liminf=0 trivially; emptiness follows by 2-line substitution. The draft's q=6m+Dirichlet argument is the same resonance repackaged in simultaneous form. ADMISSION_DEFECT: topic audit_preflight and Admission claimed no prior implication decides this slice and that Diophantine hypotheses leave the rational boundary open, missing this explicit emptiness criterion in the same paper that decides all rational lines. value: FAIL: the negative resolution is vacuity plus parameter substitution into a known general criterion, which the STANDARD and TARGET policy expressly deprive of value even when literally false. The stronger result proved is that the fiber is empty, so non-winning holds vacuously; admission preflight falsely certified nonvacuity (claimed small-height checks leave admissible intervals and both outcomes substantive), which the elementary q=6m resonance refutes. ADMISSION_DEFECT: cheap-falsification/target-integrity preflight outcome is false. Instantiating the published (1.5) at a=1/2,b=1/3 adds no new boundary, method, or downstream datum; a future researcher needing this fact would cite the general rational-line emptiness criterion, not a one-line record. Certification/replay alone does not create value.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Disproof uses the standard simultaneous sup-norm normalization of Bad(1/2,1/2) with exponent 1/2; equivalent normalizations change only the threshold constant 24/c^2, not the conclusion. The argument is specific to the named line y=x/2+1/3 (denominators 2 and 3 cleared by q=6m) and claims nothing about other rational or Diophantine lines, dual/multiplicative Bad sets, or Hausdorff-measure refinements, which remain out of scope.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
