---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For the Euclidean root lattice A4 in the zero-sum five-space, the Voronoi cell is exactly the coordinate-range<=1 polytope by root inequalities and z_i^2>=|z_i| for integral zero-sum lattice points. Its vertices have k high coordinates and squared norm k(5-k)/5, so mu^2=6/5. For every directed Hamilton path root frame, each permutation simplex has a uniform binary-coordinate translation and a containing sphere of squared radius k(5-k)/5<=6/5. The published general mu<=kappa bound supplies equality. Conversely any optimal frame has every subset sum squared norm<=4 (integral even squared norm and diameter<=2 sqrt(6/5)); no coordinate row can repeat positive or negative incidence. A squared-norm-four vector forces either >10 entries or dependent columns, so all four are roots; indegree/outdegree<=1 and connected rank four yield exactly an oriented five-vertex Hamilton path, 5!=120 full lattice bases. Independent exact integer enumeration of 50 short vectors and 230300 four-subsets produced exactly these 120, and 2880 packet witness checks in original verifier were inspected. Enumeration corroborates the infinite geometric proof; not its substitute.

## originality

PASS

PASS qualified: Xue defines original packet invariant and proves mu<=kappa. A related same-date published A_n theorem for n>=5 proves the common simple-root packet optimality and its argument extends to n=4, hence the numerical kappa(A4)=mu and existence of an optimal frame alone are already implied. It explicitly does not classify all minimizers. The full necessity and rigidity theorem, precisely 120 oriented-Hamilton-path frames among arbitrary independent lattice frames, is the noncovered contribution.

## value

PASS

PASS: classification of every optimal packet frame is a natural structural lattice-geometry question, not a recomputed A4 covering radius. Its forced unimodularity and oriented-path rigidity distinguish optimal common-frame triangulations in a nontrivial four-dimensional root lattice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
