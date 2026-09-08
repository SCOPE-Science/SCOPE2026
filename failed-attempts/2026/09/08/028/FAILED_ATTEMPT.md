# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Frontier merit-factor record for Littlewood polynomials at length 67 versus the pinned best-known optimum
- **Round:** 2026-09-07-first-light-01
- **Lane:** 120
- **Disposition:** NO_RESULT
- **Domain:** Harmonic Analysis
- **Method:** unrestricted memetic tabu and self-avoiding-walk heuristic with exact integer autocorrelation verification against pinned best-known optimum

## Problem

Exhibit an explicit Littlewood +-1 polynomial of length 67 (degree 66), eps in {+-1}^67, whose aperiodic energy E=sum_{k>=1} C_k^2 is strictly below the pinned best-known optimum E_best(67) (equivalently merit factor F=67^2/(2E) strictly above F_best(67)), where the comparator is pinned from published exact/best-known LABS tables before search and the inequality is verified by exact integer autocorrelation recomputation.

## Attempted claim

There exists an explicit eps* in {+-1}^67 with aperiodic autocorrelations C_k=sum_{j} eps_j eps_{j+k} and energy E*=sum_{k=1}^{66} C_k^2 satisfying E* <= E_best(67)-1, equivalently F*=67^2/(2E*) >= F_best(67)+0.05, where E_best(67)/F_best(67) is the best-known optimum pinned from Mertens plus current LABS best-known tables (including Zhang et al.) before search, verifiable by exact integer recomputation of the full C_k vector from eps* plus the pinned-comparator log.

## Research outcome

N=67 LABS frontier: no new record and no tightened interval. Pinned best-known E_best(67)=241 (Packebusch-Mertens skew optima, exactly re-verified with full C_k vector) could not be beaten (best heuristic E=469), and the fallback strict lower-bound tightening failed: a main-pass 'LB=34' was found to rest on a chain-truncation bug (parity-violating) and withdrawn; corrected full-chain exact censuses certify only the published parity bound LB=33 at depths 6-8. The published optimality interval [33,241] stands unchanged; useful preserved outputs are the exact E=241 verification, the corrected full-chain tight-bound code, and the documented bug withdrawal.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No strict improvement obtained on either side: no N=67 sequence with E<241 was found (best heuristic E=469 unrestricted, E=437 skew spot-check), and no proved lower bound above the published parity bound 33 was obtained — corrected exact border-relaxation censuses (full chains, parity-respecting) yield LB=33 at depths m=6,7,8, and the main-pass 'LB=34' is withdrawn as spurious (chain-truncation bug in work/tight.py: range(20) truncated chains; it reported even min|Ck| for odd-parity lags, impossible). Only the previously published interval [33,241] is certified; comparator value E=241 is a reproduced verification of the Packebusch-Mertens Table-3 skew sequences, not a new record. Lower-bound censuses at m=8 are fully reproduced; deeper depths (m>=9) were not run to completion and no partial-depth result is claimed.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No strict improvement obtained on either side: no N=67 sequence with E<241 was found (best heuristic E=469 unrestricted, E=437 skew spot-check), and no proved lower bound above the published parity bound 33 was obtained — corrected exact border-relaxation censuses (full chains, parity-respecting) yield LB=33 at depths m=6,7,8, and the main-pass 'LB=34' is withdrawn as spurious (chain-truncation bug in work/tight.py: range(20) truncated chains; it reported even min|Ck| for odd-parity lags, impos…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
