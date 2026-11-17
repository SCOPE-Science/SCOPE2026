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

Ordered pair-collision de Bruijn graph has 12 off-diagonal states. Sharing a two-bit pair propagates backwards by Rule 30 left-permutivity and would force the two inputs equal. Exact finite 12-state graph enumeration isolates 8 vertices on closed walks, paired under predecessor swapping. The four-state quotient has seven labeled signed edges with orientation-flip bits; an ordered closed lift exists iff the total flip parity is even. Each excursion from A returns with output 11 0^m b and flip parity 1_{b=0}; the C zero loop gives only 0^n. This is all-length finite automaton proof, not inference from checking n<=16.

## originality

PASS

Best-of-knowledge originality of the exact final claim (not of elementary starting tools). The all-length predecessor multiplicity histogram for Rule 30 covers counts by multiplicity, but does not classify which individual indexed words are ambiguous. A fixed-point semigroup algorithm for arbitrary words decides the event by computation without stating the signed-block intrinsic language. An all-length histogram, even together with uniqueness of the triple-predecessor word, cannot select individual outputs from each multiplicity class. The signed quotient derivation is a stronger different type of conclusion, not an immediate restatement.

## value

PASS

Exact intrinsic language recognition of individual ambiguous cyclic Rule-30 output words is independently useful beyond aggregate precursor frequencies; the global parity obstruction is a nonlocal structural condition and yields a small recognition automaton.

The dated certificate retains the supplied scientific assessment, sources and limitations.
