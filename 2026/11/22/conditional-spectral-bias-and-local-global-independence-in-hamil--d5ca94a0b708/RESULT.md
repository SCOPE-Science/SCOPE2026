# Conditional spectral bias and local–global independence in Hamiltonian random threshold graphs

## Finding

Consider the uniform random threshold graph on \(n\ge4\) vertices. Condition on the graph containing a Hamiltonian cycle. Write \(\lambda_2\) for its *unnormalized* Laplacian algebraic connectivity, \(\omega\) for clique number and \(e\) for the number of edges. Put \(L=n-1\). Then

\[
\left(\lambda_2,\;\frac{2\omega-(n+1)}{\sqrt L},\;\frac{2e-n(n-1)/2}{L^{3/2}}\right)
\xrightarrow{d}
\left(R,\,\mathfrak m(1),\,\int_0^1\mathfrak m(t)\,dt\right),
\]

where \(\mathfrak m\) is standard Brownian meander and \(R\) is **independent of the whole process** \(\mathfrak m\), with

\[
\Pr(R=r)=\frac{r-1}{2^r},\qquad r=2,3,\ldots.
\]

The convergence holds jointly with the full rescaled positive creation walk in \(C[0,1]\) (linearly interpolated). In particular, \(\mathbb E[\lambda_2\mid\text{Hamiltonian}]\to4\), versus unconditioned expectation \(1\) for each \(n\). The limiting endpoint and area are *not* mutually independent; only their joint process is independent of \(R\).

There is also an exact finite conditional law. For integer \(a\ge1\) and \(t\ge0\), let

\[
B(t,a)=\sum_{j=\lceil(t+1-a)/2\rceil}^{\lceil(t+1-a)/2\rceil+a-1}\binom tj,
\]

where binomial coefficients outside the range \(0\le j\le t\) are zero. Let \(N_L=\binom{L-1}{\lfloor(L-1)/2\rfloor}\). For \(2\le r<L\), the conditional probability that the trailing dominating-vertex run has length \(r\) is exactly \(B(L-r-1,r-1)/N_L\); at \(r=L\) it is \(1/N_L\). The algebraic connectivity equals this run length unless all creation bits are one, in which case it equals \(n\). This explicitly handles the complete-graph boundary.

## Assumptions and scope

Sample independent \(U_1,\dots,U_n\sim\operatorname{Uniform}[0,1]\), joining distinct \(i,j\) when \(U_i+U_j>1\). The equivalent creation-sequence model of Reilly and Scheinerman is used: start with one vertex and successively add an isolated vertex for bit zero or a vertex adjacent to all existing vertices for bit one, with independent fair bits \(s_1,\ldots,s_L\). The result concerns unweighted, unnormalized graph Laplacians and ordinary undirected Hamiltonian cycles. Conditioning is on an event of strictly positive probability at each finite order. Here \(\mathfrak m\) is the finite-horizon Brownian meander, not the infinite-horizon Bessel-type conditioned process.

## Proof

**1. Graph-to-walk identification.** Reverse the creation bits and set \(\xi_k=2s_{L+1-k}-1\) and \(S_k=\sum_{i=1}^k\xi_i\). The Hamiltonicity criterion in Reilly–Scheinerman, Theorem 5.20, states precisely that \(S_k>0\) for all \(1\le k\le L\). Its Appendix A gives the count \(N_L\) of such positive walks. Their results on Laplacian eigenvalues imply that the algebraic connectivity equals the number \(R_L\) of initial consecutive \(+1\) steps in this reversed walk, except for the all-up word, for which the connectivity equals \(n\). The conditional probability of the all-up word is \(1/N_L\to0\).

For every creation word, the identities \(\omega=1+\sum_{j=1}^Ls_j\) and \(e=\sum_{j=1}^Ljs_j\) yield, by summation by parts,

\[
2\omega-(n+1)=S_L,\qquad 2e-\frac{n(n-1)}2=\sum_{k=1}^L S_k.
\]

Thus the clique and edge statistics are the endpoint and integrated height of *the same* constrained walk. This normalization is exact, including at all finite boundaries.

**2. Exact local law and limit.** Survival for \(t\) further fair steps from a positive integer height \(a\) is counted by the reflection-principle number \(B(t,a)\) above. If \(2\le r<L\), the event \(R_L=r\) forces exactly \(r\) initial up steps followed by one down step; its surviving continuation begins at height \(r-1\) and has \(L-r-1\) steps. The all-up path is the unique case \(R_L=L\), establishing the stated exact distribution. For fixed \(a\) and \(t\to\infty\), the \(a\) binomial terms in \(B(t,a)\) are central and asymptotically equal. Comparing them with \(N_L\) gives, for each fixed \(r\ge2\),

\[
\Pr(R_L=r\mid\text{Hamiltonian})\longrightarrow (r-1)2^{-r}.
\]

