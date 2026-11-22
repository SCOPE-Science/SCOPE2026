# Unique fastest symmetric rejected-jump sampler on every finite interval

## Finding

For every integer \(n\ge 2\), among all state-independent, symmetric probability laws on integer displacements proposed to a random walker on \(\{1,\ldots,n\}\), with attempted moves leaving the interval rejected, there is a unique law minimizing the largest absolute nonstationary transition eigenvalue. It assigns probability \(1/[2(n-1)]\) to each of the \(2(n-1)\) displacements \(\pm1,\ldots,\pm(n-1)\), and no probability to zero or longer displacements.

The exact optimum is
\[
\min_p\mu(P_p)=\frac{n-2}{2(n-1)}=\frac12-\frac{1}{2(n-1)}.
\]
More quantitatively, writing \(a_s=p_s=p_{-s}\) for \(1\le s<n\), \(S=\sum_{s=1}^{n-1}a_s\), and \(\overline a=S/(n-1)\), every admissible law obeys the stability inequality
\[
\mu(P_p)\ge\frac{n-2}{2(n-1)}+
\frac{n}{n-1}\Big(\frac12-S\Big)+
\frac{n}{4(n-1)^{3/2}}
\left(\sum_{s=1}^{n-1}(a_s-\overline a)^2\right)^{1/2}.
\]
At the optimal law, with \(\Pi=\mathbf1\mathbf1^\top/n\),
\[
P_*=\Pi+\frac{n-2}{2(n-1)}(I-\Pi),\qquad
P_*^t=\Pi+\left[\frac{n-2}{2(n-1)}\right]^t(I-\Pi).
\]
Its stationary nonzero-move acceptance probability is exactly \(1/2\), and the total-variation distance after \(t\ge1\) steps from any fixed starting vertex is exactly \((1-1/n)[(n-2)/(2(n-1))]^t\). The case \(n=2\) mixes exactly after one step.

## Assumptions and scope

Fix an integer \(n\ge2\) and an arbitrary probability law \((p_k)_{k\in\mathbb Z}\) satisfying \(p_k\ge0\), \(\sum_{k\in\mathbb Z}p_k=1\), and \(p_k=p_{-k}\). At discrete times, independently draw a displacement \(K\) from this same law at every state. Starting at \(i\in\{1,\ldots,n\}\), replace \(i\) with \(i+K\) if the latter belongs to the interval; otherwise retain \(i\). A zero displacement also retains \(i\). No restriction on the support or moments of the proposal law is required. The resulting symmetric, doubly stochastic matrix \(P_p\) has uniform stationary law. Define \(\mu(P_p)=\|P_p-\Pi\|_{2\to2}\), equivalently the largest absolute eigenvalue on \(\mathbf1^\perp\). The minimization is over all such proposal laws, not arbitrary reversible kernels with state-dependent proposals.

The parameter \(S\in[0,1/2]\) is exactly the probability assigned to positive displacements still capable of moving from the left endpoint. The excess mass \(1-2S\) is placed at zero or displacement magnitudes at least \(n\), hence is wasted on every state. The coefficient multiplying the shape deviation in the displayed stability bound is valid, not claimed best possible.

## Proof

**1. Endpoint spectral obstruction.** Let \(e_1\) be the left endpoint coordinate vector, \(\mathbf1\) the all-ones vector, and \(x=(e_1-\mathbf1/n)/\sqrt{(n-1)/n}\). The transition matrix is symmetric and stochastic, and \(P_{11}=1-S\). Therefore
\[
\langle x,P_px\rangle=\frac{P_{11}-1/n}{1-1/n}
=\frac{n-2}{2(n-1)}+\frac{n}{n-1}\left(\frac12-S\right).
\]
By the Rayleigh principle on \(\mathbf1^\perp\), \(\mu(P_p)\) is at least this quantity. This establishes the universal lower bound \(d_n=(n-2)/[2(n-1)]\).

**2. Candidate attaining the obstruction.** Give every one of the \(2(n-1)\) nonzero displacements of magnitude at most \(n-1\) probability \(1/[2(n-1)]\). Every off-diagonal transition then has that probability and every diagonal transition has probability \(1/2\), because exactly half of the proposals from each endpoint, and an equal complementary collection at interior sites, are rejected. Thus
\[
P_{*,ij}=\begin{cases}
\frac12,&i=j,\\
\frac{1}{2(n-1)},&i\ne j,
\end{cases}
\qquad P_*=d_n I+(1-d_n)\Pi.
\]
All centered eigenvalues equal \(d_n\), so the lower bound is attained and the powers and total-variation formula follow.

