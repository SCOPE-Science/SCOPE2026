# Exact strong-resolving polynomials and sharp basis exchange in finite generalized quadrangles

## Finding

**Theorem.** Let \(\mathcal Q\) be any finite thick generalized quadrangle of order \((s,t)\), with \(s,t\ge2\), and let \(G\) be its point–line incidence graph. Put
\[
N_P=(s+1)(st+1),\qquad N_L=(t+1)(st+1),\qquad N=N_P+N_L.
\]
A vertex set \(S\subseteq V(G)\) is strong resolving if and only if its omitted point set lies on a single geometric line (including the empty set and singletons) and its omitted line set lies in one pencil through a single point (also allowing empty sets and singletons). Consequently the complete strong-resolving-set polynomial is
\[
\begin{aligned}
R_G(z)&=z^N A_P(z^{-1})A_L(z^{-1}),\\
A_P(u)&=1+N_Pu+N_L\sum_{j=2}^{s+1}\binom{s+1}{j}u^j,\\
A_L(u)&=1+N_Lu+N_P\sum_{j=2}^{t+1}\binom{t+1}{j}u^j.
\end{aligned}
\]
Every inclusion-minimal strong resolving set is minimum, with
\[
\operatorname{sdim}(G)=st(s+t+2),\qquad
\#\{\text{strong metric bases}\}=N_PN_L.
\]
Indeed, a basis is obtained uniquely by deleting all \(s+1\) points on one geometric line and all \(t+1\) lines through one geometric point. The omitted line and omitted pencil are chosen independently; the defining point need not lie on the defining line.

Define a \(k\)-exchange of bases to replace between one and \(k\) selected vertices by the same number of previously unselected vertices, with both endpoints minimum strong resolving sets. Then the least \(k\) for which the basis-exchange graph is connected is
\[
k_{\rm conn}=\max\{s,t\}.
\]
At this exact threshold it is a Cartesian product \(H_L\square H_P\), where \(H_L\) is the line-intersection graph of \(\mathcal Q\) when \(s\ge t\), and is \(K_{N_L}\) when \(s<t\); symmetrically \(H_P\) is the point-collinearity graph when \(t\ge s\), and is \(K_{N_P}\) when \(t<s\). The connected graph has radius and diameter \(4\) when \(s=t\), and \(3\) when \(s\ne t\).

## Assumptions and scope

A generalized quadrangle of order \((s,t)\) has \(s+1\) points on each line and \(t+1\) lines through each point; two points share at most one line, two lines meet in at most one point, and for every nonincident point–line pair \((p,\ell)\) there is exactly one point of \(\ell\) collinear with \(p\). "Thick" means \(s,t\ge2\). The theorem is conditional on existence of the finite quadrangle, and requires no Desarguesian, self-dual, or group-transitivity hypothesis.

The incidence graph has a vertex for every point and for every line, and adjacency only for incidence. A vertex \(w\) *strongly resolves* vertices \(u,v\) when a shortest \(w\)-to-\(u\) path passes through \(v\), or a shortest \(w\)-to-\(v\) path passes through \(u\). The coefficient of \(z^j\) in \(R_G(z)\) counts the \(j\)-element strong resolving vertex subsets (not ordered landmark lists). A *minimum* set has globally least cardinality; an *inclusion-minimal* set has no proper strong-resolving subset. A geometric line is a block of the quadrangle, not a graph edge.

## Proof

**1. Distances and mutually maximally distant pairs.** The incidence-graph distance between distinct points is \(2\) if they are collinear and \(4\) otherwise; between distinct lines it is \(2\) if they meet and \(4\) otherwise; point–line distance is \(1\) if incident and \(3\) otherwise. These follow directly from the quadrangle axioms. Two vertices are *mutually maximally distant* (MMD) when no neighbor of either is farther from the other than the pair's current distance. All pairs of points at distance \(4\), and all pairs of lines at distance \(4\), are MMD. Every other pair fails: for collinear distinct points, a line through one but not the other (available as \(t\ge2\)) is at distance \(3\) from the other, exceeding \(2\); the dual argument handles meeting lines. For an incident point–line pair, a different incident neighbor creates a distance increase from \(1\) to \(2\). For a nonincident \((p,\ell)\), only one line through \(p\) meets \(\ell\), so any other line through \(p\) is at distance \(4\) from \(\ell\), exceeding \(3\). Thus the MMD graph consists of the noncollinearity graph on the points and the nonconcurrency graph on the lines, with no cross-shore edges.

**2. Strong resolving sets.** The Oellermann–Peters-Fransen vertex-cover characterization states that \(S\) is strong resolving precisely when \(S\) meets every MMD pair. Its complement \(T=V(G)\setminus S\) must therefore contain no MMD pair. By step 1, the omitted points must be pairwise collinear and the omitted lines pairwise concurrent, independently. Any pairwise-collinear point set with at least two elements lies entirely on the unique line through its first two members: a third point not on that line could be collinear with at most one point on it, by the unique-collinear-point axiom. Dually, any pairwise-concurrent family of at least two lines is a subfamily of one complete pencil. This proves the stated if-and-only-if characterization.

**3. Polynomial, purity and minimum.** Among omitted point sets of size \(j\ge2\), the containing geometric line is unique, yielding \(N_L\binom{s+1}{j}\) possibilities; the singleton and empty counts are \(N_P\) and \(1\). Dually the corresponding omitted line counts are \(N_P\binom{t+1}{j}\), \(N_L\), and \(1\). Since the two shores are unconstrained relative to one another, multiply their omission-generating polynomials and reverse cardinality by \(z^N\). An omitted set is inclusion-maximal exactly when its point component is all points of one line and its line component is all lines of one pencil: every smaller admissible component can be enlarged. Hence the complement is inclusion-minimal strong resolving precisely for such pairs. All have cardinality
\[
N-(s+1)-(t+1)=(s+t+2)(st+1)-(s+t+2)=st(s+t+2).
\]
There are \(N_L\) choices of the point block and \(N_P\) of the line pencil, giving \(N_PN_L\) distinct bases and showing that inclusion-minimal and minimum coincide.

