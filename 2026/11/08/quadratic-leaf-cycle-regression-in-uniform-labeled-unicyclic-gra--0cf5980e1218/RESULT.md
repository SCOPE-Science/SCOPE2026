# Quadratic leaf–cycle regression in uniform labeled unicyclic graphs

## Finding

For every integer \(n\ge3\), choose a simple connected graph uniformly from the labeled graphs on \([n]=\{1,\dots,n\}\) with exactly \(n\) edges. Write \(K_n\) for the length of its unique cycle and \(L_n\) for its number of degree-one vertices. For every \(3\le k\le n\),
\[
\mathbb E[L_n\mid K_n=k]=(n-k)\left(1-\frac1n\right)^{n-k-1},
\]
with value zero at \(k=n\). This conditional expectation strictly decreases with \(k\), so \(\operatorname{Cov}(L_n,K_n)<0\) for every \(n\ge4\); at \(n=3\) both statistics are deterministic.

More precisely, let \(S\) have the half-normal distribution, with density \(\sqrt{2/\pi}\,e^{-s^2/2}\) on \(s>0\). As \(n\to\infty\),
\[
\frac{K_n}{\sqrt n}\ \xrightarrow{\mathrm d}\ S,
\qquad
\mathbb E[L_n\mid K_n]-\frac ne\ \xrightarrow{\mathrm d}\ \frac{1-S^2}{2e},
\]
and
\[
\boxed{\lim_{n\to\infty}\frac{\operatorname{Cov}(L_n,K_n)}{\sqrt n}
=-\frac{1}{2e}\sqrt{\frac2\pi}.}
\]
In particular, a change in cycle length on its natural square-root scale changes conditional mean leaf count only at constant order: the first-order, linear dependence cancels.

## Assumptions and scope

All graphs are finite, undirected, simple, connected, with distinct vertex labels and one more edge than a tree. There are no loops or multiple edges. A leaf means degree exactly one in the full graph, not degree zero in a rooted forest. The result is exact for all integer \(n\ge3\). The weak limits are for the uniform model just specified, not the evolving multigraph model or a sparse unconditioned Erdős–Rényi graph.

Put \(q_n=1-1/n\), \(b_{n,k}=(n)_k/n^k\), and \(Z_n=\sum_{k=3}^n b_{n,k}\). Here \((n)_k=n(n-1)\cdots(n-k+1)\). Then
\[
\Pr(K_n=k)=\frac{b_{n,k}}{Z_n},\qquad 3\le k\le n.
\]
These explicit weights also give a finite exact expression for every covariance by summation against the conditional mean above.

## Proof

**1. Enumerate graphs with a specified cycle.** Fix a set \(R\) of \(k\) cycle vertices. The cycle has \((k-1)!/2\) undirected arrangements. Deleting its cycle edges leaves a forest in which every component has exactly one specified root in \(R\). If \(k<n\), the number of such rooted forests is \(k n^{n-k-1}\): the matrix-tree rooted-forest determinant is \(\det(nI_{n-k}-J_{n-k})=k n^{n-k-1}\). For \(k=n\) the empty forest count is one, agreeing with the same formal expression. Consequently, the number of graphs with cycle length \(k\) is
\[
\binom nk\frac{(k-1)!}{2}\,k n^{n-k-1}
=\frac{n^{n-1}}2\frac{(n)_k}{n^k}.
\]
Normalization over \(3\le k\le n\) proves the asserted law of \(K_n\).

**2. Count conditional leaves.** Only the \(n-k\) non-cycle vertices can be leaves. For a fixed nonroot vertex \(v\), requiring it to be a leaf is equivalent to selecting its parent among the other \(n-1\) vertices and selecting a rooted forest on the remaining \(n-1\) labels with the same \(k\) prescribed roots. By the rooted-forest formula, for \(n-k\ge2\), its conditional probability of being a leaf is
\[
\frac{(n-1)\,k(n-1)^{n-k-2}}{k n^{n-k-1}}
=\left(1-\frac1n\right)^{n-k-1}.
\]
For \(n-k=1\), the unique nonroot is necessarily a leaf and the same expression equals one. For \(k=n\), there are no leaves. Summation over all nonroots yields the formula.

