# Exact frozen-state spectrum for cyclic proper ternary colorings under neighbor swaps

## Finding

Consider proper named three-colorings of the indexed cycle \(C_n\), \(n\ge3\), under the move that exchanges colors at two neighboring vertices if the result remains proper. The **frozen states** are those with no allowed swap. Their exact number is
\[
 F_n=L_n+2+2\cos(2\pi n/3)+2r_n,
\]
where \(L_0=2\), \(L_1=1\), \(L_n=L_{n-1}+L_{n-2}\) are Lucas numbers, and
\[
 r_0=3,\quad r_1=-1,\quad r_2=1,\quad
 r_n=-r_{n-1}-r_{n-3}\quad(n\ge3).
\]
In particular, frozen states do not exist exactly for lengths \(3,5,7\); they exist at every even length at least four and every odd length at least nine. Their length generating function is
\[
 \sum_{n\ge3}F_nz^n
 =-z\frac{D_0'(z)}{D_0(z)}-2z\frac{D_1'(z)}{D_1(z)}-6z^2,
\]
with \(D_0(z)=1-z^2-2z^3-z^4\) and \(D_1(z)=1-z^2+z^3-z^4\). Writing \(\varphi=(1+\sqrt5)/2\), the number of frozen states is \(\varphi^n+O(\alpha^n)\), where \(\alpha=1.4655712318\ldots\) is the modulus of the negative real root of \(u^3+u^2+1\). Thus the fraction of proper three-colorings that are frozen is asymptotic to \((\varphi/2)^n\).

## Assumptions and scope

Vertex positions are indexed modulo \(n\), and the color names \(0,1,2\) are distinct; color permutations and rotations are **not** identified. A coloring \(x\) is proper when \(x_i\ne x_{i+1}\) for all cyclic indices. An edge of the reconfiguration graph exists precisely when a swap of the colors at positions \(i,i+1\) leaves all cyclic adjacencies proper. A frozen coloring has degree zero. The count includes all such colorings, not equivalence classes; \(n\ge3\) throughout.

## Proof

**1. Encode the coloring by its increments.** Define \(s_i\in\{0,1\}\) by \(s_i=1\) when \(x_{i+1}-x_i\equiv1\pmod3\), and \(s_i=0\) when the difference is \(-1\pmod3\). Set \(p=\sum_i s_i\). The closure equation is \(2p-n\equiv0\pmod3\), equivalently \(p+n\equiv0\pmod3\). Conversely, for each binary cyclic increment word satisfying this congruence, choosing any one of the three starting colors determines a unique proper coloring. Therefore such an increment word corresponds to exactly three colorings.

**2. A local swap lemma.** Suppose a proper coloring has \(x_i=a\), \(x_{i+1}=b\), with \(a\ne b\). Swapping these colors remains proper if and only if \(x_{i-1}\ne b\) and \(x_{i+2}\ne a\). Since the original coloring was proper, these conditions force both external neighbors to be the third color \(c\notin\{a,b\}\). Equivalently, the four consecutive colors form \(c,a,b,c\), traveling around the three-color cycle in one orientation. Hence the swap is legal if and only if \(s_{i-1}=s_i=s_{i+1}\). This also applies for \(n=3\): the external neighbors coincide, and the three different colors still satisfy the two boundary inequalities. Thus a coloring is frozen exactly when the associated cyclic binary increment word avoids both constant triples \(000\) and \(111\).

