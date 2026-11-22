---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the dimer-covering covariance theorem

**Exact analytic steps.** A first proposed dimer at an edge is retained if it arrives before the first proposal at one of its two neighboring edges. Therefore site multiplicity depends on exactly four independent exponential first-arrival clocks. The proof derives accepted-edge covariances using the integral \(\int_0^p\int_0^p xy\min(x,y)\,dx\,dy=2p^5/15\), propagates these into site covariances, and verifies signs via explicit positive Bernstein coefficients.

**Standalone computations.** From an extracted artifact directory, run `python3 verify.py`. This enumerates the arrived-clock subsets and all relative orders, recomputes the exact site moments as polynomials in \(p=1-e^{-t}\), and checks coefficients, the all-time correlation range, the positivity certificates, and the terminal variance. The code uses only the Python standard library.

**Mathematical limits.** Finite order enumeration independently verifies local rational polynomial identities; it does not substitute for the proof that all sites of the infinite line have well-defined local dynamics or for the blocking proof of the central limit theorem. The analysis assumes independent unit-rate Poisson deposition attempts and concerns spatial observations at one fixed time. Scientific priority and any independent expert audit are not performed here.
