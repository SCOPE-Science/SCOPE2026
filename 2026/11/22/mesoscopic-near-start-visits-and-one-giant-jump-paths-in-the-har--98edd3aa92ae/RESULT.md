# Mesoscopic near-start visits and one-giant-jump paths in the harmonic descent chain

## Finding

For the harmonic descent chain defined below, let the starting state be \(n\), and let the target be \(n-h_n\), where \(h_n\) is integral and
\[
 h_n\to\infty,\qquad \frac{\log h_n}{\log n}\to\theta\in(0,1).
\]
Write \(E_n\) for the event that the chain ever visits \(n-h_n\), and \(K_n\) for the number of jumps used to reach this target, defined only on \(E_n\). Then
\[
 \Pr(E_n)\sim\frac{1}{h_n\log n\,(1-\theta)^2},
 \qquad
 \Pr(K_n=k\mid E_n)\longrightarrow k(1-\theta)^2\theta^{k-1}
 \quad(k\ge1).
\]
The latter is a size-biased geometric law (a probability distribution on the strictly positive integers). In particular, its mean is \((1+\theta)/(1-\theta)\), although convergence of conditional means is not needed for the statement.

There is also a conditional path-shape limit. Given \(E_n\) and \(K_n=k\), list the positive decrement sizes in time order as \((D_{n,1},\ldots,D_{n,k})\); their sum is \(h_n\). For each fixed \(k\), asymptotically exactly one decrement consumes \(1-o_{\Pr}(1)\) of \(h_n\). Its index \(J_n\), defined as the leftmost index of a maximum, converges to the uniform law on \(\{1,\ldots,k\}\). Conditional on its index being \(r\), the remaining \(k-1\) logarithmic decrement sizes
\[
 \left(\frac{\log D_{n,i}}{\log h_n}:i\ne r\right)
\]
converge jointly to independent \(\operatorname{Unif}(0,1)\) variables, independently of the limiting uniform giant index. When \(k=1\), the single decrement equals \(h_n\) and the empty family of small increments is interpreted trivially.

This characterizes the limiting number and arrangement of jumps along a tagged leaf's path when that path passes through a near-full-sized clade in the critical beta-splitting tree. By the established clade-count identity \(\mathbb E N_n(j)=n\Pr_n(\mathrm{hit}\ j)/j\), the expected number of \((n-h_n)\)-leaf clades has the same leading asymptotic as \(\Pr(E_n)\).

## Assumptions and scope

Set \(H_0=0\), and for integer \(m\ge1\) put \(H_m=\sum_{r=1}^m 1/r\). The discrete-time harmonic descent chain is the decreasing Markov chain on positive integers with transition probabilities
\[
 \Pr(X_{t+1}=j-d\mid X_t=j)=\frac{1}{dH_{j-1}},
 \qquad j\ge2,\quad 1\le d\le j-1,
\]
and with state \(1\) absorbing. Let \(X_0=n\). The integer sequence \(h_n\) satisfies \(1\le h_n\le n-2\) eventually, \(h_n\to\infty\), and \(\log h_n/\log n\to\theta\in(0,1)\). No other randomness or moments are assumed. Every convergence statement is along any such sequence \(n\to\infty\); the path-shape assertion conditions on a fixed positive integer \(k\), then lets \(n\to\infty\). It does not assert a uniform limit as \(k\to\infty\), nor does it cover \(\theta=1\).

## Proof

**Step 1: positive compositions and exact path weights.** For integers \(h,k\ge1\), let
\[
 b_{h,k}=\sum_{\substack{d_1,\ldots,d_k\ge1\\d_1+\cdots+d_k=h}}\frac{1}{d_1\cdots d_k},
 \quad b_{0,0}=1,\quad b_{h,0}=0\ (h\ge1).
\]
Equivalently, \(b_{h,k}=[z^h]L(z)^k\), where \(L(z)=\sum_{j\ge1}z^j/j=-\log(1-z)\). Write \(P_{n,h,k}=\Pr_n(E_{n,h},K=k)\) for the probability that the chain started at \(n\) makes exactly \(k\) jumps to \(n-h\). A particular ordered composition \((d_1,\ldots,d_k)\) has probability
\[
 \frac{1}{d_1\cdots d_k}\prod_{i=0}^{k-1}
 \frac{1}{H_{n-1-(d_1+\cdots+d_i)}}.
\]
Because each intermediate state belongs to \([n-h+1,n]\), monotonicity of the harmonic numbers gives, for every \(1\le k\le h\),
\[
 \frac{b_{h,k}}{H_{n-1}^{k}}\le P_{n,h,k}
 \le\frac{b_{h,k}}{H_{n-h}^{k}}.\tag{1}
\]
This is an exact two-sided inequality, not an approximation. Summing over the disjoint possible jump numbers gives an analogous sandwich for the target-hitting probability.

