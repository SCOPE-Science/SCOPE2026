# A Poisson finite-innovation window for two-state step-reinforced walks

## Finding

Let \(N\) run through positive even integers. For each \(N\), construct a usual step-reinforced random walk \(S^{(N)}\) on the additive group \(\mathbb Z_2\), starting at \(0\), with independent fresh increments uniformly distributed on \(\{0,1\}\). The first increment is fresh. At every subsequent step, independently, with probability \(\alpha_N\in[0,1]\) repeat a uniformly selected earlier increment, and otherwise take a new fair increment. Write \(q_N=1-\alpha_N\) and
\[
 b_N=2\Pr(S_N^{(N)}=0)-1.
\]

**Theorem (finite-innovation window).** If \(Nq_N\to\lambda\in[0,\infty)\), then
\[
 b_N\longrightarrow 2^{-\lambda},\qquad
 \big\|\mathcal L(S_N^{(N)})-\operatorname{Unif}(\mathbb Z_2)\big\|_{\mathrm{TV}}\longrightarrow 2^{-\lambda-1}.
\]
If instead \(Nq_N\to\infty\), then \(b_N\to0\). For every odd \(N\), the law of \(S_N^{(N)}\) is exactly uniform, for every \(\alpha_N\in[0,1]\).

A structural, jointly convergent part of the theorem is as follows. Delete every fresh-increment edge from the random recursive tree of past-step choices. Let \(M_{N,k}\) count **nonroot** components of exactly \(k\) vertices. In the finite-innovation regime \(Nq_N\to\lambda\), for every fixed \(K\),
\[
 (M_{N,1},\ldots,M_{N,K})\ \Rightarrow\ (P_1,\ldots,P_K),
 \qquad P_k\ \text{independent,}\quad P_k\sim\operatorname{Poisson}\!\left(\frac{\lambda}{k(k+1)}\right).
\]
In fact, the whole finite multiset of nonroot component sizes converges to a Poisson random measure on \(\mathbb N_{\ge1}\) with intensity \(\lambda/[k(k+1)]\) at \(k\). This assertion includes \(\lambda=0\) (the empty limit).

## Assumptions and scope

The parameter \(\alpha_N\) is fixed **within** each \(N\)-step experiment, but may depend on its horizon \(N\). All parent choices, fresh/reinforcement decisions, and fresh fair increments are mutually independent. The result concerns the standard untransformed reinforcement rule on \(\mathbb Z_2\); it does not assert an analogous closed constant for arbitrary groups, nonuniform fresh increments, or history-dependent parameters.

The Poisson component-size theorem concerns exactly the regime \(Nq_N\to\lambda<\infty\), whereas the assertion for \(Nq_N\to\infty\) concerns only the terminal two-state law. Finite-\(N\) empirical checks are not used in place of the limit proof.

## Proof

**1. Recursive-tree representation and parity.** Independently choose a parent \(U_j\) uniformly in \(\{1,\ldots,j-1\}\) for each \(j=2,\ldots,N\). Retain the edge \((j,U_j)\) if the step at \(j\) is a repetition, and delete it otherwise. Every connected component of the resulting forest receives a single independent uniform bit, the fresh increment at its smallest vertex. Thus, conditionally on the forest, the terminal bit is the sum over components of (component size) times (component bit), modulo two. It is deterministically zero precisely when **all** components have even order, and is fair otherwise. Consequently
\[
 b_N=\Pr(\text{all forest components have even order}). \tag{1}
\]
When \(N\) is odd that event is empty.

**2. Finite number of cuts.** The number \(R_N\) of deleted edges is \(\operatorname{Binomial}(N-1,q_N)\). Under \(Nq_N\to\lambda<\infty\), the elementary binomial-to-Poisson limit gives \(R_N\Rightarrow\operatorname{Poisson}(\lambda)\). Conditional on \(R_N=r\), the deleted edges are a uniformly random set of \(r\) distinct labels from \(\{2,\ldots,N\}\), independent of the recursive-tree parent choices.

