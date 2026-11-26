---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Normalized disk moments give Q(z^a bar(z)^b) with coefficient (|a-b|+1)/(max(a,b)+1). The commutator kills analytic inputs. For the monomial primitive z^k on input bar(z)^v, if k<=v the outputs from the two orders agree, with coefficient k(v-k+1)/(v+1) (k=0 contributes nothing), including the constant when k=v. If k>v and u=k-v, the coefficient difference is u-v(u+1)/(v+1)=(u-v)/(v+1). Thus the image is analytic without a constant and the square is zero. Taylor convergence beyond the closed disk justifies summation, and rescaling individual nonzero columns reduces the algebraic range computation to K_uv=(u-v)r_(u+v). At a pole the derivative is not used to set the order convention: the primitive coefficients are lambda^k times a polynomial p(k) of exact degree d-1 with leading coefficient nonzero. The coefficient matrix of (u-v)p(u+v) in degrees 0 through d has zeros for row degree plus column degree>d; on their sum=d the entries are c(2h-d) binomial(d,h)/d. Its whole anti-diagonal gives full rank for odd d, or after deleting the central row and column gives a nonsingular d-minor for even d; odd-dimensional skew symmetry supplies the upper bound in the latter case. The same argument on polynomial indices 1 through D-1 gives the degree term, with D<=2 contributing zero. The feature sequences u^h lambda_j^u are independent together with the finite-support coordinates: their generating functions have disjoint finite poles across j and strictly increasing pole orders in h at fixed j, while finite-support sequences generate polynomials. Hence a finite restriction of the common feature matrix has full column rank; using left and right inverses of it and its transpose proves rank additivity, independent of phases. The resulting column space is finite-dimensional and closed; boundedness and density of monomials identify it with the full operator range. Independent exact elimination on finite sections confirmed the polynomial and single-pole parity patterns and a mixed example of rank 10; the structural argument, not those sections, establishes the theorem.

## originality

PASS

The supported distinct theorem is the precise additive rank law by rational primitive pole multiplicities, including arbitrary mixtures with the polynomial contribution. Finite rank and square-zero are known, and both the monomial subfamily and the simple-primitive-pole example are covered. The same-day polynomial Wronskian record gives the entire pole-free specialization, not just examples. The assessment does not claim priority for that specialization or for square-zero.

## value

PASS

The finite-rank classification leaves the dimension of the range undetermined. This formula supplies it for a natural coordinate family directly from the primitive's pole orders and the degree at infinity. It gives a nontrivial odd-to-even plateau and shows that different poles never cancel one another's rank, even with complex coefficients. That precise invariant and mechanism are not captured by parity, nilpotence or the polynomial specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
