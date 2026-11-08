# Exact random-greedy independence laws on uniformly leaf-decorated paths

## Finding
For integers \(n\ge1\) and \(q\ge2\), let \(C_{n,q}\) be the tree with a spine path of \(n\) vertices and exactly \(q\) private pendant leaves attached to every spine vertex. Process the \((q+1)n\) vertices in a uniformly random order, accepting each if none of its previously accepted neighbors is adjacent to it. Let \(X_{n,q}\) be the number accepted, and set \(P_{n,q}(z)=\mathbb E[z^{X_{n,q}}]\), with \(P_{0,q}(z)=1\).

The complete finite-size distribution is specified by the formal-power-series Riccati identity
\[
F_q(u,z)=\sum_{n\ge0}P_{n,q}(z)u^n,\qquad
(q+1)\frac{\partial F_q}{\partial u}
=qz^qF_q^2+z(1+z^quF_q)^2,\quad F_q(0,z)=1.
\]
Equivalently, every coefficient can be calculated exactly by the finite recurrence
\[
(q+1)nP_{n,q}(z)=qz^q\sum_{i=1}^nP_{i-1,q}(z)P_{n-i,q}(z)
+z\mathbf1_{\{n=1\}}+2z^{q+1}\mathbf1_{\{n\ge2\}}P_{n-2,q}(z)
+z^{2q+1}\sum_{i=2}^{n-1}P_{i-2,q}(z)P_{n-i-1,q}(z).
\]
The last sum is empty for \(n\le2\). In particular, the probability support has the exact gap pattern
\[
\operatorname{supp}(X_{n,q})
=\{qn-(q-1)k:0\le k\le\lceil n/2\rceil\},
\qquad\Pr(X_{n,q}=qn)=\left(\frac q{q+1}\right)^n.
\]
Every listed value occurs with strictly positive probability.

Writing \(a=1/(q+1)\) and \(p=(1-e^{-2a})/2\), the expected cardinality has the exact finite formula
\[
\mathbb E X_{n,q}
=qn-(q-1)\sum_{j=0}^{n-1}\frac{(n-j)(-2)^j a^{j+1}}{(j+1)!},
\]
and the sharp boundary-corrected asymptotic formula
\[
\mathbb E X_{n,q}
=\bigl(q-(q-1)p\bigr)n-(q-1)\bigl(p-ae^{-2a}\bigr)
+O_q\!\left(\frac{(2a)^{n+1}}{(n+2)!}\right).
\]
Thus the limiting expected accepted fraction among all \((q+1)n\) vertices is \([q-(q-1)p]/(q+1)\).

## Assumptions and scope
All graphs are finite, simple and unweighted; arrivals are a uniformly random permutation, or equivalently independent continuous uniform priority labels. Here \(q\ge2\) and \(n\ge1\) are arbitrary integers. The path-spine endpoint cases \(n=1,2\) are included. The random variable counts accepted *vertices*, not maximal-independent-set multiplicities under uniform sampling of maximal independent sets. The generating function is an ordinary formal power series in \(u\) with polynomial coefficients in \(z\); no analytic convergence in \(u\) is needed.

## Proof
First expose the minimum-priority vertex, which is uniformly distributed over the \((q+1)n\) vertices. Its spine index \(i\) is uniform on \(\{1,\ldots,n\}\). With probability \(q/(q+1)\) it is a pendant leaf. This accepted leaf blocks its unique spine neighbor; the other \(q-1\) leaves of that cell are then isolated and must eventually be accepted. The other remaining components are independent copies of \(C_{i-1,q}\) and \(C_{n-i,q}\), with independent uniform relative orders. This contributes \(q\) accepted vertices plus the two component counts.

With probability \(1/(q+1)\) the first vertex is the spine vertex of cell \(i\). It is accepted, all \(q\) leaves of its own cell are blocked, and each adjacent spine cell (if present) has its spine vertex blocked, so all its \(q\) leaves are accepted. The remaining components are independent \(C_{\max(i-2,0),q}\) and \(C_{\max(n-i-1,0),q}\). This contributes \(1+q\mathbf1_{\{i>1\}}+q\mathbf1_{\{i<n\}}\) accepted vertices plus those component counts. Averaging the product of the two component generating polynomials over all \(i\), and splitting the spine-first case into \(n=1\), endpoints, and interior indices, proves the displayed finite recurrence. Multiplying by \(u^{n-1}\) and summing over \(n\ge1\) yields the stated Riccati equation; conversely this equation with initial value \(1\) determines each polynomial uniquely.

Let \(K_{n,q}\) count accepted *spine* vertices. At termination, each unaccepted spine vertex has all its \(q\) pendant leaves accepted, while every accepted spine vertex has none. Consequently \(X_{n,q}=qn-(q-1)K_{n,q}\) identically. Accepted spine vertices form an independent set on the path, so \(0\le K_{n,q}\le\lceil n/2\rceil\). Conversely, for any independent set of \(k\) spine indices, the positive-probability event that the spine vertex is first within its cell at those indices and some leaf is first within every other cell makes exactly those \(k\) spine vertices accepted. Thus every \(k\) in the stated interval is possible. For \(q\ge2\), \(X_{n,q}=qn\) exactly when no spine vertex is accepted; this occurs if and only if some pendant arrives earlier than the spine vertex independently in each cell, yielding the claimed product probability.

