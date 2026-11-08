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

# Verification

The accompanying `verify.py` is an executable symbolic/numerical regression checker. Running `python verify.py` requires Python 3 with SymPy and SciPy installed, and prints `VERIFY_OK` when the example algebra and representative trajectories meet their stated numerical tolerances. The script uses no hidden input files.

For the example \(b=7/10\), \(d=2\), \(c=1/2\), exact symbolic checks establish \(q=3/13\), \(k_c=2\log(10/3)\), \(p_{k_c}(0)=q\), \(p'_{k_c}(0)=k_cq(1-q)\), and \(\kappa=1+(6/13)\log(10/3)\). Numerical integration below and above the threshold checks the sign of the invasion eigenvalue and convergence to the corresponding resource equilibrium. At criticality, two disparate starts are integrated through time \(30000\); both observed \(tR(t)\) values approach the exact target \(0.6428058193\). Numerical checks are diagnostics, not proofs of asymptotic or global claims.

The proof in `RESULT.md` gives the decisive infinite-time arguments: a dissipative integral Lyapunov identity with coercivity at the resource boundary, a one-sided scalar comparison at depletion, the slow-variation justification of the convolution limit, and an implicit-function derivative for the positive branch. No independent external review has been performed.
