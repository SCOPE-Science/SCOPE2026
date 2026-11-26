# Three spatial covariance phases linking Wilcoxon rank sums and Wald–Wolfowitz runs

## Finding

Fix integers \(a,b\ge1\), put \(N=a+b\ge4\), and draw a binary word uniformly among all words with exactly \(a\) ones and \(b\) zeros. Let \(X_i\) be its indicator at rank \(i\), and define the centered Wilcoxon rank sum and adjacent-change indicators by
\[
Y=\sum_{i=1}^N\left(i-\frac{N+1}{2}\right)X_i,\qquad
T_j=\mathbf1\{X_j\ne X_{j+1}\},\qquad R=1+\sum_{j=1}^{N-1}T_j.
\]
Write \(Q=ab\). For **every** \(1\le j<N\), the exact local covariance is
\[
\boxed{\operatorname{Cov}(Y^2,T_j)=\frac{2Q}{N(N-1)}\left[\frac{1-Q}{6}+\frac{N(N+1)-6Q}{(N-2)(N-3)}\left(\left(j-\frac N2\right)^2-\frac{N(N-2)}{12}\right)\right].}
\]
The linear Wilcoxon statistic is uncorrelated with the run count, yet its **squared** centered form has strictly negative covariance with the run count except for the two-label degenerate case:
\[
\boxed{\operatorname{Cov}(Y,R)=0,\qquad \operatorname{Cov}(Y^2,R)=\frac{Q(1-Q)}{3N}<0\quad (Q>1).}
\]
At a fixed boundary position the covariance has a quadratic spatial profile, admitting qualitatively opposite positive-covariance regions despite this universal negative total. For even \(N\ge6\), let
\[
Q_{\mathrm e}=\frac{N^2+N+1}{7},\qquad
Q_{\mathrm c}=\frac{N^3+N^2-2N+6}{4N+6}.
\]
These strict thresholds satisfy \(Q_{\mathrm e}<Q_{\mathrm c}\) and classify the *signs* of the local covariances: if \(Q<Q_{\mathrm e}\), the two outermost boundaries have positive covariance and the center has negative covariance; if \(Q_{\mathrm e}<Q<Q_{\mathrm c}\), all boundaries have negative covariance; and if \(Q>Q_{\mathrm c}\), the center has positive covariance and the outermost boundaries have negative covariance. At equality an endpoint or center covariance is zero; other boundary positions follow the displayed quadratic formula. These conditional alternatives may be empty for particular integer compositions. In particular, at \(N=8\), compositions \((a,b)=(1,7),(2,6),(4,4)\) respectively realize the three regimes.

## Assumptions and scope

The null distribution is uniform over the \(\binom Na\) fixed-composition binary words; it models a tie-free two-sample pooled rank sequence. No continuous-data distribution is specified beyond exchangeability of the group labels under the null. The local formula and threshold classification use \(N\ge4\); the total-covariance identity also holds by direct enumeration at \(N=2,3\). The value \(Y\) is the ordinary Wilcoxon rank sum minus its null mean, with no variance standardization. The run count includes maximal constant blocks, so it equals one plus the number of adjacent changes. The threshold statement for an even \(N\) compares the center boundary \(j=N/2\) and the two end boundaries \(j=1,N-1\).

## Proof

By fixed-composition sampling, \(\mathbb P(T_j=1)=2Q/[N(N-1)]\), the unconditional mean of \(Y\) is zero, and the ordinary finite-population variance formula gives \(\mathbb E[Y^2]=Q(N+1)/12\). Condition on \(T_j=1\). Exactly one of positions \(j,j+1\) is labelled one, with its choice uniform. The remaining \(a-1\) ones are uniformly placed in the other \(N-2\) positions. Set \(m_j=j-N/2\). The mean of the two adjacent rank weights is \(m_j\) and their individual centered deviations are \(\pm1/2\). The remaining weights sum to \(-2m_j\), and their squared sum is \(N(N^2-1)/12-2m_j^2-1/2\). The conditional mean and conditional variance are therefore
\[
\mathbb E[Y\mid T_j=1]=\frac{b-a}{N-2}m_j,
\]
\[
\operatorname{Var}(Y\mid T_j=1)=\frac14+
\frac{(a-1)(b-1)}{(N-2)(N-3)}\left[\frac{N(N^2-1)}{12}-\frac12-\frac{2N}{N-2}m_j^2\right].
\]
Here the finite-population variance identity also applies when one of the remaining label counts vanishes, giving the zero factor correctly. Adding the square of the conditional mean, then subtracting \(\mathbb E[Y^2]\), reduces by \(Q=ab\) to
\[
\mathbb E[Y^2\mid T_j=1]-\mathbb E[Y^2]=\frac{1-Q}{6}+B\left(m_j^2-\frac{N(N-2)}{12}\right),
\qquad B=\frac{N(N+1)-6Q}{(N-2)(N-3)}.
\]
Multiplication by \(\mathbb P(T_j=1)\) proves the local covariance identity. Since \(\sum_{j=1}^{N-1}m_j^2=N(N-1)(N-2)/12\), summing local covariances cancels the entire \(B\)-term and gives \(\operatorname{Cov}(Y^2,R)=Q(1-Q)/(3N)\). Word reversal maps \(Y\) to \(-Y\) while preserving \(R\), proving \(\operatorname{Cov}(Y,R)=0\).

