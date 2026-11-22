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

# Verification and reproducibility

The main result is proved in `RESULT.md`, with hypotheses and exact identities stated explicitly. The included `VERIFY.py` is a standalone supplementary checker (Python 3 with SymPy and SciPy):

```sh
python VERIFY.py
```

It tests, with symbolic arithmetic, the decomposition of the rational Allee growth function, the comparison-root identity, the cancellation of trophic interactions in the relative entropy, and the exact sign factorization. It also checks the positive rational parameter example \((a_1,a_2,a_3,a_4,b_1,b_2)=(1/10,1/10,1/4,3/20,1/5,1/5)\), obtaining the two exact roots \(1\) and \(16/5\), a strictly positive initial state with entropy below the analytical threshold, and convergence of its numerically integrated trajectory.

**Limits of computation:** An ODE simulation cannot prove convergence for arbitrary initial data or parameters, cannot establish completeness of basin boundaries, and cannot rule out other recurrent states. Those claims are not made. Analytical properness, invariant-sublevel reasoning, and LaSalle's principle supply the infinite-time convergence proof. The periodic orbit statements are conditional and follow from analytic sign and mean identities, not trajectory searches.

**Review status:** Mathematical derivation and reproducibility checks received self-review. No independent mathematical audit or external validation has been performed.
