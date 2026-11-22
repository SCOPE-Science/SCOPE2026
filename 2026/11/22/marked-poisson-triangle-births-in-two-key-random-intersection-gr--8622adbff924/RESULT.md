# Marked Poisson triangle births in two-key random intersection graphs

## Finding

For each integer \(m\ge3\), let \(S_1,S_2,\ldots\) be independent, uniform, unordered two-element subsets of \(\{1,\ldots,m\}\). After the first \(n\) observations, put an edge between distinct indices \(i,j\le n\) exactly when \(S_i\cap S_j\ne\varnothing\), and write \(T_m(n)\) for the number of unordered vertex triples spanning triangles. For a key \(a\), let \(J_{m,a}\) be the index of its third appearance in the sequence. Then, as \(m\to\infty\),

\[
\Xi_m=\sum_{a=1}^{m}\delta_{(J_{m,a}/m^{2/3},\,a/m)}\ \Longrightarrow\ \operatorname{PPP}(4t^2\,dt\,du)
\]

as locally finite point processes on \((0,\infty)\times[0,1]\). Moreover, for every fixed \(b>0\), with probability tending to one all triangles present by time \(\lfloor b m^{2/3}\rfloor\) have a unique common key, and that key appears in exactly three sampled sets. Hence their full birth-count process satisfies

\[
\bigl(T_m(\lfloor tm^{2/3}\rfloor)\bigr)_{t\ge0}\ \Longrightarrow\ (N(t))_{t\ge0},\qquad
\mathbb EN(t)=\frac{4t^3}{3},
\]

in the Skorokhod \(J_1\) topology on bounded time intervals, where \(N\) is a nonhomogeneous Poisson process. At each bounded horizon the one-time laws have the quantitative bound

\[
\sup_{0\le t\le b}
 d_{\mathrm{TV}}\!\left(\mathcal L(T_m(\lfloor tm^{2/3}\rfloor)),
 \operatorname{Pois}(4t^3/3)\right)
 \le C_b m^{-1/3}
\]

for some finite \(C_b\) and all sufficiently large \(m\). If \(\tau_m=\min\{n:T_m(n)>0\}\), then \(\tau_m/m^{2/3}\) has limiting survival \(\exp(-4t^3/3)\), and the key producing its first triangle, divided by \(m\), tends to a uniform variable on \([0,1]\), independent of the limiting first-triangle time. A deterministic tie-breaking rule may be used when multiple triangles first appear together; such ties vanish asymptotically.

## Assumptions and scope

The two keys within any single sampled set are distinct; sets attached to different vertices are independent, and identical two-key sets at different vertices are allowed. The graph is the undirected *uniform random key graph* with exactly two keys per vertex. We let the key-pool size \(m\) grow and look at the sequential vertex scale \(m^{2/3}\), rather than the fixed-pool dense-graph limit. Triangles are counted as unordered triples of *vertices*, not as triples of keys; \(T_m(0)=0\). The process convergence concerns any fixed finite horizon, not growing horizons. Throughout the marked limit, \(u\) is the normalized numerical key label, not a position in the graph.

## Proof

**1. Exact classification and exceptional configurations.** Any three two-element sets that intersect pairwise either have a common key or are the three distinct edges of a triangle on three distinct keys. For the latter event, an ordered triple of sample sets has probability

\[
\frac{6\binom m3}{\binom m2^3}.
\]

Consequently, the probability that any such exceptional graph triangle occurs among the first \(n\) vertices is at most \(6\binom n3\binom m3/\binom m2^3\). For any single key, its appearance probability in any vertex is \(2/m\). A union bound therefore gives

\[
\Pr(\text{some key appears at least four times})
\le m\binom n4(2/m)^4=16\binom n4/m^3.
\]

If a graph triangle has two common keys, its three vertex sets must be identical; the probability that any three sampled sets coincide is at most \(\binom n3/\binom m2^2\). For \(n\le b m^{2/3}\), the three bounds are respectively \(O_b(m^{-1})\), \(O_b(m^{-1/3})\), and \(O_b(m^{-2})\). Off their union, graph triangles correspond bijectively to keys that have appeared three times, and each such triangle is born at the corresponding third appearance. This is an exact statement simultaneously for all sample prefixes up to \(n\).

**2. Coupling to independent key hits.** Take \(2n\) iid uniform labels from \(\{1,\ldots,m\}\), grouped into consecutive pairs. Conditioned on the entries of every pair being distinct, the unordered pairs have exactly the required law. The probability that any pair has equal entries is at most \(n/m=O_b(m^{-1/3})\), giving a coupling of the two models valid for all prefixes up to \(n\).

**3. Marked Poisson limit.** In continuous vertex-time, run a rate-two Poisson clock whose successive arrivals have independent uniform key labels. Splitting this process gives independent, rate-\(2/m\) Poisson processes for each key. Their third-arrival times \(H_{m,a}\) are independent \(\operatorname{Gamma}(3,2/m)\), and for \(t\ge0\)

\[
\Pr(H_{m,a}\le t m^{2/3})
=1-e^{-2t m^{-1/3}}\left(1+2t m^{-1/3}+2t^2m^{-2/3}\right)
=\frac{4t^3}{3m}+O_b(m^{-4/3})
\]

