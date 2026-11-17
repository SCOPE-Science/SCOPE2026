# Sharp extension costs and rigidity of finite Walsh coefficient maps

## Finding
Let \((\Omega,\mathbb P)=\{-1,1\}^{\mathbb N}\) with the fair product law and let \(r_j(\omega)=\omega_j\). Fix an integer \(n\ge2\). Write \(R_n=\operatorname{span}\{r_1,\dots,r_n\}\subset L^1(\Omega)\) and, for every \(1\le p\le\infty\), define the coefficient operator
\[
Q_{n,p}\Big(\sum_{j=1}^n a_jr_j\Big)=(a_1,\dots,a_n)\in\ell_p^n.
\]
Every bounded linear extension \(F:L^1(\Omega)\to\ell_p^n\) of \(Q_{n,p}\) satisfies
\[
\|F\|\ge n^{1/p},\qquad n^{1/\infty}:=1,
\]
and equality is attained by \(F_0f=(\mathbb E(fr_j))_{j=1}^n\). Among extensions, this minimizer is **unique for every \(1<p\le\infty\)**, whereas for \(p=1\) there is a nonconstant interval of distinct norm-minimizing extensions.

The norm and relative extension factor \(\mathcal E_{n,p}:=\inf_{F|_{R_n}=Q_{n,p}}\|F\|/\|Q_{n,p}\|\) are explicitly
\[
\begin{array}{c|c|c}
\text{exponent}&\|Q_{n,p}\|&\mathcal E_{n,p}\\hline
p=1&n/\mathbb E|S_n|&\mathbb E|S_n|\
2\le p\le\infty&2^{1/p}&(n/2)^{1/p}
\end{array}
\quad\text{where }S_n=\sum_{j=1}^n r_j.
\]
Here
\[
\mathbb E|S_n|=\frac{n}{2^{n-1}}\binom{n-1}{\lfloor(n-1)/2\rfloor}\sim\sqrt{\frac{2n}{\pi}}.
\]
For the remaining range \(1<p<2\), the sharp operator-extension numerator remains \(n^{1/p}\), and the certified relative lower bound is \(\mathcal E_{n,p}\ge\sqrt{n/2}\); an exact formula for the denominator is not asserted here. Hence the inclusion of the closed Rademacher span into \(L^1\) fails the finite-exponent operator-extension property for every \(1\le p<\infty\).

There is also a sharp stability identity at \(p=2\). Write any extension \(Ff=\mathbb E(fg)\) with \(g\in L^\infty(\Omega;\mathbb R^n)\). Then
\[
\mathbb E\|g-r\|_2^2=\mathbb E\|g\|_2^2-n\le\|F\|^2-n,
\qquad r=(r_1,\dots,r_n).
\]
For every \(C\ge\sqrt n\), an extension of norm exactly \(C\) attains equality.

## Assumptions and scope
All spaces and operators in the main statement are **real**. Probability measure is complete if desired (completion does not affect the conclusions). The functions \(r_j\) are independent equiprobable signs. Vector-valued integrals are ordinary Bochner integrals in finite dimensions; operator norms are induced by \(L^1\) and the target \(\ell_p\) norms. For \(p=\infty\), the convention is \(n^{1/p}=2^{1/p}=1\).

