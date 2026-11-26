# Parameter-blind digit laws and exact temporal fluctuations in a bounded-digit random Lüroth map

## Finding

For the six-cell bounded-digit random Lüroth system described below, let the first map be chosen independently with probability \(p\in[0,1]\) at each iteration and begin with the absolutely continuous stationary distribution. The entire stationary six-cell itinerary, and hence the complete two-symbol digit process, has **the same probability law for every \(p\)**. In particular, no estimator based solely on a stationary sequence of digits can identify the switching probability.

Writing \(B_n=\mathbf1_{\{D_n=3\}}\), where \(D_n\in\{2,3\}\) is the Lüroth digit at time \(n\), the exact temporal statistics, for all integers \(n\geq0\), are
\[
\mathbb EB_n=\frac3{16},\qquad
\operatorname{Cov}(B_0,B_n)=
\begin{cases}\frac{39}{256},&n=0,\\[2pt]
\frac3{256}\left(-\frac13\right)^n,&n\ge1.
\end{cases}
\]
For every integer \(N\ge1\), put \(S_N=\sum_{j=0}^{N-1}(B_j-3/16)\). Then
\[
\operatorname{Var}(S_N)=\frac{75}{512}N+
\frac9{2048}\left(1-\left(-\frac13\right)^N\right),
\qquad
\frac{S_N}{\sqrt N}\Longrightarrow \mathcal N\!\left(0,\frac{75}{512}\right).
\]
Despite being a factor of a six-state Markov chain, the two-symbol digit process is not itself first-order Markov:
\[
\mathbb P(D_2=3\mid D_0=3,D_1=2)=\frac15,
\quad
\mathbb P(D_2=3\mid D_0=2,D_1=2)=\frac4{21}.
\]
The probabilities above and the convergence are with respect to the stationary initial law and the independent map choices; the statements do not concern arbitrary nonstationary initial distributions.

## Assumptions and scope

Let \(I=[1/3,1]\), and divide it into six intervals with consecutive endpoints
\[
(z_0,z_1,z_2,z_3,z_4,z_5,z_6)
=\left(\frac13,\frac7{18},\frac49,\frac12,\frac23,\frac56,1\right).
\]
Let \(I_i\) be the interval with endpoints \(z_{i-1},z_i\). Any consistent assignment of finitely many partition endpoints may be used; they form a null set for the stationary law. Define two piecewise affine maps by their slope/intercept pairs \((a_i,b_i)\), meaning \(T_j(x)=a_i x+b_i\) for \(x\in I_i\):
\[
\begin{array}{c|rrrrrr}
 &I_1&I_2&I_3&I_4&I_5&I_6\\\hline
 T_0&(-6,3)&(6,-2)&(6,-2)&(-2,2)&(2,-1)&(2,-1)\\
 T_1&(-6,3)&(-6,3)&(6,-2)&(-2,2)&(-2,2)&(2,-1)
\end{array}.
\]
These are exactly the bounded-digit restrictions of the Lüroth/alternating-Lüroth branches in Kalle and Maggioni's six-cell example [1, §7]. Given \(X_n\), let \(X_{n+1}=T_{\xi_n}(X_n)\), with independent choices \(\mathbb P(\xi_n=0)=p\) and \(\mathbb P(\xi_n=1)=1-p\). The stationary starting density is
\[
h(x)=\frac98\mathbf1_{[1/3,2/3]}(x)+
\frac{15}{8}\mathbf1_{(2/3,1]}(x).
\]
Define the six-cell observation \(Y_n=i\) when \(X_n\in I_i\). The binary digit equals \(3\) on \(I_1\cup I_2\cup I_3\) and \(2\) on \(I_4\cup I_5\cup I_6\).

## Proof

**1. Common Markov geometry.** On each \(I_i\), *both* maps are affine bijections onto the same destination interval: \([2/3,1]\) for \(i\in\{1,3,4,6\}\), and \([1/3,2/3]\) for \(i\in\{2,5\}\). Every destination has length \(1/3\). Each map has the same absolute slope on a given cell; its orientation may differ. Therefore, conditional on being uniform in a source cell, the next position, conditional on either map choice, is uniform on that common destination interval. Conditioning successively on any finite history of visited cells preserves uniformity within the newest cell; this follows inductively because every allowed transition is the restriction of an affine onto branch to the whole destination cell. The map-choice mixture does not change this conditional distribution. Thus the entire stationary cell itinerary is a Markov chain with transition probabilities equal to three times the destination/cell overlap lengths, independently of \(p\):
\[
P=\begin{pmatrix}
0&0&0&0&1/2&1/2\\
1/6&1/6&1/6&1/2&0&0\\
0&0&0&0&1/2&1/2\\
0&0&0&0&1/2&1/2\\
1/6&1/6&1/6&1/2&0&0\\
0&0&0&0&1/2&1/2
\end{pmatrix}.
\]
Direct multiplication yields the invariant row distribution
\[
\pi=(1,1,1,3,5,5)/16,\qquad \pi P=\pi.
\]
The corresponding density obtained by dividing cell masses by lengths is precisely \(h\) above; this also proves stationarity directly for every \(p\), including \(p=0,1/2,1\). Since every finite cylinder probability equals \(\pi_{i_0}P_{i_0i_1}\cdots P_{i_{k-1}i_k}\), **all** stationary cell and digit finite-dimensional distributions are independent of \(p\). Equal laws make statistical identification of \(p\) from digits alone impossible under stationary sampling.

