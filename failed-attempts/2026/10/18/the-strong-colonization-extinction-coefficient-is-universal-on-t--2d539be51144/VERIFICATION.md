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

For each fixed connected graph the rates on a proper nonempty set S are |S| downward and λc(S) upward, where c(S)≥1. The first loss has mean wait 1/n and a uniformly chosen vertex. A monotone successful excursion gives Z/(nλ^(n−1)) at leading order. With u up jumps a successful excursion needs n−1+u specified down jumps after that first loss. At most n^(n−1+2u) state paths have this length for each initial state and each specified down step costs at most λ^−1. Summing the geometric bound at λ>n² bounds the nonmonotone contribution by O_G(λ^−n). In blocks of at most n−1 jumps there is probability uniformly bounded below of ending an excursion by consecutive up moves to full occupancy, and proper-state holding times have mean at most 1/λ. The mean excursion is O_G(1/λ). Renewal gives the mean trial time divided by success probability even if duration and success are dependent. The anchored order-chamber gaps have unit Jacobian, and every edge contributes its intervening gaps, yielding exactly the inverse cuts. Tree differences give independent one-edge integrals of 2. For unicyclic graphs use an anchor on the cycle (the formula was proved for every anchor), integrate the n−ell off-cycle edges, and reduce to the ell-fold convolution of exp(−|x|) at zero. Fourier inversion gives 2^ell times the zero density of an ell-fold normalized Laplace sum, namely binom(2ell−2,ell−1)/2^(ell−1) for the cycle integral. The successive multiplier ratio is 2ell/(2ell−1). The normalization is fixed graph, fully occupied start and unit loss, not a joint size-rate limit.

## originality

FAIL

The configured 2d2ad5c19a59 theorem expressly covers the leading permutation coefficient, the integral and the tree law, with directed/weighted generality. On both-way unit edges they are the frozen results. The additional unicyclic formula, while not printed there, follows mechanically from that same known integral by removing leaves and a standard one-dimensional Laplace convolution. 9facf36b623e separately gives exactly the fixed-graph leading mean law. Thus coverage is substantive, not just use of the same terminology. Neither catalogue path date is used to infer historical precedence or provenance.

## value

FAIL

Tree universality and the role of the unique cycle are mathematically well motivated. As an incremental finding, however, the stronger configured result already supplies the coefficients and integral, and the apparent remaining narrower invariant is their direct leaf-integration and beta-integral specialization. No distinct nonroutine increment is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
