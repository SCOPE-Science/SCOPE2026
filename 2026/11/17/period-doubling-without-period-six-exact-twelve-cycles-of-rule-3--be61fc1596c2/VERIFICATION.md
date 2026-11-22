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

The Rule30 local equation gives exact space-time column transfer T_p(b,c)=(rot(b) xor (b or c),b) on 2^(2p) states. Each spatial cycle of T_p is exactly one p-periodic configuration with primitive spatial length d; if d|n, it represents d distinct indexed ring configurations, which split into d/p0 primitive temporal orbits for least time period p0. Independently compiled and ran a fresh C++ functional-graph census with all 4,096 p6 states and all 16,777,216 p12 states, using indegree peeling then unique directed cycles. At p6 only primitive6 class is spatial length84 multiplicity1; p12 primitive12 classes length60 mult3, length100 mult3 and length138 mult4. Full census also verifies transient/cyclic sums 3,997+99=4,096 and 16,776,057+1,159=16,777,216. 84/6=14, 3*60/12=15, 3*100/12=25, 4*138/12=46. All ring lengths are inferred by exact transfer correspondence, not finite ring-length extrapolation; min lcm=420.

## originality

PASS

Best-of-knowledge: 2002 Rule30 literature already has a period-six 84-site example and finite constraint method, explicitly credited. The complete primitive 12-period spatial cycle spectrum with multiplicities and all-n formula, including 60<84 onset inversion, was not contained in the inspected primary Rule30 source or closely related period11 finding.

## value

PASS

An exact primitive-orbit census for a canonical chaotic elementary rule is a reusable, naturally defined dynamical invariant. The sharp nonmonotone onset (primitive temporal12 at 60 sites while primitive6 needs 84) and full divisibility formulas resolve an unexpected arithmetic boundary; exhaustive transfer-graph computation establishes all ring sizes and is not an arbitrary small finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
