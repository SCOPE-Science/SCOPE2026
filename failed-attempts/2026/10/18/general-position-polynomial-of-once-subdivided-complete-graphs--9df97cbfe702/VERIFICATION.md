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

In S(K_n), original–original distance is 2, original–subdivision is 1 or 3 according to incidence, and subdivision–subdivision is 2 or 4 according to edge intersection. With two originals and a subdivision vertex, incidence with either original forces a geodesic triple. With one original and two subdivision vertices, two incident edges force betweenness of the original; if just one is incident, the pair of subdivision vertices is at distance 2 or 4 and either the incident subdivision vertex or the original is between the other two, respectively. No such equality is possible when the original is disjoint from both edges. This leaves only a lone incident original–edge pair as an exception. For subdivision triples, betweenness is exactly disjoint end edges both meeting the middle one, i.e. an ordinary three-edge path, not necessarily induced. A connected graph without one is isolated, a star, or a triangle (a longer cycle or an edge attached to a triangle would supply the path; an acyclic component has diameter at most two). In the labeled component EGF, xe^(zx) counts centered stars including isolated atoms, the quadratic subtraction removes the double count on two labels, the cubic adds triangles, and e^(zx) adds the selected unused original atoms. The lone incident pair contributes n(n-1)z^2. Stars fall one edge short of their label count; equality |U|+|F|=n forces only triangle components on the complement of U, giving the stated disjoint-triple count. The natural conventions at n=0,1,2 give 1, 1+z, and 1+3z+3z^2, agreeing with the EGF; the extremal formula is claimed for n>=3. Independent Floyd-distance enumeration by legal vertex additions in branches/review_graph_crosscheck.py reproduced all coefficients for n=0 through 7, including n=7 vector (1,28,378,1890,4795,4683,1407,106). Enumeration covers every legal subset once by increasing vertex order; the all-n proof is not inferred from finite checks.

## originality

FAIL

A distinct indexed Finding gives the same full subdivision-graph polynomial in coefficient form, the same exhaustive mixed-set criterion, and both extremal formulas. The earlier line-graph enumerator already gives the edge-only component series but does not by itself cover the joint original/subdivision selection. The distinct full comparator covers that remaining part. Its later catalogue label does not settle the mathematical order, relationship of the records or historical priority.

## value

PASS

The complete set-system theorem for a natural subdivision family is more informative than one coefficient or the edge-only maximum. In particular the incidence exception changes the all-set polynomial and the component argument identifies all labeled extremizers. This distinguishes the mathematical content from a short special-case table; it does not give a case for publishing a second equivalent result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
