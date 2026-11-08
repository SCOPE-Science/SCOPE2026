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

# Verification

Run `python verify.py` and `python verify_fano.py` in the extracted directory with Python 3.9 or later. No third-party modules or network connections are required.

`verify.py` constructs the parity-check matrix by all \(7!\) permutations of the seven nonzero vectors of \(\mathbb F_2^3\). Each of \(128\) binary vectors is tested against the three parity checks; the \(16\) valid vectors are then evaluated directly under cyclic symbol-pair reads. Actual codeword-set equality identifies the thirty distinct indexed codes. It checks the spectrum coefficients and counts \((2,14,14)\); success prints `DIRECT_VERIFY_OK`.

`verify_fano.py` independently generates all seven Fano lines, checks pairwise intersection, visits all \(360\) unoriented Hamilton cycles, verifies occurrence multiplicities \((24,168,168)\), first and second incidence moments \(504\) and \(168\), and enumerates the complete 168-element automorphism group to check the three resulting cycle orbits. Success prints `FANO_VERIFY_OK`.

Both checks were run successfully in the preparation environment. The finite program checks do not independently prove claims at other block lengths; the claim is confined to length seven and has a self-contained counting proof. Independent scientific audit remains unperformed.