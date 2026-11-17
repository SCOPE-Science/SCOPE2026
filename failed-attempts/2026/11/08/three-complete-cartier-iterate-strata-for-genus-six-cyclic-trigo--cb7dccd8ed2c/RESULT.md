# Three complete Cartier-iterate strata for genus-six cyclic trigonal covers in characteristic two

## Finding
Let \(k\) be algebraically closed of characteristic \(2\). For each monic squarefree septic
\[
f(x)=x^7+a_6x^6+a_5x^5+a_4x^4+a_3x^3+a_2x^2+a_1x+a_0\in k[x],
\]
let \(C_f\) be the smooth projective model of \(y^3=f(x)\). Put
\[
\Delta=a_2+a_3a_6,\qquad E=a_3+a_6^4.
\]
For every such polynomial, the complete sequence of ranks of the Cartier operator \(\mathcal C:H^0(C_f,\Omega^1)\to H^0(C_f,\Omega^1)\) is
\[
(\operatorname{rk}\mathcal C^j)_{j\ge1}=
\begin{cases}
(4,4,4,\ldots),&\Delta\ne0,\\
(4,3,2,2,\ldots),&\Delta=0,\ E\ne0,\\
(4,3,2,1,0,0,\ldots),&\Delta=E=0.
\end{cases}
\]
Consequently the Jacobian \(2\)-rank is respectively \(4,2,0\); its \(a\)-number is \(2\) in all cases (the constant first Cartier rank is covered by [Elkin 2007], not claimed new). The rank-drop hypersurface is \(a_2=a_3a_6\). The rank-zero locus is the smooth, irreducible codimension-two graph \(a_3=a_6^4,\ a_2=a_6^5\) within the squarefree locus. All three strata occur.

## Assumptions and scope
The polynomial has degree exactly \(7\), leading coefficient \(1\), and no multiple root. In characteristic \(2\), the cyclic degree-three map \(C_f\to\mathbb P^1\) is tame and ramified at its seven distinct finite roots and at infinity, all with ramification index \(3\). Riemann--Hurwitz gives \(2g-2=3(-2)+8(3-1)=10\), so \(g=6\). The rank of a semilinear map is its image dimension over \(k\). Its stable rank equals the Jacobian \(2\)-rank. This statement concerns branch-coordinate presentations with infinity distinguished; no moduli-level irreducibility after quotienting by automorphisms is asserted.

## Proof
**Six regular differentials.** At a finite branch point \(y\) is a uniformizer, and \(\operatorname{ord}(dx)=2\). At infinity the pole orders of \(x\) and \(y\) are \(3\) and \(7\), and \(\operatorname{ord}(dx)=-4\). It follows that
\[
v_0=\frac{dx}{y},\quad v_1=\frac{x\,dx}{y},\quad
w_j=\frac{x^j\,dx}{y^2}\quad(0\le j\le3)
\]
are regular everywhere. Their six distinct leading pole orders at infinity (before cancellation) and the genus count yield a basis.

**Exact Cartier matrix.** Write \(\sigma(z)=z^{1/2}\), inverse Frobenius on \(k\). In characteristic \(2\), \(\mathcal C(g^2\omega)=g\mathcal C(\omega)\), \(\mathcal C(x^{2r+1}dx)=x^r dx\), and \(\mathcal C(x^{2r}dx)=0\). Since \(1/y=f(x)/y^4\), direct substitution yields
\[
\begin{aligned}
\mathcal C(v_0)&=a_1^{1/2}w_0+a_3^{1/2}w_1+a_5^{1/2}w_2+w_3=:A,\\
\mathcal C(v_1)&=a_0^{1/2}w_0+a_2^{1/2}w_1+a_4^{1/2}w_2+a_6^{1/2}w_3=:B,\\
\mathcal C(w_0)&=\mathcal C(w_2)=0,\qquad
\mathcal C(w_1)=v_0,\quad\mathcal C(w_3)=v_1.
\end{aligned}
\]
The vectors \(A,B\) are independent: if \(B=\lambda A\), comparison of coordinates gives \(a_6=\lambda^2\), \(a_4=\lambda^2a_5\), \(a_2=\lambda^2a_3\), \(a_0=\lambda^2a_1\); hence \(f=(x+a_6)f'\), contradicting squarefreeness because \(\deg f'=6\). Therefore \(\operatorname{rk}\mathcal C=4\).

**Iterates.** Set \(V=\langle v_0,v_1\rangle\), \(W=\langle w_0,w_1,w_2,w_3\rangle\). In block form \(\mathcal C(V)\subset W\) and \(\mathcal C(W)\subset V\). On \(V\), \(\mathcal C^2\) is \(\sigma^2\)-semilinear with matrix
\[
T=\begin{pmatrix}a_3^{1/4}&a_2^{1/4}\\1&a_6^{1/4}\end{pmatrix},
\qquad \det T=\Delta^{1/4}.
\]
On \(W\), \(\mathcal C^2\) has rank \(2\) with image spanned by \(A,B\). If \(\Delta\ne0\), \(T\) is invertible and both summands retain rank \(2\) under every further even iterate; every positive Cartier iterate has rank \(4\).

