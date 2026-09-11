# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Certified transverse Kakeya-bush extremizer saturating the three-cap cell estimate
- **Round:** 2026-09-07-first-light-01
- **Lane:** 817
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Harmonic Analysis
- **Method:** constructive-interference overlap count with direct L6 ratio certification

## Problem

Construct explicit functions f_k supported in three fixed transverse R^-1/2-caps on P, each a 0/1 sum of ~R dual wave packets (tubes of size ~R^{1/2} x R^{1/2} x R) all meeting a common central ball B_{R^{1/2}}, such that the trilinear L^6 ratio ||(prod|E f_k|)^{1/3}||_{L^6(B_R)} / prod||f_k||_2^{1/3} is >= c1 (log R)^-C1 times the known cell-term upper bound, with explicit c1, C1 at R=2^10.

## Attempted claim

An explicit 0/1 wave-packet bush from three transverse caps achieves central overlap >= cR and L^6 ratio within (log R)^C1 of the cell upper bound, proving the partitioning cell step sharp at that scale.

## Research outcome

Certified explicit transverse 3-cap 0/1 bush at R=1024: 3R central tube overlap and trilinear L6 ratio pinned in [0.112,1.28], within (log R)^2 of the cell envelope (c1=1,C1=2). Fully tabulated and script-verified.

## Why this attempt failed

Failed axes: originality, value.

originality: TARGET route: audited normally, no preset presumption. Fused live retrieval (SerpBase 10 + OpenAlex 15 + Crossref 15 per query, 20 deduplicated results, no partial failure) finds the exact prior sharpness theory the claim repackages. Bennett 2004 sharp trilinear paraboloid inequality, Bennett-Carbery-Tao 2006 d-linear restriction/Kakeya, Guth 2010 endpoint + 2014 short multilinear Kakeya proof, Demeter Ch.10 almost-extremizers (Knapp/transverse), and Ponce-Vanegas sharp transversality dependence together prove O(1) trilinear upper bound for all transverse sets and exhibit sharpness via the standard transverse indicator example (coherent phase on O(1) ball). Draft's L in [0.112,1.28] is that standard transverse-indicator calculation evaluated at one scale R=1024 with elementary cos/volume bounds; 3072 'tubes through origin' are assigned by fiat (origin_dist 0 in table) with no concentration proved, adding no new geometric content beyond drawing lines through a point. A prior source need not state 'R=1024, 3072 tubes, 0.112' verbatim: BCT/Bennett sharpness substantively implies Theta(1) ratio for transverse indicators, exhaustively covering the headline as a special case up to explicit constants. Exact table absence does not establish priority because the table is trivial assignment. Hence recomputation/certificate/corollary/repackaging of a known stronger fact. FAIL. value: TARGET, so no admission presumption. Strongest self-contained headline is one-scale interval L in [0.112,1.28] for indicators of three fixed transverse caps plus by-construction 3R line overlap. Object (transverse caps) is natural and pre-motivated, but invariant is mechanically implied by textbook transverse sharpness example: coherent-phase lower bound on B_10 and trivial L-inf envelope give Theta(1) with no new idea; precise numbers 0.112/1.28 and arbitrary 32x32 (R^-1) tiling / 3072-row table are not needed by any future researcher beyond the known O(1) sharpness, and tube table carries no wave-packet mass (draft admits analytic bound uses only full f_k). Upper side U=1.28 is disclosed as trivial pointwise envelope, not a named literature cell constant, so 'any finite cell bound matched' and 'partitioning cell step sharp' mislabels a trivial bound as the deep cell term; no asymptotics, no log-power optimality, no wall term, no downstream theorem uses the exact datum. This is textbook restatement + parameter substitution (R=2^10) + unexplained enumeration (3072 assigned lines) even if correct and new as numbers. Certification alone (rerunnable asserts) does not rescue arbitrary scope/unexplained number under the stated policy. FAIL.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Finite single scale R=2^10 only; no asymptotics in R; log power 2 not shown optimal; upper side is the trivial pointwise envelope (any finite cell bound at this scale), not a named literature cell constant; wall term untouched.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
