---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For general smooth complex plane curves d≥4, the classical Plücker invariants are D=d(d−1), F=3d(d−2), B=d(d−2)(d−3)(d+3)/2. Division by d and Euclid give gcd(D/d,F/d)=gcd(d−1,3). When d≡1 mod3, B/d is nonzero mod3, so gcd(D,F,B)=d. Pair gcds arise from d²−9≡−8 (mod d−1), a trivial parity split and factoring out d−2. Independently checked all three claimed pairwise gcd expressions and triple gcd for every integer 4≤d≤20000 using Python integer arithmetic; this checks, but does not replace, the elementary for-all-d proof.

## originality

FAIL

FAIL as an independent original mathematical claim: published classical Plücker formulas already specify all three counts as explicit polynomials in d. The asserted gcd classification is a direct, short Euclidean arithmetic corollary with no new enumerative curve geometry or independent hypothesis. Absence of an exact gcd sentence in a literature search is not enough; the stronger formulas determine the entire triple and all pairwise gcds.

## value

FAIL

FAIL: the normalized gcd and modulo-3/4 pairwise arithmetic are routine exercises in gcd of three known low-degree polynomials. The package does not motivate a research use of this precise common divisor beyond noting that one can compute it, or show a new geometric obstruction/classification beyond what the standard Plücker table mechanically gives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
