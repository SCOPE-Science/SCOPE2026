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

**Exact reproduction:** With Python 3 and SymPy, run `python checker.py` in the extracted directory. The checker was executed from this package and printed `PASS: 239 exact symbolic/rational assertions`. It independently builds the continuous-time generator from configurations of \(L-1\) particles on rings of length three through seven, solves stationary distributions by exact linear algebra, and compares currents to the spanning-tree formula. It checks the four-site factorization symbolically and both exact rational examples.

**Analytical proof:** The full-range statement comes from the enumerated rooted-tree weights, a standard directed-cycle flux cancellation, linear independence of the Bernstein basis, and direct factorization of a four-variable identity. The checker is supplemental confirmation; it does not establish validity for infinitely many ring lengths or arbitrary positive real rates.

**Source checks:** Source arXiv:2512.03316v1 dates from 2025-12-03. The relevant main text and appended supplementary argument were read. Derrida's 1983 general periodic-walk formula was read from the author-hosted copy; that foundational identity is credited, not presented as new. The model does not cover intermediate densities or thermodynamic limits.
