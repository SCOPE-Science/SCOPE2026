---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

At a crossing pair of cells U,V, the sets U and V are each accepted at the common world but U∩V is not. If the cells are nested, their intersection is the smaller cell and the operator is exactly the relational box for E∩F. In the converse derivation from the normal axiom in RESULT.md line 35, instantiate p=A and q=A∩D; then p→q has truth set (W\A)∪D. This supplies meet preservation by monotonicity. In the incidence graph each intersection is nested exactly when one endpoint is a leaf; connected components then have at most one nonleaf and are stars. The join blocks are precisely the sets of worlds in these components. On a j-world join block, one of the ordered partitions is indiscrete, so there are 2 Bell(j)−1 choices; the exponential formula and distinguished-label decomposition yield the stated EGF and recurrence, with c₀=1 only as an enumeration convention. An independent restricted-growth-string enumeration checked all ordered pairs up to n=6 (41,209 at n=6), finding agreement of the three criteria for each pair and 6,229 admissible pairs at six worlds. The recurrence gives 56,529 at seven. Replay: /workspace/branches/aecb0640-9c56-4dcc-8075-b0f5cbd28545/independent_census.py and independent_census_results.txt in the same directory. The finite check does not prove the all-size result. The supplied verifier was not run.

## originality

FAIL

The distinct indexed record 22fed275eb3d already gives the structural equivalences in stronger generality, the exact ordered two-agent EGF, recurrence and terms, and a join-component decomposition that is exactly the incidence-star statement. This is confirmed overlap at the level of theorem and proof, not a judgment from titles or a certification of historical priority.

## value

PASS

As mathematics, the precise frame criterion identifies when a generally non-normal epistemic operation can be replaced by an ordinary relational box on every valuation. The labelled census quantifies exactly which ordered frames permit that replacement, including cases of no global refinement between the agents. This substantive mathematical interest does not make the duplicate an original result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
