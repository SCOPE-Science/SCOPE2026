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

# Verification of characteristic-two Rota–Baxter index and finite-field counts

Execute `python verify.py` using Python 3's standard library. The program directly constructs all \(q^{(d+1)^2}\) candidate matrices for the tested small prime-field instances, applies each matrix to all elements, evaluates the original weight-zero Rota–Baxter identity on all ordered element pairs, and computes \(P^2\), \(P^3\), and rank pairs independently of the structural parametrization. It separately computes square-zero rank multiplicities with Gaussian coefficients and compares all observed counts and rank pairs. The sampled test cases are \((q,d)=(2,1),(2,2),(3,1),(3,2),(5,1)\). It also evaluates the finite-field formulas for \(q=2\) and \(1\le d\le6\).

Expected representative output includes `DIRECT_RB q 2 d 2 count 16 P2zero 10 P2nonzero 6`, `JORDAN_RANK_PROFILE_OK 2 2 [((0, 0), 1), ((1, 0), 9), ((2, 1), 6)]`, `DIRECT_RB q 3 d 2 count 33 P2zero 33 P2nonzero 0`, and a final `VERIFY_OK`.

The infinite-field classification, all finite extension fields, and the asymptotic probability formula follow from the proof in `RESULT.md`, not from these finite enumerations. Finite computational experiments neither establish the infinite assertion nor rule out a stronger published theorem. No independent mathematical audit has been performed.
