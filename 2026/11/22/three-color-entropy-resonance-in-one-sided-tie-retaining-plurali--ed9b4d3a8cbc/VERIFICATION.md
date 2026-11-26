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

Audited the forward three-ballot rule directly: only agreement of the two successors can change the incumbent. Proper words are fixed and thick words shift. For any original maximal run of length at least two, its predecessor and its first length-minus-one sites form a monochromatic block of the original length after the update. Its last site either stays attached or changes to the next long run's color and belongs to that run's updated block. Thus no original long-run site can become a singleton, and a singleton immediately preceding a long run is certainly removed. A mixed word has such a boundary and at most n−2 singleton sites, proving strict descent and recurrence only in the two classes. In the two-zero alternating-tail witness the shrinking tail remains alternating and nonzero and the only advancing block eats exactly one site each time, including the n=3 case. The thick-word pair transfer factors through the diagonal and row-sum coordinates as (u,v)→(v,v+(J−I)u): the symmetric color sector yields z²−z−(q−1), the other sectors z²−z+1. This and the standard proper-coloring trace give the stated formulas, equality of growth rates only at q=3, and the limits. Uniform states belong to the thick class and are fixed; the total fixed count is P+q, not P. Least periods of thick words are spatial; nonconstant primitive repeat blocks must have at least two runs of length at least two, and 00 followed by d−2 ones realizes every d≥4. Divisor inversion uses S(q,1)=S(q,2)=q, consistent with the transfer formula. Fresh replay /workspace/branches/replay_1.py enumerated the full functional graphs for q=3, n=3–8 and q=4, n=3–6 using direct ballot tallies. It checked class counts, entry times, shifts, and period-divisor counts (e.g. q=3,n=8: 258 proper, 255 thick, cutoff 6, and 12/240 thick states of least periods 4/8). This finite replay is corroboration, not the all-size proof.

## originality

PASS

The distinct result is the joint one-sided multicolor recurrent classification, sharp entry clock and proper/thick entropy equality. The proper-cycle chromatic count and transfer-matrix method are standard ingredients, not separately novel.

## value

PASS

The finite directed voting rule has a genuine three-way tie and a natural all-initial-state transient question. It is resolved by an optimal clock and complete attractor description including arbitrarily long traveling periods. The coexistence of two structurally different recurrent families with exactly equal exponential growth at three colors, but not four or more, is more than a static cycle-coloring exercise. The result concerns recurrence, not the attraction-basin proportions or a stochastic rule.

The dated certificate retains the supplied scientific assessment, sources and limitations.
