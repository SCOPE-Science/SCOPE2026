# A unique intermediate-noise variance maximum for shared leaves of coupled Cayley trees

## Finding

Encode a uniform labelled Cayley tree on \([n]\), \(n\ge2\), by its \(m=n-2\) independent uniform Prüfer letters. To generate a second tree, independently retain each letter with probability \(\rho\in[0,1]\); otherwise replace it by a new uniform letter, which may happen to equal the old one. Let \(L_1,L_2\) count the leaves of the two trees and \(H\) the labels that are leaves in both.

For fixed \(\rho\in[0,1]\), the variance density of \(H\) has limit
\[
 v(\rho)=\lim_{n\to\infty}n^{-1}\operatorname{Var}(H)
 =e^{\rho-2}-(3-2\rho+\rho^2)e^{2\rho-4}>0.
\]
It is uniquely maximized on \([0,1]\) at the solution \(\rho_*\in(0,1)\) of
\[
 2(2-\rho_*+\rho_*^2)e^{\rho_*-2}=1.
\]
Numerically, \(\rho_*\approx0.7199641975\) and \(v(\rho_*)\approx0.1173671281\), compared with \(v(0)\approx0.0803883666\) and \(v(1)\approx0.0972088747\). The optimum is for the limiting variance, not a claim about the exact location or uniqueness of each finite-size optimizer.

For fixed \(0<\rho<1\), the vector of counts centered at their exact expectations and divided by \(\sqrt n\) converges to a mean-zero Gaussian with covariance, for \(q=e^{-1}\), \(Q=e^{\rho-2}\),
\[
 \Sigma_\rho=\begin{pmatrix}
 q-2q^2 & Q-(1+\rho)q^2 & Q(1-2q)\\
 Q-(1+\rho)q^2 & q-2q^2 & Q(1-2q)\\
 Q(1-2q)& Q(1-2q)&v(\rho)
 \end{pmatrix}.
\]
The contribution concerns the variance maximum and the fixed-retention joint fluctuation law. The exact noisy-occupancy coupling and finite avoidance identities used below are covered by the finite mixed-moment formula of [1].

## Finite identities used in the proof

A label is a leaf precisely when it is absent from the code. Define
\[
 q_n=(1-1/n)^m,\qquad
 a_{n,k}=\rho(1-k/n)+(1-\rho)(1-k/n)^2,
 \quad Q_n=a_{n,1}^m .
\]
Then \(\mathbb E(H)_{\underline{k}}=(n)_{\underline{k}}a_{n,k}^{m}\) for \(0\le k\le n\), where the underline denotes a falling factorial. This is the common-vacancy case of [1] with refresh probability \(\varepsilon=1-\rho\). Equivalently, one coordinate avoids a prescribed set of \(k\) labels in both codes with probability \(a_{n,k}\), and the coordinates are independent. In particular,
\[
 \mathbb EH=nQ_n,\quad \mathbb EL_i=nq_n,\quad
 \operatorname{Var}(H)=nQ_n(1-Q_n)+n(n-1)(a_{n,2}^{m}-Q_n^2).
\]
For distinct labels \(u,v\), the one-coordinate probabilities that \(u\) is absent from both and \(v\) from the first, and that \(u\) is absent from the first and \(v\) from the second, respectively, are
\(b_n=(1-2/n)(1-(1-\rho)/n)\) and \(c_n=1-2/n+(1-\rho)/n^2\). The corresponding finite formulas used for comparison are
\[
 \begin{aligned}
 \operatorname{Var}(L_i)&=nq_n(1-q_n)+n(n-1)((1-2/n)^m-q_n^2),\\
 \operatorname{Cov}(H,L_i)&=nQ_n+n(n-1)b_n^m-n^2Q_nq_n,\\
 \operatorname{Cov}(L_1,L_2)&=nQ_n+n(n-1)c_n^m-n^2q_n^2.
 \end{aligned}
\]
At \(n=2\) all zero exponents represent empty products; both trees have two leaves.