For even \(N\), the conditional-square differences at the center and an endpoint are exactly
\[
\delta_{\mathrm c}=\frac{(4N+6)Q-(N^3+N^2-2N+6)}{12(N-3)},\qquad
\delta_{\mathrm e}=\frac{N^2+N+1-7Q}{6}.
\]
The positive factor \(\mathbb P(T_j=1)\) preserves their signs. The slope \(B\) of the quadratic profile as a function of \(m_j^2\) vanishes at \(Q_{\mathrm B}=N(N+1)/6\). Direct subtraction gives
\[
Q_{\mathrm c}-Q_{\mathrm B}=\frac{(N-3)(N-2)(N+3)}{6(2N+3)}>0,
\quad Q_{\mathrm B}-Q_{\mathrm e}=\frac{(N-2)(N+3)}{42}>0.
\]
Thus the extrema among the discrete boundary positions always occur at center or endpoint, with the orientation fixed by \(B\). The stated three regimes and exact threshold/equality cases follow from the two displayed endpoint formulas, without a continuity or asymptotic argument. At \(N=8\), exact evaluation gives all-negative local signs for \((2,6)\), central positive only for \((4,4)\), and outermost positive only for \((1,7)\).

## Verification

Run `python verify.py` with a standard Python 3 interpreter. It independently enumerates every fixed-composition word for \(4\le N\le11\), and checks all local covariance formulas and the total run covariance using exact fractions; it also checks all three eight-position regimes. A local execution passed 591 exact-rational assertions. Symbolic algebra was separately used to simplify the conditional-square coefficient, but the proof above is analytic. This finite enumeration is corroboration, not a substitute for the all-\(N\) derivation.

## Relationship to prior work

The marginal Wilcoxon rank-sum null law, the Wald–Wolfowitz runs null law, and ordinary fixed-composition indicator moments are classical and are not claimed as new. Bisewski, Jansen, and Nazarathy (2022) motivate tests sensitive to distinct aspects of ordering and empirical distribution and study a partially sorted empirical process; their full preprint does not state these fixed-composition mixed covariances. Holcombe (2025) writes both the classical two-sample runs and rank-sum tests in a common block-frequency language and discusses separate null properties; its examined Sections 3.2, 3.3, and 4.3 do not state this local quadratic mixed-moment formula or its composition phase classification. The contribution asserted here is the exact, position-resolved **second-order cross-covariance** and its contradictory local/aggregate sign regimes, not the formulas for the two marginal tests or an unqualified claim that their joint distribution was previously unknown.

## Limitations

Only second-order mixed moments under the tie-free permutation null are analyzed. No joint asymptotic distribution, joint-test calibration or power dominance is established. At odd \(N\), the exact quadratic formula applies but the center is attained at two neighboring boundaries, so the convenient even-\(N\) thresholds are not directly the odd-case criteria. Specialized historical studies of combined rank and run tests might contain an equivalent mixed-moment identity; priority is provisional pending fuller archival study and independent audit.

## References

1. K. Bisewski, H. M. Jansen, Y. Nazarathy, “Nonparametric testing via partial sorting,” arXiv:2210.14546v1, first posted 2022-10-26, https://arxiv.org/html/2210.14546v1.
2. C. Holcombe, “The Building Blocks of Classical Nonparametric Two-Sample Testing Procedures: Statistically Equivalent Blocks,” arXiv:2501.10844v1, 2025, https://arxiv.org/html/2501.10844v1.
3. A. Wald and J. Wolfowitz, “On a test whether two samples are from the same population,” Annals of Mathematical Statistics 11 (1940), 147–162.
4. F. Wilcoxon, “Individual comparisons by ranking methods,” Biometrics Bulletin 1 (1945), 80–83.
