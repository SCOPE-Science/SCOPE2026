# A strict leaf–split covariance dichotomy for uniform labeled trees

## Finding

Let \(T_n\) be uniformly distributed over all \(n^{n-2}\) trees on the labeled vertex set \([n]\), with \(n\ge4\). Let \(L_n\) count vertices of degree one. For \(1\le k\le\lfloor n/2\rfloor\), let \(B_{n,k}\) count edges whose deletion separates a component with exactly \(k\) vertices, taking the smaller component when the sizes differ. An equal split is counted **once per edge**, not twice.

Define
\[
\ell_n=n\left(1-\frac1n\right)^{n-2},\qquad
b_{n,k}=\frac{\binom nk\,k^{k-1}(n-k)^{n-k-1}}{n^{n-2}(1+\mathbf1_{\{2k=n\}})},
\]
and
\[
g(1)=1,\qquad g(m)=m\left(1-\frac1m\right)^{m-1}\quad(m\ge2).
\]
Then \(\mathbb E L_n=\ell_n\), \(\mathbb E B_{n,k}=b_{n,k}>0\), and, **simultaneously for all admissible \(n,k\)**,
\[
\boxed{\operatorname{Cov}(L_n,B_{n,k})=b_{n,k}\,[g(k)+g(n-k)-\ell_n].}
\]
The exact sign classification is
\[
\boxed{\operatorname{Cov}(L_n,B_{n,1})=\operatorname{Var}(L_n)>0,\qquad
\operatorname{Cov}(L_n,B_{n,k})<0\quad(2\le k\le\lfloor n/2\rfloor).}
\]
In particular, a pendant-edge split is positively associated with leafiness, but **every non-pendant vertex split size** is negatively associated with leafiness, with no other exceptions or internal sign transitions.

There is also a size-independent macroscopic conditional effect. If \(k=k(n)\) and \(k\to\infty\) and \(n-k\to\infty\), then for a prescribed \(k\)-vertex subset \(S\), conditioned on exactly one tree edge crossing from \(S\) to its complement,
\[
\mathbb E[L_n\mid\text{exactly one crossing edge at }S]-\mathbb E L_n
\longrightarrow -\frac1{2e}.
\]
The sign dichotomy and conditional limit belong to the same exact split-conditioning identity, not to separate assertions about alternative random-tree models.

## Assumptions and scope

The underlying tree is uniformly labeled, unrooted and unweighted; all \(n^{n-2}\) possibilities have equal probabilities. A split is measured by the number of **vertices** in a component after removing an edge, not by the number of leaves on that side. A tree edge has only one split, even when both components have equal size. For \(n\ge4\), \(B_{n,1}=L_n\). The case \(n=3\) is deterministic in leaf count and deliberately excluded from the strict-sign claim. No assumption of independent node degrees or independent edge events is used.

## Proof

**1. A specified split and its probability.** Fix \(S\subset[n]\) with \(|S|=k\), and let \(A_S\) be the event that the tree has exactly one edge between \(S\) and \(S^c\). On \(A_S\), the induced subgraphs on \(S\) and \(S^c\) are trees. Cayley's counting formula gives respectively \(k^{k-2}\) and \((n-k)^{n-k-2}\) choices (with the one-vertex case interpreted as one tree), and the joining edge has \(k(n-k)\) choices. Therefore
\[
\mathbb P(A_S)=\frac{k^{k-1}(n-k)^{n-k-1}}{n^{n-2}}.
\]
Each qualifying edge contributes exactly one set \(S\) if \(2k<n\), and two complementary sets if \(2k=n\). Summing the indicators of \(A_S\) and dividing by \(1+\mathbf1_{\{2k=n\}}\) proves \(\mathbb E B_{n,k}=b_{n,k}\).

**2. Conditional leaf count.** Under \(A_S\), the two induced trees are independently uniform labeled trees on their respective vertex sets, and the endpoints of the joining edge are independent uniform vertices of those sets. To verify this directly, every pair of internal trees and every pair of joining endpoints produces exactly one original tree in \(A_S\).

For a component of size \(m\ge2\), the probability that a fixed vertex is an internal-tree leaf is \((1-1/m)^{m-2}\) by the Prüfer-code representation. To remain a leaf of the joined tree, the vertex must additionally **not** be the uniformly selected joining endpoint, an independent event with probability \((m-1)/m\). Thus its probability of remaining a leaf is \((1-1/m)^{m-1}\). The expected surviving leaf contribution of the component is \(g(m)\). For a singleton component the new degree is exactly one, giving \(g(1)=1\). Consequently,
\[
\mathbb E[L_n\mid A_S]=g(k)+g(n-k).
\]
Unconditionally a specified vertex is absent from a length-\(n-2\) uniform Prüfer code with probability \((1-1/n)^{n-2}\), proving \(\mathbb E L_n=\ell_n\). The identity
\[
\operatorname{Cov}(L_n,\mathbf1_{A_S})=\mathbb P(A_S)\bigl(\mathbb E[L_n\mid A_S]-\ell_n\bigr)
\]
then proves the displayed exact covariance after summation.

