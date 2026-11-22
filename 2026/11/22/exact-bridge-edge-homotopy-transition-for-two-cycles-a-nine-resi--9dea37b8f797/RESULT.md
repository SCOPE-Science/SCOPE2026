# Exact bridge-edge homotopy transition for two cycles

## Finding

Let \(B_{p,q}\), for integers \(p,q\ge3\), be the graph consisting of disjoint simple cycles of lengths \(p\) and \(q\) joined by exactly one additional edge \(e=uv\), with one endpoint on each cycle. For a graph \(G\), let \(\operatorname{Ind}(G)\) be the simplicial complex of independent vertex sets. Write \(p=3a+r\) and \(q=3b+s\), for \(r,s\in\{0,1,2\}\), and put

\[
d=a+b-1+\mathbf1_{\{r=2\}}+\mathbf1_{\{s=2\}}.
\]

**Theorem.** The complete integral homotopy type is

\[
\operatorname{Ind}(B_{p,q})\simeq \bigvee^{b_{r,s}} S^d,
\qquad
\begin{array}{c|ccc}
b_{r,s}&s=0&s=1&s=2\\ \hline
r=0&3&2&1\\
r=1&2&1&1\\
r=2&1&1&0
\end{array}.
\]

The zero-fold wedge means a contractible space. In particular, all reduced integral homology groups are free, and at most three spheres occur, regardless of the cycle lengths.

There is a sharper *edge-insertion statement*. Set \(X=\operatorname{Ind}(C_p\sqcup C_q)\) and \(Y=\operatorname{Ind}(B_{p,q})\subseteq X\). If \(r=1\) or \(s=1\), the inclusion \(Y\hookrightarrow X\) is a homotopy equivalence. Otherwise the quotient cofiber satisfies \(X/Y\simeq S^d\), and the induced map

\[
\widetilde H_d(Y;\mathbb Z)\longrightarrow\widetilde H_d(X;\mathbb Z)
\]

is a split injection whose cokernel is \(\mathbb Z\). Thus inserting the single bridge destroys precisely one *primitive* integral class if neither cycle has length \(1\pmod3\), and destroys none otherwise. All other reduced homology vanishes.

## Assumptions and scope

Graphs are finite, undirected, simple, and loopless. An independence complex includes the empty face. The paths \(P_m\) have \(m\) vertices; the combinatorial complex \(\operatorname{Ind}(P_0)=\{\varnothing\}\) is treated as the join identity (formally a \((-1)\)-sphere), not as a contractible nonempty topological space. Suspensions and joins involving it use the standard augmented-complex convention. The theorem includes \(p=3\) and \(q=3\). Different choices of bridge endpoints give isomorphic graphs because cycles act vertex transitively. A homotopy equivalence here is ordinary integral, not equivariant.

## Proof

**Path and cycle inputs.** The classical formulas, for \(k\ge0\) whenever the indicated paths exist, are

\[
\operatorname{Ind}(P_{3k})\simeq S^{k-1},\quad
\operatorname{Ind}(P_{3k+1})\simeq *,\quad
\operatorname{Ind}(P_{3k+2})\simeq S^k,
\]

and, for cycle length at least three,

\[
\operatorname{Ind}(C_{3k})\simeq S^{k-1}\vee S^{k-1},\quad
\operatorname{Ind}(C_{3k+1})\simeq S^{k-1},\quad
\operatorname{Ind}(C_{3k+2})\simeq S^k.
\]

Here \(*\) denotes a contractible complex; the case \(P_0\) is formal as stated above. Joins satisfy \(S^i*S^j\simeq S^{i+j+1}\), and distribute over wedges up to homotopy for these pointed, nonempty complexes.

**Vertex-cofiber calculation.** Delete the bridge endpoint \(u\) on \(C_p\), and write \(N[u]\) for its closed graph neighborhood. The standard independent-set decomposition gives a simplicial union of a complex and a cone over its link:

\[
Y=D\cup_L(u*L),\qquad
D=\operatorname{Ind}(P_{p-1})*\operatorname{Ind}(C_q),\qquad
L=\operatorname{Ind}(P_{p-3})*\operatorname{Ind}(P_{q-1}).
\]

Indeed, deleting \(u\) breaks the first cycle into a path and removes the bridge; deleting \(N[u]\) also removes its two cyclic neighbors and the second endpoint \(v\). Hence \(Y\) is the homotopy cofiber of the natural inclusion \(L\to D\).

If \(p=3a+1\), then \(\operatorname{Ind}(P_{p-3})\) is contractible, and so is \(L\). Thus \(Y\simeq D\simeq\Sigma^a\operatorname{Ind}(C_q)\).

If \(p=3a+2\), then \(\operatorname{Ind}(P_{p-1})\) is contractible, and hence \(D\) is contractible. Thus \(Y\simeq\Sigma L\simeq\Sigma^{a+1}\operatorname{Ind}(P_{q-1})\).

If \(p=3a\) with \(a\ge2\), then \(\operatorname{Ind}(P_{p-3})\simeq S^{a-2}\) and \(\operatorname{Ind}(P_{p-1})\simeq S^{a-1}\). The inclusion of the former in the latter is nullhomotopic because \(\pi_{a-2}(S^{a-1})=0\) (including the case \(a=2\), where every map from \(S^0\) to the connected \(S^1\) is freely nullhomotopic). The map \(L\to D\) is a join of that nullhomotopic map and the inclusion \(\operatorname{Ind}(P_{q-1})\hookrightarrow\operatorname{Ind}(C_q)\), hence is nullhomotopic. When \(p=3\), the same map factors through the equatorial inclusion \(\operatorname{Ind}(C_q)\hookrightarrow\operatorname{Ind}(P_2)*\operatorname{Ind}(C_q)\), which is nullhomotopic because it bounds a simplicial cone. Therefore, for all \(p=3a\),

