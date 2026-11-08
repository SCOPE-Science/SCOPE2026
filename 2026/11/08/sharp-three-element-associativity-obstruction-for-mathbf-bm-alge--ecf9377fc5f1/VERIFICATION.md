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

# Reproduction and limits

Run `python3 checker.py` in this directory. The checker has no package dependencies beyond the standard Python library. It examines all \(1\), \(16\), and \(19683\) operation tables on respectively one, two and three elements, tests every assignment of the universal \(\mathbf B\)- and \(\mathbf M\)-equations, and treats each admissible ordered pair \((B,M)\) as a separate marked structure. It computes all isomorphism representatives under the full symmetric-group action, all fixed-point counts used in Burnside's formula, and closure under the two distinguished generators.

The expected final line is `BM_MINIMAL_NONASSOCIATIVE_CENSUS_OK`; the preceding lines display the exhaustive labelled and isomorphism-class counts. The checker also verifies that the six canonical nonassociative tables meet the equations, possess no left unit, have an absorbing zero, and include a fixed-point element. The unique generated marked example is checked explicitly.

The enumeration is exhaustive only for the stated finite cardinalities. Its soundness depends on the transparent finite loops implementing the displayed equations; it is not an independent formal proof assistant or a certification of historical priority. The complete proof of the finite claim is the exhaustive table reduction together with the group-action calculation described in RESULT.md. No external validation has been performed.
