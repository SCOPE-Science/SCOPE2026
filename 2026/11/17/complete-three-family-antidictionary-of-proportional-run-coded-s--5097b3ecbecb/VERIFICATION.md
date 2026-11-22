---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

PASS. Exact object is the factorial language of finite concatenations of 0^m1^{km}, not the larger frequency shift when k>=2. Every complete interior pair of runs must obey b=ka: excluding 01^r0 forces b=kt, excluding 0^{m+1}1^{km}0 forces a<=t, and excluding 10^m1^{km+1} forces kt<=ka, hence t=a. Edge runs may be extended to complete code blocks, giving avoidance sufficiency. For each three proposed forbidden types, its length-minus-one prefix and suffix are admitted, proving minimality; the distinct initial pairs ensure disjointness. Counts and generating series follow from the three arithmetic progressions; nonregularity follows by intersecting with 00^+1^+0, while a deterministic pushdown can dispatch on the three initial pairs. Independently recomputed exact finite languages and minimal forbidden sets for k=1..3, lengths 3..10 (24 cases) and verified rational series samples; finite corroboration is not the all-k proof.

## originality

PASS

Best-of-knowledge PASS for the complete three-family forbidden-minimal basis and explicit exact counting/formal-language consequences, not for Reyes’s already known generator description, entropy or intrinsic ergodicity. Reyes Section 5 contains a partial forbidden-run obstruction but not the two additional minimal run-mismatch families; the latter and completeness were independently checked against the underlying generator definition.

## value

PASS

PASS. This is a complete exact language invariant for a natural infinite generator family already central in rational frequency-shift dynamics. The two new run-mismatch obstruction types, coefficient-level arithmetic stratification and context-free-versus-regular distinction provide more than a restatement of topological entropy; the exact forbidden basis is useful to admissibility, symbolic dynamics and entropy-gap analysis. Its value does not rely on claiming original intrinsic ergodicity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