**3. Limiting sizes from finitely many uniformly chosen cut labels.** For fixed \(r\), sample \(r\) distinct nonroot labels uniformly. With probability \(1-o(1)\), none is an ancestor of another in the original recursive tree. Indeed, the expected depth of a uniformly chosen label is \(O(\log N)\), so for two sampled distinct labels the ancestor-pair probability is \(O(\log N/N)\), and a union bound handles fixed \(r\). On this high-probability event, removing the selected edges creates one nonroot component per selected label, and its size is exactly the size of that label's **original fringe subtree**.

We establish the joint limit of these original fringe-subtree sizes. The birth-time fractions of the sampled labels converge jointly to \(r\) independent uniform random variables \(V_1,\ldots,V_r\) on \((0,1)\). On the event \(\min_i V_i>\delta\), expose arrivals sequentially and stop the joint fringe-size process if a newly selected label belongs to an older selected fringe. This stopping event is precisely one of the already controlled ancestor events and has probability \(o(1)\). Before stopping, an active selected fringe of size \(s_i\) gains the next arriving vertex with probability \(s_i/m\) at population size \(m\); a newly born selected label outside existing marked fringes initiates a new size-one process. Conditional on the sampled labels and up to this negligible stopping event, the active disjoint subtrees have one-step transitions
\[
 \Pr(\Delta s_i=1\mid\mathbf s)=\frac{s_i}{m},\qquad
 \Pr(\Delta s_i=1,\Delta s_j=1\mid\mathbf s)=0\quad(i\ne j).
\]
With rescaled population time \(t=m/N\in[\delta,1]\), their generators converge to \(\sum_i(s_i/t)(f(\mathbf s+\mathbf e_i)-f(\mathbf s))\), the generator of independent Yule pure-birth processes after logarithmic time change. This convergence follows directly from the one-step transitions by truncating populations at a fixed bound; on \([\delta,1]\), their expected sizes are bounded by \(1/\delta\), so the truncation is removable by Markov's inequality. Starting with one vertex at relative time \(V_i=u\), the resulting size at time \(1\) is geometric:
\[
 \Pr(K_i=k\mid V_i=u)=u(1-u)^{k-1},\qquad k\ge1.
\]
The limiting processes are conditionally independent given their birth times. Integrating over the independent uniform times yields independent \(K_i\) with
\[
 \Pr(K_i=k)=\int_0^1u(1-u)^{k-1}\,du=\frac1{k(k+1)}. \tag{2}
\]
Finally let \(\delta\downarrow0\), since \(\Pr(\min_iV_i\le\delta)\le r\delta\). This proves the asserted joint fringe-size law for every fixed \(r\).

**4. Poisson marks.** Conditional on \(R_N=r\), step 3 gives \(r\) asymptotically independent marks with the distribution (2). Since \(R_N\) is tight and converges to a Poisson variable, conditioning on bounded \(r\), passing to the limit and removing the truncation gives a Poisson random multiset of marks with total intensity \(\lambda\). The Poisson marking/thinning identity makes its size-\(k\) multiplicities independent Poisson variables of respective means \(\lambda/[k(k+1)]\). Because the number of marks is tight and the limiting mark law has tail \(\Pr(K>k)=1/(k+1)\), truncation to marks of bounded size and then removal of the size cutoff also justify convergence of the complete finite multiset, not merely each fixed vector. This is the asserted component-size convergence.

**5. All-even event and its exact constant.** For even \(N\), if every nonroot component is even then the remaining root component has size \(N\) minus an even integer, hence is also even. Conversely, all-even clearly requires every nonroot component even. The mark \(K\) in (2) has odd-size probability
\[
 p_{\mathrm{odd}}=\sum_{j\ge1}\frac1{(2j-1)(2j)}=\sum_{j\ge1}\left(\frac1{2j-1}-\frac1{2j}\right)=\log2.
\]
The limiting number of odd nonroot components is therefore \(\operatorname{Poisson}(\lambda\log2)\). The probability that it vanishes tends to \(e^{-\lambda\log2}=2^{-\lambda}\), proving the first limit in conjunction with (1). The total variation limit follows because a law on two points with return bias \(b_N\ge0\) is at TV distance \(b_N/2\) from the fair law.

