---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Grid alignment is exact: at boundary j, mF(j/m)=4j(m−j)/m is integer iff m|4j², equivalently q=m/gcd(m,4) divides j² iff R=∏p p^ceil(v_p(q)/2) divides j. Monotone half-sweep counts one hit per target bin plus one for each nonaligned source boundary; for even m two sweeps yield E=3m−m/R. For odd m the central cell straddles the maximum but hits only the highest bin, and each remaining sweep gives E=3m−1−m/R. q|R² yields m/R≤2sqrt(m), equality at m=4k². The arcsine invariant ergodic law follows from conjugacy to circle doubling, so every positive-measure edge is visited infinitely often simultaneously over countably many m. Independently recomputed exact integer interval overlaps for every 2≤m≤255 and further square-family m=256,400,484,576; all match theorem, not extrapolation.

## originality

PASS

Best-of-knowledge PASS for the precise gcd/square-divisibility arithmetic edge count and sharp square-resolution deficit with positive-measure endpoint convention. Kyriakopoulos--Thurner 2007 explicitly includes zero-length endpoint-touch contacts in a four-bin example (10 vs 8 positive-measure edges) and reports approximate mean degree near 3; cannot yield the exact correction with the same convention. Published relevant current Resultary searches found no stronger same-object arithmetic all-resolution theorem. Balaji et al. 2026 same amplitude-bin methodology is a real material priority risk: its full paper could not be accessed by arXiv/OA alternatives, and authorized Oxford source reports disconnected VPN. We read accessible abstract and code references only, not claim full-paper noncoverage.

## value

PASS

For the canonical chaotic logistic map the continuum positive-measure support of equal-amplitude one-step transitions has natural graph size and edge density. The exact arithmetic fluctuation, universal sharp O(sqrt m) deficit and extremal square family resolve a meaningful finite-resolution effect hidden by the established approximate mean-degree law, independently of limited sample itineraries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
