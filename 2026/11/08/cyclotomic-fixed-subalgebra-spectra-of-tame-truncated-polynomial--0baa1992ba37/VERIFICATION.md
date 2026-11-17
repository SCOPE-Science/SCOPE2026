---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For A=F_q[t]/(t^n), p>n, the multiplier subgroup U has exponent p because its substitution matrices are unitriangular of nilpotency length at most n<p. The canonical commuting p-part and prime-to-p part of each automorphism permits a conjugate scalar multiplier σ_a (order d) and a unique centralizer parameter tuple (b_1,...,b_h), where h=floor((n−2)/d). The first nonzero b_j gives independent rows with leading coefficients kd*b_j, nonzero since 1≤kd<n<p; the resulting fixed ring is the scalar plus the upper truncated monomial ideal of dimension 1+j, and the trivial tuple gives 1+floor((n−1)/d). Counting first nonzero indices and Burnside yields exactly the stated conditional multiplicities and action-orbit sum. Boundary h=0, d=1 and coalescing dimensions are handled by adding multiplicities. Independently enumerated actual substitution matrices and fixed-space nullities at (5,3),(5,4),(7,4), recovering {1:10,2:9,3:1}, {1:50,2:45,3:4,4:1}, and {1:98,2:189,3:6,4:1}. The finite instances are checks, not proof for unbounded n/extension fields.

## originality

PASS

Best-of-knowledge PASS for the exact conditional distribution and fixed-ring normal forms. Classical tame finite-order linearization and group structure are established, but neither the inspected characteristic-zero monomial-algebra automorphism work nor the same-algebra subalgebra-orbit census supplies the counts of fixed elements of an arbitrary individual substitution. Broader literature on formal power-series conjugacy may imply some cases, so priority remains provisional.

## value

PASS

An exact probability law for fixed-subring dimensions, the embedded fixed-ring isomorphism profiles, and the Burnside orbit count for the natural full substitution automorphism group offer useful structural information beyond group order or reparametrization equivalence. The dimension law is uniform in n and q under a sharp tame hypothesis, not a tiny empirical enumeration or merely a renamed standard formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
