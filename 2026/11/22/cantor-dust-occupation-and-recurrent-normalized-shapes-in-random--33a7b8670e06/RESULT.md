# Cantor-dust occupation and recurrent normalized shapes in random Fibonacci block tilings

## Finding
Fix an integer \(d\ge2\). In the independent-fair-direction cyclic Fibonacci block tiling of Amit, Gebre, Housholder, Khan, Miller, Upton and Yau [1], let \(\mathcal R_n\) be the bounding rectangle after \(n\) placements, and scale each coordinate of \(\mathcal R_n\) by its *own current deterministic side length*. Write its resulting lower and upper faces as \(-Y_{r,n}\) and \(1-Y_{r,n}\), \(0\le r<d\). Thus \(Y_n=(Y_{0,n},\ldots,Y_{d-1,n})\in[0,1]^d\) records the normalized position of the whole rectangle, not the coverage of a fixed point.

Let \(\rho_d\in(1,2)\) solve \(\rho_d^d-\rho_d^{d-1}-1=0\), and set \(\lambda_d=\rho_d^{-d}=1-\rho_d^{-1}\in(0,1/2)\). Let \(\mu_d\) be the law of
\[
Z=(1-\lambda_d)\sum_{j=0}^{\infty}\lambda_d^j B_j,
\qquad B_j\stackrel{\mathrm{iid}}\sim\operatorname{Bernoulli}(1/2),
\]
and let \(K_d=\operatorname{supp}(\mu_d)\).

**Normalized-shape dynamics theorem.** As \(n\to\infty\), the law of \(Y_n\) converges weakly to \(\mu_d^{\otimes d}\). With probability one, the empirical measures \(n^{-1}\sum_{k=0}^{n-1}\delta_{Y_k}\) converge weakly to that same law, and the set of *all* subsequential limits of the actual normalized positions \(Y_n\) is precisely \(K_d^d\). Consequently the normalized rectangles do not converge almost surely, although their time-occupation law is deterministic.

At complete-cycle times \(n=dm\), all finite-window empirical distributions converge almost surely to those of the stationary \(d\)-coordinate affine chain
\[
Z_{r,m+1}=\lambda_d Z_{r,m}+(1-\lambda_d)B_{r,m},
\qquad 0\le r<d,
\]
with independent fair innovations. For each coordinate and fixed integer lag \(h\ge0\), the corresponding limiting time covariance (also the limit of the ordinary finite-\(m\) covariance) is
\[
\lim_{M\to\infty}\frac1M\sum_{m=0}^{M-1}
(Y_{r,dm}-\tfrac12)(Y_{r,d(m+h)}-\tfrac12)
=\frac{1-\lambda_d}{4(1+\lambda_d)}\lambda_d^h
\qquad\text{almost surely}.
\]
Different coordinates have zero limiting cross-covariance at every fixed lag. The support and the uniform Bernoulli product measure on that support have the same exact Hausdorff dimension,
\[
\boxed{\dim_H(K_d^d)=\dim_H(\mu_d^{\otimes d})
=\frac{d\log2}{\log(1/\lambda_d)}
=\frac{\log2}{\log\rho_d}<d.}
\]
In the planar case this equals \(\log2/\log((1+\sqrt5)/2)=1.4404200904\ldots\). In particular, the full-support limiting occupation measure is singular relative to \(d\)-dimensional Lebesgue measure.

## Assumptions and scope
The initial block is \([0,1]^d\). Placements update coordinates \(0,1,\ldots,d-1\) in that fixed cyclic order. Each new block is attached to the positive or negative face according to an independent fair bit, and its thickness is the order-\(d\) Fibonacci weight prescribed in [1]. Let \(F_0^{(d)}=\cdots=F_{d-1}^{(d)}=1\), and \(F_j^{(d)}=F_{j-1}^{(d)}+F_{j-d}^{(d)}\) for \(j\ge d\). The \(j\)-th added thickness in coordinate \(r\) is
\[
w_{r,j}=F_{d-1+r+jd}^{(d)}\quad(j\ge0).
\]
Write \(B_{r,j}=1\) when this placement extends the rectangle in the *negative* direction, and zero otherwise. The streams \((B_{r,j})_{j\ge0}\) are mutually independent across \(r\). After \(m\) completed updates in coordinate \(r\), its length and normalized negative displacement are
\[
L_{r,m}=1+\sum_{j=0}^{m-1}w_{r,j}=F_{dm+r}^{(d)},\qquad
Y_{r,m}^{\circ}=\frac{\sum_{j=0}^{m-1}B_{r,j}w_{r,j}}{L_{r,m}}.
\]
At global time \(n=dm+s\), with \(0\le s<d\), set \(Y_{r,n}=Y_{r,m+1}^{\circ}\) for \(r<s\) and \(Y_{r,n}=Y_{r,m}^{\circ}\) otherwise. When the finding refers to \(Y_{r,dm}\), it is \(Y_{r,m}^{\circ}\). In the covariance formula the empirical mean is centered at the *limiting* mean \(1/2\). All limits are for fixed \(d\); they are not joint dimension/time limits.

