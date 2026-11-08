# Exact signed-cycle rank law for two-block SparseStack sketches

## Finding

Consider a fully independent real two-block SparseStack matrix \(S\in\mathbb R^{2q\times N}\), with \(q\ge1\), \(N\ge k\), and the fixed coherent orthonormal frame \(U=[e_1,\ldots,e_k]\in\mathbb R^{N\times k}\). Each column of \(S\) independently puts one signed entry \(\pm1/\sqrt2\) in each of the two disjoint blocks of \(q\) rows. Every bucket and sign is uniform and all choices are independent. Write \(B=SU\).

**Finite-size identity.** Form a bipartite multigraph \(G\) on two labeled groups of \(q\) vertices, inserting one edge for each column of \(B\) between the chosen block-one and block-two buckets. Let \(u(G)\) be its number of unicyclic connected components, and let \(\mathcal P\) be the event that all components are trees or unicyclic (a *pseudoforest*). Then, for every pair of positive integers \(q,k\),
\[
\Pr\{\operatorname{rank}(B)=k\}=\mathbb E\left[{\bf1}_{\mathcal P}\,2^{-u(G)}\right].\tag{1}
\]
This includes parallel edges (cycles of length two). In particular, when \(k=2\), the probability is exactly \(1-1/(2q^2)\).

**Sharp proportional-dimension law.** For any integer sequence \(k=k(q)\) satisfying \(k/q\to c\in[0,\infty)\),
\[
\lim_{q\to\infty}\Pr\{\operatorname{rank}(B)=k\}
=\begin{cases}(1-c^2)^{1/4},&0\le c<1,\\0,&c\ge1.\end{cases}\tag{2}
\]
For \(0<c<1\), rank deficiency therefore has a nonvanishing limiting probability, even though the sketch has \(2q/k\to2/c>2\) output rows per input dimension. A limiting full-rank success probability of at least \(0.95\) requires \(c\le\sqrt{1-0.95^4}=0.4306898536\ldots\), corresponding to at least \(2/c=4.6437128324\ldots\) sketch rows per subspace dimension. This last requirement is necessary, not sufficient, for a positive lower singular-value guarantee.

## Assumptions and scope

All matrix entries are treated in exact real arithmetic. The two hashes of a column are independently uniform on \(\{1,\ldots,q\}\), and the two signs are independent fair Rademacher variables. The coordinate frame is fixed before drawing the sketch, so no adaptive selection or non-coordinate-subspace claim is made. Transposing the usual wide SparseStack convention does not change the singular values. The asymptotic holds for \(k/q\to c\) without assuming \(k\le2q\); if \(k>2q\), column rank is automatically deficient.

A connected component with \(v\) vertices and \(e\) edges is a tree if \(e=v-1\), unicyclic if \(e=v\), and multicyclic if \(e>v\). Isolated vertices are trees with no edges. Parallel edges are allowed, and two parallel edges form a length-two cycle. A cycle is *balanced* when the product of its edge switching signs is \(+1\); because all cycles are even, this is equivalently the condition that the edge constraints admit a nonzero potential on their component.

## Proof

**1. Deterministic signed-incidence reduction.** Multiplying columns by independent signs and by \(\sqrt2\) preserves rank. Each resulting column has a \(+1\) at a vertex in the upper block and a fair sign \(\tau\in\{-1,+1\}\) at a vertex in the lower block. View it as a signed incidence edge. In any connected component of \(G\), a row-vector \(y\) annihilates all edge columns exactly when \(y_b=-\tau_{ab}y_a\) on each edge. Values on a spanning tree are fixed by any root value. If every cycle satisfies the consistency product, the left nullspace of the component's \(v\)-row incidence matrix has dimension one, giving rank \(v-1\). Otherwise it has dimension zero, giving rank \(v\). Thus columns are independent on a tree, independent on a unicyclic component precisely when its unique cycle is unbalanced, and dependent on every multicyclic component. Conditional on \(G\), different unicyclic components have disjoint edge-sign sets, and each is unbalanced with probability \(1/2\). This proves (1), including multiedges and isolated vertices. For \(k=2\), dependence occurs exactly when both endpoint hashes match (probability \(q^{-2}\)) *and* the two relative signs agree (probability \(1/2\)).

