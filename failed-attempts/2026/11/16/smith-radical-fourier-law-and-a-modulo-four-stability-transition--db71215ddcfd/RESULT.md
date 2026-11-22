# Smith-radical Fourier law and a modulo-four stability transition for quadratic cycle graphs

## Finding

**Theorem (general quadratic graph).** Let \(N\ge 2\), \(R=\mathbb Z/N\mathbb Z\), \(d\ge1\), and \(Q:R^d\to R\) be the reduction of an integer homogeneous quadratic polynomial. Let \(A\) be its integral symmetric *polar matrix*, so that
\[
Q(x+h)-Q(x)-Q(h)=x^{\mathsf T}Ah\pmod N.
\]
Identify the dual of \(H=R^{d+1}\) with \(H\), and denote by \(\Pi_Q\) the Fourier projection retaining exactly the characters with frequencies in the graph \(\Gamma_Q=\{(x,Q(x)):x\in R^d\}\). For each \(b\in R\), put \(r_b=|\ker(bA:R^d\to R^d)|\). Then, at every \((a,b)\in H\), the unnormalized Fourier transform of the graph indicator has absolute value either \(0\) or \(N^{d/2}\sqrt{r_b}\); exactly \(N^d/r_b\) values of \(a\) give the latter. Consequently, its convolution rank is
\[
\operatorname{rank}(\mathbf1_{\Gamma_Q}*)=\sum_{b\in R}\frac{N^d}{r_b},
\]
and the sharp endpoint projection norm is
\[
\boxed{\|\Pi_Q\|_{\ell^1\to\ell^1}=\|\Pi_Q\|_{\ell^\infty\to\ell^\infty}=N^{d/2-1}\sum_{b\in R}r_b^{-1/2}.}
\]
This is also the **smallest norm of any projection** onto the same Fourier subspace in either endpoint norm. If \(s_1,\dots,s_d\) are the integer Smith diagonal entries of \(A\), including zeros, then
\[
r_b=\prod_{j=1}^d\gcd(N,bs_j),\qquad\gcd(N,0)=N.
\]
Thus the full Fourier-magnitude distribution and the minimal projection norm are determined by the Smith invariants of the polar matrix, independently of the diagonal quadratic refinement.

**Theorem (quadratic cycles).** For \(n\ge3\), \(k\ge1\), set \(N=2^k\) and \(Q_n(x)=\sum_{i\bmod n}x_i x_{i+1}\) on \(R^n\). Write \(\Pi_{n,k}=\Pi_{Q_n}\) and \(L_{n,k}=\|\Pi_{n,k}\|_{\ell^\infty\to\ell^\infty}\). Then
\[
\boxed{L_{n,k}=\begin{cases}
\displaystyle\frac{N^{n/2}}{2\sqrt2}\sum_{v=0}^{k-1}2^{-v(n/2+1)}+N^{-1},&n\text{ odd},\\[6pt]
\displaystyle\frac{N^{n/2}}4\sum_{v=0}^{k-1}2^{-v(n/2+1)}+N^{-1},&n\equiv2\pmod4,\\[6pt]
\displaystyle\frac{N^{n/2-1}}2\sum_{v=0}^{k-1}2^{-vn/2}+N^{-1},&n\equiv0\pmod4.
\end{cases}}
\]
In particular, for each fixed \(n\), as \(k\to\infty\), the norm has the corresponding sharp asymptotics
\[
L_{n,k}\sim\begin{cases}
\displaystyle\frac{N^{n/2}}{2\sqrt2(1-2^{-n/2-1})},&n\text{ odd},\\[4pt]
\displaystyle\frac{N^{n/2}}{4(1-2^{-n/2-1})},&n\equiv2\pmod4,\\[4pt]
\displaystyle\frac{N^{n/2-1}}{2(1-2^{-n/2})},&n\equiv0\pmod4.
\end{cases}
\]
Hence the modulus-growth exponent drops by **one full power of \(N\)** exactly when \(4\mid n\), a structural transition caused by a two-dimensional integer nullspace of the cycle adjacency matrix.

