---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

The group law gives \(\overline K_{n-1}\\veeee K_n\) for odd \(n\) and \(\overline K_{n-2}\\veeee(K_n-\\fracrac n2K_2)\) for even \(n\). The package constructs explicit rank-two symmetric Gram witnesses and classifies every two-white configuration; direct brute-force reconstruction independently reproduced the claimed polynomials for \(3\le n\le7\). The inspected verifier performs the same group-law construction, exact rank check, and exhaustive subset checks through the stated small range.

## originality

FAIL

The rank-two and polynomial conclusions are routine consequences of older general theorems once the standard dihedral noncommuting-graph structure is written down. Barrett--van der Holst--Loewy characterize all real graphs of minimum rank at most two by the form of the complement; both parity cases fit that characterization immediately. Boyer et al. Theorem 1 gives the \(N-2\) coefficient as the number of vertex pairs with distinct deleted neighborhoods, while the universal top coefficients are already fixed. Counting those pairs in the standard dihedral join/cocktail-party description gives exactly the assigned parity formulas and minimum-set types.

## value

FAIL

The dihedral graph is natural, but after the standard group-derived graph structure is known the asserted minimum rank and the complete three-term zero-forcing polynomial are direct applications of two generic published theorems plus elementary pair counting. That is a routine specialization rather than a motivated new structural result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
