# Maximal intersecting pairs have a truncated line-graph shattering complex

## Finding

Let \(n\ge4\), let \(E=\binom{[n]}2\), and let \(\mathcal H_n\) comprise the incidence vectors of **all inclusion-maximal pairwise-intersecting subfamilies** of \(E\). A query asks whether one particular pair belongs to the unknown maximal family. Let \(\mathsf{Sh}(\mathcal H_n)\) be the simplicial complex of subsets \(F\subseteq E\) on which all \(2^{|F|}\) membership patterns occur.

**Theorem.** A support \(F\subseteq E\) is shattered if and only if \(|F|\le3\) and every two distinct pairs in \(F\) intersect. Equivalently,
\[
\mathsf{Sh}(\mathcal H_n)=\bigl(\Delta(L(K_n))\bigr)^{(2)},
\]
where \(\Delta\) is the clique complex and the superscript denotes the two-dimensional skeleton. The complex is pure of dimension two, with
\[
\Phi_n(z)=1+\binom n2z+n\binom{n-1}2z^2+
\left(n\binom{n-1}3+\binom n3\right)z^3.
\]
Both its VC and Littlestone dimensions are exactly three. Its integral homology is torsion-free, and its homotopy type is
\[
\mathsf{Sh}(\mathcal H_n)\simeq\bigvee^{B_n}S^2,
\qquad B_n=\binom{n-1}{3}+n\binom{n-2}{3}
=\frac{(n-3)(n-2)(n^2-3n-1)}6.
\]
In particular, the extra \(n\binom{n-2}{3}\) two-dimensional homology classes are present in the shattering skeleton but disappear when the higher-dimensional maximal-star simplices are filled in.

## Assumptions and scope

All graphs are finite, undirected, simple and labeled. Here \(K_n\) has vertex set \([n]\), its line graph \(L(K_n)\) has vertex set \(E\), with two distinct pairs adjacent if they intersect. An intersecting family is inclusion-maximal if no additional pair can be adjoined while keeping pairwise intersection. The family of hypotheses \(\mathcal H_n\) contains each such maximal family once. For a support \(F\subseteq E\), a labeling \(A\subseteq F\) is realized when there exists \(H\in\mathcal H_n\) with \(H\cap F=A\). VC shattering means all labelings are realized; Littlestone shattering means a complete, adaptive binary membership-query tree with distinct hypotheses at its leaves. The conclusions are for each integer \(n\ge4\); no asymptotic assumption is used.

## Proof

**1. Classification of hypotheses.** If all edges of a pairwise-intersecting family share a vertex \(v\), maximality forces the complete star \(S_v=\{\{v,x\}:x\ne v\}\). Otherwise choose \(ab\) and \(ac\) in the family and an edge not containing \(a\). This third edge must be \(bc\). An edge meeting all of \(ab,ac,bc\) belongs to the triangle \(T_{abc}=\{ab,ac,bc\}\). Thus every inclusion-maximal family is one of the \(n\) complete stars or \(\binom n3\) full triangles. For \(n\ge4\) each is inclusion-maximal, and they are distinct. In particular, \(|\mathcal H_n|=n+\binom n3\).

**2. Necessity for shattering.** If a support contains disjoint edges, the all-positive labeling is impossible, since every hypothesis is intersecting. Suppose instead \(F\) is pairwise intersecting with at least four edges. Any pairwise-intersecting family of at least four distinct edges has a common vertex \(v\); this follows from the star/triangle classification above. The only hypothesis containing at least three of these edges is the full star \(S_v\). Consequently the labeling that marks exactly three edges positive and any fourth edge negative cannot be realized. Hence a shattered support is a clique in \(L(K_n)\) with at most three vertices.

**3. Sufficiency for shattering.** Any intersecting support \(F\) of size three is either a three-edge star \(\{ab,ac,ad\}\) or a triangle \(\{ab,bc,ca\}\). For a three-star, the full star \(S_a\) realizes all three positives; the triangle on \(a\) and two chosen leaves realizes exactly any specified pair; the full star at a chosen leaf realizes its sole selected edge; and the triangle on the three leaves realizes zero positives. For a triangle, \(T_{abc}\) realizes all three, \(S_a,S_b,S_c\) realize the respective two-edge pairs, a triangle on either selected edge and a point outside \(\{a,b,c\}\) realizes exactly that selected edge, and a star at an outside point realizes the zero labeling. An outside point exists because \(n\ge4\). Every intersecting support of size zero, one or two extends to an intersecting three-edge support (use a star), hence is shattered by restriction. This establishes the characterization.

**4. Face counts and purity.** Vertices of the shattering complex are all \(\binom n2\) edges of \(K_n\). Its one-faces are the \(n\binom{n-1}2\) unordered adjacent-edge pairs, counted by their unique common endpoint. Three-edge cliques are exactly the three-edge stars (\(n\binom{n-1}3\)) and triangles (\(\binom n3\)); these two types are disjoint. Every one-face extends to a three-star because \(n\ge4\), so the complex is pure of dimension two. The claimed polynomial follows, with no faces of larger cardinality. In particular \(\operatorname{VCdim}=3\).

