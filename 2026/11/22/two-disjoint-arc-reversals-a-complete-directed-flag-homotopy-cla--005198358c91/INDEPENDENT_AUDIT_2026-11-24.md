# Independent mathematical audit

## correctness

PASS

A triple contains at most one reversed arc; checking its orientations shows it cycles only if its outer arc was reversed. A tournament is transitive iff all triples are acyclic, so these are exactly the minimal nonfaces. Any label outside [a,d] gives a cone. With a=0 and d=n−1, separated arcs give either a middle-gap cone or a join of the two single-reversal complexes. Such a complex is a simplex for adjacent endpoints and otherwise consists of two simplices along their interior simplex plus the edge between endpoints, hence is a circle. The separated join is S^3 precisely if c=b+1 and both interiors are nonempty. In the nested case the outer endpoints suspend the inner complex and an extra edge attaches between the suspension vertices. This is S^1 wedged with that suspension because the suspension is path-connected; the inner complex is a circle exactly for b=a+1, c=d−1, c−b>=2, and otherwise contractible. In the crossing case a label in an outer gap dominates the appropriate interior endpoint b or c: adding that label could only make a forbidden triple whose other two vertices would already forbid the original face containing the endpoint. After its deletion the opposite exterior label is a cone vertex. Multiple central labels have identical obstructions and strongly collapse to one. With no gap the four-label core is two triangles sharing an edge plus a further edge, giving S^1. With a central label the five-label core has six triangles and no tetrahedra; the first six listed collapses remove the triangles leaving the path 1–0–3–2–4, and the last four remove its leaves to vertex 2. This proves the integral homotopy classification, not just an equality of Betti numbers. Independent direct orientations matched the forbidden-triple rule in all 756 cases for n=4 through 9 and verified the exact 21-face collapse certificate.

## originality

PASS

Pass is for the complete all-order criterion for arbitrary placements of two disjoint reversals, not for the wedge subfamily alone or for the previously computed low-order cases. A distinct same-day result genuinely covers the nested S^1 wedge S^2 subfamily as r=2 of a stronger family and should be credited for that coverage; their relative priority is unknown. The broader result does not classify separated, crossing or other nested configurations. Bibliographic correction: Govc–Levi–Smith introduce tournaplexes, but their p. 2 credits Reimann et al. with introducing the directed flag complex; the frozen related-work sentence should not be taken to establish that attribution.

## value

PASS

This classifies the effect of two local perturbations of a transitive tournament by three geometric placements and their exact gaps. It shows when the same number of reversals yields a cone or creates distinct sphere dimensions, with arbitrary numbers of unused labels and actual homotopy types. The uniform structural reduction, including the crossing contractibility dichotomy, is useful beyond the known wedge subfamily and existing finite tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
