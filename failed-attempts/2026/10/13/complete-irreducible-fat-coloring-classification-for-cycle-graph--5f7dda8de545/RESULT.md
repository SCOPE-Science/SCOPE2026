# Complete irreducible FAT coloring classification for cycle graphs

## Finding

Let \(C_n\) be the cycle on vertices \(v_0,v_1,\ldots,v_{n-1}\), with indices read modulo \(n\). A FAT \(k\)-coloring is treated as a partition into nonempty color classes, so permutations of color names do not create new colorings.

For every \(n\ge 3\), all FAT colorings of \(C_n\) are exactly these:

1. The trivial one-coloring, for every \(n\).
2. The proper bipartition, exactly when \(2\mid n\). Up to exchanging its two colors, its cyclic pattern is \(0101\cdots\), and its parameters are \(\alpha=1\), \(\beta=0\).
3. Two nonproper two-colorings, exactly when \(4\mid n\). Up to exchanging the two colors, their cyclic patterns are
\[
0011\,0011\cdots
\qquad\text{and}\qquad
0110\,0110\cdots,
\]
and both have \(\alpha=\beta=1/2\).
4. The proper three-coloring, exactly when \(3\mid n\). Up to permuting the three colors, its cyclic pattern is \(012\,012\cdots\), and its parameters are \(\alpha=1/2\), \(\beta=0\).

Therefore, if \(I(C_n)\) denotes the number of irreducible FAT colorings, then
\[
I(C_n)=1+2\mathbf 1_{4\mid n}+\mathbf 1_{6\mid n}.
\]
Thus \(I(C_4)=3\), \(I(C_6)=2\), \(I(C_8)=3\), and \(I(C_{12})=4\).

This corrects the cycle statement in Example 5.12 of Beers and Mulas: the missing colorings are the two nonproper \(\alpha=\beta=1/2\) partitions on every cycle whose order is divisible by four.

## Assumptions and scope

Graphs are finite, simple, and undirected. The FAT definition is the one used by Beers and Mulas: a coloring with nonempty classes \(V_1,\ldots,V_k\) has parameters \(\alpha,\beta\in[0,1]\) satisfying, for every vertex \(v\) and every color class \(V_i\),
\[
|N(v)\cap V_i|=
\begin{cases}
\alpha\deg(v),&v\notin V_i,\\
\beta\deg(v),&v\in V_i.
\end{cases}
\]
Color names are ignored, so a coloring is a set partition of the vertex set. A FAT coloring is irreducible when it is maximal under refinement among FAT colorings.

The claim concerns cycle graphs \(C_n\) for \(n\ge3\). It does not assert a classification for paths, disjoint unions of cycles, or general maximum-degree-two graphs.

## Proof

Every vertex of \(C_n\) has degree two. For a FAT coloring with \(k>1\), choose a vertex and a color class not containing it. Then \(2\alpha=|N(v)\cap V_i|\) is an integer in \(\{0,1,2}\), so
\[
\alpha\in\{0,1/2,1}.
\]
The identity
\[
\beta+(k-1)\alpha=1
\]
follows by summing the neighbor counts over all color classes.

If \(\alpha=0\), then \(\beta=1\). Every vertex has both neighbors in its own color class, so every color class is a union of connected components. Because \(C_n\) is connected, this forces \(k=1\), contrary to \(k>1\). Hence every nontrivial FAT coloring has \(\alpha>0\).

If \(\alpha=1\), the identity gives \(\beta=2-k\). Nonnegativity of \(\beta\) forces \(k=2\) and \(\beta=0\). Every vertex then has both neighbors in the opposite class, so the colors alternate. This is possible exactly when \(n\) is even and gives the unique proper bipartition.

Suppose \(\alpha=1/2\). Then
\[
\beta=1-(k-1)/2=(3-k)/2.
\]
Thus either \(k=2\) and \(\beta=1/2\), or \(k=3\) and \(\beta=0\). No \(k\ge4\) is possible.

Consider first \(k=2\) and \(\alpha=\beta=1/2\). Each vertex has exactly one neighbor of its own color and exactly one neighbor of the other color. For the edge \(v_iv_{i+1}\), let \(s_i=1\) when its endpoints have the same color and \(s_i=0\) otherwise. At vertex \(v_i\), exactly one of the incident edges is monochromatic, hence
\[
s_{i-1}+s_i=1.
\]
Therefore the sequence \((s_i)\) alternates, so \(n\) is even. Exactly \(n/2\) cycle edges are bichromatic; traversing each such edge flips the color, and returning to \(v_0\) requires an even number of flips. Hence \(n/2\) is even, equivalently \(4\mid n\). Conversely, when \(4\mid n\), either choice of \(s_0\) generates a valid coloring. After ignoring a global exchange of the two color names, these are precisely the two distinct partitions with patterns \(0011\cdots\) and \(0110\cdots\).

