# Exact finite-termination probabilities and optimal row orders for planar Kaczmarz regular frames

## Finding

Let \(n\ge2\) and let a consistent real planar linear system have the \(n\) unit row normals
\[
 a_j=(\cos(j\pi/n),\sin(j\pi/n)),\qquad j=0,\ldots,n-1.
\]
For each permutation \(\pi\) of these rows, apply one *unrelaxed* Kaczmarz projection onto each equation, in that order; let \(T_\pi\) be the resulting linear error propagator. Its exact operator norm is
\[
 \|T_\pi\|_2=\prod_{r=1}^{n-1}\left|\cos\left(\frac{\pi(\pi(r+1)-\pi(r))}{n}\right)\right|.
\]
Three sharp conclusions follow.

1. **Optimally ordered sweep.** If \(n\) is even, the optimal operator norm is zero, and exactly the permutations placing at least one orthogonal row pair consecutively attain it. If \(n\) is odd, the optimal norm is \(\sin(\pi/(2n))^{n-1}\), attained by exactly \(2n\) permutations: the two orientations and \(n\) starting positions of the cyclic order with modular step \((n-1)/2\).

2. **Exact random-reshuffling termination law.** If \(n=2m\) and the sweep permutation is uniform, let \(X\) count orthogonal matched pairs that occur consecutively in the permutation. The one-sweep propagator is the zero operator exactly when \(X\ge1\). For \(0\le k\le m\),
\[
 \Pr(X=k)=\sum_{j=k}^{m}(-1)^{j-k}\binom jk\binom mj\frac{2^j(n-j)!}{n!}.
\]
In particular the exact one-sweep termination probability is
\[
 p_n=1-\sum_{j=0}^{m}(-1)^j\binom mj\frac{2^j(n-j)!}{n!}.
\]
For odd \(n\), no permutation makes the one-sweep error operator zero.

3. **Sharp comparison with independent sampling.** If instead \(n\) row indices are drawn independently and uniformly (with replacement), the zero-operator probability for even \(n\) is exactly \(1-(1-1/n)^{n-1}\). Along even \(n\to\infty\),
\[
 p_n=1-e^{-1}+\frac{e^{-1}}{2n}+O(n^{-2}),\qquad
 \Pr_{\rm iid}(T=0)=1-e^{-1}-\frac{e^{-1}}{2n}+O(n^{-2}),
\]
so the reshuffling advantage is \(e^{-1}/n+O(n^{-2})\). The number \(X\) converges in distribution to \(\operatorname{Poisson}(1)\). In contrast, for every \(n\ge2\), uniform independent sampling gives exactly \(\mathbb E\|e_n\|_2^2=2^{-n}\|e_0\|_2^2\) for each deterministic initial error \(e_0\).

## Assumptions and scope

The system is consistent and has exactly the stated evenly spaced unoriented normal directions; repeated or additional rows, nonunit relaxation, noise, and inconsistent systems are excluded. All \(n\) row equations are enforced exactly once in a reshuffled epoch, while the independent-sampling comparison uses precisely \(n\) draws. Results concern the operator \(T\) (termination *for every initial error*), not accidental termination for a specially chosen initial vector. All probabilities are taken over the row order only, with deterministic row geometry. There is no computational-rounding model.

## Proof

Write \(v_j=(-\sin(j\pi/n),\cos(j\pi/n))\), the unit tangent to the \(j\)-th constraint. The error projection is \(P_j=I-a_ja_j^{\mathsf T}=v_jv_j^{\mathsf T}\). Therefore a product of projections telescopes as a rank-one outer product:
\[
 T_\pi=(v_{\pi(n)}v_{\pi(1)}^{\mathsf T})
 \prod_{r=1}^{n-1}(v_{\pi(r+1)}^{\mathsf T}v_{\pi(r)}).
\]
As each endpoint tangent is a unit vector, this proves the stated exact norm formula. It also proves that \(T_\pi=0\) if and only if at least one adjacent pair of normals is orthogonal.

For even \(n=2m\), orthogonality holds precisely when two row indices differ by \(m\) modulo \(n\). These \(m\) disjoint pairs form a perfect matching. Placing one such pair consecutively creates a zero factor and is necessary and sufficient. For odd \(n\), every absolute cosine factor is at least \(\sin(\pi/(2n))>0\), with equality precisely for modular differences \(\pm(n-1)/2\). The undirected graph of these equality edges is one cycle on \(n\) vertices because \(\gcd(n,(n-1)/2)=1\). Its Hamiltonian paths are exactly the \(2n\) ways of deleting one cycle edge and orienting the remaining path. Their consecutive factors all attain the lower bound, proving the optimal norm and optimizer classification. The special case \(n=3\) is included.

For the even case, let \(E_i\) be the event that matched pair \(i\) is consecutive in a uniformly random linear permutation. For any specified \(j\) matched pairs, compress those pairs to blocks. There are \(2^j(n-j)!\) permutations exhibiting all those adjacencies, out of \(n!\). Hence the binomial moments of the count \(X=\sum_i\mathbf1_{E_i}\) satisfy
\[
 \mathbb E\binom Xj=\binom mj\frac{2^j(n-j)!}{n!}.
\]
Binomial inversion gives the full distribution and inclusion–exclusion gives \(p_n\). For every fixed \(j\), \(\mathbb E[(X)_j]=2^j(m)_j/(n)_j\to1\); the factorial moments and tightness therefore give a Poisson-one limit.