More explicitly, for any \(b\ne0\) of dyadic valuation \(v\in\{0,\ldots,k-1\}\), the kernel size determining every Fourier-magnitude multiplicity is
\[
r_b=\begin{cases}2^{nv+1},&n\text{ odd},\\2^{nv+2},&n\equiv2\pmod4,\\2^{v(n-2)+2k},&n\equiv0\pmod4.\end{cases}
\]
Exactly \(2^{kn}/r_b\) of the \(a\)-frequencies for this \(b\) are nonzero, with magnitude \(\sqrt{2^{kn}r_b}\). There are exactly \(2^{k-v-1}\) choices of \(b\) having that valuation. For \(b=0\), only \(a=0\) survives and its magnitude is \(N^n\). These rules give the entire Fourier magnitude spectrum and the exact convolution rank at every \((n,k)\).

## Assumptions and scope

All groups are finite and equipped with counting measure for operator norms; Fourier coefficients are **unnormalized**, \(\widehat f(a,b)=\sum_{(x,z)\in H}f(x,z)e^{2\pi i(a\cdot x+bz)/N}\). The normalized convolution kernel of \(\Pi_Q\) is \(N^{-(d+1)}\widehat{\mathbf1}_{\Gamma_Q}\) (up to an irrelevant reflection). The quadratic-cycle coordinates are indexed cyclically; \(n=3\) is the usual triangle with three distinct edges. No assumptions of invertibility of \(A\) or oddness of \(N\) are needed in the general theorem.

## Proof

