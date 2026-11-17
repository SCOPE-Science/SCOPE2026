# Exact binomial contraction and a full moment spectrum for randomly switched permutation quadratic populations

## Finding

For a natural independent random calendar of pair exchanges in a four-type quadratic stochastic population system, the complete finite-generation composition deviation reduces to one binomial random variable and one finite-state orientation. This yields all positive moments, the almost-sure contraction exponent, a central limit theorem, and a strict annealed–typical relaxation gap.

Let \(v_{12}=(1,1,-2)/\sqrt6\), \(v_{23}=(-2,1,1)/\sqrt6\), and \(v_{13}=(1,-2,1)/\sqrt6\). Writing \(z=p_0-u\) and \(K_n=\sum_{r=2}^n\mathbf1_{\{I_r\ne I_{r-1}\}}\), the exact path law is
\[
p_n-u=\langle z,v_{I_1}\rangle(-1/2)^{K_n}v_{I_n},\qquad K_n\sim\operatorname{Binomial}(n-1,2/3).
\]
The initial pair and \(K_n\) are independent. For \(n\ge1\), every real \(q>0\) has the exact moment
\[
\mathbb E\|p_n-u\|^q=\frac13\sum_{i\in\{12,23,13\}}|\langle z,v_i\rangle|^q\left(\frac{1+2^{1-q}}3\right)^{n-1}.
\]
In particular, \(\mathbb E\|p_n-u\|^2=2^{-n}\|z\|^2\). The orientation has the exact joint law
\[
\Pr(I_n=j\mid I_1=i,K_n=k)=\frac13+(-1/2)^k\left(\mathbf1_{\{i=j\}}-\frac13\right).
\]
For initial \(z\) with all three inner products \(\langle z,v_i\rangle\ne0\), the almost-sure and Gaussian relaxation laws are
\[
\lim_{n\to\infty}\frac{\log\|p_n-u\|}{n}=-\frac23\log2,
\quad
\frac{\log\|p_n-u\|+\frac23(n-1)\log2}{(\log2)\sqrt{2(n-1)/9}}\Rightarrow N(0,1).
\]
The mean-square exponent \(-\log2\) is strictly slower than the typical squared-error exponent \(-(4/3)\log2\).

## Assumptions and scope

Use the probability simplex with four nonnegative coordinates summing to one, with \(0<x_{4,0}<1\). For \(i\in\{1,2,3\}\), the season associated with peripheral permutation \(\pi\) is the non-Volterra quadratic stochastic map
\[
x_i'=2x_4\bigl[\alpha x_i+(1-\alpha)x_{\pi(i)}\bigr],\qquad
x_4'=x_4^2+(x_1+x_2+x_3)^2.
\]
Fix \(\alpha=1/2\). Independently at each integer time, choose \(\pi\) uniformly from transpositions \((12),(23),(13)\), with no other permutations. Define \(p_{i,n}=x_{i,n}/(1-x_{4,n})\), which exists at every finite time for the stipulated initial domain. Let \(u=(1/3,1/3,1/3)\). The exact path and moment laws apply to every \(p_0\), including \(p_0=u\); the nondegenerate almost-sure log and CLT statements require \(\langle p_0-u,v_i\rangle\ne0\) for each of the three pairs. In particular, this excludes a possible first-step exact consensus and gives \(p_0\ne u\).

## Proof

First set \(s_n=x_{4,n}\). Direct substitution yields \(2s_{n+1}-1=(2s_n-1)^2\), hence
\[
s_n=\frac{1+(2s_0-1)^{2^n}}2.
\]
Since \(1-s_{n+1}=2s_n(1-s_n)\), dividing the peripheral update by this positive total gives \(p_{n+1}=(I+P_{I_{n+1}})p_n/2\), where \(P_{ij}\) exchanges coordinates \(i,j\).

On the two-dimensional sum-zero plane \(E=\{z:\sum_i z_i=0\}\), each \((I+P_{ij})/2\) is the orthogonal projection \(v_{ij}v_{ij}^{\mathsf T}\), where the three unit vectors displayed above have pairwise inner products \(-1/2\). Multiplication of rank-one projections therefore gives, for each finite pair word, \(p_n-u=\langle z,v_{I_1}\rangle(-1/2)^{K_n}v_{I_n}\). This is an exact identity, with no asymptotic or mixing assumption.

Conditional on a specified first pair, every pattern of \(n-1\) change indicators with \(k\) changes corresponds to exactly \(2^k\) equally likely pair words. Thus the change indicators are mutually independent Bernoulli variables of parameter \(2/3\), independent of the initial pair. Conditional on exactly \(k\) changes, successive new pairs form the three-state chain with transition matrix \((J-I)/2\). Its \(k\)th power equals \(J/3+(-1/2)^k(I-J/3)\), proving the stated joint orientation probabilities.

