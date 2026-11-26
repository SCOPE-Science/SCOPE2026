# Independent mathematical audit

## correctness

PASS

The minimal nonfaces are precisely the original triangles and the private triangles {u,v,w_uv}; a private vertex has only its two endpoints as neighbors. In the triangle-free case the private circuits have unique markers, and no isolated vertices ensures they cover all n+m vertices, so Ehrenborg–Hetyei Proposition 4.3 gives simple-homotopy type S^(n−1). For a base triangle abc, neither endpoint of the contraction edge {w_ab,w_ac} shares a minimal nonface with the other. This is the cited link condition; explicitly a face disjoint from the pair can be extended by both whenever it can be extended by each separately. After contraction, a face could fail to extend to the new vertex only if it contained both {a,b} and {a,c}, which is impossible since it would contain the original forbidden triangle. The quotient is a cone and collapses, proving the claimed simple-homotopy equivalence, not a collapse-only statement for the original complex. For m≥2 the Alexander dual cover by complements of the private circuits has nerve the boundary simplex on E, naturally under automorphisms; an omitted private edge leaves its private vertex in the intersection, whereas all circuits cover the ground set. The complementary-face chain pairing has the ambient determinant twist, so the edge sign cancels and the original vertex sign remains. An independent trace argument verifies the sign: each g-invariant face contributes minus (−1) to the power of its number of g-cycles, including the empty face. Fix its original-vertex subset U. All private vertices with edges not contained in U are independently available in the triangle-free case, and choosing whether to include each available g-orbit cancels the sum unless no such orbit exists. The only uncancelled term is U=V by the no-isolated-vertices hypothesis; the reduced Lefschetz number is (−1)^(1+#vertex cycles). Since only degree n−1 survives and its group is infinite cyclic, the integral action is exactly the sign of g on V. For m=1 the class is the triangular boundary for K_2 and its orientation check is direct. I inspected verify.py and VERIFY_OUTPUT.txt without executing the script; the ten mod-two Betti checks and fourteen integral signed traces are finite checks, not evidence of all-graph homology or simple-homotopy type on their own.

## originality

PASS

The pointed-complex sphere branch is explicitly credited, and the point branch is a short application of existing contraction machinery once the two private vertices above a base triangle are selected. The supported distinct content is the placement of that contraction in the graph dichotomy and especially the determination of the integral character in terms of original vertices alone. The general nonequivariant sphere and contraction theorems do not give the character. The natural duality and nerve tools are standard; the character still requires identifying the equivariant nerve and the ambient/private sign cancellation, a comparison particular to the decomposition used here. No distinct matching result was found among the inspected neighboring statements.

## value

PASS

The result gives a uniform detection rule relating triangles of the original graph to the simple-homotopy type after augmentation. More distinctly, it tells which automorphisms preserve orientation integrally, a datum invisible to the earlier nonequivariant sphere theorem and ordinary Betti numbers. This is useful for comparing graph symmetries and their induced actions without enumerating faces or generators.

The dated certificate retains the supplied scientific assessment, sources and limitations.
