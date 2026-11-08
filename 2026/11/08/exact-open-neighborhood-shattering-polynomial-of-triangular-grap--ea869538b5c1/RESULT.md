# Exact open-neighborhood shattering polynomial of triangular graphs

## Finding

Let \(n\ge 2\) be an integer and let \(J(n,2)\) denote the triangular graph, with vertex set \(\binom{[n]}2\) and adjacency between distinct two-element sets meeting in exactly one element. For each vertex \(e\), use its **open** neighborhood \(N(e)\), not its closed neighborhood. Let \(s_k(n)\) be the number of unordered \(k\)-vertex supports shattered by the family \(\{N(e):e\in\binom{[n]}2\}\), and put \(\Phi_n(z)=\sum_{k\ge0}s_k(n)z^k\). Then

\[
\boxed{\Phi_n(z)=1+s_1(n)z+s_2(n)z^2+s_3(n)z^3+s_4(n)z^4,}
\]

where, with \((n)_r=n(n-1)\cdots(n-r+1)\) for \(n\ge r\) and zero otherwise,

\[
\begin{aligned}
s_1(n)&=\mathbf 1_{\{n\ge3\}}\binom n2,\\
s_2(n)&=\mathbf 1_{\{n\ge5\}}\binom{\binom n2}{2},\\
s_3(n)&=\mathbf 1_{\{n\ge6\}}\left(\frac23(n)_4+\frac14(n)_5\right),\\
s_4(n)&=\mathbf 1_{\{n\ge7\}}\frac{25}{24}(n)_5
       +\mathbf 1_{\{n\ge8\}}\frac18(n)_6.
\end{aligned}
\]

Every coefficient of degree at least five is zero. In particular the VC dimension is \(0\) at \(n=2\), \(1\) at \(n=3,4\), \(2\) at \(n=5\), \(3\) at \(n=6\), and \(4\) at \(n\ge7\). For \(n=7\),

\[
\Phi_7(z)=1+21z+210z^2+1190z^3+2625z^4.
\]

The classification also gives random-support asymptotics. For a uniformly chosen unordered triple, respectively quadruple, of graph vertices as \(n\to\infty\), the shattering probabilities are \(12/n+O(n^{-2})\) and \(48/n^2+O(n^{-3})\).

## Assumptions and scope

This theorem concerns simple finite complete graphs on \(n\) labeled points, their line graphs, and exclusively open graph neighborhoods. The empty support is shattered since the concept family is nonempty for \(n\ge2\). A support of \(k\) triangular-graph vertices is treated as the \(k\)-edge set of a simple graph \(H\) on the points appearing in those edges, with no isolated vertices. Distinct edges in the support remain distinct vertices of \(J(n,2)\). There is no assumption that the support graph \(H\) is connected.

## Proof

**Cut identity.** For a center \(e=\{x,y\}\), an edge \(f=\{u,v\}\) in a support belongs to \(N(e)\) if and only if exactly one of \(x,y\) lies in \(f\). The trace of \(N(e)\) on \(E(H)\) is therefore exactly the two-vertex cut

\[
\delta_H(\{x,y\})=\{uv\in E(H):|\{u,v\}\cap\{x,y\}|=1\}.
\]

Thus the support is shattered precisely when the cuts \(\delta_H(\{x,y\})\), as the center pair ranges over the ambient \([n]\), realize every subset of \(E(H)\). Write \(v\) for the number of nonisolated vertices of \(H\). A center pair meets the \(v\)-vertex support in zero, one, or two vertices. Therefore **two additional fresh vertices suffice** to represent all possible center types: for \(n\ge v+2\), no further increase of \(n\) can change whether the fixed abstract support \(H\) is shattered. For smaller \(n\), one tests respectively zero or one available fresh vertex.

**Complete finite classification.** The following table lists *all* shattered isomorphism types of support graphs with one through four edges. The column \(r\) is the minimum number of fresh ambient vertices, over and above the \(v\) nonisolated vertices of \(H\), required for shattering. The last column is the automorphism-group order; \(\sqcup\) means disjoint union. The five-vertex tree denoted \(T\) has degree sequence \((3,2,1,1,1)\).

| Edges \(k\) | Support graph \(H\) | \(v\) | \(r\) | \(|\mathrm{Aut}(H)|\) |
|---:|---|---:|---:|---:|
| 1 | \(K_2\) | 2 | 1 | 2 |
| 2 | \(P_3\) | 3 | 2 | 2 |
| 2 | \(2K_2\) | 4 | 1 | 8 |
| 3 | \(K_{1,3}\) | 4 | 2 | 6 |
| 3 | \(P_4\) | 4 | 2 | 2 |
| 3 | \(P_3\sqcup K_2\) | 5 | 1 | 4 |
| 4 | \(K_{1,4}\) | 5 | 2 | 24 |
| 4 | \(T\) | 5 | 2 | 2 |
| 4 | \(P_5\) | 5 | 2 | 2 |
| 4 | \(P_3\sqcup P_3\) | 6 | 2 | 8 |

