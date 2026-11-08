# Assessment of the affine incidence domination gap

## Correctness
PASS. For total domination on a point–hyperplane incidence graph, the selected points must hit *all* hyperplanes and the selected hyperplanes must cover *all* points. Brouwer–Schrijver (1978, three-page proof inspected) yields the exact point lower bound \(d(q-1)+1\) for prime-power \(q\); incidence counting yields the hyperplane lower bound \(q\). A union of coordinate axes and a full coordinate parallel class attains their sum. A paired set must have equal numbers of selected points and hyperplanes, giving the doubled blocking lower bound, and a separate coordinate-hyperplane family realizes an explicit perfect matching. Two verification programs support the field examples and exhaustion in the smallest plane cases. Scope excludes non-Desarguesian affine planes.

## Originality
PASS, with priority risk. The exact blocking number is an existing 1978 theorem and is not claimed as new. The 1998 paired-domination paper introduces the predicate and bounds, without the affine point–hyperplane formula in its accessible abstract. Héger–Nagy (2016, full text searched and relevant theorem/proof/background read) classify ordinary domination in *projective* planes; the separate affine blocking facts used there do not supply the present two strengthened vertex-domination formulas or matching realization. Adriaensen–Mattheus–Spiro (2023/24, relevant sections read) concerns *edge* domination/minimum maximal matchings, which is not equivalent to paired domination. No matching formula was found in consulted mathematical-record searches or accessible prior local claims. The full 1998 article and unindexed work remain priority risks, not proof of novelty.

## Value
PASS. In connected incidence graphs of canonical finite affine geometries, requiring guard backup pairs raises the exact minimum by \((d-1)(q-1)\), a gap growing without bound independently in the two natural parameters. The construction shows the sharp obstruction is the equal bipartition sizes demanded by a perfect matching, rather than an artifact of coarse inequalities; the covering and blocking components explain both minima. This is a family-wide structural application of a deep blocking-set theorem, not a new proof of that theorem or a routine one-graph numerical observation.

## Limitations and closest literature
The proof assumes finite-field affine geometry. It does not classify all optimizers and does not settle any general incidence graph with arbitrary incidence axioms. Full text of the 1998 definitions-and-bounds paper was not inspected; no claim of exhaustive historical coverage is made. Closest sources are Brouwer–Schrijver (1978), Haynes–Slater (1998), Héger–Nagy (2016), and Adriaensen–Mattheus–Spiro (2023/24).

Self-review: passed. Independent audit: not yet performed.