Since \(\sum_{r=2}^\infty(r-1)2^{-r}=1\), the local variables are tight and converge to \(R\). More quantitatively, \(B(t,a)\le a\binom{t}{\lfloor t/2\rfloor}\) and the central-binomial bounds imply an absolute \(C\) with \(\Pr(R_L\ge r\mid\text{Hamiltonian})\le Cr2^{-r}\) for all \(2\le r\le L\). The exceptional complete-graph connectivity \(n\) occurs with probability \(1/N_L\), so its contribution to any fixed positive moment vanishes. Uniform exponential tails therefore imply convergence of all fixed positive moments of \(\lambda_2\); the displayed limiting mean is \(\sum_{r\ge2}r(r-1)2^{-r}=4\).

**3. Process convergence and independence.** The classical finite-horizon conditioned random-walk invariance principle (Iglehart's meander theorem and subsequent extensions) yields \(S_{\lfloor Lt\rfloor}/\sqrt L\Rightarrow\mathfrak m(t)\) in the uniform topology after linear interpolation under positive survival. Fix \(r\ge2\). Conditional on \(R_L=r\) and survival, the first \(r+1\) steps are deterministic and the remaining independent walk starts at the fixed height \(r-1\), conditioned to stay strictly positive for \(L-r-1\) steps. The fixed-positive-start version of the same finite-horizon invariance principle yields the *same* Brownian meander. The deterministic initial segment vanishes after space–time scaling.

Hence for every bounded continuous path functional \(F\),

\[
\lim_{L\to\infty}\mathbb E\bigl[F(S^{(L)})\,\mathbf1_{\{R_L=r\}}\mid\text{Hamiltonian}\bigr]
=\frac{r-1}{2^r}\,\mathbb E[F(\mathfrak m)].
\]

Tightness of \(R_L\) allows summing over \(r\), proving independence of the entire limiting process from \(R\). Continuous mapping of the endpoint and integral proves the joint graph-statistic limit. Replacing \(R_L\) with \(\lambda_2\) changes the finite law only on the complete-graph event of vanishing conditional probability.

## Verification

Run `python3 verify.py` using Python 3 standard library. The independent exhaustive finite checker constructs all creation words through length 12 and verifies their graph edges, universal-vertex count, minimum degree, exact edge and clique identities and positive-walk counts. For up to nine vertices it separately tests existence of Hamiltonian cycles by a subset dynamic program and compares it against the strict-positive-walk condition. It verifies the local-run reflection formula and separately checks positive-walk path-area sums by a height-state dynamic program through 79 steps. It verifies the survival reflection formula directly by exhaustive short-step enumeration. The checker executes 42,747 assertions. These finite checks are *not* proofs of the infinite-dimensional weak convergence; Step 3 invokes the classical probabilistic invariance principle.

## Relationship to prior work

Reilly and Scheinerman (2009) established the equivalent independent-bit threshold graph model, the exact Hamiltonicity criterion, unconditioned algebraic connectivity, and related individual graph invariants. Those results are inputs rather than new claims here. Iglehart (1974) and the finite-horizon random-walk meander literature established the conditioned process limit. Schwerdtfeger (arXiv first version 2011) determined joint meander endpoint and area laws. Those global limits are likewise not claimed as new. The assessed contribution is the *Hamiltonicity-conditioned local spectral distribution together with its asymptotic independence from the full global rescaled creation path*, and its precise joint interpretation for graph algebraic connectivity, clique number and edge count. This is a mathematically natural rare-event conditioning question in the original random-graph model; the exact conditional spectral law and local–global separation were not established in the accessible portions of the cited sources. Novelty is subject to the residual risks stated below.

## Limitations

The claim is restricted to iid fair-bit (uniform vertex-weight) threshold graphs, simple undirected Hamiltonian cycles and the unnormalized Laplacian. There is no assertion of independence at finite order; no explicit convergence *rate* for the joint weak limit is claimed. The endpoint and area of Brownian meander are dependent. The graph-to-walk identities and finite local law are self-contained; the process limit relies on the established finite-horizon meander invariance theorem. The 1974 primary text was not fully accessible and historical alternative formulations could have implicit stronger coverage; a dedicated external mathematical audit has not occurred.

## References

1. D. L. Iglehart, *Functional Central Limit Theorems for Random Walks Conditioned to Stay Positive*, Annals of Probability **2** (1974), 608–619, https://doi.org/10.1214/aop/1176996607 (published August 1, 1974; abstract inspected).
2. F. Caravenna and L. Chaumont, *Invariance principles for random walks conditioned to stay positive*, Annales de l'Institut Henri Poincaré **44** (2008), 170–190, https://arxiv.org/abs/math/0602306 (first public preprint February 14, 2006).
3. E. P. Reilly and E. R. Scheinerman, *Random Threshold Graphs*, Electronic Journal of Combinatorics **16** (2009), R130, https://doi.org/10.37236/219 (published October 31, 2009).
4. U. Schwerdtfeger, *Limit laws for discrete excursions and meanders and linear functional equations with a catalytic variable*, https://arxiv.org/abs/1105.5175 (first public version May 26, 2011).
