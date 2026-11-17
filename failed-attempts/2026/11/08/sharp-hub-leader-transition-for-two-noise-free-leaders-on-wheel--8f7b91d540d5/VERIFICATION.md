---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Wheel automorphisms reduce every two-noise-free-leader choice to a hub–rim pair or two rim vertices at cyclic separation d. Grounding hub and rim yields T_(m-1) with diagonal 3 and off-diagonal -1. Grounding two rim vertices yields two tridiagonal path blocks coupled through the remaining hub; its block Schur complement gives J_rr(d)=h_a+h_b+(1+g_a+g_b)/(m-f_a-f_b). Exact small-size values prove m=3 all pairs tie, 4<=m<=6 maximal-separated rim pairs win, m=7,8 hub/rim wins. The Green diagonal recurrence, Cauchy-Schwarz, and a positive radical bound prove all m>=9. Fresh independent SymPy exact rational inversion of EVERY leader pair for m=3..11 confirmed all minimizer types and m=4 31/30, m=7 954/377. This finite run corroborates but does not prove m unbounded.

## originality

FAIL

DECISIVE exact earlier published result dated 2026-10-25: "The sharp two-leader coherence transition on unweighted wheels" proves the SAME unweighted wheel, SAME two noise-free leaders, SAME inverse grounded Laplacian trace J, identical m=3 tie, 4..6 farthest rim pairs and m>=7 hub+rim pairs, all optimizer counts and even more explicit full inverse-trace formulas. Its complete RESULT.md was read and mathematically compared, not just its title/summary. The assigned Nov 8 theorem is fully covered even though its proof uses a different Schur bound.

## value

FAIL

The wheel hub-transition is a meaningful natural classification in isolation, but it has been fully established with identical optimizer cases and stronger candidate formulas in the Oct 25 published theorem. The assigned Nov 8 record supplies no new mathematical conclusion, natural previously unknown invariant, or distinct parameter regime; independent novelty/value fails notwithstanding correct proof and reproducible calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
