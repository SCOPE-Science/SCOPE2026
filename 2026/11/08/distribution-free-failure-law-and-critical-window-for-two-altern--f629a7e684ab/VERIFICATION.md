---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For common iid continuous effective cutpoints, sorting them leaves iid Bernoulli preference signs; at gap j exactly U_n-S_j voters reject. A cutpoint itself offers no smaller count because only one acceptance condition changes with equality, hence optimal V_n=U_n-M_n where M_n=max_{0<=j<=n} S_j. Conditioned on U_n=u, reflection at level u-k+1 leaves binom(n,u)-binom(n,k-1) valid paths, giving exact distribution-free tail. V_n=0 exactly for a +block followed by a -block. Negative-drift random-walk maximum has geometric hitting probabilities, giving mean correction min(p,q)/abs(p-q) and binomial CLT. For p=1/2 the reflection identity E M_n=E abs(S_n)-P(S_n>0) yields n/2-sqrt(2n/pi)+1/2+o(1), and Donsker plus continuous supremum mapping yields both Brownian maxima and p_n=1/2+theta/sqrt n drift. Independent direct enumeration all sign words n=1..10 for p=.25,.50,.75 checked every k-tail and feasibility formula.

## originality

PASS

The full primary Teh–Goldberg (2026) source Appendix E.1 Proposition E.1 gives sorting-based deterministic O(n log n) optimization of interval overlaps for two alternatives; it does not provide this iid random-cutpoint law, all-p ballot-tail distribution, or Brownian critical window. Earlier related Resultary findings concern finite-grid worst-case sampling/regret and other voter models. Classical reflection and invariance principles are tools, not the claimed novel theorems. Best-of-knowledge PASS with explicit risk of an earlier probabilistic interval-overlap equivalent.

## value

PASS

The minimum-violation statistic for randomly sampled preferences is a natural social-choice quantity: exact distribution-free feasibility probability and sharp Gaussian/Brownian phase transition quantify when perfect or near-perfect stakeholder lotteries exist. This is not a simple restatement of the deterministic optimizer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
