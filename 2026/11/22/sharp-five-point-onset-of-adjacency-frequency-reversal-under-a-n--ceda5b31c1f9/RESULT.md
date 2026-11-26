# Exact star-family reversal for edge insertion in Henson pair-type counts

## Finding

For \(m\geq 1\), let \(G_m=K_{1,m-1}\sqcup K_1\) with a designated star centre (also for the one-vertex star), and let \(G_m^+=K_{1,m}\) be obtained by joining the centre to the isolated vertex. Treat the old vertices in each graph as individually named parameters in the universal homogeneous triangle-free graph. Under the uniform distribution on complete types of ordered pairs of distinct new vertices, insertion strictly increases the fraction of adjacent types for \(m=1,2,3\) and strictly decreases it for every \(m\ge4\).

## Assumptions and scope

The inserted edge is specifically from the star centre to the isolate. The probability is over complete types of two distinct points outside the named base, not a distribution on vertices. There is no classification of general large graph insertions here.

## Proof

If \(I(G)\) counts independent subsets of the base, and \(B(G)\) counts ordered disjoint pairs of them, the adjacency-type fraction is \(B/(I^2+B)\). Indeed, each new vertex has an independent base neighbourhood; the two neighbourhoods are unrestricted relative to each other when the new pair is nonadjacent, and must be disjoint when it is adjacent to avoid triangles. These are sufficient conditions by finite extension, and homogeneity makes each full diagram a unique complete type. Hence the sign of the change is the sign of the difference in \(B/I^2\).

For a star with \(k\) leaves, either the centre is absent from an independent set (\(2^k\) leaf choices) or it is alone in that set. For a pair of disjoint independent sets, when the centre is unselected there are three states for each leaf; when the centre is in one of the two sets, there are two states for each leaf. An additional isolated vertex multiplies \(I\) by two and \(B\) by three. Setting \(x=2^m\), \(y=3^m\) thus gives
\[
(I(G_m), B(G_m))=(x+2,y+3x),\qquad
(I(G_m^+),B(G_m^+))=(x+1,y+2x).
\]
With positive denominators the desired sign is that of
\[
(y+2x)(x+2)^2-(y+3x)(x+1)^2
=y(2x+3)+x(-x^2+2x+5).
\]
For \(m=1,2,3\) the expression is \(31,87,169\), respectively. For \(m\ge4\), its sign is the sign of \(F_m-4^m\), where \(F_m=2\cdot 3^m+3(3/2)^m+2^{m+1}+5\). At \(m=4\), \(F_4=214+3/16<256\). Every positive summand of \(F_m\) grows by at most a factor of three in one step, whereas \(4^m\) grows by a factor of four. Induction gives strict negativity for every \(m\ge4\).

## Relationship to prior work

Finite graph-type realization in \(H_3\) is classical. The general five-vertex failure and the first connected-base failure are treated in *Sharp five-point failure of edge-insertion monotonicity in triangle-free Henson pair-type proportions*. The five-vertex star transition is the \(m=4\) member of the family here and is not a separate novelty claim. Padding that example by isolates preserves its sign but also preserves the number of leaves of its nontrivial component before insertion. It does not give the centre-to-isolate sign for stars with more leaves, which instead follows from the formula above.

## References

- C. W. Henson, *A family of countable homogeneous graphs*, Pacific J. Math. **38** (1971), 69–83, §2. https://doi.org/10.2140/pjm.1971.38.69
- G. Conant, *Forking and dividing in Henson graphs*, §3. https://arxiv.org/abs/1401.1570
- *Sharp five-point failure of edge-insertion monotonicity in triangle-free Henson pair-type proportions*, record SCOPE-20261122-d0d13fed5b7b.