## Proof
**Step 1 (universal extension lower bound).** For every \(F:L^1(\Omega)\to\ell_p^n\), each coordinate functional on \(L^1\) is represented by an essentially bounded scalar \(g_i\). Thus \(Ff=\mathbb E(fg)\) with \(g=(g_i)\) and \(\|F\|=\operatorname{ess\,sup}\|g(\omega)\|_p\). The interpolation conditions \(F(r_j)=e_j\) read \(\mathbb E(g_i r_j)=\delta_{ij}\); taking traces gives
\[
 n=\mathbb E\Big[\sum_{j=1}^n r_j g_j\Big]
\le n^{1/p'}\operatorname{ess\,sup}\|g\|_p.
\]
The coefficient extension \(g=r\) attains \(\|F_0\|=n^{1/p}\). This argument works equally for any finite orthonormal family of functions taking values in \(\{-1,1\}\), with no independence assumption.

**Step 2 (all equality cases).** For \(1<p<\infty\), equality in the pointwise \(\ell_p\)-\(\ell_{p'}\) Holder inequality with the fixed sign vector \(r\) and the integral trace forces \(g=r\) almost everywhere; strict convexity gives equality of every coordinate, not merely of the sum. At \(p=\infty\), each scalar \(r_jg_j\le1\) pointwise and their expectations equal one, so again \(g_j=r_j\) almost everywhere. For \(p=1\), choose any \(\varepsilon\in[-1,1]\), replace the first two entries of \(g=r\) by
\[
 g_1=r_1+\varepsilon,\qquad g_2=r_2-\varepsilon r_1r_2,
\]
and leave the other entries unchanged. Independence makes all cross-moments unchanged, while \(|g_1|+|g_2|=2\) everywhere. These are distinct extensions of the minimum norm \(n\) for \(\varepsilon\ne0\).

**Step 3 (original operator norm).** For real \(a=(a_j)\), the optimal real Khintchine inequality at exponent one and conditional Jensen give
\[
\mathbb E\big|\sum a_jr_j\big|\ge\max\{\|a\|_2/\sqrt2,\|a\|_\infty\}.
\]
For \(2\le p<\infty\), use \(\|a\|_p\le\|a\|_2^{2/p}\|a\|_\infty^{1-2/p}\). The preceding two lower bounds imply
\[
\mathbb E\big|\sum a_jr_j\big|\ge2^{-1/p}\|a\|_p.
\]
Equality holds when exactly two coefficients are equal and nonzero, since then \(\mathbb E|a_1r_1+a_2r_2|=|a_1|\). The \(p=\infty\) case follows directly from the conditional Jensen bound, with a coordinate vector attaining equality. This proves \(\|Q_{n,p}\|=2^{1/p}\) for \(p\ge2\).

At \(p=1\), by sign invariance assume \(a_j\ge0\) and \(\sum a_j=1\). The convex symmetric function \(a\mapsto\mathbb E|\sum a_jr_j|\) is minimized, by averaging over coordinate permutations, at the uniform vector. Thus its minimum is \(\mathbb E|S_n|/n\), attained there. Direct binomial summation gives
\[
\mathbb E|S_n|=\frac{n}{2^{n-1}}\binom{n-1}{\lfloor(n-1)/2\rfloor};
\]
Stirling's formula gives the displayed asymptotic. For \(1<p<2\), \(\|a\|_2\ge n^{1/2-1/p}\|a\|_p\), so Khintchine yields \(\|Q_{n,p}\|\le\sqrt2 n^{1/p-1/2}\), hence \(\mathcal E_{n,p}\ge\sqrt{n/2}\). Together, these imply lack of a uniform POE-\(p\) constant in every finite exponent by using the first \(n\) coordinate probes in the infinite Rademacher span.

**Step 4 (sharp Hilbert stability).** The moment equations imply \(\mathbb E\langle g,r\rangle=n\), and \(\mathbb E\|r\|_2^2=n\), proving the exact Pythagorean identity in the finding. Conversely, for \(C\ge\sqrt n\), put
\[
 c=\sqrt{(C^2-n)/2},\quad v=(r_2,-r_1,0,\dots,0),\quad g=r+c\,r_{n+1}v.
\]
Independence of \(r_{n+1}\) guarantees all required moments, and pointwise \(\langle r,v\rangle=0\), \(\|v\|_2^2=2\). Hence \(\|g\|_2=C\) everywhere and \(\mathbb E\|g-r\|_2^2=C^2-n\). The stability constant is therefore sharp for every admissible \(C\), not just asymptotically.

## Verification
The proof of the universal extension lower bound is an exact duality argument; the optimal coefficient norms use the sharp scalar real Khintchine constant \(1/\sqrt2\) and a convex-symmetrization argument. Explicit sign enumeration for \(2\le n\le9\) agrees with the binomial formula for \(\mathbb E|S_n|\). Random finite-coefficient checks for \(2\le n\le7\) and several \(p\ge2\) agree with the predicted sharp bound. These computations are diagnostic only; none is used to infer the infinite-dimensional conclusion.

## Relationship to prior work
Pariente-Martín and Tradacete's 2026 theorem identifies finite-exponent order continuity of induced free-lattice embeddings with the uniform operator extension property POE-\(p\), and their introduction notes that the Rademacher span inside \(L^1\) fails such extension in the relevant settings. The present result does **not** reassert that qualitative obstruction as new. It computes exact costs for natural finite-dimensional coefficient probes, classifies minimum-norm extensions at all target exponents, and obtains a sharp global Hilbert stability identity. Haagerup's sharp Khintchine constant is essential previously known input. Lewicki and Micek's Fourier-type projection theory concerns extension problems with the range norm inherited from an \(L^1\) subspace; that is not the fixed coefficient target \(\ell_p^n\) considered here. Its general minimal-extension methods are a relevant antecedent.

## Limitations
The denominator \(\|Q_{n,p}\|\) is not evaluated exactly for \(1<p<2\); only a dimension-sharp-order lower bound on the relative extension factor is proved. The theorem concerns real first-level Rademacher coefficients and, for the universal minimization statement, real unimodular orthonormal systems. No optimal constants for arbitrary operators on the Rademacher span are claimed. A logically equivalent presentation of these particular finite coefficient-probe constants under earlier Fourier-projection terminology cannot be excluded solely by the sources inspected. No independent verification is claimed.

## References
1. R. E. Pariente-Martín and P. Tradacete, *Order continuity of induced homomorphisms between free Banach lattices*, arXiv:2611.00451v1, first submitted 2026-10-30, especially Theorem 1.3 and Introduction. https://arxiv.org/html/2611.00451v1
2. U. Haagerup, *The best constants in the Khintchine inequality*, Studia Mathematica **70** (1981), 231–283, DOI:10.4064/sm-70-3-231-283.
3. G. Lewicki and A. Micek, *Uniqueness of minimal Fourier-type extensions in* \(L^1\)*-spaces*, Monatshefte für Mathematik **170** (2013), 161–178, DOI:10.1007/s00605-012-0468-8.
4. L. Mezrag, *On the* \(L_1^{2n}\)*-extension properties*, Quaestiones Mathematicae **27** (2004), 297–309, DOI:10.2989/16073600409486101 (abstract-level comparison only).
