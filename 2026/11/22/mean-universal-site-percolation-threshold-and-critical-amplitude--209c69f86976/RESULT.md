# Mean-universal site-percolation threshold and critical amplitude on grandparent graphs

## Finding
Let \(T\) be a Bienaymé–Galton–Watson rooted tree with offspring variable \(X\in\mathbb Z_{\ge0}\), \(1<m=\mathbb EX<\infty\), and generating function \(\phi\). Form its *grandparent graph* by adjoining to each parent–child edge an edge between every vertex and its grandparent. Retain each vertex independently with probability \(p\in[0,1]\), with all graph edges between retained vertices present. Write \(\mathcal C_o\) for the retained connected component of the original root, defined to be empty when the root is not retained.

Define
\[
R_m(p)=mp+m^2p(1-p),\qquad
q_m=\frac{m+1-\sqrt{(m+1)^2-4}}{2m}.
\]
Then the critical probability for \(\mathbb P(|\mathcal C_o|=\infty)>0\) is **exactly** \(q_m\), for every such offspring distribution: the root cluster is finite almost surely at and below \(q_m\), and infinite with positive probability above it. This contrasts with the distribution-sensitive *bond*-percolation threshold on the same random graph.

For \(0<p<q_m\), the conditional root-cluster susceptibility is exactly
\[
\mathbb E[|\mathcal C_o|\mid o\text{ retained}]=\frac{1}{1-R_m(p)}.
\]
The expectation is infinite at criticality, despite almost-sure finiteness. If \(\eta=\mathbb E[X(X-1)]<\infty\), then the probability of an infinite root cluster conditioned on retention obeys the sharp near-critical law
\[
\mathbb P(|\mathcal C_o|=\infty\mid o\text{ retained})
=K_{m,\eta}(p-q_m)+o(p-q_m),\qquad p\downarrow q_m\text{ from above},
\]
where
\[
K_{m,\eta}=\frac{2\left[m+m^2(1-2q_m)\right]}
{\eta\left[m(1-q_m)q_m^2+m^{-2}\right]}>0.
\]
Thus the threshold depends *only* on the offspring mean, whereas the leading survival amplitude also depends on the second factorial moment. The unconditional probability has amplitude \(q_m K_{m,\eta}\).

## Assumptions and scope
The rooted tree is locally finite almost surely and offspring counts at distinct vertices are independent with common law \(X\). Every vertex is retained independently of the tree and all other sites. This is undirected Bernoulli **site** percolation, not the independently open-edge (bond) model. The main threshold and susceptibility statements require only a finite mean \(m>1\). The linear critical-amplitude result additionally requires \(\eta<\infty\); for \(m>1\), necessarily \(\eta>0\). Root retention in conditional statements can equivalently be enforced deterministically.

## Proof
**1. A pathwise separator and a two-type genealogy.** For a vertex \(v\), the unique ancestral tree path from the root to \(v\) meets the root's retained cluster precisely when the root and \(v\) are retained and no two consecutive intermediate ancestral vertices are both deleted. Sufficiency follows by jumping over any isolated deleted ancestor on a grandparent edge. For necessity, two consecutive missing vertices separate the descendant subtree from the retained root: any graph edge crossing that pair would have to span at least three original tree edges, while every grandparent-graph edge spans at most two. Detours into side branches cannot bridge this separator.

Condition on retention of the root. Class \(A\) consists of the retained vertices connected to the root; class \(B\) consists of absent children of class-\(A\) vertices, serving as one-generation bridges. Every \(A\) vertex has \(X\) children, each independently a new \(A\) with probability \(p\) or a \(B\) with probability \(1-p\). Every \(B\) vertex has \(X\) children, each independently a new \(A\) with probability \(p\) or inactive otherwise. The two-type process reproduces on disjoint original subtrees. Its offspring generating functions are exactly
\[
G_A(x,y)=\phi(px+(1-p)y),\qquad
G_B(x,y)=\phi(px+1-p).
\]
The genealogy survives exactly when the retained root component is infinite, since \(B\) individuals cannot give birth to \(B\) individuals, and each vertex has finitely many children almost surely.

**2. Scalar survival equation and the exact threshold.** Write \(h_p\) and \(g_p\) for survival probabilities starting with one \(A\) and one \(B\). With \(f(s)=1-\phi(1-s)\), extinction equations become
\[
g_p=f(ph_p),\qquad h_p=f(ph_p+(1-p)g_p).
\]
Consequently \(h_p\) is the largest fixed point in \([0,1]\) of
\[
h=H_p(h):=f\big(ph+(1-p)f(ph)\big).
\]
For \(p\in(0,1)\), \(H_p\) is increasing and strictly concave because \(m>1\) implies \(\mathbb P(X\ge2)>0\); also \(H_p(0)=0\), \(H_p(1)<1\), and
\[
H_p'(0)=m[p+(1-p)mp]=R_m(p).
\]
The concavity/fixed-point criterion therefore yields \(h_p>0\) exactly when \(R_m(p)>1\), and \(h_p=0\) when \(R_m(p)\le1\). The quadratic \(R_m(p)-1\) has precisely one zero in \((0,1)\): \(q_m\), while \(R_m(1)=m>1\). This proves the classification, including extinction at the boundary. At \(p=0\) the component is empty; at \(p=1\) it agrees with the Galton–Watson tree, which survives with positive probability.

