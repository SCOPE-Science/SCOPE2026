# Complete retraction-rank spectra of split bilinear-product algebras over finite fields

## Finding
Let \(q\) be any prime power, \(n\geq1\), \(k=\mathbb F_q\), and \(\lambda\in k^\times\). Define the \((2n+1)\)-dimensional nonunital associative algebra
\[
 A_{n,\lambda}=k^n\oplus k^n\oplus kz,\qquad
 (x,y,s)(x',y',s')=(0,0,x\cdot y'+\lambda y\cdot x').
\]
Here \(x\cdot y=\sum_{i=1}^n x_i y_i\), and the last coordinate is the coefficient of the basis element \(z\). Let \(E_{n,\lambda,r}(q)\) denote the number of \(k\)-linear associative-algebra endomorphisms \(P\) satisfying \(P^2=P\) and \(\dim_k\operatorname{im}P=r\). Define \({a\brack b}_q\) as the Gaussian binomial coefficient, zero if \(b<0\) or \(b>a\), and \(g_t(q)=\prod_{i=0}^{t-1}(q^t-q^i)\), with \(g_0(q)=1\).

**The complete rank distribution**, valid in every characteristic, is
\[
 E_{n,\lambda,r}(q)=q^{r(2n-r+1)}S_{n,r}^{(\lambda)}(q)
 \quad(0\leq r\leq n),\qquad
 E_{n,\lambda,2n+1}(q)=1,
\]
and \(E_{n,\lambda,r}(q)=0\) at every other rank. In particular every proper retract is a square-zero algebra and no retraction has rank strictly between \(n\) and \(2n+1\).

The factor \(S_{n,r}^{(\lambda)}(q)\) has exactly three arithmetic phases:

**Generic nonsymmetric phase** (\(\lambda^2\ne1\)):
\[
 S_{n,r}^{(\lambda)}(q)=
 \sum_{\substack{0\leq a\leq n,\ 0\leq b\leq n-a\\0\leq t=a+b-r\leq\min(a,b)}}
 {n\brack a}_q{n-a\brack b}_q
 {a\brack t}_q{b\brack t}_q g_t(q).
\]

**Split symmetric phase** (\(q\) odd and \(\lambda=1\)):
\[
 S_{n,r}^{(1)}(q)={n\brack r}_q\prod_{i=0}^{r-1}(q^{n-i-1}+1).
\]

**Alternating phase** (\(\lambda=-1\), including \(\lambda=1\) when \(q\) is even):
\[
 S_{n,r}^{(-1)}(q)=\prod_{i=0}^{r-1}\frac{q^{2(n-i)}-1}{q^{r-i}-1}.
\]
Empty products are one. In even characteristic the label \(S^{(-1)}\) equals \(S^{(1)}\), and the symmetric-phase line is not used.

Thus the retraction-rank polynomial \(\sum_r E_{n,\lambda,r}(q)u^r\) depends on \(\lambda\) **only through the above phase**. The number of maximum-dimensional square-zero images in the generic case is
\[
 S_{n,n}^{\mathrm{generic}}(q)=\sum_{a=0}^{n}{n\brack a}_q,
\]
versus \(\prod_{i=1}^{n}(q^i+1)\) in the alternating case; these also give their exact maximum-proper-rank retraction counts after multiplication by \(q^{n(n+1)}\).

## Assumptions and scope
All endomorphisms are \(k\)-linear and multiplication-preserving, without a unitality requirement (the algebra has no unit). Rank means ordinary linear rank on the full \((2n+1)\)-dimensional space, including the annihilator line \(kz\). The parameter is nonzero. There is no restriction on whether \(q\) is prime or a nonprime prime power. The algebra is a central sum of \(n\) copies of the two-generator bilinear-product algebra with products \(e_if_i=z\), \(f_ie_i=\lambda z\); it is not the indecomposable algebra denoted \(H_{2n}(\lambda)\) in some classification literature.

## Proof
Write \(V=U\oplus U^*\cong k^n\oplus k^n\) and define \(B_\lambda((x,y),(x',y'))=x\cdot y'+\lambda y\cdot x'\). Because \(\lambda\ne0\), this form is nondegenerate, and \(A_{n,\lambda}^2=kz\). Every endomorphism therefore sends \(z\) into \(kz\). It has the unique form
\[
 P(v+sz)=Tv+(\ell(v)+\alpha s)z,
 \quad T\in\operatorname{End}_k(V),\ \ell\in V^*,\ \alpha\in k.
\]
Multiplicativity and idempotence are respectively equivalent to
\[
 B_\lambda(Tv,Tw)=\alpha B_\lambda(v,w),
\]
and
\[
 T^2=T,\quad \alpha^2=\alpha,\quad \ell\circ T+\alpha\ell=\ell.
\]
If \(\alpha=1\), nondegeneracy makes \(T\) injective, and \(T^2=T\) then forces \(T=I_V\). The last identity forces \(\ell=0\). This gives the unique identity endomorphism, of rank \(2n+1\).

If \(\alpha=0\), the image \(W=T(V)\) is totally \(B_\lambda\)-isotropic, meaning \(B_\lambda(W,W)=0\). Conversely, for any such \(r\)-space \(W\), any projection \(T:V\to W\) and any \(\ell\) with \(\ell\circ T=\ell\) define an idempotent algebra endomorphism, whose image is the graph \(\{w+\ell(w)z:w\in W\}\) and has dimension \(r\). For fixed \(W\), projections number \(q^{r(2n-r)}\): complements of \(W\) are graphs of arbitrary maps \(V/W\to W\). For each projection, \(\ell\) factors through \(T\), giving \(q^r\) choices. Hence the rank-\(r\) count is \(q^{r(2n-r+1)}\) times the number of totally isotropic \(r\)-spaces.

For \(\lambda^2\ne1\), let \(X\) and \(Y\) be the coordinate projections of such \(W\). For \(w=(x,y)\), \(w'=(x',y')\) in \(W\), put \(p=x\cdot y'\) and \(q'=x'\cdot y\) (the scalar \(q'\) is not the field cardinality). Two-sided isotropy yields \(p+\lambda q'=0=q'+\lambda p\). Since \(1-\lambda^2\ne0\), both vanish. Therefore \(X\perp Y\), and conversely every subspace of \(X\oplus Y\) whose projected spaces are \(X,Y\) is totally isotropic when \(X\perp Y\).

Let \(\dim X=a\), \(\dim Y=b\), \(\dim W=r\), and \(t=a+b-r\). There are \({n\brack a}_q{n-a\brack b}_q\) choices of orthogonal \((X,Y)\). The vector-space Goursat description gives \(K_X=W\cap X\) of codimension \(t\) in \(X\), \(K_Y=W\cap Y\) of codimension \(t\) in \(Y\), and an isomorphism \(X/K_X\cong Y/K_Y\). These data uniquely determine \(W\); they number \({a\brack t}_q{b\brack t}_q g_t(q)\). Summing yields the displayed generic formula. Since \(r\leq a+b\leq n\), all larger proper ranks vanish. For \(r=n\), necessarily \(a+b=n\), \(t=0\), and \(W=X\oplus Y\); summing over \(a\) gives the maximal-rank formula.

In the alternating phase \(B_\lambda\) is a nondegenerate symplectic form, so all nonzero vectors in the symplectic quotient \(W^\perp/W\) are isotropic. In the split symmetric odd-characteristic phase, the quotient is a split orthogonal space and has \((q^{m-1}+1)(q^m-1)\) nonzero isotropic vectors when its dimension is \(2m\). Count ordered isotropic frames by extending a totally isotropic \(i\)-space: every isotropic vector of the quotient has \(q^i\) lifts. Dividing by \(\prod_{i=0}^{r-1}(q^r-q^i)\), the number of ordered bases of an \(r\)-space, gives the two product expressions. These standard extension counts also show the maximal isotropic dimension is \(n\). This completes every case.

## Verification
The standalone Python program `verify.py` enumerates all subspaces via reduced row-echelon forms, independently tests the pairwise bilinear isotropy equations, and compares with the three formulas for \(n=1,2\). It covers \(\mathbb F_3\), \(\mathbb F_5\), \(\mathbb F_7\), and \(\mathbb F_4\) (the last represented as \(\mathbb F_2[t]/(t^2+t+1)\)), including all three regimes. It also independently enumerates all allowed three-dimensional linear maps and tests multiplication and idempotence directly for \(n=1\) over the three prime fields. The run returns `VERIFY_OK_BILINEAR_RETRACTIONS`.

For example with \(q=5\), \(n=2\), the complete nonzero rank counts in generic, split-symmetric, and alternating phases respectively are
\[
 (E_{2,\lambda,0},E_{2,\lambda,1},E_{2,\lambda,2},E_{2,\lambda,5})
 =(1,22500,125000,1),\ (1,22500,187500,1),\ (1,97500,2437500,1).
\]
The enumerations are finite checks, not proofs for all finite fields or all dimensions.

## Relationship to prior work
E. Mainellis, *Associative Algebras with Small Derived Ideal* (arXiv:2212.01425, publicly posted 2022-12-02), classifies extra-special associative algebras as central sums, including the two-generator \(H_2(\lambda)\) blocks, and studies Schur multipliers and capability. The algebra family here is a central sum of such blocks; this structural classification is not new. The inspected full text does not provide the enumeration of idempotent endomorphisms by image rank.

C. P. Anil Kumar and S. S. Pradhan, *On the Endomorphism Semigroups of Extra-special \(p\)-groups and Automorphism Orbits* (arXiv:1908.00331, publicly posted 2019-08-01), count symplectic isotropic spaces in the different setting of extra-special groups. In odd characteristic when \(\lambda=-1\), the associative product is half of its commutator, so the alternating-phase retraction count is the established Heisenberg-Lie case, not a novel special case. The contribution claimed here is the uniform **associative** retraction spectrum, particularly the generic nonsymmetric phase and its Goursat count, plus the precise three-phase comparison.

## Limitations
The results do not classify endomorphisms that are not idempotent, conjugacy orbits of retractions, or arbitrary extra-special associative algebras. The central-sum condition and nonzero parameter matter. General finitary bilinear-form subspace theorems may provide alternative derivations; the literature comparisons establish originality only relative to the specifically inspected sources, and publication priority is not independently certified. The standard alternating formulas overlap known symplectic/Heisenberg counting results.

## References
1. E. Mainellis, *Associative Algebras with Small Derived Ideal* (2022), arXiv:2212.01425, https://arxiv.org/abs/2212.01425.
2. C. P. Anil Kumar and S. S. Pradhan, *On the Endomorphism Semigroups of Extra-special \(p\)-groups and Automorphism Orbits* (2019), arXiv:1908.00331, https://arxiv.org/abs/1908.00331.
