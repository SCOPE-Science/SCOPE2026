# Sharp penultimate Walsh-dimension geometric signed-product constant for real cubes

## Finding
For an integer \(n\ge 4\), set \(N=2^{n-1}\), \(d=N-1\), \(m=n-1\), and \(q=4/N=2^{3-n}\). For the **real** Banach space \(X=\ell_\infty^{d}\), define the normalized geometric signed-product invariant
\[
Z_n(X)=\sup_{\sum_i\|x_i\|^2>0}\frac{\left(\prod_{\varepsilon\in\{-1,1\}^{n-1}}\left\|x_1+\sum_{i=2}^n\varepsilon_i x_i\right\|\right)^{2/N}}{\sum_{i=1}^n\|x_i\|^2}.
\]
Put
\[
z_n=\frac{(2-q)m}{m+\sqrt{m^2+q(2-q)m}}\in(0,1).
\]
Then the **exact sharp value**, attained by explicit real vectors, is
\[
\boxed{Z_n(\ell_\infty^{2^{n-1}-1})=\frac{m^{q}(m+z_n)^{2-q}}{m+z_n^2}.}
\]
For every positive integer \(d\), \(Z_n(\ell_\infty^d)=n\) if and only if \(d\ge 2^{n-1}\). Thus the displayed formula gives the exact value in the *last* dimension below saturation. Its sharp deficit obeys
\[
\boxed{n-Z_n(\ell_\infty^{2^{n-1}-1})\sim 2^{3-n}\quad(n\to\infty).}
\]
For example, the first new instance, at \(n=4\), has \(d=7\), \(z_4=3\sqrt5-6\), and \(Z_4\approx3.532200615299\), strictly below the saturation value \(4\).

## Assumptions and scope
All spaces and vectors are **real**. The vector count \(n\ge4\) is integral and \(d\) is any positive integer for the saturation assertion, or exactly \(2^{n-1}-1\) for the sharp subthreshold formula. The signs range over all \(2^{n-1}\) sign words with the first coefficient fixed at \(+1\). The exponent \(2/N\), rather than \(1/N\), makes the ratio homogeneous of degree zero and reduces to the classical two-vector Zbăganu product at \(n=2\). Zero factors yield numerator zero. No complex analogue or formula at lower dimensions is asserted.

## Proof
**1. Upper estimate from a sign collision.** Fix arbitrary \(x_1,\dots,x_n\in\ell_\infty^{N-1}\) with positive denominator. Let \(r_i=\|x_i\|_\infty\), \(R=\sum_i r_i\), and \(t=\min_i r_i\). For each of the \(N\) sign words choose a coordinate at which its signed-sum norm is attained. Because there are only \(N-1\) coordinates, two *different* sign words choose the same coordinate. At that coordinate their scalar sums can be written \(A+B\) and \(A-B\), where \(A\) and \(B\) are sums over two **nonempty complementary** subsets of the \(n\) vector indices (the fixed positive first sign guarantees the first subset is nonempty, and distinct words guarantee the second is). Hence
\[
|A+B|\,|A-B|=|A^2-B^2|\le\max\{|A|,|B|\}^2\le (R-t)^2.
\]
Every other signed-sum norm is at most \(R\). With \(q=4/N\), it follows that
\[
\left(\prod_\varepsilon \left\|x_1+\sum_{i=2}^n\varepsilon_i x_i\right\|_\infty\right)^{2/N}\le R^{2-q}(R-t)^q.
\]
The claim also holds when \(t=0\), by the same argument.

**2. Reduction to one scalar.** Relabel so that \(r_n=t\); write \(s=\sum_{i<n}r_i\). By Cauchy–Schwarz,
\[
\sum_i r_i^2\ge s^2/m+t^2.
\]
For \(s>0\), set \(z=mt/s\in[0,1]\), since \(t\) is a minimum. The resulting universal ratio bound is
\[
\frac{R^{2-q}(R-t)^q}{\sum_i r_i^2}\le F_n(z):=\frac{m^q(m+z)^{2-q}}{m+z^2}.
\]
The case \(s=0\) has all \(r_i=0\), excluded by the denominator condition. The derivative of \(\log F_n\) has the sign of
\[
(2-q)m-2mz-qz^2.
\]
This polynomial is strictly decreasing on \([0,1]\), positive at zero and negative at one; its unique zero is precisely \(z_n\). Thus \(F_n(z_n)\) is the sharp upper bound.

