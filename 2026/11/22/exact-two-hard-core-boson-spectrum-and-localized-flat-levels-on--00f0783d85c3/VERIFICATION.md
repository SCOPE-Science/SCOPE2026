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

# Verification notes

The separate `VERIFY.py` program constructs the two-token adjacency matrix from the base friendship-graph edge list, without using the symmetry decomposition or precomputed spectra. It evaluates the integer characteristic polynomial with SymPy and compares it to the factored formula for \(m=3,4,5,6,7\), covering matrix sizes \(21,36,55,78,105\). Each comparison returned `True`. The proof of all sizes is the orthogonal decomposition and unsigned incidence Gram calculation in `RESULT.md`; no finite sample establishes an infinite theorem.

The three fixed-energy orthogonal mode families have dimensions \(\binom m2\), \(m(m-2)\), and \(m(m-3)/2\) with total complement dimension \(5m\). The last family is zero-dimensional at \(m=3\). The limiting measure is a multiplicity-counting measure, not a claim about all localized initial states.

The other closely related published calculation treats the **Laplacian** of the same nonregular token graph; it does not yield a scalar-shift formula for the adjacency Hamiltonian. The originality assessment is a best-knowledge comparison, not definitive proof of priority. Independent scholarly audit has not been performed.
