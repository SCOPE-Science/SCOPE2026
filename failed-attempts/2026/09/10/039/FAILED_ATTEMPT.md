# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Constant-size Index lifting for bit-pigeonhole search with monotone formula size corollary
- **Round:** 2026-09-07-first-light-01
- **Lane:** 598
- **Disposition:** NO_RESULT
- **Domain:** Proof Complexity
- **Method:** constant-size Index disperser/stifling lifting analysis with Karchmer-Wigderson monotone interpolation

## Problem

Determine whether deterministic query complexity for the bit pigeonhole search problem lifts to two-party communication with a constant-size Index gadget: prove a linear randomized (target) respectively deterministic (fallback) CC lower bound for Search(BPHP_n) o IND_3^N with explicit constants and derive the monotone formula size corollary, or certify a small-cost protocol/disperser obstruction reshaping the constant-gadget lifting threshold.

## Attempted claim

Let BPHP_n be the bit pigeonhole principle with n+1 pigeons and n holes for n a power of 2, with N=(n+1)*log2(n) query bits, and let F_n = Search(BPHP_n) o IND_3^N where IND_3 is the constant-size Index gadget (Alice holds 1-bit pointer i, Bob holds 2-bit string y, output y_i). Then for every n >= 16 a power of 2, the randomized two-party communication complexity R^{cc}(F_n) >= n/16, hence via Karchmer-Wigderson the associated monotone Boolean function requires monotone formula size at least 2^{n/16}. Binary test: the stated inequality for all such n with a logged lifting-plus-KW certificate.

## Research outcome

Target (randomized R^cc(F_n)>=n/16) blocked: IND_3 fails all known lifting hypotheses (discrepancy 0.25, mono-rectangle density 0.25, rank 2, D=1) and direct routes give only DT(BPHP_2)=3, O(log n) counting, no sampling refutation. Preset fallback (deterministic D^cc(F_n)>=n/16 for all n>=16 via disperser-plus-simulator) attempted with 3 bounded routes and blocked: counting proves it only for n<=256 with hard gap at n=512; required method certified inapplicable; no refuting protocol. CLEAN_EXIT with no original increment.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['Neither target nor fallback proved or disproved; residual is the documented open constant-size Index lifting conjecture (Beame-Koroth).', 'Computed evidence consists of small exact censuses (2x4 gadget, 3-bit minimax) and elementary counting/birthday arithmetic, not a lifting proof.', 'No refuting protocol found for either claim; binary tests remain open at n>=512 (fallback) and all n>=16 (target).']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['Neither target nor fallback proved or disproved; residual is the documented open constant-size Index lifting conjecture (Beame-Koroth).', 'Computed evidence consists of small exact censuses (2x4 gadget, 3-bit minimax) and elementary counting/birthday arithmetic, not a lifting proof.', 'No refuting protocol found for either claim; binary tests remain open at n>=512 (fallback) and all n>=16 (target).']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