\[
Y\simeq D\vee\Sigma L\simeq
\Sigma^a\operatorname{Ind}(C_q)\vee
\Sigma^a\operatorname{Ind}(P_{q-1}).
\]

Substitution of the two classical path/cycle formulas in these three cases yields all nine entries of \(b_{r,s}\). Whenever it is noncontractible, every summand has dimension \(d\), as stated. This proves the full integral homotopy classification, not merely a field-homology calculation.

**Edge-relative calculation.** In the disjoint union of cycles, the vertex pair \(e=\{u,v\}\) is a face of \(X\), and removing precisely the simplices containing both endpoints gives \(Y\). Its link is

\[
R=\operatorname{lk}_X(e)
=\operatorname{Ind}(P_{p-3})*\operatorname{Ind}(P_{q-3}).
\]

The deleted closed star is \(e*R\), and its intersection with \(Y\) is \(\partial e*R\). As a consequence, the simplicial-pair quotient is

\[
X/Y\cong (e*R)/(\partial e*R)\simeq\Sigma^2 R.
\]

If either residue equals one, the corresponding path factor in \(R\) is contractible; both the deleted star and the attaching intersection are contractible, so the inclusion \(Y\to X\) is a homotopy equivalence by the homotopy pushout property. If neither residue equals one, each path factor is a sphere, with the formal \(S^{-1}\) convention for a triangle, and the join formula yields \(R\simeq S^{d-2}\). Therefore \(X/Y\simeq S^d\).

Finally, the independent-set complex of the disjoint cycles is the join of their cycle complexes. It is a wedge of \(c_r c_s\) spheres of dimension \(d\), where \(c_0=2\) and \(c_1=c_2=1\). The vertex-cofiber calculation gives \(\widetilde H_i(Y;\mathbb Z)=0\) except in dimension \(d\). The long exact sequence of \((X,Y)\), together with \(H_d(X,Y;\mathbb Z)=\mathbb Z\) and zero other relative homology, now reduces to

\[
0\longrightarrow\widetilde H_d(Y;\mathbb Z)
\longrightarrow\widetilde H_d(X;\mathbb Z)
\longrightarrow\mathbb Z\longrightarrow0.
\]

All these groups are free; since the quotient is free, the injection splits integrally. This proves the primitive, rank-one edge-insertion statement. For \(d=1\) the same reduced homology sequence applies, and no additional connectivity assumption is needed.

## Verification

The companion exact finite verifier enumerates every independent set of \(B_{p,q}\) and \(C_p\sqcup C_q\) for all \(3\le p,q\le8\), evaluates all simplicial boundary ranks over \(\mathbb F_2\), and separately computes relative homology groups of the inclusions. All 72 absolute and 36 relative checks agree with the stated formulas. These are consistency checks; the uniform integral and primitive conclusions are established by the preceding topological argument, not extrapolation from finite examples. In particular, \((p,q)=(3,3)\) changes four circles to three, while \((p,q)=(5,5)\) changes a three-sphere to a contractible space, and \((p,q)=(3,4)\) changes no homotopy type.

Reproduce using Python 3 standard library: `python verify.py`. The expected output is embedded as `verification_output.txt`.

## Relationship to prior work

Przytycki and Silvero (2016), Proposition 3.12, showed that independence complexes of cactus graphs are wedges of spheres; since \(B_{p,q}\) is a cactus, that covers the *qualitative* wedge property but not these nine exact multiplicities, the edge cofiber, or integral primitivity. Their Proposition 3.15 also implies noncontractibility when both cycles have lengths divisible by three, but gives no exact rank. Kim's 2021 ternary-graph theorem supplies the contractible-or-single-sphere dichotomy whenever neither cycle has length divisible by three, but does not determine which case, its dimension, or the bridge-induced homology map. Daundkar–Panja–Prasad (2023) compute one-vertex wedges of cycles; vertex identification is not insertion of an edge between two disjoint cycles and does not provide the pair inclusion studied here. These results were compared at the level of implications rather than titles. The case-by-case structural map across the bridge is the distinguishing result.

## Limitations

No statement is made about longer bridge paths, arbitrary cactus graphs, equivariant homology, or minimality under alternative graph modifications. The wedge-of-spheres property for cactus graphs is previously known and is not claimed as new. The presented originality assessment concerns the inspected primary sources and indexed records; an unindexed equivalent calculation remains possible. This is mathematical derivation plus finite verification, not independent external review.

## References

- J. Kim, *The homotopy type of the independence complex of graphs with no induced cycles of length divisible by 3* (first submitted 2021-01-18), arXiv:2101.07131, Theorem 1.1 and cycle formulas. https://arxiv.org/abs/2101.07131
- N. Daundkar, S. Panja, S. Prasad, *Independence complexes of wedge of graphs* (first submitted 2023-03-15), arXiv:2303.08798, Theorem 3.5. https://arxiv.org/html/2303.08798v2
- J. H. Przytycki and M. Silvero, *Homotopy type of circle graphs complexes motivated by extreme Khovanov homology* (first submitted 2016-08-09), arXiv:1608.03002, Propositions 3.12 and 3.15. https://arxiv.org/abs/1608.03002
- D. Kozlov, *Complexes of directed trees* (1999), cited for the classical path/cycle independence-complex formulas in the above papers.
