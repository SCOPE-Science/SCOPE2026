# A sharp weak-damping budget concentration law for controllability volume on directed cascades

## Finding

Let \(n\ge3\), \(S>0\), and \(\mu>0\). On a directed \(n\)-vertex chain, allocate positive forward rates \(w_1,\ldots,w_{n-1}\) with \(\sum_{i=1}^{n-1}w_i=S\). Each vertex loses mass at rate \(\mu\); a forward transmission rate is also a loss from its upstream vertex. Control enters only at the first vertex. For the infinite-horizon controllability Gramian \(W\), maximize its determinant over all rate allocations.

For **every** positive \(\mu\), every maximizing allocation exists and is strictly decreasing:
\[
w_1>w_2>\cdots>w_{n-1}>0.
\]
For all rates (including coincident rates), the exact determinant is
\[
\boxed{\displaystyle
\det W=\frac{\prod_{i=1}^{n-1}w_i^{2(n-i)}}
{\prod_{i,j=1}^{n}(\lambda_i+\lambda_j)},
\quad\lambda_i=\begin{cases}\mu+w_i&i<n,\\\mu&i=n.\end{cases}}
\]

The two extreme damping regimes have different, sharp allocation laws:

1. **Strong damping.** For any choice of maximizer at each \(\mu\),
\[
\lim_{\mu\to\infty}\frac{w_i}{S}=\frac{2(n-i)}{n(n-1)}
\quad(1\le i<n).
\]
2. **Weak damping.** For any choice of maximizer,
\[
 w_1\longrightarrow S,\qquad
 \frac{w_i}{\mu}\longrightarrow c_i\quad(2\le i<n),
\]
where \(c_2>\cdots>c_{n-1}>0\) is the **unique** maximizer of
\[
F_n(c)=\frac{\prod_{i=2}^{n-1}c_i^{2(n-i)}}
{\prod_{i,j=2}^{n}(2+c_i+c_j)},\qquad c_n=0.
\]
Equivalently, its positive components solve, uniquely,
\[
\boxed{\displaystyle n-i=\sum_{j=2}^{n}\frac{c_i}{2+c_i+c_j},
\qquad 2\le i<n.}
\]
The optimal determinant has the sharp asymptotic law
\[
\boxed{\displaystyle
\max_{\substack{w_i>0\\\sum_i w_i=S}}\det W
\sim\frac{F_n(c)}{2S\,\mu^{n-1}}\qquad(\mu\downarrow0).}
\]
By contrast, fixing every rate independently of \(\mu\) gives only a \(\mu^{-1}\) divergence. For \(n=3\), \(c_2=1+\sqrt5\), and the optimal leading constant is \((5\sqrt5-11)/(16S)\).

## Assumptions and scope

The state obeys \(\dot x=A x+e_1u\), with \(A_{i,i}=-(\mu+w_i)\) for \(1\le i<n\), \(A_{n,n}=-\mu\), \(A_{i+1,i}=w_i\), and all other entries zero. The Gramian is \(W=\int_0^\infty e^{At}e_1e_1^{\mathsf T}e^{A^{\mathsf T}t}\,dt\). Its eigenvalues are positive because the controllability matrix \([e_1,Ae_1,\ldots,A^{n-1}e_1]\) is triangular with nonzero diagonal \(1,w_1,w_1w_2,\ldots,\prod_{i=1}^{n-1}w_i\). Every eigenvalue of \(A\) is negative. No claim concerns non-feedforward graphs, multiple actuators, stochastic transmission, finite-horizon Gramians, or a unique optimizer at arbitrary finite damping.

The design constraint is a **fixed sum of transition rates**, not a sum of spectral or edge-resistance costs. Thus each nonnegative rate simultaneously changes a subdiagonal transmission and its upstream diagonal loss.

## Proof