uniformly on \(0\le t\le b\). Independence and the rare-event product formula, with labels \(a/m\) forming an asymptotically uniform grid, give the marked Poisson limit \(4t^2\,dt\,du\). This follows, for example, by multiplying the Laplace functionals of the independent indicators of a third hit for compactly supported nonnegative test functions. For the original deterministic number of single-key draws, the time of the \(2n\)-th Poisson-clock arrival differs uniformly from vertex-time \(n\) by \(o_{\Pr}(m^{2/3})\) on each compact horizon, by the Poisson martingale maximal inequality (or the strong law). Thus the de-Poissonized marked event times have the same limit. Step 2 transfers this result to distinct-within-pair sampling. Step 1 then transfers it to triangle births. The limit has no time ties, justifying \(J_1\) convergence and the first-event and mark conclusions by the continuous mapping theorem.

**4. Total-variation error.** Let \(R_m(a)\) be the number of keys with at least three appearances among \(a=2n\) independent uniform single-key draws. Couple it to \(R_m(K)\), where \(K\sim\operatorname{Pois}(a)\) is independent of the iid labels. When the current sample size is \(r\), adding one draw creates a new third-or-later key with conditional unconditional probability at most \(\binom r2/m^2\): for each pair of preceding indices, the probability that the pair and the new draw all have the same label is \(m^{-2}\). Therefore, by the union bound and moment estimates for \(K\),

\[
\Pr(R_m(a)\ne R_m(K))
\le m^{-2}\mathbb E\bigl[|K-a|\binom{\max(K,a)}2\bigr]
=O_b(m^{-1/3})
\]

uniformly for \(0\le n\le bm^{2/3}\); the last estimate uses \(\mathbb E|K-a|^2=a\) and \(\mathbb E\max(K,a)^4=O((1+a)^4)\). Under Poissonization, \(R_m(K)\sim\operatorname{Bin}(m,q)\), with \(q=\Pr(\operatorname{Pois}(a/m)\ge3)\). Le Cam's bound is \(d_{\mathrm{TV}}(\operatorname{Bin}(m,q),\operatorname{Pois}(mq))\le mq^2=O_b(m^{-1})\), while

\[
\left|mq-\frac{4t^3}{3}\right|
\le \left|mq-\frac{4n^3}{3m^2}\right|
+\left|\frac{4n^3}{3m^2}-\frac{4t^3}{3}\right|
=O_b(m^{-1/3})
\]

for \(n=\lfloor tm^{2/3}\rfloor\). Poisson laws can be coupled within total variation at most the difference of their means. Combining these bounds with the \(n/m\) pair-coupling error and the three exceptional-configuration bounds from Step 1 establishes the displayed uniform \(O_b(m^{-1/3})\) theorem. The argument does not claim this rate is optimal.

## Verification

The accompanying Python 3 program `verify.py` enumerates every ordered triple of sampled two-key sets with pool sizes \(3\) through \(6\), verifying the exact common-key/three-key-cycle dichotomy; confirms the complete three-vertex triangle probability formula for pool sizes \(3\) through \(7\); and checks the exact correspondence of graph-triangle and third-key birth indices in every clean ordered four-vertex configuration with pool sizes \(3\) through \(5\). It also runs a seeded finite-size simulation as a diagnostic only. The analytic proof above, not the finite checks or the simulation, establishes every asymptotic assertion. Run with `python3 verify.py` using only the Python standard library.

## Relationship to prior work

Yağan and Makowski (arXiv:0910.0499v1, 2009) establish the zero-one threshold for existence of triangles in exactly the random-key-graph family, including the relative contribution of common-key triangles; this theorem **does not claim** that threshold or the basic triangle probability as new. It refines the critical window to a time-indexed, key-marked Poisson arrival law and supplies a deterministic-time, single-marginal total-variation error. Arratia, Garibaldi and Kilian (arXiv:1310.7055v1, 2013) study birthday occupancy collision limits; the third-occupancy limit is a key ingredient, not an independently new fact. Rybarczyk and Stark (arXiv:1609.01699v1, 2016) give Poisson subgraph-count results for binomial object inclusion, not the two-distinct-keys-per-vertex process. The new assertion is the combined marked graph-triangle process, its unique witness mechanism and the uniform finite-horizon quantitative estimate for this fixed-size uniform model.

## Limitations

The result assumes exactly two distinct uniformly chosen keys per vertex and a fixed time horizon after \(m^{2/3}\) rescaling. It does not address heterogeneous keys, larger key rings, nor horizons tending to infinity. Only one-time triangle-count total variation is bounded; a total-variation bound for the entire continuous-time path law is not claimed. Mathematical priority has not been established by exhaustive access to every related paper, and independent mathematical validation has not been performed.

## References

- Osman Yağan and Armand M. Makowski, *A zero-one law for the existence of triangles in random key graphs*, arXiv:0910.0499v1 (first public 2009-10-02), https://arxiv.org/abs/0910.0499 .
- Richard Arratia, Alexander Garibaldi and Alfred W. Kilian, *Asymptotic distribution for the birthday problem with multiple coincidences, via an embedding of the collision process*, arXiv:1310.7055v1 (2013-10-26), https://arxiv.org/abs/1310.7055 .
- Katarzyna Rybarczyk and Dudley Stark, *Poisson approximation of counts of subgraphs in random intersection graphs*, arXiv:1609.01699v1 (2016-09-06), https://arxiv.org/abs/1609.01699 .
- Liang Dong and Zhishui Hu, *The Number of Triangles in Random Intersection Graphs*, Communications in Mathematics and Statistics 11 (2023), DOI: 10.1007/s40304-021-00270-7; binomial-subset model and abstract-level comparison, not relied upon in the proof.
