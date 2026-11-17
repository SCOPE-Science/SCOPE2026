# Exact counting of connected outer-EF1 allocations of binary-valued biclique goods

## Finding

Let \(G=K_{a,b}\) have two nonempty sides of sizes \(a,b\), and let \(1\le k\le a+b\). All \(k\) labelled agents have one **identical**, additive \(\{0,1\}\)-valued valuation on the vertices. A complete allocation gives each agent a nonempty connected induced vertex set and allocates every vertex. It is *outer-EF1* when envy of any other bundle can be removed by deleting at most one vertex from the envied bundle, while keeping the remainder connected (the empty remainder is permitted).

The contribution here is an **exact counting formula for every fixed valuation profile**, not a new proof of the already published universal existence spectrum. Let \(a_+,a_0,b_+,b_0\) be the numbers of positive/zero vertices on the respective sides, and \(P=a_++b_+\). For a bundle profile \(h=(i,j,\ell,m)\), put \(s_A=i+j\), \(s_B=\ell+m\), \(t(h)=i+\ell\) and
\[
 C(h)\iff (s_A+s_B=1)\ \text{or}\ (s_A\ge1\ \text{and}\ s_B\ge1),
\]
\[
 R(h)\iff [s_A+s_B=1\ \text{and}\ t(h)=1]
 \lor [i\ge1\ \text{and}\ (s_A\ge2\ \text{or}\ s_B=1)]
 \lor [\ell\ge1\ \text{and}\ (s_B\ge2\ \text{or}\ s_A=1)].
\]
The predicate \(C\) expresses connectedness; \(R\) expresses the existence of a positive vertex whose removal leaves a connected bundle, including the allowed empty singleton remainder.

With \(x^h=x_+^i x_0^j y_+^\ell y_0^m\), define finite polynomials
\[
 P_t(x)=\sum_{\substack{0\le h\le(a_+,a_0,b_+,b_0)\\C(h),\ t(h)=t}}
 \frac{x^h}{i!j!\ell!m!},\qquad
 Q_t(x)=\sum_{\substack{0\le h\le(a_+,a_0,b_+,b_0)\\C(h),\ R(h),\ t(h)=t}}
 \frac{x^h}{i!j!\ell!m!}.
\]
Set \(Q_{P+1}=0\). The number of **labelled complete connected outer-EF1 allocations** is exactly
\[
\boxed{\mathcal N(a_+,a_0,b_+,b_0;k)=a_+!a_0!b_+!b_0!
 [x_+^{a_+}x_0^{a_0}y_+^{b_+}y_0^{b_0}]
 \sum_{t=0}^{P}\big[(P_t+Q_{t+1})^k-Q_{t+1}^k\big].}
\]
All expressions may be truncated to the prescribed four degrees. A four-category dynamic program computes the count in time polynomial in \(a+b+k\), including polynomial-bit-size integer arithmetic.

For the all-one profile let \(n=a+b=kq+r\), \(0\le r<k\), and \(H_1(z)=1+z\), \(H_s(z)=(1+z)^s-1-z^s\) for \(s\ge2\). Then
\[
\boxed{\mathcal N_1(a,b;k)=\binom{k}{r}\frac{a!b!}{(q!)^{k-r}((q+1)!)^r}
 [z^a]H_q(z)^{k-r}H_{q+1}(z)^r.}
\]
For example, \(\mathcal N_1(2,4;k)\) for \(k=1,\dots,6\) equals \((1,12,0,288,960,720)\).

## Definitions, scope, and proof

Every nonempty connected induced set of \(K_{a,b}\) is either a singleton or meets both sides. Removing a positive vertex from a nonsingleton preserves this property precisely under the two alternatives expressed by \(R\). Its utility falls by exactly one. An outer-EF1 allocation with binary common values either has a common utility \(t\) in all bundles, or has utility values \(t,t+1\), with both levels occurring and with every high-valued bundle satisfying \(R\). Necessity follows because deleting one binary good reduces utility by at most one. Conversely these conditions permit envy of every high-valued bundle to be removed while preserving connectivity.

