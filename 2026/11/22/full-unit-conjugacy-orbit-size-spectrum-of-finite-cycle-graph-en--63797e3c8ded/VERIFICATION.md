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

A strict endomorphism gives a unique signed closed walk. Winding ±1 gives exactly the units; winding zero forces a balanced word and a reversal, hence a repeated image. A commuting rotation of nonzero step k forces period gcd(n,k); the sum per period is zero for a balanced word, contradicting f(i+k)=f(i)+k. A commuting reflection pairs steps by i↦c−1−i and imposes 2f(0)=c−sum_{i=0}^{c−1} ε_i modulo 2m. For c=0 there are m pairs and balance needs m even. For c=1 two fixed steps require paired sum ±1 if m is even, or 0 if m is odd; the initial congruence has two solutions. This reproduces all three parity counts and the unit contribution of four. Two distinct reflections cannot stabilize a singular map, so the reflection incidence sum 2nH_m counts distinct singular maps and gives precisely the two stated orbit sizes. The dihedral unit classes give the remaining terms (including the merged y² coefficient at n=4); Stirling yields both asymptotics. An independent JavaScript enumeration extended vertex-image tuples by adjacent images and retained those whose last image was adjacent to the first. For each actual map and unit it tested f(u(i))=u(f(i)) and formed conjugates via f_u(u(i))=u(f(i)). For n=4,6,8,10,12,14,16 the resulting singular size-(n,2n) orbit counts were (4,1),(4,8),(12,29),(12,120),(40,442),(40,1696),(140,6365), and every unit centralizer agreed. Odd n=5,7,9,11 gave only units and the stated odd orbit histogram. This finite check corroborates the universal proof, not the reverse.

## originality

PASS

The supported distinct result is the full simultaneous conjugation census on all strict endomorphisms and the resulting unit centralizer formulas. The labeled total and standard dihedral part are not new. A distinct same-day idempotent census is a genuine overlap on a proper subset; no order of priority is inferred from its date.

## value

PASS

Conjugation identifies relabelings of an endomorphism by a single graph symmetry, a natural equivalence in a unit-bearing monoid. The two-size classification on all singular maps quantifies precisely how often any polygon symmetry persists, with an exact reflection-axis distinction and an exponentially small exceptional proportion. This supplies stabilizer information absent from labeled totals and rank or kernel counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
