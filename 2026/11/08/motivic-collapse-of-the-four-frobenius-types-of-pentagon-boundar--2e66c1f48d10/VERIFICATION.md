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

# Verification and limits

Run `python3 check_pentagon.py` with the standard-library Python interpreter. It computes the ten exceptional classes on the four-point blowup, their complete intersection graph, all twelve pentagons and 120 oriented cycles, proves exact determinant \(\pm1\) for each lattice basis, and verifies the anticanonical class sum. It tests the five rotations and five reflections for their first twenty extension powers over five small field sizes, checks the blowup and explicit affine counts for sample finite fields, and performs a formal symbolic \(K_0\) scissor-expression comparison using independent generators for \(\mathbb L\), \([\operatorname{Spec}\mathbb F_{q^2}]\), and \([\operatorname{Spec}\mathbb F_{q^5}]\).

The actual output in `verification_output.txt` ends `ALL_TESTS_PASSED`. The general proof requires the blowup/blowdown existence arguments, Galois twisting, finite étale divisor normalization identity, and the étale localization sequence in `RESULT.md`; these are mathematical arguments not asserted as empirically exhausted by finite tests. The published geometric classification, both split/quadratic affine cases, and the known cohomological orientation character are distinguished from the new claimed unlocalized motivic identities. Historical priority remains provisional; independent scientific audit has not been performed.
