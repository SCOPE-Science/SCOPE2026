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

# Reproducibility

Run `python3 verify_singer_building.py` in a directory containing that standalone file. The script uses only Python 3 standard-library operations on finite sets, integer bit masks and freely reduced signed words.

It reconstructs the finite field defined by \(t^4+t+1\), enumerates every subspace and strict chain, checks orbit-cell counts for each subgroup of order \(1,3,5,15\), and explicitly transforms every quotient two-cell presentation through justified elementary eliminations. The resulting residual attaching degrees are inspected and asserted before the expected homotopy types are reported.

Execution of the included script succeeded with terminal marker `VERIFY_OK`. Residual presentations: \(64\) null two-cell maps; \(24\) null two-cell maps; six degree-five and seven null maps; and two opposite degree-five and three null maps, respectively. The first two give wedges of two-spheres. In the last two, integral two-cell slides leave one degree-five Moore attachment and the remaining null attachments.

The calculations are exhaustive for the specified finite spherical building, **not** an experiment purporting to establish an infinite-family statement. They do not address larger finite fields or ranks. Independent external mathematical audit has not been performed.
