# Opposite leaf responses to matching and star deletions in Cayley-tree hosts

## Finding

The expected number of leaves of a uniform spanning tree is sensitive not only to the **number** of missing edges, but also to how those edges intersect. The following gives a strict, all-parameter sign reversal between two canonical ways of deleting the same number of edges from a complete graph.

For an integer \(n\ge4\), write \(K_n\) for the complete graph on \(n\) labeled vertices. Let \(M_r\) denote any matching of size \(r\), and let \(S_r\) denote any star with \(r\) edges. Put
\[
G^M_{n,r}=K_n\setminus E(M_r),\qquad G^S_{n,r}=K_n\setminus E(S_r).
\]
For a connected finite graph \(G\), write \(L(G)\) for the number of degree-one vertices in a uniformly chosen spanning tree of \(G\). Define the Cayley-tree reference mean
\[
B_n=n\left(1-\frac1n\right)^{n-2}.
\]
**Theorem.** For all integers \(n\ge4\) and \(2\le r\le\lfloor n/2\rfloor\), one has
\[
\boxed{\mathbb E L(G^M_{n,r})<B_n<\mathbb E L(G^S_{n,r}).}
\]
More precisely, with \(m_{n,r}=\mathbb E L(G^M_{n,r})\) and \(s_{n,r}=\mathbb E L(G^S_{n,r})\),
\[
\boxed{\frac{m_{n,r}}{B_n}=\left(1+\frac{2r}{n(n-3)}\right)\left(\frac{n(n-3)}{(n-1)(n-2)}\right)^r,}
\]
\[
\boxed{\frac{s_{n,r}}{B_n}=\frac1n\left(\frac n{n-1}\right)^r+\frac{n-1}n\left(\frac{n(n-2)}{(n-1)^2}\right)^r.}
\]
Both expressions equal \(1\) at \(r=1\) (an individual edge deletion leaves the expected leaf count unchanged). The star expression, and its strict greater-than-one conclusion, remain valid separately for \(2\le r\le n-2\); the matching expression requires \(r\le\lfloor n/2\rfloor\).

## Assumptions and scope

Every graph is finite, simple, undirected and unweighted. Spanning trees are sampled with equal probabilities among all labeled spanning trees of that graph. The two host graphs in the stated ranges are connected. The symbol \(\tau(G)\) denotes the spanning-tree count, with value zero for a disconnected graph. A vertex-deleted graph may be disconnected, in which case its term in the leaf identity vanishes. The result concerns **expectations**, not stochastic dominance of leaf-count distributions and not an extremal theorem over arbitrary missing-edge subgraphs.

## Proof

**1. A general leaf identity.** For any connected graph \(G\) and vertex \(v\), a spanning tree with \(v\) as a leaf is uniquely obtained by choosing a spanning tree of \(G-v\) and then one of \(\deg_G(v)\) edges incident to \(v\). Therefore
\[
\Pr(v\text{ is a leaf})=\frac{\deg_G(v)\,\tau(G-v)}{\tau(G)},\qquad
\mathbb E L(G)=\frac{\sum_{v\in V(G)}\deg_G(v)\tau(G-v)}{\tau(G)}.
\tag{1}
\]
If \(G-v\) is disconnected, both the leaf-event count and \(\tau(G-v)\) are zero; the same identity still holds.

**2. Tree counts for deleted matching and star.** The Laplacian of \(K_n\) is \(nI-J\); deleting an edge with endpoints \(u,v\) subtracts the rank-one Laplacian \((e_u-e_v)(e_u-e_v)^\top\). The \(r\) edge-vectors of a matching are mutually orthogonal, each of squared norm \(2\); its deleted-edge Laplacian has nonzero eigenvalues \(2\) with multiplicity \(r\). The deleted-edge Laplacian of \(S_r\) has nonzero eigenvalues \(r+1\) once and \(1\) with multiplicity \(r-1\). Both annihilate the constant vector. Kirchhoff's matrix-tree theorem thus gives
\[
\tau(G^M_{n,r})=n^{n-r-2}(n-2)^r,\tag{2}
\]
\[
\tau(G^S_{n,r})=n^{n-r-2}(n-1)^{r-1}(n-r-1).\tag{3}
\]
For \(r=0\), both reduce to Cayley's \(n^{n-2}\), interpreted separately. Formula (3) holds for \(1\le r\le n-2\), and formula (2) for \(1\le r\le\lfloor n/2\rfloor\).

