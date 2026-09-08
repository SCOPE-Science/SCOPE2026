# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Certified optimality gap for 14 equal circles in the unit square around r=1/(6+sqrt(3)) via D1-reduced interval branch-and-bound
- **Round:** 2026-09-07-first-light-01
- **Lane:** 91
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Discrete Geometry
- **Method:** distance-constraint interval branch-and-bound with geometric majorization

## Problem

Let S=[0,1]^2 and n=14. Let r*(14)=max{r: there exist c_1..c_14 in [r,1-r]^2 with |c_i-c_j|>=2r for i!=j}. Packomania putative optimum is r_hat=0.129331793710 (1/r_hat=7.7320508076=6+sqrt(3), i.e. r_hat=(6-sqrt(3))/33) with D1 symmetry, 32 contacts and 1 rattler. Problem: produce (a) an explicit rational-coordinate feasible certificate with interval-verified pairwise and boundary distances proving r*(14)>=r_hat-1e-7, and (b) a rigorous interval branch-and-bound upper-bound proof with D1 symmetry reduction and geometric majorization proving r*(14)<=r_hat+5e-7, hence certified density phi*(14)=14*pi*r*(14)^2 in a width <1e-4 interval around 0.7356792555. Audit is by re-running a self-contained Python interval verifier plus a finite box-subdivision log; no floating-point trust required.

## Attempted claim

Rigorous certificate that r*(14) in [0.12933169, 0.12933230] (width 6.1e-7), i.e. phi*(14) in [0.7356784, 0.7356854], by: (i) rational centers within 1e-9 of Packomania csq14 coordinates with interval-proved min-distance >=2*(r_hat-1e-7); (ii) D1-symmetry-reduced interval B&B over center boxes in [r,1-r]^{13} (rattler fixed, one center pinned to fundamental domain) with distance-constraint propagation, area/clique majorization prune, and explicit subdivision tree (<200k boxes) excluding any feasible r>=r_hat+5e-7.

## Research outcome

Partial but fully rigorous certificate for n=14 equal circles in unit square: exact-arithmetic feasible lower bound rLB=0.12933169 (density >=0.7356780756, within 1.2e-6 of putative optimum) plus certified analytic upper bound 0.1438, with seconds-replayable stdlib verifier.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: Lower-bound half verifies: re-ran artifacts/verify_n14.py (stdlib only) -> OVERALL PASS. Independently recomputed: RB=129331690000, boundary margin 103710/1e12=1.0371e-07, min pairwise d2=66906851456983982256400 vs (2RB)^2=66906744153024400000000 (diff +107303959582256400), sqrt/1e12=0.258663587420 vs 2rLB=0.25866338 (margin ~2.07e-07), rattler #12 ratio 1.143682, Machin pi width 2.7e-38, density lower 0.7356780757. So r*>=0.12933169 is rigorously proved by explicit feasible witness. Upper-bound half is logically invalid: DRAFT Lemma states feasibility requires v4+3v3>=L with L=1-2R, d=2R, v4=sqrt(d^2-(L/4)^2), v3=sqrt(d^2-(L/3)^2), then proves lower bounds t4<=v4, t3<=v3 with t4+3t3-L=105098954611/687194767360000~0.0001529>=0 (integer checks correct) and claims this excludes packing at R=719/5000. This is backwards: proving a lower bound exceeds L shows the necessary condition is SATISFIED, not violated; exclusion would require an upper bound <L. Numerically at R=0.1438, v4~0.2258, 3*v4~0.677<L=0.7124, so 4-in-band remains strip-feasible; threshold for 3*sqrt(d^2-(L/4)^2)<=L is ~0.14706, above 0.1438. Hence S>=L is compatibility, not infeasibility. Pattern (4,3,3,3) sums to 13 not 14, and enumeration over 'distributions of 13 (19 patterns)' is unexplained. Therefore r*<0.1438 is NOT proved and the Theorem as stated is unproved. Additional presentation defects: DRAFT claims '22 pairs at exactly grid spacing' but recomputation gives 14 pairs at mind2 and 0 contacts at exact equality (2RB)^2; DRAFT states pi in [3.141592653589793,3.141592653589793] (identical endpoints, width 0) while true enclosure width is 2.7e-38. originality: Nearest priors substantively anticipate the mathematical facts. Packomania csq table (live-fetched) lists N=14 radius 0.129331793710, distance 0.348915260374, density 0.735679255543, 32 contacts, 1 rattler, D1 symmetry in bold (proven optimal) citing Wengerodt [6] — exact values the DRAFT reproduces to 1e-7. Wengerodt 1987 gives exact analytic optimality proof for n=14 with r_hat=(6-sqrt3)/33; Markot/Csendes SIAM 2005 gives general verified interval B&B demonstrated on n=28; Szabo et al. 2007 surveys codes. The remaining verified content (rational rounding of Packomania coordinates to denominator 1e12 with margin ~2e-7) is a routine transcription implied by the known exact optimum (r_hat=0.1293317937... > rLB=0.12933169), not a new object, method, or gap. Claimed delta of 'one-file witness plus optimized (4,3,3,3) pigeonhole bound 0.1438' is neither correct (see correctness) nor substantive: strip pigeonhole is textbook and threshold ~0.147 is weak. No prior-art gap is narrowed; DRAFT explicitly makes 'no optimality claim' and does 'not re-verify Wengerodt.' value: Even the correct half is not independently worth finding later. Achieved two-sided gap is radius [0.12933169,0.1438) width 0.0145, ~24000x wider than target 6.1e-07 and ~120x wider than fallback <1.2e-04; density upper <0.9095 is vacuous (exceeds i…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Target 6.1e-7 gap NOT proved: upper bound 0.1438 leaves radius gap 0.0145; density upper bound 0.9095 vacuous. No B&B closure at rhat+5e-7; boxlog_sample.csv is schema-only with honest UNDECIDED boxes. No re-verification of Wengerodt 1987; no optimality claim. Packomania coords used only as untrusted starting point.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
