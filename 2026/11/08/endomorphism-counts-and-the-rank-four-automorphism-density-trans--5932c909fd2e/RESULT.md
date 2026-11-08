# Endomorphism counts and the rank-four automorphism-density transition in tensor powers of dual numbers

## Finding
For a finite field \(k=\mathbb F_q\), set \(A_r(k)=k[x_1,\ldots,x_r]/(x_1^2,\ldots,x_r^2)\). All homomorphisms below are unital \(k\)-algebra homomorphisms, and \(1\le r\le4\). The following formulas determine the exact numbers of endomorphisms and automorphisms of these canonical \(2^r\)-dimensional monomial complete intersections.

For odd \(q\), define
\[
S_1=q,\qquad S_2=q(2q-1),\qquad S_3=q^3(4q-3),\qquad S_4=q^7(q^3+5q-5).
\]
Then
\[
|\operatorname{End}_k(A_r)|=S_r^r,\qquad
|\operatorname{Aut}_k(A_r)|=r!(q-1)^r q^{r(2^{r-1}-1)}.
\]
The exact automorphism densities among endomorphisms are, in increasing ranks,
\[
1-q^{-1},\quad \frac{2(q-1)^2}{(2q-1)^2},\quad
\frac{6(q-1)^3}{(4q-3)^3},\quad
\frac{24(q-1)^4}{(q^3+5q-5)^4}.
\]
As odd prime powers \(q\to\infty\), they tend to \(1,1/2,3/32,0\), respectively, and the rank-four density is asymptotic to \(24q^{-8}\).

For even \(q\), for every \(1\le r\le4\),
\[
|\operatorname{End}_k(A_r)|=q^{r(2^r-1)},\qquad
|\operatorname{Aut}_k(A_r)|=q^{r(2^r-r-1)}|\operatorname{GL}_r(q)|.
\]
Their quotient is \(\prod_{j=1}^r(1-q^{-j})\), which tends to one as even prime powers \(q\to\infty\). Thus rank four is the first rank in this sequence where the odd-characteristic density decays to zero, in contrast to characteristic two.

## Assumptions and scope
The ring \(A_r\) is the tensor product over \(k\) of \(r\) copies of the dual-number algebra \(k[\varepsilon]/(\varepsilon^2)\). A basis is the set of square-free monomials \(x_I=\prod_{i\in I}x_i\), for subsets \(I\subseteq\{1,\ldots,r\}\), with \(x_\varnothing=1\). Its unique maximal ideal \(\mathfrak m_r=(x_1,\ldots,x_r)\) has dimension \(2^r-1\). The theorem counts *labeled ring maps* on the specified presentation, not isomorphism classes, and does not claim a complete algebraic description of the composition monoid. Every \(q\) is a prime power, not necessarily a prime. The first four ranks are classified; no general assertion for \(r>4\) is made.

## Proof
**Reduction to square-zero elements.** A unital \(k\)-algebra map is determined by \(y_i=f(x_i)\). It exists precisely when \(y_i^2=0\) for every \(i\). Each square-zero element has zero constant term because its constant term squared vanishes in the field; hence it lies in \(\mathfrak m_r\). All choices are independent. Consequently, if \(S_r\) counts square-zero elements in \(\mathfrak m_r\), then \(|\operatorname{End}_k(A_r)|=S_r^r\).