**6. Above the window.** Corollary 1.6 of Peres and Qin (2026) proves, for the same walk and each even \(N\), the upper bound
\[
 0\le b_N\le\alpha_N^{N/2}\le e^{-Nq_N/2}.
\]
It holds for each \(N\) independently of the choice of \(\alpha_N\). If \(Nq_N\to\infty\) the upper bound tends to zero. The odd case follows from step 1.

## Verification

The standalone program `verify.py` independently calculates the binary-walk parity bias and the all-even forest-component probability by **different** exact rational recurrences. It compares them for every \(1\le N\le12\) at reinforcement probabilities \(0,1/4,1/2,3/4,1\), checks the odd-horizon identity and even-horizon upper bound, and evaluates larger finite horizons in representative critical windows. These checks yield 135 successful exact or numerical assertions in the provided implementation. They only test finite consequences of the proof. The Poisson limit, generator convergence and exact exponent are established analytically above.

Run `python3 verify.py` using Python 3 standard-library modules only.

## Relationship to prior work

Peres and Qin (2026a), especially Corollary 1.6 and their equation (37), establish the forest-parity identity and exponential return-probability bounds. They do not state the joint critical scaling \(N(1-\alpha_N)\to\lambda\) with exact limiting bias \(2^{-\lambda}\). Their fixed-parameter bounds allow a range of constants in that window and hence do not imply the exact answer. Their companion paper (2026b) establishes finite-group mixing for fixed reinforcement and gives fixed-parameter forest-cluster information; it likewise does not evaluate the rare-innovation window.

The law \(\Pr(K=k)=1/[k(k+1)]\) for the size of a single uniformly cut recursive-tree fringe is classical, recorded by Meir and Moon (1974) and Baur and Bertoin (2014). The contribution here is not that marginal. It is the **joint, finitely-cut Poisson marking limit at deletion rate \(\lambda/N\)** and its use to calculate the exact reinforced-walk return bias. Baur (2014) analyzes near-one percolation primarily in regimes where \((1-p(n))n^{p(n)}\to\infty\); the window \(1-p(n)\asymp1/n\) has only finitely many deletions and does not meet that hypothesis for nonroot-cluster asymptotics. We do not claim novelty of the underlying recursive-tree, Yule-process or parity representations.

## Limitations

The theorem is for the two-element group and **uniform** fresh increments. Its convergence assertions do not supply a finite-size error rate, moment convergence, or joint laws across experiments with different horizons. Independent scientific validation and historical-priority verification have not been performed. The specific residual priority risk is the possibility that the finite-cut Poisson marking corollary already appears elsewhere in recursive-tree fragmentation or mutation literature under a different formulation; the full primary comparisons described above did not identify such a covering statement.

## References

- Y. Peres and S. Qin, *Transition probabilities of step-reinforced random walks*, arXiv:2604.07227 (first publicly posted April 8, 2026), §§1.2, 2.1, 2.5, especially Corollary 1.6 and equation (37). https://arxiv.org/html/2604.07227v2
- Y. Peres and S. Qin, *Mixing times of step-reinforced random walks*, arXiv:2604.07207 (first publicly posted April 8, 2026), §§1, 3. https://arxiv.org/html/2604.07207v3
- E. Baur and J. Bertoin, *Cutting edges at random in large recursive trees*, arXiv:1406.2238 (2014), Proposition 1 and §5. https://arxiv.org/abs/1406.2238
- E. Baur, *Percolation on random recursive trees*, arXiv:1407.2508 (2014), introduction, Theorem 1 hypotheses, §§2.2–2.3. https://arxiv.org/abs/1407.2508
- A. Meir and J. W. Moon, *Cutting down recursive trees*, Mathematical Biosciences 21 (1974), 173–181; cited through Baur and Bertoin (2014), Proposition 1.
