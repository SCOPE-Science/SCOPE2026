# Sharp logarithmic propagation constant for probabilistic zero forcing on friendship graphs

## Finding

Let \(F_m=K_1\vee(mK_2)\), the graph of \(m\) edge-disjoint triangles sharing only their common central vertex \(o\). Run **synchronous probabilistic zero forcing**: initially only \(o\) is blue, blue vertices stay blue, and in each round every blue vertex \(u\) independently attempts to turn each white neighbor \(v\) blue with probability \(|N[u]\cap B|/\deg(u)\), based on the colors at the *start* of the round. A white vertex becomes blue when at least one of its attempted forces succeeds. Let \(\tau_m\) be the number of rounds until every vertex is blue.

**Theorem.** As the integer \(m\to\infty\),
\[
\frac{\tau_m}{\log m}\xrightarrow{\mathbb P}\frac{1}{\log(1+\sqrt2)},
\qquad
\frac{\mathbb E\tau_m}{\log m}\longrightarrow\frac{1}{\log(1+\sqrt2)}.
\]
All logarithms are natural. The hub-centered friendship graph therefore has an explicit logarithmic growth constant, not merely an order-of-growth estimate. The constant comes from the Perron root of the two-stage linearized infection matrix, \(\begin{psmallmatrix}2&1\\1&0\end{psmallmatrix}\).

An exact finite-state kernel is also established. If \(E_t\) is the number of triangles whose two noncentral vertices are white, \(S_t\) the number with exactly one noncentral blue vertex, and \(B_t=2m-2E_t-S_t\), then, conditionally on \((E_t,S_t)=(e,s)\), the pair \((E_{t+1},S_{t+1})\) is obtained from \(e\) independent three-outcome trials with probabilities
\[
(1-p)^2,\quad 2p(1-p),\quad p^2,\qquad p=\frac{1+2m-2e-s}{2m},
\]
for the categories empty, single, and full whenever at least one white vertex remains; the \(s\) existing single triangles become full with certainty. The fully blue state has no forcing attempts and is absorbing. This kernel supplies an exact reproducible finite-size description but is not itself the asymptotic theorem.

## Assumptions and scope

The graph has exactly \(2m+1\) vertices and no edges other than those within the \(m\) triangles. The common hub is the *only* initially blue vertex. All forcing attempts are independent conditional on the current coloring; all new colors are applied simultaneously at the end of a round. In particular, a blue noncentral vertex whose partner in the same triangle is white has exactly two blue vertices in its closed neighborhood (itself and the hub), so it forces that partner with probability one on the following round. No claim is made about the minimizing starting vertex over all vertices of \(F_m\).

## Proof

**1. Exact quotient dynamics.** Set \(X_t=B_t\) and write \(e=E_t,s=S_t,b=X_t\). Since the central vertex has degree \(2m\) and has \(1+b\) blue vertices in its closed neighborhood, it attempts to force each white noncentral vertex with probability \(p=(1+b)/(2m)\). Whenever any white vertex remains, \(0<p\le1\). For each of the \(e\) completely white pairs, its two vertices independently succeed with probability \(p\). The completed state has no trials and is absorbing. Every existing single pair completes deterministically in the next round. Thus the claimed three-outcome kernel holds, and, conditionally on the current state,
\[
X_{t+1}=b+s+H_t,\quad H_t\sim\mathrm{Bin}(2e,p),\qquad
S_{t+1}\sim\mathrm{Bin}(e,2p(1-p)). \tag{1}
\]
The two displayed binomial variables need not be independent. Both marginal laws and the three-outcome joint kernel are exact. Since \(X_0=S_0=0\) and \(E_0=m\), these equations specify the entire process.

**2. Early-time lower bound for completion.** From \(2e\le2m\), (1) gives
\[
\mathbb E[X_{t+1}\mid\mathcal F_t]\le 2X_t+S_t+1,
\quad
\mathbb E[S_{t+1}\mid\mathcal F_t]\le X_t+1. \tag{2}
\]
Let \(\lambda=1+\sqrt2\), so \(\lambda=2+\lambda^{-1}\). Multiplying the second inequality by \(\lambda^{-1}\) and adding the first shows, for \(L_t=X_t+S_t/\lambda\),
\[
\mathbb E L_{t+1}\le\lambda\mathbb E L_t+1+\lambda^{-1}.
\]
Consequently \(\mathbb E X_t\le \mathbb E L_t\le C\lambda^t\) for an absolute \(C\). Completion by round \(t\) requires \(X_t=2m\), hence \(\Pr(\tau_m\le t)\le C\lambda^t/(2m)\). For every fixed \(\varepsilon>0\), choosing \(t=\lfloor(1-\varepsilon)\log m/\log\lambda\rfloor\) makes this probability tend to zero.

