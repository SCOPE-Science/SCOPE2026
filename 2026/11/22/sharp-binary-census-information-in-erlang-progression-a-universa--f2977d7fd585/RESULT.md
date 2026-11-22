# Sharp binary-census information in Erlang progression: a universal high-stage offset

## Finding
Consider a synchronous cohort of a Poisson-distributed number of independent individuals with unknown mean \(\theta>0\). Each individual passes through \(k\ge1\) sequential, independent exponential stages, with common unknown transition rate \(\lambda>0\) and **known integer** \(k\). At a chosen follow-up time \(t>0\), only two aggregate counts are retained: completed all stages and not yet completed. Define \(x=\lambda t\), and
\[
 f_k(x)=\frac{x^{k-1}e^{-x}}{(k-1)!},\qquad
 P_k(x)=1-e^{-x}\sum_{j=0}^{k-1}\frac{x^j}{j!},\qquad Q_k(x)=1-P_k(x).
\]
With the local logarithmic parameters \((\log\theta,\log\lambda)\), the Fisher determinant is \(\theta^2 J_k(x)\), where
\[
 J_k(x)=\frac{x^2 f_k(x)^2}{P_k(x)Q_k(x)}.
\]
For **every integer** \(k\ge1\), \(J_k\) has exactly one global maximizer \(x_k\in(0,\infty)\), characterized by
\[
 2(x_k-k)=\frac{x_k^k e^{-x_k}}{(k-1)!}
 \left(\frac1{Q_k(x_k)}-\frac1{P_k(x_k)}\right).
\]
It is also the unique optimal split, up to exchanging output labels and null sets, among **all measurable binary classifications** of the exact completion time. The optimal follow-up is locally \(t_k=x_k/\lambda\), requiring a nominal rate for advance scheduling.

The following high-stage expansion is sharp:
\[
 x_k=k+\frac{2}{3(\pi-2)}+o(1),\qquad
 \frac{J_k(x_k)}{k}=\frac2\pi\left[1+\frac{10-3\pi}{18(\pi-2)k}+o(k^{-1})\right].
\]
Thus the locally optimal cutoff lies approximately \(0.583979464628\ldots\) stage-mean time units **after** the overall mean \(k/\lambda\) for large \(k\), while one binary readout retains asymptotically \(2/\pi\) of the complete-event-time Fisher information on \(\log\lambda\). For a three-stage model, \(x_3=3.588084450369\ldots\) and \(J_3(x_3)/3=0.641578310051\ldots\).

## Assumptions and scope
The individuals begin the sequential stages simultaneously at time zero; stage rates are identical, independent, and positive; \(k\) is fixed, known, and integer; a Poisson number of individuals is observed with both completed and uncompleted individuals counted; observations have no misclassification or loss; the information criterion is local Fisher D-optimality. Only the experimental design cutoff varies. The full-data comparison observes each exact completion time and the cohort count. No epidemic transmission, right-censoring of unknown start times, informative dropout, or observation cost is modeled.

## Proof
**1. Likelihood and information.** Erlang completion has CDF \(P_k(\lambda t)\). Poisson thinning makes the two readouts independent Poisson random variables with means \(\theta P_k(x)\) and \(\theta Q_k(x)\). Differentiating their log likelihood with respect to \(\eta=\log\theta\) and \(\rho=\log\lambda\), and using \(\partial_\rho P_k(x)=x f_k(x)\), gives the diagonal Fisher matrix \(\operatorname{diag}(\theta,\theta J_k(x))\). The full completion-time score for \(\rho\) is \(k-\lambda T\); its variance is \(k\), giving full-data rate information \(\theta k\).

