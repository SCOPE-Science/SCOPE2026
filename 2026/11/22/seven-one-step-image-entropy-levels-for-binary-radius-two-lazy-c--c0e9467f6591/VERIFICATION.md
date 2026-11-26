---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Every length-n output word comes from an input of length n+4, which extends to a bilateral full-shift point. Starting the subset automaton from all four-bit states recognizes exactly these words, counts them once, and makes all live states reachable. Hence a reachable Perron component gives both the correct exponential lower bound and, by finite-matrix growth, the matching upper bound. In the independent replay below, all sixteen state sets (sizes 11–14), both catalogs, all seven polynomial divisibilities and their ordered rational isolating intervals were reproduced; root counts also exclude any larger real root through 2. Exact tests on all 512 nine-bit words per code give precisely 1,3,7,8,12,14 as non-idempotent. Removing the active edge gives t^11(t−1)(t^4−t^3−t^2−t−1) in those six cases; the maximal recurrent component determines the fixed shift entropy. The fixed Perron interval lies below both B and D; the two log gaps agree with the reported approximations. Bit complement doubles every count; in the idempotent cases image equals Fix. This is a proof for one spatial image of the bilateral full shift, not merely agreement at bounded word lengths or a statement about temporal entropy.

## originality

PASS

Supports the complete evaluated census for the centered five-site family, especially the distinct one-step B and D classes with the same fixed entropy and exact populations. Does not confer credit for the known idempotence or fixed-point structure, the automata method, or the numerical D gap in isolation, which is already a corollary for a different asymmetric rule.

## value

PASS

The centered one-flip family is small but complete at a natural radius; the exact comparisons show that equal fixed-state entropy need not imply equal one-step information retention, even among rules with the same neighborhood size and one active transition. Two resolved positive gaps and sharp populations give a concrete benchmark beyond reapplying the idempotence criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
