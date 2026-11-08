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

The standalone `verify.py` uses only Python 3's standard library. It constructs the incidence matrix in lexicographic order and checks vertex degrees, the Gram identity, a rank-65 incidence-column basis, rank-16 point observations of the zero singular sector, and ranks 32, 24, 8, and 1 for the positive singular sectors. All computed ranks are over the exact finite field of 101 elements. Algebraic upper bounds from the tensor decomposition turn these modular lower-rank certificates into exact rational-rank equalities. The program additionally confirms that no initially actuated vertex can initiate zero forcing.

Verified observed output: `VERIFY_OK`. The file is executable as `python3 verify.py`. The theorem is about this fixed finite graph; the calculations are exact certificates, not a claim about general dimensions or arbitrary edge weights. Independent audit has not been performed.
