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

The analytic proof derives the exact number of unavoidable envious agents, all fixed-order factorial moments of isolated-edge components, and uniform upper bounds for larger tree components. The Python checker is a supplementary independent enumeration of the finite definitions, not a substitute for analytic asymptotic proof or a formal theorem prover.

Run `python verify_envy.py` with Python 3 and no third-party packages. The checker exhausts the \(1099\) labeled simple graphs on at most five vertices under all assignments of each good to one endpoint, and the \(75\) simple graphs on at most four vertices under all complete allocations to arbitrary agents. It also prints finite random-graph samples and factorial-moment diagnostics. All exhaustive comparisons passed in the self-review. Numerical simulations do not prove Poisson convergence.

Known scope boundary: a vertex's valuation of another agent's bundle is bounded by one only for simple graphs, so multiple parallel goods or nonbinary values require a different proof. The zero-deficit existence criterion is known from Misra–Sethia (2024); the exact positive deficit count and its critical-window law are the additional subject. Independent audit was not performed.
