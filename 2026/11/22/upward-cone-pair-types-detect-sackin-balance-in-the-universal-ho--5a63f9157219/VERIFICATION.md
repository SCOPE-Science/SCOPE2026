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

For a cone point x the nonempty set B_x of old leaves below x is a clade: if a,b are below x, an old leaf c in their least clade but not below x would be incomparable with x and witness C(c,ab), against the old rooted triple. Conversely apply the universal binary-tree extension Lemma 3.1 with U the clade and W its complement (the required branching triples hold by rooted-tree clade separation). With two points on one clade, apply the lemma a second time with the first point as an upper constraint; exactly two strict orders are possible. For distinct clades the order is forced by nesting or disjointness. To rule out hidden C-splitting, give each new name its below-leaf clade and each old name its singleton. For incomparable a,b, their common upper bounds are exactly the common upper bounds of any chosen leaf representatives a',b': a bound of the latter shares a lower leaf with each point, so is comparable with each, and being strictly below either would place the other representative in its clade. For the third point z, if its clade intersects either of those of a,b, no such bound is incomparable with z. Otherwise incomparability of the bound with z is equivalent to incomparability with any representative z': comparability with z but not z' would require the bound below z and hence both a',b' below z, a contradiction. Thus all branching triples are fixed by the proposed data. Homogeneity then gives exactly one complete type per distinct ordered clade pair and two per equal-clade pair. Counting ancestor-or-equal positions gives H=2S+1 by the two-subtree recurrence, including H=1 at n=1. The first shape-dependent example n=4 and both bounds and equality cases follow. The upper extremum also follows by induction with deficit (a−1)(b−1) for split a+b; the lower extremum uses the shallow-leaf/deepest-cherry exchange to force depths differing by at most one, then Kraft equality. Frozen checker and its recorded 48-tree output were inspected, not executed; they cover the constructed diagrams, not general realization or exhaustiveness.

## originality

PASS

Best of current knowledge the distinct contribution is the complete upward-cone pair spectrum and the way its relation channels recover the named antichain's Sackin index while the total does not vary. The homogeneous expansion, its finite extension lemma and the Sackin extremal results are known inputs. The derived numerical extremal formulas are not separate originality claims.

## value

PASS

The named antichain and its strict upward cone are natural configurations in the homogeneous semilinear order. The classification shows exactly which classical tree statistic a binary logical observable retains even when both unary and total pair counts forget the shape. It gives a concrete extrapolatable invariant, a first distinguishing size of four, and a balance-dependent comparable-type fraction, not just a small census or a new label for a known tree-index bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
