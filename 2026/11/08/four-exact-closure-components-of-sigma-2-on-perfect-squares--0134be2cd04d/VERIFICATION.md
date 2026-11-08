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

# Reproduction and limitations

Run `python3 verify.py` with the Python 3 standard library. It checks seven finite rational Euler-product comparisons, the rational sum-of-three-prime-ratio bound, the \(\pi^2/9\) overlap lower bound, and three rational interval-separation inequalities. It also evaluates every \(F(n)\) for \(1\le n\le60000\) independently from the prime factorization of \(n\) as a diagnostic. Expected output begins `VERIFY_OK` and ends with a statement that the infinite claims require the proof.

Correctness of the infinite statement rests on the mathematical argument in `RESULT.md`, including a published prime-ratio lemma, convergence of the Euler product, and the binary-subsums lemma. Finite tests are corroboration, not proof of a universal quantifier. The closure endpoints may not be attained on finite inputs. No independent audit or external validation has been performed.
