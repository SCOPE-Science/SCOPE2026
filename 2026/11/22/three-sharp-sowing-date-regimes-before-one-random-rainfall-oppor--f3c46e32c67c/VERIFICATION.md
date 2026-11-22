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

# Reproduction and verified scope

Run `python3 check.py` in the same directory as the embedded files, with a standard Python 3 installation. The checker actually passed 18,131 checks: nine exact rational-polynomial identities, nine groups of optimizer-domain and positivity checks, 18,000 feasible-calendar comparisons, 65 independent direct integrations of the conditional rain-event law, and 21 local threshold perturbations. The reported phase constants were `p1=0.537524704426` and `p2=0.851288471547`; at `p=1` the reproduced optimum was `t1=0, t2=0.1568194231133884, t3=0.7068958511210482`, with success `0.7895887539534517`.

The finite checks do not prove uniqueness, complete parameter coverage or historical originality. The mathematical proof is the existence/compactness and global stationary-point classification in `RESULT.md`. The model excludes correlated establishment conditional on the shared rain, unequal exponential rates, repeat rains and empirical parameter uncertainty. Independent external validation has not been performed.
