# Gumbel coverage of all pairs by a Johnson-subset walk

## Finding
Fix an integer \(r\geq3\). Let \(H_0\) be a uniformly random \(r\)-subset of \([n]\), with \(n>r\). At every integer time, independently choose a uniform element of the current set to delete and a uniform element of its *previous complement* to insert. A pair is observed when it is contained in one of the visited sets. Define \(T_n\) as the smallest nonnegative integer such that every pair has been observed in \(H_0,\ldots,H_{T_n}\), and put
\[
M_n=\binom n2,\qquad a_n=\frac{M_n}{r-1}.
\]
Then, for every real \(x\),
\[
\lim_{n\to\infty}\Pr\left\{\frac{T_n-a_n\log M_n}{a_n}\le x\right\}
=\exp(-e^{-x}),
\]
and
\[
\mathbb E T_n\sim a_n\log M_n\sim\frac{n^2\log n}{r-1}.
\]
In particular the conjectured first-order Markovian two-super-coupon coverage time holds for **every fixed \(r\ge3\)**; the conclusion is stronger because it also gives the sharp Gumbel window.

## Assumptions and scope
The replacement step samples the new label uniformly from the complement of the set **before** deletion, not from the complement after deletion. The observations at time zero count toward coverage. Fix \(r\) first, then let \(n\) tend to infinity. The result uses no independence between consecutive \(r\)-subsets. The pair-covering problem here is the case \(s=2\) of Markovian super-coupon collection. The source preprint was first public on 2023-04-03.

## Proof
**1. Exact finite-state avoidance reduction.** Fix any integer \(k\ge1\) and \(k\) distinct target pairs. Regard these pairs as edges of a fixed finite simple graph \(F\), with \(w\le2k\) nonisolated vertices. Let \(S_t=H_t\cap V(F)\). Until a target pair appears, \(S_t\) belongs to the finite set \(\mathcal A_F\) of edge-free subsets of \(V(F)\) of cardinality at most \(r\). This is an *exact* killed Markov chain: its substochastic matrix \(Q_F(n)\) has entries obtained by dropping each currently present marked vertex with probability \(1/r\), dropping an unmarked vertex with the complementary probability, and inserting each individually absent marked vertex with probability \(1/(n-r)\) conditional on the deletion. Transitions completing an edge of \(F\) are killed.

Set \(\varepsilon=(n-r)^{-1}\). Since \(r\) and \(F\) are fixed, \(Q_F\) is a fixed-dimensional matrix whose entries are polynomials in \(\varepsilon\). At \(\varepsilon=0\), no new marked vertices can enter; each present marked vertex disappears with probability \(1/r\) at a step. Ordering states by cardinality makes this matrix triangular with eigenvalues among \(1-j/r\), \(0\le j\le r\). The eigenvalue 1 is simple (its sole recurrent class is the empty marked set); the others have modulus at most \(1-1/r\). Consequently the Perron eigenvalue \(\lambda_F(\varepsilon)\) and its normalized left eigenvector \(\alpha_F(\varepsilon)\) are analytic near zero. For all sufficiently small positive \(\varepsilon\), the killed matrix is irreducible and aperiodic on its safe states.

**2. The universal rare-entrance coefficient.** Normalize \(\sum_{S\in\mathcal A_F}\alpha_F(S)=1\). Its first-order stationary equations give
\[
\alpha_F(\varnothing)=1+O_F(\varepsilon),\qquad
\alpha_F(\{v\})=r\varepsilon+O_F(\varepsilon^2),\qquad
\sum_{|S|\ge2}\alpha_F(S)=O_F(\varepsilon^2).
\]
For a safe state \(S\), let \(d_F(S)=1-\sum_{S'}Q_F(S,S')\) be the one-step killing probability. Exactly,
\[
d_F(\varnothing)=0,\qquad
 d_F(\{v\})=\frac{r-1}{r}\deg_F(v)\,\varepsilon.
\]
For any other safe state, \(d_F(S)=O_F(\varepsilon)\): an existing safe set cannot become unsafe without inserting a marked vertex. Multiplying the left-eigenvector identity by the all-ones vector now yields
\[
1-\lambda_F
=\sum_S\alpha_F(S)d_F(S)
=(r-1)\varepsilon^2\sum_{v\in V(F)}\deg_F(v)+O_F(\varepsilon^3)
=2(r-1)k\varepsilon^2+O_F(\varepsilon^3).
\]
This coefficient depends **only on the number of target pairs**, not on how those pairs overlap.

