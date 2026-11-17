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
# Finite reproducibility

Install the declared `sympy` dependency, then run `python3 verify_m2_k7.py`. The checker enumerates all 2,097,152 edge subsets of the 21-edge graph, builds all 15,795 nonempty faces, all Hasse covers and the entire Morse reduction, and calculates the integer Smith normal form. It independently computes the direct simplicial boundary ranks over the field of two elements. The terminal success token is `M2_K7_INTEGRAL_MIXED_WEDGE_PASS`. The original computation is finite and exhaustive, not an unproved infinite extrapolation.

The integer Morse matrix has size 132 by 312, exactly 131 unit diagonal invariant factors, and no nonunit factors. This determines attaching degrees since only 4- and 5-dimensional positive cells remain. The mod-two direct boundary ranks are separate corroboration; they cannot by themselves prove absence of torsion or nullhomotopy.

Independent mathematical audit has not been performed. The primary full text of Jonsson's relevant bounded-degree chapter was not read; originality retains that specified residual risk.
