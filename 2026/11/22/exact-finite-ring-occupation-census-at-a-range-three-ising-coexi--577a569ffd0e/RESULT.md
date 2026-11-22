# Exact finite-ring occupation census at a range-three Ising coexistence field

## Finding
For every integer \(n\ge7\), let \(\sigma_i\in\{0,1\}\) be spins on a cyclic ring, with subscripts taken modulo \(n\), and define
\[
E_n(\sigma;h)=J\sum_{i=0}^{n-1}\sum_{d=1}^3\mathbf1\{\sigma_i=\sigma_{i+d}\}-h\sum_{i=0}^{n-1}\sigma_i,\quad J>0.
\]
At \(h=10J/3\), one has \(E_n\ge -nJ\). Equality is attainable exactly for \(n\in\{8,9,10\}\cup\{12,13,\ldots\}\). Whenever attainable, the *entire* polynomial counting configurations attaining this bound by their occupied-spin number is
\[
P_n(y)=\sum_{\substack{a,b\ge0\\4a+5b=n}}\frac{n}{a+b}\binom{a+b}{a}y^{3(a+b)}.
\]
Consequently the coefficient at occupation number \(k\) is nonzero precisely for \(k=3(a+b)\) with \(4a+5b=n\); the displayed rational form always gives an integer. For \(n=7,11\), all states have strictly higher energy and the displayed sum is empty, not the actual ground-state polynomial.

For a uniformly chosen minimizing configuration at the coexistence field, let \(K_n=\sum_i\sigma_i\). With \(\lambda>1\) the unique positive root of \(\lambda^5=\lambda+1\), put \(p_4=\lambda^{-4}\), \(p_5=\lambda^{-5}\), and \(L=4p_4+5p_5\). Then
\[
\frac{K_n-\mu n}{\sqrt n}\Longrightarrow\mathcal N(0,v),\quad
\mu=\frac3L,\qquad v=\frac{9p_4p_5}{L^3}>0,
\]
with \(\operatorname{Var}(K_n)/n\to v\) and \(\mathbb E[K_n]/n\to\mu\), where \(n\) ranges through all sufficiently large integers. Numerically \(\mu\approx0.6724342484\) and \(v\approx0.0251867731\). The exact occupation polynomial, commensurability exceptions, and fluctuation coefficient are the contribution; the bulk phase boundary and residual entropy were previously established.

## Assumptions and scope
All \(2^n\) labeled binary configurations are distinct, with periodic boundaries and positive equal first-, second-, and third-neighbor same-spin penalties. Each unordered distance-\(d\) bond is counted once by the oriented sum for \(n\ge7\). The magnetic field couples to the number of \(1\) spins; converting to the conventional \(\pm1\) Ising normalization rescales its field. The result concerns the single specified coexistence field and does not classify off-field ground states. The Gaussian limit is for the uniform measure on its equality configurations, not for finite-temperature Gibbs measures.

## Proof
Write \(w(\sigma)=3E_n(\sigma;10J/3)/J\). Track the last three spins by a de Bruijn state \(a=b_0+2b_1+4b_2\in\{0,\ldots,7\}\), oldest first. Appending \(b\in\{0,1\}\) makes state \(j=\lfloor a/2\rfloor+4b\) and contributes \(3(\mathbf1\{b=b_0\}+\mathbf1\{b=b_1\}+\mathbf1\{b=b_2\})-10b\) to \(w\). Define the potential, indexed in increasing state order,
\[
(p_0,p_1,p_2,p_3,p_4,p_5,p_6,p_7)=(0,-3,-4,-9,-7,-10,-11,-12).
\]
Checking both outgoing arcs at each of eight states proves
\[
3(\mathbf1\{b=b_0\}+\mathbf1\{b=b_1\}+\mathbf1\{b=b_2\})-10b+3\ge p_j-p_a.
\]
Summing this inequality around a closed walk telescopes the potential and yields \(w(\sigma)+3n\ge0\). Equality requires every transition to be tight. Their complete directed edge list is
\[
0\to4,\quad1\to4,\quad3\to1,\quad3\to5,\quad4\to6,\quad5\to2,\quad5\to6,\quad6\to7,\quad7\to3.
\]
Vertices \(0,2\) occur in no closed tight walk. Every closed walk in the other six states is obtained by concatenating one of two excursions from state \(3\) back to state \(3\): \(3\to5\to6\to7\to3\) (four sites), or \(3\to1\to4\to6\to7\to3\) (five sites). Both append exactly three occupied spins. Their concatenations provide every minimizing spin configuration because length-\(n\) closed de Bruijn walks are in bijection with labeled periodic binary spin words. This gives the necessary and sufficient condition \(n=4a+5b\). For \(n\ge7\), the representable values are \(8,9,10\) and every \(n\ge12\) (the Frobenius gap for 4 and 5 is 11).

