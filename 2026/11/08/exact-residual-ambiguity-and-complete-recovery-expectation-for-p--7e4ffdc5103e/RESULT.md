# Exact residual ambiguity and complete-recovery expectation for pairwise labeled coupon collection

## Finding

For every integer \(n\ge3\), in the Type-II labeled coupon collector with independent uniformly sampled unordered pairs of distinct coupons, let \(T_n\) be the first draw by which every coupon has appeared, \(Q_n\) the first draw at which all coupon-label matches are determined, and \(Y_n\) the number of two-vertex connected components in the accumulated pair graph at draw \(T_n\). The entire finite-sample distribution of \(Y_n\), and consequently \(\mathbb E[Q_n-T_n]\) and \(\mathbb E Q_n\), admit the following explicit finite binomial-rational expressions. No Markov-chain linear system over graph states is needed.

Write \(E=\binom n2\), \(K=\lfloor n/2\rfloor\), \(A_0=1\). For each \(1\le r\le K\), put
\[
N=n-2r,\qquad b=E-\binom N2-r,\qquad c_{N,\ell}=\binom N2-\binom{N-\ell}2,
\]
\[
A_r=\frac{n!}{(n-2r)!\,2^r}\,b
\sum_{j=0}^{r}\sum_{\ell=0}^{N}
\frac{(-1)^{j+\ell}\binom rj\binom N\ell}{b+j+c_{N,\ell}}.
\]
All denominators are positive because \(n\ge3\) and \(r\ge1\). Then for \(0\le y\le K\),
\[
\boxed{\Pr(Y_n=y)=p_y=\frac1{y!}\sum_{r=y}^K\frac{(-1)^{r-y}A_r}{(r-y)!}.}
\]
Define \(h_0=0\), and for \(1\le r\le K\), recursively
\[
h_r=\frac{E}{2r(n-r-1)}+
\frac{n-2r}{n-r-1}h_{r-1}+
\frac{r-1}{n-r-1}h_{r-2},
\]
with \(h_{-1}=0\). The expected **extra number of pair drawings due solely to unresolved labels after every coupon has already appeared** is
\[
\boxed{\mathbb E(Q_n-T_n)=\sum_{y=0}^K p_yh_y.}
\]
Finally, inclusion-exclusion for the standard pair-cover stopping time gives
\[
\boxed{\mathbb E Q_n=\sum_{j=1}^n
\frac{(-1)^{j+1}\binom nj}{1-\binom{n-j}2/\binom n2}
+\sum_{y=0}^K p_yh_y.}
\]
Thus the complete-recovery expectation is a fully explicit finite expression involving only binomial coefficients, factorials and rational arithmetic. Evaluation requires \(O(n^3)\) rational arithmetic operations by direct summation, apart from bit complexity. These statements are exact for each finite \(n\), not asymptotic approximations.

For instance, at \(n=4\), \(\Pr(Y_4=2)=1/5\), \(\Pr(Y_4=0)=4/5\), and \(\mathbb E(Q_4-T_4)=3/10\), while \(\mathbb E Q_4=41/10\). At \(n=5\), \(\Pr(Y_5=1)=11/42\), and \(\mathbb E(Q_5-T_5)=55/126\).

## Assumptions and scope

The \(n\) coupons have a fixed but unknown bijection to \(n\) labels. Each round samples one unordered 2-subset uniformly among the \(E\) possible pairs, independently with replacement. It reveals the sampled coupon pair and the *unordered* pair of their labels, not the correspondence. In Type-II collection, the set of labels is not supplied in advance. The accumulated simple graph joins coupons observed together; repetitions do not introduce new edges. A component with at least three vertices identifies all its labels, whereas a two-vertex component leaves the matching ambiguous and an isolated vertex has not yet been observed. Hence at \(T_n\) the only unresolved components are size-two components, counted by \(Y_n\); \(Q_n\) is the first time no components of size one or two remain.

The formulas make no large-\(n\) limit claim, do not concern Type-I knowledge of the label set, and do not assume edges arrive without replacement. The edge-order representation used below only describes the order of **first appearances of distinct pairs**; repeated draws still contribute to waiting time.

## Proof

**1. First appearances and exponential clocks.** For each of the \(E\) possible pairs attach an independent rate-one exponential clock. Ordering these first-ring times yields a uniform random permutation of all distinct edges. The order in which distinct edges first appear under iid uniform repeated pair sampling is also a uniform random permutation. Thus the random graph at the first time it has no isolated vertices, including its size-two-component count \(Y_n\), has exactly the same distribution under these two representations. We use exponential clocks only to calculate this stopping graph's distribution.

**2. Factorial moments of residual pairs.** Fix an **ordered** collection of \(r\) pairwise vertex-disjoint candidate edges and let \(N=n-2r\). Among the \(E\) edges, \(\binom N2\) are entirely within the complementary vertex set, \(r\) are the candidate edges, and the remaining \(b=E-\binom N2-r>0\) are forbidden if those \(r\) candidate edges are still isolated components at coverage. The first forbidden clock is an independent exponential variable \(B\) of rate \(b\). Let \(M\) be the latest first-ring time among the \(r\) candidate edges, and let \(S_N\) be the first time all complementary vertices have been touched by edges internal to the complement. These are independent. Set \(S_0=0\); set \(S_1=\infty\), since one vertex cannot be touched by an edge internal to a singleton. The specified pairs survive as isolated two-vertex components at the full-coverage time **if and only if** \(B>\max(M,S_N)\). This condition also includes the case where the final vertex is covered by a candidate pair's first edge; one must not replace the maximum by \(S_N\) alone.

