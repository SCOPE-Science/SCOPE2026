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

An independent derivation of the character sum is supplied in `RESULT.md`. The separate `nilpotent_spectrum_checker.py` enumerates the cone directly and recomputes exact Fourier values. On fields of sizes \(2\) and \(3\), it exhausts, respectively, \(512\) and \(19683\) frequencies and independently confirms all seven eigenline-count multiplicities. It tests \(701\) fixed-seed frequency vectors each over fields of sizes \(4\) and \(5\). The finite tests are not used to conclude a universal theorem. For all \(q,n\), correctness rests on the exact hyperplane character-orthogonality identity and the listed centralizer-class counts. The least singular values are witnessed by the explicit matrix types in the proof. The relevant historical orbit-Fourier chapter was not available in full, and no independent mathematical audit has been performed.

Reproduction: `python3 nilpotent_spectrum_checker.py` (requires NumPy). Expected final line: `ALL_MINIMAL_NILPOTENT_SPECTRUM_CHECKS_OK`.
