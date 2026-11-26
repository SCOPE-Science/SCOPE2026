# Parity-rigid Walsh recovery from connected vertex sets of complete multipartite graphs

## Finding

Let \(t\ge 2\), let \(n_1,\ldots,n_t\) be positive integers, and let \(G=K_{n_1,\ldots,n_t}\) be the labelled simple complete multipartite graph on \(N=\sum_i n_i\) vertices. Let \(\mathcal C(G)\) consist of all **nonempty vertex sets** inducing a connected subgraph of \(G\). On the binary group \(B=\mathbb F_2^N\), let \(Tg=f*g\), where \(f\) is the incidence indicator of \(\mathcal C(G)\) and convolution is unnormalized.

For any frequency \(\xi\in B\), denote its Hamming weight by \(w=|\xi|\), and let \(J(\xi)=\{i:\xi\text{ vanishes identically on the }i\text{-th part}\}\). Every Walsh multiplier, with multiplicities determined by these frequency data, is

\[
\lambda(\xi)=2^N\mathbf1_{\{\xi=0\}}+N+t-1-2w-\sum_{i\in J(\xi)}2^{n_i}.
\]

The exact convolution-invertibility criterion is

\[
T\text{ is invertible}\quad\Longleftrightarrow\quad N-t\text{ is even}.
\]

Write \(d=|\mathcal C(G)|=2^N+N+t-1-\sum_i2^{n_i}\). The maximum singular value is exactly \(d\). The least **strictly positive** singular value is \(1\) when \(N-t\) is even and \(2\) when \(N-t\) is odd. Consequently the sharp positive-subspace condition number is \(d\) or \(d/2\), respectively.

There is also an exact nullity formula. For each proper subset \(J\subsetneq[t]\), put \(s_J=(N+t-1-\sum_{i\in J}2^{n_i})/2\), and interpret a coefficient with noninteger or negative exponent as zero. Then

\[
Z=\operatorname{nullity}(T)=\sum_{J\subsetneq[t]}[z^{s_J}]\prod_{i\notin J}\bigl((1+z)^{n_i}-1\bigr),
\qquad\operatorname{rank}(T)=2^N-Z.
\]

Here the product chooses nonzero frequency blocks; the term indexed by \(J\) counts exactly the zero multipliers with zero blocks precisely \(J\). For fixed \(t\), along any sequence with \(N-t\) odd and all part sizes \(n_i=N/t+O(1)\),

\[
Z/2^N\sim\sqrt{\frac{2}{\pi N}}.
\]

Thus a parity change can switch the operator from full invertibility to a quantitatively specified, asymptotically vanishing but exponentially large nullspace.

## Assumptions and scope

Parts are labelled, nonempty and pairwise disjoint; \(t\ge2\). Connectivity is that of the vertex-induced graph, with singletons counted as connected and the empty vertex set excluded. Addition in \(B\) is coordinatewise mod two. The Walsh character is \(\chi_\xi(x)=(-1)^{\sum_j\xi_jx_j}\). The full group has \(2^N\) coordinates. The Fourier transform and convolution are both unnormalized; no normalized probability measure is used in the multiplier formula.

## Proof

**Step 1: Exact connected-set indicator.** A nonempty set is connected precisely when it meets at least two of the multipartite parts, or is a singleton. Equivalently, from the family of all \(2^N\) vertex subsets remove the empty set and, for each part, all subsets of that part of cardinality at least two. These removed families are disjoint. Thus \(d=2^N-1-\sum_i(2^{n_i}-1-n_i)\), equal to the expression above.

**Step 2: Every multiplier.** For a frequency \(\xi\), Walsh character orthogonality gives \(\sum_{x\in B}\chi_\xi(x)=2^N\mathbf1_{\{\xi=0\}}\). For the subsets of a single part \(i\), the same sum is \(2^{n_i}\mathbf1_{\{i\in J(\xi)\}}\). The empty subset contributes \(1\), while the singletons in part \(i\) contribute \(n_i-2w_i\), where \(w_i\) is the frequency's weight in that part. Subtracting precisely the forbidden subsets gives

\[
\sum_{x\in\mathcal C(G)}\chi_\xi(x)=2^N\mathbf1_{\{\xi=0\}}-1-\sum_i\bigl(2^{n_i}\mathbf1_{\{i\in J(\xi)\}}-1-n_i+2w_i\bigr),
\]

which simplifies to the claimed multiplier. Characters form an orthogonal eigenbasis of \(T\), so multiplier zeros count its nullity and their absolute values are its singular values.

**Step 3: Complete parity classification.** For any nonzero frequency, \(\lambda(\xi)=N+t-1-2w-\sum_{i\in J(\xi)}2^{n_i}\). The subtracted powers and \(2w\) are all even. If \(N-t\) is even, then \(N+t-1\) is odd, so no multiplier can vanish; \(\lambda(0)=d>0\) as there are at least \(N\) singleton sets. If \(N-t\) is odd, then \(N\ge t+1\). Choose a frequency that is nonzero in every part and has total weight \(w=(N+t-1)/2\). Such a frequency exists: one first selects one coordinate per part, then allocates the remaining \(w-t\) bits among the available \(N-t\) coordinates; the required number is between \(0\) and \(N-t\). Its multiplier is zero.

