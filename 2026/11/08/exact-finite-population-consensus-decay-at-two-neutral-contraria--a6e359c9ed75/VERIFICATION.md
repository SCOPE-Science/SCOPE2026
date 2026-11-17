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

For each triple with a pre-update A agents, individual outputs are Binomial(3,a/3) at (c30,c21)=(0,1/3) and Binomial(3,1−a/3) at (1,2/3). Mixed triples have variance 2/3; the expected number under fresh uniform triple partition with k A agents is k(N−k)/(N−1). Consequently conditional K-next mean is k or N−k and conditional variance 2k(N−k)/[3(N−1)]. H(k)=k(N−k) is a one-step eigenfunction with q_N=1−2/[3(N−1)] on both corners. H is bounded above N²/4 and below N−1 off unanimity, hence two-sided geometric survival bounds, finite a.s. hitting, matching log(q_N) exponent; martingale/signed martingale yields initial A-fraction phase probability. Complement kernel duality gives reversal interpretation. Handles N=3, k=0,N boundaries without asserting positive tail there.

## originality

PASS

Original Galam (2026) supplies the cubic deterministic density map and known identity/involution corners. Its accessible primary full text emphasizes dynamical fixed points and does not provide the particular annealed finite-N conditional variance or full two-phase hitting tail. Toth–Galam group-decision flips have a different variance kernel. Standard neutral-drift convergence alone does not fix q_N for this update rule.

## value

PASS

Two deterministic neutral singular corners do not describe stochastic finite populations. An exact all-N absorption-rate baseline and alternating consensus selection distinguish independent individual activation from shared group flipping, and quantify the scale of stochastic drift. The model is specified enough to be a meaningful benchmark rather than a generic voter slogan.

The dated certificate retains the supplied scientific assessment, sources and limitations.
