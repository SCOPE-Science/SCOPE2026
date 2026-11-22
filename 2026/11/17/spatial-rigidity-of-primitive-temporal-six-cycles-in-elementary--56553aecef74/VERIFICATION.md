---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

PASS: Reconstructed the exact Rule54 temporal-history graph G_t from the actual RESULT.md (9ed106cc776d4447dafb54f8e2d5433f4bbbad39) and C++17 certificate blob ab572147af3b156207542a954914faf3e4c0a64d. Independently generated all ordered triple edges and Kosaraju SCCs for t=1,2,3,6: vertex/edge counts 4/2,16/20,64/56,4096/4160 and recurrent cycles [1],[1,4],[1],[1,4,8,8,8], with exactly one in and one out per recurrent vertex. Trace powers therefore give Fix(F_n^6)=1+4[4|n]+24[8|n], Fix(F_n²)=1+4[4|n], Fix(F_n³)=Fix(F_n)=1; inclusion/exclusion yields primitive six-period states 24[8|n] and four time orbits on every n≥3. Eight-site recurrent words and temporal traces give least spatial period eight and F³ equals translation four on that class. Finite transfer graph enumeration is exhaustive and algebraic trace identity extends to all ring lengths; direct finite ring checks alone would not.

## originality

PASS

PASS, best of knowledge: 2008 and 2014 Martínez–Adamatzky–McIntosh period-six diagrams and examples on finite rings are acknowledged; the specifically completed recurrent SCC decomposition proving no additional six-period rings and exactly 24 states for every 8|n is not supplied by their selected tables. The 2026 Resultary exact four-period Rule54 theorem concerns a different temporal fixed-point subshift.

## value

PASS

PASS: The unexpected constant number of primitive six-period states for arbitrarily long rings, and the forced eight-site spatial rigidity, are natural exact dynamical classification results, not a mere small-ring sample; the universal divisibility statement contrasts with exponential temporal-four growth.

The dated certificate retains the supplied scientific assessment, sources and limitations.
