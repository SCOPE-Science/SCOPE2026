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

# Reproduction and verification

The new result has been checked by exact polynomial identities and by point counts with a completely separate finite-field implementation.

Run `python3 verify_cartier_rank.py` with SymPy. The script expands the hyperelliptic polynomial square, compares the full \(4\times4\) coefficient matrix, computes the cubic branch discriminant, verifies the semilinear stable-rank polynomial, factors its intersection with the elliptic Hasse divisor, excludes singular parameters, and enumerates the \(25\) coefficient pairs in the prime field. The successful output includes `GENUS4_P5_CARTIER_PASS 4 17`.

Run `python3 verify_point_counts.py` using only Python's standard library. For each of four rank witnesses over \(\mathbb F_5\), it independently constructs \(\mathbb F_{5^n}\) for \(1\le n\le4\), counts projective curve points including the two points at infinity, and derives the first four zeta-numerator coefficients using Newton identities. The successful output ends `GENUS4_P5_POINTCOUNTS_PASS` and reports the four stable ranks \(0,1,2,3\).

The complete geometric statement for all \(a,b\in\overline{\mathbb F}_5\) follows from the proof in RESULT.md; the finite point counts only test stated examples. Arithmetic ranks are not claimed to determine full Newton polygons or to certify supersingularity. Verification here does not constitute independent audit.
