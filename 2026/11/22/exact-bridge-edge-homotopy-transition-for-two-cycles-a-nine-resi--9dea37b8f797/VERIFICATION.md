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

The companion `verify.py` uses only the Python 3 standard library. It enumerates all independent faces as bitmasks for the two graph families with \(3\le p,q\le8\); it calculates mod-two simplicial boundary ranks of both absolute complexes and of their simplicial pairs. Run `python verify.py` and compare with `verification_output.txt`.

The 72 absolute and 36 relative mod-two computations agree with the statement. All integral freeness, primitive inclusions and general parameter ranges follow from the path/cycle homotopy equivalences and the two explicit cofiber decompositions in `RESULT.md`; these checks do not by themselves prove infinitely many cases. No integral Smith form computation is claimed for the finite cases, because the written argument does not require one.

The proof assumes only the standard path/cycle independence-complex formulas, simplicial vertex-link decomposition, ordinary joins and their standard homotopy properties, and exactness of the integral homology sequence of a CW pair. The triangle/empty-path normalization is stated in the theorem. Independent audit has not been performed.
