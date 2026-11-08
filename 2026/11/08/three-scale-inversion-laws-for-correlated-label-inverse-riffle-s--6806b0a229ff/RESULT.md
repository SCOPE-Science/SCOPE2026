# Three-scale inversion laws for correlated-label inverse riffle shuffles

## Finding

For the stationary two-state correlated-label inverse riffle shuffle of \(n\) cards with adhesion \(p_n\in[0,1)\), write \(I_n\) for the number of inversions after **one** shuffle. The exact mean and a three-way fluctuation transition are as follows.

Let \(h_n=1-p_n\) and \(q_n=h_n/2\). For every \(n\ge2\),
\[
\mathbb E I_n=\frac14\sum_{d=1}^{n-1}(n-d)(1-p_n^d),\qquad
\Pr(I_n=0)=(1-q_n)^{n-1}+\frac{n-1}{2}q_n(1-q_n)^{n-2}.
\]

If \(nh_n\to\infty\), then
\[
\frac{I_n-\mathbb E I_n}{\sqrt{n^3(1+p_n)/(48h_n)}}\Longrightarrow N(0,1).
\]
If \(nh_n\to\lambda\in(0,\infty)\), then
\[
\frac{I_n}{n^2}\Longrightarrow J_\lambda
=\int_{0<s<t<1}\mathbf1\{S(s)=+1,\ S(t)=-1\}\,ds\,dt,
\qquad
\Pr(J_\lambda=0)=e^{-\lambda/2}\left(1+\frac{\lambda}{4}\right),
\]
where \(S\) is a fair-initial telegraph process whose switches form a Poisson process of rate \(\lambda/2\). If \(nh_n\to0\) (and \(h_n>0\)), then
\[
\Pr(I_n>0)\sim\frac{nh_n}{4},\qquad
\mathcal L\left(\left.\frac{I_n}{n^2}\ \right|\ I_n>0\right)
\Longrightarrow\mathcal L(U(1-U)),\quad U\sim\mathrm{Uniform}(0,1).
\]
The last limit has distribution function \(1-\sqrt{1-4y}\) for \(0\le y\le1/4\), and density \(2/\sqrt{1-4y}\) in the open interval.

## Assumptions and scope

Start from the identity arrangement of \(n\ge2\) distinguishable cards. Sample a stationary, fair binary Markov label string \(L_1,\ldots,L_n\), with \(L_1\) fair and every adjacent label changing with probability \(q_n=(1-p_n)/2\), independently of previous change decisions. Place all cards labelled \(0\) before those labelled \(1\), preserving input order within a label class. This is the correlated-label inverse riffle rule \(\mathsf M_{p_n}\) in Jiang's Definition 2.4. Inversions are counted in the resulting permutation; inversion counts are the same for a permutation and its inverse. The parameter may vary with \(n\), but is always in \([0,1)\). The claims are asymptotic as \(n\to\infty\) through all integers, with no even-deck restriction.

## Proof

**1. Exact reduction.** Let \(S_i=2L_i-1\in\{-1,+1\}\), \(M_n=\sum_{i=1}^n S_i\), and \(a_i=n+1-2i\). Stable sorting reverses a pair \((i,j)\) with \(i<j\) precisely when \((L_i,L_j)=(1,0)\). Hence
\[
I_n=\sum_{i<j}\frac{(1+S_i)(1-S_j)}4
=\frac{n^2}{8}+\frac14\sum_{i=1}^na_iS_i-\frac18M_n^2.\tag{1}
\]
The stationary chain satisfies \(\mathbb E[S_iS_j]=p_n^{|i-j|}\) and \(\mathbb ES_i=0\), proving the displayed exact mean. The event \(I_n=0\) is exactly that the labels are nondecreasing. It consists of either zero switches or one \(0\)-to-\(1\) switch. This proves the exact zero-atom probability.

**2. Gaussian regime.** Suppress the subscript on \(p=p_n\), \(h=1-p\). With \(\mathcal F_k=\sigma(S_1,\ldots,S_k)\), put \(D_k=S_k-pS_{k-1}\) for \(k\ge2\). These are bounded martingale differences with deterministic predictable variance \(\mathbb E[D_k^2\mid\mathcal F_{k-1}]=1-p^2\). The exact representation
\[
\sum_{i=1}^n a_iS_i=c_1S_1+\sum_{k=2}^nc_kD_k,
\quad c_k=\sum_{j=k}^na_jp^{j-k},
\]
has \(|c_1|\le n/h\) and
\[
\left|c_k-\frac{a_k}{h}\right|
\le \frac{np^{n-k+1}}h+\frac{2p}{h^2}.\tag{2}
\]
By orthogonality of martingale differences, the squared \(L^2\) norm of the replacement error is bounded by an absolute constant times
\[
\frac{n^2}{h^2}+\frac{n}{h^3},
\]
where the first term also absorbs the initial spin. This is \(o(n^3/h)\) when \(nh\to\infty\). Moreover \(\sum_{k=2}^n a_k^2\sim n^3/3\); therefore the predictable variance of \(h^{-1}\sum_{k=2}^na_kD_k\), divided by \(n^3(1+p)/h\), tends to \(1/3\). Its largest possible normalized increment is \(O((nh)^{-1/2})\), which verifies the martingale triangular-array Lindeberg condition. Consequently
\[
\frac{\sum_ia_iS_i}{\sqrt{n^3(1+p)/(3h)}}\Longrightarrow N(0,1).
\]
Finally \(\mathbb EM_n^2\le n+2n/h=O(n/h)\). By Markov's inequality, \(M_n^2-\mathbb EM_n^2=O_{\Pr}(n/h)=o_{\Pr}(\sqrt{n^3/h})\). Inserting this in (1) and dividing by \(4\) establishes the stated central limit theorem and constant \(1/48\).

