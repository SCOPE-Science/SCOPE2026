---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

From p_(2r)=0 and p_(2r+1)=1-p_r, ones of every factor occur in one local parity, and neither 11 nor 0000 occurs. At odd length the sole even cyclic gap between 1s must straddle the cut in any represented rotation; its at-most-three boundary runs allow at most three cuts. Zero-one factors have a singleton orbit. For B=mu^(2j)(0), applying mu^(2j) to 00 gives BB as a factor, and its three distinct rotations B0,0B,00B[:-1] are represented. Morse-Hedlund plus known c_p(2^k)=2 yield limsup at least 1/3 and liminf zero. Independent finite factor enumeration at odd lengths 1,3,5,7,9,17,31,65 found maximum one or three, corroborating not proving the quantified statement.

## originality

PASS

Best-of-knowledge originality survives statement/implication comparison: Lie complexity counts completely represented cyclic orbits, whereas this counts the size of each partially represented orbit at odd lengths. The 2014 Cassaigne result c(2^k)=2 is at even dyadic lengths, no odd class-size ceiling. The named reductions and remaining inaccessible plausible sources are recorded as residual risks, not treated as proof of originality.

## value

PASS

Partially represented conjugacy classes are central to cyclic factor complexity. A universal sharp ceiling at every odd length and infinitely many extremal witnesses explain a nontrivial coexistence of linear odd-length growth and bounded dyadic complexity; not merely recomputing a known Lie table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
