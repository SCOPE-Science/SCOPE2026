# Geometric degree law for all linear de-preferential attachment multiplicities

## Finding

**Theorem.** Fix an integer \(m\ge1\) and use the sequential linear de-preferential attachment multigraph defined below. Let \(\widehat\mu_N\) denote the empirical distribution of the \(N\) vertex degrees. Then, almost surely in total variation,

\[
\widehat\mu_N\longrightarrow\pi_m,\qquad
\pi_m(m+r)=\frac1{m+1}\left(\frac m{m+1}\right)^r\quad(r=0,1,2,\ldots),
\]

with zero mass on degrees below \(m\). Moreover there is a pathwise coupling to the uniform \(m\)-out recursive multigraph such that, if \(H_N\) is the number of attachment decisions at which the two targets differ, then

\[
H_N\le R_N,\qquad \frac{R_N}{\log N}\longrightarrow m\quad\text{almost surely},
\qquad
\big\|\widehat\mu_N^{\mathrm{de}}-\widehat\mu_N^{\mathrm{unif}}\big\|_{\mathrm{TV}}
\le \frac{2R_N}{N}.
\]

Thus the two empirical measures are almost surely asymptotically identical at rate \(O((\log N)/N)\), while their common limiting law is the shifted geometric distribution above. The new empirical-law conclusion is of particular interest for \(m>1\).

## Assumptions and scope

At the starting stage \(n=2\), the seed has two vertices, \(m\) joining edges, and \(m\) free half-edges incident to one seed vertex. Its degrees are \((m,2m)\). At the start of each subsequent stage there are \(n\) old vertices with positive degrees \(d_1,\ldots,d_n\); the sum is \((2n-1)m\). A new vertex will acquire exactly \(m\) edges to old vertices. For each half-edge in order, let \(D\) be the sum of the **old-vertex degrees at that instant**, including previously attached half-edges of the same new vertex. Conditionally on all preceding choices, choose old vertex \(i\) with probability

\[
Q_i=\frac{1-d_i/D}{n-1}.
\]

The chosen old degree increments by one; after all \(m\) choices the new vertex is adjoined with degree \(m\). Repeated old-vertex targets within a birth are permitted, as in the motivating multigraph model. The uniform comparison model has the same seed and chooses each old target uniformly from all \(n\) old vertices, independently at every half-edge. The parameter \(m\) is fixed as \(N\to\infty\). For probability measures on nonnegative integers, \(\|\mu-\nu\|_{\mathrm{TV}}=\frac12\sum_{k\ge0}|\mu(k)-\nu(k)|\).

## Proof

**1. Exact rejection coupling.** At an arbitrary half-edge step with \(n\) old vertices, sample a first proposal \(U\) uniformly from the old vertices and an independent uniform mark \(T\). Accept if \(T\le1-d_U/D\). Otherwise repeat with fresh independent uniform proposals and marks until one is accepted. At each attempt,

\[
\Pr(\text{accept candidate }i\mid\text{current graph})=\frac1n\left(1-\frac{d_i}D\right),
\quad
\Pr(\text{accept any})=1-\frac1n=\frac{n-1}n.
\]

Therefore the accepted vertex has precisely conditional distribution \(Q_i\). Use each first proposal \(U\), whether or not accepted by the de-preferential process, as the uniform model's attachment target. The first proposals are independent uniforms (given the respective old-vertex counts), so the second process has the uniform \(m\)-out recursive law. If the first proposal was accepted the targets agree. The first-rejection event, conditional on the **entire previous history**, has probability exactly \(1/n\), because \(\sum_i d_i=D\). Thus these events are mutually independent, with \(m\) Bernoulli variables of parameter \(1/n\) for each \(n=2,\ldots,N-1\). If \(R_N\) counts them, clearly \(H_N\le R_N\).

**2. The logarithmic error budget.** Independence gives

\[
\mathbb ER_N=m\sum_{n=2}^{N-1}\frac1n=m\log N+O_m(1),
\qquad
\log\mathbb Ee^{tR_N}=m\sum_{n=2}^{N-1}
\log\left(1+\frac{e^t-1}{n}\right).
\]

For any fixed positive \(\varepsilon\), exponential Markov bounds with a sufficiently small fixed positive or negative \(t\) imply

\[
\Pr\big(|R_N-m\log N|>\varepsilon\log N\big)\le C_{m,\varepsilon}N^{-c_{m,\varepsilon}}.
\]

Summing this bound along dyadic \(N=2^j\), applying Borel--Cantelli, and using monotonicity of \(R_N\) between consecutive dyadic points proves \(R_N/\log N\to m\) almost surely. Altering a single attachment target changes the final degree count of at most two old vertices, each by one. In any coupled realization, changing all \(H_N\) discordant targets hence changes the histogram \(\ell^1\) distance by at most \(4H_N\). The empirical total variation bound is consequently \(2H_N/N\le2R_N/N\).

