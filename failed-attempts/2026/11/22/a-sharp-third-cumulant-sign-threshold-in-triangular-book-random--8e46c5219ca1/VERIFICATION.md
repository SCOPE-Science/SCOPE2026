---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For m≥3 and real q>1, v>0, enumerate the one-page weights q,v,v,v² according to the spoke state. After those weights, the two hub factors are q if a bridge or the spine is present and q² otherwise. Summing the spine gives the unnormalized vector law q[(1+v)B^m times the Bernoulli(p) product law + (q−1)A^m times the all-zero point mass], with A=q+2v, B=A+v², p=v²/B. For distinct page labels the joint rth product moment is θp^r, so the stated covariance and third cumulant follow. The sign is that of R−1 with R=(1−θ)/θ=(q−1)/[(1+v)(1+v²/(q+2v))^m]; v²/(q+2v) strictly increases on v>0. R decreases from q−1 to 0: at q=2 there is no positive zero, while q>2 gives exactly one. For v=a/sqrt(m), mp→a²/q and R→(q−1)exp(−a²/q); bracketing the root between two fixed scaled activities proves its limit, and binomial-to-Poisson convergence gives the claimed count law. No thermodynamic singularity is asserted. Frozen RESULT.md lines 41–64 establish the argument; verify.py and VERIFICATION.md were inspected, not executed.

## originality

FAIL

The exact page law, hence the boundary and sparse scaling, is mechanically implied by the earlier finite-core FK factorization combined with ordinary spine deletion–contraction. The prior record does not explicitly state the book sign theorem and its main asymptotic model lacks a spine; neither difference blocks this implication. This is positive coverage evidence, not an inference from a missing paper or a common title.

## value

FAIL

The contrast between positive pair covariance and a sign-changing third cumulant is scientifically intelligible, but the advertised exact boundary is a routine readout of the existing exact two-hub product tilt: adding the spine only multiplies the product contribution by 1+v. The sign and the asymptotic scale require no additional structural estimate. It is a useful illustrative corollary, not a distinct valuable unknown exact invariant under the audit standard. No surviving repair is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
