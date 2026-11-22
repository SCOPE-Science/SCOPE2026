# Exact corank-two Brauer product fibers and parity-dependent absorption laws

## Finding
Let \(n\ge3\), let \(\mathcal B_n\) be the finite Brauer diagram monoid, and let \(\mathcal C_n\) denote its complete stratum of diagrams of propagating rank \(n-2\), **not merely its idempotents**. Choose \(X_1,X_2,\ldots\) independently and uniformly from \(\mathcal C_n\), and set \(Y_k=X_1\cdots X_k\). Put \(m=n\bmod2\), \(J=(n-2-m)/2\), \(r_j=n-2-2j\) for \(0\le j\le J\), and
\[
p_j=\frac{r_j(r_j-1)}{n(n-1)},\qquad a_j=1-p_j,\qquad p_J=0.
\]
Then the ranks of successive products form the pure-death Markov chain \(r_j\mapsto r_{j+1}\) with probability \(p_j\) and \(r_j\mapsto r_j\) with probability \(a_j\). Its complete exact law is
\[
\Pr(\operatorname{rank}Y_k=r_j)=[z^{k-1}]\,\frac{z^j\prod_{i=0}^{j-1}p_i}{\prod_{i=0}^{j}(1-a_i z)}\quad(k\ge1),
\]
where an empty product equals one. No other ranks occur.

More strongly, the law of \(Y_k\) is **uniform within each attainable rank stratum**. With \((-1)!!=1\) and
\[
D_{n,r}=\binom nr^2\big((n-r-1)!!\big)^2r!,\qquad C_n=D_{n,n-2},
\]
the number of **ordered, prescribed-output** factorizations \(x_1\cdots x_k=h\), with every \(x_i\in\mathcal C_n\), is exactly
\[
N_{n,k}(h)=\frac{C_n^k}{D_{n,r}}[z^{k-1}]\,\frac{z^j\prod_{i=0}^{j-1}p_i}{\prod_{i=0}^{j}(1-a_i z)},\qquad r=\operatorname{rank}h=r_j;
\]
it is zero for other target ranks. This includes \(k=1\), all small degrees, and every Brauer diagram as a prescribed target. The displayed rational coefficient always gives a nonnegative integer after the indicated normalization.

Let \(T_n\) be the number of further multiplicative steps after \(X_1\) needed to enter the minimum-rank stratum \(r=m\). It is the sum of independent geometric waiting times, one for each \(r=n-2,n-4,\ldots,m+2\), with success parameter \(r(r-1)/(n(n-1))\). Consequently, with \(H_a=\sum_{i=1}^a1/i\) and \(H_0=0\), its exact expectation is
\[
\mathbb E T_n=\begin{cases}
n(n-1)(H_{n-2}-H_{(n-2)/2}),&n\text{ even},\\
n(n-1)(1+H_{(n-3)/2}-H_{n-2}),&n\text{ odd}.
\end{cases}
\]
Hence \(\mathbb E T_n/[n(n-1)]\to\log2\) along even \(n\) and \(\to1-\log2\) along odd \(n\). More precisely, along either parity subsequence,
\[
\frac{T_n}{n(n-1)}\ \Longrightarrow\
\begin{cases}
\displaystyle\sum_{j\ge1}\frac{E_{2j}}{(2j)(2j-1)},&n\text{ even},\\
\displaystyle\sum_{j\ge1}\frac{E_{2j+1}}{(2j+1)(2j)},&n\text{ odd},
\end{cases}
\]
where the \(E_r\) are independent unit-mean exponential variables. Both limiting sums converge almost surely and in \(L^1\), have finite, positive variance, and differ in law. If \(U_m\) denotes the uniform law on the minimum-rank stratum, then the **exact**, finite-\(n\) mixing identity is
\[
d_{\rm TV}(\mathcal L(Y_k),U_m)=\Pr(T_n>k-1).
\]
In particular, the approach to the minimal ideal occurs on a quadratic scale with a nondegenerate parity-dependent profile, rather than a vanishing-width cutoff.

## Assumptions and scope
A Brauer \(n\)-diagram is a perfect matching on the two copies \(\{1,\ldots,n\}\) and \(\{1',\ldots,n'\}\). The product is obtained by stacking and identifying the middle row, discarding components entirely in that row; **no loop weight from a Brauer algebra is retained**. Its propagating rank is the number of matching edges connecting the upper to lower boundary. Allowed ranks have the parity of \(n\). Uniform means each distinct matching of rank \(n-2\) has the same mass. Product-length \(k\) is any integer at least one, and \(h\) is an arbitrary diagram in \(\mathcal B_n\). The case \(n=3\) is degenerate but included: the initial rank one is already minimum, so \(T_3=0\).