**1. Exact determinant identity.** Write \(\lambda_i=\mu+w_i\) for \(i<n\), \(\lambda_n=\mu\). The Laplace transform of the impulse response at vertex \(i\) is
\[
H_i(s)=\frac{\gamma_i}{\prod_{k=1}^{i}(s+\lambda_k)},\qquad
\gamma_i=\prod_{k=1}^{i-1}w_k,\quad\gamma_1=1.
\]
Assume first that the \(\lambda_i\) are pairwise distinct. Partial fractions represent the impulse-response vector as \(h(t)=Ce^{-\Lambda t}\), with \(C\) lower triangular and
\[
 C_{ii}=\frac{\gamma_i}{\prod_{k<i}(\lambda_k-\lambda_i)}.
\]
Consequently \(W=CKC^{\mathsf T}\), where \(K_{ij}=1/(\lambda_i+\lambda_j)\). The ordinary Cauchy determinant formula gives
\[
\det K=\frac{\prod_{i<j}(\lambda_i-\lambda_j)^2}
{\prod_{i,j}(\lambda_i+\lambda_j)}.
\]
Every Vandermonde factor cancels against \((\det C)^2\), leaving the formula in the Finding section because \(\prod_i\gamma_i^2=\prod_{i<n}w_i^{2(n-i)}\). Both sides are continuous in strictly positive rates, so the identity extends to all repeated-pole cases without taking singular partial-fraction limits in numerical computations.

**2. Existence and strict rate ordering.** The formula extends continuously to the closed budget simplex, with value zero whenever any rate is zero and positive on the interior. Therefore a maximizer exists in the interior. Its denominator depends only on the *multiset* of rates. If \(i<j\) but \(w_i<w_j\), exchanging these two rates strictly increases the numerator. Thus rates must be nonincreasing. If two are equal, transferring an infinitesimal positive amount from the later rate to the earlier rate strictly increases the logarithm of the numerator to first order, while the symmetric denominator has zero first derivative in that exchange direction at equality. Every maximizing rate vector is therefore strictly decreasing.

**3. Strong-damping limit.** Uniformly over the closed rate simplex,
\[
\prod_{i,j}(\lambda_i+\lambda_j)=(2\mu)^{n^2}
\bigl(1+O_n(S/\mu)\bigr).
\]
The unique maximum of \(\prod_{i<n}w_i^{2(n-i)}\) at fixed sum \(S\) is obtained by the strict concavity of its logarithm: \(w_i/S=2(n-i)/[n(n-1)]\). Compactness and uniform convergence of normalized objectives show that *every* optimizing family converges to this allocation.

**4. Weak-damping rescaling and existence of a nonzero limit.** At any maximizer \(w_1\ge S/(n-1)\). Since the \(\lambda_i\) are now nonincreasing, pairwise denominator factors obey
\[
\prod_{i,j=1}^n(\lambda_i+\lambda_j)
\ge 2^n\prod_{i=1}^n\lambda_i^{2(n-i)+1}.
\]
Indeed the diagonal contributes \(2\lambda_i\), and for \(i<j\) both symmetric factors are at least \(\lambda_i\). Hence
\[
\det W\le\frac{2^{-n}}{\prod_i\lambda_i},\qquad
\mu^{n-1}\det W\le
\frac{2^{-n}}{\mu+w_1}
\prod_{i=2}^{n-1}\frac{\mu}{\mu+w_i}.
\]
For arbitrary fixed positive \(c_2>\cdots>c_{n-1}\), choose \(w_i=\mu c_i\) for \(i\ge2\) and \(w_1=S-\mu\sum_{i=2}^{n-1}c_i\) (valid for sufficiently small \(\mu\)). Directly in the exact determinant formula,
\[
\lim_{\mu\downarrow0}\mu^{n-1}\det W=\frac{F_n(c)}{2S}>0.
\]
The trial family supplies a positive lower bound for all optimal normalized determinants. The preceding upper bound therefore forces every \(w_i/\mu\), for \(i\ge2\), to remain bounded as \(\mu\downarrow0\). In particular \(w_1\to S\). The exact rescaled determinant additionally tends to zero if any one of those bounded ratios tends to zero while the other ratios stay bounded, contradicting the positive trial lower bound. Thus all rescaled smaller rates lie in a fixed compact subset of the positive orthant.

