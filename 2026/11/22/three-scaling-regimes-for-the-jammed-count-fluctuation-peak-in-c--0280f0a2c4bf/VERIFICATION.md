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

With total residual length x−1<2, a second segment fits iff Y is in the two endpoint tails of width e=(x−2)/(x−1); no third segment fits. The independent charge draws give mixture weights q=m_alpha m_beta, h and k with h+k=w. Each beta tail sum strictly increases from 0 to 1, so the Bernoulli variance has a unique maximum at probability 1/2. At fixed e the repulsive term tends to 6e²−4e³ and the two attraction-containing terms tend to 1, giving the positive-excess limit for w<1/2 by bracketing. For e shrinking, integrate the t-shape endpoint density: replacing (1−y)^(b−1) by 1 incurs relative O(te) on [0,e], since its derivative is bounded uniformly for b=t or 2−t and t is small. The opposite non-singular tail in the mixed case is O(t e^(2−t)), and gamma normalization gives leading tB(t,2−t)=1+O(t) and tB(t,t)=2+O(t). Thus at cutoff exp(−s/t) the mixture tends to w exp(−s), giving the exponential rate. At e=c sqrt(t log(1/t)), e^t=1−(t/2)log(1/t)+o(t log(1/t)) while the repulsive tail is 6c² t log(1/t)(1+o(1)). At w=1/2 the signed balance divided by t log(1/t) tends to 3c²−1/4, proving the critical coefficient by a two-sided bracket. The conversion delta=e/(1−e) preserves the small-excess equivalents. The composition thresholds follow directly from w=1−m_alpha m_beta, including w>=3/4 for unlike boundaries.

## originality

PASS

The distinct result is the three-regime singular location law, especially the exponential and critical shrinking-length windows. The exact binary law, variance, and fixed-cutoff kernel limits are prior; the peak condition and fixed-positive limiting root are readily obtained from them. No inspected source supplies the two singular shrinking windows of the location problem.

## value

PASS

The binary shell is the first nontrivial count fluctuation, and its variance height alone cannot distinguish any compositions. The maximizing length separates a persistent gap from collapse, and at the natural balance of endpoint mass it has a logarithm-enhanced critical scale with an exact coefficient. This is a substantive singular effect beyond substituting parameters into the known fixed-coupling formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
