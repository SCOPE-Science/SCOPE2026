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

An adjacent unequal swap reverses inversion parity. The first unequal designated pair remains first after the swap, so exchanging it partitions all nonfixed words into disjoint graph edges without changing content. Fixed words consist of doubled letters and possibly a last singleton, and have even parity since cross-pair inversions come in fours and inversions with the singleton in twos. The edge-and-singleton partition bounds the independent set by the even side, which attains the bound. Fixed words have the required count F in each composition, and globally have q^ceil(n/2) choices. The n=1 case and zero multiplicities cause no exception. The finding treats detection, not correction.

## originality

FAIL

Kim's published sign-reversing involution for skew tableaux specializes to precisely the claimed adjacent-edge matching, not merely to the inversion-parity enumeration. To see this, place each symbol's copies in its own horizontal skew row, with disjoint column sets. Assign the label j to the next cell in the row prescribed by the j-th letter. Standard fillings and words of the composition are then in bijection. Kim's first pair of consecutive entries 2i−1,2i in distinct rows and columns becomes the first unequal designated pair of letters. For odd word length, fix the final symbol and apply the same even-size construction separately on each prefix slice. The parity of unmatched words and the independence bound then follow immediately, completing the exact formulas without a new structural theorem. This is broader prior coverage by reduction; it is not a claim that Kim states a detection code result.

## value

FAIL

The single-swap detection optimum is a natural quantity, but the claimed advance over classical parity enumeration is the matching certificate, and that certificate is already supplied by the same first-pair construction in a broader result. The swap-channel reformulation and counts are useful exposition, not a distinct nonroutine contribution or a new code property beyond the implication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