**3. Exponential avoidance and Poisson missing pairs.** The spectral gap in step 1, analytic spectral projections, and the fact that uniform \(H_0\) has \(\Pr(S_0=\varnothing)=1-O_F(n^{-1})\), imply, for all nonnegative integer \(t\),
\[
\Pr\{\text{all }k\text{ target pairs remain unseen through }t\}
=(1+O_F(n^{-1}))\lambda_F(n)^t+O_F(q_F^t),
\]
where \(q_F<1\) is fixed, for all sufficiently large \(n\). The \(O_F\) bounds are uniform over the finitely many isomorphism types of graphs with \(k\) distinct edges.

Let \(t_n(x)=\lfloor a_n(\log M_n+x)\rfloor\), and let \(N_n(x)\) count the pairs not yet observed at this time. Because
\[
\lambda_F(n)=1-\frac{2(r-1)k}{n^2}+O_F(n^{-3}),
\]
the displayed probability at \(t_n(x)\) equals \(M_n^{-k}e^{-kx}(1+o(1))\). Summing over ordered \(k\)-tuples of distinct pairs gives every factorial-moment limit
\[
\mathbb E[(N_n(x))_k]=(M_n)_kM_n^{-k}e^{-kx}(1+o(1))\longrightarrow e^{-kx}.
\]
The factorial-moment criterion therefore gives \(N_n(x)\Rightarrow\operatorname{Poisson}(e^{-x})\), and \(\Pr(T_n\le t_n(x))=\Pr(N_n(x)=0)\to\exp(-e^{-x})\).

**4. Expectation.** The Gumbel convergence implies \(T_n/(a_n\log M_n)\to1\) in probability and hence the required lower bound on its nonnegative expectation. For the upper bound, the \(k=1\) avoidance formula implies, for sufficiently large \(n\) and every \(t\ge0\),
\[
\Pr(T_n>t)\le M_n\left[C\lambda_1(n)^t+Cq^t\right],
\]
with constants \(C<\infty\) and \(q<1\), and \(-a_n\log\lambda_1(n)=1+O(n^{-1})\). Summing this inequality after \(t=(1+\eta)a_n\log M_n\) gives a tail contribution \(o(a_n\log M_n)\) for any fixed \(\eta>0\). Hence \(\mathbb E T_n\sim a_n\log M_n\).

## Verification
Run `python verify.py` with Python 3 and no third-party packages. The checker compares exact rational avoidance probabilities from the complete Johnson walk with those from the reduced finite-state chain for small \(n\), multiple \(r\), disjoint and intersecting forbidden-pair families. It also numerically checks the universal coefficient \(2(r-1)|E(F)|\) through quasi-stationary power iteration. The packaged run passed 212 assertions. Finite calculations check the reduction and rate approximations, not the infinite theorem; the analytic argument above supplies the latter.

## Relationship to prior work
Athreya, S. Mukherjee, and S. S. Mukherjee explicitly conjectured the leading expectation for Markovian \(s\)-super-coupons and proved only the diagonal \(s=r\) walk case. Their independent-block \(r\)-subset model has a Gumbel limit, but does not cover temporally dependent Markovian pair coverage. The present result treats **\(s=2\), fixed \(r\ge3\)** and supplies both the conjectured leading expectation and the Gumbel law by a different finite-avoidance spectral argument. Earlier random covering-design results concern independently sampled blocks and do not imply the Markovian conclusion. This statement is not a claim that all cases \(2<s<r\) are settled.

## Limitations
The proof is asymptotic for each fixed \(r\); it does not handle \(r\) growing with \(n\), higher super-coupon sizes, nonuniform update kernels or an explicit finite-\(n\) convergence rate. The displayed Poisson convergence is weak convergence, not a total-variation bound. Literature comparison supports novelty relative to sources examined, but cannot conclusively rule out an equivalent result elsewhere. Independent mathematical validation has not been performed.

## References
1. S. Athreya, S. Mukherjee, S. S. Mukherjee, *On a generalisation of the coupon collector problem*, arXiv:2304.01145, first posted 2023-04-03; Journal of Theoretical Probability 38, article 54 (2025). https://arxiv.org/abs/2304.01145 ; https://doi.org/10.1007/s10959-025-01417-w . Conjecture 2.4 and Theorems 2.3, 2.5.
2. A. P. Godbole and S. Janson, *Random covering designs*, Journal of Combinatorial Theory, Series A 75 (1996), 85–98. https://doi.org/10.1006/jcta.1996.0065 . Independent randomly chosen blocks.
3. P. Erdős and A. Rényi, *On a classical problem of probability theory*, Magyar Tud. Akad. Mat. Kutató Int. Közl. 6 (1961), 215–220. Classical coupon collection and Gumbel extremes.
