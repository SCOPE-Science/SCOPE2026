---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

In the normalized two-boson basis, hopping out of a doublon carries a factor √2. The unsigned incidence map R from distinct leaf pairs to hub–leaf states has RRᵀ=(m−2)I+J; eigenvalues 2(m−1) on constants and m−2 on the sum-zero leaf space give the two hopping magnitudes to the separated leaf-pair states. Including doublons, the squared first couplings are 2(m+1) in the trivial sector and 2 in the standard sector. In the trivial sector the orthogonal doublon combination gives energy U, and rank m of R leaves exactly m(m−3)/2 zero modes. The remaining arrowhead determinant is (x−U)(x²−b²)−a²x with the indicated squared couplings; this gives both proposed cubics and the dimension count. Both cubics change signs in each of (−∞,0),(0,U),(U,∞), making all roots simple and excluding flat-level collisions for the entire specified range. Subtraction is m(U−3x), and evaluating the standard cubic at U/3 gives 2U[9(m−3)−U²]/27, proving the only crossing. On (0,U) each cubic is positive to the left of its middle root and negative to the right. The sign of the standard cubic at U/3 places its root to the right of U/3 below U* and to its left above U*; the subtraction identity at that root orders the symmetric root as claimed. Exactly one trivial and m−1 standard eigenstates give the crossing multiplicity. Both supplied checkers and VERIFICATION.md were inspected, not executed; the Gram-matrix and sign checks establish all m analytically.

## originality

FAIL

The mathematics is correct, but an independent distinct contribution is not established on the inspected record. The same-day indexed complete-bipartite result does not literally state the star theorem (it explicitly requires both shores of size at least two). Its explicit spectral blocks and crossing proof nonetheless give the entire frozen claim by a mechanical boundary reduction: there is no distinct-pair state in the singleton shore, so delete its decoupled zero row and column in the symmetric arrowhead, and retain only the large-shore standard and incidence blocks. The two surviving cubics, crossing uniqueness, multiplicity and order reversal specialize exactly, not just the numerical threshold. This is a finding of demonstrable mathematical coverage, not a claim about which same-day result was first. The older Pouthier paper is a separate, partial overlap for the symmetric sector, not a basis for the fail verdict.

## value

PASS

As mathematics, the full interacting spectrum and tunable m-fold degeneracy of a canonical finite network are useful, with an exact level-order reversal and a relevant distinction between the hub-visible and standard multiplets. This value judgment is about the theorem; the frozen record supplies no distinct valuable remainder after the verified broader block comparison and therefore cannot be accepted as an independent new finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