## Proof
**1. Rank transition.** Fix a diagram \(x\) of rank \(r\). Exactly \(r\) middle-row vertices of \(x\) lie on propagating strands; the remaining \(n-r\) are paired into bottom hooks. Every diagram \(y\) of rank \(n-2\) has a unique top hook, which is a two-element subset \(U\subseteq\{1,\ldots,n\}\). For uniformly chosen \(y\), the set \(U\) is uniform among all \(\binom n2\) subsets, since boundary permutations act transitively and preserve the rank stratum. If both points of \(U\) are among the propagating middle endpoints of \(x\), two propagating paths terminate in a new top hook, and the product rank drops from \(r\) to \(r-2\). Otherwise no two propagating paths terminate against one another: tracing the length-two middle path when one selected point belongs to a bottom hook, or the internal middle cycle/path when both do, shows the rank stays \(r\). Thus
\[
\Pr(\operatorname{rank}(xy)=r-2\mid x)=\frac{\binom r2}{\binom n2}=\frac{r(r-1)}{n(n-1)}.
\]
The answer depends on \(x\) only via its rank, proving the Markov law under independent right multiplication. The minimum rank has zero downward probability.

**2. Uniform conditional fibers.** The units \(\mathfrak S_n\subset\mathcal B_n\) permute upper and lower vertices. For any allowable \(r\), the two-sided action \((\sigma,\tau):x\mapsto\sigma x\tau\) is transitive on \(\mathcal D_{n,r}=\{x:\operatorname{rank}x=r\}\): independently map the top and bottom nonpropagating perfect matchings to standard matchings, then map the propagating bijection to the identity. The uniform law on \(\mathcal C_n\) is invariant under left and right unit multiplication. Therefore every convolution power of that law has the same two-sided invariance, so all diagrams within \(\mathcal D_{n,r}\) have equal probability. Counting top and bottom propagating subsets, their remaining matchings and the connecting bijection gives \(D_{n,r}\). Therefore a prescribed target \(h\) of rank \(r\) has mass \(\Pr(\operatorname{rank}Y_k=r)/D_{n,r}\); multiply by \(C_n^k\) to get the number of ordered factorizations.

**3. Exact generating function.** Let \(f_j(t)=\Pr(\operatorname{rank}Y_{t+1}=r_j)\). By Step 1, \(f_0(0)=1\), \(f_j(0)=0\) for \(j>0\), and
\[
f_j(t+1)=a_j f_j(t)+p_{j-1} f_{j-1}(t)
\]
for \(j\ge1\), with the obvious \(j=0\) equation. Taking ordinary generating functions in \(t\) and iterating the recurrence gives
\[
\sum_{t\ge0}f_j(t)z^t=\frac{z^j\prod_{i=0}^{j-1}p_i}{\prod_{i=0}^j(1-a_i z)}.
\]
This proves the complete prescribed-output count, including finite-time support constraints from the numerator \(z^j\).

**4. Absorption and its limit.** At rank \(r>m\), every step has conditional decrement probability \(p_r>0\). Independent fresh factors, the strong Markov property and the memoryless geometric law yield independent waiting times \(G_{n,r}\) of parameter \(p_r\), with \(T_n=\sum_rG_{n,r}\). The means sum to \(n(n-1)\sum_r1/(r(r-1))\). Splitting consecutive reciprocal differences \(1/[r(r-1)]=1/(r-1)-1/r\) into alternating harmonic sums gives the stated even/odd formulas.

For each fixed admissible \(r\), the rescaled \(G_{n,r}/[n(n-1)]\) tends in law to an exponential of rate \(r(r-1)\); waiting times at distinct ranks remain independent. The remaining tail beyond fixed rank \(R\) has expected scaled size at most \(\sum_{r>R}1/[r(r-1)]\), which goes to zero uniformly in \(n\). This proves the weak convergence of the sums by truncation. The limit series converges absolutely almost surely by finite expected sum, and in \(L^1\); its variance is finite and nonzero because \(\sum_r1/[r^2(r-1)^2]\) is finite and positive. Finally, the minimum-rank class is absorbing and conditional uniformity holds there at every time. On its complement the law has disjoint support from \(U_m\). Therefore total variation equals the mass outside the minimum class, proving the exact mixing identity and the nondegenerate quadratic scaling.

