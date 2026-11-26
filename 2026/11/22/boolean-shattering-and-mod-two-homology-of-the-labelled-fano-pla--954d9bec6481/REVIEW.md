# Independent mathematical audit

## correctness

PASS

The membership-query ground set is the 35 triples; the concepts are the 30 labelled line sets. The binary projective plane and its order-168 automorphism group give 30 concepts. Incidence counts and relabelling give six planes per triple and two per compatible pair (intersection exactly one). Of the 945 pairwise compatible three-supports, 105 are concurrent and 840 triangular; each plane contains 7 and 28 respectively. Transitivity gives two completions for every concurrent support and one for each triangle. Concurrent supports miss a trace with exactly two positives, whereas triangular supports have trace counts 17 for none, 3 per singleton, and 1 per pair and for the full set. A shattered four-support would require both the unique plane containing a specified triangle and another plane containing that triangle but missing the fourth triple, a contradiction. All compatible edges extend to a triangle, and the six-used-label triangles form one orbit. An online depth-four tree would need eight distinct planes in the positive branch of the first query, but each query belongs to six; a shattered triangle realizes depth three. Independently constructing the edge and triangular-face boundary over F₂ yields ranks 34 and 281, and hence reduced Betti numbers 0, 0, 559 in degrees 0, 1, 2 and zero elsewhere. The rank replay relies on the face classification proved above, not on an independent trace enumeration: /workspace/branches/53aab6c5-0b4a-4030-b048-01f2c6cc7cc4/rank_fano_repro.py, with rank_fano_repro.out in the same directory. Inspected both frozen checkers without executing them. No integral homology or homotopy equivalence is inferred.

## originality

PASS

The thirty labelled planes, their one-line frequencies, and relevant incidence geometry are prior. The supported distinct result is the Fano membership shatter complex, in particular the deletion of precisely the concurrent triangles from the compatible-triple graph in dimension two and the resulting mod-two homology. The inspected table gives the concepts, not that invariant. Neither the most relevant general shattering framework nor the analogous graph-based catalogue theorem provides the Fano boundary rank.

## value

PASS

The labelled projective plane gives a canonical design class, with exact query complexity and a natural shatter complex. The criterion distinguishes the otherwise indistinguishable compatible triangles by incidence type, and the boundary rank gives the first mod-two cycle structure not specified by the face vector alone. The result is useful as an exact small design benchmark independently of any larger Steiner-system claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