**3. Exact strict sign.** Define \(g_n(k)=(n-k)q_n^{n-k-1}\) for \(0\le k\le n\), with the natural zero at \(k=n\). Direct subtraction gives
\[
g_n(k+1)-g_n(k)=-\frac{k}{n}q_n^{n-k-2},\qquad 0\le k<n.
\]
For every \(k\ge3\) this is strictly negative. For independent copies \(K_n,K_n'\), the covariance identity
\[
2\operatorname{Cov}(K_n,g_n(K_n))
=\mathbb E[(K_n-K_n')(g_n(K_n)-g_n(K_n'))]
\]
is therefore strictly negative when the support has at least two values, namely for \(n\ge4\). The tower property identifies it with \(\operatorname{Cov}(K_n,L_n)\).

**4. Half-normal cycle limit and moment control.** For \(k=O(\sqrt n)\), uniformly on bounded rescaled intervals,
\[
\log b_{n,k}=-\frac{k(k-1)}{2n}+O\!\left(\frac{k^3}{n^2}\right).
\]
Moreover \(0\le b_{n,k}\le\exp[-k(k-1)/(2n)]\), and \(Z_n/\sqrt n\to\sqrt{\pi/2}\). The sum is a Riemann sum, and the displayed bound supplies Gaussian domination. It follows that \(K_n/\sqrt n\) converges in distribution to \(S\), with convergence of every fixed positive moment.

**5. Quadratic regression and covariance constant.** The exact differences in Step 3 telescope to
\[
g_n(k)-g_n(0)=-\frac1n\sum_{j=0}^{k-1}j q_n^{n-j-2}.
\]
For \(k/\sqrt n\to s\ge0\), the right side tends to \(-s^2/(2e)\), while \(g_n(0)-n/e\to1/(2e)\). The convergence is uniform for bounded \(s\). Since \(q_n^{n-j-2}\le2\) for \(0\le j<n\) and \(n\ge2\), the absolute value of the telescoping sum is bounded by \(k^2/n\). The moment control in Step 4 consequently permits passage to expectations and products with \(K_n/\sqrt n\). Thus
\[
\lim_{n\to\infty}\frac{\operatorname{Cov}(L_n,K_n)}{\sqrt n}
=-\frac1{2e}\operatorname{Cov}(S^2,S).
\]
Finally \(\mathbb ES=\sqrt{2/\pi}\), \(\mathbb ES^2=1\), and \(\mathbb ES^3=2\sqrt{2/\pi}\), giving the claimed constant.

## Verification

The standalone Python 3 script `verify_unicyclic.py` performs exhaustive independent edge-set enumeration of all labeled simple connected unicyclic graphs on \(3\le n\le7\). It directly peels degree-one vertices to locate the cycle, then checks the predicted cycle-length counts and exact conditional leaf means. It also verifies strict monotonicity and negative covariance in exact rational arithmetic for \(4\le n<75\), and checks the finite-difference identity. The current run passed 2,738 exact assertions. Numerical evaluations of the normalized covariance at orders 80, 300, 1000, 3000 and 10000 approach the predicted \(-0.14676266317\). All limiting statements rest on the proof above, not on finite computations.

Run with `python3 verify_unicyclic.py` using the Python standard library only.

## Relationship to prior work

Kolchin's *Random Graphs* (1999), §1.7, gives the classical cycle-rooted-forest framework and enumeration for unicyclic graph families. Janson (2003) studies cycle-length and component-size point processes in sparse random graphs near criticality; his graph ensemble and observables differ from the present conditionally uniform connected model. Ben-Naim and Krapivsky (2004) obtain unicyclic component-size laws in an evolving random multigraph. These works supply structural motivation and related enumeration machinery. The assessed finding is the finite strictly decreasing leaf regression and its quadratic square-root-scale law, not the classical unicyclic count or half-normal cycle limit alone. Known rooted-forest formulas make parts of the derivation short; a prior unlocated joint leaf–cycle generating function could still implicitly imply the result.

## Limitations

This is a self-review, not an independent audit. The claim concerns a conditional first moment, its sign implication and the specified asymptotic limits; it does not assert a conditional leaf-count distribution, a central limit theorem for leaves, independence of leaves and cycle length, or optimal uniform error bounds. Older unlocated bivariate enumeration work may affect historical priority.

## References

- V. F. Kolchin, *Random Graphs*, Cambridge University Press, 1999, §1.7, ISBN 0-521-44081-5.
- S. Janson, “Cycles and Unicyclic Components in Random Graphs,” *Combinatorics, Probability and Computing* 12 (2003), 27–52, DOI: https://doi.org/10.1017/S0963548302005412 (online January 28, 2003).
- E. Ben-Naim and P. L. Krapivsky, “Unicyclic Components in Random Graphs,” arXiv:cond-mat/0403453, first posted March 18, 2004, https://arxiv.org/abs/cond-mat/0403453.
