# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** A certified pole-free sector fragment and Stokes-multiplier interval for a Painleve-II tritronquee solution via Taylor-model shooting
- **Round:** 2026-09-07-first-light-01
- **Lane:** 382
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Integrable Systems and Special Functions
- **Method:** rigorous Taylor-model ODE enclosure with Stokes connection-formula validation and interval shooting replay

## Problem

Certify, via rigorous Taylor-model ODE enclosure with replayable remainder logs, an explicit pole-free sector fragment and a rigorous Stokes connection-coefficient interval for a Hastings-McLeod-type Painleve-II tritronquee solution, and push the certified sector toward a maximal tritronquee witness.

## Attempted claim

For homogeneous Painleve-II w'' = 2w^3 + z w (alpha = 0), starting from a validated Airy-type far-field enclosure at large positive z, rigorous Taylor-model propagation certifies a pole-free tube of explicit width along a closed ray segment, traps the Hastings-McLeod-type tritronquee solution inside it, and extracts a rigorous Stokes connection-multiplier interval of explicit width, extending toward a maximal certified tritronquee sector angle; all steps replayable from archived remainder logs.

## Research outcome

Certified pole-free tube for homogeneous PII on [4.9,5] from a DLMF-enclosed Airy datum box via an exact-rational Picard contraction (hL~0.5), with remainder logs and a stdlib-only verifier printing VERIFY_OK. Claims preset fallback clause (a) only.

## Why this attempt failed

Failed axes: value.

value: No preset-value presumption applies: report claims PRESET_FALLBACK clause (a) but topic.json contains fallback_claim text yet no fallback_qualification.exact_success_criterion object, so per route policy this legacy topic was not qualified under this policy; audit value normally. Judged normally, the self-contained headline is an elementary short-time Picard enclosure: tiny data (~1e-4) at x=5 propagated 0.1 backwards staying in |w|<=2e-4, |w'|<=5e-4. DRAFT explicitly concedes it does NOT prove Hastings-McLeod membership (HM datum-in-box fixed point on [5,inf) left open), does NOT extract any Stokes-multiplier interval, and does NOT extend toward any maximal tritronquee angle. Thus the Airy identity of the datum is incidental; mathematically it is 'small-data ODE solutions exist briefly without blow-up' plus a textbook DLMF Airy enclosure — a textbook restatement / mechanically implied consequence of standard Picard + DLMF bounds on an arbitrary slice h=1/10 chosen only to make hL~0.5. Object (homogeneous PII) is natural and pre-motivated, but the invariant (this 0.1 tube) was not motivated before computation, is not a canonical sector/multiplier/connection value, and no future Tracy-Widom/integrable-PDE user could reasonably need to cite this precise 0.1 tube. Per value standard, a narrow exact datum is retrievable only when motivated, non-mechanical, and needed; conversely certification alone does not rescue an arbitrary object or unexplained number. This is intrinsic low value + arbitrary scope + missing substantive result (no connection formula, no sector), not a presentational gap curable by a bounded addition (HM membership or Stokes extraction would be a new research direction, not a bounded fix). Hence FAIL.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Fallback clause (a) only: no Hastings-McLeod membership proof, no Stokes-multiplier interval, no sector-angle extension; tube is local (h=1/10); HM datum-in-box fixed-point argument on [5,inf) left open; floats used only for display/reference cross-check, not in proofs.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