For the refined asymptotics, write the binomial moment as
\[
 B_{n,j}=\frac1{j!}\prod_{s=0}^{j-1}\frac{n-2s}{n-s}
 =\frac1{j!}\left(1-\frac{j(j-1)}{2n}+O\left(\frac{j^4}{n^2}\right)\right)
\]
for \(j\le n^{1/3}\). The error is summable over \(j\), while the remaining factorial tails are \(O(n^{-2})\). Inserting into \(\Pr(X=0)=\sum_j(-1)^jB_{n,j}\), and using \(\sum_j(-1)^j/j!=e^{-1}\) and \(\sum_j(-1)^j j(j-1)/j!=e^{-1}\), proves \(\Pr(X=0)=e^{-1}-e^{-1}/(2n)+O(n^{-2})\).

For independent uniform sampling, conditional on every previously drawn index, the next index is its unique orthogonal partner with probability \(1/n\) when \(n\) is even. The adjacent-pair success indicators are independent Bernoulli variables by iterated conditioning. The probability of no consecutive orthogonal pair in \(n-1\) transitions is therefore \((1-1/n)^{n-1}\). Its logarithmic expansion yields the claimed asymptotics. Finally, for either parity, the regular-frame identity \(n^{-1}\sum_j a_ja_j^{\mathsf T}=I/2\) gives \(\mathbb E(\|P_J e\|_2^2\mid e)=\|e\|_2^2/2\). Iteration proves the exact independent-sampling mean-square formula.

## Verification

The standalone `verify.py` uses exact fractions for the matching-adjacency distribution and exhaustive row permutations for \(n=2,4,6,8\) and \(n=3,5,7\). It independently compares the zero-product condition and the odd-size minimizing-order count against enumerated projections. Run `python3 verify.py`; in this package it reports `PASS 87320 finite checks`. These finite checks are diagnostics, **not** an exhaustive proof for arbitrary \(n\); all-size and asymptotic assertions are proved above.

## Relationship to prior work

Oswald and Zhou (first public 2015) study **the identical even-order equispaced planar row family** in their equation (18), but analyze the slow convergence of its natural cyclic ordering and obtain general shuffled/preshuffled SOR error bounds rather than its exact random-permutation zero-operator probability, full matching-count law, or globally optimal row orders. The frame geometry itself and its natural cyclic rate are expressly prior art. Strohmer and Vershynin's 2007 randomized Kaczmarz work studies independently drawn equations and mean-square convergence, not the probability that a complete random permutation yields the exact zero error operator. Wallace and Sekmen (2014) describe projection-angle dependence and randomized row selection; their setting does not provide the matched-pair termination distribution. Diaconis, Evans and Graham (2013) analyze unseparated adjacent *consecutive labels* in random permutations and a Poisson limit; the present combinatorial count concerns a fixed disjoint matching of orthogonal pairs, and the significant linkage is to exact Kaczmarz termination. The geometry-based row-ordering motivation is also discussed by Dax (2022); this is prior art for ordering by orthogonality, not a claim of a new ordering heuristic. The finite matching-adjacency count itself is an inclusion–exclusion computation and should not be treated as a new general permutation-counting principle. Published research on regular-simplex Kaczmarz reshuffling and optimal planar independent sampling addresses different frames/objectives, so those results do not directly imply this exact one-sweep law.

## Limitations

The classification relies on exact planar orthogonality and therefore is sensitive to perturbed row angles and finite-precision arithmetic. It gives one-sweep zero-operator probabilities, not exact convergence times over repeated random epochs, high-dimensional performance, or a universal superiority theorem for random reshuffling. Directly related results in unindexed literature, and applications of general matching-adjacency enumeration, remain originality risks; independently auditing the proof and literature is necessary before publication.

## References

- P. Oswald and W. Zhou, *Random Reordering in SOR-Type Methods*, first public preprint 2015-10-15, arXiv:1510.04727v1, identical even-row planar frame in equation (18), https://arxiv.org/abs/1510.04727.
- T. Strohmer and R. Vershynin, *A randomized Kaczmarz algorithm with exponential convergence*, first public preprint 2007-02-08, https://arxiv.org/abs/math/0702226.
- T. Wallace and A. Sekmen, *Kaczmarz Iterative Projection and Nonuniform Sampling with Complexity Estimates*, 2014, https://pmc.ncbi.nlm.nih.gov/articles/PMC4809392/.
- P. Diaconis, S. N. Evans and R. Graham, *Unseparated pairs and fixed points in random permutations*, Berkeley technical report 822, 2013-08-01, https://live-statistics.pantheon.berkeley.edu/sites/default/files/tech-reports/unseparated_pairs.pdf.
- A. Dax, *Kaczmarz Anomaly in Tomography Problems*, 2022, https://doi.org/10.3390/appliedmath2020012.
