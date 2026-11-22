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

# Verification details

The theorem is proven by the local analytic nonedge expansion, an intermediate-time positive lower bound, and a uniform all-later-time perturbation estimate against the strictly positive ordinary heat semigroup. The exact graph in the proof has ratios obtained by multiplication of the displayed integer Laplacian.

Run `python artifacts/check_diameter2.py` in an environment with NumPy and SciPy. The finite checker separately constructs conductance Laplacians, forms mixed generators, calls matrix exponentials, brackets nonedge roots, and compares rescaled numerical roots to the derived two-term law. Its recorded successful execution covered 336 graph–parameter cases and 1,584 individual nonedge roots. These checks are consistency tests, not proof of the all-graph claim or independent audit.

Not proved: a graph-uniform perturbation radius, global recovery formulas at arbitrary coupling, or higher-order selection between tied nonedges.
