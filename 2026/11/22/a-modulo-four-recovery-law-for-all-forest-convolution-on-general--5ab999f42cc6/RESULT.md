# A modulo-four recovery law for all-forest convolution on generalized theta graphs

## Finding

For an arbitrary generalized theta graph with at least three internally disjoint terminal-to-terminal paths, each of length at least two, unnormalized convolution by the indicator of **all acyclic edge subsets** has an exact arithmetic Fourier spectrum. If the number of paths is \(k\), convolution is invertible for every choice of path lengths whenever \(k\not\equiv1\pmod4\). This is sharp as a universal statement: for every \(k=4t+1\ge5\), the graph with all path lengths two has nonzero nullity. An exact arithmetic zero test and nullity formula are given below for every individual choice of lengths.

A particularly sharp boundary occurs for five paths. If \(h\) is the number of length-two paths among the five, the operator is singular precisely when \(h\ge3\), and its nullity is
\[
\sum_{\substack{Z\subseteq\{i:\ell_i=2\}\\|Z|=3}}\ \prod_{i\notin Z}(2^{\ell_i}-1).
\]
Thus extending one length-two path can restore full invertibility; the conclusion concerns forests of *any* cardinality, not only spanning trees.

## Assumptions and scope

Fix \(k\ge3\) and integers \(\ell_1,\ldots,\ell_k\ge2\). The simple undirected generalized theta graph \(G\) has two distinguished vertices connected by \(k\) internally vertex-disjoint paths \(P_i\), with \(|E(P_i)|=\ell_i\). Let \(E\) be its edge set, \(N=\sum_i\ell_i\), and \(H=(\mathbb Z/2\mathbb Z)^E\). Every \(x\in H\) represents an edge subset; define \(f(x)=1\) exactly when that subset is acyclic (isolated vertices are permitted). Define unnormalized convolution on complex functions on \(H\) by
\[
(T_fg)(x)=\sum_{y\in H}f(y)g(x-y).
\]
For \(\xi\in H\), the Walsh character is \(\chi_\xi(x)=(-1)^{\sum_{e\in E}\xi_ex_e}\), and the unnormalized Fourier multiplier is \(W(\xi)=\sum_{x\in H}f(x)\chi_\xi(x)\). Thus the eigenvalues of \(T_f\) are the real integers \(W(\xi)\), its singular values are \(|W(\xi)|\), and its nullity is the number of zero multipliers.

For a frequency \(\xi\), let \(Z=Z(\xi)=\{i:\xi_e=0\text{ for all }e\in E(P_i)\}\), put \(z=|Z|\), and define \(d_i=2^{\ell_i}-1\). Empty products equal one, and empty sums equal zero.

## Proof

**(1) Exact multiplier.** Every cycle in \(G\) is the union of two complete distinct terminal paths. Hence a subset of edges is acyclic if and only if it contains every edge of at most one complete path. On path \(i\), let \(s_i=(-1)^{\sum_{e\in E(P_i)}\xi_e}\) be the signed contribution of its unique full edge subset. The signed sum over *proper* edge subsets of that path is \(b_i=\prod_{e\in E(P_i)}(1+(-1)^{\xi_e})-s_i\). Enumerating zero or one full path gives the identity
\[
W(\xi)=\prod_{i=1}^{k}b_i+\sum_{i=1}^{k}s_i\prod_{j\ne i}b_j. \tag{1}
\]
If \(i\in Z\), then \(s_i=1\) and \(b_i=d_i\). Otherwise \(b_i=-s_i\). Setting \(U(\xi)=\prod_{i\notin Z}(-s_i)\in\{-1,1\}\), equation (1) becomes the *integer* formula
\[
\boxed{W(\xi)=U(\xi)\left[(1-k+z)\prod_{i\in Z}d_i+\sum_{i\in Z}\prod_{\substack{j\in Z\\j\ne i}}d_j\right].} \tag{2}
\]
Equivalently, because each \(d_i>0\), a zero occurs **exactly** when
\[
\boxed{\sum_{i\in Z}\frac1{2^{\ell_i}-1}=k-z-1.} \tag{3}
\]
This is an all-parameter finite arithmetic criterion, not a heuristic about approximate cancellation.

**(2) Universal congruence.** Since each \(\ell_i\ge2\), \(d_i\equiv-1\pmod4\). Reducing the integer bracket in (2) modulo four gives
\[
(1-k+z)(-1)^z+z(-1)^{z-1}\equiv(1-k)(-1)^z\pmod4.
\]
Also \(U(\xi)=(-1)^{k-z+\sum_{e\in E}\xi_e}\), so
\[
\boxed{W(\xi)\equiv(-1)^{k+\sum_{e\in E}\xi_e}(1-k)\pmod4.} \tag{4}
\]
When \(k\not\equiv1\pmod4\), the right side is nonzero modulo four, whence every multiplier is nonzero, proving invertibility regardless of path lengths. In particular, when \(k\) is even, every Fourier multiplier is odd; when \(k\equiv3\pmod4\), every multiplier is congruent to two modulo four.