**5. Unique limiting optimizer and limit value.** Compactness gives subsequential limit vectors \(c\). On their compact feasible range the normalized exact determinant converges uniformly to \(F_n(c)/(2S)\); comparing each optimizer with all fixed feasible trial vectors proves that any limit maximizes \(F_n\). To prove uniqueness, put \(c_i=e^{y_i}\) for \(2\le i<n\). The logarithm of \(F_n\) is a linear function of \(y\) minus a sum of convex log-sum-exp terms \(\log(2+e^{y_i}+e^{y_j})\), including strictly convex diagonal terms \(\log(2+2e^{y_i})\). Therefore \(\log F_n\) is strictly concave in \(y\). The same pairwise-factor bound used above, now with \(\lambda_i=1+c_i\) and \(c_n=0\), shows that \(F_n\to0\) whenever any ordered \(c_i\) tends to zero or infinity. Thus the maximum exists in the interior and is unique. Its logarithmic first-order conditions are precisely the displayed equations. An exchange argument forces the limiting rates to be strictly ordered. Every subsequence has the same limit, so the entire optimizing family converges. The normalized optimal determinant converges as claimed.

For \(n=3\), the stationarity equation simplifies to \(c_2^2-2c_2-4=0\), giving \(c_2=1+\sqrt5\). Inserting this value into \(F_3(c)\) gives \(F_3=(5\sqrt5-11)/8\), and the leading determinant constant follows.

**6. Fixed-rate contrast.** If all \(w_i\) are fixed and strictly positive, exactly one denominator factor, \(\lambda_n+\lambda_n=2\mu\), tends to zero; the others stay strictly positive as \(\mu\downarrow0\). The determinant therefore grows like a positive constant times \(\mu^{-1}\), compared with \(\mu^{-(n-1)}\) for the optimally reallocated rates.

## Verification

The included `verify.py` uses the exact Lyapunov recurrence
\[
(\lambda_i+\lambda_j)W_{ij}=\mathbf1_{i=j=1}
+\mathbf1_{i>1}w_{i-1}W_{i-1,j}
+\mathbf1_{j>1}w_{j-1}W_{i,j-1}
\]
(using one-based indices), calculates determinants by rational Gaussian elimination, and compares them with the closed product formula. Run `python verify.py` with standard Python; the script checks 125 exact cases, including repeated rates, several damping choices, dimensions \(2\) through \(7\), and all relevant early/late rate exchanges. The infinite-parameter assertions follow from the proof above, not from these finite checks.

## Relationship to prior work

Controllability-Gramian metrics and their role in network actuation are established in Pasqualetti, Zampieri and Bullo (2013) and Summers, Cortesi and Lygeros (2014). Becker, Pequito, Pappas and Preciado (2019) investigate the distinct problem of edge-weight design under constraints on the smallest Gramian eigenvalue or the inverse trace, via optimization relaxations. The classical Cauchy determinant identity and the standard impulse-response Gramian representation are not new. The new assertion here is the exact *budget-optimal rate hierarchy*, especially the all-dimension weak-damping concentration, its unique finite scaling vector, and the contrast with the strong-damping allocation. None of the inspected source results yields this allocation through a parameter match or stated implication.

## Limitations

The result is specific to the stated positive, mass-conserving forward-chain couplings with common leakage, one upstream control, and the determinant criterion. It does **not** establish uniqueness of the maximizing rate vector at a fixed intermediate \(\mu\), numerical conditioning at the optimum, a practical robust optimum when rates are lower-bounded, or any behavior of directed networks with branches and feedback. The uniqueness claim is only for the *limiting weak-damping rate vector* (and for the limiting strong-damping profile). The analytical proof has not received independent mathematical validation. Previously unknown equivalent literature might alter publication priority; the checked works address neighboring but not identical design questions.

## References

1. F. Pasqualetti, S. Zampieri and F. Bullo, *Controllability Metrics, Limitations and Algorithms for Complex Networks*, arXiv:1308.1201, first publicly posted August 6, 2013. https://arxiv.org/abs/1308.1201
2. T. H. Summers, F. L. Cortesi and J. Lygeros, *On Submodularity and Controllability in Complex Dynamical Networks*, arXiv:1404.7665 (2014). https://arxiv.org/abs/1404.7665
3. C. O. Becker, S. Pequito, G. J. Pappas and V. M. Preciado, *Network Design for Controllability Metrics*, arXiv:1902.04195 (2019). https://arxiv.org/abs/1902.04195