**Step 2: exact coefficient control.** Differentiating \(L(z)^k\) gives
\[
 h b_{h,k}=k\sum_{j=0}^{h-1}b_{j,k-1}.
\]
The last sum is the weight of all ordered \((k-1)\)-tuples of positive integers with total at most \(h-1\) (with the empty tuple when \(k=1\)). Hence
\[
 0\le b_{h,k}\le\frac{k}{h}H_{h-1}^{k-1}\quad(1\le k\le h).\tag{2}
\]
For each fixed \(k\), this is asymptotically sharp:
\[
 b_{h,k}\sim\frac{k}{h}(\log h)^{k-1}\quad(h\to\infty).\tag{3}
\]
Indeed, for each \(\varepsilon\in(0,1)\), every \((k-1)\)-tuple with entries at most \(\lfloor h^{1-\varepsilon}\rfloor\) has total at most \(h-1\) for all sufficiently large \(h\); its total weight is \(H_{\lfloor h^{1-\varepsilon}\rfloor}^{k-1}\). This gives the lower bound \((1-\varepsilon)^{k-1}(\log h)^{k-1}(1+o(1))\) for the sum in the derivative identity. The upper bound is \(H_{h-1}^{k-1}\). Letting \(\varepsilon\downarrow0\) proves (3); the case \(k=1\) holds exactly.

**Step 3: summing all path lengths.** For \(a>0\), put
\[
 U_h(a)=\sum_{k=1}^h a^k b_{h,k}.
\]
Suppose that \(h\to\infty\) and \(aH_{h-1}\to\theta\in(0,1)\). By (2),
\[
 0\le \frac{h}{a} a^k b_{h,k}
 \le k(aH_{h-1})^{k-1},
\]
which is dominated for all sufficiently large \(h\) by a summable geometric-derivative sequence. For every fixed \(k\), by (3),
\[
 \frac{h}{a}a^k b_{h,k}
 \sim k(a\log h)^{k-1}\to k\theta^{k-1}.
\]
Dominated convergence for series now yields
\[
 U_h(a)\sim\frac{a}{h}\sum_{k\ge1}k\theta^{k-1}
 =\frac{a}{h(1-\theta)^2}.\tag{4}
\]
In our regime \(h_n=o(n)\) and \(\log h_n/\log n\to\theta\); therefore both \(a_n^-=H_{n-1}^{-1}\) and \(a_n^+=H_{n-h_n}^{-1}\) satisfy \(a_n^\pm\log h_n\to\theta\) and \(a_n^\pm\log n\to1\). Applying (4) to the two sums in (1) and squeezing proves
\[
 \Pr(E_n)\sim [h_n\log n(1-\theta)^2]^{-1}.
\]
For each fixed \(k\), (1), (3), and \(H_{n-1}/H_{n-h_n}\to1\) also give \(P_{n,h_n,k}\sim k(\log h_n)^{k-1}/[h_n(\log n)^k]\). Dividing by \(\Pr(E_n)\) proves the asserted conditional jump-number law. It sums to one since \(\sum_{k\ge1}k\theta^{k-1}=(1-\theta)^{-2}\), ensuring tightness.

**Step 4: conditional giant-jump geometry.** Fix \(k\ge2\). In the exact conditional law given \(E_n,K_n=k\), the weight of a composition is its reciprocal product times the product of intermediate harmonic normalizers. By (1), uniformly over all such compositions, the latter product differs by a multiplicative factor \(1+o(1)\) from \(H_{n-1}^{-k}\): the ratio is at most \((H_{n-1}/H_{n-h_n})^k\to1\). Thus total-variation distance from the reference composition law with weights proportional to \(1/(d_1\cdots d_k)\) tends to zero.

Under this reference law, fix an index \(r\in\{1,\ldots,k\}\) and numbers \(t_i\in(0,1)\) for \(i\ne r\). Restrict to compositions with \(1\le d_i\le\lfloor h^{t_i}\rfloor\) for \(i\ne r\), and put \(d_r=h-\sum_{i\ne r}d_i\). Uniformly over the restricted tuples, \(d_r/h\to1\), so the unnormalized total weight is
\[
 \frac{1+o(1)}h\prod_{i\ne r}H_{\lfloor h^{t_i}\rfloor}
 \sim \frac{(\log h)^{k-1}}h\prod_{i\ne r}t_i.\tag{5}
\]
By (3), division by \(b_{h,k}\) makes its probability tend to \(k^{-1}\prod_{i\ne r}t_i\). For fixed \(t_i<1\), the events (5) for distinct \(r\) are disjoint when \(h\) is large: the designated \(d_r\) exceeds \(h/2\). Let all \(t_i\uparrow1\); summing over \(r\) shows that, with probability tending to one, there is exactly one increment asymptotically equal to \(h\). The displayed joint rectangular distribution functions establish that its index is uniform and that, conditional on this index, the other scaled logarithms have independent uniform distributions on \((0,1)\). Since the limit is continuous, the convergence of these rectangular events suffices for joint weak convergence. Transferring the result through the total-variation approximation completes the proof. The \(k=1\) case is immediate.

