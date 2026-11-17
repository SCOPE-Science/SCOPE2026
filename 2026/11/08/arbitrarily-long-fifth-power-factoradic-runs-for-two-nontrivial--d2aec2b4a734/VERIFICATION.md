---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For factorial-base digits a_j<=j, a_j j!-a_j^5>=0 at j>=7, the total worst j<=6 loss is -7162 and the highest j>=8 digit contributes at least 8!-8^4=36224, proving S(n)<n for n>=8!. For 1<=n<8!, fifth-power digit sum is <=sum(j^5,j=1..7)=29008, so the finite set 1..40319 traps all positive orbits. An independently coded greedy-factoradic orbit census exhausted all 40,319 states, finding exactly seven fixed points (1,34,35,308,309,1058,1059) and 2114<->3401. Independently checked all 18 complete paths from offsets 1373 and 75004 across every member of U, reaching 34 or 1058. The stated shift f_t moves factoradic positions without digit overlap; surjectivity S(sum_{j=1}^c j!)=c gives the backward lifts. This proves arbitrarily long runs for both targets, not just finite tested runs.

## originality

PASS

Carlson, Goedhart and Harris (2019/2020), Sequences of consecutive factoradic happy numbers, provides the exact fifth-power finite periodic set and a conditional theorem reducing arbitrary runs to a common translation of the periodic set. Its unconditional construction covers exponents 1 through 4; the fifth-power case with the 2114-3401 cycle is left without synchronization. The submitted 1373/75004 translations and all 18 explicit orbits solve the missing e=5 hypotheses for targets 34 and 1058, and were rechecked. No matching earlier unconditional statement found in Results semantic search or checked literature. This is an original useful certificate-supported instantiation, not an independently new lifting lemma.

## value

PASS

The fifth-power case is a natural first exponent with a nontrivial positive periodic cycle, blocking the earlier e<=4 uniform synchronization argument. Two exact and independently reproduced common translations for entire nine-point U close a concrete unsolved hypothesis and unlock arbitrarily long consecutive-run theorems in two nontrivial fixed-point basins. This is a meaningful exact finite witness with a global conclusion, despite using an existing lifting lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
