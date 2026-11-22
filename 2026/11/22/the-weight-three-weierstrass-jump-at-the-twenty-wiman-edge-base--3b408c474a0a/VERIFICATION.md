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
# Reproducibility and verification

Run `python verify_wiman.py` with Python 3.10 or later and SymPy. The script uses only integer/rational polynomial arithmetic and gives the success line `WIMAN_BASEPOINT_CANONICAL_RAMIFICATION_VERIFIED_OK` if every exact assertion succeeds.

It computes the formal curve parametrization through order seven over the quadratic algebra with \(u^2-u+1=0\), checks the displayed canonical jet determinant, performs exact reduction by \(\varphi^2=105/4\), verifies every potentially nonzero minor through the relevant degrees, and checks rank witnesses for vanishing orders \((0,1,2,3,5,7)\). An independent consistency check is the global weight total \(6(6^2-1)=210\), larger than the contribution \(20\cdot3=60\); the remaining weight is not classified.

The program does not check the historical novelty of the finding, the geometry of singular fibers, or all canonical Weierstrass points away from the marked base locus. Independent scientific assessment has not been performed.
