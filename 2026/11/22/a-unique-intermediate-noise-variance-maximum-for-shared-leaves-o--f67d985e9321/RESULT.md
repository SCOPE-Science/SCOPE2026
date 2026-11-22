# A unique intermediate-noise variance maximum for shared leaves of coupled Cayley trees

## Finding

For each integer \(n\ge 2\), encode a uniform labelled Cayley tree on \([n]\) by its independent uniform Prüfer letters \(X_1,\ldots,X_{n-2}\). Independently at each code position, retain the letter with probability \(\rho\in[0,1]\), or otherwise replace it with an independent uniform label, obtaining letters \(Y_i\) and a second uniform Cayley tree. Let \(L_1,L_2\) denote the numbers of leaves of the two trees, and let \(H\) count labels that are leaves of both.

Write \(m=n-2\), \(q_n=(1-1/n)^m\) and, for integers \(0\le k\le n\),
\[
 a_{n,k}=\rho(1-k/n)+(1-\rho)(1-k/n)^2,\qquad Q_n=a_{n,1}^{m}.
\]
For every integer \(0\le k\le n\), the following is an exact factorial-moment identity:
\[
 \mathbb E(H)_{\underline{k}}=(n)_{\underline{k}}a_{n,k}^{m}.
\]
In particular, \(\mathbb EH=nQ_n\), and the exact variance is
\[
 \operatorname{Var}(H)=nQ_n(1-Q_n)+n(n-1)(a_{n,2}^{m}-Q_n^2).
\]
Here \(a_{n,2}\) is defined by the same formula, including at \(n=2\).

For each fixed \(\rho\in[0,1]\), as \(n\to\infty\),
\[
 \frac{\operatorname{Var}(H)}n\longrightarrow
 v(\rho)=e^{\rho-2}-(3-2\rho+\rho^2)e^{2\rho-4}>0.
\]
The variance density \(v\) has a **unique global maximum** on \([0,1]\), at the unique solution \(\rho_*\in(0,1)\) of
\[
 2(2-\rho_*+\rho_*^2)e^{\rho_*-2}=1.
\]
Numerically, \(\rho_*\approx0.7199641975455873\), \(v(\rho_*)\approx0.1173671281376303\), whereas \(v(0)\approx0.0803883665704102\) and \(v(1)\approx0.0972088746982169\). Thus *neither independent nor identical trees maximize common-leaf-count uncertainty*; retaining about 72% of the original Prüfer letters does.

Moreover, for fixed \(0<\rho<1\), the exactly centered vector
\[
 \frac1{\sqrt n}
 \begin{pmatrix}L_1-\mathbb EL_1\\ L_2-\mathbb EL_2\\ H-\mathbb EH\end{pmatrix}
 \xrightarrow{d}N_3(0,\Sigma_\rho),
\]
where \(q=e^{-1}\), \(Q=e^{\rho-2}\), and
\[
 \Sigma_\rho=
 \begin{pmatrix}
 q-2q^2 &Q-(1+\rho)q^2&Q(1-2q)\\
 Q-(1+\rho)q^2&q-2q^2&Q(1-2q)\\
 Q(1-2q)&Q(1-2q)&v(\rho)
 \end{pmatrix}.
\]
The central limit theorem concerns this particular coordinatewise coupling of Prüfer codes; it does not claim the same result for all possible couplings of uniform Cayley trees.

## Assumptions and scope

A Prüfer code has \(m=n-2\) positions; for \(n=2\) it is the empty word and both trees have two leaves. The refresh decisions and all replacement letters are independent; refresh means replacing by a new uniform letter, which can coincidentally equal the old letter. Each marginal code is uniform, so each marginal tree is uniform. A vertex is a leaf precisely when its label is absent from the corresponding code. All finite formulas hold for every integer \(n\ge2\) and \(0\le\rho\le1\). The Gaussian statement is for fixed interior \(\rho\), not for a moving noise window.

## Proof

**1. Exact law.** A specified set of \(k\) labels is absent from both codes at a given position with probability \(a_{n,k}\): with probability \(\rho\) the two letters are identical and avoid the set with probability \(1-k/n\), and otherwise two independent letters avoid it with probability \((1-k/n)^2\). Independence across code positions gives \(a_{n,k}^m\). Summing over ordered \(k\)-tuples of distinct labels proves the falling-factorial identity. Its first two cases give the exact mean and variance.