**5. Adaptive dimension.** Let \(e=ab\) be any first query. Exactly two star hypotheses and \(n-2\) triangle hypotheses contain \(e\). In this positive restriction \(\mathcal H_n(e=1)\), a different edge \(f\) either is disjoint from \(e\) (then its positive branch is empty) or meets \(e\) in one endpoint, say \(f=ac\) (then exactly the two hypotheses \(S_a,T_{abc}\) have \(f=1\)). Therefore **every** nontrivial root query in \(\mathcal H_n(e=1)\) has a positive child of size at most two. No complete tree of depth three can fit into that restriction: a depth-three root would require a positive child supporting depth two, which needs at least four distinct hypotheses. Thus \(\operatorname{Ldim}(\mathcal H_n(e=1))\le2\) for every \(e\), ruling out depth four for the original class. Conversely, every shattered three-edge support yields a complete adaptive tree of depth three by querying the three edges in a fixed order. Hence \(\operatorname{Ldim}=3\).

**6. Homotopy and integral homology.** Let \(X=\mathsf{Sh}(\mathcal H_n)\), and let \(X_v\) be the two-skeleton of the simplex on the \(n-1\) edges incident with \(v\). The union \(Y=\bigcup_v X_v\) contains every vertex and edge of \(X\); the missing two-faces are exactly the triangles \(T_{abc}\). Each \(X_v\) is simply connected (the two-skeleton of a simplex with at least three vertices). Different \(X_v,X_w\) meet in the one vertex corresponding to \(vw\), and no three meet. The graph-of-spaces form of van Kampen gives \(\pi_1(Y)\cong\pi_1(K_n)\), a free group whose cycles are generated by the ordinary triangles in \(K_n\). Attaching the missing faces \(T_{abc}\) fills precisely these generators; thus \(\pi_1(X)=0\). The complex has dimension two, so \(\widetilde H_2(X;\mathbb Z)\) is free abelian, \(\widetilde H_1(X;\mathbb Z)=0\), and all other reduced homology groups vanish. Its rank is determined from the Euler characteristic:
\[
\operatorname{rank}\widetilde H_2=f_2-f_1+f_0-1
=n\binom{n-1}3+\binom n3-n\binom{n-1}2+\binom n2-1
=\binom{n-1}3+n\binom{n-2}3.
\]
A connected simply connected two-dimensional CW complex is homotopy equivalent to a wedge of its \(\operatorname{rank}\widetilde H_2\) two-spheres, by Hurewicz and the homological Whitehead theorem. This proves the claimed homotopy type.

## Verification

The supplied `verify.py` independently constructs all star/triangle concepts, checks every support of sizes zero through four for each \(n=4,5,6,7,8\) against the statement, and computes ranks of the simplicial boundary matrices over \(\mathbb F_2\). The separately written `verify.cpp` independently builds the concepts as bit masks and repeats every support/trace check. Both yield the shattered-support counts \((1,6,12,8,0)\), \((1,10,30,30,0)\), \((1,15,60,80,0)\), \((1,21,105,175,0)\), and \((1,28,168,336,0)\) for those five orders. Boundary computations give integral-theorem-compatible two-dimensional ranks \(1,9,34,90,195\). These finite checks corroborate, but do not replace, the proof for all \(n\).

Run `python3 verify.py` and compile the other verifier using `g++ -std=c++17 -O2 verify.cpp -o verify_bin && ./verify_bin` in the directory containing the sources.

## Relationship to prior work

Frankl and Kupavskii (arXiv:1701.04110, first public 15 January 2017) study enumerations of intersecting families of uniform sets, including the maximal-family framework. This provides the extremal-set-theoretic context, but their results are asymptotic counts and do not characterize membership shattering or online learning of the individual maximal two-set families. Nikseresht (arXiv:2007.13082, first public 26 July 2020) characterizes algebraic properties of the full clique complex and records the same star/triangle cliques; no shattering claim is made. Goyal, Shukla and Singh (arXiv:2009.12130, first public 25 September 2020), in particular Lemma 3.2 and Theorem 3.4, identify and determine homotopy types of **full** line-graph clique complexes and classify their facets as stars or triangles. Their results imply the full complex \(\Delta L(K_n)\) has homotopy type \(\bigvee^{\binom{n-1}3}S^2\). Here the independently defined **VC-shattering** complex is instead its two-skeleton, with \(n\binom{n-2}3\) additional two-spheres, and has exact static and adaptive learning ranks. Neither inspected text states this shattering-equivalence or its two-skeleton Betti polynomial. The maximal-star classification and full-complex topology are credited rather than claimed as new.

## Limitations

The maximal-intersecting-two-set hypothesis class is special: the result does not assert analogous claims for intersecting \(k\)-sets when \(k\ge3\), for arbitrary Kneser graphs or arbitrary host graphs. The integral homotopy proof is mathematical and not an independent computational homotopy certification; the finite boundary programs calculate mod-two ranks only. The online conclusion concerns individual pair-membership queries, not arbitrary subset queries. A comprehensive historical-priority guarantee is not claimed; equivalent unindexed literature remains possible. The identification of the shattering complex as a truncation is distinct from the previously established full clique-complex homotopy and should not be confused with that result.

## References

- P. Frankl and A. Kupavskii, *Counting intersecting and pairs of cross-intersecting families*, arXiv:1701.04110 (first publicly posted 2017-01-15), https://arxiv.org/abs/1701.04110.
- A. Nikseresht, *Algebraic Properties of Clique Complexes of Line Graphs*, arXiv:2007.13082 (first publicly posted 2020-07-26), https://arxiv.org/abs/2007.13082.
- S. Goyal, S. Shukla and A. Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:2009.12130 (first publicly posted 2020-09-25), https://arxiv.org/html/2009.12130v2.
