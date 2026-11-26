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

The Finding holds, although RESULT.md line 33 incorrectly asserts irreducibility for m,n>=2. The state (m-1,0) has no incoming transitions and has positive exits. Uniqueness follows instead by reaching the all-positive free configuration from every state (turn second-part voters positive via the fixed positive vertex, then first-part voters via a positive free second-part voter). In a star, each free voter is absorbed at the opposite fixed opinion, including the no-free-voter case. For m,n>=2 put a=m-1, b=n-1, t=a+b, N=t+2. The drift equations give means b/(t+1) and (b+1)/(t+1), and E[Y]=n. Centered-pair generator equations give cross covariance (a+1)(b+1)t/((t+1)^2(3t+2)) and same-part factors b/(b+1) and a/(a+1). The single-site sum of variances is abN/(t+1)^2; the ordered distinct-pair covariance sum is ab t^2 N/((t+1)^2(3t+2)), yielding the formula. At fixed N, ab=((N-2)^2-(m-n)^2)/4 gives the stated exact extrema. In stationarity D=x-y has E[D^2]=O(1/(m-1)+1/(n-1)); expanding test polynomials for z=(x+y)/2 gives scaled drift (theta-z)/(2 theta(1-theta)) and scaled half squared-jump rate z(1-z)/(4 theta(1-theta)) in L^1, with scaled remainder O(1/N). Stationarity identifies the moments by (k+1)M_k=(2 theta+k-1)M_{k-1}. The beta law is determinate on [0,1]; synchronization gives joint convergence and Y/N-z tends to zero in probability. Boundedness gives convergence of the variance. This passes the Finding, not the erroneous irreducibility sentence.

## originality

FAIL

A distinct indexed record states the identical aggregate fluctuation and beta law, and a frozen counterpart gives the same joint limit and exact one-site and pair information that implies the fluctuation. The star extension and size extrema are elementary consequences of the same model and formula, not separately original results. This is a mathematical coverage judgment, not a chronological priority judgment.

## value

FAIL

Macroscopic fluctuations are a motivated invariant here, but this record adds no independently useful unknown fact beyond the covered variance and limit. The ostensible additional extremizer classification is a quadratic maximization/minimization of the same formula, and the stars are deterministic boundary cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
