---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For unrestricted deterministic k-symbol feedback, existence iff every pair of equal cyclic k-factors has identical next symbol; thus M=1+max length of equal factors with different successors. With nonzero support {0,d}, unequal symbols preclude matching nonzero contexts, while equal symbols with d<L permit one aligned spike and at most 2d-1 common letters; the zero-run conflict has length L-2. The antipodal same-symbol word has primitive period d. These sharp witnesses yield M=max(L-1,2d),L-1,d-1,d in the four cases stated. Cyclic pair counts n for d<n/2 and n/2 for d=n/2 prove the entire q-ary polynomial for all n>=4. The d=1 boundary and smaller-period exception are included.

## originality

PASS

The classical successor-conflict criterion and published high-complexity binary classes are credited. Exact q>=3 colored two-spike distance classes and full period-word polynomial are not given by the inspected general/binary papers. A generic algorithm for arbitrary sequences does not assert this explicit classification. Best-of-knowledge acceptance retains unindexed predecessor risk.

## value

PASS

A natural complete low-Hamming-weight census of shortest unrestricted nonlinear feedback registers, with genuinely different equal/unequal spike colors and a sharp antipodal primitive-period exception; this exact probability distribution can be reused in low-weight complexity/coding work without re-enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
