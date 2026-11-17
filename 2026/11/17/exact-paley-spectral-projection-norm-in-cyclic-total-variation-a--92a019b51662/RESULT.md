# Exact Paley spectral projection norm in cyclic total variation and nonlinear shrinkage instability

## Finding
Let \(p\ge5\) be prime with \(p\equiv1\pmod4\). On real signals indexed by the cyclic group \(G=\mathbb Z/p\mathbb Z\), set
\[
\operatorname{TV}(f)=\sum_{x\in G}|f(x+1)-f(x)|.
\]
Write \(R\) for the nonzero quadratic-residue frequencies and \(P_R\) for the Fourier multiplier that keeps precisely the frequencies in \(R\). Then the **exact sharp seminorm operator constant** is
\[
\boxed{\displaystyle
\sup_{\operatorname{TV}(f)>0}\frac{\operatorname{TV}(P_R f)}{\operatorname{TV}(f)}
=\frac12+\frac{p+1}{4\sqrt p}.}
\tag{1}
\]
Every nonresidue \(d\in G\setminus\{0\}\) supplies a maximizer: take \(f\) to be the indicator of a cyclic arc of length \(d\), represented by the integers \(0,\ldots,d-1\).

A related nonlinear conclusion holds for **orthonormal Fourier radial soft thresholding** \(S_\lambda\), for any fixed \(\lambda>0\), with the mean coefficient left unchanged. Its sharp two-input total-variation Lipschitz constant satisfies
\[
\boxed{\displaystyle
\frac12+\frac{p+1}{4\sqrt p}
\le \operatorname{Lip}_{\operatorname{TV}}(S_\lambda)
\le\sqrt p.}
\tag{2}
\]
The **lower bound is achieved exactly by an explicit pair** (constructed below) for each \(p\) and \(\lambda\). Thus the real periodic Fourier soft-threshold operator, despite its Euclidean nonexpansiveness, has two-input total-variation sensitivity of order \(\sqrt p\) along these primes. Equation (2) does **not** assert an exact value for the nonlinear Lipschitz constant.

## Assumptions and scope
The Fourier transform is unitary:
\[
\widehat f(r)=\frac1{\sqrt p}\sum_{x\in G}f(x)e^{-2\pi i rx/p},
\qquad
f(x)=\frac1{\sqrt p}\sum_{r\in G}\widehat f(r)e^{2\pi i rx/p}.
\]
Let \(\chi\) be the Legendre symbol extended by \(\chi(0)=0\); thus \(R=\{r\ne0:\chi(r)=1\}\). Because \(p\equiv1\pmod4\), \(\chi(-1)=1\), and the multipliers preserve real signals. The mean coefficient is omitted from \(R\). The seminorm is cyclic *edge-sum* total variation, not the maximum-edge Lipschitz seminorm and not the Fourier variation of partial sums.

For \(\lambda>0\), define \(S_\lambda f\) by leaving \(\widehat f(0)\) unchanged and applying
\[
\varphi_\lambda(z)=\begin{cases}(1-\lambda/|z|)z,&|z|>\lambda,\\0,&|z|\le\lambda\end{cases}
\]
to each nonzero Fourier coefficient. This is radial complex soft thresholding, applied to conjugate coefficient pairs, hence a real-output operator. Its \(\operatorname{TV}\) Lipschitz constant is the supremum of \(\operatorname{TV}(S_\lambda f-S_\lambda g)/\operatorname{TV}(f-g)\) over real pairs with nonzero denominator; constants are harmless because the nonzero modes are unchanged by adding constants and the mean is preserved.

## Proof
**1. The zero-sum derivative reduction.** Let \(Df(x)=f(x+1)-f(x)\). The map \(D\) is a linear isomorphism from real signals modulo constants to
\[
H=\{u\in\mathbb R^p:\sum_xu(x)=0\},
\]
and \(\operatorname{TV}(f)=\|Df\|_1\). Since \(D\) and \(P_R\) are translation-invariant, \(DP_R=P_RD\). For any real convolution kernel \(K\) (\(Pu(x)=\sum_y K(x-y)u(y)\)), its induced norm on \((H,\|\cdot\|_1)\) is exactly
\[
\|P\|_{H,1\to1}=\frac12\max_{d\ne0}\sum_x|K(x)-K(x-d)|.
\tag{3}
\]
Indeed every zero-sum real vector of \(\ell^1\)-norm one is a convex combination of signed atoms \((e_i-e_j)/2\): decompose its positive and negative parts, each of mass \(1/2\), into probability vectors and couple them. Formula (3) follows by translation symmetry, and equality is achieved at a maximizing atom.