**2. Short-cycle counting.** Let \(C_{\ell,q}\) count elementary cycles of length \(2\ell\) in this labeled-edge multigraph; \(\ell=1\) means a pair of parallel edges. For \(\ell\ge2\), the number of distinct index-labeled cycles has expectation
\[
\mathbb E C_{\ell,q}=\frac{(q)_{\ell}^2\,(k)_{2\ell}}{2\ell\,q^{4\ell}}\longrightarrow\frac{c^{2\ell}}{2\ell},\tag{3}
\]
where \((a)_j=a(a-1)\cdots(a-j+1)\). For parallel pairs, \(\mathbb E C_{1,q}=\binom{k}{2}/q^2\to c^2/2\). For any fixed finite set of lengths, the joint factorial moments converge to those of independent Poisson variables with means \(c^{2\ell}/(2\ell)\): collections of vertex-disjoint cycles contribute the product of means, while overlapping distinct cycles have at least one more edge than vertices and contribute \(O(q^{-1})\) in the fixed-size enumeration. The sign-product of each disjoint cycle is independently fair.

**3. Subcritical completion.** Suppose \(c<1\) and choose \(c<c'<1\). Eventually \(k/q<c'\). The expected number of cycles longer than \(2L\) is bounded, uniformly in sufficiently large \(q\), by \(\sum_{\ell>L}(c')^{2\ell}/(2\ell)\): for each \(\ell\), the expectation in (3) is bounded by \((k/q)^{2\ell}/(2\ell)\), and the same bound holds for parallel pairs. This tail tends to zero as \(L\to\infty\). Moreover, a subcritical bipartite random multigraph with \(k\le c'q\) sampled edges has no component containing two cycles with probability \(1-o(1)\). One elementary proof explores each connected component: the two-type binomial exploration is dominated, after a fixed small slack, by a subcritical branching process with an exponential component-size tail; on the event that all explored components have at most \(A\log q\) vertices, the chance that any exploration has two surplus edges is \(O((\log q)^4/q)\). Choosing \(A\) sufficiently large makes the exceptional component-size event \(o(1)\). Thus the graph is a pseudoforest with probability \(1-o(1)\).

Consequently the total number \(U_q\) of unicyclic components converges in law to a Poisson random variable of mean
\[
\mu(c)=\sum_{\ell\ge1}\frac{c^{2\ell}}{2\ell}=-\frac12\log(1-c^2).
\]
By (1), bounded convergence for the law of integer-valued counts gives
\[
\lim\Pr\{\operatorname{rank}(B)=k\}=\mathbb E[2^{-U}]
=\exp(-\mu(c)/2)=(1-c^2)^{1/4}.
\]
The \(c=0\) case follows from the same cycle-tail bound, since the chance of any cycle tends to zero.

**4. Critical and supercritical completion.** For every fixed \(L\), the balanced cycles among lengths \(2,4,\ldots,2L\) converge jointly to independent Poisson counts whose total mean is \(\tfrac12\sum_{\ell=1}^L c^{2\ell}/(2\ell)\); overlaps have probability \(o(1)\). Any balanced cycle creates a nontrivial column dependence, even when other cycles are present. Hence
\[
\limsup_{q\to\infty}\Pr\{\operatorname{rank}(B)=k\}\le
\exp\left(-\sum_{\ell=1}^L\frac{c^{2\ell}}{4\ell}\right).
\]
For \(c\ge1\), the series diverges as \(L\to\infty\), forcing the limit to zero. This completes (2).

## Verification

The accompanying standalone `check.py` uses only the Python standard library. It computes small exact-rational matrix ranks independently of a parity-union-find graph test, exhaustively enumerating all sampled relative signs and endpoint hashes for eight small parameter pairs. The enumerated numbers of full-rank outcomes versus total outcomes are: \((q,k)=(1,1):2/2\); \((1,2):2/4\); \((1,3):0/8\); \((2,1):8/8\); \((2,2):56/64\); \((2,3):336/512\); \((3,2):306/324\); \((3,3):4896/5832\). Five seeded simulation settings, up to \(q=300\), also compare success rates against the asymptotic expression. To replay: run `python3 check.py` from the directory containing this document and its checker; successful output ends with `VERIFY_OK`.

These finite computations test the model and the deterministic rank identity; they do not establish Poisson convergence or the infinite asymptotic, which are proved above.

## Relationship to prior work

Jeendgar, Flint and Anzt (2026) study GPU implementations of CountSketch and SparseStack for coherent inputs, including quantization effects, without a sharp rank-loss phase law. Camaño, Epperly, Meyer and Tropp (2025), Definition 1.7 and Section 3, define SparseStack and analyze subspace injection at logarithmic stack count. Huang, Rudelson and Tikhomirov (2026), Theorem 1.3 and Section 6, prove a stronger type of failure for *constant positive singular-value bounds* with constant sparsity; this does **not** state or imply an exact *full-rank* probability, since an injective sketch may still have a vanishing least singular value. Heidary (2026) supplies OSE guarantees at growing stack count, rather than the two-block rank distribution.

The signed-incidence rank criterion is classical (see Zaslavsky), as is Poisson convergence of short cycles in sparse random graphs. Daudé and Ravelomanana (2009/2011) and de Panafieu et al. (2015/2016) study closely related random 2-XOR satisfiability problems, whose cycle-sign obstructions use the opposite sign-consistency event. Their **non-bipartite** random-formula laws and multigraph enumeration do not themselves state the two-block bipartite SparseStack full-rank law. Equation (2) is therefore a new application and an exact specialization-specific classification, not a claim to invent the component-rank lemma or Poisson method. Undetected earlier bipartite 2-XOR / signed-graph enumeration remains a priority risk.

## Limitations

The statement concerns exactly two fully independent CountSketch blocks, a fixed coordinate subspace and exact arithmetic. It neither bounds the positive smallest singular value nor gives the distortion distribution, nor covers general incoherent subspaces, GPU FP16 behavior, block correlation, or more than two stacks. No finite Monte Carlo run validates an infinite theorem. No independent audit has been performed.

## References

- Jeendgar, A., Flint, C., and Anzt, H., *Randomized Sketching is Robust to Low-Precision Rounding on GPUs*, arXiv:2606.20195v1, first posted 2026-06-18, https://arxiv.org/abs/2606.20195.
- Camaño, C., Epperly, E. N., Meyer, R. A., and Tropp, J. A., *Faster Linear Algebra Algorithms with Structured Random Matrices*, arXiv:2508.21189v1, first posted 2025-08-28, https://arxiv.org/html/2508.21189.
- Huang, H., Rudelson, M., and Tikhomirov, K., *Well-invertible column subsets of sparse matrices are rare*, arXiv:2607.05384v1, first posted 2026-07-06, https://arxiv.org/abs/2607.05384.
- Heidary, D., *SparseStack Is an Optimal Oblivious Subspace Embedding*, arXiv:2609.02978v1, first posted 2026-09-02, https://arxiv.org/abs/2609.02978.
- Daudé, H., and Ravelomanana, V., *Random 2 XORSAT Phase Transition*, Algorithmica 59, 48–65 (2011), https://doi.org/10.1007/s00453-009-9308-1.
- de Panafieu, É., Gardy, D., Gittenberger, B., and Kuba, M., *2-Xor revisited: satisfiability and probabilities of functions*, arXiv:1511.07813, https://arxiv.org/abs/1511.07813.
- Zaslavsky, T., *Signed graphs*, Discrete Applied Mathematics 4 (1982), 47–74, https://doi.org/10.1016/0166-218X(82)90033-5.
