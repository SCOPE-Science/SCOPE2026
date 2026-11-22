# Random-erasure Fourier-frame fluctuations and ambiguity-flatness rigidity

## Finding

For every integer \(N\geq 2\), every unit vector \(g\in\mathbb C^N\), and every uniformly chosen subset \(R\subseteq\mathbb Z_N^2\) with \(|R|=m\), the trace-square \(Q_R=\operatorname{tr}(S_R^2)\) of the retained Gabor frame operator has an exact mean and variance. Put \(n=N^2\), and define
\[
\mathcal D(g)=\sum_{(a,b)\ne(0,0)}\left(\left|\langle g,M_bT_ag\rangle\right|^2-\frac1{N+1}\right)^2.
\]
Then, for every \(0\leq m\leq n\),
\[
\mathbb E Q_R=m+\frac{m(m-1)}{N+1},\qquad
\operatorname{Var}(Q_R)=\frac{2m(m-1)(n-m)(n-m-1)}{(n-1)(n-2)(n-3)}\,\mathcal D(g).
\]
Moreover,
\[
0\leq\mathcal D(g)\leq\frac{N(N-1)}{N+1}.
\]
The lower equality holds exactly when the full Gabor orbit is an equiangular tight frame (a Weyl--Heisenberg SIC), if such a window exists. The upper equality holds exactly for a stabilizer window: a common eigenvector of a maximal commuting subgroup of projective time--frequency shifts of order \(N\). In particular, the upper variance bound is attained in every dimension by a coordinate impulse. For \(2\leq m\leq n-2\), these are also the precise equality conditions for the respective variance bounds; at the four trivial mask sizes \(m\in\{0,1,n-1,n\}\) variance vanishes for all windows.

When \(N=p\geq5\) is prime and \(g(j)=p^{-1/2}\exp(2\pi i j^3/p)\), the Alltop window satisfies
\[
\mathcal D(g)=\frac{p-1}{p(p+1)},
\]
so its random-erasure trace-square variance is exactly \(p^{-2}\) of the maximum over all windows at the same dimension and retained cardinality.

## Assumptions and scope

Use the Hilbert-space inner product \(\langle u,v\rangle=\sum_{j=0}^{N-1}\overline{u(j)}v(j)\), with \(T_ag(j)=g(j-a\bmod N)\), \(M_bg(j)=\exp(2\pi i bj/N)g(j)\), and \(v_{a,b}=M_bT_ag\). The full family contains \(n=N^2\) *labelled* unit vectors even when some are proportional. Its frame operator is \(\sum_{a,b}v_{a,b}v_{a,b}^*=NI_N\). The retained operator is \(S_R=\sum_{(a,b)\in R}v_{a,b}v_{a,b}^*\). Subsets are sampled uniformly without replacement from the labelled family, not independently by Bernoulli sampling. All expectations are solely over the choice of \(R\), and \(g\) is deterministic.

A stabilizer window is any unit vector that is a simultaneous eigenvector of \(\{M_bT_a:(a,b)\in H\}\) up to phases for a subgroup \(H\leq\mathbb Z_N^2\) of order \(N\) on which \((a,b),(a',b')\mapsto ab'-a'b\) vanishes modulo \(N\). A SIC window has all nontrivial squared ambiguities equal to \(1/(N+1)\). No existence assertion for SIC windows in every \(N\) is made.

## Proof

**1. Tightness and regularity.** Summation over all modulations kills off-diagonal entries of \(\sum_{a,b}v_{a,b}v_{a,b}^*\), while summation over all translations makes each diagonal equal to \(N\). Thus the full operator is \(NI_N\). Define \(w_{xy}=|\langle v_x,v_y\rangle|^2\) for distinct labels \(x,y\in\mathbb Z_N^2\). Its weighted row sum is exactly \(N-1\), because \(\sum_y|\langle v_x,v_y\rangle|^2=N\). Consequently the mean off-diagonal squared correlation is \(\mu=(N-1)/(N^2-1)=1/(N+1)\). Weyl covariance gives \(w_{xy}=|\langle g,M_{y_b-x_b}T_{y_a-x_a}g\rangle|^2\), up to harmless unit phases.

**2. Fixed-size sampling identity.** Write \(X_R=\sum_{\{x,y\}\subset R}w_{xy}\), so \(Q_R=m+2X_R\). Let \(W=\sum_{x<y}w_{xy}=n(N-1)/2\), \(A=\sum_{x<y}w_{xy}^2\), and let \(B\) be the sum of \(w_{xy}w_{xz}\) over unordered pairs of distinct edges sharing a vertex. Row regularity gives \(B=n(N-1)^2/2-A\). Put \(p_r=(m)_r/(n)_r\) for \(r=2,3,4\), with \((t)_r=t(t-1)\cdots(t-r+1)\). Classifying pairs of edges by whether they coincide, share one endpoint, or are disjoint gives
\[
\mathbb E X_R^2=(p_2-p_4)A+2(p_3-p_4)B+p_4W^2,
\quad \mathbb E X_R=p_2W.
\]
A simplification yields
\[
\operatorname{Var}(X_R)=c_{n,m}\left(A-\binom n2\mu^2\right),\quad
c_{n,m}=\frac{m(m-1)(n-m)(n-m-1)}{n(n-1)(n-2)(n-3)}.
\]
By group-translation covariance, \(A-\binom n2\mu^2=\frac n2\mathcal D(g)\), proving the stated variance identity. Similarly \(\mathbb E Q_R=m+2p_2W\) is the displayed mean. These formulas are valid at every boundary \(0\le m\le n\) (and \(n\ge4\)).