**3. Strict rigidity and quantitative shape stability when \(S=1/2\).** Write \(\delta_s=a_s-1/[2(n-1)]\), so \(\sum_s\delta_s=0\), and \(\Delta=P_p-P_*\). Let \(L_s\) be the unweighted graph Laplacian whose edges join precisely those pairs of interval sites separated by \(s\). Then \(\Delta=-\sum_{s=1}^{n-1}\delta_s L_s\), \(\Delta\mathbf1=0\), and \(\|L_s\|_{2\to2}\le4\), since each vertex has degree at most two. Consequently
\[
B:=4\sqrt{n-1}\,\|\delta\|_2\ge\|\Delta\|_{2\to2}.
\]
The choice of \(x\) above gives \(\langle x,\Delta x\rangle=0\) because \(P_{11}=P_{*,11}=1/2\), while \(\Delta e_1\) has zero first coordinate and remaining coordinates \(\delta_1,\ldots,\delta_{n-1}\). Hence
\[
\langle x,\Delta^2 x\rangle=\|\Delta x\|^2
=\frac{n}{n-1}\|\delta\|_2^2.
\]
Let \(a=\lambda_{\max}(\Delta\vert_{\mathbf1^\perp})\). Every eigenvalue \(\lambda\) appearing in the spectral measure of \(\Delta\) at \(x\) satisfies \(-B\le\lambda\le a\). Averaging the nonnegative polynomial \((\lambda+B)(a-\lambda)\) and using its zero first moment gives \(\langle x,\Delta^2x\rangle\le aB\). For \(\delta\ne0\), this proves
\[
a\ge \frac{n}{4(n-1)^{3/2}}\|\delta\|_2.
\]
The centered restriction of \(P_*\) is scalar \(d_n I\), so \(\lambda_{\max}(P_p\vert_{\mathbf1^\perp})=d_n+a\). Since \(\mu(P_p)\ge\lambda_{\max}(P_p\vert_{\mathbf1^\perp})\), the asserted strict deviation bound follows. For \(\delta=0\), it holds with equality.

**4. Wasted proposal mass.** If \(S>0\), set \(v_s=a_s/(2S)\) and let \(Q\) denote the fully supported proposal kernel with \(q_{\pm s}=v_s\), zero elsewhere. Since every proposal not accounted for by \(S\) always leaves the state unchanged, \(P_p=(1-2S)I+2S Q\). The maximum centered eigenvalue is \(1-2S+2S\lambda_{\max}(Q\vert_{\mathbf1^\perp})\). Apply step 3 to \(Q\) and multiply by \(2S\), obtaining the full stated inequality, with deviation \(a_s-S/(n-1)\). If \(S=0\), then \(P_p=I\) and the bound is exact with value \(1\). Any wasted mass makes the second term strictly positive, and otherwise any nonuniform profile makes the third strictly positive. This proves uniqueness of the entire proposal law.

**5. Stationary acceptance and exact mixing.** In the optimal chain each of the \(n-1\) off-diagonal entries in a row is \(1/[2(n-1)]\), making the move probability \(1/2\). Since \(P_*\Pi=\Pi\) and \(P_*\vert_{\mathbf1^\perp}=d_n I\), the power formula follows. A point-mass start has total-variation distance \((1-1/n)d_n^t\) from uniform for \(t\ge1\).

## Verification

Run `python3 checker.py` using Python's standard library. It constructs transition matrices from rejected proposal moves with exact rational arithmetic. It verifies exact entries, stationarity, the claimed scalar centered spectrum and acceptance for orders \(2\le n\le19\). Separately, Jacobi diagonalization tests random nonuniform proposals and extraneous zero/long displacements for orders \(2\le n\le13\) against the sharp lower bound and displayed stability inequality. In the present check it reported **15,483** exact identities or independently evaluated numerical inequalities. The all-size assertion rests on the preceding proof, not on these finite tests.

## Relationship to prior work

Chepelianskii, Majumdar, Schawe and Trizac (arXiv:2303.08535, first publicly posted March 15, 2023) analyze uniform continuous-position Metropolis walks in a box and establish the \(1/2\) optimal relaxation factor for continuous uniform jumps spanning the box. Their 2022 precursor (arXiv:2207.10488) analyzes relaxation/localization for continuous spatial proposals and uses finite matrices for numerical approximation. Neither inspected work gives the exact finite-integer-displacement optimum, its strictly smaller value \(1/2-1/[2(n-1)]\), or the all-proposal quantitative rigidity asserted here. The finite correction reflects the exactly \(2(n-1)\) feasible nonzero integer displacements, allowing \(2(n-1)\) off-zero proposals with each row's rejected mass exactly \(1/2\).

Boyd, Diaconis and Xiao formulate fastest mixing over graph-constrained transition matrices; on a complete graph, their unconstrained class contains the independent-uniform kernel with centered spectral radius zero. That kernel is inadmissible in the present state-independent rejection-only proposal family for \(n>2\). Boyd, Diaconis, Sun and Xiao treat the nearest-neighbor path case, which excludes the long-range proposals required here for \(n>2\). Thus neither stronger optimization framework implies this same admissible optimizer or stability estimate without additional argument.

## Limitations

The optimality and stability results are for symmetric, state-independent integer displacement proposals with hard rejection only. They do not apply unchanged to continuous-position boxes, state-dependent proposals, nonuniform targets, alternative boundary handling, or arbitrary reversible Markov kernels. The shape-stability coefficient has not been optimized. Although the searched primary literature does not state this exact finite theorem, additional unindexed results or implications from broader optimization work may affect publication priority; independent literature auditing has not been performed.

## References

1. Chepelianskii, A. D., Majumdar, S. N., Schawe, H., and Trizac, E., *Singular relaxation of a random walk in a box with a Metropolis Monte Carlo dynamics*, arXiv:2303.08535v1 (2023). https://arxiv.org/abs/2303.08535
2. Chepelianskii, A. D., Majumdar, S. N., Schawe, H., and Trizac, E., *Metropolis Monte Carlo sampling: convergence, localization transition and optimality*, arXiv:2207.10488 (2022). https://arxiv.org/abs/2207.10488
3. Boyd, S., Diaconis, P., and Xiao, L., *Fastest mixing Markov chain on a graph*, SIAM Review 46 (2004), 667–689. https://stanford.edu/~boyd/papers/pdf/fmmc.pdf
4. Boyd, S., Diaconis, P., Sun, J., and Xiao, L., *Fastest mixing Markov chain on a path*. https://web.stanford.edu/~boyd/papers/pdf/fmmc_path.pdf