**1. Magnitudes from the polar radical.** Put \(F_b(a)=\sum_{x\in R^d}e^{2\pi i(a\cdot x+bQ(x))/N}\). Let \(K_b=\ker(bA)\), of size \(r_b\). Replacing one of the two variables in \(|F_b(a)|^2\) by its difference from the other gives
\[
|F_b(a)|^2=N^d\sum_{h\in K_b}e^{2\pi i(a\cdot h+bQ(h))/N}.
\]
On \(K_b\), the function \(h\mapsto bQ(h)\) is additive, since the polar term \(b h^{\mathsf T}Ah'\) vanishes. Thus the final sum is a character sum over \(K_b\), equal either to \(0\) or \(r_b\). Every character of the subgroup \(K_b\) extends to \(R^d\), so precisely \(N^d/r_b\) characters \(a\) cancel the restriction of \(bQ\). This proves the asserted magnitude and multiplicity without a nondegeneracy hypothesis. Summing the nonzero magnitudes over \(a\) gives \(N^{3d/2}/\sqrt{r_b}\).

**2. Sharpness of the projection norm.** The unique translation-invariant projection onto the Fourier subspace for \(\Gamma_Q\) is convolution by \(N^{-(d+1)}\widehat{\mathbf1}_{\Gamma_Q}\). Its two endpoint norms both equal the \(\ell^1\)-mass of this kernel, which, by step 1, is \(N^{d/2-1}\sum_b r_b^{-1/2}\). The lower bound is attained by choosing input phases conjugate to the kernel coefficients in an endpoint row. For any other bounded projection \(P\) onto the same Fourier subspace, averaging its conjugates under all translations does not increase either endpoint norm, preserves the range and the identity action on that range, and produces the unique translation-invariant projection. Hence the displayed norm is minimal among all projections onto this subspace.

**3. Smith formula.** Integral unimodular row and column operations diagonalize \(A\) to \(\operatorname{diag}(s_1,\ldots,s_d)\) and remain invertible modulo every \(N\). On one coordinate, multiplication by \(bs_j\) has exactly \(\gcd(N,bs_j)\) kernel elements. Taking products proves the Smith-radical identity, including \(s_j=0\).

**4. Cycle Smith forms without a spectral assumption.** For \(Q_n\), the polar matrix is the ordinary adjacency matrix of \(C_n\). To determine its integer cokernel, write its defining relations as \(e_{i-1}+e_{i+1}=0\), whence \(e_{i+2}=-e_i\). All generators are therefore determined by \(e_0,e_1\), repeating with period four. The cyclic closure relations yield respectively a free group of rank two if \(n\equiv0\pmod4\), \((\mathbb Z/2\mathbb Z)^2\) if \(n\equiv2\pmod4\), and \(\mathbb Z/2\mathbb Z\) if \(n\) is odd. Thus the Smith diagonals consist of \(n-2\) units and two zeros, \(n-2\) units and two twos, or \(n-1\) units and one two. These are also the three forms obtained by Williams (2014, Corollary 4.4).

**5. Dyadic sum and asymptotics.** For a nonzero \(b\) with \(v_2(b)=v<k\), multiplication by a unit Smith entry has a \(2^v\)-element kernel, by a two has a \(2^{v+1}\)-element kernel, and by a zero has a \(2^k\)-element kernel. These give the three displayed \(r_b\). Since there are \(2^{k-v-1}\) choices of such \(b\), and \(b=0\) contributes \(1/N\) to the endpoint norm, inserting these sizes in step 2 yields each finite geometric sum. Sending \(k\to\infty\) gives the three asymptotic constants by convergence of geometric series. All statements include the boundaries \(n=3\) and \(k=1\).

## Verification

Run `python cycle_quadratic_fourier_check.py` using Python's standard library. The checker enumerates all \((a,b)\)-frequencies and all \(x\) for cycle cases \((n,k)=(3,1),(3,2),(3,3),(4,1),(4,2),(5,1),(6,1),(8,1)\); its cyclotomic-integer basis checks nonzero Fourier magnitudes **exactly**, not numerically. It separately counts adjacency kernels without using Smith forms, checks Parseval, and tests four unrelated quadratic forms at moduli \(2,3,4,5\). The final marker is `CYCLE_QUADRATIC_FOURIER_EXACT_PASS`.

For illustration, the predicted pairs (convolution rank, minimal endpoint projection norm) are \((5,3/2)\) at \((n,k)=(3,1)\), \((69,3/4+2\sqrt2)\) at \((3,2)\), \((1093,67/8+\sqrt2)\) at \((3,3)\), \((37,11/4)\) at \((4,2)\), and \((65,9/2)\) at \((8,1)\). Exact finite verification complements, but does not replace, the all-parameter proof above.

## Relationship to prior work

The polar-radical argument rests on classical character orthogonality for quadratic Gauss sums. Cai, Chen, Lipton, and Lu (arXiv:1005.2632, 2010) give algorithms for evaluating quadratic exponential sums over arbitrary moduli, including dyadic moduli; that prior computational framework is not presented here as a new result. Williams (2014, Corollary 4.4) determines the integer Smith forms of cycle adjacency matrices, which are explicitly credited and independently reconstructed above. Iosevich and Koh (arXiv:0804.4505, 2008) study finite-field quadratic Fourier restriction, principally in odd characteristic, rather than exact dyadic endpoint projection norms. The present combined statement identifies the sharp endpoint projection norms and every frequency-magnitude multiplicity for an infinite two-parameter family, and expresses a general endpoint norm solely through Smith data. No claim of exhaustive historical priority is made.

## Limitations

The three geometric-series formulas apply to the specific homogeneous cycle quadratic forms over dyadic rings; other graph forms require their own Smith data. The general radical law applies to any homogeneous quadratic polynomial on a finite cyclic ring, but it does not cover cubic phases or arbitrary nonlinear frequency sets. There is no assertion about sharp \(\ell^p\) norms for \(1<p<\infty\) other than the standard orthogonal-projection \(\ell^2\) norm. Repeated computation is corroborative and not an independent mathematical audit. An unidentified older equivalent formulation of the projection-norm identity is a residual priority risk.

## References

1. A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505v1, first public 2008-04-28. https://arxiv.org/abs/0804.4505
2. J.-Y. Cai, X. Chen, R. Lipton, and P. Lu, *On Tractable Exponential Sums*, arXiv:1005.2632v1, first public 2010-05-14. https://arxiv.org/abs/1005.2632
3. G. Williams, *Smith forms for adjacency matrices of circulant graphs*, Linear Algebra and its Applications 443 (2014), 21–33, DOI:10.1016/j.laa.2013.11.006; repository deposited 2014-01-07. https://repository.essex.ac.uk/8578/
4. J. Gilbert and Z. Rzeszotnik, *The norm of the Fourier transform on finite abelian groups*, Annales de l'Institut Fourier 60 (2010), 1317–1346, DOI:10.5802/aif.2556. https://www.numdam.org/articles/10.5802/aif.2556/
