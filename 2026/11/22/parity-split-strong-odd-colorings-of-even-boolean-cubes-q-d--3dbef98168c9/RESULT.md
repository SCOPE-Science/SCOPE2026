# Parity-split strong odd colorings of even Boolean cubes \(Q_d\)

## Finding

Let \(d\ge 2\) be even, and let \(Q_d\) be the graph on the \(d\)-bit strings, with edges joining strings differing in exactly one bit. Write \(E\) and \(O\) for its even- and odd-Hamming-weight vertex classes. A *strong odd coloring* is a proper coloring such that each color occurring in the open neighborhood of any vertex occurs an odd number of times there.

A four-coloring is *parity-split* if each of its four nonempty color classes is entirely contained in either \(E\) or \(O\), with exactly two colors used on each side. Color names are distinct and the vertices of \(Q_d\) are labelled bit strings. The following numbers are exact:

\[
\#\{\text{parity-split strong odd colorings with named colors }1,2,3,4\}
=6\,2^{2^{d-1}}.
\]

Up to permutation of the four colors, the corresponding number of color partitions is
\[
2^{2^{d-1}-2}.
\]

Moreover, for a fixed pair of named colors on \(E\), their assignments form an affine space over \(\mathbb F_2\) of dimension \(2^{d-2}\). Its associated homogeneous code is self-dual, with length \(2^{d-1}\) and dimension \(2^{d-2}\). Independently the same is true on \(O\). The known minimum number of colors is four; a self-contained lower-bound argument is included below. Thus every counted coloring uses a minimum palette, but **the formula does not count colorings in which a color occurs on both parity sides**.

The named-color counts for \(d=2,4,6\) are respectively \(24\), \(1536\), and \(25\,769\,803\,776\); the corresponding unnamed counts are \(1\), \(64\), and \(1\,073\,741\,824\).

## Assumptions and scope

The graph is finite, simple, connected, and exactly the ordinary binary hypercube. Here \(d\) ranges over *all even integers at least two*. We count every function from the labelled vertex set to the four *named* colors satisfying the conditions, without factoring graph automorphisms. The unnamed count factors **only** the permutation of color names. No assertion is made about arbitrary nonsplit four-colorings.

## Proof

**1. Odd-neighborhood equations.** Index \(E\) and \(O\) in any fixed order and let \(B\) be their \(2^{d-1}\)-by-\(2^{d-1}\) bipartite incidence matrix over \(\mathbb F_2\), with rows indexed by \(O\) and columns by \(E\). If the first color on \(E\) has indicator vector \(f\), then the second has indicator \(\boldsymbol{1}+f\). All opposite-side vertices must see each of these colors an odd number of times, exactly when
\[
Bf=\boldsymbol{1}, \qquad B(\boldsymbol{1}+f)=\boldsymbol{1}.
\]
Because \(d\) is even, \(B\boldsymbol{1}=\boldsymbol{0}\), so the second equation follows from the first. Similarly on \(O\), using \(B^{\mathsf T}\). Colors do not appear in neighborhoods of vertices on their own parity side, and all cross-side edges have unlike colors, so these equations are both necessary and sufficient. A solution cannot be constant, because either constant has zero neighborhood sum. Thus both colors on each side are nonempty.

**2. Solvability.** Define \(f_0\) on \(E\) by \(f_0(x)=1\) exactly when the first coordinate of \(x\) is zero. At an odd vertex whose first coordinate is one, exactly one neighboring even vertex has first coordinate zero; at an odd vertex whose first coordinate is zero, exactly \(d-1\) neighboring even vertices have first coordinate zero. Both numbers are odd when \(d\) is even. Hence \(B f_0=\boldsymbol{1}\).

**3. Exact binary rank.** Identify the even-parity group \(H=E\) with \((\mathbb F_2)^{d-1}\), and the odd-parity side with \(e_1+H\). The neighbors of an odd vertex translate, relative to \(H\), by \(0\) and \(a_i=e_1+e_i\), for \(2\le i\le d\). Thus the matrix \(B\), after identical coordinate labels, represents multiplication in the group algebra \(\mathbb F_2[H]\) by \(1+\sum_{i=2}^d a_i\). This group algebra is
\[
R=\mathbb F_2[t_2,\ldots,t_d]/(t_2^2,\ldots,t_d^2),\quad a_i=1+t_i.
\]
The multiplier is \(d+\sum_{i=2}^d t_i=\sum_{i=2}^d t_i\), since \(d\) is even. An invertible linear change of the \(t_i\) makes this multiplier one generator, say \(t_2\). Such a change induces an algebra automorphism because in characteristic two every linear combination of square-zero generators also has square zero. Multiplication by \(t_2\) takes the \(2^{d-2}\) monomials without \(t_2\) bijectively to the monomials with \(t_2\) and kills the other \(2^{d-2}\) monomials. Therefore
\[
\operatorname{rank}_{\mathbb F_2}(B)=2^{d-2},\quad
\dim\ker B=2^{d-2}.
\]
There are exactly \(2^{2^{d-2}}\) solutions to \(Bf=\boldsymbol{1}\), and the same number to \(B^{\mathsf T}g=\boldsymbol{1}\).

