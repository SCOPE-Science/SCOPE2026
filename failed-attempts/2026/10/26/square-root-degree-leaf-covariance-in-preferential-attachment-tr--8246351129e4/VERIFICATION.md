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

For a_n=1/[2(n-1)], attachment to the marked vertex and attachment to a leaf overlap with conditional probability a_n times its leaf indicator. Expanding the mixed product cancels the opposing a_n D_n L_n drifts and gives Delta C_n=a_n^2 E[D_n]E[L_n]-a_n q_n. The marginal updates give d_n=(2n-3)q_n and ell_n=[2(n-1)+4q_n]/3; substitution gives the stated increment, including cancellation at n=2 and strict positivity thereafter. Stirling and summation give the square-root constant and dividing by d_n gives 1/3. The Bernoulli update yields E[D_n^2]=2(n-1)-d_n; the leaf-variance recurrence telescopes after multiplication by n-1 and its forcing tends to 2/9, giving variance n/9. These constants give the Pearson prefactor and n^(-1/2) decay. Independent exact rational replay via python -B /workspace/checks/bounded.py evolved the reduced joint distribution of degree and leaf count and agreed with the covariance formula through n=32. That bounded check is not a proof for arbitrary n.

## originality

FAIL

The distinct indexed record ending a3885e62cb19 has the identical finite covariance increment and sum, initial values, positivity and leading asymptotic for exactly the same seed, marked vertex and global leaf observable. The ratio is a direct division of two asymptotics already in that record. The explicitly stated Pearson constant is a normalization using the two marginal variance asymptotics, not a new mixed-moment result. Exact coverage is established by the available text, independently of unverified publication timestamps.

## value

FAIL

The exact marked-versus-global covariance is a useful structural statistic, but the submitted record repeats that already covered theorem. Its only separately displayed additions are the ratio of the known growth laws and a routine Pearson rescaling by marginal standard deviations. Neither supplies a distinct substantive fact or a motivated new invariant warranting a repaired finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