**2. Strictly single-peaked information.** Let \(X\sim\operatorname{Gamma}(k,1)\), and write \(a(x)=\mathbb E[X\mid X\le x]\), \(b(x)=\mathbb E[X\mid X>x]\), and \(L(x)=x-a(x)\), \(R(x)=b(x)-x\). Integration by parts of \(Xf_k(X)\) gives \(a=k-h/P_k\), \(b=k+h/Q_k\), with \(h=x f_k(x)\). Consequently
\[
 J_k(x)=P_k(x)Q_k(x)(b(x)-a(x))^2,
 \qquad J_k'(x)=f_k(x)(b(x)-a(x))(R(x)-L(x)).
\]
Both \(P_k\) and \(Q_k\) are log-concave on positive arguments. Here is a direct justification, without any log-concave marginal theorem. Since \(\ell(x)=\log f_k(x)\) is concave, the integrand \(f_k(x-u)/f_k(x)\), for fixed \(0<u<x\), is nondecreasing in \(x\). Hence \(P_k(x)/f_k(x)=\int_0^x f_k(x-u)/f_k(x)\,du\) increases strictly, so its reciprocal \(f_k/P_k=(\log P_k)'\) decreases strictly. Similarly \(Q_k(x)/f_k(x)=\int_0^\infty f_k(x+u)/f_k(x)\,du\) is nonincreasing, so \(f_k/Q_k=-(\log Q_k)'\) is nondecreasing. For \(k=1\) the latter derivative is constant. The resulting mean-residual monotonicities can be checked through
\[
 L(x)=\int_0^x\frac{P_k(x-u)}{P_k(x)}\,du,
 \qquad R(x)=\int_0^\infty\frac{Q_k(x+u)}{Q_k(x)}\,du.
\]
Because \((\log P_k)'\) is decreasing, the ratio in the first integral is nondecreasing in \(x\) for every fixed \(u>0\); extending its integration domain makes \(L\) **strictly increasing**. Because \((\log Q_k)'\) is nonincreasing, the second ratio is nonincreasing in \(x\), so \(R\) is nonincreasing. These conclusions hold for \(k=1\), where \(R\equiv1\), too. As \(x\downarrow0\), \(L\to0\) and \(R\to k\). As \(x\to\infty\), \(L\to\infty\) and \(R\to1\). Therefore \(R-L\) crosses zero exactly once, from positive to negative. Since all other factors in the displayed derivative of \(J_k\) are positive, \(J_k\) rises then falls; the crossing gives the globally unique maximizer and its printed equation. The endpoints have \(J_k\to0\).

**3. All measurable binary classifications.** For any measurable two-label statistic \(Y\) of the exact completion time, the retained information is \(\operatorname{Var}(\mathbb E[X\mid Y])\). Equivalently, maximizing it minimizes \(\mathbb E[(X-\mathbb E[X\mid Y])^2]\). Holding the two class centroids fixed, assigning every value to its *nearest* centroid cannot increase squared loss; this is a single-threshold assignment. Replacing the fixed centroids by their actual conditional means further decreases or preserves loss. The global binary optimum is therefore attained by a threshold, and the strict single-peak result identifies that threshold uniquely up to label swaps and zero-measure boundaries. For either class of zero mass, the information is zero and cannot be optimal.