Now take \(k=3\) and \(\alpha=1/2,\beta=0\). The coloring is proper, and each vertex has one neighbor in each of the two colors different from its own. Once the colors of two consecutive vertices are fixed, the next color is forced to be the third color. Thus the sequence is periodic with period three. It closes on the cycle exactly when \(3\mid n\), and in that case it gives one partition up to permutation of the three color names.

This proves the complete FAT-coloring classification.

It remains to identify the irreducible members. There are no FAT colorings with more than three classes. Hence every three-coloring above is irreducible. A two-coloring could only fail to be irreducible if the three-coloring refined it.

When both the proper two-coloring and the three-coloring exist, \(6\mid n\). A class of the three-coloring contains \(v_i\) and \(v_{i+3}\), which have opposite parity, so that class is not contained in either bipartition class. Thus the three-coloring does not refine the proper two-coloring.

When a paired nonproper two-coloring and the three-coloring both exist, \(12\mid n\). For the \(0011\cdots\) partition, the three-color class containing \(v_0\) also contains \(v_3\), and these lie in different paired classes. For the shifted \(0110\cdots\) partition, the three-color class containing \(v_1\) also contains \(v_4\), again in different paired classes. Thus the three-coloring refines neither paired coloring. Consequently every nontrivial FAT coloring in the classification is irreducible.

The trivial one-coloring is irreducible exactly when no nontrivial FAT coloring exists. Counting the resulting maximal partitions yields
\[
I(C_n)=1+2\mathbf 1_{4\mid n}+\mathbf 1_{6\mid n}.
\]

## Verification

The accompanying script `artifacts/verify.py` independently enumerates all labeled colorings with one, two, or three colors for every cycle \(C_n\) with \(3\le n\le12\), discards non-surjective labelings, tests the FAT equations directly from neighborhoods using exact rational arithmetic, canonicalizes color names to set partitions, computes refinement maximality, and compares the observed partitions with the classification above.

The analytic proof already shows that no FAT coloring with four or more colors can occur on a cycle, so enumeration through three colors is exhaustive for each checked order. The replay checks \(805342\) labeled colorings and confirms the predicted FAT partitions and irreducible counts for every order from three through twelve, including the corrective cases \(C_4\), \(C_8\), and \(C_{12}\).

The finite computation is corroborative; the proof establishes the statement for every \(n\ge3\).

## Relationship to prior work

Beers and Mulas introduced FAT colorings and, in Example 2.17 of their 2025 preprint, correctly determined the FAT chromatic number of every cycle. Their later Example 5.12 states that \(C_n\) has two irreducible FAT colorings when \(6\mid n\) and exactly one otherwise. That conclusion omits the nonproper two-colorings with \(\alpha=\beta=1/2\) that occur whenever \(4\mid n\). The smallest counterexample is \(C_4\), which has the proper bipartition and two additional paired irreducible colorings.

Shaebani's 2026 paper performs a complete case analysis for \(C_6\) while constructing a graph with exactly two irreducible FAT colorings. It explicitly considers the \(\alpha=\beta=1/2\) case and proves that this case does not occur on \(C_6\). The present theorem explains the exact boundary: that case occurs on \(C_n\) if and only if \(4\mid n\), so Shaebani's \(C_6\) conclusion remains valid.

Targeted literature searches for the paired \(0011\) cycle colorings, the divisibility-by-four condition, and the corrected irreducible-count formula located no later source stating this correction. A 2026 spectral follow-up discusses FAT colorings under graph operations and uses copies of \(C_4\) in an unrelated complement example, but does not supply this cycle irreducibility correction.

## Limitations

The result is restricted to cycles. It corrects one explicit family-level statement in the current FAT-coloring literature but does not alter the previously published FAT chromatic numbers of cycles.

The originality conclusion is based on targeted searches and direct inspection of the most relevant accessible full texts. Concurrent or poorly indexed work could independently contain the same correction.

## References

1. L. Beers and R. Mulas, “Fair and Tolerant (FAT) Graph Colorings,” arXiv:2510.18494, first public October 21, 2025; current inspected version v2, November 13, 2025.
2. S. Shaebani, “On The Number of Irreducible FAT Colorings,” arXiv:2606.22374v1, June 21, 2026. Mathematics Subject Classification: \(05C15,05C07\).
3. L. Beers and R. Mulas, “Spectral Perspectives on FAT Graph Colorings,” arXiv:2604.21665v1, April 23, 2026.
