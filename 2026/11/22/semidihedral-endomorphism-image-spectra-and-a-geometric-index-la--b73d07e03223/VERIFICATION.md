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

# Verification and limitations

The proof is the exhaustive, symbolic three-case classification of images of the generators of \(G_n\) in `RESULT.md`. The three cases rely on the explicit order formula for elements in the noncyclic coset and the congruence \(\gcd(m,h-2)=2\); neither depends on computational interpolation.

The self-contained standard-library script `check.py` enumerates all candidate generator images satisfying all defining relations; computes the actual image of each homomorphism; verifies its rank and composition-idempotence; constructs all automorphisms from the same enumeration; and calculates automorphism-conjugacy orbits. Verified group orders are \(16,32,64,128\); expected coefficient lists and the final success marker are preserved in `CHECK_OUTPUT.txt`.

Reproduce with `python3 check.py` in a directory containing the embedded script. No external package, network access, random seed, or external data is required.

The finite tests are corroboration only: they do not prove the infinite formulas or the asymptotic theorem, whose proof is in `RESULT.md`. Comparisons with the inaccessible 2002 cyclic-semiproduct endomorphism paper remain a scientific priority limitation; no independent mathematical validation has been performed.
