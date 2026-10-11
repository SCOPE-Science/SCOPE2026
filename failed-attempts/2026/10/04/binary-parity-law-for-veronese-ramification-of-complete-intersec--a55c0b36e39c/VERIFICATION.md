---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The parity calculation is correct under the stated range \(1\le k<\min d_i\). In that range the restricted degree-\(k\) ambient forms form the complete basepoint-free series of dimension \(M-1\), where \(M=\binom{N+k}{k}\), and adjunction gives \(g-1=D(S-N-1)/2\). The classical Wronskian/Plucker formula yields total ramification degree \(M(kD+(M-1)(g-1))\). Modulo two, oddness therefore forces and is forced by \(M\), \(k\), and all defining degrees being odd; Lucas/Kummer gives \(M\) odd exactly when \(N\mathbin{\&}k=0\). I independently replayed 4746 complete-intersection tuples and all \(N,k<256\) binomial parity checks. The real conclusion follows because a conjugation-invariant effective zero-cycle of odd degree has a real point.

## originality

FAIL

The claimed parity law is a direct corollary of classical general formulas rather than an original theorem under the implication-based bar. Laksov's generalized Wronskian/Plucker theory supplies the total ramification formula for a linear series on a smooth curve; complete-intersection adjunction supplies \(D\) and \(g\); and Lucas' theorem supplies the carry-free parity criterion for \(\binom{N+k}{k}\). Substituting and reducing modulo two mechanically yields exactly the audited binary condition. The real-point conclusion is the standard parity argument for conjugation-invariant zero-cycles.

## value

FAIL

The final theorem combines a classical ramification-degree formula, the textbook adjunction formula for complete-intersection curves, and the textbook Lucas parity criterion. The binary simplification is neat, but it is a routine substitution/parity exercise rather than a motivated unresolved invariant or structural lemma under the stated value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
