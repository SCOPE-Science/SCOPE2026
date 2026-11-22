---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The specified simplicial vertices are all 2n+2 directed arcs of an n-cycle with one bidirected leaf (n=3..6); masks are faces iff every vertex has indegree/outdegree <=1 and no directed cycle. Independently generated all nonempty face sets (26,66,162,394), applied the four exact frozen certificate pivot permutations, reconstructed 11,31,78,195 face-poset pairs, checked acyclicity by independently oriented Hasse DAG topological sorting, and computed each integer Morse differential by recursively eliminating matched lower cells with signed +-1 simplex incidences. Every differential vanished and the critical multiplicities were {0:1,1:3}, {0:1,1:1,2:2}, {0:1,2:3,3:2}, {0:1,3:1,4:2}. The CW attaching maps vanish because pi_1(S1)=Z at n4, pi_2(wedge 3 S2)=Z^3 at n5 and pi_3(S3)=Z at n6; n3 has only 0- and 1-cells. This establishes integral homotopy wedges, not just ranks. No n>=7 or periodicity claim.

## originality

PASS

Same-object prior literature studies the unmodified bidirected polygon and oriented T-operation graph, whereas adding exactly one *bidirected* pendant pair at a cyclic vertex changes the arc set and constrained paths. The 2026 original Caputi–Collari–Smith Theorems 2.8/2.10 are bare-polygon connectivity/homology, and Proposition 2.3's W2 T-operation requires a source/sink and is not the one-leaf cycle edit. Resultary bare-cycle integral wedges also do not cover the leafed digraph. No exact four-case leafed table found; best-of-knowledge O with archival risk.

## value

PASS

A natural, minimal bidirected leaf perturbation of a thoroughly studied cyclic multipath object changes exact integral homotopy types. The four first representatives of all n mod 4 residue classes expose mixed-dimensional sphere wedges, with a certified homotopy rather than mere homology classification. Finite classification is a motivated boundary benchmark for general leaf-attachment theorems; it is not asserted as the unbounded periodic law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
