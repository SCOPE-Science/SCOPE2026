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

Reassessed /workspace/repairs/4/RESULT.md. The frozen coefficient statement needed to exclude the constant term: a_0=0 and a_1=L>0 even on the one-vertex tree. The repaired text states the tail formula and monotonicity for j>=1, with the separate constant term. Complements of closed sets are exactly omissions in which each omitted nonleaf has an omitted child. Starting at any omitted u produces a downward path to a leaf; conversely every such path is a minimal omission containing u, since its consecutive children are forced. Proper meet-irreducibles in a finite closure system are precisely maximal closed sets omitting a point: maximal omission implies irreducibility by intersection, and a proper irreducible has a unique cover whose added points occur in every strict superset. Thus distinct ancestor-leaf paths give all proper meet-irreducibles without duplicates. Each leaf supplies exactly one path of each positive size through depth+1; coefficient differences recover the depth histogram. Counting by starting vertex gives at least one path from every vertex, strictly more from any branching vertex. At fixed n and L every leaf depth is at most n-L, and simultaneous equality forces every internal vertex onto every root-to-leaf path, exactly a broom. Each feasible fixed-(n,L) broom exists; the integer quadratic L*(n-L+1) then gives the stated global maximum, including the constrained n=2 case. For n=1 the empty set is the only proper meet-irreducible. The frozen checker and record were read, not executed; they are finite corroboration and unnecessary for this proof.

## originality

PASS

The repaired Finding is the sharp fixed-total-size (and fixed-leaf-count) model-count bound and its equality cases. The original structural emphasis did not give sufficient credit to concrete implications of earlier, broader Horn results. Acyclic splitting by deepest leaves yields the path complements by induction, and the deficit polynomial is then their length count. The repair explicitly treats both as structural input and corollaries, not the unsupported novelty claim. The checked Horn results do not optimize over rooted trees of a specified total size; Fischer's Sackin extremum fixes leaf count and excludes nonroot unary internal vertices. In the checked sources the extremal model-count remainder is not covered.

## value

PASS

The repaired extremum gives the exact worst-case cardinality of the characteristic representation for a canonical acyclic Horn family, including the shapes that blow up the number of models from linear to quadratic. Knowing that an enumeration algorithm is efficient does not give this output bound or identify the maximizing inputs. The fixed-leaf count bound identifies the structural cause of the output growth. The earlier structural specialization and spectrum are useful context but are not counted as additional novel contributions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