**3. Uniform strict inequality for nontrivial splits.** We establish for every integer \(m\ge2\) the bound
\[
\boxed{g(m)<\frac{m+3/4}{e},}
\]
and for every integer \(n\ge2\) the bound
\[
\boxed{\ell_n>\frac{n+3/2}{e}.}
\]
Here is a direct analytic argument that proves the bounds for **all** integers rather than only numerically. Put \(x=1/m\in(0,1/2]\) and observe the absolutely convergent power series
\[
S(x)=1+\left(\frac1x-1\right)\log(1-x)
=\sum_{j\ge1}\frac{x^j}{j(j+1)}.
\]
The function \(S\) is strictly convex on \((0,1/2]\), whereas \(x\mapsto\log(1+3x/4)\) is strictly concave. Hence their difference
\(F(x)=\log(1+3x/4)-S(x)\) is strictly concave. It extends continuously to \(F(0)=0\), while
\[
F(1/2)=\log(11/4)-1>0,
\]
because \(e<11/4\). Concavity implies \(F(x)>0\) throughout \((0,1/2]\). It follows that
\[
\left(1-\frac1m\right)^{m-1}
=e^{-1+S(1/m)}<\frac1e\left(1+\frac{3}{4m}\right),
\]
proving the first bound.

For the second, put \(x=1/n\). Direct expansion yields
\[
1+\left(\frac1x-2\right)\log(1-x)
=\sum_{j\ge1}\left(\frac2j-\frac1{j+1}\right)x^j
>\frac{3x}{2}.
\]
All terms beyond the first are positive. Thus
\[
\left(1-\frac1n\right)^{n-2}>\frac1e e^{3/(2n)}
>\frac1e\left(1+\frac{3}{2n}\right),
\]
which proves the second bound. For \(k,n-k\ge2\), the two strict estimates combine to give
\[
g(k)+g(n-k)<\frac{n+3/2}{e}<\ell_n.
\]
Since \(b_{n,k}>0\), the nontrivial covariance is strictly negative.

For \(k=1\), the split count equals the number of leaves. Therefore the covariance equals \(\operatorname{Var}(L_n)>0\), because stars and paths have different numbers of leaves and both have positive probability whenever \(n\ge4\). This completes the entire sign classification.

**4. Universal conditional deficit.** The logarithmic series above gives the expansions
\[
g(m)=\frac m e+\frac1{2e}+O(m^{-1}),\qquad
\ell_n=\frac n e+\frac3{2e}+O(n^{-1}).
\]
If \(k\to\infty\) and \(n-k\to\infty\), substitution into the conditional expectation in Step 2 gives the asserted limit \(-1/(2e)\). For fixed \(k\ge2\), the analogous limit is
\[
\mathbb E[L_n\mid A_S]-\mathbb E L_n
\longrightarrow g(k)-\frac{k+1}{e}<0.
\]
These asymptotics are refinements of the same exact identity.

## Verification

The standalone standard-library Python program `verify.py` enumerates every Prüfer code for all orders \(2\le n\le8\), reconstructs the tree, counts leaves and every edge's smaller-side vertex count, and compares exact rational moments against the claimed formulas. The resulting exhaustive sample consists of 280,392 distinct labeled trees. It also checks the sign inequality by exact rational arithmetic for every admissible parameter pair with \(4\le n\le150\). Its run completed 11,014 exact equality/sign assertions without a failure. Exhaustive small-case verification is supplementary to, not a substitute for, the all-size proof in Steps 1–4.

Reproduction: `python3 verify.py`. Only Python's standard library is required.

## Relationship to prior work

Janson (2013, arXiv:1312.1211, especially the introduction, Examples 2.1–2.2 and the degree-covariance proof) develops fringe-subtree and additive-functional limit theory including uniformly labeled trees; it treats marginal leaf fluctuations and general rooted fringe counts. A rooted encoding of an unrooted edge split of size \(k\) can be expressed in terms of fringe-subtree sizes \(k\) and \(n-k\), so this framework is genuinely related. It does not state the finite unrooted vertex-split conditional leaf identity or the uniform strict sign dichotomy, and the general limit theorems alone do not imply the claimed all-parameter signs.

Fischer and Liebscher (2015, arXiv:1510.07882) study deterministic balance functionals of splits of **leaf sets** in phylogenetic trees, including extremal shapes. These are not the unrooted uniformly vertex-labeled Cayley model, nor the joint random leaf-count/vertex-split covariance. Meir and Moon (1970) consider random edge removals from uniformly labeled trees; the available bibliographic description concerns the number of cuts needed to isolate a root. Its full text was not inspected, so an implicit earlier special case remains a priority risk. No claim is made that a general combinatorial decomposition or any classical count is original.

## Limitations

Only covariance and its sign are classified. Negative covariance does not imply negative quadrant dependence, stochastic monotonicity, or conditional independence; no such claims are made. The result is specific to uniform labeled trees and to vertex-count splits, not general spanning-tree laws or phylogenetic leaf-set splits. Full historical-priority exhaustiveness is not established; an older equivalent expression or an immediate consequence of a more specialized joint generating function could affect novelty. The computational tests cover finite sizes, whereas the analytic proof establishes the infinite family.

## References

- S. Janson, *Asymptotic normality of fringe subtrees and additive functionals in conditioned Galton–Watson trees*, arXiv:1312.1211v1, publicly posted 2013-12-04. https://arxiv.org/abs/1312.1211
- M. Fischer and V. Liebscher, *On the Balance of Unrooted Trees*, arXiv:1510.07882v1, publicly posted 2015-10-27. https://arxiv.org/abs/1510.07882
- A. Meir and J. W. Moon, *Cutting down random trees*, J. Austral. Math. Soc. 11 (1970), 313–324. DOI:10.1017/S1446788700006698 (bibliographic description examined; full text not inspected).
- The classical Cayley formula and Prüfer-code representation are used as established counting tools.
