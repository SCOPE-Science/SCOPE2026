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

The exact stationary-phase fibre identity, noncancellation for one or two odd-order roots of unity, the \(p=2\) parity obstruction and the \(p=3\) ninth-cyclotomic obstruction were checked algebraically. The imprimitive case was reduced exactly to the minimal polynomial of a primitive \(p\)-th root and thus to permutation of \(\mathbb F_p\). Rootless derivative counts, depressed-cubic collision counts, multiplicities of lifts, and the Fourier-diagonalization normalization were independently recomputed.

The companion `verify.py` computes the actual Fourier sums via exponent histograms and exact cyclotomic divisibility; it does not invoke the stationary-phase identity. Its completed execution produced `ALL_EXACT_CUBIC_MOMENT_CHECKS_OK` with residue-level counts tested at \(p=2,3,5,7,11,13\). It covers all \(64\) frequencies and all selected deformations at \(p=2\), all \(729\) frequencies in three deformation examples at \(p=3\), all \(15,625\) frequencies in two \(p=5\) examples, all \(117,649\) frequencies for the unperturbed \(p=7\) curve, and deterministic randomized samples for deformations at \(p=7,11\). To reproduce, run `python3 verify.py` in Python 3 using only its standard library. The script explicitly asserts the formula for each checked frequency.

These finite checks corroborate but do not certify the universal statement. No external mathematical validation or independent audit was performed. The classification does not determine the nonzero Fourier coefficients or behavior for ring exponents greater than two.