Fix \(t\) and use labelled exponential generating functions in the four vertex categories. In \((P_t+Q_{t+1})^k\), each of the \(k\) labelled bundles is connected and either has utility \(t\), or has utility \(t+1\) and an outer positive vertex. The subtraction \(Q_{t+1}^k\) removes exactly the all-high allocations, thereby requiring at least one utility-\(t\) bundle. All-equal allocations appear only in the \(P_t^k\) contribution at their actual utility \(t\). Consequently the sum over \(t\) counts every outer-EF1 partition exactly once. The four factorials and coefficient extraction select and distribute the distinctly labelled physical vertices in each category, establishing the main formula.

For the all-one specialization, the binary utility-spread condition forces bundle sizes \(q\) or \(q+1\), with precisely \(r\) larger bundles. For a singleton the generating polynomial marking its \(A\)-vertex count is \(1+z\), while for size \(s\ge2\), connectedness requires at least one vertex of each shore and hence contributes \((1+z)^s-1-z^s\). Choose which \(r\) labelled bundles are larger, extract the coefficient of \(z^a\), and multiply by the multinomial factors \(a!b!/(q!)^{k-r}((q+1)!)^r\). This yields the stated specialization.

The polynomial algorithm stores at most \((a_++1)(a_0+1)(b_++1)(b_0+1)\) four-category degree states and processes \(k\) labelled bundles, with at most \(P+1\) utility levels; the number counted is at most \(k^{a+b}\), so its integer bit length is polynomial. In particular the statement is not restricted to a fixed number of agents, and computes zero where no feasible outer-EF1 allocation exists.

## Previously established existence spectrum

The published *Exact binary outer-EF1 spectrum of complete bipartite graphs* (November 1, 2026) already proves that universal existence for all identical binary valuations holds if and only if \(k\le\min(a,b)\) or \(k\ge\max(a,b)\), including polynomial constructive algorithms. The later *Exact connected EF1 spectrum of complete bipartite graphs under arbitrary monotone valuations* (November 2, 2026) proves the broader **ordinary EF1** spectrum for heterogeneous monotone valuations and proves outer-EF1 sufficiency in the full high-agent range. Those existence theorems are credited, not newly claimed. The new result here is the full valuation-refined **allocation count**, not merely the yes/no threshold; the all-one coefficient formula is a specialization of that count.

## Verification and limitations

The accompanying unchanged `checker.py` computes the same four-profile count using exact integer dynamic programming, and independently enumerates every assignment of small numbers of distinct goods to labelled agents, testing induced connectivity and deletability. Its finite checks compare 304 small binary profiles, 252 all-one coefficient cases, and 1,611 universal-existence cases. An independent direct enumeration reproduces the displayed \(K_{2,4}\) six-vector. These checks do not prove the all-parameter theorem; the local connectedness predicate and labelled generating-function argument above do.

The exact enumeration assumes complete bipartite vertex-resource graphs, one common binary additive valuation, all vertices allocated, all bundles nonempty and connected, and deletion leaving a connected (possibly empty) remainder. It does not count arbitrary monotone, heterogeneous, weighted, or nonbinary valuations, nor arbitrary resource graphs. The count is polynomial-time only in this restricted family. A general multitype generating-function formalism could conceivably imply the formula implicitly in earlier literature; that historical-priority risk is retained.

## References

- *Exact binary outer-EF1 spectrum of complete bipartite graphs* (published November 1, 2026), https://github.com/Resultary/2026/tree/main/2026/11/1/SCOPE-exact-binary-mathrm-ef1-mathrm-outer-spectrum-of-complete-bipart--018091c6bd7b.
- *Exact connected EF1 spectrum of complete bipartite graphs under arbitrary monotone valuations* (published November 2, 2026), https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-exact-connected-ef1-spectrum-of-complete-bipartite-graphs-under--a444bb42185d.
- N. Bousquet, F. Connor, A. Totschnig and S. Zeitoun, *Fair Division of Graphs: Beyond Traceability*, arXiv:2608.29902 (2026), https://arxiv.org/abs/2608.29902.
- X. Bei, A. Igarashi, X. Lu and W. Suksompong, *The Price of Connectivity in Fair Division*, arXiv:1908.05433, https://arxiv.org/abs/1908.05433.
- A. Igarashi and W. S. Zwicker, *Fair Division of Graphs and of Tangled Cakes*, DOI:10.1007/s10107-023-01945-5.