**3. Matching configuration.** Index the \(N\) sign rows by \(\varepsilon=(1,\varepsilon_2,\ldots,\varepsilon_n)\). Omit the two rows with \(\varepsilon_2=\cdots=\varepsilon_{n-1}=+1\) and \(\varepsilon_n=\pm1\) from individual coordinate assignments, and instead allocate one shared coordinate \(c_0\) to this pair. There are then \(N-1\) coordinates. Define \(x_i(c_0)=1\) for \(i<n\) and \(x_n(c_0)=0\). For each remaining sign row \(\varepsilon\), allocate its own coordinate \(c_\varepsilon\) and set \(x_i(c_\varepsilon)=\varepsilon_i\) for \(i<n\) and \(x_n(c_\varepsilon)=z_n\varepsilon_n\). The first \(m\) vectors have norm \(1\) and the last norm \(z_n\). Every individually allocated row has signed-sum norm \(m+z_n\). Each of the omitted pair has signed-sum norm **exactly \(m\)** at \(c_0\): at all other coordinates it differs in at least one of the \(m-1\) noninitial signs, and its absolute scalar sum is at most \(m\) because \(0<z_n\le1\). Thus the product has precisely \(N-2\) factors \(m+z_n\) and two factors \(m\), proving equality in the displayed formula.

**4. Exact saturation dimension.** The triangle inequality and \(R^2\le n\sum_i r_i^2\) imply \(Z_n(\ell_\infty^d)\le n\). When \(d\ge N\), assign a separate coordinate to every sign row, with components \(x_i(c_\varepsilon)=\varepsilon_i\); then each signed-sum norm is \(n\), so equality holds. Conversely the supremum is attained in every finite dimension by compactness after normalizing \(\sum_i r_i^2=1\). If equality \(n\) holds, both the Cauchy and product/triangle bounds are equalities; hence all \(r_i\) are equal and strictly positive, and **every** sign word must attain \(\sum r_i\) at some coordinate. Equality in the real scalar triangle inequality requires that coordinate's \(n\) values have exactly that sign pattern up to simultaneous negation. Because the first coefficient is fixed positive, a single coordinate can serve only one of the \(N\) sign words. Thus \(d\ge N\).

**5. Exponential deficit.** With \(q=2^{3-n}\), the root equation gives \(1-z_n=O(q)\). Uniform expansion of the smooth function \(F_n\) near \(z=1\) yields \(F_n(z_n)=F_n(1)+O(q^2)\); here \(F_n(1)=n((n-1)/n)^q\). Consequently
\[
n-F_n(z_n)=q\,n\log\frac{n}{n-1}+O(q^2)=q(1+O(1/n))+O(q^2),
\]
which proves the displayed asymptotic. The \(O(q^2)\) follows, for example, by differentiating \(\log F_n\) twice on \([1/2,1]\), where its second derivative is \(O(1/n)\), and observing \(1-z_n=O(q)\).

## Verification
The accompanying standalone Python 3 program `verify.py` recomputes the unique positive root, constructs all \(2^{n-1}-1\) coordinates of each equality witness for \(4\le n\le8\), explicitly evaluates all sign-word norms, checks the predicted multiplicities, the maximizing polynomial's signs, and compares thousands of deterministic rational random examples against the analytic bound. This is a finite **diagnostic**, not a substitute for the preceding proof. Run `python3 verify.py` from the package directory. No nonstandard Python libraries are required.

## Relationship to prior work
Li, Yin, Wang, Liu and Zhang (2025) study a **different**, three-vector, distance-constrained generalized Zbăganu constant, motivating quantitative geometric-product invariants but not implying the present exact arbitrary-order finite-cube formula. Ifronika, Gunawan and Lindiarny (2026, first public 18 November, **later than the source-date cutoff**) introduce the general higher-order Zbăganu constant, establish comparisons with James and von Neumann–Jordan constants, and compute certain infinite classical-function-space values. Their inspected introduction, theorems and examples do not state the penultimate finite-cube formula or its exponential deficit. An existing exact three-vector (\(n=3\)) calculation for finite real cubes is **not** claimed here; the theorem starts at \(n=4\) and establishes an infinite all-orders dimension-threshold law. The older work on higher-order von Neumann–Jordan constants gives arithmetic-mean estimates, not this geometric-product equality formula.

## Limitations
The formula does not classify every maximizing tuple, and no claim is made for dimensions below \(2^{n-1}-1\) or for complex cubes. A complete exhaustive bibliography is not possible; an equivalent result under an alternative name may exist. The late-November higher-order source is used only for scientific comparison and is **not** the earlier qualifying primary source. 

## References
1. Q. Li, Z. Yin, Y. Wang, Q. Liu and H. Zhang, “A new constant in Banach spaces based on the Zbăganu constant,” *AIMS Mathematics* **10** (2025), 6480–6491, DOI: 10.3934/math.2025296, https://www.aimspress.com/aimspress-data/math/2025/3/PDF/math-10-03-296.pdf (publisher-reported 24 March 2025; alternative SciOpen metadata reports 15 March 2025).
2. Ifronika, H. Gunawan and J. Lindiarny, “The n-th Zbáganu constant,” arXiv:2611.24308v1, https://arxiv.org/abs/2611.24308 (first public 18 November 2026; **comparison only**, after source-date cutoff).
3. M. Ciesielski and R. Płuciennik, “On some modifications of n-th von Neumann–Jordan constant for Banach spaces,” *Banach Journal of Mathematical Analysis* **14** (2020), 1273–1294, DOI: 10.1007/s43037-019-00033-1.