**4. Sharp basis exchanges.** Index a basis by \((\ell,p)\): the deleted points lie on \(\ell\), and the deleted lines go through \(p\). Replacing the first coordinate \(\ell\) by \(\ell'\ne\ell\) requires \(s\) exchanges if the lines meet, and \(s+1\) if they are disjoint; this counts points in the symmetric difference of the deleted sets on that shore. Replacing the second coordinate \(p\) by \(p'\ne p\) requires \(t\) exchanges when the points are collinear, and \(t+1\) otherwise. A simultaneous change of both coordinates requires at least \(s+t>\max\{s,t\}\) exchanges. Consequently, for \(k<\max\{s,t\}\), at least one coordinate is fixed along every edge, so the graph is disconnected. At \(k=\max\{s,t\}\), only one coordinate changes at a time: the first-coordinate factor permits intersecting lines if \(s\ge t\), or all line pairs if \(s<t\); the second permits collinear points if \(t\ge s\), or all point pairs if \(t<s\). This gives the claimed Cartesian product. Both the point-collinearity and the line-intersection graphs have diameter exactly \(2\): for any noncollinear point pair, the quadrangle axiom supplies a common collinear point, and dually for disjoint lines. All complete-graph factors have diameter \(1\). The Cartesian-product distance is the sum of its factor distances, hence the asserted radius and diameter \(4\) or \(3\). This proves the sharp threshold and all claimed metrics.

## Verification

The proof is uniform and does not infer an infinite-family assertion from finite examples. Two standalone reproducibility programs supply independent small-case checks:

- `verify.py` constructs the symplectic quadrangle \(W(3,2)\) and a non-self-dual order-\((2,4)\) quadrangle from the 27-curve intersection geometry, then independently checks each quadrangle axiom, all shortest-path distances and MMD pairs, omitted-shore enumerators, all bases and all exchange components through the connectivity threshold. For \(W(3,2)\), it also checks the strong-resolving distance definition directly for all 225 bases and exhaustively tests every six-vertex omission candidate.
- `verify_duads.cpp` independently constructs \(W(3,2)\) as the duad–syntheme incidence geometry of \(K_6\). Its exact checks recover 120 MMD pairs, 225 optimal bases, 1,350 two-exchange edges and exchange-graph diameter four.

Representative verified values are

| Quadrangle | Vertices | Strong dimension | Bases | First connected exchange threshold | Exchange diameter |
|---|---:|---:|---:|---:|---:|
| \(W(3,2)\), order \((2,2)\) | 30 | 24 | 225 | 2 | 4 |
| Order \((2,4)\) | 72 | 64 | 1,215 | 4 | 3 |

For order \((2,4)\), at exchange budgets \(1,2,3,4\), the component decompositions are respectively 1,215 isolated vertices, 27 components of size 45, 27 components of size 45, and one component of size 1,215. Both programs use exact integer operations and terminate without heuristics.

Reproduce from a directory containing the two source files with `python3 verify.py` and `g++ -std=c++17 -O2 verify_duads.cpp -o verify_duads && ./verify_duads`.

## Relationship to prior work

Oellermann and Peters-Fransen's general theorem (first available online 21 August 2006) proves the equivalence between strong resolving sets and vertex covers of the mutually-maximally-distant graph. This theorem is a cited input, not a new assertion here. Standard finite-generalized-quadrangle axioms and distance formulas also predate this finding. The contribution is the all-order geometric description of *every* strong resolving set, its complete cardinality polynomial, purity of all inclusion-minimal strong resolving sets, and the exact sharp basis-exchange transition in thick quadrangle incidence graphs. The later work of Bartoli, Héger, Kiss and Takáts on generalized quadrangles concerns ordinary distance-resolving sets; its bounds neither imply nor enumerate the strong resolving sets classified here.

## Limitations

The result concerns finite thick generalized quadrangles only; the thin cases \(s=1\) or \(t=1\) are not included. It makes no existence assertion for parameter pairs. The exchange definition keeps cardinality minimum at each endpoint and permits simultaneous vertex replacements, not adjacent token sliding or reconfiguration with extra temporary landmarks. The finite computations test two examples and are not substitutes for the general proof. Earlier unindexed treatments of strong metric bases in generalized incidence geometries may exist; no claim of exhaustive bibliographic priority is made.

## References

1. O. R. Oellermann and J. Peters-Fransen, "The strong metric dimension of graphs and digraphs," *Discrete Applied Mathematics* **155** (2007), 356–364, first online 2006-08-21. DOI: https://doi.org/10.1016/j.dam.2006.06.009 ; lawful full-text reading: https://www.academia.edu/15273597/The_strong_metric_dimension_of_graphs_and_digraphs .
2. C. Godsil and G. Royle, *Algebraic Graph Theory*, Springer, 2001, chapter 5 on generalized polygons and quadrangles, https://djvu.online/file/xLrm4thdjUfDN .
3. D. Bartoli, T. Héger, G. Kiss and M. Takáts, "On the metric dimension of affine planes, biaffine planes and generalized quadrangles," arXiv:1706.06583 (2017), https://arxiv.org/abs/1706.06583 .
4. D. Kuziak, I. G. Yero and J. A. Rodríguez-Velázquez, "Strong metric dimension of rooted product graphs," *International Journal of Computer Mathematics* (2015), https://doi.org/10.1080/00207160.2015.1061656 .
