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

# Reproducible verification and limits

The exact domain is all ordered pairs of square-zero \(3\)-by-\(3\) matrices over every finite field \(\mathbb F_q\). The proof is in RESULT.md. The finite tests are corroborations, not substitutes for the projective-idempotent argument.

Run, from the extracted package root, `python3 artifacts/check_fibers.py` and `python3 artifacts/check_direct.py`. No external dependencies are required. The known-good output of these commands concatenated in that order is stored at `artifacts/check_results.txt`.

`check_fibers.py` constructs square-zero matrices independently through nonzero rank-one factorizations, evaluates the complete additive convolution, and compares class-predicted counts with the actual convolution. It exhausts all 512, 19,683 and 262,144 targets over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), respectively, and tests 94,325 targets over \(\mathbb F_5\) (all nonzero fibers plus reproducible samples). Arithmetic in \(\mathbb F_4\) uses polynomial representatives modulo \(t^2+t+1\). `check_direct.py` uses a different construction: it directly enumerates all matrices and tests \(A^2=0\) by full multiplication over \(\mathbb F_2\) and \(\mathbb F_3\), then tallies every ordered sum.

The output contains the success markers `SQUARE_ZERO_SUM_FIBERS_ALL_CHECKS_PASS`, `DIRECT_CHECK_PASS 2` and `DIRECT_CHECK_PASS 3`. It records \(22,105,316,745\) square-zero matrices at orders \(2,3,4,5\), and \(148,2835,19216\) representable targets at orders \(2,3,4\).

The unrestricted proof requires the following independently checkable lemmas: rank of a square-zero endomorphism in dimension three is at most one; rank-one sum rank-one forces a shared image or row line; rank-two decompositions correspond to complementary rank-one projections; and projector trace constraints reduce to eigenline/kernel incidence. Similarity-centralizer sizes yield the class populations. None relies on a finite enumeration. The unverified limits are higher dimensions, conjugation-orbits of pairs, and independent historical priority; independent external audit has not been performed.
