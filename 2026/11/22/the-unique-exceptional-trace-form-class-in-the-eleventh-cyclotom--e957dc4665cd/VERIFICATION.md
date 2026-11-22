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

## Reproduction

Run `python3 check.py` in the same directory. Python 3's standard library is sufficient. The script builds exact elements of \(\mathbb Q[Z]/\Phi_{11}(Z)\) with rational coefficients and checks the inverses of \(2-Z^k-Z^{11-k}\) for each \(k=1,\ldots,5\). The real-field trace is one-half the full cyclotomic trace. The resulting Gram matrix has diagonal entries \(11\), off-diagonal entries \(3\) or \(4\), and determinant \(75625\). There are no floating-point or probabilistic steps.

The nonsingular matrix proves that five equally minimal cyclotomic units constrain the positive embedding weights to one ray. This is a finite exact algebraic certificate for that lemma. It does **not** check the infinite claim that the reference form has minimum \(10\); that statement follows from the independent mathematical proof of Chang, arXiv:2611.15432v1, Lemma 5.5 and Proposition 3.4. The published assertion that a nonunit minimum must have norm \(11\) is likewise an external premise (Corollary 4.9). Therefore code execution alone does not certify the whole theorem.
