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

# Verification and reproducibility

The standalone `verify.py` requires only Python 3 and standard-library modules. Run `python3 verify.py`; successful execution prints `PASS 9282 finite exact tests`, the first nine count values, and confirmation of all nine argument classes through \(n<6561\). It uses the defining binomial sum for small arguments/indices, independently uses the exact integer Legendre recurrence for all nine argument residues through \(3^8\), and checks the digit characterization, binomial scaling, and count formula against direct enumerations.

The infinite statement follows from the symbolic proof: polynomial Lucas reduction, Legendre parity and its generating function, exact binomial scaling modulo nine, the two digit recurrences, and the six-state rational generating function. Finite tests cannot certify the universal quantifier. The theorem does not claim congruence as a coefficientwise polynomial identity, or a result for modulus twenty-seven. The associated scientific review is a self-review; independent mathematical audit has not been performed.
