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

Use Python 3.10 or newer with the standard library; run `python3 VERIFY.py` in this directory. The code implements the exact bipartite count formula, an independent exhaustive enumerator for small labeled allocations with an unassigned state, an explicit multipartite construction, a direct test of maximality and EF1, and a Stirling-number count of maximal feasible outcomes for the odd balanced family.

In the completed checks, the script reported `PASS: 121 exact count comparisons; 116020 constructive checks; one independent maximal-outcome count`. It printed the odd balanced cases with numbers of fair and total maximal feasible assignments: \((t,\text{fair},\text{total})=(3,12,54),(5,240,127460),(7,10080,1932563262),(9,725760,92742026116392)\).

These finite tests do not establish the infinite-family theorem. The proof of the general existence and enumeration statements is analytic in `RESULT.md`. The inequality yielding superexponential scarcity follows from explicit subclasses of set partitions and factorial estimates; the verifier checks selected exact finite instances rather than estimating its asymptotic error.
