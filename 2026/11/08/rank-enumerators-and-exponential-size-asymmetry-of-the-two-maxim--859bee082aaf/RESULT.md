# Rank enumerators and exponential size asymmetry of the two maximal regular partition-preserving transformation semigroups

## Finding
Let \(m\ge2\) and partition a \(2m\)-element set into two labeled classes \(A,B\), each of size \(m\). Write \(T_m\) for the transformation monoid preserving the equivalence relation, \(\mathcal R_m\) for its set of regular elements, and \(\mathcal M_{1,m},\mathcal M_{2,m}\) for the two maximal regular subsemigroups containing the units identified by Sangkhanan (2026). Rank is the cardinality of the transformation image.

Let \(S(m,r)\) be a Stirling number of the second kind, and for \(1\le r\le m\) put
\[
u_{m,r}=r!S(m,r),\qquad b_{m,r}=\binom mr\,u_{m,r},\qquad P_m(z)=\sum_{r=1}^m b_{m,r}z^r.
\]
Set
\[
c_{m,r}=4b_{m,r}r^m-2\binom mr\,u_{m,r}^{\,2},\qquad C_m(z)=\sum_{r=1}^m c_{m,r}z^r.
\]
For any set \(\mathcal F\) of transformations, define its rank enumerator as \(R_{\mathcal F}(z)=\sum_{f\in\mathcal F}z^{|\operatorname{im}f|}\). Then the four complete rank enumerators are
\[
\boxed{R_{\mathcal R_m}(z)=2P_m(z)^2+C_m(z),}
\]
\[
\boxed{R_{\mathcal M_{1,m}}(z)=2P_m(z)^2+2mz,}
\]
\[
\boxed{R_{\mathcal M_{2,m}}(z)=C_m(z)+2(m!)^2z^{2m},}
\]
\[
\boxed{R_{\mathcal M_{1,m}\cap\mathcal M_{2,m}}(z)=2mz+2(m!)^2z^{2m}.}
\]
In particular, \(|T_m|=4m^{2m}\), and for a uniformly chosen element of \(T_m\),
\[
\frac12\le \Pr(f\text{ is regular})\le \frac12+\left(\frac78\right)^m+e^{-m/32}.
\]
Thus the regular proportion tends exponentially to \(1/2\), whereas
\[
\frac{|\mathcal M_{1,m}|}{|\mathcal R_m|}\longrightarrow1,
\qquad
\frac{|\mathcal M_{2,m}|}{|\mathcal R_m|}\longrightarrow0
\]
with exponentially small errors. The two inclusion-maximal regular subsemigroups are therefore asymptotically radically different in size.

## Assumptions and scope
All functions are total maps on \(A\sqcup B\). Preservation means each input class is mapped into a single output class; distinct input classes may be sent to the same class. Regularity of \(f\) means that some preserving transformation \(g\) satisfies \(fgf=f\). The two maximal regular subsemigroups are exactly those defined in Sangkhanan's Theorem 3.15; their maximality and uniqueness are prior work, not new claims. All cardinalities count labeled maps and all ranks lie in \(1\le r\le2m\). No statement is made for nonuniform partitions or more than two classes.

## Proof
**1. Criterion from images, reproved directly.** Every \(f\in T_m\) induces one of four maps on the two equivalence classes. If it interchanges or fixes the two classes bijectively, each restriction \(f|_A\) and \(f|_B\) has a set-theoretic right inverse on its image. Extending these right inverses blockwise gives \(g\in T_m\) with \(fgf=f\), so every one of these \(2m^{2m}\) transformations is regular.

If both input blocks map into one output block, let \(U=f(A)\) and \(V=f(B)\). Suppose \(fgf=f\) with \(g\in T_m\). For each \(y\in U\cup V\), \(f(g(y))=y\). Since the whole output block containing \(U\cup V\) must be sent by \(g\) into one fixed input block, either every \(y\in U\cup V\) lies in \(U\) or every such \(y\) lies in \(V\). Thus \(U\subseteq V\) or \(V\subseteq U\). Conversely, if (say) \(U\subseteq V\), choose for every \(y\in V\) a preimage in \(B\), extend the choice to a map from the output block to \(B\), and extend arbitrarily to the other output block. The resulting \(g\in T_m\) satisfies \(fgf=f\). So regularity in the constant quotient-image case is equivalent to nested block images.

**2. Enumerating the nested-image cases by rank.** For a fixed \(r\)-subset \(U\) of the target block, the number of surjections \(A\to U\) is \(u_{m,r}\), and the number of unrestricted maps \(B\to U\) is \(r^m\). Therefore the number of ordered pairs of maps with \(f(A)=U\) and \(f(B)\subseteq U\) is \(u_{m,r}r^m\). Summing over \(\binom mr\) choices of \(U\), doubling for the opposite inclusion, and subtracting pairs with equal images (each counted twice), gives \(2b_{m,r}r^m-\binom mr\,u_{m,r}^2\) regular pairs of union-rank \(r\) for one specified output block. There are two choices of output block, yielding exactly \(c_{m,r}\). For quotient-bijective maps, ranks from the two blocks add, and there are two quotient permutations: their enumerator is \(2P_m(z)^2\). This proves the first formula.