**3. Sharp range and equality cases.** Each nonzero squared ambiguity \(u_z=|\langle g,M_bT_ag\rangle|^2\) lies in \([0,1]\), and Weyl orthogonality gives \(\sum_{z\ne0}u_z=N-1\). Hence
\[
\mathcal D(g)=\sum_{z\ne0}u_z^2-\frac{N-1}{N+1}\in\left[0,\frac{N(N-1)}{N+1}\right].
\]
The lower endpoint is equivalent to \(u_z=\mu\) for all \(z\ne0\), precisely the SIC property. The upper endpoint requires every \(u_z\) to equal zero or one. The set \(H=\{z:u_z=1\}\), including \(z=0\), is a subgroup because every corresponding shift maps \(g\) to a scalar multiple of itself. Any two shifts in \(H\) commute on \(g\); their scalar commutator must therefore equal one, so \(H\) is isotropic. The identity \(\sum_z u_z=N\) implies \(|H|=N\), making \(H\) maximal isotropic. Thus \(g\) is a stabilizer window. Conversely, an eigenvector of any such maximal isotropic subgroup has \(u_z=1\) on it and \(u_z=0\) off it: for any \(z\notin H=H^\perp\), a member of \(H\) has a nontrivial commutator with \(z\), forcing \(\langle g,M_bT_ag\rangle=0\). Coordinate impulses give explicit maximizers. Since \(c_{n,m}>0\) exactly for \(2\le m\le n-2\), the variance equality descriptions follow.

**4. Alltop comparison.** For a prime \(p\ge5\), the Alltop cubic phase has \(u_{0,b}=0\) for \(b\ne0\). For \(a\ne0\), the phase difference \((j-a)^3-j^3\) has a nonzero quadratic term, so its complete additive-character sum has magnitude \(\sqrt p\), giving \(u_{a,b}=1/p\). There are \(p-1\) nonzero shifts of the first type and \(p(p-1)\) of the second. Substitution yields \(\mathcal D=(p-1)/(p(p+1))\), a factor of \(p^{-2}\) below the sharp maximum.

## Verification

Run `python CHECK.py` with Python 3.9 or newer. It requires only the standard library. The checker directly enumerates all fixed-size erasure subsets of four different Gabor windows in dimensions two and three, checks the Alltop ambiguity magnitudes in dimensions five and seven, and uses exact integer combinatorics and rational arithmetic to compare occupancy-based moments at six erasure sizes in dimension five. It tests the formulas but does not replace the general argument, the isotropic-subgroup proof, or a comprehensive bibliographic search.

## Relationship to prior work

Salanevich and Strachan, *Robustness to noise and erasures of Gabor frames in finite dimensions* (arXiv:2509.01325, first public September 1, 2025), study frame bounds for structured and random Gabor subframes and obtain a deterministic frame-potential formula for mutually unbiased basis subframes. In particular, their formula already determines the Alltop trace-square for each fixed mask, so the Alltop evaluation above is a derived comparison rather than a separately asserted novel theorem. The result here concerns the **exact fixed-cardinality sampling variance for every unit window**, plus its complete ambiguity-based extremal characterization; this covariance statistic and stabilizer-versus-SIC rigidity do not appear in the inspected assertions.

Haikin, Zamir and Gavish, *Frame Moments and Welch Bound with Erasures* (arXiv:1801.04548, first public January 14, 2018), prove Bernoulli-erasure bounds on expectations of individual spectral moments \(\mathbb E\operatorname{tr}(S^d)\) through order four. Such single-trace expectations are distinct from the covariance \(\operatorname{Var}(\operatorname{tr}S^2)\) under a uniform fixed-size mask. The frame-potential context and ETF lower-equality theme are acknowledged; neither paper is claimed to settle the existence of SICs.

## Limitations

Variance of \(Q_R\) is not variance of an extremal frame bound, a condition number, a reconstruction error or a full eigenvalue distribution. Its vanishing at a SIC window does not mean every erased subframe has the same spectrum. The claimed universal lower value zero is attained only in those dimensions where a Weyl--Heisenberg SIC window exists. The Alltop comparison is restricted to primes at least five, and it is not a bound for arbitrary random windows. An unlocated equivalent covariance formula in finite-population sampling or frame-potential literature remains a residual originality risk.

## References

1. P. Salanevich and N. Q. D. Strachan, *Robustness to noise and erasures of Gabor frames in finite dimensions*, arXiv:2509.01325, first version September 1, 2025. https://arxiv.org/abs/2509.01325
2. M. Haikin, R. Zamir and M. Gavish, *Frame Moments and Welch Bound with Erasures*, arXiv:1801.04548, first version January 14, 2018. https://arxiv.org/abs/1801.04548
3. D. J. Alltop, *Complex sequences with low periodic correlations*, IEEE Transactions on Information Theory 26 (1980), 350--354. The Alltop MUB property and original citation are also recorded in Reference 1.