Suppose \(\Delta=0\). Put \(u=a_3^{1/4}\) and \(w=a_6^{1/4}\). Then \(T=(u,1)^t(1,w)\), so \(T\) has rank one, giving \(\operatorname{rk}\mathcal C^2=3\). Further products on \(V\) are governed by
\[
T\,T^{\sigma^2}=(u,1)^t\bigl(u^{1/4}+w\bigr)(1,w^{1/4}).
\]
The scalar vanishes precisely when \(a_3+a_6^4=0\), equivalently \(E=0\). Tracking the two alternating summands \(V,W\) gives ranks \(4,3,2,2,\ldots\) when the scalar is nonzero, and \(4,3,2,1,0,0,\ldots\) when it vanishes. There are no other possibilities. Stable rank is the p-rank, proving the stated values.

**Locus geometry and coordinate invariance.** In the affine space with coordinates \(a_0,\ldots,a_6\), \(\Delta=0\) is the graph \(a_2=a_3a_6\), smooth and irreducible. Within it, \(E=0\) is the graph \(a_3=a_6^4, a_2=a_6^5\), smooth and irreducible of codimension two. Intersecting with the nonempty open squarefree locus preserves smoothness and irreducibility. Explicit examples over \(\mathbb F_2\) are \(x^7+x+1\) in the rank-zero locus, \(x^7+x^6+x\) in the middle stratum, and \(x^7+x^6+x^3+x\) in the rank-four stratum; each is squarefree. Under \(x\mapsto ux+v\) with \(u\ne0\), monic normalization changes \(\Delta\) to \(\Delta/u^5\) and \(E\) to \(E/u^4\); therefore the vanishing loci do not depend on the affine branch coordinate.

## Verification
The independent explicit matrix construction in `artifacts/verify_rank.py` enumerates all \(4^7=16384\) monic septics over \(\mathbb F_4\), detects squarefreeness by polynomial gcd, and for every one of the \(12288\) squarefree inputs recomputes the full semilinear Cartier matrix and its first six iterates by exact finite-field arithmetic. The resulting numbers of curves with p-ranks \(0,2,4\) are \(768,2304,9216\), respectively, and there are zero discrepancies. A separate calculation (`artifacts/verify_points.py`) counts points over extensions of \(\mathbb F_2\) of degrees up to six and independently recovers the p-ranks \(0,2,4\) for explicit representatives through the initial coefficients of their zeta numerators. All checks are finite corroboration, not a replacement for the symbolic proof valid over every algebraically closed characteristic-two field. Reproduce with `python3 artifacts/verify_rank.py` and `python3 artifacts/verify_points.py`.

## Relationship to prior work
Elkin [1] proves general lower bounds and a formula for the *first* Cartier rank of cyclic covers, implying that the first rank is constantly four here. The new statement determines **every higher iterate and every coefficient-level p-rank stratum**, which do not follow from a constant first rank. Bouw [2] investigates generic and maximal p-ranks of cyclic and other covers but does not supply these exact branch-coordinate jumping equations in the inspected material. Özman--Pries--Weir [3] treat p-rank strata of trielliptic moduli; their main existence result for primes congruent to two modulo three assumes an odd prime and does not yield the characteristic-two equations. Bucur--David--Feigon--Lalín [4] study asymptotic distributions of Frobenius traces of cyclic trigonal curves, not exact Cartier-iterate equations for every genus-six septic. Existing explicit genus-four quintic-cover rank strata concern a different genus and ramification degree and do not imply this genus-six, three-stratum classification. No unqualified claim of worldwide first discovery is made; unindexed specialized coefficient computations remain a priority risk.

## Limitations
This result addresses Cartier-iterate ranks and p-ranks, not full Ekedahl--Oort types, Newton polygons, unmarked curve-isomorphism classes, or scheme-theoretic multiplicities of corresponding moduli substacks. The analytic and intrinsic moduli consequences beyond the distinguished cyclic covering are not determined. Historical novelty should be independently assessed against specialist literature and inaccessible or unindexed tables.

## References
[1] Arsen Elkin, *The Rank of the Cartier operator on cyclic covers of the projective line*, arXiv:0708.0431, first publicly dated 2007-08-02, https://arxiv.org/abs/0708.0431.

[2] Irene I. Bouw, *The p-Rank of Ramified Covers of Curves*, Compositio Mathematica 126 (2001), 295--322, DOI:10.1023/A:1017513122376, https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6D1BEC9200F6849339665AC4371AB7AF/S0010437X01000343a.pdf.

[3] Ekin Özman, Rachel Pries, Colin Weir, *The boundary of the p-rank 0 stratum of the moduli space of cyclic covers of the projective line*, arXiv:1907.05684, first publicly dated 2019-07-12, https://arxiv.org/abs/1907.05684.

[4] Alina Bucur, Chantal David, Brooke Feigon, Matilde Lalín, *Statistics for traces of cyclic trigonal curves over finite fields*, first manuscript dated 2009-09-07, DOI:10.1093/imrn/rnp162, https://ueaeprints.uea.ac.uk/id/eprint/18580/1/cyclictrigonal-general.pdf.