## Verification
Run `python3 verify.py` alongside this document; it uses only the Python standard library. It independently constructs perfect matchings, concatenates three-layer diagrams by tracing components, enumerates all corank-two inputs for \(n=3,4,5\), and compares every prescribed-product target with the coefficient formula for two factors (and up to four factors for \(n\le4\)). It also tests the local rank-drop characterization for sampled current diagrams of every rank at \(n=6\) against all possible top hooks, and checks stochastic normalization across \(3\le n<20\) and several product lengths. The separately supplied `checker_output.txt` is the actual output from running the included code. These finite checks validate the implementation and boundary cases; the all-degree theorem and asymptotic assertions rest on the proof above.

For example, for \(n=4\) the first rank stratum has \(72\) elements. Two-factor products attain \(864\) rank-zero and \(4320\) rank-two ordered pairs; these are uniform over the \(9\) rank-zero and \(72\) rank-two targets, respectively. For \(n=5\), there are \(600\) one-hook diagrams, and two factors give \(108000\) products of rank one and \(252000\) of rank three, each equally distributed among the respective rank classes.

## Relationship to prior work
East and Gray (first public arXiv version 9 April 2014, Section 8) establish the Brauer monoid rank classes, ideal structure, idempotent generation and minimum generating-set enumeration. Their Lemma 8.3 shows reachability of lower rank classes by higher-rank products, but not the **number of ordered factorizations at every length**, rank-uniform convolution, stochastic transitions or absorption laws. Dolinka and East (first preprint 29 October 2015, Sections 2–3) analyze Green relations, ideals and idempotent generation in the twisted Brauer monoid, where floating components are retained as an extra coordinate; none of their statements supplies the present fixed-corank unweighted convolution law. Wolff (2018, Sections 3–5) studies Metropolis/systematic-scan walks generated by local diagram moves for Brauer/BMW algebras; her walk and limiting objective are different from independent uniform sampling from the entire rank-\(n-2\) class, and the complete fibers and quadratic absorption profile are not given. The basic loop-erasing product and individual rank-stratum combinatorics are acknowledged inputs, not novelty claims.

The pair-merger rates and sums of exponential waiting times are standard features of the Kingman coalescent (Kingman, 1982). These probabilistic identities are not claimed new in isolation; the asserted contribution is the exact correspondence with multiplication by the entire Brauer corank-two rank class and the resulting per-diagram product fibers, including a forced parity restriction on merger states.

The symmetric inverse monoid also has rank-uniform convolution laws under uniform fixed-corank partial permutations; its deleted-subset/coupon-collector mechanism has different transition rates and does not cover the hook-pairing Brauer monoid. Earlier work on commuting subsets of corank-two Brauer/Jones idempotents concerns commutation, not distributions of arbitrary (non-idempotent) product factors. Search-based novelty is provisional; an unlocated general double-coset convolution or diagram-monoid probability theorem could imply these formulas.

## Limitations
The result concerns the **uniform** entire rank-\(n-2\) Brauer stratum and products in the loop-erasing monoid. It does not include nonuniform or idempotent-only factor measures, a joint distribution with erased-loop counts, random products of arbitrary rank strata, Brauer algebra scalar weights, or the BMW braid/tangle product. The all-length coefficient formula is explicit but not simplified to a single elementary binomial expression. Although the primary closely related sources have been compared in material detail, historical exhaustiveness and independent mathematical validation are not claimed. This is a self-contained proof checked against finite exact enumeration, not an infinite computer certificate.

## References
1. J. East and R. D. Gray, *Diagram monoids and Graham–Houghton graphs: idempotents and generating sets of ideals*, first public preprint 9 April 2014, arXiv:1404.2359, https://arxiv.org/abs/1404.2359 .
2. I. Dolinka and J. East, *Twisted Brauer monoids*, first public preprint 29 October 2015, arXiv:1510.08666, https://arxiv.org/abs/1510.08666 .
3. S. Wolff, *Random walks on the BMW monoid: an algebraic approach*, first online publication 28 November 2018, *Journal of Algebraic Combinatorics* 50 (2019), 347–361, https://doi.org/10.1007/s10801-018-0858-7 .
4. J. F. C. Kingman, *The coalescent*, *Stochastic Processes and their Applications* 13 (1982), 235–248, https://doi.org/10.1016/0304-4149(82)90011-4 .
