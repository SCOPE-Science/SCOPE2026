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

Classified forests by final hub partition: three separate hubs admit no branching peripheral; a pair block has one degree-two branch; the full block needs either one triple or two different pair masks. Each branch consumes one or two of the only two available hub mergers. In the pair-block case each ordinary peripheral has component attachment weights 2v and v, so two ordinary marked terminals have connected weight 5v²; in the full-block case every nonisolated terminal is connected to its partner if that partner is also nonisolated. Unmarked nonbranching vertices have factor A=1+3v. These checks confirm the census mechanism, and a fresh exact symbolic census reproduced Z=A^(m+2)P, Z_X=3v²A^m Q and Z_XY=3v⁴A^(m−2)S, including m=0,1 where impossible exceptions have zero multiplicity. Terminal exchangeability gives Z_Y=Z_X. Expansion verifies SP−3Q²=4vR with R coefficientwise nonnegative and R(0,0)=4. The denominator is positive at every allowed parameter. Full independent edge-subset checks give 1,856, 9,984 and 51,712 forests at v=1 for n=4,5,6, respectively; the all-n conclusion rests on the symbolic classification, not those finite checks.

## originality

PASS

Best-of-knowledge pass for the exact correlation and strict all-fugacity three-hub theorem. Credit known high-fugacity arboreal-gas connectivity results and the general conjectural framework. The closest indexed all-fugacity peripheral-pair result is on two hubs; the known three-hub edge correlations concern a different observable.

## value

PASS

This proves an all-size all-fugacity case of a natural four-terminal question on a family with overlapping cycles, where edge correlation results do not settle connectivity. The nonnegative coefficient certificate demonstrates strictness in the full parameter range, including regimes inaccessible to a high-fugacity argument. The fixed hub count makes it tractable without reducing it to an isolated numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
