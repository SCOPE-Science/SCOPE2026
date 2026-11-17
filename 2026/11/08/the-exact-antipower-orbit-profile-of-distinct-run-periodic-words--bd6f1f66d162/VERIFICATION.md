---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Each ordered unequal adjacent-letter boundary digram appears at exactly one phase, including q=2, so any equal nonmonochrome length-m factors would force the same phase. Equal factors at different phases are exactly monochrome inside the same run. Therefore the first possible index separation is the first modular distance not exceeding M-m; the phase-step orbit order is T=L/g. The subgroup minimum nonzero circular distance is gcd(L,m), giving sharp full-orbit threshold, and residue-class counting gives H. Cases m>=M, m>=L and T=1 are handled. Independent direct word enumeration checked 1692 configurations against both K and H, without extrapolating finite checks to arbitrary run lengths.

## originality

PASS

Full primary work of Kociumaka et al. gives generic algorithms counting antipower factors of a finite word, not a closed all-parameter phase-orbit theorem in a periodic distinct-run family. Other nearby published claims count Abelian powers or antipowers in aperiodic morphic sources. String equality versus Parikh equivalence and quantification over every phase/order make the submitted classification distinct.

## value

PASS

A natural tractable periodic word class has a complete uniform antipower profile and residue-sensitive phase census. It separates worst-phase guarantees from phases attaining the full block orbit, and identifies a sharp gcd transition; this is structurally informative even though general-purpose algorithms can enumerate any fixed instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
