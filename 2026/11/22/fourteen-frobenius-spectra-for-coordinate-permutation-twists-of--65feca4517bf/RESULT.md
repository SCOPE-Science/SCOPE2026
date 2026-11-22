# Fourteen Frobenius spectra for coordinate-permutation twists of the Clebsch cubic

## Finding

Let \(S\subset\mathbf P^4\) be the Clebsch cubic defined by
\[\sum_{i=0}^{4}x_i=\sum_{i=0}^{4}x_i^3=0.\]
For every finite field \(\mathbf F_q\) of characteristic greater than five, the twists of \(S\) arising from its coordinate-permutation group \(S_5\) have exactly seven cocycle classes. The complete Frobenius spectra of their 27 lines, ten Eckardt points, and seven-dimensional geometric Picard representations are determined by the seven cycle partitions \(\lambda\vdash5\) and the indicator \(\epsilon\in\{0,1\}\), where \(\epsilon=0\) for \(q\equiv1,4\pmod5\) and \(\epsilon=1\) for \(q\equiv2,3\pmod5\).

More structurally, write \(V_{(2,2,1)}\) for the five-dimensional irreducible rational representation of \(S_5\) indexed by the partition \((2,2,1)\). The arithmetic Frobenius action on the geometric Picard space has the decomposition
\[\operatorname{Pic}(\overline{S_\sigma})\otimes\mathbf Q\simeq\mathbf1\oplus V_{(2,2,1)}(\sigma)\oplus(\delta\operatorname{sgn})(\sigma),\qquad\delta=(-1)^\epsilon.\]
In particular, \(\operatorname{Tr}(F\mid\operatorname{Pic})=1+\chi_{(2,2,1)}(\sigma)+\delta\operatorname{sgn}(\sigma)\), where the seven character values in the partition order below are \(5,-1,1,-1,-1,1,0\). The isolated sign summand is negated precisely when the squareclass of five is nonsplit in the ground field.

Write \(d^m\) for \(m\) Frobenius orbits of size \(d\), and \(\Phi_r=\Phi_r(U)\) for the \(r\)-th cyclotomic polynomial. The final column is the full degree-seven characteristic polynomial \(\chi_F(U)=\det(UI-F\mid\operatorname{Pic})\).

| Cycle partition \(\lambda\) | \(\epsilon\) | 27-line orbits | Ten Eckardt orbits | Picard trace | \(\chi_F(U)\) |
|---|---:|---|---|---:|---|
| \((1,1,1,1,1)\) | 0 | \(1^{27}\) | \(1^{10}\) | 7 | \(\Phi_1^7\) |
| \((1,1,1,1,1)\) | 1 | \(1^{15},2^{6}\) | \(1^{10}\) | 5 | \(\Phi_1^6\Phi_2\) |
| \((2,1,1,1)\) | 0 | \(1^{3},2^{12}\) | \(1^{4},2^{3}\) | -1 | \(\Phi_1^3\Phi_2^4\) |
| \((2,1,1,1)\) | 1 | \(1^{3},2^{12}\) | \(1^{4},2^{3}\) | 1 | \(\Phi_1^4\Phi_2^3\) |
| \((2,2,1)\) | 0 | \(1^{7},2^{10}\) | \(1^{2},2^{4}\) | 3 | \(\Phi_1^5\Phi_2^2\) |
| \((2,2,1)\) | 1 | \(1^{3},2^{12}\) | \(1^{2},2^{4}\) | 1 | \(\Phi_1^4\Phi_2^3\) |
| \((3,1,1)\) | 0 | \(3^{9}\) | \(1,3^{3}\) | 1 | \(\Phi_1^3\Phi_3^2\) |
| \((3,1,1)\) | 1 | \(3^{5},6^{2}\) | \(1,3^{3}\) | -1 | \(\Phi_1^2\Phi_2\Phi_3^2\) |
| \((3,2)\) | 0 | \(3,6^{4}\) | \(1,3,6\) | -1 | \(\Phi_1\Phi_2^2\Phi_3\Phi_6\) |
| \((3,2)\) | 1 | \(3,6^{4}\) | \(1,3,6\) | 1 | \(\Phi_1^2\Phi_2\Phi_3\Phi_6\) |
| \((4,1)\) | 0 | \(1,2^{3},4^{5}\) | \(2,4^{2}\) | 1 | \(\Phi_1^3\Phi_2^2\Phi_4\) |
| \((4,1)\) | 1 | \(1^{5},2,4^{5}\) | \(2,4^{2}\) | 3 | \(\Phi_1^4\Phi_2\Phi_4\) |
| \((5)\) | 0 | \(1^{2},5^{5}\) | \(5^{2}\) | 2 | \(\Phi_1^3\Phi_5\) |
| \((5)\) | 1 | \(2,5^{3},10\) | \(5^{2}\) | 0 | \(\Phi_1^2\Phi_2\Phi_5\) |

