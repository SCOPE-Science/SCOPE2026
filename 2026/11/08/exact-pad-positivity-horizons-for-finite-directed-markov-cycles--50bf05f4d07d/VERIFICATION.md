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

# Verification of exact directed-cycle Padé positivity

Execute `python artifacts/verify.py` using Python 3 and SymPy. The program symbolically constructs each actual rational transition matrix for the six finite dimensions two through seven. It checks the row sums and circulant entries, every reduced denominator has strictly positive constant and nonnegative coefficients, the two and three-state entries are nonnegative, and the four nearest-neighbor numerators are exactly the stated negative multiples of their defining \(F_n\). The four Descartes sign counts and exact rational root brackets are checked. It certifies positivity of each of the other entries through either ordinary coefficient nonnegativity or a fully rational transformed-polynomial certificate on \(0<h<4\). It also checks the Padé sixth/seventh Taylor coefficients and the cyclic group-inverse formula in finitely many examples.

The recorded output in `artifacts/verification.txt` corresponds to the included standalone script. The source code and rational coefficient tests are the verification evidence; the success log alone is not relied upon. The assertions about every integer dimension \(n\ge8\) and the large-step expansion for all \(n\ge4\) follow from the explicit analytic path-length and group-inverse arguments in the proof, not from these finitely many tests. Bounds on floating-point rounding, general Markov generators and internal RK stage positivity are not asserted. No independent scientific audit was performed.