**3. Poisson-switch regime.** When \(nh_n\to\lambda\in(0,\infty)\), changes between labels are independent Bernoulli variables with probabilities \(h_n/2\). Their point process on the grid \(\{1/n,\ldots,(n-1)/n\}\) converges to a Poisson process of rate \(\lambda/2\), independently of the fair initial sign. A path with finitely many distinct switches defines the inversion-area functional by pairwise integration over \(0<s<t<1\), and convergence of jump times away from measure-zero endpoint coincidences makes the discrete area \(I_n/n^2\) converge to \(J_\lambda\). The limiting area is zero exactly when there are no switches, or there is precisely one switch and the initial sign is negative. The Poisson probabilities yield the claimed atom \(e^{-\lambda/2}(1+\lambda/4)\).

**4. Rare-switch regime.** If \(nh_n\to0\), the chance of two or more switches is \(O((nh_n)^2)\). The event of exactly one descending switch (\(+1\) to \(-1\)) has probability \((n-1)(h_n/4)(1-h_n/2)^{n-2}\sim nh_n/4\). Any positive inversion count outside this event requires two or more switches, giving the asserted nonzero probability. Conditionally on the single descending switch, all \(n-1\) gap positions are equally likely. A descending switch after position \(k\) produces precisely \(k(n-k)\) inversions. Thus, given positive inversions, the rescaled count converges to \(U(1-U)\) with \(U\) uniform on \([0,1]\).

## Verification

Run \(\texttt{python3 verify_inversion.py}\) with Python 3 and no third-party packages. Exact enumeration checks every binary word for \(2\le n\le10\) and four rational adhesion parameters, verifying (1), the exact mean, total probability and the zero atom; 8,284 exact rational assertions pass. Separate seeded Monte Carlo checks confirm that sample normalizations and the critical/rare probabilities are consistent with the formulas, but do not prove any asymptotic statement. The martingale argument, point-process convergence and one-switch conditioning above are the infinite-size proofs.

## Relationship to prior work

Jiang (2026, arXiv:2611.02092v1), Definition 2.4 and Sections 2.2, 9 and 13, introduces and studies this same Markov inverse-riffle model in relation to **multi-shuffle mixing**. Jonasson and Morris (2015), pages 2–4 and 11–14, analyze the same symmetric Markov-label mechanism under a different persistence parameter and prove fixed-parameter logarithmic-power mixing bounds. Işlak (2013), Lemma 2.2 and Theorem 3.2, treats inversion statistics of classical **independent-label** riffle shuffles, corresponding to \(p_n=0\) here. These papers supply the mechanism and a special iid case, but the inspected results do not state the triangular-array three-scale inversion-area transition and rare positive-inversion law in this theorem. Their general tools do not, without additional estimates, give the boundary law for \(nh_n\) finite.

## Limitations

The theorem concerns a **single** inverse-riffle step from the identity; it gives neither mixing time nor cutoff after repeated steps. The Gaussian statement is an asymptotic normalization, not an exact finite-\(n\) variance formula or a Berry–Esseen rate. In the Poisson regime the limit has an atom and is not Gaussian. The positive-inversion conditional limit in the rare regime assumes \(p_n<1\) for all sufficiently large \(n\); at \(p_n=1\), conditioning on positive inversions is undefined. An unlocated 2011 dissertation on very clumpy riffle shuffles is a remaining historical-priority risk, notwithstanding the separate comparisons above.

## References

1. Y. Jiang, *Adhesive riffle shuffles: one-parameter models and mixing bounds*, arXiv:2611.02092v1, submitted 2026-11-01. https://arxiv.org/abs/2611.02092
2. Ü. Işlak, *Descent-Inversion Statistics in Riffle Shuffles*, arXiv:1303.2387v1, 2013-03-10. https://arxiv.org/abs/1303.2387
3. J. Jonasson and B. Morris, *Rapid mixing of dealer shuffles and clumpy shuffles*, Electronic Communications in Probability **20** (2015), no. 20, 1–11. https://doi.org/10.1214/ECP.v20-3682
4. S. Wager, *Clumpy riffle shuffles*, PhD thesis, Stanford University (2011), as cited by Jonasson and Morris; not materially inspected.