**3. The two maximal regular subsemigroups.** In Sangkhanan's notation, \(\mathcal M_1=\operatorname{Reg}(T_{E^*})\cup L\). When a transformation has image in one output block, the defining condition for \(L\) holds precisely for a constant map: the occupied output block must meet the image in one point. Every quotient-bijective transformation already belongs to \(\operatorname{Reg}(T_{E^*})\). Hence \(\mathcal M_1\) comprises those \(2m^{2m}\) transformations together with the \(2m\) constant maps. Also \(\mathcal M_2=M\cup G_E\), where \(M\) consists of all regular maps whose images lie in one block and \(G_E\) is the unit group; \(|G_E|=2(m!)^2\), all of rank \(2m\). The intersection is exactly the union of the constant maps and the units. The remaining three enumerators follow, with all sets disjoint where added.

**4. Exponential size disparity.** Let \(F,G:[m]\to[m]\) be independent uniform maps and put \(K=|\operatorname{im}G|\). Conditional on \(G\),
\[
\Pr(\operatorname{im}F\subseteq\operatorname{im}G\mid G)=(K/m)^m.
\]
For \(m\ge2\), \(\mathbb EK=m[1-(1-1/m)^m]\le3m/4\), because \((1-1/m)^m\ge1/4\). Changing one coordinate of \(G\) changes \(K\) by at most one. The bounded-differences inequality therefore gives
\[
\Pr(K>7m/8)\le e^{-m/32}.
\]
It follows that
\[
q_m:=\Pr(\operatorname{im}F\subseteq\operatorname{im}G)
\le (7/8)^m+e^{-m/32}.
\]
The fraction of regular maps among those whose two input blocks have the same output block is at most \(2q_m\), and the quotient-bijective maps make up exactly half of \(T_m\). This gives the asserted bound. Moreover, the fraction of regular one-output-block maps in all of \(T_m\) is at most \(q_m\). The unit group satisfies \((m!/m^m)^2\le2^{-(m-1)}\), by multiplying the first \(\lfloor m/2\rfloor\) factors of \(m!/m^m\), all at most \(1/2\). Consequently the proportion of \(\mathcal M_2\) in \(\mathcal R_m\) is at most \(2q_m+2^{-(m-1)}\), while the proportion of \(\mathcal R_m\setminus\mathcal M_1\) in \(\mathcal R_m\) is at most \(2q_m\). Both converge exponentially to zero. This completes the proof.

## Verification
The self-contained standard-library program `verify_regular.py` counts all preserving maps explicitly for block sizes \(m=2,3,4\), compares every rank distribution against the four formulas, and for \(m=2,3\) independently searches for a witnessing inverse \(g\) rather than trusting the nested-image criterion. The computation examines \(64\), \(2916\), and \(262144\) transformations, respectively. The program's recorded output is in `verification_output.txt`. This finite replay is supporting evidence, not an infinite proof. The proof above establishes the theorem for every integer \(m\ge2\).

## Relationship to prior work
Sangkhanan (arXiv:2610.38341v1, 2026) identifies \(\mathcal M_1,\mathcal M_2\) and proves they are the only maximal regular subsemigroups containing the unit group for the stated uniform two-class situation; Section 3 gives their structural definitions and the union \(\mathcal R_m=\mathcal M_1\cup\mathcal M_2\). Pei (2005) established a general regular-element criterion, recalled as Theorem 3.1 in Sangkhanan. The present theorem does not claim these structural classifications or criteria: it evaluates complete rank-by-rank multiplicities and asymptotic volumes of the two maximal subsemigroups and their overlap, which are not stated as explicit formulas in the inspected primary paper. This is a derivation from prior structure, not an independent reproof of the earlier maximality classification.

## Limitations
The result is specific to finite sets with two equal-size equivalence classes. It does not classify maximal regular subsemigroups for more classes or nonuniform blocks, and the exponential estimate gives a convenient quantitative upper bound, not the sharp decay exponent. The relevant early regularity literature has not been exhaustively inspected in full text, so priority under alternative enumerative terminology remains a residual risk.

## References
1. K. Sangkhanan, *Maximal regular subsemigroups containing the group of units of transformation semigroups that preserve a uniform equivalence relation with two classes*, arXiv:2610.38341v1 (first public version October 28, 2026), https://arxiv.org/abs/2610.38341 .
2. H. Pei, *Regularity and Green's relations for semigroups of transformations that preserve an equivalence*, Communications in Algebra 33 (2005), 109–118, https://doi.org/10.1081/AGB-200040921 .
3. H. Chen, X. Liu, and S. Wang, *On semigroups of transformations that preserve a double direction equivalence*, Open Mathematics 21 (2023), 20220606, https://doi.org/10.1515/math-2022-0606 .
