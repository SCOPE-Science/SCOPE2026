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

A unit flow in the acyclic caracol graph is a convex combination of its uniquely indexed source–sink path indicators [i,j]. Their squared ambient distance is the interval symmetric-difference cardinality plus 2 for each differing source and sink endpoint. Splitting all unordered pairs by 2, 3, or 4 distinct endpoints proves the entire O(n)-term histogram. Maximization isolates exactly two families of endpoint-overlap diametral pairs, diameter² n+2 for n>=4 (n=3 gives 4). Mean follows by finite polynomial derivative. Quantizing sorted i.i.d. uniforms and applying Dirichlet(1,1,1,1,1) spacings plus explicit total-variation bounds proves Beta(2,3) with O(1/n) Kolmogorov error; this is not inferred from samples. Independent exact all-path pair histograms and diametral loci agree for n=3,4,6,9,12.

## originality

PASS

Jang–Kim, Benedetti et al. treat caracol netflow definitions and volume/Ehrhart-like enumeration, not unit-flow vertex-pair ambient Euclidean distances. The inspected transitive-complete-DAG flow theorem gives only a different graph diameter and maximizers. Affine equivalence to other flow/order polytopes is not metric equivalence. Classical beta spacings are credited as prior and do not alone determine the discrete exact histogram or sharp diameter.

## value

PASS

The caracol flow family is an established natural network-flow polytope; its complete exact ambient vertex-pair Euclidean histogram compresses quartically many pairs to O(n) summands, determines exact diameter and maximizers, and couples to a sharp beta law. Affine volume knowledge does not supply this metric.

The dated certificate retains the supplied scientific assessment, sources and limitations.
