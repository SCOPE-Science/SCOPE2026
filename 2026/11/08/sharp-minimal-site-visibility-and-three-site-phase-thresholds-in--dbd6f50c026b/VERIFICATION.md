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
# Reproducibility and checks

The analytic theorem is proved in `RESULT.md`. Run the standalone Python 3 script with `python verify.py`. No external libraries, data files, or network access are necessary. The script reconstructs exact rational nonconvexity/nonvisibility witnesses and checks 12,338 reproducible finite test assertions, printing `QUADRATIC_VORONOI_PHASE_CHECKS_OK 12338` on success. Parameter-loop tests are finite samples; they do not certify the universal statement. The universal root and endpoint arguments are the displayed symbolic proof. The full first motivating paper was accessible in author-provided arXiv HTML, and comparison was made to accessible primary older studies. No external or independent mathematical audit has been performed.
