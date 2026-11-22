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

The proof establishes the metric-speed formula for arbitrary positive-length differentiable finite-bar families and all finite \(p\)-norms, including collisions of tent values. Strong differentiability is explicitly not claimed at such collisions.

The accompanying `check.py` uses exact rational breakpoints, line intersections and integrals of affine differences for \(p\) equal to 1, 2 and 3. The actual replay yielded 324 passed secant-distance comparisons over 18 barcode families, three perturbation magnitudes and two signs. The smallest magnitude was \(1/16384\). Checks are finite corroboration; all-parameter correctness relies on the written sorting and dominated-convergence argument.

Source comparison: arXiv:2611.11358v1 treats a common fixed birth and identifies moving births as a further direction. The older persistence-landscape sources establish basic definitions and stability. Bibliographic searches and scientific-index queries did not identify an exact general moving-endpoint metric-speed theorem. Non-indexed equivalences remain possible.

Independent mathematical validation and an exhaustive literature-priority review are not included.