**3. The transfer matrix.** Index the four states \(00,01,10,11\). Allow a transition \((a,b)\to(b,c)\) if \((a,b,c)\notin\{(0,0,0),(1,1,1)\}\) and assign it weight \(t^c\). The transfer matrix is
\[
 T(t)=\begin{pmatrix}
 0&t&0&0\\
 0&0&1&t\\
 1&t&0&0\\
 0&0&1&0
 \end{pmatrix}.
\]
For every \(n\ge3\), \(\operatorname{tr}T(t)^n=\sum_s t^{p(s)}\), summed over **indexed** cyclic binary words avoiding the two triples; each closed state walk has one fixed starting index, so periodic words require no division. Let \(\omega\) be a primitive cubic root of unity and put \(M_j=\omega^jT(\omega^j)\), \(j=0,1,2\). The roots-of-unity filter for \(p+n\equiv0\pmod3\), multiplied by the three choices of initial color, gives exactly
\[
 F_n=\sum_{j=0}^{2}\operatorname{tr}(M_j^n).
\]
Direct four-by-four determinant expansion gives
\[
\det(I-zM_0)=(1-z-z^2)(1+z+z^2)=D_0(z),
\]
\[
\det(I-zM_1)=\det(I-zM_2)
=(1-z)(1+z+z^3)=D_1(z).
\]
Because \(\operatorname{tr}(M^n)\) is the sum of the \(n\)-th powers of its eigenvalues (also for a nondiagonalizable matrix), the \(M_0\) contribution is \(L_n+2\cos(2\pi n/3)\). Each remaining contribution is \(1+r_n\), by Newton identities for \(u^3+u^2+1=0\). This proves the formula. Summing the trace identities via \(-zD'(z)/D(z)\) and subtracting the first two coefficients (zero at length one and six at length two) proves the stated \(n\ge3\) generating function.

**4. Exactly which lengths have frozen states.** For lengths \(3,5,7\), the closure congruence permits respectively \(p\in\{0,3\}\), \(p\in\{1,4\}\), and \(p\in\{2,5\}\). In each case the minority bit can split the majority bits into too few cyclic runs to keep all runs of length at most two. Thus no permitted sign word exists. For every even \(n\ge4\), the alternating sign word \((01)^{n/2}\) satisfies both closure and the two triple exclusions. For every odd \(n\ge9\), the sign word \((001)^3(01)^{(n-9)/2}\) does likewise: it has \(p+n\equiv0\pmod3\). These constructions prove existence at all other lengths.

**5. Asymptotics.** The Lucas contribution equals \(\varphi^n+(-\varphi^{-1})^n\). The three roots of \(u^3+u^2+1\) have maximum modulus \(\alpha\approx1.4655712318<\varphi\); the other terms are bounded. Therefore \(F_n=\varphi^n+O(\alpha^n)\). The number of proper named three-colorings of \(C_n\) is \(2^n+2(-1)^n\), so the fraction is asymptotic to \((\varphi/2)^n\).

## Verification

Run `python3 verify.py` with Python 3.10 or later. The self-contained program directly constructs every proper named coloring for lengths \(3\) through \(13\), computes legal adjacent swaps without using the increment criterion, checks the predicted local degree and formula, and compares a separate enumeration of admissible increment words through length \(20\). It checks explicit existence witnesses through length \(301\) and a transfer-matrix trace recurrence. These finite tests support, but do not replace, the complete proof. For example, the frozen counts for lengths \(3\) through \(13\) are \(0,18,0,42,0,90,18,216,66,522,234\).

## Relationship to prior work

Arrighi, Fernau, de Oliveira Oliveira, and Wolf study adjacent-element reconfiguration with width constraints and two-letter string rewriting, motivating constrained swap reachability but not this cyclic-color frozen enumeration [1]. Fuchs, Saito, Suga, Suzuki, and Tamura introduce adjacent color swapping for proper graph colorings and analyze rigid three-colorings on **paths**, rather than the exact number of rigid states on cycles [2]. Agur, Fraenkel, and Klein enumerate binary cyclic configurations forbidding both constant triples in a majority-rule setting [3]; without the new congruence filter this does not enumerate proper cyclic three-colorings under swap moves. Belavadi, Cameron, and Merkel analyze one-vertex recoloring, a different transition relation [4]. No claim of exhaustive historical priority is made.

## Limitations

The result counts degree-zero colorings only. It does not classify nontrivial components, all degrees, or graph diameter. The earlier binary forbidden-triple count does not by itself establish novelty for a weighted congruence refinement; a previously unindexed equivalent weighted enumeration remains possible. Computational checks terminate at the explicitly stated lengths. No external independent validation has been performed.

## References

[1] E. Arrighi, H. Fernau, M. de Oliveira Oliveira, P. Wolf, *Order Reconfiguration Under Width Constraints*, MFCS 2021, first public 2021-08-18, https://doi.org/10.4230/LIPIcs.MFCS.2021.8.

[2] J. Fuchs, R. Saito, T. Suga, T. Suzuki, Y. Tamura, *Coloring Reconfiguration under Color Swapping*, arXiv:2511.06473 (2025), https://arxiv.org/abs/2511.06473.

[3] Z. Agur, A. S. Fraenkel, S. T. Klein, *The Number of Fixed Points of the Majority Rule* (1988), https://www.imbm.org/wp-content/uploads/2020/01/AFK88.pdf.

[4] G. C. Belavadi, K. Cameron, O. Merkel, *Reconfiguration of Vertex Colouring and Forbidden Induced Subgraphs*, arXiv:2206.09268 (2022), https://arxiv.org/abs/2206.09268.
