---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

All nonempty proper Walsh characters have zero mean, leaving only theta on the full cube; the only degree-n term with all n odd powers has multiplicities (1,...,1), so the relative discrepancy is exactly theta n! product(a_i)/F_0(a). There is no discrepancy in lower-degree polynomial tests. If any coefficient vanishes the denominator remains positive and the discrepancy vanishes. Otherwise the independent moment is a symmetric sum of exponentials of linear forms in log|a_i| with strictly positive diagonal Hessian contribution from the pure powers. Permutation averaging fixes the log sum, hence gives the sharp minimum M_n product|a_i|, strict unless magnitudes are all equal. Their signs realize either endpoint for theta nonzero; theta=0 gives ratio one everywhere. For the asymptotic, the cosh tilt has generating function cosh(rz)/cosh(r), mean r tanh(r)=1, and variance r tanh(r)+r^2 sech^2(r)=r^2. Its span is exactly 2, and the mean n is on the sum lattice along even n. Thus the local limit mass at n is 2/(r sqrt(2 pi n)); undoing the tilt and taking the reciprocal gives the claimed prefactor. Independently recomputed the three constants by repeated truncated convolution: start with p_0=1, multiply n times by the polynomial with coefficient 1/(2k)! in degree k, truncating at n/2, and take the reciprocal of its degree-n/2 entry. This gives 3/5, 15/47, 315/1957 exactly.

## originality

PASS

Credit the exact relative n-th moment extremum and its flat-magnitude equality classification and large-order behavior, not the already published Walsh-law classification, unnormalized moment identity, Euclidean upper bound, or general lattice limit machinery. The closest inspected relative-moment result concerns absolute order one; the closest inspected n-th moment result uses a Euclidean denominator. Neither states or implies the sharp n-th moment ratio. This conclusion is best-of-knowledge, not priority certification.

## value

PASS

The objective quantifies how much almost full independence can first change a polynomial moment, on the natural scale of the corresponding independent moment rather than a worst-case Euclidean bound. Exact two-sided extremizers and the lattice-corrected exponential decay describe both where the distortion concentrates and how small it inevitably becomes. They are a useful tight benchmark, not a new claim about all k-wise Khintchine constants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
