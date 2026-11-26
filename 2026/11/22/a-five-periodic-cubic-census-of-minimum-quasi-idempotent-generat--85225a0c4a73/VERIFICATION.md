---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Rank cannot increase under composition. A rank-(n−1) map e_(i,j) has the collapsed pair {i,i+1} and omitted j; its monotone nonfixed run has maximal time to reach a fixed point i+1−j for j≤i, or j−i for j≥i+1. Strict quasi-idempotence is exactly maximal time 2, giving the two stated candidates. Every lower-rank map factors through a top-rank map collapsing an adjacent repeated value: delete one occurrence from its value list and insert a missing value into the shortened list in sorted order to obtain the second factor of rank one higher. Iterate to generate all lower ranks. For top-rank products, appending e_(i,j) preserves rank iff the current omitted index belongs to {i,i+1}, and then changes the omitted index to j. Rows and columns must be covered. A prefix cut k without a right crossing traps the initial generators of row k−1 in the prefix (k≥2, and k=1 is forced by row 1); without a left crossing row k+1 is trapped on the right (with the other endpoint forced). Conversely, in the directed graph on omitted indices a closed sink component cannot have an interior hole: if a belongs and a+1 does not, the right crossing at a forces r_a and a+2 in the component (r_(a−1) would go from a to a+1). But then neither possible way to cover column a+1 is allowed: r_(a−1) and l_(a+2) would send a component vertex to a+1. A proper interval is not closed either, since a crossing of its adjacent cut includes an arc out of its boundary vertex. The graph is strongly connected, so all omitted indices are reachable for each covered first row. Column coverage and consecutive cut tests give precisely the three stated transition predicates, initial r_1=1 and terminal l_(n−1)=1, r_(n−3)=r_(n−2)=1. Direct expansion of all five-step transition words verified the symbolic anchor update and all terminal polynomials, including their costs; the eight cost offsets are constant apart from 6j, so no hidden j-dependent ties are possible. A fresh direct composition check through n=8 agreed with the graph criterion and yielded (minimum size, count)=(4,1),(6,1),(6,1),(8,3),(9,2). Replay: /workspace/branches/semigroup_replay.py. The all-n proof is the graph equivalence and polynomial induction, not the small-n enumeration. Lower-rank generators cannot supplement a minimum set because its top-rank part already generates.

## originality

PASS

The corank-one characterization, generation criteria, and optimum cardinality are predecessors, not new findings here. The earlier rank alone does not count how many choices attain that rank. The weighted transfer calculation determines those ties in each residue, including an infinite uniqueness class. Bounded comparison found no earlier enumeration that entails that result.

## value

PASS

For the natural restricted rank of a classical transformation semigroup, the number of optimal generating systems is a useful equality-case invariant, not determined by the rank. The exact result distinguishes one infinite family with a unique optimizer from other residues with linear, quadratic, or cubic multiplicity. The proof simultaneously yields a practical exact model for checking equality cases without trying all transformation subsets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
