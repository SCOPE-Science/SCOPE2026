# Fourteen forbidden supports and \(4{,}712\) Zariski chambers on two three-torsion extremal elliptic surfaces

## Finding
Let \(X_{44}\) and \(X_{431}\) be the complex extremal rational elliptic surfaces, in the Miranda--Persson classification, with respective singular fibers \(IV^*+IV\) and \(IV^*+I_3+I_1\). Their Zariski-chamber generating polynomials, with the variable recording the cardinality of the negative part's support, coincide:
\[
\begin{aligned}
Z_{X_{44}}(t)=Z_{X_{431}}(t)={}&1+13t+78t^2+282t^3+672t^4\\
&+1092t^5+1215t^6+896t^7\\
&+393t^8+70t^9.
\end{aligned}
\]
In particular, each has exactly \(4{,}712\) Zariski chambers, including the nef chamber, and exactly \(70\) chambers have the maximum support size \(9\).

More structurally, both surfaces have precisely \(13\) negative irreducible curves. Label the \(IV^*\) fiber components by \(C,A_i,B_i\), where \(i\in\{0,1,2\}\), and label the three components of \(IV\) or \(I_3\) by \(T_0,T_1,T_2\), and the three disjoint torsion sections by \(S_0,S_1,S_2\). Their intersection graph has edges
\[
(C,A_i),\ (A_i,B_i),\ (B_i,S_i),\ (S_i,T_i)
\quad(i=0,1,2),
\]
and \((T_i,T_j)\) for each \(i<j\); all unlisted intersections vanish. Each fiber component has square \(-2\) and each section has square \(-1\).

**Complete forbidden-support description.** A subset of the negative curves supports a Zariski chamber if and only if it contains none of the following \(14\) configurations:

1. The complete set \(\{C,A_0,A_1,A_2,B_0,B_1,B_2\}\) and the triangle \(\{T_0,T_1,T_2\}\).
2. For each \(i\in\{0,1,2\}\), the triples \(\{B_i,T_i,S_i\}\) and the six-sets \(\{C,A_0,A_1,A_2,B_i,S_i\}\).
3. For each unordered pair \(\{i,j\}\subset\{0,1,2\}\), the four-sets \(\{T_i,T_j,S_i,S_j\}\) and the seven-sets \(\{C,A_i,A_j,B_i,B_j,S_i,S_j\}\).

Each forbidden support is inclusion-minimal among supports whose intersection matrices fail to be negative definite. Each has determinant zero, while every proper subset has a negative-definite intersection matrix.

## Assumptions and scope
The base field is \(\mathbb C\); the surfaces are relatively minimal elliptic fibrations with a section and have the specified full Kodaira fiber configurations. Zariski chambers are the chambers in the big cone defined by the support of the negative part of Zariski decomposition. The empty support counts as the nef chamber. The polynomial records support cardinalities of **all** negative irreducible curves, not only a chosen subset.

## Proof
**(1) Geometry determines exactly thirteen negative curves.** On a rational elliptic surface, the canonical class is the negative of the fiber class \(F\), and \(F\) is nef. If an irreducible curve \(D\) has \(D^2<0\), the adjunction identity \(2p_a(D)-2=D^2-F\cdot D\), with \(F\cdot D\ge0\), implies \(p_a(D)=0\); indeed, since \(D^2\le-1\), the left side cannot be nonnegative. It then follows that \(D^2=F\cdot D-2\), so either \(F\cdot D=0,D^2=-2\), or \(F\cdot D=1,D^2=-1\). The first curves are components of singular fibers; the latter are sections because a degree-one map to the base from a smooth rational curve is an isomorphism. For both named extremal fibrations the Miranda--Persson classification gives a section group of order \(3\). Consequently there are exactly \(7+3=10\) negative fiber components and \(3\) sections.

**(2) Their intersections form one marked graph.** A Kodaira \(IV^*\) fiber has the extended \(E_6\) dual graph, three arms \(C-A_i-B_i\); a Kodaira \(IV\) fiber and an \(I_3\) fiber both have triangular component intersection matrices. In the 3-torsion section group, a nonzero section meets a nonidentity component in each reducible fiber: the height formula \(0=2+2(S_i\cdot S_0)-(4/3+2/3)\) forces \(S_i\cdot S_0=0\) and both local contributions to be maximal. The three sections are pairwise disjoint (translation by a torsion section preserves intersections), while each meets its own corresponding outer component and triangle component transversely in one point. Number the nonidentity sections and the corresponding components compatibly. This produces precisely the \(13\)-vertex graph displayed above for both surfaces.