**(3) Sharpness for every branch count \(4t+1\).** Let \(k=4t+1\ge5\) and set \(\ell_i=2\) for all paths. Choose a frequency which is identically zero on precisely \(z=3t\) paths, and nonzero on each other path. Then each denominator in (3) equals three, so the left side is \(z/3=t\), while the right side is \(4t+1-3t-1=t\). Thus this multiplier vanishes. The universal invertibility condition on \(k\) cannot be expanded.

**(4) Exact nullity for every graph.** Each specified zero-block set \(Z\) occurs at exactly \(\prod_{i\notin Z}(2^{\ell_i}-1)\) frequencies, since all other path blocks must be nonzero. Distinct sets \(Z\) partition the frequency domain. Consequently
\[
\boxed{\operatorname{nullity}(T_f)=\sum_{\substack{Z\subseteq\{1,\ldots,k\}\\ \sum_{i\in Z}1/d_i=k-|Z|-1}}\ \prod_{i\notin Z}d_i,\qquad \operatorname{rank}(T_f)=2^N-\operatorname{nullity}(T_f).} \tag{5}
\]
For \(k=5\), (3) is impossible at \(z\le2\) because its left side is at most \(z/3\), and at \(z\ge4\) because its left side is positive while the right side is nonpositive. The only remaining case \(z=3\) requires three reciprocals, each at most \(1/3\), to sum to one, forcing all three lengths to be exactly two. This proves the five-path criterion and displayed nullity formula.

**(5) Equi-length resonances.** When all paths have common length \(L\ge2\), (3) simplifies to \(z/(2^L-1)=k-z-1\), so a zero exists exactly when \(2^L\) divides \(k-1\), with \(z=(2^L-1)(k-1)/2^L\). If this divisibility holds, the complete nullity is
\[
\boxed{\binom{k}{z}(2^L-1)^{k-z}.} \tag{6}
\]
In particular, for \(k=5\) and \(L=2\) the nullity is \(90\), while for \(k=9\) and \(L=2\) it is \(2268\). Equation (6) is a complete classification of *all equal-length generalized theta graphs*, not merely an existence construction.

## Verification

The accompanying standalone `verify.py` constructs the complete forest indicator, computes an integer Walsh–Hadamard transform, and checks (2), (4), and relevant nullity claims for six graph configurations. Running `python3 verify.py` checks 284032 frequency values and reports exact rank, nullity, and forest count for each configuration. Its tested cases include unequal lengths, all-five-length-two singularity, a five-path graph with exactly three length-two paths, an invertible seven-path graph, and a singular nine-path graph. The proof of all-parameter equations (1)–(6) is symbolic; these finite tests are corroboration only, not exhaustive evidence for all parameters.

## Relationship to prior work

The spanning-forest generating polynomial and the Rayleigh property for series-parallel graphs are developed by Erickson (2010); the generalized theta family lies in the series-parallel setting. Thus the multivariate forest enumerator, and the possibility of evaluating it at signed edge weights, are *not* claimed to be new. Goodall (2008) provides finite Fourier analysis of graph polynomials and Tutte–Grothendieck invariants, while Bernardi (2006) develops forest-counting Tutte specializations and spanning-subgraph bijections. These general frameworks supply context, but their inspected statements do not classify the modulo-four invertibility of all-forest convolution on generalized theta graphs, give equation (3)'s Mersenne-denominator criterion, or determine the nullities in (5)–(6).

The spanning-tree indicator on the *same* generalized-theta graphs has an independently studied signed Fourier spectrum. Spanning trees are only the maximal-cardinality part of the forest support; their Walsh multipliers and invertibility conditions differ from equations (2)–(6). No claim is made that the all-forest polynomial itself, or the standard Fourier diagonalization of convolution, originated here.

## Limitations

The theorem concerns simple generalized theta graphs with \(k\ge3\), path lengths at least two, binary edge-subset incidence, and unnormalized convolution. It supplies full signed multipliers and an exact nullity test, but not a closed-form classification of every solution of the Mersenne reciprocal equation for arbitrary unequal lengths, nor sharp smallest *positive* singular values and projection endpoint norms. The finite checks do not substitute for the combinatorial and modular proof. An equivalent specialization in unindexed literature on signed graphic-matroid independence polynomials remains a historical-priority risk; no independent audit is represented.

## References

1. A. Erickson, *Sums of squares and negative correlation for spanning forests of series parallel graphs*, first public arXiv version 21 August 2010, arXiv:1008.3660, https://arxiv.org/abs/1008.3660.
2. A. Goodall, *Graph polynomials and Tutte-Grothendieck invariants: an application of elementary finite Fourier analysis*, first public arXiv version 30 June 2008, arXiv:0806.4848, https://arxiv.org/abs/0806.4848.
3. O. Bernardi, *Tutte polynomial, subgraphs, orientations and sandpile model: new connections via embeddings*, first public arXiv version 30 November 2006, arXiv:math/0612003, https://arxiv.org/abs/math/0612003.
