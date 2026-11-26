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

A nonempty column intersects only one occupied component, and adjacent column masks intersect precisely when that component continues. Parity is forced from each finite left end and is freely initialized on an infinite-left component to satisfy any right closure. The primitive right-resolving graph has at most seven lifts per finite word, justifying the entropy retained as context. For an n-periodic marked word containing a break, each occupied component is finite and there is exactly one n-closed lift iff the word is admissible. With no break the single occupied component is bilateral and admissible; it has 2 lifts when the singleton count is even and 0 otherwise (including n=1). The signed trace of W is exactly the excess; the formal trace determinant identity yields the stated quotient. Independently counted components in an n-column quotient graph using integer displacement consistency to distinguish winding components, and checked both characteristic polynomials exactly. Periods 1–8 gave 4,14,40,158,514,1844,6374,22446. Replay: python3 /workspace/branches/independent_reproduction.py 4 (SymPy).

## originality

PASS

The repaired result asserts only the explicit periodic census and zeta as distinct. Neither the same entropy nor the seven-state matrix is claimed as new. No inspected statement supplies the periodic correction or its determinant quotient. Access and unindexed-priority limitations remain.

## value

PASS

The all-period fixed-point census at the first interacting width gives an exact benchmark a researcher testing wider-strip representations can use. It resolves a genuine infinite-component issue: closed finite counts, periodic state paths, and periodic visible configurations are inequivalent. The parity correction is an explicit structural explanation, not just a small periodic table or a repeated entropy estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