**4. Sharp high-stage asymptotics.** For every fixed real \(c\), Stirling's expansion of the exact density at \(x=k+z\sqrt{k}\) gives \(\sqrt{k}f_k(k+z\sqrt{k})=\phi(z)[1+(z^3-3z)/(3\sqrt{k})]+O(k^{-1})\) for bounded \(z\), where \(\phi\) is the standard normal density. Standard exponential-tail bounds for the sum of \(k\) exponentials justify integrating this local expansion to obtain \(P_k(k)=1/2+1/(3\sqrt{2\pi k})+O(k^{-1})\); integrating from \(k\) to \(k+c\) contributes \(c/\sqrt{2\pi k}+O(k^{-1})\). A second direct Stirling expansion at \(k+c\) gives the density formula. Accordingly, uniformly for bounded \(c\),
\[
 P_k(k+c)=\frac12+\frac{c+1/3}{\sqrt{2\pi k}}+O(k^{-1}),\quad
 f_k(k+c)=\frac1{\sqrt{2\pi k}}
 \left[1-\frac{c+c^2/2+1/12}{k}+O(k^{-2})\right].
\]
The exact root equation for the strictly decreasing difference \(L-R\), evaluated at \(x=k+c\), then yields
\[
 L(k+c)-R(k+c)=2c-\frac4\pi(c+1/3)+o(1).
\]
The right side is strictly increasing in \(c\), with its single zero at \(c_0=2/[3(\pi-2)]\). Evaluate at any two fixed \(c_-<c_0<c_+\) and use the previously proved strict monotonicity to trap \(x_k-k\) between \(c_-\) and \(c_+\) for all sufficiently large \(k\). Thus \(x_k-k\to c_0\), without a hidden assumption about where the maximizer lies. A direct expansion of the exact information formula, uniformly for bounded \(c\), gives
\[
 \frac{J_k(k+c)}{k}=\frac2\pi\left[1+\frac{H(c)}{k}+o(k^{-1})\right],\quad
 H(c)=\frac2\pi(c+1/3)^2-c^2-\frac16.
\]
Substitution of \(c=x_k-k\to c_0\), and elementary simplification of \(H(c_0)\), yields \(H(c_0)=(10-3\pi)/[18(\pi-2)]\), proving the information-retention expansion. The coefficient is positive.

## Verification
`check_erlang.py` recomputes exact truncated Erlang probabilities in high precision, brackets the unique root for selected shapes, independently compares the conditional-mean and Fisher-score equations, checks the Poisson Fisher determinant by direct differentiation, and tests the asymptotic predictions for large shapes. Its finite checks support arithmetic reproducibility only; Steps 1–4 above supply the universal proof.

## Relationship to prior work
Erlang-distributed residence times and their sequential-stage interpretation are established in Wearing, Rohani and Keeling (2005). General scalar quantization and Fisher-information optimization, including other scale families and high-resolution limits, are treated by Cabral Farias and Brossier (2013). Gao et al. (2015) optimize one-bit detection of Gaussian scale changes under a different likelihood and communication model. The nearest universal background is classical Lloyd–Max quadratic quantization: the conditional-centroid characterization is not claimed novel. The specific object established here is the entire Erlang-stage binary-census cutoff family together with its **sharp fixed absolute offset** and its **first finite-stage information-retention correction**, neither an immediate numerical restatement of Gaussian large-sample symmetry nor a claim about all forms of binary testing.

## Limitations
The theoretical result applies to synchronous independent Erlang completions with fixed known stage number. Local-optimal scheduling uses the unknown true rate or a nominal estimate, and there is no robustness guarantee against rate misspecification. No decision-theoretic, epidemic-transmission, misclassification, heterogeneous-stage, or field-performance claim is made. Although targeted literature comparisons found no same-statement published theorem, exhaustive historical priority is not certified; broad two-level optimal-quantization theory is a continuing overlap risk.

## References
- Wearing, H. J., Rohani, P. and Keeling, M. J. (2005), *Appropriate Models for the Management of Infectious Diseases*, PLOS Medicine 2, e174, https://doi.org/10.1371/journal.pmed.0020174 (first published 2005-07-26).
- Cabral Farias, R. and Brossier, J.-M. (2013), *Optimal Scalar Quantization for Parameter Estimation*, arXiv:1310.6945, https://arxiv.org/abs/1310.6945 (first public 2013-10-25).
- Gao, F., Guo, L., Li, H. and Fang, J. (2015), *One-Bit Quantization and Distributed Detection with an Unknown Scale Parameter*, Algorithms 8, 621–631, https://doi.org/10.3390/a8030621 (2015-08-11).
- Lloyd, S. (1982), *Least squares quantization in PCM*, IEEE Transactions on Information Theory 28, 129–137 (originating from earlier 1957 work), https://doi.org/10.1109/TIT.1982.1056489.
