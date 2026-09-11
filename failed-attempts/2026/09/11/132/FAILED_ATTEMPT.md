# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Southeast-polar quarter-plane walk: infinite group and total-walk constant
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1032
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Analytic Combinatorics
- **Method:** singularity analysis of total-walk series with polar drift excursion certification

## Problem

Classify the named southeast-polar small-step model S3={(-1,-1),(0,1),(1,0),(1,-1)} in the quarter plane: prove infinite order of its walk group via kernel uniformization and decide D-finiteness of its total counting series Q(1,1;t) by certifying the excursion growth constant and singular exponent.

## Attempted claim

For S3={(-1,-1),(0,1),(1,0),(1,-1)}, G(S3) is infinite with an explicit infinite-order word, the kernel curve has genus one for 0<t<1/4, and the total series Q_{S3}(1,1;t) is non-D-finite with certified excursion asymptotics e_n ~ kappa*rho^n*n^alpha and irrational alpha separating S3 from D-finite cases.

## Research outcome

Certified infinite-order group word, genus-one kernel on (0,1/4), and exact excursion/total growth upper bounds for southeast-polar walk S3, with full stdlib-only replay scripts.

## Why this attempt failed

Failed axes: correctness, value.

correctness: EMERGENT_FINDING route verified as target-generated (same S3 model, kernel/group methods) so absence from topic.json is not adverse. Reran all four stdlib scripts: GROUP_WORD_OK, TRACEPOLY_OK, GENUS_OK, BOUNDS_OK all reproduce. Sympy cross-check confirms Res_z(f,w-(z^3-2))=T, T irreducible, disc(C)=-16t^3h, disc(E)=-256t^7h, det/tr identities hold mod f. However Theorem 1 proof is incomplete as written: [Q(tau):Q]=5 forces phi(m)=10, i.e. m in {11,22} with DISTINCT minimal polynomials M11=w^5+w^4-4w^3-3w^2+3w+1 and M22=w^5-w^4-4w^3+3w^2+3w-1. Submission checks only Res(T,M11)=3056498369 and claims it excludes both 2cos(2pi/11) and 2cos(pi/11) types, which is false as stated. Res(T,M22)=-67621991909 (nonzero) repairs it, but archived certificate lacks this case. Additionally the claimed rigorous excursion/total separation is invalid: two upper bounds rho_exc<3.61 and rho_tot<3.8285 cannot prove regime separation. Claim is true but proof incomplete and interpretation overstated. value: EMERGENT_FINDING must independently pass value; narrow exact datum can pass only if motivated, not mechanically implied, and reasonably needed later. This ledger fails that test. Infiniteness and genus-one reprove the known BMM/Dreyfus classification for S3 (finite in exactly 23 cases; remainder infinite/elliptic) with a new certificate, and certification alone does not create value per STANDARD. The two growth bounds are one-line textbook Cramer evaluations e_n<=S(x,y)^n and q_n<=S(x,y)^n at arbitrary rationals (0.634,1.487) and (1,1.4142); upper-only bounds with no lower bound or exponent, and upper-vs-upper comparison cannot rigorously separate regimes as claimed. No non-D-finiteness, exponent, or transfer is proved (explicitly disclaimed). The specific T/resultant/fractions are proof artifacts, not downstream-needed invariants; no material benchmark or classification advance beyond the 13 proved polar cases is established.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: This report does not prove the irrational excursion or total-walk exponent and does not prove Q_{S3}(1,1;t) non-D-finiteness; the polar singularity transfer from excursions to total walks remains open. Least-squares estimates rho_tot~3.8277 and box-truncation eigenvalues are heuristics and lower bounds only, not exponent certificates. Results are S3-specific and cover t in (0,1/4) for the genus statement.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
