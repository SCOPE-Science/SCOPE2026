# Even-Poisson jamming defects at an inverse-size weak channel in a complete tripartite adsorption model

## Finding

For each integer \(n\ge1\), take the complete tripartite graph with independent vertex classes \(A,B,C\) of sizes \(n,n,2n\), respectively. At each step an admissible edge is selected proportionally to its weight, its two endpoints are occupied irreversibly, and the procedure repeats until no admissible edge remains. Each edge between \(A\) and \(B\) has weight \(w_n\ge0\); every edge between \(A\) and \(C\), or \(B\) and \(C\), has weight one. Equivalently, the edges attempt adsorption with independent exponential clocks of the specified rates, and attempted occupations are accepted only if both endpoints are vacant.

Let \(K_n\) be the number of accepted \(A\)-\(B\) dimers, and \(R_n\) the number of vertices still vacant after jamming. If \(n w_n\to\lambda\) for a finite \(\lambda\ge0\), then

\[
R_n=2K_n\quad\text{pathwise},\qquad K_n\xrightarrow{\mathrm d}\operatorname{Poisson}(\lambda/2).
\]

For every fixed nonnegative integer \(j\),

\[
\Pr(R_n=2j)\longrightarrow e^{-\lambda/2}\frac{(\lambda/2)^j}{j!},
\qquad \Pr(R_n\text{ is odd})=0.
\]

Every fixed nonnegative integer moment converges. In particular,

\[
\Pr(R_n=0)\longrightarrow e^{-\lambda/2},\qquad
\mathbb E R_n\longrightarrow\lambda,\qquad
\operatorname{Var}(R_n)\longrightarrow 2\lambda.
\]

Thus, at the naturally vanishing interaction scale \(w_n\asymp n^{-1}\), the terminal vacancy count has a nondegenerate *even-Poisson* law rather than a deterministic extensive density. The zero-parameter case includes the regime \(n w_n\to0\), when complete occupancy holds with probability tending to one.

## Assumptions and scope

The graph has exactly \(4n\) vertices partitioned as stated; all cross-part edges are present, there are no intra-part edges, and all weights are nonnegative. Occupation attempts are memoryless and independent, with rates as above; after any success the occupied endpoints are unavailable forever. The theorem addresses the *terminal* state for sequences with a finite limit of \(n w_n\). It does not assert a limit for \(n w_n\to\infty\), nor for spatial adsorption models.

The model is an exactly lumpable Markov chain. If the remaining vacant counts are \((a,b,c)\), the next successful adsorption chooses \(AB,AC,BC\) with respective rates \(w_n ab,ac,bc\). This specifies both the stochastic dynamics and its reproduction without simulating futile attempts.

## Proof

**1. Conservation and termination.** Initially \(c=a+b=2n\). When an \(AC\) or \(BC\) edge is accepted, both sides of \(c-(a+b)\) decrease by one, preserving their difference. When an \(AB\) edge is accepted, \(a+b\) decreases by two while \(c\) is unchanged, increasing the difference by two. Consequently, at every step,

\[
c=a+b+2k,\]

where \(k\) is the current number of accepted \(AB\) edges. If \(a+b>0\), then \(c>0\), so at least one admissible \(AC\) or \(BC\) edge exists. Hence the process ends precisely when \(a=b=0\), at which time \(c=2K_n\). This proves the pathwise relation \(R_n=2K_n\) and shows there are at most \(2n\) successful events.

**2. A universal rare-event bound.** Write \(s=a+b\) and \(d=a-b\). Given the state just before a committed adsorption, the probability that its edge is \(AB\) is

\[
p_n(s,d,k)=\frac{w_n ab}{cs+w_n ab}
=\frac{\frac{w_n}{4}(s^2-d^2)}{s(s+2k)+\frac{w_n}{4}(s^2-d^2)}\le\frac{w_n}{4}
\]

for \(s>0\). If \(w_n/4\le1\), a standard uniform-variable coupling of the success indicators therefore bounds \(K_n\) by a binomial random variable with \(2n\) trials and success probability \(w_n/4\). Since \(nw_n\) is bounded, this yields \(K_n=O_{\mathbb P}(1)\) and, for each fixed real \(t>0\),

\[
\sup_{n\text{ sufficiently large}}\mathbb E e^{tK_n}
\le\sup_{n\text{ sufficiently large}}\bigl(1+\tfrac{w_n}{4}(e^t-1)\bigr)^{2n}<\infty.
\]

The finite initial indices for which \(w_n/4>1\) do not affect the limit.

**3. Control of the competition between the two small classes.** Conditioned on the next accepted edge *not* being \(AB\), it is \(AC\) with probability \(a/s\) and \(BC\) with probability \(b/s\). In these cases \(d\) changes by \(-1\) and \(+1\), respectively; an \(AB\) event leaves it unchanged. Consequently, for the event-indexed filtration,

\[
\mathbb E(d_{t+1}^2-d_t^2\mid\mathcal F_t)
=(1-p_n(s,d,k))\left(1-\frac{2d^2}{s}\right)\le1.
\]

Stop after jamming by retaining the final value, so there are at most \(2n\) steps and the same upper bound applies. Starting from \(d_0=0\), optional stopping at the first time \(\lvert d_t\rvert\ge\delta n\) shows, for any fixed \(\delta>0\),

\[
\Pr\!\left(\max_{0\le t\le2n}|d_t|\ge\delta n\right)
\le\frac{2}{\delta^2 n}.
\]

In particular, \(\max_t|d_t|/n\to0\) in probability, while the number \(k\) of weak-channel events is uniformly tight by Step 2.