**3. Leaf expectations via vertex deletion.** In \(G^M_{n,r}\), precisely \(2r\) vertices have degree \(n-2\); deleting one leaves \(G^M_{n-1,r-1}\). The other \(n-2r\) vertices have degree \(n-1\); deleting one leaves \(G^M_{n-1,r}\). Consequently (1) and (2) give
\[
\mathbb E L(G^M_{n,r})=
\frac{2r(n-2)\tau(G^M_{n-1,r-1})+(n-2r)(n-1)\tau(G^M_{n-1,r})}{\tau(G^M_{n,r})}.
\tag{4}
\]
At the borderline \(n=2r\), there are no unmatched vertices, so the zero-coefficient second term in (4) is omitted; this avoids invoking an impossible size-\(r\) matching on \(n-1\) vertices. Where the reduced missing-edge count is zero, the complete-graph tree count is used. Simplifying (4) gives the first boxed normalized formula.

For \(G^S_{n,r}\), partition vertices into the star center (one vertex of degree \(n-r-1\)), the \(r\) forbidden-edge endpoints (degree \(n-2\)), and the remaining \(n-r-1\) vertices (degree \(n-1\)). The three vertex-deleted graphs are, respectively, \(K_{n-1}\), \(G^S_{n-1,r-1}\) and \(G^S_{n-1,r}\). Accordingly
\[
\begin{split}
\mathbb E L(G^S_{n,r})={}&\big[(n-r-1)(n-1)^{n-3}
+r(n-2)\tau(G^S_{n-1,r-1})\\
&+(n-r-1)(n-1)\tau(G^S_{n-1,r})\big]/\tau(G^S_{n,r}).
\end{split}\tag{5}
\]
When the reduced missing-star size is zero the corresponding graph is complete; when the reduced graph is disconnected, its tree count is zero. Substitution of (3), cancellation and grouping yield the second boxed normalized formula; this identity also follows by direct expansion of (5).

**4. Exact opposite signs.** Put \(a=n(n-3)/[(n-1)(n-2)]\), so \(0<a<1\). The matching ratio is \(a^r[1+r(a^{-1}-1)]\). The strict Bernoulli inequality \((1+x)^r>1+rx\) for integers \(r\ge2\), \(x=a^{-1}-1>0\), shows this ratio is strictly less than \(1\).

Put \(b=n/(n-1)\), \(c=n(n-2)/(n-1)^2\); these are unequal positive numbers satisfying \(b/n+(n-1)c/n=1\). Strict convexity of \(x\mapsto x^r\) for \(r\ge2\) gives
\[
\frac1n b^r+\frac{n-1}n c^r>
\left(\frac1n b+\frac{n-1}n c\right)^r=1.
\]
For \(r=1\) both expressions equal \(1\). Finally, Prüfer coding gives \(\Pr_{K_n}(v\text{ leaf})=(1-1/n)^{n-2}\), establishing the stated \(B_n\). This proves the theorem.

## Verification

The accompanying standalone Python standard-library program `check.py` reconstructs graph Laplacian cofactors with a fraction-free Bareiss determinant, evaluates leaf expectations from individual vertex-deletion minors independently of the closed forms, enumerates spanning trees exhaustively for small instances, and compares with both formulas as exact fractions. Running `python check.py` produced `VERIFY_OK 181 exact assertions` for the checked parameter ranges. This is a finite consistency check, not a substitute for the all-integer proof above.

## Relationship to prior work

Kirchhoff's matrix-tree theorem and Cayley's/Prüfer tree enumeration are standard inputs, rather than discoveries. Rapoport (2023) obtains general explicit joint degree probabilities for uniform spanning trees using fermionic and transfer-current methods; such general formulas imply that arbitrary leaf probabilities are in principle computable, but do not state the two exact graph-family responses or their opposite all-parameter signs. Fita Sanmartín, Schnörr and Hamprecht (2024) develop general node-degree moment formulas for random spanning trees, with a degree-distribution polynomial; the statistic here is the **count of degree-one vertices**, not the expected vertex degree. The specific contribution is the paired graph-deletion comparison and strict sign classification, derived with explicit rank-\(r\) Laplacian spectra and convexity.

## Limitations

This result does not prove that the two deletion patterns globally extremize expected leaves among all graphs with \(r\) missing edges, nor does it establish a stochastic ordering of the corresponding random leaf counts. Literature and database checks are not a proof of historical priority; further independent priority review may reveal an earlier equivalent statement. No independent mathematical audit has been performed.

## References

- Kirchhoff's matrix-tree theorem (classical): spanning-tree counts via Laplacian cofactors.
- Cayley's formula and Prüfer encoding (classical): uniform spanning trees of the complete graph.
- Alan Rapoport, *Correlations in uniform spanning trees: a fermionic approach*, arXiv:2312.14992v1, first publicly posted 2023-12-22; https://arxiv.org/html/2312.14992v1.
- Enrique Fita Sanmartín, Christoph Schnörr, Fred A. Hamprecht, *Expectation and Variance of the Degree of a Node in Random Spanning Trees*, arXiv:2409.13472v1, first publicly posted 2024-09-20; https://arxiv.org/html/2409.13472v2.