**(3) Negative-definiteness is finite and exactly decidable.** In the order
\[
(C,A_0,A_1,A_2,B_0,B_1,B_2,T_0,T_1,T_2,S_0,S_1,S_2),
\]
the symmetric intersection matrix \(M\) has the displayed diagonals and edge entries. For each of the \(2^{13}=8192\) subsets \(I\), the principal matrix \(M_I\) is negative definite if and only if its leading principal minors have signs \((-1)^j\) for all \(j=1,\ldots,|I|\) (Sylvester's criterion). The accompanying standalone verifier computes these signs using both exact rational \(LDL^T\) elimination and an independent integer Bareiss determinant algorithm. For *every* subset, the two tests agree with avoidance of the \(14\) explicitly listed forbidden sets. Moreover, each forbidden matrix has determinant zero and every deletion of one chosen curve gives a negative-definite matrix; any smaller proper subset lies in such a deletion and is likewise negative definite. Hence this is exactly the list of minimal forbidden supports. This is an exhaustive finite proof, not sampling.

**(4) Count supports.** The bijection between negative-definite supports and Zariski chambers, including the empty nef support, is the established Bauer--Funke--Neumann correspondence. The exact test gives support counts \((1,13,78,282,672,1092,1215,896,393,70)\) and none of size \(\ge10\). Independently, inclusion--exclusion over the \(14\) forbidden sets \(\mathcal F\) computes
\[
Z(t)=\sum_{\mathcal G\subseteq\mathcal F}(-1)^{|\mathcal G|}
 t^{|\cup\mathcal G|}(1+t)^{13-|\cup\mathcal G|},
\]
with the convention \(\cup\varnothing=\varnothing\). The resulting coefficients coincide with the determinant test and sum to \(4{,}712\). Both surfaces have exactly the same intersection data, so the polynomial is identical.

## Verification
Run `python3 verification/verify.py` using only the standard library. It constructs the \(13\)-curve matrix, tests all \(8{,}192\) subsets in two exact-arithmetic implementations, identifies precisely the \(14\) inclusion-minimal non-negative-definite supports, verifies each is singular and every one-point deletion negative definite, and independently reproduces every coefficient using inclusion--exclusion over all \(2^{14}\) selections of forbidden supports. It prints `ALL_CHECKS_PASSED`. The full recorded output is in `verification/output.txt`. No external datasets or approximate floating-point tests are used.

## Relationship to prior work
Miranda and Persson (1986) classify the two elliptic surfaces, their fiber types, and their Mordell--Weil group order; these facts are foundational, not new. The general negative-support/Zariski-chamber correspondence and counting method are due to Bauer, Funke, and Neumann (2009), with algorithmic extensions by Bauer and Schmitz (2012). Those inspected works do **not** list the \(14\) forbidden supports or the \(4{,}712\)-chamber polynomial for the \(IV^*\) pairs. The claim here is a complete new specialization of the correspondence to two classical *three-torsion* configurations, including the minimal-obstruction classification. It is different from analogous computations for rational elliptic surfaces with \(II^*\) fibers and trivial Mordell--Weil groups.

## Limitations
The computation concerns only the two named complex elliptic surfaces; it is not a uniform statement for all extremal rational elliptic surfaces. No Mori-chamber classification is claimed. Exact historical priority remains provisional because an unindexed specialist computation or older graph-counting table could cover this incidence configuration. The independent scientific audit has not been performed. The enumeration's completeness depends on the prior geometric classification of negative curves, which is separately justified above; merely running the code would not establish that geometry.

## References
- Rick Miranda and Ulf Persson, *On Extremal Rational Elliptic Surfaces*, Math. Z. 193 (1986), 537--558, https://doi.org/10.1007/BF01160474; open full text: https://www.math.colostate.edu/~miranda/preprints/Miranda-Persson1986_Article_OnExtremalRationalEllipticSurf.pdf .
- Tyler Jarvis, William Lang, Jeremy Ricks, *Integral Models of Extremal Rational Elliptic Surfaces*, first publicly dated preprint 2009-08-13, https://arxiv.org/abs/0908.1831 .
- Thomas Bauer, Michael Funke and Sebastian Neumann, *Counting Zariski Chambers on Del Pezzo Surfaces*, 2009-12-04, https://arxiv.org/abs/0912.0958 .
- Thomas Bauer and David Schmitz, *Zariski chambers on surfaces of high Picard number*, 2012-04-19, https://arxiv.org/abs/1204.4373 .