There are exactly \(1,2,5,11,26\) isomorphism types of finite simple graphs without isolated vertices having respectively one through five edges. Of the five three-edge types, the triangle and three disjoint edges are not shattered. Of the eleven four-edge types, only the four displayed types are shattered. **None of the twenty-six five-edge types is shattered**, even with two fresh vertices. This rules out shattering of every five-edge support for every \(n\), and hence also rules out larger supports by heredity of shattering.

For completeness, the finite classification is not an inference from testing a few graph orders. It is a complete finite certificate: begin at the empty graph, add an edge (between two existing vertices, between one existing and one new vertex, or between two new vertices), merge isomorphic graphs, and repeat through five edges. Every graph without isolated vertices arises in this recursion: delete one edge, discard newly isolated vertices, and reverse the operation. The certificate in `verify.py` implements this recursion without external libraries, computes graph isomorphisms by exhaustive degree-preserving adjacency bijections, and checks every cut against all \(2^k\) required subsets using exactly \(v,v+1,v+2\) ambient vertices. The script asserts the complete type counts, all positive cases, the minimal fresh-vertex thresholds, and the absence of five-edge cases. These finite operations are exhaustive for *every* ambient \(n\) by the cut identity and two-fresh-vertex reduction.

**Counting.** For an abstract support graph on \(v\) nonisolated vertices, the number of labeled copies in a complete \(n\)-vertex graph is \((n)_v/|\mathrm{Aut}(H)|\). A type contributes only for \(n\ge v+r\). Summing the table gives the singleton and pair coefficients, using

\[
\frac{(n)_3}{2}+\frac{(n)_4}{8}=\binom{\binom n2}{2}
\qquad(n\ge5),
\]

and gives

\[
\frac{(n)_4}{6}+\frac{(n)_4}{2}+\frac{(n)_5}{4}
=\frac23(n)_4+\frac14(n)_5
\quad(n\ge6),
\]

\[
\frac{(n)_5}{24}+\frac{(n)_5}{2}+\frac{(n)_5}{2}
+\mathbf1_{\{n\ge8\}}\frac{(n)_6}{8}
=\frac{25}{24}(n)_5+\mathbf1_{\{n\ge8\}}\frac18(n)_6
\quad(n\ge7).
\]

The zero cases follow from the minimum ambient-vertex thresholds in the table. Finally \(\binom{\binom n2}{3}\sim n^6/48\) and \(\binom{\binom n2}{4}\sim n^8/384\); the leading terms of the third and fourth coefficients are \(n^5/4\) and \(n^6/8\), yielding the stated asymptotic probabilities.

## Verification

Run `python3 verify.py` in the package directory. It uses only the Python standard library. It enumerates all unlabeled support graphs of sizes one through five with no isolated vertices, verifies all two-vertex cuts and automorphism orders, compares the resulting counts with the displayed formulas for all \(2\le n\le12\), and independently enumerates every labeled support of sizes at most four in \(J(n,2)\) for \(2\le n\le10\). The recorded replay ends with `ALL_OPEN_TRIANGULAR_GRAPH_CHECKS_PASS`. This finite computation is a complete certificate because the mathematical reduction establishes that the test list contains every possible graph support of size at most five, and five-point nonshattering bounds every larger size.

## Relationship to prior work

Adler, Benediktsson and Macpherson (arXiv:2007.16042, first posted 2020-07-31; later published in *Discrete Applied Mathematics*) prove that the open-neighborhood VC dimension of every Johnson graph is at most four, determine the range in which four-point shattering exists, and analyze 16 local four-point configurations. In particular their results imply the **dimension** part here. The present claim is instead a coefficient-by-coefficient count of **all** shattered supports in the triangular subfamily \(J(n,2)\), with exact exceptional orders, a cut-based global motif classification, and resulting random-support probabilities. Their local case analysis is relevant prior coverage, not claimed as an independent novelty here. The 2024 work of Coudert, Csikós, Ducoffe and Viennot on graph VC-dimension gives general computational methods for closed neighborhoods rather than this open-neighborhood enumeration.

## Limitations

The theorem does not count nonshattered traces, describe arbitrary Johnson graphs \(J(n,k)\) with \(k>2\), or establish new asymptotic VC-density bounds. A fully exhaustive historical-priority check beyond the inspected sources has not been performed; equivalent coefficient formulas might exist under edge-cut or graph-shattering terminology. The bound in the earlier Johnson-graph paper is not new here. Independent mathematical validation of the present coefficientwise formulas remains outstanding.

## References

1. I. Adler, B. G. Benediktsson and D. Macpherson, *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042v1 (2020-07-31), especially Section 3, Theorems 3.6–3.9; published in *Discrete Applied Mathematics* 312 (2022), 29–44, DOI:10.1016/j.dam.2021.09.017.
2. D. Coudert, K. Csikós, G. Ducoffe and L. Viennot, *Practical Computation of Graph VC-Dimension*, arXiv:2405.07588 (2024-05-13); *SEA 2024*, DOI:10.4230/LIPIcs.SEA.2024.8.
