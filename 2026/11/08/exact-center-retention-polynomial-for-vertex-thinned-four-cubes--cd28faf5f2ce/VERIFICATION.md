---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For a 16-vertex Boolean four-cube, strict separation of 0 from a convex hull characterizes avoidance by subset containment in a transversal picking one vertex from each of eight antipodal pairs. All 256 oriented threshold sign patterns are explicitly excluded by signed small circuits or witnessed by integer normals in [-2,2]^4; exactly 104 are feasible. Their down-closures give avoidance a_k=(1,16,112,448,1096,1584,1312,576,104) at k=0..8 and zero for k>8. A second complete finite proof uses Carathéodory with all minimal positive supports of sizes 2,4,5 (respectively 8,24,16), then the 2^16 upward closure; probability follows by Bernoulli weighting. I independently enumerated 104 normal tope witnesses and every one of 65536 subsets, reproducing the histogram and 5249 avoiding sets; a separate exact rational kernel classification reproduced 8/0/24/16 minimal supports. Since the entire finite state space is exhausted, this is a finite proof, not a sample extrapolation. Endpoints and empty set are correctly treated.

## originality

PASS

The classic 104 three-input threshold functions and general separation/Carathéodory methods are prior knowledge, not the asserted novelty. The new exact statistic is the overlapping-subset cardinality histogram and the corresponding center-containment probability of a randomly thinned four-cube; neither the inspected threshold-logic cut classification nor published expected-volume studies states this polynomial. Priority remains provisional particularly with respect to earlier cut-complex literature.

## value

PASS

Vertex-thinned convex polytopes are a natural probabilistic geometry model and center retention is an intrinsic event. This nontrivial exact finite benchmark gives all without-replacement conditional probabilities and the Bernoulli reliability polynomial; it resolves overlapping down-closures not given by the known 104 maximal separators. Coexistence of 2-,4-,5-point minimal positive supports in dimension 4 motivates this exact natural cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
