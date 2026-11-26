---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For the ordinary single query of RESULT.md lines 5–48, averaging the squared sine and cosine gives 1/2 each and the sine-cosine cross term integrates to zero. Thus the alternatives are the channels E_j=(Id+Ad(H_j))/2, with an untouched ancilla allowed. For a pure input (sufficient by convexity), the shared branch cancels, and the trace norm of the output difference is √(1−|⟨H_0 H_1⟩|²), with expectation taken in the reduced qubit state. The Pauli product gives c+i(n_0×n_1)·r for its Bloch vector r. Its squared modulus is at least c² and a maximally entangled probe attains c² (a pure qubit in the plane of the axes also suffices). Equal-prior Helstrom then gives exactly 1/2+√(1−c²)/4; c=0 yields 3/4 and |c|=1 gives identical channels. VERIFICATION.md records an analytic derivation and boundary checks, not numerical or formal certification.

## originality

FAIL

The generic-angle law is a direct consequence of Acín's published one-use result for arbitrary pairs of fixed SU(2) gates. The averaged channels are not themselves unitary gates, but the common identity branch cancels in their difference, so the optimized Helstrom advantage is precisely half the one for the corresponding fixed gates. This gives the complete frozen formula, not only its orthogonal endpoint.

## value

FAIL

The angular formula is a useful check on the unknown-time model, but the precise invariant is mechanically implied by the earlier arbitrary-qubit-gate optimum and a common-branch cancellation. The submission does not establish a distinct discrimination result beyond that corollary; the unrestricted larger-query problem is outside the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
