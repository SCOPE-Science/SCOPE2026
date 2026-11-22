---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

The extension is constant-preserving precisely when signed weights sum to one; the operator norm is max(1,Phi(w)/R). Testing distance cones gives Phi>=max_i Dw_i>=average_i Dw_i=c_n; uniform weights attain c_n. Equality forces Dw=c_n 1, and cyclic second differences give 2w_i=w_(i+m)+w_(i+m+1) for odd n=2m+1, hence uniformity via a maximum principle and gcd(m,2m+1)=1. For even n=2m they force antipodal equality; increasing the value of a distance-cone potential at the antipode of a negative coefficient by 1 preserves graph-edge Lipschitz constraints and contradicts optimality. Conversely any nonnegative antipodal pair weights have constant distance mean m/2 and attain Phi=c_n. Metric iff R>=diam/2, optimizer set full-dimensional and compact for R>c_n by continuity and finite-dimensional norm coercivity. This is a complete analytic proof, not a claim based on finite integer dual enumeration n<=12.

## originality

FAIL

Covered by published mathematical stronger result or proof; this is scientific originality rejection, not a claim that the theorem is false.

## value

PASS

Classifying *all* optimizing signed extension operators is a natural nontrivial equality-case problem beyond the previously known homogeneous-metric optimal value: the parity-dependent singleton versus growing simplex and sharp radius-dependent full-dimensional transition are substantive geometric structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
