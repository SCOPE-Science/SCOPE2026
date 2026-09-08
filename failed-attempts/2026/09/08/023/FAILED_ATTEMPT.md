# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** A certified ECH capacity gap beyond volume and folding for rational ellipsoids into polydisks in the staircase window
- **Round:** 2026-09-07-first-light-01
- **Lane:** 114
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Symplectic Geometry
- **Method:** embedded-contact-homology capacity lattice-point optimization

## Problem

Survey rational 4D embeddings E(1,a) into dilates of P(1,beta) for reduced-fraction a in the Frenkel-Mueller staircase window (convergents/neighbours of 3+2*sqrt(2) with bounded denominators) at one or two fixed rational beta near 1: compute ECH capacities via the Hutchings lattice formula with logged weight sequences, compare against the volume threshold and the folding-construction threshold, and isolate at least one explicit witness index k with a certified gap delta>0.

## Attempted claim

There exists an explicit rational pair (a,beta) in the surveyed staircase window and an explicit index k <= Kmax such that the Hutchings ECH capacity inequality certifies non-embedding of E(1,a) into lambda*P(1,beta) at every lambda <= lambda_vol*(1+delta) and lambda <= lambda_fold*(1+delta) for some explicit delta>0 (i.e., strictly above both the volume bound and the folding-construction bound), with the full capacity vectors, weight expansions, and minimizing lattice paths logged for independent integer-arithmetic replay.

## Research outcome

Certified two hand-checked beyond-volume ECH witnesses (5,1,5: 5/3 vs sqrt(5/2); 6,1,8: 7/4 vs sqrt(3)) and an exact-arithmetic 39-pair census in the Frenkel-Mueller window classifying ECH-decided vs volume-only pairs, with weight-sequence logs, minimizing lattice paths, and packing cross-checks.

## Why this attempt failed

Failed axes: originality, value.

originality: All numerical claims are mechanically implied by the prior Hutchings lattice formulas by finite exact arithmetic. Given (E) and (P), any skilled reader computes c5(E(1,5))=5, c5(P)=3, c8(E(1,6))=7, c8(P)=4 in minutes; the 39-pair census is direct parameter substitution (13 fixed rationals x 3 betas x k<=80) of the same two formulas. No optimal folding threshold is computed -- construction side is the trivial inclusion E(1,a) subset P(1,a) giving lambda<=max(1,a/beta) -- so the admitted delta of a witness strictly above both volume and folding is absent; draft Sec.4 honestly retreats to strictly above volume inside the volume-vs-crude-inclusion gap. Beyond-volume non-embedding at the headline pairs is already entailed by published optimal functions: Frenkel-Mueller arXiv:1210.2266 completely determines E(1,a)-into-cube function with infinite Pell staircase below sigma^2=3+2*sqrt(2) (hence a=5 optimal>volume known since 2012) and 7 exceptional intervals on [sigma^2,7+1/32] (a=6 must be exceptional since valid ECH bound 7/4>sqrt(3) forces optimal>volume); Usher arXiv:1801.06762 shows C_beta|[1,sigma^2] is determined by Frenkel-Mueller work for arbitrary beta, covering beta=6/5,5/4 cases. Hutchings-Beyond treats the opposite direction and refined criteria but does not make routine forward-direction evaluations new. A failed live search does not establish priority; substantive comparison shows the concrete triples are renamings/instantiations of known formulas and known above-volume steps, not a new claim/boundary. value: Independently worth finding later? No. Contribution is a textbook application of known formulas plus a finite enumeration: 39 exact ratios with scope-relative labels ECH-decided vs volume-only-in-scope (k<=80). It proves no staircase fact, no sharpness, no embedding existence, and no folding comparison (acknowledged limitations 2-3). The two hand witnesses restate known above-volume steps of the solved Frenkel-Mueller cube function via a different (ECH) route without improving the known optimal threshold; the remaining census rows are unexplained enumerations with no downstream use beyond replaying the same script. Crude inclusion upper bound max(1,a/beta) (e.g. 5 at headline pair) makes inside-the-gap framing trivial. This falls squarely under the excluded categories: textbook restatement of Hutchings computation, mere parameter substitution over a rational window, and unexplained finite enumeration, even though correct. The fallback census does not materially advance the recognized staircase-decidability question because volume-only verdicts are relative to an arbitrary Kmax=80 and folding/beyond-capacity criteria are not evaluated.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: ['ECH formulas, monotonicity, and packing identity are Hutchings/McDuff prior art; novelty is only the concrete witnesses plus finite census logs.', "Construction side is a crude inclusion upper bound lambda<=max(1,a/beta), not an optimal folding threshold; 'beyond folding' is honestly scoped as ECH strictly improving volume inside the volume-vs-construction gap.", "'Volume-only' verdicts are relative to k<=80; higher k could still yield ECH gaps. No claim about staircase functions, sharpness,…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
