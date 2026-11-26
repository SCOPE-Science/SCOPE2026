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

A swap of adjacent positions changes just the swapped pair in the value inversion graph. The graph of a layered permutation is a union of cliques on consecutive value intervals. Deleting an edge of a clique of order at least three makes an induced three-vertex path; adding a cross-clique edge also does so unless both endpoints are singleton cliques. These singleton layers must be consecutive because the entries are position-adjacent. Conversely those two moves preserve layering, so the legal changes are exactly 2↔1+1. The positions of long layers are fixed and the other gaps are independent monomer–dimer tilings. Their dimer starts are the no-adjacent-ones strings of length max(ℓ−1,0). Delete source-only dimers, then add target-only ones to realize Hamming distance; coordinatewise majority is admissible and is the unique Hamming median. Complementary alternating strings realize the factor diameter, including zero. Counting tilings gives F_{ℓ+1}, also F₁=1 in the empty gap. A signature is a gap followed by a sequence of (long layer, gap) pairs. Substitution of gap series (1−z)⁻¹ and 1+z for all signatures and for singleton components, respectively, with long-layer series z³/(1−z), gives both rational functions. Edges are counted by their dimer endpoint: a crossing at either end admits 2^{n−3} remaining compositions, at each of n−3 interior starts 2^{n−4}; n=1,2 separately. For all nonempty long-layer signatures the total free length is at most n−3; concatenation injects tuples of gap tilings into tilings of that total length, strictly fewer than F_{n+1}. The all-short component is the unique largest and its relative size decays as (φ/2)^n up to a constant, where φ is the golden ratio. Read the frozen verifier and output, not executed. Replay: python3 -B /workspace/review_evidence/independent_checks.py 2, enumerating from forbidden triples rather than layer compositions through n=7, testing all component distances (via inversion-set difference), all triples for unique medians, edge counts and both count sequences. This is finite evidence only.

## originality

PASS

The distinct content is the exact layered trace inside the swap graph and its global layered component, isolation and edge enumerators. The layered characterization, Fibonacci-cube facts, and the ambient involution component structure are not novelty grounds; the same-day involution result gives strong partial coverage, including the ambient distance rule and identity component, but does not give the layered trace or its enumerators.

## value

PASS

The question of which local edits preserve one-pass sortability has a natural uniform state space. The rigid layers and complete description of the feasible trace allow exact reachable-state counts and shortest routing, and the two exact global enumerators describe how fragmented this class is. These are not given by the ambient involution counts or the size of the sortable class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
