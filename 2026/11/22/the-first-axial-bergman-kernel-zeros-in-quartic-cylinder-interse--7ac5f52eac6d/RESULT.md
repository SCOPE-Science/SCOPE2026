# The first axial Bergman-kernel zeros in quartic-cylinder intersections occur with nine fibres

## Finding
For each integer \(m\ge1\), consider the bounded complete Reinhardt domain
\[
\Omega_m=\{(z,w_1,\ldots,w_m)\in\mathbb C^{m+1}: |z|^4+|w_j|^2<1\text{ for }1\le j\le m\}.
\]
Let \(K_m\) be its unweighted Bergman reproducing kernel with Euclidean volume measure. For \(|z|,|\zeta|<1\), restrict both arguments to the central axis and write \(s=z\overline\zeta\). Then the **first axial failure of the Lu Qi-Keng property in this family** occurs at exactly nine quadratic cylinder fibres:

- For every integer \(1\le m\le8\), \(K_m((z,0),(\zeta,0))\ne0\) for all such pairs.
- For \(m=9\), the axial kernel has exactly two attainable zero products \(s\), counted with multiplicity. They are a simple nonreal conjugate pair, numerically
\[
 s_\pm\simeq0.5748056806982\pm0.8125137259860\,i,
 \qquad |s_\pm|\simeq0.995278918434<1.
\]
Consequently the ten-complex-dimensional domain \(\Omega_9\) is not Lu Qi-Keng. No assertion about zero-freeness away from the axis for \(m\le8\), or about \(m\ge10\), is made.

More precisely, let
\[
 A_m(n)=\prod_{j=0}^{m}(n+2j+1),\qquad
 Q_m(s)=\sum_{j=0}^{m}\left[\sum_{k=0}^j(-1)^{j-k}\binom{m+2}{j-k}A_m(k)\right]s^j.
\]
Then
\[
 K_m((z,0),(\zeta,0))=\frac{Q_m(s)}{\pi^{m+1}2^m m!(1-s)^{m+2}}.
\]
In particular, the explicit degree-nine numerator is
\[
\begin{aligned}
Q_9(s)={}&654729075-3486128625s+8884606500s^2\\
&-14023894500s^3+14939174250s^4-11039178150s^5\\
&+5618913300s^6-1889187300s^7+379053675s^8-34459425s^9.
\end{aligned}
\]
The polynomial formula and the exact right-half-plane counts below are reproducible without external computer-algebra packages.

## Assumptions and scope
The family uses **unweighted volume** in the entire domain, not a weighted Bergman space introduced independently. For \(m\ge1\), each variable \(w_j\) is a single complex coordinate and the central axis is \((z,0,\ldots,0)\). The product \(s=z\overline\zeta\) can attain every point of the unit disk: for any \(|s|<1\), take \(|z|=|\zeta|=\sqrt{|s|}\) and choose the relative arguments appropriately. Thus zeros of the displayed one-variable kernel in \(|s|<1\) are actual zeros of the full Bergman kernel, while their absence controls only the axial restriction.

The integer \(m=0\) appears in the supplied checker solely as the auxiliary ordinary-disk generating-function base case; it is not defined by an empty system of cylinder inequalities and is not used in the first-fibre assertion.

## Proof
The slice at any fixed \(z\) has Cartesian product volume \(\pi^m(1-|z|^4)^m\). Holomorphic monomials in the complete Reinhardt domain form an orthogonal basis. All basis elements involving a positive power of any \(w_j\) vanish when both points are on the central axis. Direct beta integration gives the exact monomial norms:
\[
\begin{aligned}
\|z^n\|_{A^2(\Omega_m)}^2
 &=2\pi^{m+1}\int_0^1 r^{2n+1}(1-r^4)^m\,dr\\
 &=\frac{\pi^{m+1}}2 B\bigl((n+1)/2,m+1\bigr)\\
 &=\frac{\pi^{m+1}2^m m!}{\prod_{j=0}^m(n+2j+1)}.
\end{aligned}
\]
Therefore the axial kernel is \(\bigl(\pi^{m+1}2^m m!\bigr)^{-1}\sum_{n\ge0}A_m(n)s^n\). Since \(A_m(n)\) is a polynomial of degree \(m+1\) in \(n\), its generating function has the form \(Q_m(s)/(1-s)^{m+2}\), with numerator coefficients obtained by multiplication by \((1-s)^{m+2}\). This proves the stated exact kernel formula.

