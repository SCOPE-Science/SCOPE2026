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

The posted NetworkX generator edge list agrees with the 24 edges in the supplied verify.py. For the ordinary cut complex, σ fails to be in the dual exactly when V\σ is a face of Δ_4, i.e. when σ contains a disconnected four-set. Independently checked all quadruples by testing proper bipartitions, then listed every face of the full uncollapsed dual. Replay: python /workspace/audit-evidence/frozen4.py. This finds 282 disconnected quadruples and dual face vector (12,66,220,213,48), with no higher face. On the full signed boundaries, integer unit row/column splitting gives Smith forms with only unit nonzero entries and ranks (11,55,157,48); the code tests that the residual matrix after the unit pivots vanishes and verifies consecutive compositions are zero. Thus each boundary image is primitive in its target chain group; H_i embeds in the resulting torsion-free quotient of that chain group. Ranks in degrees 2 and 3 are 220−55−157=8 and 213−157−48=8, and other reduced ranks are zero. The frozen collapse-based script was inspected, not executed: its unique immediate coface and maximality tests are sufficient for the reported elementary-collapse approach, and the independent full-dual integer computation bypasses it. Integral UCT introduces no Ext term, so Alexander duality on twelve vertices places the two free groups in original degrees 9−2=7 and 9−3=6. All 282 original facets have size eight; H̃_6≠0 rules out pure shellability. This is not an identification of homotopy type or a map between cut parameters.

## originality

PASS

The supported distinct result is the complete integral ordinary four-cut homology on the standard Chvátal graph, notably two adjacent free groups of rank eight and no torsion. The same-graph three-cut Moore space, related four-cut computations, and conditional general four-cut theorems do not imply this invariant. In particular, the most relevant general result requires a complete 6-skeleton, whereas the computed dual has 48 faces of size five whose complements give absent size-seven faces. The comparison uses exact graph, parameter, and ordinary/total distinctions, not inference from absent keywords.

## value

PASS

The standard Chvátal graph is already a test object for torsion in ordinary cut complexes. Its next cut parameter is a natural point of comparison, is outside the available girth theorem, and gives a concrete benchmark with two nonzero free integral homology degrees rather than the nearby sphere-wedge pattern or three-cut torsion. The exact integer computation also settles nonshellability; this is a meaningful invariant for this named graph, not a proposed persistence trend.

The dated certificate retains the supplied scientific assessment, sources and limitations.