For \(t\ge0\), \(\Pr(M\le t)=(1-e^{-t})^r\). Inclusion-exclusion for isolated vertices in the complementary graph gives
\[
\Pr(S_N\le t)=\sum_{\ell=0}^N(-1)^\ell\binom N\ell e^{-c_{N,\ell}t}.
\]
This also gives the required values zero for \(N=1\) and one for \(N=0\). Conditioning on the independent forbidden clock therefore yields
\[
\Pr(B>\max(M,S_N))=\int_0^\infty b e^{-bt}(1-e^{-t})^r
\Pr(S_N\le t)\,dt.
\]
Expansion of the two finite binomial sums and integration of each exponential give precisely the displayed double sum for a fixed candidate matching. There are \(n!/(2^r(n-2r)!)\) *ordered* disjoint \(r\)-tuples of candidate edges. By counting ordered \(r\)-tuples of surviving size-two components,
\[
A_r=\mathbb E[(Y_n)_r],\quad (y)_r=y(y-1)\cdots(y-r+1).
\]
Ordinary factorial-moment inversion for a variable supported on \(\{0,\ldots,K\}\) proves the formula for \(p_y\).

**3. Exact additional waiting conditional on \(Y_n\).** Once all vertices have appeared, a graph with \(r\ge1\) unresolved size-two components has exactly \(2r(n-r-1)\) eligible *distinct* pairs whose appearance merges one or two such components. Among these, \(4\binom r2\) connect two unresolved components to each other and eliminate two at once; all remaining eligible pairs eliminate one. Since each drawing is uniform among \(E\) pairs, the expected wait for a change is \(E/[2r(n-r-1)]\), and the probability that the change eliminates two unresolved components is \((r-1)/(n-r-1)\). The resulting one-dimensional skip-death recurrence is exactly the displayed formula for \(h_r\). The state of the other, larger components is irrelevant to these counts. Strong Markov conditioning at \(T_n\) gives \(\mathbb E(Q_n-T_n)=\sum p_yh_y\).

**4. Full expectation.** A specified set of \(j\) vertices remains unseen after \(m\) draws with probability \((\binom{n-j}2/E)^m\). Inclusion-exclusion followed by the geometric sum over \(m\ge0\) gives the formula for \(\mathbb E T_n\). Adding the independently established extra conditional mean completes the proof of the full-recovery identity. Every sum is finite, all probabilities are nonnegative by their probabilistic derivation, and the formulas include all boundary cases \(n\ge3\).

## Verification

Run `python verify.py` using only the Python standard library. The checker evaluates every factorial-moment and probability identity with exact `fractions.Fraction` arithmetic, verifies normalization for all \(3\le n\le13\), and independently enumerates the uniform-new-edge graph process through \(n=6\) to recover both the residual-component law and the complete Type-II expected waiting time by direct first-step equations. It reports 79 exact-rational assertions passed. Its exhaustive enumeration covers only the stated finite sizes; the general identities follow from the analytical proof.

## Relationship to prior work

Berrebi, Yaakobi, Yakhini and Bar-Lev (arXiv:2502.02968, first version February 5, 2025) identify connected components of size at least three as the units that reveal labels for pair sampling and give finite-state Markov-chain approaches for recovery questions. Tan et al. (arXiv:2507.15231, July 21, 2025) describe expected Type-I/II completion times using a Markov-chain model. Barak-Pelleg and Berend (arXiv:2510.23249, October 27, 2025) prove that the Type-II expected completion time differs from ordinary two-coupon coverage by at most \(O((\log n)^5)\), via an upper bound on surviving isolated edges. These results motivate the finite-dimensional ambiguity variable; they do not in their inspected statements or proofs give its full law at the **random coverage stopping time** or the resulting explicit finite-sum exact expectation formula. The standard inclusion-exclusion for coupon coverage is used as a supporting calculation and not claimed as new. The exponential-clock argument strengthens a generic state-recursion approach by reducing the exact residual law to finite combinatorial sums.

## Limitations

Historical uniqueness is not mathematically certified; an unlocated general random-graph stopping-time enumeration might specialize to the displayed formula. The result is for uniformly selected unordered pairs and Type-II complete recovery only; no asymptotic constant, limit law or higher-sample-size analogue is asserted. Alternating exact sums may suffer numerical cancellation in floating-point arithmetic, so rational arithmetic or sufficient precision is recommended. Independent mathematical audit has not been performed.

## References

1. S. S. Berrebi, E. Yaakobi, Z. Yakhini, D. Bar-Lev, *The Labeled Coupon Collector Problem with Random Sample Sizes and Partial Recovery* (2025), https://arxiv.org/abs/2502.02968 (first public version 2025-02-05).
2. A. Tan, O. Limor, D. Bar-Lev, R. Gabrys, Z. Yakhini, P. H. Siegel, *The Labeled Coupon Collector Problem* (2025), https://arxiv.org/abs/2507.15231 (first public version 2025-07-21).
3. D. Barak-Pelleg, D. Berend, *On Conjectures concerning the Labeled Coupon Collector Problem* (2025), https://arxiv.org/abs/2510.23249 (first public version 2025-10-27; primary MSC2020 60C05).
4. R. Tauraso, *Edge cover time for regular graphs*, Journal of Integer Sequences 11 (2008), https://art.torvergata.it/handle/2108/27711 (general context for pair-cover stopping times; no priority claim about residual ambiguity).