## Proof
**1. Exact affine recursion and its geometric limit.** Directly from the placement rule,
\[
Y_{r,m+1}^{\circ}=a_{r,m}Y_{r,m}^{\circ}+(1-a_{r,m})B_{r,m},
\qquad a_{r,m}=\frac{L_{r,m}}{L_{r,m+1}}.
\]
The length identity follows by induction from the Fibonacci recursion (it is also [1, Proposition 2.2]); indeed \(F_{(m+1)d+r}^{(d)}-F_{md+r}^{(d)}=F_{(m+1)d+r-1}^{(d)}=w_{r,m}\). The dominant-root expansion in [1, Theorem 2.7] implies, for every fixed \(r\),
\[
a_{r,m}=\frac{F_{md+r}^{(d)}}{F_{(m+1)d+r}^{(d)}}\longrightarrow\rho_d^{-d}=\lambda_d.
\]
The defining polynomial yields \(\lambda_d=1-\rho_d^{-1}\), and \(1<\rho_d<2\) implies \(0<\lambda_d<1/2\).

**2. Uniform asymptotic coupling.** Enlarge the probability space with independent bits \(B_{r,j}\) for all negative indices \(j\) (the original nonnegative-index bits remain unchanged), and put
\[
Z_{r,m}=(1-\lambda_d)\sum_{k=0}^{\infty}\lambda_d^k B_{r,m-1-k},\qquad m\in\mathbb Z.
\]
The series converges absolutely and gives a strictly stationary factor of the two-sided independent Bernoulli shift. It satisfies the displayed stationary affine recursion. Subtracting the finite-time recursion gives
\[
|Y_{r,m+1}^{\circ}-Z_{r,m+1}|
\le a_{r,m}|Y_{r,m}^{\circ}-Z_{r,m}|+|a_{r,m}-\lambda_d|.
\]
For sufficiently large \(m\), all \(a_{r,m}\le q<1\). Iteration bounds the discrepancy by \(q^{m-m_0}\) plus a geometrically weighted convolution of a deterministic sequence tending to zero. Splitting that convolution into finitely old and uniformly small recent terms shows
\[
\max_{0\le r<d}\sup_{\{B_{r,j}\}}
|Y_{r,m}^{\circ}-Z_{r,m}|\longrightarrow0.
\]
Here the supremum refers to bit realizations in the coupled construction, including the auxiliary past; the bound is deterministic and uniform. Consequently every global phase \(s\) is uniformly approximated by the stationary process with coordinates \(Z_{r,m+1}\) for \(r<s\) and \(Z_{r,m}\) otherwise.

**3. Distribution, empirical law, and complete cluster set.** The coordinate streams are independent, so at any fixed global phase the stationary comparison vector has law \(\mu_d^{\otimes d}\). Uniform coupling proves weak convergence for every phase, and hence for the full sequence of global move counts. The Bernoulli shift is ergodic, as are each of its measurable stationary vector factors and every fixed finite-window factor. Birkhoff's theorem, first for a countable dense family of continuous functions on the compact cube and then by uniform approximation, proves almost-sure weak convergence of phase-specific and all-time empirical measures. Applying the same argument to consecutive complete-cycle vectors gives the stated finite-window empirical convergence.

Let \(K_d=\operatorname{supp}\mu_d\). Every comparison vector \(Z_m\) lies in \(K_d^d\), so the uniform coupling implies every accumulation point of \(Y_{dm}\) is in \(K_d^d\). Conversely every open ball meeting \(K_d^d\) has positive \(\mu_d^{\otimes d}\)-mass; by the ergodic theorem the comparison process visits it with positive limiting frequency. A countable basis of such balls, together with uniform coupling, implies every point of \(K_d^d\) is an accumulation point of \(Y_{dm}\). The entire-time sequence contains the completed-cycle subsequence and is asymptotically close to \(K_d^d\) at every phase; therefore its cluster set is exactly \(K_d^d\). Since the support has more than one point, almost-sure convergence is impossible.

**4. Exact fractal dimension and covariance.** The one-coordinate support is the invariant set of \(x\mapsto\lambda_dx\) and \(x\mapsto\lambda_dx+(1-\lambda_d)\). The \(d\)-fold product is the invariant set of the \(2^d\) maps \(\Phi_e(x)=\lambda_dx+(1-\lambda_d)e\), \(e\in\{0,1\}^d\). Their first-level cubes are pairwise separated because \(\lambda_d<1/2\), and every level-\(j\) cylinder has diameter proportional to \(\lambda_d^j\) and mass \(2^{-dj}\). Covering by all cylinders gives the dimension upper bound \(d\log2/\log(1/\lambda_d)\); cylinder separation and the uniform mass bound on balls of comparable radii give the matching lower bound by the mass-distribution principle. The same cylinder estimates establish exact dimensionality of the uniform self-similar measure. Since this dimension is strictly smaller than \(d\), the measure is Lebesgue-singular.

