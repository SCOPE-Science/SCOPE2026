---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For the four-site generator with bonds (1,1,1,k), the exact characteristic polynomial is zQ_{k,t}(z); substituting t²=4+s into the cubic discriminant yields P_k(s). All three nonconstant coefficients are strictly negative for k>0 because their quadratics have negative discriminants. P_k(0)>0 except k=1, and P_k(s)→−∞, giving one threshold; the k↓0 and k→∞ limits follow by dominant balance. Independently reconstructed exact SymPy characteristic polynomial and cubic discriminant in this run (initial simplification not canonical; polynomial factorization confirmed zero).

## originality

PASS

Avnit–Cohen 2023 treats stochastic ring spectra and quantum coherent effects, and Hurowitz–Cohen 2015 provides general ring machinery and asymptotic weak-link criteria. Retrieved abstracts and the submitted bibliography do not establish the exact all-k four-site monotone cubic discriminant, its unique threshold, or its k→∞ limit log(3)/2. Resultary semantic search found the assigned record but no clearly dominating earlier published finite four-site theorem. This is best-of-knowledge, not a proof of priority; the directly relevant Avnit–Cohen primary full text was not obtained for a comprehensive theorem-by-theorem comparison.

## value

PASS

A sharp minimal finite-state example differentiates real overdamped from complex underdamped relaxation, including a nontrivial strong-defect limiting boundary. It is a motivated complete parametric classification and useful benchmark, not merely an arbitrary numerical instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