**3. Rapid initial growth.** Fix \(c\in(0,1/4)\). Until \(X_t\ge cm\), at least \(m-X_t\ge(1-c)m\) triangles are empty. Hence the binomial \(H_t\) in (1) has mean
\[
\mu_t=2E_t p\ge (1-c)(X_t+1). \tag{3}
\]
In this range \(\Pr(H_t\ge1\mid\mathcal F_t)\ge1-e^{-(1-c)}>1/2\). A coupling with independent fair Bernoulli trials therefore shows that, for any sufficiently large fixed \(A\), the level \(A\log\log m\) is reached within \(4A\log\log m\) rounds with probability tending to one (or the larger level \(cm\) is reached earlier). For \(X_t\ge A\log\log m\), the multiplicative Chernoff bound and (3) imply
\[
\Pr(H_t<X_t/4\mid\mathcal F_t)\le e^{-\kappa X_t}, \tag{4}
\]
with an absolute \(\kappa>0\) depending only on \(c\). Taking \(A>3/\kappa\), a union bound over \(O(\log m)\) rounds shows that growth by at least a factor \(5/4\) per round continues, with probability tending to one, until \(X_t\ge K\log m\), for any fixed \(K>0\). This warm-up consumes \(O(\log\log m)\) rounds in probability.

**4. Sharp macroscopic growth exponent.** Fix \(\delta\in(0,1/4)\). Choose \(c>0\) small enough, depending on \(\delta\), and then choose \(K\) large enough. For \(K\log m\le X_t<cm\), the conditional means satisfy
\[
\mathbb E[H_t\mid\mathcal F_t]\ge(1-c)(X_t+1),\qquad
\mathbb E[S_{t+1}\mid\mathcal F_t]\ge(1-c)(1-c/2-o(1))(X_t+1).
\]
The second bound follows from \(p\le c/2+o(1)\). Separate Chernoff bounds, which do not require independence of \(H_t\) and \(S_{t+1}\), give
\[
H_t\ge(1-\delta)X_t,\qquad S_{t+1}\ge(1-\delta)X_t \tag{5}
\]
except with conditional probability at most \(2e^{-\kappa_\delta X_t}\). By choosing \(K\) sufficiently large, a union bound makes (5) valid simultaneously for the next \(O(\log m)\) rounds with probability tending to one, up to the first time \(X_t\ge cm\).

Let \(\lambda_\delta>1\) be the positive root of
\[
\lambda_\delta^2-(2-\delta)\lambda_\delta-(1-\delta)=0.
\]
From (1) and (5) the nonnegative vector \((X_t,S_t)\) grows coordinatewise at least as fast as the matrix
\[
M_\delta=\begin{pmatrix}2-\delta&1\\1-\delta&0\end{pmatrix}.
\]
The positive left Perron eigenvector is \((1,1/\lambda_\delta)\). Thus \(F_t=X_t+S_t/\lambda_\delta\) satisfies \(F_{t+1}\ge\lambda_\delta F_t\) while below \(cm\). Since \(0\le S_t\le X_t\), we have \(F_t\le2X_t\), so starting from \(F_t\ge K\log m\), it takes at most
\[
\frac{\log(2cm/(K\log m))}{\log\lambda_\delta}+O(1)
=\frac{\log m}{\log\lambda_\delta}+o(\log m)
\]
additional rounds to reach \(X_t\ge cm\), with probability tending to one. As \(\delta\downarrow0\), \(\lambda_\delta\to1+\sqrt2\).

**5. The final white vertices vanish in \(O(\log\log m)\) rounds.** Once \(X_t\ge cm\), let \(W_t=2m-X_t\), so \(W_t\le (2-c)m\). When \(W_t\ge1\), the hub attempts to force every white vertex, independently, with failure probability \((W_t-1)/(2m)\); at \(W_t=0\) the process is already complete. Other blue vertices can only accelerate forcing; therefore
\[
W_{t+1}\ \preceq_{\mathrm{st}}\ \mathrm{Bin}\!\left(W_t,\frac{W_t-1}{2m}\right), \tag{6}
\]
conditionally on the present state. Put \(r_0=1-c/2\) and \(r_{j+1}=r_j^{3/2}\). If \(W_t\le2mr_j\), the next white count is stochastically bounded by \(\mathrm{Bin}(\lfloor2mr_j\rfloor,r_j)\), whose mean is at most \(2mr_j^2\). As long as \(2mr_{j+1}\ge(\log m)^2\), Chernoff bounds imply \(W_{t+1}\le2mr_{j+1}\) except with probability \(\exp[-\Omega((\log m)^2)]\), uniformly in \(j\). There are only \(O(\log\log m)\) such steps. At the first step for which \(2mr_{j+1}<(\log m)^2\), a further Chernoff bound gives \(W_{t+1}\le2(\log m)^2\) with high probability. One more round suffices with probability tending to one, because (6) then gives conditional expectation at most \(2(\log m)^4/m=o(1)\). Thus the time after the level \(cm\) is reached is \(O_{\mathbb P}(\log\log m)\).

