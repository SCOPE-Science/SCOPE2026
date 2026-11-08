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

The standalone `verify.py` ran to completion with Python 3 and SymPy. It confirmed the nine connected isomorphism classes of order two through four (43 labeled graphs), certified 82 exact symbolic winner comparisons for all positive transmission/recovery ratios, and proved the paw switching polynomial has one positive root. It independently enumerated finite event paths for the 12 paw seed/threshold combinations at transmission/recovery ratio 18 and checked their exact rational values against a separate state-recursion calculation.

The proof covers all positive parameter values through polynomial sign analysis, not interpolation between finitely many test points. No numerical simulation, empirical epidemic data, or external formal proof certification is claimed. Results are limited to homogeneous continuous-time SIR on connected unweighted undirected graphs of at most four vertices; independent scientific audit has not been performed.