Fix nonnegative \(a,b\) with \(4a+5b=n\), and let \(t=a+b\). The number of cyclic-site-labeled walks consisting of \(a\) four-excursions and \(b\) five-excursions is \(\frac nt\binom ta\): mark one of the \(t\) occurrences of state 3, choose the corresponding order of excursion types, and then use the \(n\) possible marked site positions; each underlying labeled walk is counted \(t\) times. All have \(K_n=3t\). Summing gives \(P_n\).

Let \(B(y)\) be the six-state tight adjacency matrix with each transition weighted by \(y\) if it appends spin 1, otherwise by 1. Then \(P_n(y)=\operatorname{tr}B(y)^n\). The nonzero eigenvalues satisfy \(x^5=y^3(x+1)\); the remaining eigenvalue is zero. For real \(y>0\), the strongly connected six-state graph is primitive, since its two cycle lengths have gcd 1, and its simple Perron root \(\rho(y)\) is analytic near \(y=1\). Therefore the moment generating function of \(K_n\) has the uniform local form
\[
\log\mathbb E e^{tK_n}=n(\log\rho(e^t)-\log\rho(1))+O(\theta^n)
\]
for \(t\) in a fixed complex neighborhood of zero and some \(0<\theta<1\). Analytic differentiation gives the mean and variance limits and the characteristic-function Taylor expansion gives the Gaussian limit. Differentiating \(\rho(y)^5=y^3(\rho(y)+1)\), or equivalently using excursion probabilities \(p_4=\lambda^{-4},p_5=\lambda^{-5}\) with \(p_4+p_5=1\), gives \(\mu=3/L\) and \(v=9p_4p_5/L^3\). The limit variance is strictly positive since both excursion types occur.

## Verification
Run the standalone Python 3 script `verify.py` without nonstandard dependencies. It checks all 16 potential inequalities, the exact tight-edge set, equality polynomials against exhaustive enumeration of all \(2^n\) configurations for \(7\le n\le19\), and independently compares the unweighted six-state transfer trace against the polynomial formula for \(1\le n\le150\). These finite checks corroborate but are not substitutes for the all-size arguments above.

## Relationship to prior work
Gastner (2015) demonstrated that occupation constraints and finite ring size can change Ising magnetization statistics, for nearest-neighbor chains. Zarubin, Kassan-Ogly and Proshkin (2020) treated zero-field Ising chains with interactions through the third neighbor. More decisively, Zarubin and Kassan-Ogly (2022) studied the *same first-through-third-neighbor field-dependent model* by an eight-state transfer matrix and determined its bulk phase boundaries, residual entropy, and magnetization. Their general finite-volume transfer expression can in principle encode the present finite counts. The present result does not re-claim any of those bulk conclusions: it gives an explicit finite-ring occupied-site polynomial, the sharp ring-size attainment exceptions, a two-excursion equality-state bijection, and a critical occupation central-limit law and exact fluctuation coefficient. No claim of priority over unpublished or unindexed derivations is made.

## Limitations
This result concerns one equal-coupling coexistence field and rings of length at least seven. At sizes seven and eleven the universal bound is strict; their actual minimum energies are not classified by this theorem. It neither establishes uniqueness of any phase boundary nor a finite-temperature critical phenomenon. The full finite-volume transfer representation in Zarubin and Kassan-Ogly (2022) is a substantial prior-art overlap: it could support a different derivation of these specialized finite-size results; historical priority of the explicit formulas requires independent checking. Gaussian convergence is asymptotic; the finite-size law is discrete.

## References
- M. T. Gastner, *The Ising chain constrained to an even or odd number of positive spins*, arXiv:1502.02883 (first public 2015-02-10), https://arxiv.org/abs/1502.02883.
- A. V. Zarubin, F. A. Kassan-Ogly and E. B. Proshkin, *On the ground-state frustration of the Ising model with interactions up to the third neighbors*, arXiv:2002.05430 (2020), https://arxiv.org/abs/2002.05430.
- A. V. Zarubin and F. A. Kassan-Ogly, *Frustration and ordering in Ising chain in an external magnetic field with third-neighbor interactions*, arXiv:2206.06753 (first public 2022-06-14), https://arxiv.org/abs/2206.06753.