For a stationary coordinate, \(\mathbb E Z_{r,m}=1/2\) and independence of its Bernoulli digits yields
\[
\operatorname{Var}(Z_{r,m})=\frac{(1-\lambda_d)^2}{4}\sum_{j\ge0}\lambda_d^{2j}
=\frac{1-\lambda_d}{4(1+\lambda_d)}.
\]
The affine recursion gives \(Z_{r,m+h}=\lambda_d^hZ_{r,m}+V_{r,m,h}\), where \(V_{r,m,h}\) depends only on later innovations and is independent of \(Z_{r,m}\). Hence the lag covariance is the claimed variance times \(\lambda_d^h\); coordinate independence gives zero cross-covariances. Almost-sure empirical statements follow from the finite-window ergodic theorem and uniform coupling, while ordinary covariance limits follow from bounded convergence under that coupling.

## Verification
The standalone standard-library checker `check.py` reconstructs each coordinate thickness, finite-time length and affine recursion with exact integers and rational numbers for dimensions \(2\) through \(12\), including intermediate coordinate phases. It checks independent-bit exact finite means, variances and lag-covariances against the limiting formulas, verifies \(\lambda_d=1-\rho_d^{-1}<1/2\) numerically across dimensions, and evaluates finite-run stationary trajectories as additional diagnostics. Run `python3 check.py`. The diagnostic output is `PASS: 15083 exact/arithmetic and bounded numerical checks` with planar shape dimension `1.4404200904125564`. These finite checks do not prove almost-sure recurrence, exact Hausdorff dimension or the ergodic limit; those follow from the four proof steps above.

## Relationship to prior work
Amit et al. [1] give the specific random growth model, order-\(d\) Fibonacci length formula, coordinate-weight asymptotics and exact *point covering-time* distributions. Their Sections 4 and 5 classify individual coverage probabilities and derive covering-time bounds, not normalized rectangle positions, the almost-sure occupation of shapes, or the full orbit cluster set; their Section 6.5 expressly raises asymptotic shape as a further question. A related previously published result [2] classifies *centered covering-time* limit laws for this same model, not empirical geometric shapes. Its full stated result and proof were compared, including the exact variables and conclusions.

Classical theory of contracting random affine iterates [3] supplies ergodicity techniques, and self-similar-set theory [4] supplies the general dimension method. These general tools are credited rather than claimed as new. A published analysis of random-reshuffling stochastic gradient descent [5] obtains a Bernoulli-convolution invariant law for a different two-component optimization chain; it does not involve cyclic Fibonacci tilings or their almost-sure geometric cluster set. Work on metallic-mean deterministic fractal tilings [6] concerns a separate geometric construction, rather than the independently randomized direction process studied here.

The new contribution claimed here is the complete normalized-*geometric*-shape dynamic of the Fibonacci block growth model: the limiting Cantor-dust occupation law, almost-sure full recurrence of the corresponding shape support, and exact completed-cycle covariance/dimension data in one coherent description.

## Limitations
The result fixes \(d\) before taking the time limit, assumes independent fair placement bits, and normalizes *each axis by its current side length*. Other geometric scalings and the square-by-square curve itself are not classified. As all finite-time position laws are atomic while \(\mu_d^{\otimes d}\) is nonatomic, total-variation convergence of these marginals is impossible: their total-variation distance is exactly \(1\) for every finite time. No total-variation convergence or almost-sure convergence of a single normalized rectangle is asserted. The self-similar geometry is an application of standard iterated-function methods; independently established historical priority beyond the inspected sources cannot be guaranteed. Independent mathematical validation has not been performed.

## References
[1] Y. Amit, A. Gebre, C. Housholder, J. Khan, S. Miller, E. Upton, C. Yau, *Random Fibonacci Tilings*, arXiv:2611.08317v1, first publicly posted 2026-11-05, https://arxiv.org/html/2611.08317v1 . Relevant: Proposition 2.2, Theorem 2.7, Sections 4–5 and 6.5.

[2] *Complete subsequential covering-time laws for random Fibonacci tilings*, publicly posted mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-complete-subsequential-covering-time-laws-for-random-fibonacci-t--e2af1a5dfd9a . Relevant: Finding, Proof, Relationship to prior work.

[3] P. Diaconis and D. Freedman, *Iterated Random Functions*, SIAM Review 41 (1999), 45–76, https://doi.org/10.1137/S0036144598338446 .

[4] J. E. Hutchinson, *Fractals and Self Similarity*, Indiana University Mathematics Journal 30 (1981), 713–747, https://maths-people.anu.edu.au/~john/Assets/Research%20Papers/fractals_self-similarity.pdf .

[5] *Random reshuffling has a Cantor-to-interval stationary-support transition*, publicly posted mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-random-reshuffling-has-a-cantor-to-interval-stationary-support-t--ec57811b8333 .

[6] S. Coates, *Metallic mean fractal systems and their tilings*, Journal of Fractal Geometry (2025), https://doi.org/10.4171/JFG/170 .
