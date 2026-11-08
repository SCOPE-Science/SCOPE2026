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

# Reproduction and boundaries

Run `python verify_retractions.py` and `python verify_orbits.py` with Python 3. Both must end in `VERIFY_OK`.

`verify_retractions.py` enumerates all binary \(2m\)-by-\(2m\) matrices for \(m=1,2\), checks idempotence and isotropic image, computes the restricted alternating rank of the kernel, weights by the exact number of central lifts and checks every \((r,s)\) stratum against the formula. It includes the identity as a separate map. For \(m=2\), it obtains \(1,240,480,480,1\).

`verify_orbits.py` independently generates the full binary \(\mathrm{Sp}_4\) action using symplectic transvections; it partitions all 361 eligible projections into orbit sizes \(1,120,120,120\). It also enumerates the complete \(3^9\) space of linear maps on the three-dimensional ternary Heisenberg algebra and directly tests both \(F^2=F\) and \(F([a,b])=[F(a),F(b)]\), finding rank counts \(1,36,1\).

All finite enumerations are exhaustive for those specific small fields/dimensions; neither verifies arbitrary \(m\) or all prime powers by itself. The general theorem rests on the proof of symplectic transitivity and alternating-form complement counting in `RESULT.md`. No external independent audit has been carried out.