**Characteristic two.** Frobenius squaring is additive. Every nonconstant square-free monomial has square zero, so every element of \(\mathfrak m_r\) has square zero. Thus \(S_r=q^{2^r-1}\) in characteristic two. Such a map is invertible exactly when its linear map on \(\mathfrak m_r/\mathfrak m_r^2\) is invertible: the forward direction is necessary, and a surjective map on the cotangent space is surjective on the finite-dimensional local algebra by induction on powers of its nilpotent maximal ideal (or Nakayama's lemma). The \(r\) linear coefficient columns may form any element of \(\operatorname{GL}_r(q)\); the \(r(2^r-1-r)\) remaining coefficients are arbitrary. This proves the even-characteristic formulas.

**Odd-characteristic square-zero recursion.** Decompose \(A_{r+1}=A_r\oplus x_{r+1}A_r\). For \(y=u+x_{r+1}v\),
\[
y^2=u^2+2x_{r+1}uv.
\]
Since the two summands occupy distinct direct-sum components and \(2\) is invertible, the condition is \(u^2=0\) and \(uv=0\). Hence
\[
S_{r+1}=\sum_{u\in\mathfrak m_r,\ u^2=0}q^{\dim_k\operatorname{Ann}_{A_r}(u)}.
\]
It is immediate for \(r=1\) that \(S_1=q\). In \(A_1\), zero has annihilator dimension two and each of the \(q-1\) nonzero multiples of \(x_1\) has annihilator dimension one. This yields \(S_2=q^2+(q-1)q=q(2q-1)\).

In \(A_2\), the square-zero elements are zero, nonzero multiples of \(x_1x_2\), and the elements \(x_i(a+bx_j)\) with \(a\ne0\), for the two choices \(\{i,j\}=\{1,2\}\). Their counts and multiplication ranks are respectively \((1,0)\), \((q-1,1)\), and \((2q(q-1),2)\). Their annihilator dimensions are four minus those ranks, yielding
\[
S_3=q^4+(q-1)q^3+2q(q-1)q^2=q^3(4q-3).
\]

To compute \(S_4\), write an element of \(\mathfrak m_3\) as
\[
u=a_1x_1+a_2x_2+a_3x_3+b_{12}x_1x_2+b_{13}x_1x_3+b_{23}x_2x_3+c x_1x_2x_3.
\]
The degree-two coefficients of \(u^2\) are \(2a_i a_j\); therefore at most one \(a_i\) is nonzero. If, say, \(a_1\ne0\), the cubic coefficient forces \(b_{23}=0\), and \(u=x_1(a_1+b_{12}x_2+b_{13}x_3+c x_2x_3)\) has multiplication rank four, because its second factor is a unit of the two-variable algebra. There are \(3(q-1)q^3\) such elements. If all \(a_i=0\), any quadratic and cubic coefficients yield a square-zero element. There is one zero element of multiplication rank zero; \(q-1\) nonzero pure cubic elements of rank one; and \(q(q^3-1)\) elements with nonzero quadratic part, of rank two (the image of multiplication is spanned by \(u\) and the nonzero socle monomial). These four strata exhaust the square-zero locus, with annihilator dimensions \(8,7,6,4\). Therefore
\[
\begin{aligned}
S_4&=q^8+(q-1)q^7+q(q^3-1)q^6+3(q-1)q^3q^4\\
&=q^7(q^3+5q-5).
\end{aligned}
\]
This establishes all endomorphism counts.

**Odd-characteristic automorphisms.** The degree-two component of \(y_i^2=0\) implies that its degree-one coefficient vector has at most one nonzero coordinate. An automorphism must induce an invertible linear map on \(\mathfrak m_r/\mathfrak m_r^2\), so its linear matrix is monomial, associated with a permutation \(\sigma\in S_r\). For one image with linear part \(a x_j\), \(a\ne0\), decompose it uniquely as \(y=x_j u+v\), where \(u,v\) belong to the algebra on the remaining \(r-1\) variables. The constant coefficient of \(u\) equals \(a\), so \(u\) is a unit. From \(0=y^2=v^2+2x_j uv\) the direct-sum decomposition forces \(uv=0\), whence \(v=0\). Conversely every \(x_j u\) with \(u\) a unit in the remaining-variable algebra has square zero. There are exactly \((q-1)q^{2^{r-1}-1}\) such images for each prescribed position \(j\). Since their distinct linear coordinates make the cotangent map invertible, every independent selection yields an automorphism. Multiplying by \(r!\) proves the automorphism formula.

Finally divide the formulas. The odd-characteristic rank-four density has numerator of degree four and denominator of degree twelve; the lower ranks yield the stated positive limits. The even-characteristic density is the standard order ratio for \(\operatorname{GL}_r(q)\), proving the contrast.

## Verification
A self-contained Python 3 checker, `verify.py`, independently enumerates square-zero elements of \(A_3(\mathbb F_3)\) and \(A_3(\mathbb F_5)\), computes ranks of multiplication matrices, and weights annihilator dimensions to reconstruct \(S_4(3)=80919\) and \(S_4(5)=11328125\). It additionally enumerates all \(2^{15}=32768\) elements of the radical of \(A_4(\mathbb F_2)\), exhaustively checks rank-one and rank-two formulas over three small prime fields, and independently checks the 72 automorphisms of \(A_2(\mathbb F_3)\). The recorded output ends with `VERIFY_OK`. Run `python3 verify.py` without third-party packages. These finite tests are consistency checks; the proof covers every finite field.

## Relationship to prior work
Díaz, Lucchini Arteche, and Manzano-Flores (arXiv:2609.13741v1, 2026-09-12) study the automorphism algebraic groups of general zero-dimensional monomial algebras over algebraically closed fields of characteristic zero. Díaz, Liendo, Manzano-Flores, and Regeta (arXiv:2408.02197v1, 2024-08-05) determine automorphism groups in characteristic zero. Díaz and Lucchini Arteche (arXiv:2409.15081v1) examine reconstruction of a monomial algebra from its automorphism group. These are broader automorphism themes but, as explicitly scoped in their accessible abstracts, do not state the complete finite-field endomorphism counts, the odd-characteristic rank-four square-zero enumeration, or the characteristic-dependent endomorphism-to-automorphism density. The full primary texts could not be inspected, so implicit coverage within these works is a residual historical-priority risk. A published research record on truncated coordinate-cross algebras considers different multiplication, with all mixed degree-two products zero; that classification does not imply the count for the present square-free complete intersection, whose mixed products survive.

## Limitations
Only ranks \(1\) through \(4\) are enumerated in odd characteristic. No claim is made for larger ranks or for nonunital, non-\(k\)-linear ring maps. The result concerns counts of labeled maps, not their conjugacy classes or full semigroup multiplication. A qualified originality assessment is not an independent priority certification. The nearest motivating 2026 paper and the related 2024 papers were inspected at abstract and scope level, not in full text, and a specialized historical account could already contain equivalent formulas.

## References
- R. Díaz, G. Lucchini Arteche, G. Manzano-Flores, *The structure of automorphism groups of zero-dimensional monomial algebras*, arXiv:2609.13741v1 (publicly posted 2026-09-12), https://arxiv.org/abs/2609.13741 .
- R. Díaz, A. Liendo, G. Manzano-Flores, A. Regeta, *The Automorphism groups of zero-dimensional monomial algebras*, arXiv:2408.02197v1 (2024-08-05), https://arxiv.org/abs/2408.02197 .
- R. Díaz, G. Lucchini Arteche, *Finite monomial algebras are determined by their automorphism group*, arXiv:2409.15081v1 (2024-09-23), https://arxiv.org/abs/2409.15081 .
- *Automorphisms of truncated coordinate-cross algebras over arbitrary fields*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-automorphisms-of-truncated-coordinate-cross-algebras-over-arbitr--625ba30274cb .
