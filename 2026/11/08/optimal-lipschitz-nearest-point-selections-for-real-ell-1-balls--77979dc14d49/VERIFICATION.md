---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Characterized nearest points by equality in triangle inequality: interior inputs fixed and exterior positive-sign coordinate shrinkages with output norm r. Soft threshold exists uniquely for any ell1 input, with finite active set above positive tau even for arbitrary infinite I. Finite-dimensional sign-cell Jacobian is a sign conjugate of C_k=I−11^T/k on active coordinates, with induced ell1 norm 2−2/k, giving optimal upper bound (and exact slope realization). For any selector its value near b=(1/n,...,1/n) must be compared to n fixed boundary inputs at ell1 distance epsilon; the unrestricted zero-sum minimax is convex and symmetric, reduces to q=(a,−a/(n−1),...), and minimizes max(2a,2−2a/(n−1)) at a=(n−1)/n, so all selectors have modulus >=2−2/n. Finite supports force infinite lower bound 2; countable-support truncation yields upper bound 2. Exact rational minimax witnesses recomputed, not substitutes for universal proof.

## originality

PASS

Best-of-knowledge after detailed primary prior reading: earlier October 11 research proves the very same soft-threshold nearest-point formula and optimal Lipschitz modulus of that particular map for unique projections in strictly convex ell_p norm, but explicitly requires 1<p<infinity and does not consider the multivalued ell1 endpoint. An endpoint limit could yield the norm of the displayed threshold choice but not the new universal lower bound against ALL nonlinear/discontinuous selections. Jinlu Li 2026 paper concerns exactly the set-valued ell1-ball metric projection but accessible abstract treats generalized derivatives and covering constants, not an all-selector sharp modulus; full text inaccessible, recorded significant priority risk. No exact earlier all-selector bound was established in checked results; best-knowledge PASS without independent priority certification.

## value

PASS

Sharp optimal Lipschitz constants of arbitrary nearest-point selections are a natural multivalued variational analysis invariant, not merely a chosen algorithm’s modulus. The theorem proves a universal nonlinear/asymmetric lower bound and exact finite/infinite dimension threshold for nonexpansiveness; both geometric obstruction and limit are useful structural facts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