For completeness, evaluate the expectation independently of the distribution recurrence. Give every vertex an independent uniform arrival time. In a one-sided decorated path with \(m\) spine cells and with the predecessor of its endpoint removed, let \(h_m(t)\) be the probability that the endpoint spine vertex has not been accepted by time \(t\). We have \(h_0(t)=1\) and
\[
h_m(t)=1-\int_0^t(1-s)^qh_{m-1}(s)\,ds.
\]
Indeed, acceptance of the endpoint at time \(s\) requires its \(q\) private leaves not to have arrived before \(s\), and its unique surviving spine neighbor not to have been accepted in the graph with this endpoint removed. With \(x(t)=[1-(1-t)^{q+1}]/(q+1)\), the recursion gives
\[
h_m(t)=\sum_{j=0}^m\frac{(-x(t))^j}{j!}.
\]
At spine index \(i\), its left and right branches become independent when the index is removed. Its acceptance probability therefore equals \(\int_0^a E_{i-1}(-x)E_{n-i}(-x)\,dx\), where \(E_m(y)=\sum_{j=0}^m y^j/j!\). Summing over \(i\), and using the formal identity
\[
\sum_{m\ge0}E_m(-x)y^m=\frac{e^{-xy}}{1-y},\qquad
\sum_{i=1}^n E_{i-1}(-x)E_{n-i}(-x)
=\sum_{j=0}^{n-1}\frac{(n-j)(-2x)^j}{j!},
\]
shows that
\[
\mathbb E K_{n,q}
=\sum_{j=0}^{n-1}\frac{(n-j)(-2)^ja^{j+1}}{(j+1)!}.
\]
This proves the exact expected-cardinality formula via the identity for \(X_{n,q}\). Extending the last series to infinity gives \(\mathbb E K_{n,q}=(n+1)p-ae^{-2a}+R_n\), where
\[
|R_n|\le \frac{a(2a)^{n+1}}{(n+2)!}\left(1-\frac{2a}{n+3}\right)^{-2}.
\]
Since \(q\ge2\), \(2a\le2/3\); the displayed bound proves the superfactorial remainder uniformly in the stated range and completes the proof.

## Verification
The standalone file `VERIFY.py` constructs the family polynomials by first-cell decomposition and independently computes the full probability law by the general graph rule \(R_H(z)=z|V(H)|^{-1}\sum_{v\in V(H)}R_{H-N[v]}(z)\), using exact rational arithmetic and a graph-neighborhood bitmask. It checks complete polynomial equality on all instances with \((q+1)n\le16\) for \(1\le q\le6\), and checks normalization, support, maximum-output probability, the closed finite mean, and every displayed polynomial recurrence through \(n=17\). The run produced `VERIFY_OK 738 exact checks`. The case \(q=1\) is used only as an independent boundary control: then the output is deterministically \(n\), and the maximum-output probability formula above is deliberately restricted to \(q\ge2\). The infinite-size asymptotic is proved by the explicit series remainder bound, not by finite testing.

## Relationship to prior work
Krivelevich, Mészáros, Michaeli and Shikhelman establish an extensive local-limit framework for random-order greedy maximal independent sets, including the exact mean on ordinary paths (with a truncated exponential series), asymptotic densities, and tree comparisons. The expected-size expression above is a parameter-rescaled relative of their ordinary-path formula and is not claimed as a new general method. Penrose and Sudbury give general blocking-RSA forward equations and probabilities on regular infinite trees. Those general approaches are foundational to this problem; the specific contribution here is a finite-volume *full probability law* on uniformly leaf-decorated paths with arbitrary integer decoration number, a compact exact Riccati equation, an all-size support characterization, and a sharp boundary correction. The source texts inspected do not give these evaluated full-distribution formulas for this family. General methods could imply portions after specialization, and a comprehensive historical-priority proof is not claimed.

## Limitations
The theorem concerns the uniform random arrival order, not a uniform random choice among maximal independent sets; nonuniform priorities and random graph topology are not treated. It gives the complete finite distribution algorithmically through an exact recursion, not a simple closed coefficient formula for every probability. No central limit theorem, variance asymptotic, or uniqueness statement about the literature is asserted. Source comparison is limited to the cited works and targeted searches; earlier or unindexed specialized enumerations remain possible.

## References
1. M. Krivelevich, T. Mészáros, P. Michaeli and C. Shikhelman, *Greedy maximal independent sets via local limits*, arXiv:1907.07216, first public version 2019-07-16; *Random Structures & Algorithms* 64 (2024), 986–1015, DOI: 10.1002/rsa.21200. https://arxiv.org/abs/1907.07216
2. M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, *Annals of Applied Probability* 15 (2005), 853–889, arXiv:math/0503519. https://arxiv.org/abs/math/0503519
