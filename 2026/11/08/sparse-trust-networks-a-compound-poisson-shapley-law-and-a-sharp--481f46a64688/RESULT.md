# Sparse trust networks: a compound-Poisson Shapley law and a sharp zero-credit threshold

## Finding

Let \(G_n\) be a directed loopless Erdős–Rényi graph on \(n\ge2\) labeled vertices, with every ordered arc present independently with probability \(p_n\). Every present arc has trust weight one. For a coalition \(S\), define the cooperative trust game
\[
 v_{G_n}(S)=\#\{(j,k)\in E(G_n):j,k\in S\}
 +\#\{k\in S:\exists j\notin S,\ (j,k)\in E(G_n)\}.
\]
Let \(\phi_i^{(n)}\) be the ordinary Shapley value of vertex \(i\), and let \(W_n=\#\{i:\phi_i^{(n)}=0\}\).

**Exact finite-network law.** For any \(n\ge2\) and \(p_n\in[0,1]\), the tagged payoff has the exact representation in distribution
\[
 \phi_i^{(n)}\ \overset d=\ h(D^-)+\sum_{r=1}^{D^+}t(B_r),\qquad
 h(d)=\frac d2+\frac d{d+1},\quad t(b)=\frac{b}{2(b+2)},
\]
where \(D^-\) and \(D^+\) are independent \(\operatorname{Bin}(n-1,p_n)\), and \((B_r)_{r\ge1}\) are independent \(\operatorname{Bin}(n-2,p_n)\), independent of both degrees. Consequently,
\[
 \mathbb P(\phi_i^{(n)}=0)
 =(1-p_n)^{n-1}\bigl(1-p_n+p_n(1-p_n)^{n-2}\bigr)^{n-1},
 \qquad \mathbb E\phi_i^{(n)}=(n-1)p_n.
\]

**Sparse payoff distribution and population profile.** Suppose \(np_n\to\lambda\in(0,\infty)\). Let \(P^-,P^+,(Z_r)_{r\ge1}\) be independent \(\operatorname{Poisson}(\lambda)\) variables, and set
\[
 Y_\lambda=h(P^-)+\sum_{r=1}^{P^+}t(Z_r).
\]
Then \(\phi_i^{(n)}\Rightarrow Y_\lambda\), and the empirical Shapley distribution \(n^{-1}\sum_{i=1}^n\delta_{\phi_i^{(n)}}\) converges weakly in probability to the law of \(Y_\lambda\). In particular,
\[
 \frac{W_n}{n}\xrightarrow{\mathbb P}q_\lambda
 :=\exp\bigl(-2\lambda+\lambda e^{-\lambda}\bigr),
\]
while \(\mathbb E Y_\lambda=\lambda\) and
\[
 \operatorname{Var}(Y_\lambda)=
 \operatorname{Var}\left(\frac{P^-}{2}+\frac{P^-}{P^-+1}\right)
 +\lambda\,\mathbb E\left[\left(\frac{Z_1}{2(Z_1+2)}\right)^2\right].
\]
Thus a positive fraction of vertices obtain no Shapley credit at every fixed positive limiting average outdegree, although the mean credit remains positive.

**Sharp disappearance window.** If
\[
 2np_n-\log n\longrightarrow t\in\mathbb R,
\]
then
\[
 W_n\ \Rightarrow\ \operatorname{Poisson}(e^{-t}).
\]
More precisely, in this window \(W_n\) equals the number of vertices with neither incoming nor outgoing arcs with probability tending to one. Consequently, for every fixed \(\varepsilon\in(0,1)\), under \(p_n=(1-\varepsilon)\log n/(2n)\), some zero-credit vertex exists with probability tending to one, whereas under \(p_n=(1+\varepsilon)\log n/(2n)\), none exists with probability tending to one.

## Assumptions and scope

Arcs \((i,j)\) and \((j,i)\) are independent. There are no loops, no other edges, no negative trust weights, and no normalization of the Shapley allocation by total network trust. The external term counts each represented coalition member only once, irrespective of how many outgoing-to-it arcs originate outside the coalition. The random graph model includes all orientations, including reciprocal pairs. The random variables used in the representation above are independent as specified; the empirical convergence concerns the correlated vertex payoffs on one common random graph.

The tagged-vertex law is exact for every \(n\ge2\), while the limiting statements hold along the indicated sequences. At \(\lambda=0\), the Poisson limit degenerates at zero; it is excluded from the positive-fraction statement. The sharp-window law concerns unscaled credit zero, not small positive credit or a normalized credit share.

## Proof

**1. A graphwise identity.** Write \(d_i^-\) and \(d_i^+\) for in- and outdegrees, and \(N^-(i)\) for the set of in-neighbors. Let \(u_T(S)=\mathbf1\{T\subseteq S\}\) denote the unanimity game. The internal portion is \(\sum_{(j,k)\in E}u_{\{j,k\}}\). The external portion for vertex \(k\) is precisely \(u_{\{k\}}-u_{\{k\}\cup N^-(k)}\), including the case \(N^-(k)=\varnothing\) (when these terms cancel). By linearity and \(\phi_i(u_T)=\mathbf1\{i\in T\}/|T|\),
\[
 \phi_i(G)=\frac{d_i^-+d_i^+}{2}
 +1-\frac1{d_i^-+1}
 -\sum_{j:(i,j)\in E}\frac1{d_j^-+1}.
 \tag{1}
\]
Each outgoing edge \((i,j)\) contributes \(\frac12-\frac1{d_j^-+1}\). Since \(d_j^-=1+(d_j^--1)\), this equals \(t(d_j^--1)\), giving the asserted positive-sum form.

**2. Exact independence and moments.** For a fixed root \(i\), its incoming arcs and outgoing arcs form disjoint families of independent Bernoulli variables, so their counts \(D^-\), \(D^+\) are independent \(\operatorname{Bin}(n-1,p_n)\). Conditional on the entire outgoing arc set of \(i\), each selected destination \(j\) has exactly one prescribed incoming arc \((i,j)\), plus \(n-2\) other potential independent incoming arcs. For distinct destinations, these additional incoming arc variables are disjoint, and none is an incoming arc of \(i\) or an outgoing arc of \(i\). Their counts therefore are iid \(\operatorname{Bin}(n-2,p_n)\), independently of both root degrees. This proves the exact distributional factorization.

Since \(h(d)>0\) exactly when \(d>0\), and \(t(b)>0\) exactly when \(b>0\), zero payoff requires \(D^-=0\) and, for every potential outgoing destination, either the root arc is absent or no other arc enters that destination. The \(n-1\) destination events are independent, giving the displayed exact null probability. Shapley efficiency yields \(\sum_i\phi_i(G)=v_G(V)=|E(G)|\); exchangeability then yields \(\mathbb E\phi_i^{(n)}=(n-1)p_n\).

**3. Sparse weak and empirical limits.** If \(np_n\to\lambda\in(0,\infty)\), the three binomial laws in step 2 converge to \(\operatorname{Poisson}(\lambda)\). Since the sum has a tight number of terms and \(0\le t(b)<1/2\), finite-dimensional convergence and truncation of \(D^+\) give the claimed \(Y_\lambda\) limit. Its Laplace transform is explicitly
\[
 \mathbb E e^{-sY_\lambda}
 =\mathbb E e^{-s h(P^-)}
 \exp\left\{\lambda\bigl(\mathbb E e^{-s t(Z_1)}-1\bigr)\right\},\quad s\ge0.
\]
The null mass is \(\Pr(P^-=0)\mathbb E[(\Pr(Z_1=0))^{P^+}]=e^{-\lambda}\exp\{\lambda(e^{-\lambda}-1)\}=q_\lambda\). The displayed variance follows from independence and the compound-Poisson variance identity. To check its mean directly, use
\[
 \mathbb E\frac1{P+1}=\frac{1-e^{-\lambda}}\lambda,
 \qquad \mathbb E\frac1{P+2}=\frac{\lambda-1+e^{-\lambda}}{\lambda^2},
\]
for \(P\sim\operatorname{Poisson}(\lambda)\), which gives \(\mathbb E Y_\lambda=\lambda\).

For completeness, fix two distinct roots and expose only the incoming and outgoing arcs of each root and all arcs entering its outgoing neighbors. These are sufficient to compute both payoffs. Under \(p_n=O(1/n)\), all root degrees and destination in-degrees are tight; after truncating them at a fixed bound \(K\), the chance that the two exposed depth-two rooted structures intersect through a root, a common outgoing destination, or a cross-arc involving a selected destination is \(O_K(1/n)\). Off this event, the two truncated explorations use disjoint independent arc variables and converge jointly to independent copies of the finite-depth directed Poisson exploration. Letting \(n\to\infty\) and then \(K\to\infty\) proves joint convergence of two payoffs to independent copies of \(Y_\lambda\), and likewise joint convergence of their zero/nonzero indicators (which are determined by the same integer-valued local data). Exchangeability and the second-moment method imply the empirical weak convergence for bounded continuous tests and \(W_n/n\to q_\lambda\). Tightness of the empirical measures follows from their exact mean bound; a countable convergence-determining class yields weak convergence in probability.

**4. The critical zero-credit window.** Write \(I_n\) for the number of vertices with no incoming or outgoing arcs; clearly \(I_n\le W_n\). For one vertex, the isolation probability is \(a_n=(1-p_n)^{2(n-1)}\), whereas its zero-credit probability is \(q_n\), as computed in step 2. Thus
\[
 \frac{q_n}{a_n}=\left(1+\frac{p_n(1-p_n)^{n-2}}{1-p_n}\right)^{n-1}.
\]
If \(2np_n-\log n\to t\), then \(p_n\to0\), \(np_n\sim\frac12\log n\), and \(np_n(1-p_n)^{n-2}=O((\log n)/\sqrt n)\to0\). Consequently \(q_n/a_n\to1\), while \(na_n\to e^{-t}\). Therefore \(\mathbb E(W_n-I_n)=n(q_n-a_n)\to0\), hence \(\Pr(W_n\ne I_n)\to0\).

For fixed positive integer \(r\), the falling factorial moments of the isolate count satisfy
\[
 \mathbb E[(I_n)_r]=(n)_r(1-p_n)^{2r(n-r)+r(r-1)}\longrightarrow e^{-rt}.
\]
Indeed, \(2r(n-r)+r(r-1)\) is the number of directed arcs with at least one endpoint among \(r\) specified vertices. These are the factorial moments of \(\operatorname{Poisson}(e^{-t})\), establishing \(I_n\Rightarrow\operatorname{Poisson}(e^{-t})\), hence the asserted result for \(W_n\).

For \(p_n=(1-\varepsilon)\log n/(2n)\), \(\mathbb E I_n=n^{\varepsilon+o(1)}\) and the ratio of two-vertex isolation probability to \(a_n^2\) is \((1-p_n)^{-2}=1+o(1)\). Therefore \(I_n>0\) with probability tending to one by the second-moment method. For \(p_n=(1+\varepsilon)\log n/(2n)\), the exact null formula gives \(\mathbb E W_n=n^{-\varepsilon+o(1)}\), so \(W_n=0\) with probability tending to one by Markov's inequality.

## Verification

The standalone \(\texttt{verify.py}\) independently computes each coalition worth and each Shapley marginal from its original definition, rather than calling identity (1). It exhaustively checks all \(4+64+4096=4164\) loopless labeled digraphs with \(2,3,4\) vertices, all player payoffs, and the efficiency identity. It independently constructs the finite mixture distribution from the binomial factorization and matches the entire tagged-player distribution using exact rational probabilities \(p=1/3\), as well as the exact zero mass and expectation. It reports the finite critical-window excess of null vertices over isolates at three increasing network sizes; these numerical checks do not replace the limit proofs.

Run using \(\texttt{python3 verify.py}\) in a directory containing the standalone file. No third-party packages are needed.

## Relationship to prior work

The binary-weight trust-game coalition function is Example 3.2 of Bandhana, Kroupa and García (2024). Ryzák and Kroupa (2026) prove a general deterministic unanimity decomposition and formulas for Shapley/Banzhaf values on weighted directed networks. Identity (1) is a specialization and is **not claimed as new**. Neither inspected paper supplies a sparse Erdős–Rényi tagged-credit law, an empirical compound-Poisson profile, or a sharp Poisson disappearance window for zero-credit vertices. Classical Poisson limits for isolated vertices supply the final step, but do not by themselves identify when zero-credit vertices agree with isolates.

The directed-digraph Shapley framework of Khatri (2017) instead constrains admissible permutations by a dominance relation and studies directed cycles; it is not a theorem about the ordinary Shapley value of the minimum-incoming-exposure trust characteristic function. Generic random-graph local weak convergence and classical occupancy/Poisson approximations are supporting methods, not uniqueness evidence. Searches cannot rule out equivalent unindexed work.

## Limitations

Every arc weight is exactly one; arbitrary positive weights change the external minimum and the mark distribution. The network is directed with independent arcs, not the undirected \(G(n,p)\) graph. The mean formula and the deterministic Shapley specialization are previously implied; the contribution is the joint stochastic classification. The theorem does not assert a central limit theorem for the number of zero-credit vertices away from its critical window, nor quantify finite-sample rates of convergence in the sparse empirical law. No independent scientific audit has been performed.

## References

1. A. Bandhana, T. Kroupa and S. García, “Trust in Shapley: A Cooperative Quest for Global Trust in P2P Network,” AAMAS (2024), pp. 132–140. https://aamas.csc.liv.ac.uk/Proceedings/aamas2024/pdfs/p132.pdf (binary-edge Example 3.2; characteristic function and experiments).
2. D. Ryzák and T. Kroupa, “A Tractable Class of Cooperative Games Defined by Directed Networks: Unanimity Decomposition and Shapley Value,” arXiv:2605.18157v1 (18 May 2026). https://arxiv.org/html/2605.18157v1 (deterministic decomposition and graphwise allocation).
3. K. Khatri, “The Shapley Value of Cyclic Digraph Games,” arXiv:1701.01677 (2017). https://arxiv.org/abs/1701.01677 (different restricted-permutation cooperative model).
4. T. P. Michalak et al., “Efficient computation of the Shapley value for game-theoretic network centrality,” Journal of Artificial Intelligence Research 46 (2013), 607–650. https://eprints.soton.ac.uk/349140/ (broader network centrality and algorithms).
