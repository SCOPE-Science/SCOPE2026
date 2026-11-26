---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The proof works over any field K of odd characteristic p for R_p. In the associative group ring the native product is α(u)β(w), and augmentation zero implies an idempotent lies in I=(T−1); iterating its equation doubles the minimum filtration degree until I^p=0. Augmentation one instead permits the mutually inverse truncated exp and log, whose identities hold through total degree p−1 in the commutative ring. Hence log takes nonzero idempotents to the kernel of α+β−1. Splitting by the involution α, the +1 summand contributes nothing because β is invertible, and the −1 part requires βv=2v. In group-ring coefficients this says c_(ha)=h^(-1)c_a for h in H, and c_0=0, so the exact kernel has the disjoint-support basis V_C. Its augmentation is zero by αv=−v. Exponentiating gives the asserted native product law and hence the core quandle, with zero excluded from that law. The finite-field count and prime-field rigidity criterion follow; at p=17 and 31 the subgroup orders are 8 and 10, and for p≡1 mod 8 both generators are quadratic residues. Independent small checks found the exhaustive counts 4 and 6 for p=3 and 5 and verified higher-rank witnesses at p=17 and 31. The supplied script was read, not executed.

## originality

FAIL

Two earlier records cover the full classification. In particular the October 18 record already gives the same exponential kernel, core-quandle product law, count, basis-only condition and arithmetic examples over precisely the same fields. The present coset-coordinate basis is a routine change of basis in that same kernel and does not provide a separate new theorem.

## value

FAIL

The arithmetic rank and quandle classification would be useful as a first result, but both are known. The remaining coset basis is recovered by one free coefficient per orbit of the known eigenspace, and the Dirichlet observation is immediate from quadratic residues. Neither gives an independently substantial surviving theorem here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