## Verification

The standalone Python 3 script `checker.py` is included. It computes exact rational composition coefficients using both coefficient recurrence and direct enumeration, exact finite-state hitting probabilities using the Markov recursion and complete path enumeration, and checks the harmonic-number sandwich for small states. It also checks numerically the mesoscopic coefficient crossover for large chosen \(n\). Its most recent execution passed 497 assertions. These checks are corroborative: the proofs of the infinite limits are Steps 1–4 and do not rely on finite experiments.

To reproduce, run `python3 checker.py` with a standard Python 3 interpreter; the script uses only the standard library. The finite exact assertions cover \(4\le n\le21\), positive \(h\le\min(n-2,9)\), and composition coefficients through \(h=10\); numerical checks use larger \(n\) and several fixed mesoscopic exponents. No outside data or numerical package is required.

## Relationship to prior work

The chain and its tagged-leaf interpretation originate with Aldous, Janson, and Li [1]. Their main occupation result concerns targets held fixed as the starting state grows. Brandenberger, Chin, and Mossel [2, Theorem 1.1(iii)] give bounds near the starting state, including \(O(1/[hH_{n-h}])\) for a broad sublinear range, but do not identify the \(\theta\)-dependent coefficient or the rare-path jump structure. Svihla [3, Theorem 2.1] obtains a detailed expansion for target states \(k=o(\sqrt n)\), in contrast with the present target \(k=n-h_n\sim n\). The regenerative-composition interpretation in Iksanov [4] and the bulk block-count limit theorems of Gnedin and Iksanov [5] are relevant background; their inspected results concern fixed-target visitation or global counts rather than the conditional mesoscopic near-start path described here. Iksanov, Nikitin, and Yakymiv [6] study global joint leaf-height/decrement-count fluctuations, another different scaling.

The proof uses elementary path enumeration rather than relying on a black-box renewal theorem. Exact general finite-state recursion and occupation identities are known; their existence is not claimed as new. The claimed distinction is the combined mesoscopic constant, size-biased geometric visit depth, and one-giant-jump/log-uniform conditional path law.

## Limitations

The theorem requires a fixed exponent strictly between zero and one and a target of the form \(n-h_n\), and it conditions on a rare event. Nothing here proves a uniform assertion when the exponent approaches either endpoint, a limit for conditional jump number growing with \(n\), or a general theorem for other decrement kernels. The numerical checks do not independently certify any asymptotic. General regenerative-composition and analytic-combinatorics theory could conceivably subsume parts of these particular conclusions; a systematic historical-priority assessment beyond the inspected sources remains open. No independently conducted mathematical assessment is claimed.

## References

1. D. J. Aldous, S. Janson, and X. Li, *The Harmonic Descent Chain*, Electronic Communications in Probability 29 (2024), arXiv:2405.05102, https://arxiv.org/abs/2405.05102.
2. A. Brandenberger, B. Chin, and E. Mossel, *Asymptotics for the Harmonic Descent Chain and Applications to Critical Beta-Splitting Trees*, arXiv:2505.24821, https://arxiv.org/abs/2505.24821.
3. S. P. Svihla, *Exact Asymptotics for the Harmonic Descent Chain and Extended Convergence Bounds for Recursive Statistics*, arXiv:2611.00347v1 (first public 2026-10-30), https://arxiv.org/abs/2611.00347.
4. A. Iksanov, *A Comment on the Article ‘The Harmonic Descent Chain’ by D. J. Aldous, S. Janson and X. Li*, arXiv:2412.06826, https://arxiv.org/abs/2412.06826.
5. A. Gnedin and A. Iksanov, *Regenerative Compositions in the Case of Slow Variation: A Renewal Theory Approach*, Electronic Journal of Probability 17 (2012), arXiv:1109.5985, https://arxiv.org/abs/1109.5985.
6. A. Iksanov, A. Nikitin, and R. Yakymiv, *An Infinite Balls-in-Boxes Approach to the Critical Beta-Splitting Tree: Some Central Limit Theorems*, 2026 preprint, https://do.csc.knu.ua/iksan/wp-content/uploads/sites/3/2026/02/iksnikyak130226-rev.pdf.