**2. Exact covariance.** Set \(f=(1,1,1,0,0,0)^\mathsf T\) and \(g=f-(3/16)\mathbf1\). Explicit matrix multiplication gives
\[
\pi f=\frac3{16},\qquad P^2g=-\frac13Pg,\qquad
\sum_i\pi_i g_i^2=\frac{39}{256},\qquad
\sum_i\pi_i g_i(Pg)_i=-\frac1{256}.
\]
Consequently, for every \(n\ge1\),
\[
\operatorname{Cov}(B_0,B_n)
=\sum_i\pi_i g_i(P^ng)_i
= -\frac1{256}\left(-\frac13\right)^{n-1}
=\frac3{256}\left(-\frac13\right)^n.
\]
These are exact identities for every lag, not a numerical truncation.

**3. Finite-horizon variance and limit law.** Stationarity gives
\[
\operatorname{Var}(S_N)
=N\operatorname{Cov}(B_0,B_0)
+2\sum_{k=1}^{N-1}(N-k)\operatorname{Cov}(B_0,B_k).
\]
Substitute the geometric covariance formula and sum the finite progression. This yields the claimed expression and the strictly positive asymptotic variance \(75/512\). The matrix \(P\) is irreducible and aperiodic: all six states communicate, and the second state has a positive self-loop. The stationary finite-state Markov-chain central limit theorem for the bounded additive observable \(f\) therefore supplies the Gaussian limit with this variance. No assertion of a corresponding central limit theorem for arbitrary nonstationary initialization is needed.

**4. The binary factor is not Markov of order one.** Multiplication with the appropriate diagonal digit projections gives the joint probabilities
\[
\mathbb P(3,2,3)=\frac1{32},\quad
\mathbb P(3,2)=\frac5{32},\quad
\mathbb P(2,2,3)=\frac18,\quad
\mathbb P(2,2)=\frac{21}{32}.
\]
The two resulting conditional transition probabilities are respectively \(1/5\) and \(4/21\), which are unequal. This rules out a one-step Markov digit process, even though its six-cell refinement is Markov.

## Verification

The standalone standard-library Python file `verify.py` checks all twelve affine branch images and absolute slopes using rational arithmetic, reconstructs all six Markov rows from exact interval overlap, checks the stationary density and vector, the matrix identity \(P^2g=-Pg/3\), covariance formulas at lags \(0\) through \(69\), finite-time variances for \(1\le N\le99\), and the four joint probabilities used in the non-Markov witness. Execute `python3 verify.py` from the package directory. The unbounded-lag and CLT statements are proved in the preceding text; finite checks are consistency tests rather than their justification.

## Relationship to prior work

Kalle and Maggioni [1, §7] introduced this exact six-cell random Lüroth system and computed the stationary density and single-digit frequencies \(13/16\) and \(3/16\). Those facts and the underlying maps are **prior results**, not new claims here. Their main density construction and its §7 application do not state the all-length parameter-blind symbolic law, exact oscillating correlations, finite-horizon variance, Gaussian limit coefficient, or failure of the two-digit Markov property. The follow-up [2] treats related random \(c\)-Lüroth systems, Markov partitions and digit frequencies, rather than these exact full-process formulas. The contribution here is the explicit refinement from one-time frequencies to complete temporal statistics and parameter identifiability, not a new general Markov partition method. General finite-state Markov theory is used as established background.

## Limitations

Only the specified bounded-digit six-cell system and its stationary absolutely continuous initial measure are covered. Identical digit laws do not imply identical full real-valued orbit laws, nor do they prohibit estimating \(p\) from observations that include map choices or detailed real-valued states. The result does not classify arbitrary holes, nonstationary trajectories, or higher-digit restrictions. The relevant first preprint version of [1] is dated 2018, but the readily inspected complete online text is its revised 2020 version; publication priority for the precise bounded-digit example should be assessed accordingly. Unindexed equivalent symbolic calculations cannot be excluded; the results have not undergone independent audit.

## References

[1] C. Kalle and M. Maggioni, *Invariant densities for random systems of the interval*, arXiv:1805.11430, first posted 29 May 2018, revised 10 August 2020, §7; subsequently *Ergodic Theory and Dynamical Systems* 42 (2022), 141–179. https://arxiv.org/html/1805.11430v2

[2] C. Kalle and M. Maggioni, *On approximation by random Lüroth expansions*, arXiv:2101.01982 (2021), especially §4 and §5. https://arxiv.org/abs/2101.01982
