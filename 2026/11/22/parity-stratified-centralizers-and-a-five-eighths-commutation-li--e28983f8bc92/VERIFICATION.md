---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For nonboundary words with lengths a,b, the concatenation loses exactly one letter if the junction letters agree and otherwise none; an alternating word reaching length m represents the absorbing z. Equal starts and equal length parities give equal products without needing absorption. Different starts prohibit equality before absorption, and simultaneous absorption requires a+b>=m for different starts with both lengths odd, or a+b>=m+1 for every remaining case. For m=2k, the numbers of same-start and opposite-start partners are k+j-1 and 2j-1 at a=2j-1 or 2j (the latter restricted to j<k); for m=2k+1 they are k+j-1 and 2j-2 at a=2j-1, and k+j-1 and 2j-1 at a=2j. Including 1 and z gives the claimed spectra, including the extra even-m central elements of length m-1. Summing gives 10k^2+6k or 10k^2+12k+4 with denominator (2m)^2. A separate finite word-concatenation/run-contraction check agreed for every element at 3<=m<=24; generality is from the predicate and interval counts, not the test.

## originality

PASS

Best of current knowledge, the exact all-element dihedral monoid centralizer spectrum and parity-dependent pair count survive the comparisons. Normal forms and the algebra-center results are prior, and the title of the latter does not settle this monoid question.

## value

PASS

Centralizer sizes distinguish how each element of the natural rank-two test family participates in commutation, beyond whether the monoid is commutative or what its center is. The full spectrum shows two additional central elements at even braid length and identifies the persistent 5/8 proportion with exact finite corrections. The parity stratification and probability are reusable baselines for comparison with other zero-Hecke types, rather than a finite sample or an algebra-center rephrasing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
