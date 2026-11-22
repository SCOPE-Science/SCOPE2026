# Three finite-horizon optimal leader types on complete bipartite networks

## Finding

For each integer \(q\ge9\), consider the unweighted complete bipartite graph \(K_{2,q}\), and select exactly two *perfectly grounded* leaders. Let \(F\) be the other \(q\) vertices and \(L_{FF}\) the principal submatrix of the original unnormalized graph Laplacian, retaining the edges from followers to leaders in its diagonal. At every time \(t>0\), minimize the grounded heat trace
\[
H_t(S)=\operatorname{tr}(e^{-tL_{FF}(S)}).
\]
Let \(a=|S\cap P|\in\{0,1,2\}\), where \(P\) denotes the two-vertex part. The **unique optimal leader type** (up to relabeling within each part) is
\[
\boxed{\begin{array}{c|ccc}
 t&1/5&67/100&1\\\hline
 \operatorname{argmin}_{a\in\{0,1,2\}} H_t(a)&0&1&2
\end{array}.}
\]
All inequalities are strict; consequently, each of these three types is uniquely optimal on a nonempty open interval of observation times surrounding the indicated value. The exact numbers of minimizing two-element leader sets at these three times are respectively \(\binom q2\), \(2q\), and \(1\).

More strongly, at every **fixed positive time away from two transition values**, the optimal type for all sufficiently large \(q\) is determined exactly by
\[
\boxed{\begin{cases}
 a=0,&0<t<\log\varphi,\\
 a=1,&\log\varphi<t<\log2,\\
 a=2,&t>\log2,
\end{cases}}
\qquad \varphi=(1+\sqrt5)/2.
\]
There is no assertion here about the finite-\(q\) optimizer at every possible time, or about exact ties at the two limiting transition times.

## Assumptions and scope

Edges are undirected with unit conductance; pinned leaders remain fixed at zero, and each unpinned state evolves by \(\dot x=-L_{FF}x\). The heat trace equals the expected squared norm of the follower state at time \(t/2\) when its initial covariance is the identity: \(\mathbb E\|e^{-(t/2)L_{FF}}x(0)\|_2^2=H_t(S)\). Thus the finite-time objective measures total mean-square deterministic diffusion remaining from isotropic initial disturbances, not stationary variance under ongoing white noise. Exactly two distinct leaders are allowed, \(q\ge9\), and \(t>0\).

## Proof

**Exact orbit spectra.** All pairs with the same \(a\) are equivalent by automorphisms of \(K_{2,q}\). For \(a=0\) both leaders are in the size-\(q\) part, leaving two vertices in the size-two part and \(q-2\) in the other. The full grounded Laplacian has eigenvalue \(2\) with multiplicity \(q-3\), eigenvalue \(q\) once, and two remaining eigenvalues \(\delta_q,q+2-\delta_q\), where
\[
\delta_q=\frac{q+2-\sqrt{(q+2)^2-16}}2,
\quad \delta_q(q+2-\delta_q)=4.
\]
Indeed, on constant vectors in each part its final two-by-two block is \(\left(\begin{smallmatrix}q&-\sqrt{2(q-2)}\\-\sqrt{2(q-2)}&2\end{smallmatrix}\right)\), with determinant four. The zero-sum subspaces give the other eigenvalues.

For \(a=1\), one small-part and one large-part leader remain pinned. The spectrum is \(2\) with multiplicity \(q-2\) together with \(1,q+1\). For \(a=2\), both size-two-part vertices are leaders, leaving the grounded matrix \(2I_q\). Therefore, writing \(H_a(t)\) for the heat trace of type \(a\),
\[
\begin{aligned}
H_0(t)&=(q-3)e^{-2t}+e^{-qt}+e^{-\delta_q t}+e^{-(q+2-\delta_q)t},\\
H_1(t)&=(q-2)e^{-2t}+e^{-t}+e^{-(q+1)t},\\
H_2(t)&=q e^{-2t}.
\end{aligned}
\]
In particular,
\[
\begin{aligned}
H_0-H_1&=e^{-\delta_qt}-e^{-t}-e^{-2t}+e^{-qt}(1-e^{-t})+e^{-(q+2-\delta_q)t},\\
H_0-H_2&=e^{-\delta_qt}+e^{-qt}+e^{-(q+2-\delta_q)t}-3e^{-2t},\\
H_1-H_2&=e^{-2t}(e^t+e^{-(q-1)t}-2).
\end{aligned}
\]
All expressions hold for every integer \(q\ge9\) and time \(t>0\).

**Uniform finite-\(q\) inequalities.** Since \(q\ge9\), the root \(\delta_q\) is positive and decreases as \(q\) increases, and \(\delta_q\le\delta_9<19/50<1\). The latter is exact: the quadratic \(z^2-11z+4\) is negative at \(z=19/50\), and its smaller root is \(\delta_9\). Thus \(q+2-\delta_q>q\). At \(t=1/5\), the displayed differences satisfy
\[
\begin{aligned}
H_0-H_1&<1-e^{-1/5}-e^{-2/5}+2e^{-9/5}<1-81/100-66/100+34/100<0,\\
H_0-H_2&<1-3e^{-2/5}+2e^{-9/5}<1-198/100+34/100<0.
\end{aligned}
\]
The elementary rational estimates \(e^{-1/5}>81/100\), \(e^{-2/5}>66/100\), and \(e^{-9/5}<17/100\) follow from the alternating Taylor bounds for the first two expressions and the positive Taylor lower bound \(e^{9/5}>100/17\) for the last; all are checked in `verify.py` using exact rational arithmetic. Thus type zero is strictly best.

