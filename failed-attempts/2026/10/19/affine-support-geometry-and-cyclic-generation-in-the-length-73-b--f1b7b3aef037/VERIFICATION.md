---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

An independently written exact checker verifies that T^9+T^4+1 has no monic factor of degree ≤4, constructs the order-73 root T^7, and finds the two minimal polynomials by testing monic degree-nine polynomials and excluding lower degrees. Their product is 0x5165f. Remainders modulo g distinguish weights up to two from each other and from all triples, excluding nonzero weights 1 through 5. Equal remainders of disjoint triples give exactly 876 supports, each with 10 triple partitions. Generating the action by rotation and doubling gives the two disjoint orbits of sizes 219 and 657 with the stated seeds, covering all supports. The independent checker computes gcd(f_S,X^73+1)=0xf3ae1=(X+1)g for all 876 supports; the shifted span is the corresponding cyclic ideal of dimension 54 and equals the even subcode since g(1)=1. Direct enumeration of all coordinate pairs gives (6,4,5,5) in the specified four cosets, histogram (4:657,5:1314,6:657), and point replication 72. This is an exhaustive finite check for the specified coordinate convention, not a result for other code lengths.

## originality

FAIL

No inspected earlier statement gives the three invariants verbatim, but the October 4 primary certificate gives the complete set of minimum words in twelve translation classes, with the same coordinates and both later seeds. The exact three additions are short mechanical transforms of its twelve representatives. The review computed all three from that certificate alone, without searching the code or using the frozen enumerator.

## value

FAIL

The code and its minimum-support population are natural, and the incidence and cyclic-generation questions are reasonable. The claimed contribution nevertheless consists entirely of routine transforms of a published exhaustive set of cyclic representatives. Two representative checks and an orbit argument make the proof economical, but there is no surviving nonmechanical mathematical claim or valuable repair in this package.

The dated certificate retains the supplied scientific assessment, sources and limitations.