## Variance limit and its unique maximum

Write \(a=2-\rho\) and \(c=(1-\rho)-a^2/2\). For each fixed \(k\), expansion gives
\[
 m\log a_{n,k}=-ak+\frac{2ak+ck^2}{n}+O(n^{-2}).
\]
Thus \(Q_n\to Q=e^{-a}\), \(n(a_{n,2}^m-Q_n^2)\to 2cQ^2\), and the finite variance gives \(v=Q(1-Q)+2cQ^2\). This is positive since \(v\ge Q[1-(3-\rho)Q]\) and \((3-\rho)e^{\rho-2}\le 2/e<1\) on \([0,1]\). Also,
\[
 v'(\rho)=e^{\rho-2}[1-2(2-\rho+\rho^2)e^{\rho-2}].
\]
The subtracted function inside the bracket is strictly increasing, with derivative \(2(1+\rho+\rho^2)e^{\rho-2}>0\), and it ranges from \(4e^{-2}<1\) to \(4e^{-1}>1\). This establishes the unique strict maximum and the endpoint comparisons.

## Joint Gaussian limit

Let \(S\) be the binomial \((m,\rho)\) number of latent retain decisions, not the number of observed letters that coincide. Given \(S=s\) and the retained positions, there are independent uniform allocations in three streams, with sizes \(s,m-s,m-s\). The leaf indicators in a box are respectively emptiness in streams \((1,2)\), \((1,3)\), and \((1,2,3)\). The joint law of their sums given the retained positions depends only on \(s\).