At \(t=67/100\), positivity of the last two terms in \(H_0-H_1\) gives
\[
H_0-H_1>e^{-1273/5000}-e^{-67/100}-e^{-67/50}>0.
\]
The last strict comparison follows from rational alternating exponential bounds: the fifth-order lower partial sum for the first exponential exceeds the sum of the sixth- and tenth-order upper partial sums for the other two, by more than \(1/1000\). Moreover, \(e^{67/100}<49/25\) and \(e^{-8(67/100)}<e^{-4}<1/25\), so \(H_1-H_2<e^{-2t}(49/25+1/25-2)=0\). The first exponential upper bound follows from a degree-seven Taylor sum and a geometric tail; the last follows from \(e^4>25\). The packaged rational checker verifies all inequalities with their stated exact bounds. Thus type one is strictly best.

At \(t=1\), using \(e^{-z}>1-z\) for \(z>0\) and \(e^2>7\),
\[
H_0-H_2>e^{-\delta_q}-3e^{-2}>1-19/50-3/7>0.
\]
Also \(H_1-H_2=e^{-2}(e+e^{-(q-1)}-2)>0\) because \(e>2\). Hence type two is strictly best. Continuous dependence on \(t\) yields the stated open-time intervals and strict orbit multiplicities.

**Large-size phase law.** As \(q\to\infty\), \(\delta_q\to0\), and for fixed \(t>0\) the exponentially decaying terms with rates \(q\), \(q+1\), and \(q+2-\delta_q\) vanish. Consequently
\[
\begin{aligned}
H_0-H_1&\longrightarrow 1-e^{-t}-e^{-2t},\\
H_1-H_2&\longrightarrow e^{-t}-2e^{-2t},\\
H_0-H_2&\longrightarrow1-3e^{-2t}.
\end{aligned}
\]
The first limit changes sign at \(t=\log\varphi\), the second at \(t=\log2\), and the third at \(t=(\log3)/2\); these times satisfy \(\log\varphi<(\log3)/2<\log2\). Therefore the three asserted winning types follow by strict pairwise inequalities in each open interval. For each fixed time outside the two optimizing boundaries, the convergence of the three differences preserves these strict signs for sufficiently large \(q\). The extra pairwise crossing at \((\log3)/2\) never changes the minimizing type in this limit.

## Verification

Run `python3 verify.py` beside this document; the script uses only the standard library. It certifies the exact rational exponential inequalities and the positive-root bound, then checks 480 exact integer matrix spectral moments against the stated orbit spectra for \(9\le q\le40\) and moment orders one through five, 96 strict three-time optimizer comparisons, and six large-size phase samples. On the packaged file it prints `VERIFY_OK 582 exact_and_numerical_crosschecks` together with the positive rational lower bound. Finite checks independently corroborate the spectral formulas; the all-\(q\) claims follow from the analytic inequalities, not finite sampling.

## Relationship to prior work

Lin, Fardad, and Jovanović (2013) formulated perfect/noise-free leader selection with the *stationary* inverse-grounded-Laplacian trace; Fitch and Leonard (2014) developed joint-centrality rankings for noisy stationary leader selection. The publicly accessible complete manuscript *Exact leader allocation and a square-root law on complete bipartite networks* gives the arbitrary-budget inverse-trace allocation on this same graph family, but not the time-dependent heat-trace ranking. The complete same-graph four-leader finite-gain phase diagram treats stationary inverse trace with four imperfect leaders, not two perfect leaders and transient heat decay. Simpson and Chung use heat kernel PageRank to approximate consensus in leader-following networks, but they optimize neither the leader locations nor the grounded finite-time heat trace. These stationary objectives are time integrals of spectral heat traces or variants, and their optimizer statements alone do not imply any of the strict pointwise comparisons shown here. The new assertion is the three disjoint finite-time optimal orbit classes on the infinite two-leader family and their limiting time-phase boundaries; basic symmetry, spectral decomposition, and prior stationary objectives are not claimed as new.

## Limitations

The theorem applies to the unit-edge \(K_{2,q}\) family for integers \(q\ge9\), two perfect leaders, and the unnormalized heat trace at positive times. It proves optimality at three specified times and for each time strictly inside the limiting phase intervals when the large-part size is sufficiently large. It does **not** assert a complete finite-\(q\) phase diagram for all times, that \(q=9\) is the first possible size for three regimes, or the behavior exactly at limiting boundaries. The result is a same-study mathematical proof and reproducibility check; no independent audit or claim of exhaustive research priority is made. An as-yet-unindexed equivalent heat-trace selection theorem remains possible.

## References

- F. Lin, M. Fardad and M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450, first posted 2013-02-03. https://arxiv.org/abs/1302.0450
- K. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, first posted 2014-07-07. https://arxiv.org/abs/1407.1569
- *Exact leader allocation and a square-root law on complete bipartite networks*, publicly accessible manuscript (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-leader-allocation-and-a-square-root-law-on-complete-bipart--3151e2186be2
- *Complete four-leader phase diagram on unequal complete bipartite networks*, publicly accessible manuscript (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-complete-four-leader-phase-diagram-on-unequal-complete-bipartite--5b299daa2230
- O. Simpson and F. Chung, *Finding Consensus in Multi-Agent Networks Using Heat Kernel PageRank*, full freely accessible manuscript, https://cseweb.ucsd.edu/~osimpson/consensus.pdf
