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

Both the frozen numbers and the narrowed carousel claim were independently verified. The 23-bit update uses eleven offsets and cutoff six, with Paley offsets generated as the nonzero squares and carousel offsets consecutive. Replay: python /workspace/audit-evidence/frozen3.py (Python with NumPy providing bitwise_count). After comparing two update computations on a 65,536-state slice, it builds each 8,388,608-state successor array in chunks and compares F^t(x) to F^(t+p)(x) simultaneously for every x. Every carousel input agrees by t=4 with p=23; since 23 is prime and only all-zero and all-one entries are fixed, every other entry has least period 23. For Paley all agree by t=10 with p=4, and the p=2 check excludes period two. The independent first-agreement method reproduces every frozen table entry, including carousel totals 4,482,196 and 3,906,412, 60,858 depth-four inputs all reaching consensus, and 47,012 wave inputs first entering at time three. It directly checks carousel mask 171551 (depth 4, eventual period 1) and 63 (least period 23); Paley masks 23807 and 15611 give depth 10 and period 4 respectively. Hence F^27=F^4 but F^26≠F^3 on the carousel. The repaired recurrence explanation is also valid: F=S^6M_5 and commuting with S of order 23 gives the same periodic configurations as M_5, via taking a 23-fold multiple of an iterate. Theorem 1 then leaves constants and two homogeneous runs of at least six sites, because on the prime ring any nontrivial shift symmetry would force constancy and four such runs would need at least 24 sites. This gives one orbit of length 23 for each block length 6 through 17. Both frozen C++ programs and outputs were inspected, not executed. Nothing establishes a census outside this rule and graph size.

## originality

PASS

This pass applies to the actual repaired finding in /workspace/repairs/3/RESULT.md, not to the frozen originality claim. The original headline claim of a new disjoint recurrent-period census fails originality: the complete Paley component is exactly covered in a distinct same-day record, and the carousel recurrent counts are a direct corollary of Nakar–Ron Theorem 1. Together the two sources imply the disjoint nontrivial period sets. The same-day exact match demonstrates coverage, not prior time, direction of dependence or misconduct. The replacement narrows the finding to the labelled carousel attraction and first-entry profile, including its sharp four-update global clock; it credits both sources for the recurrent spectrum and uses Paley only as an explicitly cited comparator. Neither those sources nor the order-19 analogue determines the narrowed quantitative claim. The replacement result, slogan and scientific metadata have been aligned with that scope; the frozen evidence and the unchanged reproducibility materials are preserved.

## value

PASS

Retained value is the labelled attraction and depth census on a canonical directed orientation, not a known recurrent classification. At the same order, threshold and out-degree as Paley, the carousel draws nearly half the inputs into oscillation while the cited Paley census draws fewer than one percent, yet the carousel has the shorter relaxation tail. The supplied table resolves how attraction accumulates, including that all final-layer inputs are consensual and all waves are reached earlier. Those are precise benchmarks a researcher comparing attraction in degree-matched threshold systems can use; no general claim about tourney order or time-to-consensus is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