**2. The Paley kernel.** Fourier inversion and the classical quadratic Gauss sum give the real convolution kernel
\[
K(x)=\frac1p\sum_{r\in R}e^{2\pi irx/p}
=\begin{cases}
\dfrac{p-1}{2p},&x=0,\\[3pt]
\dfrac{-1+\sqrt p\,\chi(x)}{2p},&x\ne0.
\end{cases}
\tag{4}
\]
The only classical input is \(\sum_{a\ne0}\chi(a)e^{2\pi ia/p}=\sqrt p\) for \(p\equiv1\pmod4\), with the stated positive sign convention.

**3. The exact arithmetic shift calculation.** Fix \(d\ne0\). Since \(\chi(-d)=\chi(d)\), the two terms \(x=0,d\) in \(\sum_x|K(x)-K(x-d)|\) together contribute \(1-\chi(d)/\sqrt p\). At the remaining \(p-2\) positions both characters are \(\pm1\), and the kernel difference has modulus \(1/\sqrt p\) precisely when the two Legendre symbols disagree, otherwise zero.

The basic character autocorrelation identity is
\[
\sum_{x\in G}\chi(x)\chi(x-d)=-1\qquad(d\ne0).
\tag{5}
\]
For completeness, replace \(2x-d\) by \(t\); the sum becomes \(\sum_t\chi(t^2-d^2)\). For each fixed nonzero \(a\), the number of pairs \((t,z)\) with \(z^2=t^2-a\) is \(p-1\), since \((t-z)(t+z)=a\) and both factors can be chosen uniquely from any nonzero first factor. Therefore \(\sum_t(1+\chi(t^2-a))=p-1\), proving (5). With the two zero-character positions omitted, (5) says that exactly \((p-1)/2\) remaining positions have unequal symbols. Hence
\[
\sum_x|K(x)-K(x-d)|
=1+\frac{p-1-2\chi(d)}{2\sqrt p}.
\tag{6}
\]
The maximum occurs when \(\chi(d)=-1\). Substitution into (3) proves (1). If \(d\) represents an integer in \(\{1,\ldots,p-1\}\), the arc indicator \(f=\mathbf1_{\{0,\ldots,d-1\}}\) has precisely two cyclic jumps whose difference is a translate (up to sign) of \(e_0-e_d\). It therefore attains (1), not just an asymptotic bound.

**4. Exact nonlinear lower witness.** Fix such an arc \(f\) and choose a real \(h=\varepsilon f\) with \(\varepsilon>0\) small enough that \(|\widehat h(r)|<\lambda\) for all \(r\ne0\). At each \(r\in R\), choose the base Fourier coefficient
\[
\widehat b(r)=2\lambda\frac{\widehat h(r)}{|\widehat h(r)|},
\]
and put \(\widehat b(r)=0\) for \(r\notin R\). No nonzero Fourier coefficient of an arc indicator vanishes, since \(p\) is prime and the geometric-series numerator \(1-e^{-2\pi ird/p}\) is nonzero for \(r,d\ne0\). Because \(-R=R\) and \(h\) is real, \(b\) is real. Radial soft thresholding along the rays defined by \(\widehat h(r)\) now gives an *exact*, not infinitesimal, identity in Fourier space:
\[
S_\lambda(b+h)-S_\lambda(b)=P_Rh+\overline h\,\mathbf1,
\qquad \overline h=\frac1p\sum_xh(x).
\tag{7}
\]
Indeed on \(R\) the radial output difference is exactly \(\widehat h(r)\), outside \(R\cup\{0\}\) both outputs vanish, and at frequency zero the difference is \(\widehat h(0)\). Applying \(D\) and using (1) proves the lower bound in (2), with equality for this pair at the lower-bound value.

**5. Euclidean-to-variation upper bound.** The map \(\varphi_\lambda:\mathbb C\to\mathbb C\) is the Euclidean proximal map of \(\lambda|z|\), hence is nonexpansive. Each Fourier component of \(D\) is multiplication by a fixed complex scalar. Therefore for real \(f,g\), coefficientwise nonexpansivity and Parseval give
\[
\|D(S_\lambda f-S_\lambda g)\|_2
\le\|D(f-g)\|_2.
\]
Consequently Cauchy–Schwarz and \(\|u\|_2\le\|u\|_1\) imply
\[
\operatorname{TV}(S_\lambda f-S_\lambda g)
\le\sqrt p\,\operatorname{TV}(f-g).
\]
This proves (2). The lower bound behaves as \(\sqrt p/4\) and Dirichlet's classical theorem gives infinitely many primes \(p\equiv1\pmod4\), so the order claim follows.