Combining steps 2–5 and letting \(\delta\downarrow0\) proves the convergence in probability in the theorem.

**6. Convergence of expectations.** For every state with the hub blue, monotone coupling to the same graph started with only the hub blue yields a stochastically no larger remaining time: extra blue vertices can only increase the success probabilities of hub attempts and add successful attempts. The hub-started process itself is stochastically bounded by the hub-started star on \(2m\) leaves: in that coupling all hub success probabilities are at least those of the star, and the pair-edge forces can only help. Geneson and Hogben's star-neighborhood argument (Lemma 2.3 in their 2022 paper, already present in the 2018 preprint) proves a uniform upper bound \(C\log(2m)\) on the expected completion time from the hub of this star. Thus any state with hub blue has conditional remaining expectation at most \(C\log(2m)\).

By Markov's inequality and the strong Markov property, in every block of \(\lceil2C\log(2m)\rceil\) rounds there is conditional probability at least \(1/2\) of completing. This gives geometric block tails and \(\mathbb E\tau_m^2=O((\log m)^2)\). The family \(\{\tau_m/\log m\}\) is therefore uniformly integrable. Its convergence in probability to the displayed constant implies the expectation limit.

## Verification

`check_friendship.py` implements (i) the reduced three-outcome transition using exact rational arithmetic and (ii) an independent full-coloring-state transition over every pattern of individual blue/white leaves. It compares both distributions through seven synchronous rounds for each \(m=1,2,3\), tests all reduced states through \(m=5\) against the normalization and the exact conditional first-moment identities in (1), and solves the finite absorbing expectation equation for \(m=1,\ldots,6\). Run with `python check_friendship.py` using only the Python standard library. Its finite checks validate the quotient and boundary conventions; the asymptotic conclusions follow from the analytic proof above, not from finite enumeration or simulation.

## Relationship to prior work

Chan, Curl, Geneson, Hogben, Liu, Odegard and Ross introduced systematic Markov computations for the same forcing rule in their June 25, 2019 preprint, and their Theorem 3.2 proves \(\Theta(\log n)\) for the graph-optimized expected propagation time of graphs formed by joining a universal vertex to a bounded-degree graph. Here the outer graph is a perfect matching: the present theorem specifies its leading constant, explains it through a nontrivial two-stage Perron eigenvalue, and establishes a matching expectation asymptotic. The earlier theorem concerns the minimum expected time over all starting vertices, and neither determines the hub-started leading coefficient nor proves its convergence in probability. Geneson and Hogben (first publicly circulated December 24, 2018; journal 2022) provide the star-neighborhood time bound used only for uniform integrability. Narayanan and Sun (2019) prove general radius-based upper bounds and extremal graph estimates but no family-specific leading constant. Hu and Sun (2020) and Behague, Marbach and Prałat (2020/2021) examine grids, regular graphs and hypercubes, with different graph regimes. No originality is claimed for the general forcing rule, the general Markov-chain method, or the universal-vertex logarithmic order bound.

## Limitations

The coefficient is specific to synchronous forcing from the common hub on an unweighted bouquet of triangles. It does not cover starting from a noncentral vertex, arbitrary clique-bouquet sizes, asynchronous infection, graph families with shared nonhub vertices, finer centered fluctuation laws, or exact finite-size expected times in elementary closed form. The literature comparison is a best-knowledge scientific priority assessment, not a proof of global uniqueness.

## References

1. Y. Chan, E. Curl, J. Geneson, L. Hogben, K. Liu, I. Odegard, M. Ross, *Using Markov chains to determine expected propagation time for probabilistic zero forcing*, arXiv:1906.11083v1, first posted 2019-06-25, especially Sections 1–3 and Theorem 3.2. https://arxiv.org/pdf/1906.11083
2. J. Geneson, L. Hogben, *Propagation time for probabilistic zero forcing*, arXiv:1812.10476v1, first posted 2018-12-24; journal title *Expected propagation time for probabilistic zero forcing*, *Australasian Journal of Combinatorics* 83 (2022), 397–417, especially Lemma 2.3 and Corollary 2.7. https://ajc.maths.uq.edu.au/pdf/83/ajc_v83_p397.pdf
3. D. Hu, A. Sun, *Probabilistic Zero Forcing on Grid, Regular, and Hypercube Graphs*, arXiv:2010.12343v1, first posted 2020-10-22. https://arxiv.org/pdf/2010.12343
4. N. C. Behague, T. Marbach, P. Prałat, *Tight Bounds on the Probabilistic Zero Forcing on Hypercubes and Grids*, arXiv:2012.00216, first posted 2020-12-01. https://arxiv.org/pdf/2012.00216
5. S. Narayanan, A. Sun, *Bounds on expected propagation time of probabilistic zero forcing*, arXiv:1909.04482v1, first posted 2019-09-10; the radius-based bounds are not a sharp friendship-graph asymptotic. https://arxiv.org/pdf/1909.04482
