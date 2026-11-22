# A Gaussian law for degree agreement across independent Cayley trees

## Finding
For every fixed integer \(r\ge2\), let \(T_1,\ldots,T_r\) be independent uniform unrooted labelled trees on \([n]=\{1,\ldots,n\}\), \(n\ge2\). Define
\[
X_{n,r}=\sum_{v=1}^n \mathbf1\{\deg_{T_1}(v)=\cdots=\deg_{T_r}(v)\}.
\]
There is an exact finite probability generating function, stated below. Let
\[
\rho_r=e^{-r}\sum_{k\ge0}\frac1{(k!)^r},\qquad
\eta_r=e^{-r}\sum_{k\ge0}\frac{k}{(k!)^r},\qquad
\sigma_r^2=\rho_r(1-\rho_r)-r(\eta_r-\rho_r)^2.
\]
Then \(0<\sigma_r^2<\rho_r(1-\rho_r)\), and as \(n\to\infty\),
\[
\frac{X_{n,r}-n\rho_r}{\sqrt n}\ \Rightarrow\ N(0,\sigma_r^2),\qquad
\frac{\operatorname{Var}(X_{n,r})}{n}\longrightarrow\sigma_r^2.
\]
For distinct labels \(u\ne v\), their degree-agreement indicators satisfy
\[
n\operatorname{Cov}\bigl(\mathbf1\{\text{degrees agree at }u\},\mathbf1\{\text{degrees agree at }v\}\bigr)
\longrightarrow -r(\eta_r-\rho_r)^2<0.
\]
For two trees, \(\rho_2=e^{-2}I_0(2)\approx0.3085083226\) and \(\sigma_2^2\approx0.1959439028\), where \(I_j\) is the modified Bessel function.

## Assumptions and scope
All trees are sampled independently and uniformly from the \(n^{n-2}\) Cayley trees on the same fixed labels; degrees are unrooted. The number \(r\) is fixed while \(n\to\infty\); no claim is made for \(r\) increasing with \(n\). The label agreement events are distinct from agreement of edge sets or of unlabelled degree histograms. Let \(m=n-2\). Write \([x_1^m\cdots x_r^m]F\) for a multivariate coefficient, with \(z\) an indeterminate. The exact full probability generating function is
\[
\mathbb E z^{X_{n,r}}=\frac{(m!)^r}{n^{rm}}[x_1^m\cdots x_r^m]
\left(e^{x_1+\cdots+x_r}+(z-1)\sum_{k\ge0}\frac{(x_1\cdots x_r)^k}{(k!)^r}\right)^n.
\]
Only finitely many terms can contribute to the displayed coefficient.

## Proof
**Prüfer encoding and exact formulas.** The Prüfer word of each tree is a uniform word of length \(m\) over \([n]\), and vertex degree equals one plus the number of occurrences of its label. The \(r\) independent words have independent multinomial occupancy vectors, each with \(m\) balls and \(n\) boxes. For one label, the coefficient weight is \(\prod_{j=1}^r1/k_j!\), multiplied by \(z\) precisely when all \(k_j\) agree. Its exponential generating function equals the factor in the displayed expression; taking the product over \(n\) labels and extracting all row totals yields the full pgf.

For a fixed vertex and fixed distinct pair, respectively, put
\[
a_n(k)=\binom{m}{k}\left(\frac1n\right)^k\left(1-\frac1n\right)^{m-k},
\qquad
b_n(a,b)=\frac{m!}{a!b!(m-a-b)!}\left(\frac1n\right)^{a+b}
\left(1-\frac2n\right)^{m-a-b}.
\]
The convention is that \(b_n(a,b)=0\) when \(a+b>m\). Independence among tree copies gives the exact finite quantities
\[
p_{n,r}=\sum_{k=0}^{m}a_n(k)^r,\qquad
q_{n,r}=\sum_{a+b\le m}b_n(a,b)^r,
\]
\[
\mathbb E X_{n,r}=np_{n,r},\quad
\operatorname{Var}(X_{n,r})=np_{n,r}(1-p_{n,r})+n(n-1)(q_{n,r}-p_{n,r}^2).
\]

**Limit and covariance correction.** For fixed indices \(k,a,b\), direct factorial expansions give, with \(s=a+b\),
\[
a_n(k)=\frac{e^{-1}}{k!}\left[1+\frac{3-k-k^2}{2n}+O_k(n^{-2})\right],
\]
\[
b_n(a,b)=\frac{e^{-2}}{a!b!}\left[1+\frac{2+s/2-s^2/2}{n}+O_{a,b}(n^{-2})\right].
\]
The difference between the first-order bracket coefficients for \(b_n(a,b)\) and the product \(a_n(a)a_n(b)\) is \(-(a-1)(b-1)\). For indices below \(n^{1/8}\), Taylor remainders are bounded by a polynomial in the indices times \(n^{-2}\). The complementary binomial/multinomial tails are superpolynomially small, using the factorial-moment bounds \(\mathbb P(K\ge k)\le1/k!\) for a fixed-label occupancy \(K\). These estimates justify summing the expansions and yield
\[
p_{n,r}=\rho_r+O_r(n^{-1}),\qquad
n(q_{n,r}-p_{n,r}^2)\longrightarrow
-r\left[e^{-r}\sum_{k\ge0}\frac{k-1}{(k!)^r}\right]^2
=-r(\eta_r-\rho_r)^2.
\]
Substitution in the exact variance formula proves its claimed limit.

