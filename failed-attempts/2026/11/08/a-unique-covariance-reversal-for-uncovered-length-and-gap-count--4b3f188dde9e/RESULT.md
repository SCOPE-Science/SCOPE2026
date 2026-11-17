# A unique covariance reversal for uncovered length and gap count in random circle covering

## Finding
Let \(n\ge2\) and let \(n\) points be chosen independently and uniformly on a circle of circumference one. At each point start a clockwise arc of length \(a\), with \(0<a<1\). Denote by \(U_{n,a}\) the total uncovered length and by \(G_{n,a}\) the number of connected uncovered arcs. Then
\[
\operatorname{Cov}(U_{n,a},G_{n,a})
=(1-a)^n+(n-1)(1-2a)_+^n-n(1-a)^{2n-1},
\]
where \((t)_+=\max(t,0)\). For \(n=2\), the covariance is strictly negative on \(0<a<1/2\), zero at \(a=1/2\), and strictly positive on \(1/2<a<1\). For every \(n\ge3\), there exists exactly one \(a_n\in(0,1/2)\) at which the covariance vanishes; it is negative below \(a_n\) and positive above it. If \(c_*>0\) is the unique positive solution of \(e^c=1+c+c^2\), then
\[
n a_n\longrightarrow c_*=1.7932821329007556\ldots.
\]
More precisely, for every fixed \(c>0\),
\[
\lim_{n\to\infty}\operatorname{Cov}(U_{n,c/n},G_{n,c/n})
=e^{-2c}(e^c-1-c-c^2).
\]
The covariance in this last display is not normalized by \(n\): it has a finite, generally nonzero limit.

## Assumptions and scope
The points are independent, continuous and uniform; the circle has total length one, arc lengths are all identical and deterministic, and arcs run in one common orientation. There is no conditioning on the number of gaps or on complete coverage. The statement concerns finite \(n\ge2\) and \(0<a<1\). An uncovered component of zero length is not counted; coincident and exactly touching endpoints have probability zero. If \(X_1,\ldots,X_n\) are the clockwise spacings between ordered point locations, their joint law is \(\operatorname{Dirichlet}(1,\ldots,1)\). Consequently,
\[
U_{n,a}=\sum_{i=1}^n(X_i-a)_+,
\qquad
G_{n,a}=\sum_{i=1}^n\mathbf1_{\{X_i>a\}}.
\]
The result is an exact dependence statement about two distinct measures of coverage failure, not a claim about an entire joint distribution or arbitrary nonuniform arc placement.

## Proof
The uniform-simplex spacing law implies, for distinct indices and nonnegative \(s,t\),
\[
\Pr(X_i>s)=(1-s)_+^{n-1},\qquad
\Pr(X_i>s,X_j>t)=(1-s-t)_+^{n-1}.
\]
The second identity follows by translating two simplex coordinates; it also holds for \(n=2\) by uniformity on a line segment. From the layer-cake identity \((x-a)_+=\int_a^1\mathbf1_{\{x>t\}}\,dt\),
\[
\mathbb EU_{n,a}=n\int_a^1(1-t)^{n-1}\,dt=(1-a)^n,
\qquad
\mathbb EG_{n,a}=n(1-a)^{n-1}.
\]
Separating the terms with equal and unequal spacing indices gives
\[
\begin{aligned}
\mathbb E(U_{n,a}G_{n,a})
&=n\int_a^1(1-t)^{n-1}\,dt
 +n(n-1)\int_a^1(1-t-a)_+^{n-1}\,dt\\
&=(1-a)^n+(n-1)(1-2a)_+^n.
\end{aligned}
\]
Subtracting the product of means proves the covariance identity without an approximation.

