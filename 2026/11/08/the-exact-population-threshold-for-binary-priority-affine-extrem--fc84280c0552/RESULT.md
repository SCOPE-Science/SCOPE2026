# The exact population threshold for binary-priority affine extremality

## Finding

In a complete-conflict priority game with two levels and a fixed deterministic total-order tie-breaker, **affine rank payoffs maximize the potential-energy share precisely for populations of at most six agents**. For every integer \(N\ge 7\) there is a strictly decreasing rank payoff with potential-energy share larger than the affine benchmark \((N-1)/N\). The previously known seven-agent witness handles \(N=7\); the new contribution is a single analytic witness for **all** \(N\ge8\).

Specifically, at every integer \(N\ge2\), choose the rank payoff (rank \(r=1\) is best)
\[
f_N(r)=-\frac{r(r-1)}2,\qquad r\in\{1,\ldots,N\}.
\]
Its potential-energy share under uniform weighting of unilateral moves is exactly
\[
\rho_{\mathrm{pot}}(f_N)=1-\frac{(N+1)(25N-18)}{2N(13N^2-N-2)},
\]
and hence
\[
\rho_{\mathrm{pot}}(f_N)-\frac{N-1}{N}
=\frac{(N-2)(N-7)}{2N(13N^2-N-2)}.
\]
This is strictly positive for every integer \(N\ge8\); at \(N=8\) the share is exactly \(1919/2192\), exceeding \(7/8\) by \(1/2192\). The excess is asymptotic to \(1/(26N)\), not a claim of optimality among nonlinear payoffs.

## Assumptions and scope

There are \(N\ge2\) agents, with complete conflict graph and two pure priority levels \(s_i\in\{0,1\}\). Higher priority acts first. A tie is broken by the same fixed total order, which after relabeling is \(1\prec2\prec\cdots\prec N\); a smaller index acts earlier. Every agent's payoff is \(f_N(r_i(s))\), where \(r_i(s)\) is its service rank in the resulting strict order. There are no transfers or action-dependent costs. The nonlinear payoff is strictly decreasing because \(f_N(r)-f_N(r+1)=r>0\) for \(1\le r<N\).

Let \(d_i(s_{-i})=u_i(1,s_{-i})-u_i(0,s_{-i})\). Each upward unilateral edge is given equal weight; divide energies by the same factor \(2^{N-1}\) without changing their ratio. Set
\[
\mathcal T=\sum_{i=1}^N 2^{-(N-1)}\sum_{s_{-i}}d_i(s_{-i})^2,
\qquad
\mathcal P=\mathcal T-\min_{\Phi:\{0,1\}^N\to\mathbb R}
\sum_i2^{-(N-1)}\sum_{s_{-i}}
\bigl[d_i(s_{-i})-\Phi(1,s_{-i})+\Phi(0,s_{-i})\bigr]^2.
\]
Thus \(\mathcal P\) is precisely the squared norm of the orthogonal projection of the unilateral-gain field \(d\) onto gradient fields. Let \(\mathcal H=\mathcal T-\mathcal P\) and \(\rho_{\mathrm{pot}}=\mathcal P/\mathcal T\), with \(\mathcal T>0\).

## Proof

**1. Incentive field.** For agent \(i\) (one-based index) put \(A_i=\sum_{j<i}s_j\), \(B_i=\sum_{j>i}s_j\). When agent \(i\) chooses high priority its rank is \(1+A_i\); when it chooses low priority its rank is \(i+B_i\). Therefore
\[
d_i=\frac{(i+B_i)(i+B_i-1)-(1+A_i)A_i}{2}
=\frac{i(i-1)}2+iB_i-A_i
+\sum_{i<j<k}s_js_k-\sum_{j<k<i}s_js_k.
\]
Thus its dependence on opponents has degree at most two.

**2. Exact Fourier projection.** Put \(\chi_j=2s_j-1\) and expand each \(d_i\) in the orthonormal Walsh basis of opponents, writing \(\widehat d_i(S)\) for the coefficient on \(\prod_{j\in S}\chi_j\). The preceding formula gives
\[
\begin{aligned}
\widehat d_i(\varnothing)&=c_i=\frac{N^2+2Ni-N-4i+2}{8},\\
\widehat d_i(\{j\})&=\begin{cases}-i/4,&j<i,\\ (N+i-1)/4,&j>i,\end{cases}\\
\widehat d_i(\{j,k\})&=\begin{cases}-1/4,&j,k<i,\\+1/4,&j,k>i,\\0,&\text{otherwise}.\end{cases}
\end{aligned}
\]
All coefficients at degree three or above vanish. A potential \(\Phi=\sum_{S}\widehat\Phi(S)\prod_{j\in S}\chi_j\) has edge difference \(\Delta_i\Phi=2\sum_{S\ni i}\widehat\Phi(S)\prod_{j\in S\setminus\{i\}}\chi_j\). Orthogonal least squares on each nonempty \(S\) therefore yields
\[
\mathcal P=\sum_{\varnothing\ne S\subseteq[N]}
\frac1{|S|}\left(\sum_{i\in S}\widehat d_i(S\setminus\{i\})\right)^2,
\qquad
\mathcal T=\sum_i\sum_{S\subseteq[N]\setminus\{i\}}\widehat d_i(S)^2.
\]
This is a direct finite-dimensional derivation of the Hodge projection, not an assumption about best-response dynamics.