**3. Limiting degree law of the uniform comparison process.** Ignoring the two seed vertices (whose proportion is \(2/N\)), a vertex born at time \(i\ge3\) starts with degree \(m\). At every later stage with \(n\) existing vertices, its incident count increases by an independent \(\operatorname{Binomial}(m,1/n)\). Thus its excess degree at terminal stage \(N\) is a sum of independent Bernoulli variables with parameter \(1/n\), each repeated \(m\) times for \(n=i,\ldots,N-1\). If \(i/N\to u\in(0,1]\), its mean tends to \(m\log(1/u)\), while the sum of squared probabilities tends to zero. Therefore its excess degree converges to \(\operatorname{Poisson}(m\log(1/u))\). Averaging over birth ranks, for fixed \(r\ge0\), bounded convergence (with the endpoint near \(u=0\) removed and then restored) gives

\[
\lim_{N\to\infty}\mathbb E\widehat\mu_N^{\mathrm{unif}}(m+r)
=\int_0^1 e^{-m\log(1/u)}
\frac{[m\log(1/u)]^r}{r!}\,du
=\int_0^\infty e^{-(m+1)s}\frac{(ms)^r}{r!}\,ds
=\frac{m^r}{(m+1)^{r+1}}.
\]

The entire uniform graph at stage \(N\) is a function of \(m(N-2)\) independent uniform attachment choices. Changing one choice changes the degrees of at most two vertices, so the empirical fraction of any fixed degree is Lipschitz with constant at most \(2/N\) per choice. The bounded-differences inequality therefore gives, for any fixed \(r\) and \(\varepsilon>0\), a concentration bound of form \(2\exp[-c_m\varepsilon^2N]\). Borel--Cantelli implies almost-sure convergence of each degree fraction to the displayed geometric probability. A countable intersection over \(r\), together with \(\sum_{r\ge0}\pi_m(m+r)=1\), upgrades this to almost-sure total variation convergence: truncate degrees at a fixed large \(r\), use convergence there, and bound both tails by the remaining geometric mass plus the finite-coordinate error.

**4. Transfer.** The coupling estimate in step 2 and the comparison limit in step 3 imply the claimed almost-sure total variation convergence for the linear de-preferential multigraph. In particular, \(m\ge2\) requires no new local recurrence solution.

## Verification

The included standalone `verify.py` uses only the Python standard library and is run with `python3 verify.py`. It exactly enumerates the normalized sequential transition kernels for small graphs at \(m=1,2,3\), checks the rejection coupling identity with rational arithmetic, checks finite uniform attachment generating functions, and samples coupled graphs of 20,000 vertices for each of \(m=1,2,3\). The recorded run completed with `VERIFY_OK check_count= 156614`. These finite checks are corroboration only; steps 1--4 provide the infinite mathematical proof.

## Relationship to prior work

Bandyopadhyay and Sen, *De-Preferential Attachment Random Graphs* (arXiv:2508.18144, 2025), equations defining linear attachment in Section 1.2.1 and Theorems 2.3--2.6, obtain the geometric law for \(m=1\) but explicitly leave the empirical law for \(m>1\) unresolved in the remark following Theorem 2.6. Bandyopadhyay and Joshi, *Generalised De-Preferential Random Graphs* (arXiv:2512.12408, 2025), state their linear empirical-law formula only for \(m=1\). The uniform recursive attachment geometric law is classical and is not asserted to be new. Here the novel tree/graph-model statement is the exact small-error pathwise coupling and its consequences for the previously unresolved multiple-attachment model, not geometric mixing itself.

## Limitations

The theorem is restricted to the **linear** de-preferential kernel given above, with fixed \(m\), sequential conditional choices, and permitted repeated targets. It does not cover inverse-de-preferential kernels, growing \(m\), or no-multiple-edge variants whose per-edge transition law changes. The bound compares empirical **degree histograms**, not the graph structures in total variation. Historical priority has been compared against the stated closely related manuscripts and database queries but has not been independently certified. The finite verification cannot replace the proof of the almost-sure limit.

## References

1. Antar Bandyopadhyay and Subhabrata Sen, *De-Preferential Attachment Random Graphs*, arXiv:2508.18144 (first posted 2025-08-25), https://arxiv.org/html/2508.18144v2.
2. Antar Bandyopadhyay and Kunal Joshi, *Generalised De-Preferential Random Graphs*, arXiv:2512.12408 (first posted 2025-12-13), https://arxiv.org/abs/2512.12408.
3. Classical uniform recursive attachment and the exponential--Poisson mixture, used only as a comparison; its standard limit is reproved above for self-containment.
