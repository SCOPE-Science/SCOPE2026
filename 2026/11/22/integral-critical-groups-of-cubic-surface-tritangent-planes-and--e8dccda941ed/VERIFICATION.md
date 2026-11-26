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

The frozen group and spectrum calculations are mathematically correct; the repaired result is independently rechecked on the exact same graphs. In the six-point blowup the tritangent triples are the 30 triples E_i,L_ij,Q_j with i!=j, and the 15 partitions into three pairs of indices for L_ij; this follows by comparing H-degree and exceptional coefficients with -K. They are anticanonical plane sections. An independent reconstruction and exact reduced-Laplacian calculation (replay /workspace/branches/78d5923b-33c2-43b6-a947-13a107255317/independent_check.py with independent_check.log) verified the SRG parameters and local factors without executing the frozen verifier. Primary catalogue identity was separately verified: Spence's live srgraphs.php links the public binary file SRGs/45-12-3-3. Reading the raw response gives 3510 rows of 45 binary digits; rows 46–90, counted among those rows, agree with all 45 rows in the frozen spence_second.txt. For both graphs A^2=9I+3J gives spectra 12^1,3^20,(-3)^24 and reduced determinant 3^62*5^23. Measured 3-adic counts (including valuations zero) are (15,10,5,14) for tritangents and (17,8,3,16) for Spence matrix 2. Local elimination has no saturated pivot and the counts exhaust the determinant valuation 62. The 5-adic counts are (21,23) for both; the repaired proof also derives the 5-part directly because L(24I-L)=135I-3J annihilates the degree-zero quotient by 135. Pairing primary valuations in sorted order yields the repaired full group and the claimed generator gap. Over Z_(3), the tritangent group also follows from the published Levi-group calculation by the verified block elimination described below. The corrected RESULT.md in /workspace/repairs/2 is the witness claim with this explicit baseline; no data or verifier change is needed.

## originality

PASS

Pass for the repaired graph-specific 3-primary determination of Spence matrix 2 and its use as a cospectral witness against the tritangent graph. The frozen account gives too much independent novelty credit to the canonical group's determination: the distinct same-day Levi record 616774bc1c5b mechanically yields the canonical 3-part and the parameters force the 5-part. This is demonstrable coverage of that subclaim, not evidence of same-day priority or of coverage of Spence matrix 2. The repair states the comparator result as the finding, deriving or crediting the canonical and non-3 input. The strongest inspected parameter theorem limits the comparator to two forms at its given 3-rank but does not select one; the primary matrix and classification table do not state the exact comparison.

## value

PASS

Rather than another standalone computation on the canonical baseline already implied by the Levi result, the repair supplies a checkable natural witness in the published classification, tied to a standard incidence graph from cubic surfaces. It distinguishes their integral groups at the one prime where parameters leave graph-specific ambiguity, and gives the exact elementary divisors beyond the rank obstruction. This is useful as an explicit reference comparison for parameter-based critical-group theory: the order and whole spectrum agree, the 5-part is forced, but the 3-part and its minimum generator number differ. It makes no claim that the group distinguishes all 78 graphs or that a general method is new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