For deterministic stream totals \(m_j\) with \(\lambda_{n,j}=m_j/n\to\alpha_j>0\), take independent Poisson counts of means \(\lambda_{n,j}\) in each box; conditioning on the totals gives the independent uniform allocations exactly. Let \(Z\) denote a single Poisson count vector and \(f\) its bounded vector of indicators. Fourier inversion for the totals yields a ratio of integrals over \([-\pi,\pi]^3\). The numerator integrand is the \(n\)-th power of the single-box characteristic function of \(t\cdot(f-\mathbb Ef)/\sqrt n+\theta\cdot(Z-\lambda_n)\), and the denominator takes \(t=0\). At \(\theta=u/\sqrt n\), the quadratic expansion converges to the joint Gaussian characteristic function of \(f,Z\) at the limiting means. For domination near zero, the independent-copy identity for one minus the squared modulus gives a lower bound \(c\|\theta\|^2-C_t/n\) by restricting to the events \((Z,Z')=(e_j,0)\) for the coordinate vectors \(e_j\). Their probabilities are bounded below as the rates converge to positive limits; boundedness of \(f\) and \((a+b)^2\ge a^2/2-b^2\) give the bound. Thus the scaled integrands are dominated by \(C'_t e^{-c'\|u\|^2}\). Outside any fixed neighborhood of zero the unperturbed Poisson modulus is uniformly below one, and the bounded tilt changes it by \(O(n^{-1/2})\). Integrating the limiting Gaussian and dividing by the denominator gives covariance
\[
 \operatorname{Cov}(f(Z)) - \sum_j
 \frac{\operatorname{Cov}(f(Z),Z_j)\operatorname{Cov}(Z_j,f(Z))}{\alpha_j}.
\]
Here for an indicator requiring streams \(J\) empty, the conditional expectation per box is \((1-1/n)^{\sum_{j\in J}m_j}\); it differs from its Poisson mean by \(O(n^{-1})\). Thus one may center by the exact conditional means.

At means \((\rho,1-\rho,1-\rho)\), the three indicator means are \((q,q,Q)\). For an emptiness indicator of mean \(p\), the cross-covariance with \(Z_j\) is \(-p\alpha_j\) if the indicator requires stream \(j\) empty and zero otherwise. Hence the Gaussian correction subtracts \(q^2\) from the marginal leaf variances, \(\rho q^2\) from their covariance, \(qQ\) from the leaf/common-leaf covariances and \((2-\rho)Q^2\) from the common-leaf variance. The conditional covariance is therefore \(\Sigma_\rho\) except that its last diagonal entry is \(Q-(3-\rho)Q^2\).

Finally the conditional means of \(L_1,L_2\) do not depend on \(S\), while the conditional mean of \(H\) is \(g_n(S)=n(1-1/n)^{2m-S}\). The derivative at \(\rho m\) tends to \(Q\) and the second derivative is uniformly \(O(n^{-1})\) for \(0\le S\le m\). Since \(\operatorname{Var}(S)=m\rho(1-\rho)\), it follows that \(g_n(S)-\mathbb EH=Q(S-\rho m)+o_{\mathbb P}(\sqrt n)\). The fixed-totals characteristic function argument applies along every sequence \(s/m\to\rho\); consequently the conditional characteristic functions converge in probability to the same deterministic Gaussian characteristic function. Their moduli are bounded by one, so the joint limit with \((S-\rho m)/\sqrt n\) factors. The binomial fluctuation adds independent variance \(\rho(1-\rho)Q^2\) to the last coordinate, yielding \(\Sigma_\rho\).

## Verification and scope

The companion `check.py` compares the displayed finite means, variances and covariances with weighted enumeration of pairs of words through \(n=5\) at \(\rho=1/2\), and checks finite endpoint identities and inequalities at rational parameters through \(n=30\). These checks do not prove either limit. The variance maximum follows from differentiation and strict inequalities, and the Gaussian law follows from the conditional argument. The result concerns coordinatewise code refresh, not edge-level perturbation, and the Gaussian limit is only stated for fixed interior \(\rho\).

## Relationship to prior work

[1] gives the same noisy occupancy model, including exact mixed factorial moments for vacancy categories at every finite size. Its mixed moments with only common vacancy counted give the common-leaf identities after taking \(m=n-2\); the other avoidance identities also follow directly from its forbidden-set formula. Its asymptotic theorem is instead a three-Poisson law at coupon coverage, \(m=n\log n+O(n)\), not the linear-load Gaussian statement or its variance optimization. No priority inference for the shared formulas follows from the catalogue date. The relevant finite formulas and the underlying coupling are acknowledged here rather than claimed as new.

[2] uses an analogous conditioned-Poisson Schur complement for agreement of full degrees over independent Cayley trees. The present limit requires three streams with potentially unequal limiting rates and a separate random binomial size fluctuation. Classical occupancy variance and de-Poissonization methods [3–5] are not claimed as new. The coupling and statistic also differ from partial shared growth of uniform-attachment trees. The comparison with inspected sources is limited; unlocated work on multistream occupancy may cover parts of the linear-load law.

## References

1. *Critical resampling noise and a three-Poisson vacancy law at coupon coverage*, [RESULT.md, Proof (finite mixed factorial moments)](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-critical-resampling-noise-and-a-three-poisson-vacancy-law-at-cou--c552f8b16e6b/RESULT.md).
2. *A Gaussian law for degree agreement across independent Cayley trees*, [RESULT.md, conditional limit proof](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-a-gaussian-law-for-degree-agreement-across-independent-cayley-tr--b3d73bd92af7/RESULT.md).
3. L. V. Bogachev, A. V. Gnedin and Yu. V. Yakubovich, *On the variance of the number of occupied boxes*, [arXiv:math/0609498](https://arxiv.org/abs/math/0609498).
4. A. D. Barbour and A. V. Gnedin, *Small counts in the infinite occupancy scheme*, [arXiv:0809.4387](https://arxiv.org/abs/0809.4387).
5. H.-K. Hwang and S. Janson, *Local limit theorems for finite and infinite urn models*, [arXiv:math/0604397](https://arxiv.org/abs/math/0604397).