**2. Variance density and unique optimizer.** Let \(a=2-\rho\). Taylor expansion of \(m\log a_{n,k}\), for each fixed \(k\), gives
\[
 m\log a_{n,k}=-ak+\frac{2ak+c k^2}{n}+O(n^{-2}),
 \quad c=(1-\rho)-\frac{(2-\rho)^2}{2}.
\]
Consequently \(Q_n\to Q=e^{-a}\) and
\[
 n(a_{n,2}^{m}-Q_n^2)\to2cQ^2,
\]
which proves \(v(\rho)=Q(1-Q)+2cQ^2\). Differentiation yields
\[
 v'(\rho)=e^{\rho-2}
 \left[1-2(2-\rho+\rho^2)e^{\rho-2}\right].
\]
The bracket decreases strictly because the derivative of its subtracted term is \(2(1+\rho+\rho^2)e^{\rho-2}>0\). Its values have opposite signs at zero and one, since \(4e^{-2}<1<4e^{-1}\). Hence there is exactly one interior maximum. Positivity follows either from the Gaussian conditional variance calculation below or directly from
\[
 v(\rho)\ge Q-(3-\rho)Q^2
 =Q[1-(3-\rho)e^{\rho-2}]>0,
\]
because \((3-\rho)e^{\rho-2}\le 2/e<1\) on \([0,1]\).

**3. Finite cross moments.** For two distinct labels \(u\ne v\), the probability that \(u\) is absent from both codes and \(v\) from the first code at one position is
\(b_n=(1-2/n)(1-(1-\rho)/n)\). The probability that \(u\) is absent from the first and \(v\) from the second is \(c_n=1-2/n+(1-\rho)/n^2\). Thus, exactly,
\[
 \begin{aligned}
 \mathbb EL_i&=nq_n,\\
 \operatorname{Var}(L_i)&=nq_n(1-q_n)+n(n-1)[(1-2/n)^m-q_n^2],\\
 \operatorname{Cov}(H,L_i)&=nQ_n+n(n-1)b_n^m-n^2Q_nq_n,\\
 \operatorname{Cov}(L_1,L_2)&=nQ_n+n(n-1)c_n^m-n^2q_n^2.
 \end{aligned}
\]
Expansion to first order in \(1/n\) gives all entries of \(\Sigma_\rho\): in particular \(n(b_n^m-Q_nq_n)\to-Qq\) and \(n(c_n^m-q_n^2)\to-\rho q^2\). These calculations also independently check the covariance values in the subsequent Gaussian proof.

**4. Joint Gaussian theorem.** Let \(S\sim\operatorname{Binomial}(m,\rho)\) count retained code positions. Conditional on their identities and on \(S=s\), the two codes are built from three independent uniform-letter streams: \(s\) shared letters, \(m-s\) letters exclusive to the first code, and \(m-s\) letters exclusive to the second. A label is a first-tree leaf exactly when its box is empty in streams one and two; similarly the second-tree leaf uses streams one and three; a common leaf is empty in all three.

For completeness, the finite-stream occupancy CLT used here is as follows. If \(d\) independent uniform allocations put \(m_j\) letters into \(n\) labelled boxes, with \(m_j/n\to\alpha_j>0\), and \(f\) is any bounded vector-valued function of the \(d\) per-box counts, then the centered sum of \(f\) over boxes, divided by \(\sqrt n\), converges to a Gaussian with covariance
\[
 \Sigma_f-\sum_{j=1}^d \frac{c_jc_j^{\mathsf T}}{\alpha_j},
 \quad \Sigma_f=\operatorname{Cov}(f(Z)),\quad
 c_j=\operatorname{Cov}(f(Z),Z_j),
\]
where the coordinates \(Z_j\) are independent \(\operatorname{Poisson}(\alpha_j)\). To see this, take independent Poisson box counts of means \(m_j/n\). Their sums conditioned to equal \(m_j\) are exactly the required multinomial allocations. Apply the multivariate iid central limit theorem jointly to the sums of \(f\) and to the Poisson coordinate totals. Multidimensional Fourier inversion for the conditioning event, with frequencies scaled by \(n^{-1/2}\), gives the conditional Gaussian characteristic function. Near zero the logarithm of the single-box characteristic function has its quadratic covariance expansion; outside a shrinking neighborhood its modulus decays exponentially because each positive-rate Poisson coordinate has a strongly aperiodic lattice law and \(f\) is bounded. Dividing by the usual product-Poisson local limit probabilities yields the stated Schur-complement covariance. The same argument holds for any deterministic sequence of totals converging to those positive rates, and thus uniformly for sequences of \(s\) with \(s/m\to\rho\).

