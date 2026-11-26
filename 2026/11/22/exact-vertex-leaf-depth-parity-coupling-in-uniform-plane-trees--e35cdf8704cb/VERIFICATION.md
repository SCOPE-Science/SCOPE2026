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

For uniform plane-tree shapes, the root decomposition reflects both signed marks on each child subtree and adds a leaf mark only at a singleton root. Write B=F(z;0,0), D=1−B, z=BD and w=1−2B. The first-derivative equations have factor 1+z/D² and give F_s=z and F_t=zD. The second-derivative equations have factor 1−z/D²=w/D and give F_ss=z(1−2z)/w, F_st=zD/w−z² and F_tt=(zD+2z³)/w. Thus for n≥3 the mixed coefficient is half the central binomial coefficient at n−1, i.e. n C_(n−1)/2; the first all-vertex mean is zero. The leaf raw square is n/2+2(n−2)C_(n−3)/C_(n−1), algebraically the stated expression before centering. The Catalan ratios give both variances, with respective linear terms n/2 and 5n/8; the correlation limit follows without a CLT. At n=3 the same extraction includes C_0 and all denominators are nonzero. Both variables are nonconstant for n≥3 (compare the star and the tree with one length-two arm and all other arms of length one).

## originality

PASS

The reviewed distinct result is the exact same-tree mixed moment and leaf-parity variance and the resulting correlation, not the known marginals or the all-vertex parity limit theory. The closest inspected results do not determine these joint statistics under the assigned law.

## value

PASS

The statistics are natural signed bipartition imbalances before and after restriction to terminal vertices. Exact joint covariance gives a sharp measure of the information retained by that restriction, and the 4/5 least-squares fraction is not fixed by marginal enumeration or an all-vertex CLT. The result is useful as an exact benchmark for joint marked-tree results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