**4. A uniform Poisson hazard before depletion.** Fix \(0<\varepsilon<2\), and consider steps at which \(s\ge\varepsilon n\). Rewrite the exact conditional probability as

\[
p_n(s,d,k)=\frac{w_n}{4}\frac{1-(d/s)^2}{1+2k/s+(w_n/4)(1-(d/s)^2)}.
\]

By Steps 2–3, uniformly over those steps,

\[
\max_{s\ge\varepsilon n}\left|n p_n(s,d,k)-\frac{\lambda}{4}\right|
\xrightarrow{\mathbb P}0.
\]

This holds also for \(\lambda=0\). Let \(T_{n,\varepsilon}\) be the number of accepted edges until \(s\le\varepsilon n\). Every non-\(AB\) event reduces \(s\) by one, and every \(AB\) event reduces it by two, so after \(t\) events \(s_t=2n-t-k_t\). Hence

\[
T_{n,\varepsilon}=(2-\varepsilon)n+O_{\mathbb P}(1)
\]

(up to integer rounding). Use fresh independent uniform random variables to realize the \(AB\) indicators. Conditional on previous choices, replacing the state-dependent threshold \(p_n\) with the constant \(q_n=\lambda/(4n)\) changes that indicator with conditional probability \(|p_n-q_n|\). The uniform convergence just proved, bounded by a constant times \(1/n\), implies that the chance of any replacement error among the first \((2-\varepsilon)n+O_{\mathbb P}(1)\) steps tends to zero. The \(O_{\mathbb P}(1)\) variation in the stopping index has vanishing probability of containing an extra weak-channel event. Thus the count \(K_{n,\varepsilon}\) accumulated before the threshold satisfies

\[
K_{n,\varepsilon}\xrightarrow{\mathrm d}
\operatorname{Poisson}\bigl((2-\varepsilon)\lambda/4\bigr),
\]

by the binomial-to-Poisson limit.

**5. Control of the terminal boundary layer.** Once \(s\le\varepsilon n\), at most \(\lceil\varepsilon n\rceil\) more successful adsorptions occur, each with conditional \(AB\) probability no larger than \(w_n/4\). Therefore

\[
\Pr(K_n\ne K_{n,\varepsilon})
\le\lceil\varepsilon n\rceil w_n/4
\longrightarrow\varepsilon\lambda/4.
\]

Letting \(\varepsilon\downarrow0\) proves convergence to \(\operatorname{Poisson}(\lambda/2)\) for the full process. The exponential-moment bound in Step 2 makes every fixed integer power uniformly integrable, giving all moment assertions. Together with Step 1, this finishes the proof.

## Verification

The included standard-library program `verify.py` computes exact rational terminal generating polynomials using both (i) the aggregate three-count Markov recurrence and (ii) an independent labelled-vertex-subset recurrence. It also checks exact nonnegativity, normalization and the binomial mean bound for additional sizes, and uses fixed-seed simulations as a limited numerical smoke test. It returns `PASS 52 exact-rational identities and seeded statistical smoke checks`. Reproduce with `python3 verify.py` from the same directory. Finite testing is not the proof of the stated limit; the argument above covers every admissible sequence with finite \(\lambda\).

## Relationship to prior work

Random sequential adsorption and irreversible graph occupancy are established subjects. Pippenger [1] studied random adsorption on graphs, primarily sparse regular/girth regimes, including edge occupancy. Hilhorst, Washenberger and Täuber [2] developed multispecies pair-annihilation mean-field and fluctuation theory, with a finite-volume final-state analysis; their permutation-symmetric interaction and equal-initial-density assumptions are distinct from the present strongly unequal populations and rate tending to zero. Cadilhe, Araújo and Privman [3] surveyed continuous, lattice and patterned random sequential adsorption; Purvis *et al.* [4] analysed near-jamming availability in one- and two-dimensional lattice settings.

Exact finite-size Markov recursions and deterministic large-system limits at *fixed positive* tripartite edge weights do not, by themselves, establish the simultaneous \(w_n\sim\lambda/n\) limit, the even-Poisson terminal law or convergence of all moments. The contribution here is the stochastic weak-channel boundary law under a balanced-capacity conservation relation, not a new general construction of adsorption processes.

## Limitations

The result is for the specific classes \((n,n,2n)\), complete cross-part connectivity, and a single weak edge type. It does not describe spatial propagation, finite-time kinetics or an unbounded limit of \(nw_n\). This derivation is neither an independent external certification nor evidence that equivalent findings cannot exist in unindexed literature. Full text of one historically relevant graph-adsorption article [1] was not available through the examined access routes; its publicly accessible abstract describes different sparse-graph regimes, but the incomplete inspection leaves a residual historical-priority risk.

## References

1. N. Pippenger, “Random Sequential Adsorption on Graphs,” *SIAM Journal on Discrete Mathematics* **2** (1989), 393–401. DOI: https://doi.org/10.1137/0402034.
2. H. J. Hilhorst, M. J. Washenberger and U. C. Täuber, “Symmetry and species segregation in diffusion-limited pair annihilation,” arXiv:cond-mat/0409079v1, first publicly available 2004-09-03. https://arxiv.org/html/cond-mat/0409079v1.
3. A. Cadilhe, N. A. M. Araújo and V. Privman, “Random Sequential Adsorption: From Continuum to Lattice and Pre-Patterned Substrates,” arXiv:cond-mat/0611413v1, first publicly available 2006-11-15. https://arxiv.org/abs/cond-mat/0611413.
4. B. E. Purvis, L. Reeve, J. A. D. Wattis and Y. Mao, “Scaling behavior near jamming in random sequential adsorption,” *Physical Review E* **91** (2015), 022118. https://doi.org/10.1103/PhysRevE.91.022118.