**Step 4: Exact gap and conditioning.** In the even case every multiplier is odd, so each nonzero modulus is at least \(1\). A frequency nonzero on every part with weight \((N+t)/2\) is feasible and has multiplier \(-1\). In the odd case every nonzero-frequency multiplier is even, as is the trivial multiplier \(d\); hence every nonzero modulus is at least \(2\). A frequency nonzero on every part with weight \((N+t+1)/2\) is feasible since \(N\ge t+1\), and has multiplier \(-2\). The character triangle inequality gives \(|\lambda(\xi)|\le d\), with equality at frequency zero. These facts prove both sharp singular-value assertions.

**Step 5: Exact zero counts and asymptotics.** At a nonzero frequency, fixing its zero-part set \(J\) forces each remaining part to have positive weight; the generating polynomial \(\prod_{i\notin J}((1+z)^{n_i}-1)\) counts such frequencies by their total weight. The coefficient condition for the multiplier to vanish is exactly \(w=s_J\). The all-zero frequency cannot vanish because \(d>0\), so summing over proper \(J\) proves the nullity formula. For \(N-t\) odd let \(s=(N+t-1)/2=N/2+O_t(1)\). The zeros with no zero part comprise all \(\binom Ns\) weight-\(s\) frequencies except those with at least one zero part; every zero with some zero part is likewise among the frequencies missing some part. A union bound therefore yields the explicit estimate

\[
\bigl|Z-\binom Ns\bigr|\le 2\sum_{i=1}^t2^{N-n_i}.
\]

If \(t\) is fixed and each \(n_i=N/t+O(1)\), the relative error after dividing by \(2^N\) is exponentially small; Stirling's central-binomial estimate gives \(\binom Ns/2^N\sim\sqrt{2/(\pi N)}\).

## Verification

The standalone `verify.py` constructs the incidence indicator independently by direct graph-connectivity classification, computes every Walsh multiplier using an in-place integer Walsh–Hadamard transform, and compares each to the closed formula. It also computes nullity independently using the coefficient-extraction formula and checks the invertibility criterion and smallest positive singular value. Running `python3 verify.py` checks 269 labelled part-size tuples with two to four parts, each part of size one to four, and total size at most 11. The exhaustive finite checks are corroboration only; Steps 1–5 are the proof for all permissible integers.

Examples: \(K_{2,2}\) has rank \(16\), \(K_{2,3}\) has rank \(20\) and nullity \(12\), \(K_{2,2,2}\) has rank \(40\) and nullity \(24\), and \(K_{2,2,3}\) has rank \(128\).

## Relationship to prior work

The subgraph component polynomial of Tittmann, Averbouch and Makowsky (arXiv:0812.4147, first public 2008-12-22), especially its connected-subset specialization and Theorem 18 on joins, motivates the natural connectivity family. Liao and Hou (arXiv:1311.6856, 2013-11-27) study the same graph-polynomial framework and characterize complete bipartite graphs by the unweighted invariant. Elbassioni (arXiv:1411.2262, 2014-11-09) develops general connected-induced-subgraph enumeration. Trevisan's 2016 lecture gives general finite Abelian Cayley diagonalization. These prior results provide the graph-family and character-spectral context, but the inspected treatments do not state the all-part-size Walsh multiplier, exact zero classification, sharp nonzero spectral gap, or parity-dependent rank transition here. In particular, scalar connected-set counts do not specify the full vertexwise signed character sums.

## Limitations

The result applies only to vertex-induced connectivity supports in complete multipartite graphs, not arbitrary graphs, edge-induced connectivity supports, or other coefficient fields. The exact integer coefficient formula may require evaluation for each part-size profile. No claim is made about numerical stability for a different normalization or nonlinear inverse problems. The source comparison is bounded and cannot rule out unindexed equivalent results. There has been no independent audit.

## References

- P. Tittmann, I. Averbouch and J. A. Makowsky, *The Enumeration of Vertex Induced Subgraphs with respect to the Number of Components*, first arXiv version 2008-12-22, https://arxiv.org/abs/0812.4147.
- Y. Liao and Y. Hou, *Note on the subgraph component polynomial*, first arXiv version 2013-11-27, https://arxiv.org/abs/1311.6856.
- K. Elbassioni, *A Polynomial Delay Algorithm for Generating Connected Induced Subgraphs of a Given Cardinality*, first arXiv version 2014-11-09, https://arxiv.org/abs/1411.2262.
- L. Trevisan, *CS294 Lecture 15: Abelian Cayley graphs*, 2016-03-16, https://lucatrevisan.wordpress.com/2016/03/16/cs294-lecture-15-abelian-cayley-graphs/.