**Conditional central limit theorem.** Let the random vectors \((Y_{v,1},\ldots,Y_{v,r})\), \(1\le v\le n\), have independent Poisson(1) coordinates, independently across labels. Condition on every total \(\sum_vY_{v,j}=n-2\). The resulting joint distribution is exactly that of the \(r\) independent Prüfer occupancy vectors. Unconditionally set \(J_v=\mathbf1\{Y_{v,1}=\cdots=Y_{v,r}\}\). The i.i.d. vector \((J_v,Y_{v,1},\ldots,Y_{v,r})\) has mean \((\rho_r,1,\ldots,1)\) and covariance matrix
\[
\begin{pmatrix}
\rho_r(1-\rho_r)&c_r\mathbf1_r^\mathsf T\\
c_r\mathbf1_r&I_r
\end{pmatrix},\qquad c_r=\eta_r-\rho_r.
\]
Fourier inversion of the lattice conditioning, combined with the ordinary multivariate central limit expansion, gives the conditional characteristic function
\[
\mathbb E\!\left[\exp\!\left(\frac{it\sum_v(J_v-\rho_r)}{\sqrt n}\right)\ \middle|\ \sum_vY_{v,j}=n-2\text{ for every }j\right]
\longrightarrow \exp\!\left(-\frac{t^2}{2}\bigl[\rho_r(1-\rho_r)-rc_r^2\bigr]\right).
\]
To justify this inversion, split the \(r\)-torus at distance \(n^{-2/5}\) from the origin. Near the origin, the joint covariance expansion bounds the modulus by \(\exp[-c\|\boldsymbol\theta\|^2+O_t(\|\boldsymbol\theta\|/\sqrt n+1/n)]\); thus the annulus outside radius \(n^{-2/5}\) is exponentially negligible after raising to the \(n\)-th power. Away from a fixed neighborhood of the origin the underlying independent Poisson-total characteristic function has modulus strictly below one, and its \(O_t(n^{-1/2})\) perturbation remains bounded away from one. Within the neighborhood rescale the phases by \(\sqrt n\); dominated Gaussian integration yields the Schur complement in the last display. The fixed shift \(-2\) in each conditioned total vanishes at this scale. Consequently the stated Gaussian convergence holds, by Lévy's theorem. Strict positivity of the Schur complement follows because a nonconstant equality indicator of \(r\) unbounded independent Poisson variables cannot agree almost surely with an affine function of their coordinates.

Finally, \(\eta_r<\rho_r\) when \(r\ge2\): the identity \(\sum_{k\ge0}(k-1)/k!=0\) becomes strictly negative if factorial powers increase from \(1\) to \(r\), since the sole negative term remains \(-1\) while all positive terms strictly decrease. This proves the strict negative covariance limit.

## Verification
Run `python3 verify.py` with the supplied source file. The checker enumerates Prüfer words independently for \((n,r)=(2,2),(3,2),(3,3),(4,2),(4,3),(5,2)\), comparing exact rational means, marked probabilities and variances with the finite formulas. It also checks exact formulas for \(3\le n\le18\), \(2\le r\le4\), and numerically evaluates convergent constant series and asymptotic first moments. It reported **249 passed assertions**. Exhaustive small cases and numerical convergence checks are not substitutes for the analytic limit arguments.

## Relationship to prior work
Prüfer encoding and the multinomial degree model are classical (see Frieze–Karoński, *Introduction to Random Graphs*, chapter 14). Bogachev, Gnedin and Yakubovich (2006) analyze variance phenomena in occupancy models, supplying context for conditioning and occupancy fluctuations; their principal setting is not the degree-coincidence count across independent labelled trees. Single-variable Poisson coincidences also appear in Nijimbere (2016), whereas the present joint statistic includes a shared fixed-total occupancy constraint, whose negative covariance correction controls its Gaussian variance. Nearby random-tree studies of degree counts, tree isomorphism and shared-edge overlap concern different statistics. The novelty claim is for the specific exact finite pgf and its joint finite-correction/Gaussian asymptotic pair, not the general Prüfer bijection or the existence of classical occupancy central limit methods.

## Limitations
This is a mathematically derived distribution and limit under independent uniform Cayley trees; it does not cover dependent tree samples, arbitrary graph hosts, or growing \(r\). The covariance statement is eventually negative, and is **not** asserted to be negative for every finite \(n\). Full historical priority is not established against every older occupancy-coincidence theorem; some related publisher-hosted works were available only as excerpts/abstracts. Independent validation has not been performed. The supplied finite checker is supplementary to the analytic proof.

## References
1. L. V. Bogachev, A. V. Gnedin, Y. V. Yakubovich, *On the variance of the number of occupied boxes*, preprint first public 2006-09-18, https://arxiv.org/abs/math/0609498 .
2. A. Frieze and M. Karoński, *Introduction to Random Graphs*, Chapter 14, *Trees*, online 2015-11-05, https://doi.org/10.1017/CBO9781316339831.015 .
3. V. Nijimbere, *Coincidences, Goodness of Fit Test and Confidence Interval for Poisson Distribution Parameter via Coincidence*, *American Journal of Applied Mathematics and Statistics* 4 (2016), 185–193, https://doi.org/10.12691/ajams-4-6-4 .
