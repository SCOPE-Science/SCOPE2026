---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For N=2^k, k>=2, translation t→t+N/2 splits the N-point function space into equal +/- sectors labeled by first-coordinate parity. For first difference even and second odd, exact quadratic Gauss-sum squared modulus 2N is nonzero; all orthogonal frequencies within a sector therefore have the same second-coordinate parity. After removing the fixed chirp, dividing both coordinates by 2 reduces orthogonality to the level-(k-1) parabola. This gives a unique decomposition into two smaller bases and two parity bits, B_k=4 B_(k-1)^2, B_1=4 and B_k=2^(2^(k+1)-2). Inspected check_spectra.py provides finite checks only; the induction proves all k.

## originality

FAIL

Decisively covered by an Oct 18, 2026 published Resultary theorem with the identical object, recursion, quantifiers and exact enumeration; an additional Nov 1 published theorem gives an equivalent complete classification and identical count. Later relabeling cannot establish originality.

## value

FAIL

The exact natural spectral-set classification is mathematically worthwhile in isolation, but this package contributes neither a new invariant nor a refinement beyond the previously published complete recursion and enumeration, indeed lacks the prior extension result. A duplicate formulation has no incremental scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