For example, at a five-cycle and \(q\equiv2,3\pmod5\), all 27 lines occur in the orbit pattern \(2^1 5^3 10^1\), no line or Eckardt point is rational, and \(\#S_\sigma(\mathbf F_q)=q^2+1\). At a three-cycle, no line is rational but one Eckardt point is rational, for either squareclass.

## Assumptions and scope

The base is a finite field of order \(q=p^a\), with \(p>5\). A coordinate-permutation twist means the form obtained by descent along a continuous cocycle \(\operatorname{Gal}(\overline{\mathbf F}_q/\mathbf F_q)\to S_5\), where \(S_5\) permutes the five defining coordinates. Such cocycles are classified up to conjugacy by the seven partitions of five; all seven occur over every finite field. The statement concerns these twists and their geometric lines, Eckardt points and rational Picard representation, not arbitrary cubic surfaces or bad characteristic.

## Proof

**Line model and descent.** Let \(D\) be the fifteen objects consisting of a singleton label and an unordered partition of the other four labels into two pairs. They represent the diagonal lines spanned by vectors with opposite entries in each pair and zero at the singleton. Let \(P\) be the set of bijections \(e:\{0,1,2,3,4\}\to\mathbf Z/5\mathbf Z\), quotiented by \(e\sim\pm e+c\). Its cardinality is \(120/10=12\). For a primitive fifth root of unity \(\zeta\), the object \(e\) represents the line spanned by
\[(\zeta^{e(0)},\ldots,\zeta^{e(4)})\quad\text{and}\quad(\zeta^{-e(0)},\ldots,\zeta^{-e(4)}).\]
These are the classical complete 27-line parametrizations. The ten Eckardt points are the coordinate vectors with one \(1\), one \(-1\), and three zero entries, indexed by unordered two-subsets of the five labels. The geometric 27-line construction spreads out over the connected cyclotomic base \(\operatorname{Spec}\mathbf Z[1/30,\zeta_5]\). Its relative Fano scheme is finite étale of degree 27 because the normal bundle of a line on a smooth cubic surface is \(\mathcal O_{\mathbf P^1}(-1)\). The explicit sections are distinct at a good fiber, hence distinct in every good fiber, and exhaust all geometric lines. Their intersection products are locally constant under smooth proper specialization. The ten displayed labeled Eckardt points are likewise distinct for \(p>5\).

For an \(S_5\)-cocycle sending arithmetic Frobenius to \(\sigma\), the Frobenius action on \(D\) and on the Eckardt labels is the ordinary permutation induced by \(\sigma\). On \(P\) it is
\[e(i)\longmapsto q\,e(\sigma^{-1}(i))\pmod5,\]
followed by the quotient by translations and sign. The fifth-root multiplier is trivial on \(P\) if \(q\equiv\pm1\pmod5\) and is the nontrivial commuting involution otherwise. Enumerating these two finite permutation actions for one representative of each \(S_5\) conjugacy class gives the first two orbit columns. Any finite étale zero-dimensional locus with orbit profile \(d_1^{m_1}\cdots d_r^{m_r}\) has zeta function \(\prod_i(1-T^{d_i})^{-m_i}\), so these columns determine the line-scheme and Eckardt-scheme zeta functions over every finite extension.

**Picard representation.** The 27 line classes span the rank-seven rational geometric Picard group of any smooth cubic surface. Let \(G\) denote their \(27\times27\) integer intersection matrix: \(G_{ii}=-1\); for distinct lines \(G_{ij}=1\) when they intersect and zero otherwise. Directly from the explicit line spans, \(G\) has ten off-diagonal ones per row, and satisfies
\[G^3=3G^2+54G,\qquad\operatorname{rank}_{\mathbf Q}G=7,\qquad\operatorname{Spec}(G)=\{9^1,(-6)^6,0^{20}\}.\]
Thus \(\Pi=(G^2-3G)/54\) is the rational projection of the line-label space onto the Picard quotient, and for any Frobenius line permutation matrix \(A\) we obtain the exact identity
\[\operatorname{Tr}(F^n\mid\operatorname{Pic})=\frac1{54}\operatorname{Tr}\bigl(A^n(G^2-3G)\bigr),\qquad n\ge1.\]
The seven degree-seven characteristic polynomials in each quadratic-character case follow by the Newton identities from \(n=1,\ldots,7\); the table gives all fourteen. The \(S_5\) character of this action when \(\epsilon=0\) is the sum of the trivial character, the sign character and the degree-five irreducible character with values \(5,-1,1,-1,-1,1,0\) on the seven conjugacy classes. When \(\epsilon=1\) the fifth-root involution flips only the sign character. This gives the stated uniform Picard decomposition.

**Zeta function of the surface.** Smooth cubic surfaces are geometrically rational, so all second cohomology is algebraic and arithmetic Frobenius acts with eigenvalues \(q\) times those on the Picard space. Consequently, with \(\chi_F\) from the table,
\[Z(S_\sigma,T)=\frac1{(1-T)(1-q^2T)\det(I-qTF\mid\operatorname{Pic})},\]
and in every extension degree \(n\ge1\),
\[\#S_\sigma(\mathbf F_{q^n})=1+q^{2n}+q^n\operatorname{Tr}(F^n\mid\operatorname{Pic}).\]
Both formulas hold for all fourteen cases. The full Frobenius spectra, not merely the first trace, are included in the table.

## Verification

Run `python3 verify_clebsch.py` in an environment with standard Python 3 and no additional dependencies. The program independently enumerates 15 and 12 line labels, ten Eckardt labels, all 120 coordinate permutations, and both fifth-root actions. It realizes the complete 27-line incidence over \(\mathbf F_{11}\) with primitive fifth root \(3\), builds the integer intersection matrix, tests its spectral identity and the Picard projector, and checks every orbit table row and trace. It computes seven Picard traces and reconstructs characteristic polynomials by exact Newton identities. Independent direct projective point counts of the untwisted surface over \(\mathbf F_{11}\) and \(\mathbf F_{17}\) give respectively \(199\) and \(375\) points, agreeing with the predicted Picard traces \(7\) and \(5\). The finite matrix computation is a verification of the explicit algebraic construction; completeness for arbitrary finite fields comes from the geometric 27-line parametrization and the descent argument, not from sampling fields.

## Relationship to prior work

Polo-Blanco (2007), §2.4.3, constructs twists of the Clebsch cubic over \(\mathbf Q\) and treats selected quadratic and quintic cases, while giving the same symmetric coordinate description. Baez (2016) provides the explicit split \(15+12\) line construction. Rybakov–Trepalin (2016), Appendix A, lists the general Weyl-group Frobenius eigenvalue types of cubic surfaces. Those general Weyl eigenvalues already determine the zeta function **once the Weyl class is known**; the zeta formula itself is not claimed as a new general theorem. Sottile–Yahl study general cubic-surface line splitting types, rather than giving the full Clebsch coordinate-twist classification. The contribution here is the concrete uniform seven-by-two classification simultaneously identifying line orbits, Eckardt-point orbits, the Weyl/Picard eigenvalue type, and their fifth-root-squareclass coupling for every coordinate-permutation twist. The formulas for the historical geometric configuration and the general cohomological point-count identity are used, not rediscovered.

## Limitations

This does not classify arbitrary smooth cubic surfaces, and no extension to characteristics two, three or five is asserted. It classifies coordinate-permutation twists, not other possible forms arising from extra automorphisms in special characteristics. The geometric Picard representation is considered over \(\mathbf Q\), not as an integral Galois lattice. The complete historical priority of the combined fourteen-case table is provisional: an earlier unindexed Weyl-subgroup calculation may imply the same table. There has been no independent external mathematical review.

## References

1. I. Polo-Blanco, *Theory and History of Geometric Models*, PhD thesis, University of Groningen, defended 4 May 2007, §2.4.3. https://pure.rug.nl/ws/portalfiles/portal/2803507/thesis.pdf
2. J. Baez, *27 Lines on a Cubic Surface*, AMS Visual Insight, 15 February 2016. https://blogs.ams.org/visualinsight/2016/02/15/27-lines-on-a-cubic-surface/
3. S. Rybakov and A. Trepalin, *Minimal cubic surfaces over finite fields*, arXiv:1611.02475, 8 November 2016, Appendix A. https://arxiv.org/abs/1611.02475
4. F. Sottile and T. Yahl, *Splitting types of the 27 lines on cubic surfaces*, https://franksottile.github.io/research/stories/27_Frobenius/index.html
5. S. McKean, *Rational lines on smooth cubic surfaces*, arXiv:2101.08217, 20 January 2021. https://arxiv.org/abs/2101.08217
