# Scientific assessment

## Correctness — PASS

The definitions fix directed incoming balls, include the center, and retain indexed binary vertices. The lower bound is proved by the shared-predecessor property of each two-vertex prefix class. The attained upper bounds are given by complete hexadecimal selector functions, not opaque random seeds: every selected vertex is obtained by an explicit integer-bit formula. Two independent procedures verify nonempty, pairwise different signatures over all 128 and 512 graph vertices, respectively. The Python procedure uses a direct prefix formula; the C++ procedure constructs shift-and-append arcs and reverse BFS. Both completed and agreed on cardinalities 64 and 256. The claim is finite at these two graph sizes; no infinite generalization is alleged.

## Originality — PASS (historical priority qualified)

The closest primary source is Boutin, Horan Goliber, and Pelto, arXiv:1412.5842, first posted 2014-12-18. Its full text supplies the universal lower bound, optimal constructions at lengths at least twice the radius, and a nonoptimal boundary construction; the boundary cases \((7,4)\) and \((9,5)\) are not solved there. Searches for exact directed boundary parameters, alternative in-ball formulations, and matching database results did not reveal a covering theorem or table. An earlier finite result at \((5,3)\) is not asserted here. Horan's arXiv:1508.00403 instead treats undirected adjacency. Residual risk: unindexed subsequent reports, theses or unpublished computations might contain these two values; this is not an independent priority certification.

## Value — PASS

The boundary \(n=2t-1\) is singled out in the primary paper as the sharp identifiability threshold and an open optimum-size regime. The two next finite radii after the smaller previously investigated case correspond to 128- and 512-vertex sensor-location problems. Compared with the known boundary construction of respective sizes \(80\) and \(288\), the attaining codebooks save \(16\) and \(32\) sensors. Showing that the general lower bound is attained in both cases narrows a motivated gap, supplies reproducible exact constructions, and provides concrete evidence for—but not proof of—a broader pattern. The claim is neither a restatement of the existing lower bound nor a mere reparameterization of a known family.

## Scope and limitations

The result does not cover other radii, general alphabets, outgoing-ball identification or failed sensors. Only self-review was performed, without independent review.

Self-review: passed. Independent audit: not yet performed.