For the zero count, define the real polynomial
\[
 R_m(u)=(1+u)^m Q_m\left(\frac{1-u}{1+u}\right).
\]
The Möbius map \(u=(1-s)/(1+s)\) takes \(|s|<1\) bijectively to \(\operatorname{Re}u>0\). The numerator has degree exactly \(m\), and the leading coefficient of \(R_m\) is nonzero, so no root is lost at \(s=-1\). Its constant coefficient is nonzero, so \(s=1\) is not a zero either. Imaginary-axis roots are excluded exactly: substitute \(u=it\), split the real polynomial into its even and odd parts, and use the rational Euclidean algorithm to verify they have no common real-root parameter. In fact their polynomial gcd is a nonzero constant for every \(1\le m\le9\). The supplied checker performs these integer/rational computations and then executes the ordinary Routh array with rational arithmetic and without zero pivots or zero rows.

For \(m=1,\ldots,8\), all the Routh first-column entries are positive, so the right-half-plane root count is zero in every case. For \(m=9\), their signs are precisely \(+++++++-++\), giving exactly two sign changes and hence exactly two right-half-plane roots, counted with multiplicity. No numerical root-finding enters this count. To identify their type, note that the coefficients of every \(Q_m\) alternate strictly in sign for \(0\le m\le9\), as checked exactly. For negative real \(s\) in the disk, \(Q_m(s)>0\) term-by-term, and for positive real \(s\) in the disk, the strictly positive generating series \(Q_m(s)/(1-s)^{m+2}\) implies \(Q_m(s)>0\). Thus the two \(m=9\) disk roots are nonreal. Real coefficients make them a conjugate pair; a total multiplicity of two forces both to be simple. This completes the classification for the ten integer fibre counts in scope.

## Verification
Run the self-contained Python 3 standard-library script `verify.py`, delivered with this result. It recomputes every \(Q_m\) for \(0\le m\le9\), checks the rational generating-function coefficient identities, computes every Cayley polynomial \(R_m\), proves absence of imaginary-axis roots with exact polynomial gcds, and applies exact-fraction Routh arrays. Its expected interior counts for \(m=1,\ldots,9\) are \(0,0,0,0,0,0,0,0,2\), with sign strings recorded in the script. It also checks every displayed coefficient of \(Q_9\). The approximate two complex zeros above are explanatory only, not used as certification.

## Relationship to prior work
Perälä's *Vanishing Bergman kernels on the disk* (first public arXiv version 17 March 2017) develops zero-producing radial Bergman weights and the finite-zero perspective; it does not state the nine-fibre threshold for this specific quartic-cylinder intersection. Beberok's 2016 preprint on Bergman kernels for intersections of complex ellipsoids treats other exponent patterns and develops related kernel and Lu Qi-Keng techniques. Park's 2021 paper gives general Lauricella and monomial formulas for higher-dimensional intersections of cylinders, **including the geometric family considered here**; those formulas imply the initial axial series after specialization. The present contribution is the exact integer threshold through nine fibres, the strict ten-case zero census, and the exact symbolic root-count certificate, rather than the existence of a general formula. Accessible indexed sections of Park's paper did not state this threshold; its complete publisher PDF was not accessible for a final text-wide exclusion. Thus historical priority is a best-knowledge assessment, not a formal uniqueness assertion.

## Limitations
This is an axial, not a full-domain, zero classification. The integer range \(1\le m\le9\) is exhaustive **within that stated range only**, and the result does not extrapolate a later-dimensional zero count. The approximate root locations do not provide proof of the sharp threshold; exact integer/rational arithmetic plus the Routh–Hurwitz theorem provide that proof. The full text of one highly relevant general-cylinder paper was not obtainable despite its indexed sections being accessible. Independent mathematical validation has not been performed.

## References
1. A. Perälä, *Vanishing Bergman kernels on the disk*, arXiv:1703.05976v1 (17 March 2017), https://arxiv.org/abs/1703.05976.
2. T. Beberok, *The Bergman kernel: explicit formulas, deflation, Lu Qi-Keng problem and Jacobi Polynomials*, arXiv:1601.02989v1 (12 January 2016), https://arxiv.org/abs/1601.02989.
3. J.-D. Park, *The Bergman kernel function for intersections of some cylindrical domains and Lauricella's hypergeometric function*, Journal of Mathematical Analysis and Applications 504 (2021), 125398, https://doi.org/10.1016/j.jmaa.2021.125398.
4. Classical Routh–Hurwitz theorem on right-half-plane zeros of real polynomials; its exact rational application is provided in `verify.py`.