For the coding assertion, the same group-algebra representation is symmetric because each translating group element is its own inverse; hence \(B^{\mathsf T}=B\) under the canonical identification. The multiplier squared is zero (each \(t_i^2=0\)), so \(B^2=0\). Rank equals half the dimension, thus \(\operatorname{im}B=\ker B\). Symmetry yields \((\operatorname{im}B)^\perp=\ker B\), and hence \(\ker B=(\ker B)^\perp\), proving self-duality.

**4. Coloring enumeration.** Choose the two named colors assigned to \(E\) in \(\binom42=6\) ways. After ordering each pair by its names, each parity side has independently \(2^{2^{d-2}}\) assignments by Steps 1–3. Multiplication gives \(6(2^{2^{d-2}})^2=6\,2^{2^{d-1}}\) named colorings. Every coloring has four nonempty classes, so each color partition has exactly \(4!=24\) distinct renamings. This gives \(2^{2^{d-1}-2}\).

**5. Optimal palette.** Every strong odd coloring of \(Q_d\) using just two colors is impossible because each degree is positive and even and all neighbors of a vertex would have the other color. Suppose a three-color strong odd coloring existed. At every vertex the other two colors must each appear an odd positive number of times: because the positive even degree is the sum of zero-or-odd counts for at most two other colors, both counts must be odd. For each color indicator \(h\) on all vertices, the full binary adjacency matrix \(A\) would therefore satisfy \((I+A)h=\boldsymbol{1}\). But over \(\mathbb F_2\), \(A=\sum_{i=1}^d T_{e_i}\) (coordinate-flip operators), whence \(A^2=dI=0\) and \(A\boldsymbol{1}=0\) because \(d\) is even. Applying \(I+A\) to the equation forces \(h=(I+A)\boldsymbol{1}=\boldsymbol{1}\) for each of the three colors, a contradiction. One color is also impossible for a graph with edges. Since four-color constructions exist by Steps 1–4, the minimum is exactly four. This last scalar minimum was already established in the literature (see References), and is not claimed as novel.

## Verification

The standalone scripts `verification/check_rank.py` and `verification/check_direct.py` use different enumeration approaches. The first computes incidence ranks over \(\mathbb F_2\) for \(d=2,4,6,8\), checks a particular affine solution, and enumerates solutions at \(d=2,4\). The second directly enumerates subsets on each parity side at \(d=2,4\), checks every selected color class and every local color multiplicity, and matches the named and unnamed totals. Expected exact stdout is in `verification/expected.txt`. These finite checks corroborate, but do not replace, the all-even-\(d\) algebraic proof.

## Relationship to prior work

Kwon and Park introduced strong odd coloring and its neighborhood condition in 2024 [1]. Caro, Petruševski, Škrekovski and Tuza established general graph-product bounds in 2024 [2]. The same authors later proved that \(\chi_{\mathrm{so}}(Q_d)=4\) for even \(d\) (Proposition 26 of [3]), using a four-color construction. The claim here is distinct: it counts **all** optimal four-colorings that respect the canonical even/odd bipartition and identifies a self-dual binary kernel governing those choices. A standard code-rank statement alone would not count arbitrary strong odd colorings; the neighborhood constraints and restriction are both part of the exact claim.

## Limitations

This is not the complete count of all four-color strong odd assignments of an even-dimensional cube: a color may in principle be present on both parity sides. The count is independent of palette-name choices and cube automorphisms only in the stated senses. The proof does not characterize nonsplit optimal colorings or their number. Historical priority of this particular restricted counting formula has not received independent exhaustive clearance.

## References

1. H. Kwon and B. Park, *Strong odd coloring of sparse graphs*, arXiv:2401.11653 (first posted 22 January 2024), https://arxiv.org/abs/2401.11653.
2. Y. Caro, M. Petruševski, R. Škrekovski, and Z. Tuza, *On strong odd colorings of graphs*, arXiv:2410.02336 (first posted 3 October 2024), https://arxiv.org/abs/2410.02336.
3. Y. Caro, M. Petruševski, R. Škrekovski, and Z. Tuza, *The odd independence number of graphs, I: Foundations and classical classes*, arXiv:2509.20763 (first posted 25 September 2025), Proposition 26 and Section 5, https://arxiv.org/abs/2509.20763.
