# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Insertion-bounded transfer-matrix growth bound and extremal stability for the 1324-avoiding slice
- **Round:** 2026-09-07-first-light-01
- **Lane:** 658
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Enumerative Combinatorics
- **Method:** insertion-encoding transfer-matrix with singularity analysis of generating functions

## Problem

Let Av(1324) be the 1324-avoiding permutation class and E_k its insertion-encoding slice of slot-depth <= k (regular language with finite automaton by Vatter theory). Determine a lowered exponential upper bound on the depth<=3 slice E_3 via its transfer matrix and classify the extremal subclass of E_3 attaining the current lower-bound construction, with stability for near-extremal encodings.

## Attempted claim

Let E_3 be the insertion-depth<=3 slice of Av(1324). Then limsup_{n->infty} |E_3 cap S_n|^{1/n} <= 12, proved by an explicit finite transfer matrix M_3 with rigorous Perron-root enclosure rho(M_3) <= 12, together with a stability classification: every subclass of E_3 with growth > 11 - epsilon is contained in an explicitly described extremal family F (the lift of the current lower-bound construction) up to finitely many encoding deviations.

## Research outcome

Proved the depth<=3 slice bound limsup<=8<=12 via explicit M_3 with rigorous Perron enclosure in (7,8), explicit monotone spine F_0 subset E_3, and stability (eps_0=1, vacuous, transparent) plus a genuine >5-forces-state-3 localization.

## Why this attempt failed

Failed axes: originality, value.

originality: FAIL: headline bound uses zero 1324-specific filtering. M_3 counts all slot-count walks with depth<=3 for any permutation class (m/l/r/f counts per slot), dropping 1324-avoidance entirely; draft admits 'M_3 counts a rigorous superset' and 'M_3 bounds a superset (one-sided only); not an exact E_3 automaton'. Therefore |E_3|<=3*8^{n-1} follows by subset monotonicity from the generic bound for ALL depth<=3 permutations, which is immediate from Vatter's generic definitions (4s letters, slot transitions s->s+1/s/s-1). Vatter arXiv:0911.2683 provides the general insertion-encoding alphabet and accepting-automaton method; instantiating its slot-transition counts at s=1,2,3 yields M_3 with no new 1324 idea. No fused source states the number 8 for E_3, but a prior source need not state headline verbatim: generic definitions substantively imply it as a one-step corollary/repackaging of a stronger generic fact. F_0 avoidance (increasing avoids 1324) is textbook; localization is generic linear algebra on the same generic submatrix. Full-class uppers (Claesson-Jelinek-Steingrimsson <=16, Bona (7+4sqrt3)~13.93, Bevan et al. 13.5) indeed imply only E_3<=13.5, not <=8, so they do not cover — but generic slot counting does. Hence claim is a corollary/repackaging, not a new 1324 lemma. Failed search alone does not establish priority; mechanical implication defeats novelty. value: FAIL: textbook restatement + vacuous classification. (1) Bound <=8<=12 is generic alphabet/slot counting ignoring 1324, applicable to any pattern; no 1324 structure, no refined state splitting tracking increasing subsequences as hypothesized, no transfer-matrix singularity analysis of a true E_3 automaton. Crude universal cap, far above true E_3 growth, gives no 1324 insight. (2) Stability: admitted target required classification of >11-eps subclasses into explicit extremal family F (lift of current ~10-growth lower-bound construction). Delivered eps0=1 threshold 10 above proven cap 8, so antecedent empty; any F (including growth-1 identities) vacuously satisfies. F_0={id_n} growth 1 is not the ~10-growth lift; draft's 'shared monotone spine' relabel does not supply it, and admits 'no ~10-growth family can live in E_3'. Non-vacuous lemma (>5 forces state 3) uses threshold 5, not 11-eps, and is again generic. Thus no near-extremal region localized, no extremal mass explanation, no reusable 1324 template beyond generic counting, no sharpened target interval for full constant (slice bound does not improve full-class bound; 'extremal mass cannot live in E_3' is generic: any >8-growth family must use depth>=4 for any pattern). Narrow-datum test fails: object motivated, but value mechanically implied and not needed as precise 1324 fact. Honest disclosure of vacuousness does not create value. Intrinsic low value, not a bounded presentation fix.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: M_3 bounds a superset of slice walks (one-sided upper bound only); not an exact E_3 automaton and not the exact E_3 growth. Stability implication with eps_0=1 is logically valid but vacuous, stated transparently; the non-vacuous structural content is the >5-forces-state-3 localization. No full-class 1324 constant claimed. F_0 has growth 1; no ~10-growth family lives in E_3 given the cap of 8.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
