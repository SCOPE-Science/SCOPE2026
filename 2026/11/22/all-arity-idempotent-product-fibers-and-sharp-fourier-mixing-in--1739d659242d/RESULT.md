# All-arity idempotent-product fibers and sharp Fourier mixing in character-table Rees semigroups

## Finding

Let \(A\) be any nontrivial finite abelian group of order \(n\) and exponent \(m\), and let \(b:A\times A\to C_m\) be a perfect bicharacter into the cyclic group \(C_m=\langle\omega\rangle\). Form the completely simple Rees matrix semigroup \(S=A\times C_m\times A\) with sandwich matrix \(P_{\lambda i}=b(\lambda,i)\). Its idempotent set consists of the \(n^2\) elements \(e_{i\lambda}=(i,b(\lambda,i)^{-1},\lambda)\).

For every integer \(k\ge2\), every \(i,\lambda\in A\), and every \(v\in\{0,\ldots,m-1\}\), the exact number of **ordered** \(k\)-tuples of idempotents with product \((i,\omega^v b(\lambda,i)^{-1},\lambda)\) equals

\[
F_k(v)=\frac{n^{k-1}}{m}\sum_{r\mid m}|A[m/r]|^{k-1}c_r(v),
\]

where \(A[d]=\{a\in A:da=0\}\) and \(c_r(v)=\sum_{d\mid\gcd(r,v)}d\mu(r/d)\) is the integer Ramanujan sum. In particular, the formula is independent of the endpoint indices. Every element of \(S\) is a product of **exactly two** idempotents, while some elements are not idempotent, so idempotent-product width is exactly two.

