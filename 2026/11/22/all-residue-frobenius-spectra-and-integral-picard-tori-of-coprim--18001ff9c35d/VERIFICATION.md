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

The projective closure of \(T_n(X)-T_m(Y)=0\) is normalized by \(\mathbb P^1\). The proof accounts separately for its two-branch finite nodes and one-branch infinity singularity. The finite node-label construction in `verify.py` enumerates pair indices modulo \(2mn\); Frobenius multiplies each index by \(q\). Its orbit signs test whether the returning Frobenius fixes or interchanges normalization branches.

Execution: `python3 verify.py`. The saved `check_output.txt` reports `CHEBYSHEV_ALL_RESIDUES_ORBITS_AND_ZETA_OK`, 1471 exact residue configurations, 498 direct prime-field evaluations and 162 quadratic-extension evaluations. Prime-field counts are obtained by directly enumerating the polynomial equation; quadratic-field counts use a separately coded quadratic extension field and its own polynomial evaluator. The \((3,8,7)\) example is explicitly tested in both degrees one and two.

The universal assertion follows from the written normalization and local-unit proof, not the bounded checker. Historical priority and mathematical proof have not been independently assessed. No external certification is claimed.