## Verification
Run the standalone standard-library program `python3 artifacts/verify_paley.py`. It enumerates the twenty-one primes \(p\equiv1\pmod4\) from \(5\) through \(197\) and independently computes the Fourier kernel by direct root-of-unity sums, all shift differences, their predicted Legendre-class dependence, the arc maximizer, and an explicit nonlinear soft-threshold witness at threshold one. It compares the nonlinear result modulo constants, because the threshold leaves the mean unchanged. The executed checker returned `EXACT_PALEY_AND_RADIAL_SOFT_THRESHOLD_WITNESS_CHECKS_PASS 21`.

These finite floating-point checks corroborate (1)–(7) but do not prove them beyond the enumerated primes. The infinite-family proof is the preceding zero-sum atomic norm reduction and arithmetic character calculation, together with the direct soft-threshold construction.

## Relationship to prior work
Cohen, Dahmen, Daubechies and DeVore [1] study bounded variation through wavelet coefficient estimates and show the importance of coefficient geometry; their paper does not supply the present finite cyclic Paley projector coefficient. Poon [2] studies recovery of gradient-sparse signals from partial Fourier measurements by *total-variation minimization*, which is not projection onto a prescribed arithmetic frequency set. Chen and Selesnick [3] study group shrinkage for denoising in transformed coordinates; the present operator is the precisely defined radial coefficientwise shrinker and the focus is its two-input graph total-variation sensitivity.

The published exact Fourier-algebra norm of the complete square set on odd prime-power cycles [4] computes a full-space \(\ell^1/\ell^\infty\) multiplier norm (including the zero frequency and nonunit squares), whereas (1) is the norm **on zero-sum derivatives** of a distinct multiplier without the mean. The published sharp harmonic projection constant on finite metric cycles [5] concerns the maximum-edge Lipschitz norm and a single real harmonic pair; (1) treats the *edge-sum* variation norm and an arithmetic half-spectrum. A cubic-residue Fourier projection result [6] computes a full-space endpoint norm for a different frequency subgroup. These are different statements and none of the inspected formulas implies (1) or (2) by simply substituting parameters.

## Limitations
The exact linear norm formula requires real signals, cyclic unweighted edge-sum variation, primes \(p\equiv1\pmod4\), and the **nonzero** quadratic-residue frequency mask. The nonlinear theorem gives a sharp explicit **lower witness** and a dimensionally matching order upper bound, not its exact Lipschitz coefficient. There is no result here for primes \(p\equiv3\pmod4\), asymmetric complex-residue masks, arbitrary composite cyclic groups, or non-cyclic boundary conditions. The Gauss-sum identity and finite-dimensional zero-sum duality are classical; the stated contribution is their exact combination in this variation norm and its nonlinear threshold consequence. Historical uniqueness cannot be guaranteed against unindexed cyclotomic or Paley-multiplier literature. No independent mathematical audit has been performed.

## References
[1] A. Cohen, W. Dahmen, I. Daubechies and R. A. DeVore, *Harmonic Analysis of the space BV*, Revista Matemática Iberoamericana 19 (2003), 235–263, published April 30, 2003, https://doi.org/10.4171/RMI/345.

[2] C. Poon, *On the role of total variation in compressed sensing*, arXiv:1407.5339v1, publicly posted July 20, 2014, https://arxiv.org/abs/1407.5339.

[3] P.-Y. Chen and I. W. Selesnick, *Translation-Invariant Shrinkage/Thresholding of Group Sparse Signals*, arXiv:1304.0035v1, publicly posted March 29, 2013, https://arxiv.org/abs/1304.0035.

[4] *Exact Fourier-algebra norm of the complete square set on odd prime-power cyclic groups*, public research result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-fourier-algebra-norm-of-the-complete-square-set-on-odd-pri--c42daa360e08.

[5] *Sharp harmonic projection constants on finite metric cycles*, public research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-harmonic-projection-constants-on-finite-metric-cycles--616f4adc601f.

[6] *Exact cubic-residue Lebesgue constants from Gaussian period arithmetic*, public research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-cubic-residue-lebesgue-constants-from-gaussian-period-arit--36f40db19f8d.

[7] B. C. Berndt, R. J. Evans and K. S. Williams, *Gauss and Jacobi Sums*, Wiley, 1998, Chapter 1 (classical quadratic Gauss-sum identity).
