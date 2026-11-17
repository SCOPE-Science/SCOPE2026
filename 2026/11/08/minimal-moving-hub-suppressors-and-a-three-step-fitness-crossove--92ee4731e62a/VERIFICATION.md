---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Defined the actual birth-death transition on three-bit mutant masks with fitness-proportional parent and uniform neighbor replacement, including self-loops. Two connected phases yield a 6x6 transient backward system for the boundary-aligned 2tau-update product. Independently solved this system in exact fractions at 30,58,86,114 positive integer fitness values respectively for tau=1..4, matching the claimed rational A_tau/B_tau certificate and verifying the coefficient identity for S_tau. The original proof establishes the rational numerator/denominator degree bound <=24tau by Cramer on entries with denominator ((r+2)(2r+1))^(2tau), so cross-multiplication has degree <=28tau+1; those 28tau+2 distinct exact rational checks prove identity for all r>0, not just finite samples. S1,S2 have strictly negative coefficients, S4 strictly positive; S3=r^5 H(r+1/r-2) with H(0)<0 and all positive higher coefficients yields exactly one root r*>1 and reciprocal. Static constituent path formula checked separately, and minimality of three sites follows from uniqueness of a connected 2-vertex simple graph.

## originality

PASS

The switching-network matrix framework and effects for a path-to-triangle switch are acknowledged prior. The exact two-individually-amplifying P3 moving-hub pair, all-real-fitness universal signs for tau=1,2,4, and sharp unique tau=3 crossover are not covered by the inspected earlier mathematical statements.

## value

PASS

The all-fitness signs demonstrate that two individually amplifying static networks can jointly suppress selection at short dwell times, then amplify at longer dwell times; a single precise three-step fitness crossing is a genuinely informative threshold. The network has the smallest nontrivial connected switching pair, and exact positivity-polynomial certificates permit reliable parameter comparison beyond numerics. Neither generic Markov solvability nor tau=1 neutral inspection gives this selection-reversal phase diagram.

The dated certificate retains the supplied scientific assessment, sources and limitations.