For \(0<a<1/2\), put \(w=a/(1-a)\in(0,1)\). Dividing the covariance by \((1-a)^n>0\) yields
\[
g_n(w)=1+(n-1)(1-w)^n-n(1+w)^{-(n-1)}.
\]
A derivative calculation gives
\[
\frac{g_n'(w)}{n(n-1)}=(1+w)^{-n}-(1-w)^{n-1}.
\]
Let \(h_n(w)=(1-w)^{n-1}(1+w)^n\). Then \(g_n'(w)\) has the opposite sign from \(h_n(w)-1\), while
\[
\frac{d}{dw}\log h_n(w)=\frac{1-(2n-1)w}{1-w^2}.
\]
Thus \(h_n(0)=1\), it first strictly increases, then strictly decreases to zero, and it crosses level one at exactly one interior point. It follows that \(g_n\) strictly decreases from \(g_n(0)=0\), and then strictly increases. Since \(g_n(1)=1-n/2^{n-1}\) is zero for \(n=2\) and strictly positive for \(n\ge3\), the claimed zero classification on \(0<a<1/2\) follows. For \(1/2\le a<1\), the covariance equals
\[
(1-a)^n[1-n(1-a)^{n-1}],
\]
which is strictly positive for \(a>1/2\), and at \(a=1/2\) is positive when \(n\ge3\) and zero when \(n=2\). There are no other zeros.

Finally, with fixed \(c>0\) and \(a=c/n\), Taylor expansion of the three powers, keeping their first-order corrections after cancellation of terms of order \(n\), gives
\[
(1-c/n)^n+(n-1)(1-2c/n)^n-n(1-c/n)^{2n-1}
\longrightarrow e^{-2c}(e^c-1-c-c^2).
\]
The function \(f(c)=e^c-1-c-c^2\) has \(f(0)=f'(0)=0\), \(f''(c)=e^c-2\), is negative just to the right of zero and tends to infinity. Its derivative decreases initially then increases, so \(f\) has exactly one positive zero \(c_*\); its sign is negative below and positive above that zero. Using the already established unique finite-\(n\) sign change, for any \(0<c_-<c_*<c_+\) the limiting signs imply \(c_-/n<a_n<c_+/n\) for all large \(n\). Hence \(n a_n\to c_*\).

## Verification
The standalone `checker.py` calculates the covariance independently by expanding and integrating the uniform-simplex bivariate density using exact rational arithmetic and compares it with the closed formula for \(n=2,\ldots,19\) at rational lengths. It also checks exact finite grids for the sign pattern and the derivative characterization, and numerical convergence of the sparse scaling. It completed 5,657 assertions. These tests are corroborative; the preceding calculus and simplex identities, not finite computation, establish the all-\(n\) conclusions. Run using `python3 checker.py` from the extracted artifact directory; only the standard library is required.

## Relationship to prior work
Classical circle-covering work gives the distribution of uncovered-gap counts and the moments or limiting distribution of total covered length. Moriarty, Marchesi and Metcalfe (2007) develop error bounds for the gap-count distribution and state its exact expectation, but do not derive the mixed covariance or a unique sign threshold in the inspected main article. Siegel (1978) treats marginal coverage moments. Holst and Hüsler (1984) explicitly study joint limit distributions of the number of gaps and uncovered proportion; only their accessible abstract was inspected, so possible implicit asymptotic covariance coverage is a substantive unresolved historical-priority issue. The present finite-\(n\) uniqueness theorem does not follow merely from convergence of a joint limiting law. The classic simplex exceedance identities give the displayed mixed moment, but neither their existence nor a search miss proves the one-crossing theorem new in all literature.

## Limitations
No extension is asserted to random arc lengths, nonuniform start positions, dependent starts, or higher-dimensional coverage. The finite result is exact but has not undergone independent review. The full 1984 Holst–Hüsler text could not be obtained for claim-level checking. Known moment and joint-limit techniques may contain the asymptotic formula implicitly; an independent literature comparison remains important. In the large-\(n\) statement \(c>0\) is fixed; no uniformity in growing \(c\) is claimed.

## References
1. J. Moriarty, J. R. Marchesi and A. Metcalfe, “Bounds on the distribution of the number of gaps when circles and lines are covered by fragments: Theory and practical application to genomic and metagenomic projects,” *BMC Bioinformatics* **8** (2007), article 70, published 2007-03-02. https://pmc.ncbi.nlm.nih.gov/articles/PMC1821341/
2. L. Holst and J. Hüsler, “On the random coverage of the circle,” *Journal of Applied Probability* **21** (1984), 558–566. https://doi.org/10.2307/3213617
3. A. F. Siegel, “Random arcs on the circle,” *Journal of Applied Probability* **15** (1978), 774–789. https://doi.org/10.2307/3213433
4. W. L. Stevens, “Solution to a geometrical problem in probability,” *Annals of Eugenics* **9** (1939), 315–320. https://doi.org/10.1111/j.1469-1809.1939.tb02216.x
