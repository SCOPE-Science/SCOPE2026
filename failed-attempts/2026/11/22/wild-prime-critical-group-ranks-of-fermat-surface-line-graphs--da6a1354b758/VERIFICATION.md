---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The three families are the lines of the complex degree-p Fermat surface; substituting their equations gives the same-family rook rule and the three cross congruences, with the +1 in the A–C rule because λ²=ζ. The graph is connected, of degree 4p−2. Over F_p the two fixed axis directions give the diagonal 2 of EHEᵀ and the three exchanged diagonal-fiber pairs give the cross adjacencies, so L=−EHEᵀ. Function evaluation in a,b is injective for polynomials of separate degrees below p. In each family the four degree-k ridge forms have ranks 1,2,3 at k=0,1,2 and rank four thereafter (use the coefficients of a^k,b^k,a^(k−1)b,a^(k−2)b²); thus K=ker E has dimension 18 with fiber polynomials of degree at most two. Since im Eᵀ=K^⊥ and H is an involution, the lost rank from im Eᵀ upon applying EH is exactly the radical dimension of H restricted to K. For p≥7, each pairing is a sum of degree-at-most-four polynomials, zero in F_p, giving rank 12p−36. Fresh direct elimination at p=3 and p=5 independently returned 7 and 26, giving the required exceptions. A connected graph has one free summand in its full integral Laplacian cokernel, so n−1−rank(L mod p) yields precisely the stated p-ranks.

## originality

FAIL

The uniform rank and quintic boundary are already explicitly covered via the Fermat divisor-intersection Gram matrix in the public Double Ladder manuscript. Writing G=A+(2−p)I and L=(4p−2)I−A shows G+L=3pI; hence modular ranks coincide, and connected cokernel rank subtraction gives the exact graph critical-group p-ranks without further scientific input. This is equivalent coverage, not an inference about historical priority based on dates. The uncovered cubic boundary is a routine consequence of classical cubic surface geometry and was also reproduced directly; it does not sustain the frozen all-prime claim as distinct.

## value

FAIL

Wild critical-group ranks of these natural graphs would be useful and are not determined by the ordinary adjacency spectrum. But the proposed exact invariant is mechanically deducible from the explicit known modular rank of the divisor matrix via a scalar diagonal shift and one connected-cokernel subtraction, while the cubic completion is elementary. The frozen work does not determine the genuinely different integral Smith invariants or establish a new general-purpose lemma beyond this covered calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