Taking absolute norms in the path formula and then averaging first over \(K_n\) and subsequently over the uniform first pair yields the all-order moment formula. At \(q=2\), \(\sum_i v_iv_i^{\mathsf T}=(3/2)I_E\), so the initial average squared projection is \(\|z\|^2/2\), and the one-step moment factor is \(1/2\), giving \(2^{-n}\|z\|^2\).

Under the nonzero-projection hypothesis, \(\log\|p_n-u\|=\log|\langle z,v_{I_1}\rangle|-K_n\log2\). The first term is an almost surely finite, time-independent random variable. The strong law and central limit theorem for the independent Bernoulli change indicators give the claimed almost-sure exponent and Gaussian limit. For squared norms, doubling the almost-sure log exponent yields \(-(4/3)\log2\), different from the exact mean-square exponent \(-\log2\).

## Verification

The accompanying pure-Python exact-rational checker enumerates every one of the \(3^n\) possible pair calendars for each \(1\le n\le8\), totaling \(9840\) words. It verifies the original nonlinear four-coordinate update against the normalized three-coordinate pair projections, the exact \(s_n\) formula, all binomial multiplicities, the conditional terminal-orientation distribution, and the \(q=2,4\) moment formulas by rational arithmetic. It completes with `RANDOM_QSO_THREE_PROJECTION_ALL_EXACT_OK; all_words=9840, joint_endpoint=PASS, moments_2_4=PASS`. This finite checker corroborates but does not replace the general rank-one and Bernoulli proof.

Reproduce using `python3 check_random_transposition.py` from the two-file extraction directory, using only Python standard-library modules.

## Relationship to prior work

Jamilov's permutation quadratic stochastic operators provide the nonlinear model and the fixed-permutation trajectory results; those autonomous results are not claimed. The general framework of pairwise randomized averaging, including mean-square convergence of gossip algorithms, is established by Boyd, Ghosh, Prabhakar and Shah. Bajović, Xavier, Moura and Sinopoli establish general exact rates for convergence in probability of random stochastic-matrix products. The present statement specifies, for the smallest fully connected three-agent exchange among the peripheral coordinates, the **complete finite-time signed path reduction**, **all positive moments**, **joint endpoint law**, and **explicit fluctuation exponent**, not merely an expectation-rate bound. An earlier random Volterra-operator paper concerns convergence to simplex vertices for a different family, rather than peripheral consensus for this non-Volterra operator.

## Limitations

The exact binomial structure uses three peripheral coordinates, uniformly and independently selected transpositions, and the singular exchange value \(\alpha=1/2\). It is not asserted for higher dimensions or biased, correlated, or nonprojective switching. Genericity is essential to the logarithmic almost-sure statement: if the initial composition lies on one of the three orthogonality lines, a first selected projection can give exact consensus with positive probability. The finite enumeration is not a proof for arbitrary horizons. Priority relative to unavailable full texts and potentially equivalent classical gossip special cases is not independently settled; full literature review and independent audit remain outstanding.

## References

1. U. U. Jamilov, *A family of non-Volterra quadratic operators corresponding to permutations*, arXiv:2210.05107 (first public 2022-10-11), https://arxiv.org/abs/2210.05107.
2. U. U. Jamilov, K. O. Khudoyberdiev, M. Ladra, *Quadratic operators corresponding to permutations*, Stochastic Analysis and Applications (2020), https://doi.org/10.1080/07362994.2020.1747494.
3. S. Boyd, A. Ghosh, B. Prabhakar, D. Shah, *Randomized Gossip Algorithms*, IEEE Trans. Inf. Theory (2006), https://web.stanford.edu/~boyd/papers/pdf/gossip.pdf.
4. D. Bajović, J. Xavier, J. M. F. Moura, B. Sinopoli, *Consensus and Products of Random Stochastic Matrices: Exact Rate for Convergence in Probability*, arXiv:1202.6389, https://arxiv.org/abs/1202.6389.
5. U. U. Jamilov, K. O. Khudoyberdiev, *On the dynamics of non-Volterra quadratic operators corresponding to permutations*, Journal of Difference Equations and Applications (2023), https://doi.org/10.1080/10236198.2023.2284827.
6. U. U. Jamilov, M. Scheutzow, M. Wilke-Berenguer, *On the Random Dynamics of Volterra Quadratic Operators*, arXiv:1401.7840, https://arxiv.org/abs/1401.7840.
