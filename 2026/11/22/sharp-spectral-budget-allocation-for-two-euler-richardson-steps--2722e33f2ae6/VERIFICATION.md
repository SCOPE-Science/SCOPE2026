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

# Verification record

The proof reduces all admissible two-step allocations to the compact product interval \(0\le u\le t^2/4\). The maximum absolute residual is determined exactly by the two endpoint values and (when admissible) the vertex value. This exhaustive characterization, together with the strict monotonicity crossing, is the infinite-domain certificate for the optimizer. Threshold ordering is given by explicit positive rational differences; there is no interpolation from numerical experiments.

To reproduce supplemental checks, execute `python3 check.py` from this directory using standard Python 3. The script evaluates endpoint/vertex suprema independently and compares the theorem's product with a separate golden-section minimization for 1,886 parameter configurations; it tests exact rational endpoint balances and stability boundaries at eight condition numbers. The checker output was:

`PASS: 1886 independent minimax comparisons; four exact-rational endpoint balances; eight sharp stability-boundary tests`

The numerical sweep is finite and does not certify all real parameters. The mathematics in `RESULT.md`, not the numerical sweep, proves the universal statement. No independent mathematical or publication-priority audit has been performed.
