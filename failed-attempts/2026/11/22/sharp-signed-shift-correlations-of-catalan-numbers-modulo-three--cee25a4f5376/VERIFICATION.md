---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The signed digit rule can be recovered independently in F_3[[x]]: the central-binomial generating function B satisfies B^2=(1-x)^(-1), so B=(1-x)B(x^3). Its coefficients therefore have digit weights (1,-1,0). The Catalan generating function C satisfies x C=B^(-1)-1 modulo 3, with B^(-1)=(1-x)^2 B(x^3)=(1+x+x^2)B(x^3). Reading the coefficient at n+1 gives epsilon(n)=s(floor((n+1)/3)). Splitting the correlation of s by its low digit gives all three recurrences in the submission; each positive lag strictly descends, while the zero lag has normalized value one at every depth. Equivalently, alpha(v)=(-1/2)^d(v), where d counts the nonzero balanced ternary digits. For x=n+1, the classes of x mod 3 contribute (3-t) terms at lag q and t at lag q+1. Moving the x-window endpoint from 0 to 3^r flips each of the two signs for fixed h and sufficiently large r (and preserves zeros); hence the product does not change. This verifies exact stabilization on the ordinary, noncyclic blocks. For positive v, |alpha(v)|=1/2 precisely at the powers of three, with value -1/2. Two consecutive positive arguments cannot both be such powers. Finally q=0 gives R(1)=3/4 and R(2)=0, and t=0 gives R(3q)=(3/2)alpha(q), yielding exactly the proposed extremizers. The independent finite replay /tmp/opencode/frozen-digit-correlations.py used the exact integer Catalan ratio, not the digit rule, for the observed sequence; all 656 tested noncyclic correlations agreed with the balanced-ternary predictions. The proof supplies the universal argument.

## originality

FAIL

The underlying signed invariant is mechanically recoverable from a distinct indexed exact table on the same Catalan support and the known digit signs, not merely analogous to a density calculation. The exact table is the target-by-target modular two-sum representation count for the nonzero Catalan indices at every ternary depth. Reflection converts its entries into cyclic unsigned lag counts, and taking lags divisible by three isolates the core 0/1 digit set. For its supported pairs the sign is determined by the parity of the core lag. The fixed-lag endpoint comparison converts these counts into the submitted noncyclic limit by a two-term formula. The extremizers are then the one-nonzero-balanced-digit case of the same elementary ternary product, plus the first two lags from the three residue classes. This is a mathematical implication judgment, not a claim that the signed theorem appears verbatim in the indexed record or that same-day publication establishes temporal priority.

## value

FAIL

The Catalan support and its sparse signed correlation are natural, and the formula is correct. The issue is specific to this result: its new-looking sign statistics are fixed parity transforms of exact same-support pair counts, and the extremal lags follow by counting a single nonzero balanced digit and splitting three residue classes. The fixed-shift boundary cancellation ensures that this transform applies to the stated blocks but leaves no separate uncaptured statistic. The frozen result therefore does not establish a distinct unknown exact invariant or nonroutine classification beyond the documented coverage. No scientifically distinct repaired claim was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
