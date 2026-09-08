# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Auditable portrait census for postcritically finite monic centered cubics with critical periods <= 4: complete realizability table plus one certified obstructed-vs-realized gap
- **Round:** 2026-09-07-first-light-01
- **Lane:** 145
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Complex Dynamics
- **Method:** Hubbard-tree enumeration with Thurston-pullback verification and dynatomic-resultant elimination

## Problem

Let f(z)=z^3+a z+b with critical points c1,c2. Restrict to postcritically finite maps where each critical orbit is preperiodic with exact period <=4 (periodic or strictly preperiodic landing on a cycle of period <=4). Enumerate all abstract cubic critical portraits in this window up to affine conjugacy, and for each portrait decide realizability: either exhibit explicit (a,b) with certified critical-orbit logs, or exhibit a Thurston obstruction (Levy cycle) certificate. Target: a complete period<=4 portrait table plus one extremal gap pair — one provably obstructed portrait and one adjacent realizable portrait — certified by Hubbard-tree combinatorics, Thurston-pullback logs, and dynatomic resultant elimination replayable from committed integer data.

## Attempted claim

Complete classification: the finite list L of abstract cubic critical portraits with critical periods <=4 up to conjugacy, with each entry marked REALIZED (with explicit monic centered polynomial coefficients a,b and verifiable critical-orbit period logs) or OBSTRUCTED (with an explicit Levy-cycle / Thurston-obstruction log), including at least one certified obstructed portrait and one certified realized neighbor forming a realizability gap; verified by Hubbard-tree enumeration + Thurston pullback + dynatomic resultant elimination.

## Research outcome

Verified partial cubic portrait census: unique symmetric bicritical fibers, one realized tail portrait, unicritical exact-period counts 1/1/4/12 for n=1..4 with explicit n=1,2 realizers, and one fiber-empty portrait — all replayable from committed integer data; full period<=4 list L and Levy-cycle certificates remain open.

## Why this attempt failed

Failed axes: originality, value.

originality: The promised delta — complete period<=4 list L with per-portrait Levy-cycle logs, explicit (a,b) realizers and resultant elimination — is explicitly absent (DRAFT Sec.3 admits no L, no Levy certificate, no general a!=0 resultants). What remains is substantively implied by prior general theory plus routine algebra, not a new classification. Nearest priors: Poirier math/9305207 gives the critical-portrait framework of which (a)(b)(d) are one-line linear substitutions f(c)=c*2a/3+b; Floyd et al. 2105.10055 proves every abstract polynomial portrait is realized topologically and classifies unobstructed-only cases, so the general realizability criterion already exists and the single linear-incompatible portrait (c fixed, -c->c) is a trivial fiber-emptiness from e1-e2=4ACc/3, not a new Levy obstruction type and not the claimed adjacent Thurston pair; Blokh et al. 2304.11516 and Thurston et al. 1906.05324 give cubic-locus/portrait tools, not a census, but standard unicritical dynatomic theory (deg f^n(0)=3^{n-1}, Moebius quotient, oddness=>evenness) mechanically implies deg Q3=8, deg Q4=24 and counts 4,12 up to b~-b — a parameter substitution (n=3,4) any expert reproduces in minutes. The symmetric cubics z^3-3z (Chebyshev-type, 1->-2 tails) and z^3+/-1.5z are classical PCF examples, not new witnesses. No source was found publishing the same partial table verbatim, but a failed search does not establish priority; substantive comparison shows textbook restatement + routine dynatomic degrees, not an independent finite-window completeness or new gap extremal. value: The independently valuable headline — complete realizability table plus certified obstructed-vs-realized Levy gap locating first bicritical obstructions — is missing by the authors' own admission. The remaining fragment does not advance the recognized Thurston-rigidity/Hubbard-tree/cubic-locus question: (a)(b) are two rational symmetric fibers solvable by linear equations; (c) is standard unicritical degree arithmetic (1,1,4,12) with n=3,4 existence non-constructive and no boxes/minimal polynomials; (d) is linear incompatibility, not a Levy cycle, and paired gap is algebraic-combinatorial, not the targeted Thurston gap. These are mechanically implied exact data any future researcher recomputes instantly from definitions, not precise facts reasonably needing retrieval (e.g., z^3-3z tails and unicritical degree counts are exercises). Certification via sympy replay is correct but does not rescue an arbitrary narrow slice under the stated standard. The partial table plus dynatomic fragment, while honestly described, is an unexplained enumeration fragment / textbook restatement with tiny unmotivated scope (three symmetric points + unicritical line) and no demonstrated downstream calibration use beyond assertion. Intrinsic low value and missing substantive result; no bounded addition without new research (full L, Levy logs, general resultants) would create the claimed value.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Partial census only: no complete portrait list L, no mixed-period/tail enumeration, no general a!=0 dynatomic resultants; obstruction proved by elementary fiber emptiness, not by Levy-cycle/Thurston-matrix log; periods 3-4 unicritical existence non-constructive (no isolating boxes/minimal polynomials); gap pair is algebraic-combinatorial, not an adjacent Thurston-obstructed pair.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