**3. Harmonic energy.** Singleton terms contribute no residual. For each pair \(i<j\), the coefficient pair is \(((N+i-1)/4,-j/4)\), and the squared residual after projection onto the equal-coordinate line is \((N+i+j-1)^2/32\). For each triple \(i<j<k\), the three coefficient entries are \((1/4,0,-1/4)\), with zero projection and residual \(1/8\). There are no higher-order contributions. Hence
\[
\mathcal H=
\sum_{1\le i<j\le N}\frac{(N+i+j-1)^2}{32}+\frac18\binom N3
=\frac{N(N-1)(N+1)(25N-18)}{384}.
\]

**4. Total energy.** Parseval's identity using the displayed coefficients gives
\[
\begin{aligned}
\mathcal T
&=\sum_{i=1}^N\left[c_i^2+
\frac{(i-1)i^2+(N-i)(N+i-1)^2}{16}
+\frac{\binom{i-1}{2}+\binom{N-i}{2}}{16}\right]\\
&=\frac{N^2(N-1)(13N^2-N-2)}{192}.
\end{aligned}
\]
Both final equalities follow from finite sums of integer powers (and the usual binomial formulas), with no asymptotic interchange. In particular \(\mathcal T>0\) for \(N\ge2\).

**5. Comparison and sharp threshold.** Dividing \(\mathcal H\) by \(\mathcal T\) gives the exact share and its difference from \((N-1)/N\). The denominator is positive for \(N\ge2\), so the sign is the sign of \((N-2)(N-7)\). This proves the new strict improvement for every \(N\ge8\). For \(N\le6\), Lin–Lan–Nguyen–Kawahara proved positive semidefiniteness of the complete-game binary-priority comparison quadratic form (Supplement, Section S-N), which establishes global affine optimality; the statement is also reproduced independently using exact finite matrices in the checker. For \(N=7\), the same publication supplied an exact, distinct strictly decreasing witness, with rank increments \((9,8,6,4,2,1)\) and share \(53454277/62354880>6/7\). Together these facts give the complete threshold.

## Verification

Run `python3 check_priority.py` using Python 3.8 or newer (Python 3.10 or newer is required for `int.bit_count`). No third-party dependencies are needed. The checker computes each unilateral gain from literal service ranks, takes an exact rational Walsh transform over every opponent profile, reconstructs both energies and their difference, and compares the resulting fractions with the above formulas for every integer population from two through nine. It also establishes, through exact Gram matrices and positive Schur pivots, the affine optimality comparison for all populations of at most six, and reproduces the published seven-agent witness share exactly. These finite computations supplement the displayed symbolic proof for all \(N\); they are not a substitute for it.

## Relationship to prior work

Lin, Lan, Nguyen and Kawahara (arXiv:2610.05832v1; October 5, 2026) prove affine optimality for at least three priority levels, certify the binary-priority comparison as positive semidefinite for populations through six, and give the seven-agent counterexample. They explicitly leave the set of population sizes where binary affine extremality fails open (conclusion, PDF p. 12, and supplement pp. 14–15). Their table lists floating-point evidence of failure at some sizes from seven to twelve but warns that these entries are **not part of a proof**. Those numerical signs, the published seven-agent witness, and the small-population positive semidefiniteness are *not claimed as new*. The contribution here is an explicit all-population analytic witness and closed-form energy identities that prove failure for every \(N\ge8\).

## Limitations

The result assumes a complete conflict graph, exactly two priority levels, a deterministic global tie-breaker, and uniform weighting of the unilateral edges. It concerns the relative squared projection energy, not welfare or physical safety. It does not assert that the displayed nonlinear payoff maximizes the potential share, nor does it determine the optimal excess for each population. No conclusion is drawn for random tie-breaking, sparse graphs, larger priority alphabets, or nonlinear learning dynamics. Other unpublished or unindexed derivations of the all-population witness cannot be excluded.

## References

1. Z. Lin, J. Lan, A.-T. Nguyen and Y. Kawahara, *Priority Coordination Games: Hodge Decomposition and a Sharp Design Limit*, arXiv:2610.05832v1 (first public October 5, 2026), https://arxiv.org/pdf/2610.05832 . See Sections V–VI, VIII, Supplement Sections S-N and S-E, and Table S3.