If \(k\) independent uniform idempotents are multiplied, their product distribution \(P_k\) tends to uniform on \(S\). More precisely, write the primary decomposition \(A=\bigoplus_p\bigoplus_j C_{p^{a_{pj}}}\), let \(a_p=\max_j a_{pj}\), and \(r_p=\#\{j:a_{pj}=a_p\}\). Set \(B=\min_{p\mid m}p^{r_p}\), \(\rho=B^{-1}\), and \(\mathcal P=\{p\mid m:p^{r_p}=B\}\). There is a number \(0\le\sigma<\rho\), depending only on \(A\), such that

\[
\lVert P_k-U_S\rVert_{\mathrm{TV}}=
\frac{\rho^{k-1}}{2m}\sum_{v=0}^{m-1}
\left|\sum_{p\in\mathcal P}\left(p\mathbf1_{p\mid v}-1\right)\right|
+O_A(\sigma^{k-1}).
\]

The displayed leading coefficient is strictly positive. Hence the exact exponential mixing rate is \(\rho\). Both the full finite-length spectrum and the sharp asymptotic depend on the torsion profile of \(A\), not just its cardinality.

## Assumptions and scope

The group \(A\) is finite, abelian and nontrivial; \(n=|A|\) and \(m=\exp(A)\ge2\). The pairing is bimultiplicative and perfect in both variables, meaning that its induced maps to \(\operatorname{Hom}(A,C_m)\) are isomorphisms. Such pairings exist: if \(A\simeq\bigoplus_j C_{d_j}\) with every \(d_j\mid m\), one may put \(b(\lambda,i)=\omega^{\sum_j(m/d_j)\lambda_j i_j}\). Multiplication in the Rees semigroup is

\[
(i,h,\lambda)(j,t,\mu)=(i,hb(\lambda,j)t,\mu).
\]

An element is called an idempotent if its square equals itself. There is no adjoined zero in \(S\). The group-coordinate exponent \(v\) refers to the normalized coordinate relative to \(e_{i\lambda}\); it is not the unnormalized exponent of an arbitrary Rees representation. All assertions hold for every finite abelian group, without a characteristic restriction. The uniform law \(U_S\) has mass \(1/(n^2m)\) per element.

## Proof

**Idempotents and telescoping.** Squaring gives \((i,h,\lambda)^2=(i,h^2b(\lambda,i),\lambda)\), so idempotence forces \(h=b(\lambda,i)^{-1}\). For \(e_{i_1\lambda_1}\cdots e_{i_k\lambda_k}\), expand the Rees product and divide its group coordinate by \(b(\lambda_k,i_1)^{-1}\). The resulting normalized coordinate is

\[
\prod_{t=1}^{k-1}b(\lambda_t-\lambda_{t+1},i_{t+1}-i_1).
\]

Here additive notation is used for \(A\). Once the endpoints \(i_1=i\) and \(\lambda_k=\lambda\) are fixed, the variables \(a_t=\lambda_t-\lambda_{t+1}\) and \(d_t=i_{t+1}-i_1\), for \(1\le t<k\), range independently and bijectively over \(A^{k-1}\times A^{k-1}\). This is a bijection, not merely an equality of aggregate counts.

**Character diagonalization.** Let \(X=b(a,d)\) for independent uniform \(a,d\in A\), and let \(\chi_j(\omega)=e^{2\pi i j/m}\) for \(j\in\mathbb Z/m\mathbb Z\). Orthogonality in the variable \(d\) yields

\[
\mathbb E\chi_j(X)=\frac{1}{n^2}\sum_{a,d\in A}\chi_j(b(a,d))=\frac{|A[j]|}{n}.
\]

Indeed \(d\mapsto\chi_j(b(a,d))\) is trivial exactly when \(ja=0\), by perfection. The normalized target group coordinate is a product of \(k-1\) independent copies of \(X\). Fourier inversion on \(C_m\) therefore gives

\[
\Pr(\text{normalized coordinate}=\omega^v)=
\frac1m\sum_{j=0}^{m-1}\left(\frac{|A[j]|}{n}\right)^{k-1}e^{-2\pi i jv/m}.
\]

There are \(n^{2(k-1)}\) internal choices for fixed endpoints. Multiplying by this count and grouping the Fourier indices according to their exact additive order \(r=m/\gcd(j,m)\) gives the claimed integer Ramanujan-sum formula. This also proves integrality and nonnegativity independently of the alternating appearance of Ramanujan sums.

**Sharp width.** By perfection and the existence of an element of order \(m\) in \(A\), there exist \(a,d\in A\) for which \(b(a,d)\) is any prescribed element of \(C_m\). Thus every target has a two-idempotent representation, while \(m\ge2\) ensures that not all elements are idempotent.

**Sharp spectral rate.** For each nontrivial character of exact order \(r\), the Fourier eigenvalue is \(|A[m/r]|/n\). Primary decomposition shows that the largest nontrivial eigenvalue equals \(\rho=1/B\). Equality holds exactly for characters of prime order \(p\) with \(p^{r_p}=B\): in the \(p\)-primary part, imposing multiplication by \(m/p\) kills precisely one coordinate layer of each maximal-order cyclic direct summand, while every higher prime-power character and every character involving multiple primes kills strictly more. All other eigenvalues are bounded by a fixed \(\sigma<\rho\). The sum of the \(p-1\) characters of order \(p\), evaluated at \(\omega^v\), is \(p-1\) for \(p\mid v\) and \(-1\) otherwise. Fourier inversion and the elementary inequality \(\left||x+y|-|x|\right|\le|y|\) give the total-variation expansion. The leading coefficient is positive because at \(v=0\) all its summands equal \(p-1>0\).

## Verification

The supplied `verify.py` independently multiplies Rees idempotents in coordinates and compares every normalized group-coordinate fiber at four pairs of distinct endpoints to an integer-only implementation of the Ramanujan formula. It checks six examples, including noncyclic \(2\)-groups, mixed-primary groups and lengths up to four. The program requires only Python's standard library. Run `python verify.py`. A captured output file is included. These finite computations check examples but are **not** used in place of the general proof above.

For instance, for \(A=C_4\oplus C_2\), the fibers of three-idempotent products at fixed endpoints, ordered by normalized exponent \(v=0,1,2,3\), are \((1312,768,1248,768)\). The formula also covers cyclic groups and all other finite abelian groups.

## Relationship to prior work

The classical Rees structure theorem and Graham--Houghton path labels describe completely simple semigroups and the support of their idempotent-generated subsemigroups. Gray's archival work uses these to determine generator ranks. Cross-connection theory recovers the sandwich-matrix structure from categorical data. Research on convolution products of probability measures on completely simple semigroups studies qualitative convergence. The present claim is different: it determines every **finite-length**, **fixed-target** fiber and the exact character-spectrum and sharp mixing coefficient for the canonical character-table sandwich family. Generic Rees multiplication, general group Fourier inversion, and classical convergence are acknowledged inputs, not claimed as discoveries.

## Limitations

The result concerns the canonical family with a perfect abelian bicharacter, not arbitrary sandwich matrices or nonabelian structure groups. The assertion that no earlier equivalent specialized formula has been published is not proved; older literature on completely simple semigroup probability and character pairings may contain a form of this calculation. The limit is in the product length with the finite group fixed; no uniform-in-group limit is asserted. No independent mathematical audit has been performed.

## References

1. R. D. Gray, *The minimal number of generators of a finite semigroup*, arXiv:1307.8280, first publicly posted 2013-07-31. https://arxiv.org/abs/1307.8280
2. P. A. Azeef Muhammed and A. R. Rajan, *Cross-connections of completely simple semigroups*, arXiv:1509.02886, first publicly posted 2015-09-09. https://arxiv.org/abs/1509.02886
3. G. Budzban and G. Högnäs, *Convolution products of probability measures on completely simple semigroups*, accessible author-paper text at https://www.academia.edu/58666746/Convolution_products_of_probability_measures_on_completely_simple_semigroups (publication date not used to establish archival eligibility).
