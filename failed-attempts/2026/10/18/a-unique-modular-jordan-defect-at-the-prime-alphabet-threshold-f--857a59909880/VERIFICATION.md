---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The result concerns the full unital monoid algebra. The word-count recurrence gives b_r=(x)_r, including b_(n+1)=0. For n=p this gives x^p-x=b_p, the sum of distinct full words. Every full word absorbs every basis word on the right, so all columns of L_b_p are the same nonzero vector and its rank is one; L_b_p^2=p! L_b_p=0 and x b_p=0 by the recurrence. The split annihilator T^2 product_(j=1)^(p-1)(T-j) forces all nonzero blocks to be simple and zero blocks to have size at most two, and T^p-T has rank one per size-two zero block. The integer matrix has characteristic-zero multiplicities n!/j! by the cited module formula and the derangement identity; independently, each word of length r acts as an idempotent of rank equal to the number of injective words on the remaining n-r letters. Traces of the falling factorials (L_x)_r then recover the same n!/j! by a triangular system. Reduction of the characteristic polynomial adds only the 0 and p multiplicities. The same annihilator before the collision has distinct linear factors, proving semisimplicity for n<p. Independent replay: python3 /workspace/check_frozen_mathematics.py 4 (NumPy), for p=2,3,5, dimensions 5,16,326. It checks the literal defect vector in every column and the requisite finite-field kernels. The frozen program constructs only the one-letter left-action columns, not the complete multiplication table as its verification prose says; that is sufficient for the stated finite checks, which are not the general proof.

## originality

FAIL

The full modular Jordan form is a direct corollary of the earlier Brauner–Commins–Reiner results and their multiplication definition. This is stronger evidence than mere overlap of the minimal polynomial: Lemma 2.5 already yields the exact orbit sum for x^p-x, so its rank on the full algebra is mechanically read off from the fact that every word in that sum contains the entire alphabet. No historical claim is made that the corollary was printed as a separate Jordan theorem.

## value

FAIL

The operator and the exact block size are naturally motivated, and a compiled corollary can be a useful reference. The specific invariant submitted here, however, is mechanically implied by prior explicit orbit-sum and spectral formulas with the defining full-word product and no additional structural argument. No independent valuable remainder is established for this narrow exact claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