**3. Exact susceptibility and level profile.** Let \(s_n\) be the probability that a specified vertex at ancestral depth \(n\) belongs to the retained root cluster, conditional on root retention and on the original tree. The separator criterion gives
\[
s_0=1,\quad s_1=p,\quad s_n=p s_{n-1}+p(1-p)s_{n-2}\quad(n\ge2).
\]
Explicitly,
\[
s_n=\sum_{j=0}^{\lfloor n/2\rfloor}\binom{n-j}{j}p^{n-j}(1-p)^j.
\]
By independence of branching and retention, the expected connected population at depth \(n\), conditionally on root retention, is \(a_n=m^n s_n\). Hence
\[
\sum_{n\ge0}a_n z^n=\frac{1}{1-mpz-m^2p(1-p)z^2}.
\]
Monotone convergence at \(z=1\) gives the exact stated susceptibility for \(R_m(p)<1\); when \(R_m(p)\ge1\), the positive-coefficient series diverges. At \(p=q_m\) this coexists with almost-sure extinction by Step 2.

**4. Sharp near-critical amplitude.** Assume \(\eta<\infty\). As \(s\downarrow0\),
\[
f(s)=ms-\tfrac12\eta s^2+o(s^2).
\]
Uniformly for \(p\) near \(q_m\), this gives
\[
H_p(h)=R_m(p)h-\tfrac12\eta\{m(1-p)p^2+[p(1+m(1-p))]^2\}h^2+o(h^2).
\]
Strict concavity and uniqueness of the zero fixed point at criticality show \(h_p\to0\) as \(p\downarrow q_m\). Using \(m q_m[1+m(1-q_m)]=1\) and \(R_m'(q_m)=m+m^2(1-2q_m)>0\), division by the positive solution \(h_p\) yields
\[
\frac{h_p}{p-q_m}\longrightarrow
\frac{2R_m'(q_m)}{\eta[m(1-q_m)q_m^2+m^{-2}]}=K_{m,\eta}.
\]
Independence of root retention multiplies this by \(p\), yielding the unconditional amplitude. Each step uses only the stated finite-moment assumptions.

## Verification
A standalone Python 3 standard-library checker verifies the ancestral separator statement against full breadth-first graph connectivity for all \(2^{14}=16384\) site assignments (with root retained) on the 15-vertex depth-three binary tree; this checks all 15 vertices per assignment. The same package checks Fibonacci-word formulas, exact expected-level recurrences with rational arithmetic, and high-precision supercritical fixed points for two offspring laws with the same mean \(m=2\) but different \(\eta\). It reports 245892 passed assertions. These computations are diagnostics; the infinite and near-critical conclusions are proved analytically above.

## Relationship to prior work
Ménard and Sénizergues (arXiv:2611.09762v1, posted November 6, 2026) study *bond* percolation on the same grandparent graphs, where independent edge states make the critical value depend on the entire offspring law. They explicitly analyze that distribution dependence; the independent-site model, the mean-only threshold, and its susceptibility/critical amplitude are not assertions of their inspected main theorems. de Lima, Szabó and Valesin (2023) study *oriented bond* percolation on regular trees with short and long edges, a different stochastic mechanism. Standard multitype branching and near-critical theory supplies general mathematical tools; the specific graph-separator reduction and the closed formulas above are the proposed model-specific contributions.

## Limitations
The law is annealed over both random tree and retained sites; no new quenched threshold theorem is asserted. The near-critical linear law requires \(\eta<\infty\); no corresponding amplitude is asserted for infinite-second-moment offspring. The resulting one-parameter threshold is not asserted for other kinds of tree powers, dependence between sites, or independent-edge percolation. No independent mathematical verification has been performed, and unindexed equivalent results remain possible.

## References
1. L. Ménard and D. Sénizergues, *Percolation on grandparent graphs of Bienaymé trees*, arXiv:2611.09762v1 (public source November 6, 2026), https://arxiv.org/abs/2611.09762.
2. B. N. B. de Lima, R. Szabó and D. Valesin, *Multirange percolation on oriented trees: Critical curve and limit behavior*, Random Structures & Algorithms 62 (2023), 519–541, https://doi.org/10.1002/rsa.21104 (first online June 24, 2022).
3. M. P. Quine, *The multitype Galton–Watson process with rho near 1*, Advances in Applied Probability 4 (1972), 429–452, https://doi.org/10.2307/1425989.
