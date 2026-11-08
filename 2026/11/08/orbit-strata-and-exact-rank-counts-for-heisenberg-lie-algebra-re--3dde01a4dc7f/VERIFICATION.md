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

# Reproducibility and limits

The standalone Python 3 script `verify.py` has no third-party dependencies. Execute it from a directory containing the script using `python3 verify.py`. Its recorded stdout is `verification_output.txt`.

The checker exhaustively scans all \(3\times3\) matrices over \(\mathbb F_2\) and \(\mathbb F_3\) and verifies each candidate directly against \(P^2=P\) and \(P([x,y])=[P(x),P(y)]\) for all basis pairs. It also constructs every allowable quotient projection in dimensions three and five and directly checks the original equations for each central lift, while independently evaluating the finite-field orbit-size formula. For \(n=2,q=2\), the orbit-rank counts are \(1,240,480,480,1\), distinguished by the image rank and restricted alternating rank, giving 1202 maps. The output ends with `HEISENBERG_IDEMPOTENT_RETRACTION_ORBIT_COUNTS_OK`.

The checker uses prime-field arithmetic. The general finite-field and arbitrary-field statements are established by the mathematical proof, not by extrapolation from this finite census. No external or independent formal verification has been performed. The test concerns ordinary Lie algebra endomorphisms; no claims about restricted-Lie structures or the unreduced equation scheme are tested.