Use the three occupancy streams with rate vector \((\rho,1-\rho,1-\rho)\). For a single Poisson box let \(I,J,K\) be the indicators that streams \((1,2)\), \((1,3)\), and \((1,2,3)\), respectively, are all empty. Their means are \((q,q,Q)\). The correction above subtracts \(q^2\) from each leaf variance, \(\rho q^2\) from their covariance, \(qQ\) from each leaf/common-leaf covariance, and \((2-\rho)Q^2\) from common-leaf variance. Hence the conditional Gaussian fluctuation variance of common leaves is \(Q-(3-\rho)Q^2\), while the other entries are exactly those displayed in \(\Sigma_\rho\).

It remains to restore the random retained-position count. Conditional on \(S=s\), the mean common-leaf count is \(n(1-1/n)^{2m-s}\). Expanding at \(s=\rho m\) gives
\[
 \mathbb E(H\mid S)-\mathbb EH
 =Q(S-\rho m)+o_{\mathbb P}(\sqrt n).
\]
The conditional means of both marginal leaf counts do not depend on \(S\). Since \((S-\rho m)/\sqrt n\Rightarrow N(0,\rho(1-\rho))\), the conditional characteristic-function convergence above gives an independent additional Gaussian contribution solely to the common-leaf coordinate, with variance \(\rho(1-\rho)Q^2\). Adding it produces \(v(\rho)=Q-(3-2\rho+\rho^2)Q^2\) and completes the joint central limit theorem.

## Verification

Run `python3 check.py` from the extracted artifact directory. The script independently enumerates all pairs of Prüfer words through \(n=5\) at retention probability \(\rho=1/2\) using integer weights, and compares six exact means, variances, and covariances with the formulas above. It also evaluates the exact formulas at sizes through \(n=30\) and five rational retention probabilities, checking nonnegative variances, covariance Cauchy–Schwarz bounds, and the independence/identity endpoints. This exact finite verification does not prove the asymptotic Gaussian theorem; that follows from the occupancy-conditioning argument.

## Relationship to prior work

Prüfer's classical correspondence turns uniform labelled Cayley trees into uniform strings and identifies leaves as missing labels. Bogachev, Gnedin and Yakubovich (2006) investigate one-stream infinite-urn occupancy variance and normality questions, while Barbour and Gnedin (2008) develop joint small-count normal approximation in a single infinite occupancy scheme. Neither inspected treatment states the coordinatewise two-code perturbation, its exact common-leaf factorial transform, or the unique intermediate-retention variance maximum. Related analyses of correlated recursive or uniform-attachment trees use different growth couplings; their resulting leaf correlations do not imply this code-refresh result. Classical Poissonization and conditional central limit methods are reused rather than claimed as new.

## Limitations

The coupling is specified at the code-position level, so its behavior need not persist under edge-level changes to a tree. The Gaussian law is established for fixed \(0<\rho<1\); no uniform Berry–Esseen rate or arbitrary moving-parameter central limit theorem is asserted. The optimizer concerns *variance*, not mean-square prediction error or all distributional measures of stability. Priority relative to a possible general multistream allocation theorem remains a literature risk; independent validation has not been performed.

## References

1. L. V. Bogachev, A. V. Gnedin, and Yu. V. Yakubovich, *On the variance of the number of occupied boxes*, arXiv:math/0609498, first posted 2006-09-18, https://arxiv.org/abs/math/0609498 .
2. A. D. Barbour and A. V. Gnedin, *Small counts in the infinite occupancy scheme*, arXiv:0809.4387, first posted 2008-09-25, https://arxiv.org/abs/0809.4387 .
