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

# Verification details

Run `python verify.py` in a clean Python 3 environment; the script uses only the standard library. The observed saved output is in `verify_output.txt` and concludes `ALL_VERIFY_OK`. It enumerates directed-arrow subsets and tests the actual graph path condition independently of the proof's cyclic-word reduction. Signed Lefschetz traces are checked for all rotations and global-arrow-reversal compositions in cycle lengths 5 through 10, totaling 90 transformations and 11,418 face records. Independently generated quotient chain complexes are reduced over two odd primes in cycle lengths 5 through 8; both primes agree with the predicted rational Betti numbers in these cases.

No finite test establishes the infinite theorem or rules out 2-primary integral torsion in quotients. The published integral homology concentration and connectivity are imported from arXiv:2601.05670v1; the integral homology **operator** relation follows from rational operator equality and torsion-freeness. No independent audit has taken place.
