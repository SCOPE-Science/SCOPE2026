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

# Reproduction and limits

Run `python3 verify_arch_and_polynomial.py` and `python3 verify_direct_subsequences.py` in the extracted package directory using the Python 3 standard library. The former uses the greedy complete-arch count and direct scattered-pair enumeration for all balanced binary words of length \(2k+2\), \(1\le k\le7\), compares the complete coefficient histogram to the independently computed three-branch polynomial, and verifies the exact parity-dependent central coefficient gap for \(2\le k\le100\). The latter uses the semantic definition of subsequence universality: for each balanced word at \(1\le k\le6\), explicitly test all \(2^k\) binary length-\(k\) patterns by greedy subsequence matching. Its 4,704 words are drawn from every balanced word in those six parameter cases, not from a random sample.

`verification_arch_output.txt` and `verification_direct_output.txt` contain the actual outputs from these programs. They terminate with `VERIFY_OK arch_vs_polynomial_k1_to7=7 central_identity_k2_to100=99` and `VERIFY_OK independent_semantic_cases=4704` respectively. This is evidence for the finite computations; the unrestricted theorem is established by the greedy-arch case partition and exact binomial difference algebra in `RESULT.md`, not by extrapolation of the code. The explicit binomial coefficient convention handles negative lower indices and the small-parameter boundaries.

The analytic correctness check also compares the one-variable total \(2^{k-2}(k^2+3k+8)\) to the previously known unrefined balanced-index result, separating known marginal information from the claimed new weighted information. No independent external audit has been performed.
