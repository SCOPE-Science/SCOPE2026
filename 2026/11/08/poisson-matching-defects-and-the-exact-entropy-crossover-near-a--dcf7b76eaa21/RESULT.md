# Poisson matching defects and the exact entropy crossover near a complete geometric circle graph

## Finding

Fix \(\lambda>0\). Let \(X_1,\ldots,X_n\) be independent uniform points of the unit circle \(\mathbb T=\mathbb R/\mathbb Z\). Join distinct labels \(i,j\) when their circular distance \(d(X_i,X_j)\) is at most \(r_n=(1-\lambda/n^2)/2\), for \(n\) large enough that \(0<r_n<1/2\). Write \(D_n\) for the **missing-edge graph**, i.e. the complement of this labeled hard geometric graph, and \(M_n=|E(D_n)|\). Shannon entropies are in bits.

**Theorem (near-completeness critical window).** The number of missing edges converges in law to \(\operatorname{Pois}(\lambda/2)\). With probability \(1-O_\lambda(1/n)\), all missing edges are pairwise vertex-disjoint, so \(D_n\) is a matching. Moreover, as a random labeled graph, \(D_n\) has total-variation distance tending to zero from the independent-edge graph \(G(n,\lambda/n^2)\), and the **exact constant-order entropy expansion** is

\[
\boxed{H(D_n)=H(G_n)=\lambda\log_2n+\frac{\lambda}{2}\log_2\frac{e}{\lambda}+o(1).}
\]

Here \(G_n\) denotes the original nearly complete geometric graph, and its entropy equals that of its complement. In particular, the defect count has a nontrivial Poisson limit precisely at the natural \(n^{-2}\) proximity scale to maximal connection radius, yet geometrically dependent missing edges have the same entropy through the constant term as independent rare edges.

## Assumptions and scope

The circle has circumference one; circular distance is \(d(x,y)=\min_{k\in\mathbb Z}|x-y+k|\). The parameter \(\lambda>0\) is fixed and independent of \(n\); \(n>\sqrt\lambda\) ensures the connection radius lies in the stated interval. Positions are i.i.d. uniform and the graph is labeled. The claim concerns \(r_n=1/2-\lambda/(2n^2)\), not any fixed radius or an arbitrary varying-radius regime. An edge of \(D_n\) occurs exactly when one point lies in the open antipodal arc of length \(q_n=\lambda/n^2\) centered at the other; interval endpoints have zero probability.

## Proof

**1. Edge probabilities and matching concentration.** Every unordered pair is a defect with probability \(q_n=\lambda/n^2\). For two distinct pairs sharing exactly one vertex, their defect indicators are independent: condition on the common point; the other two points are independent uniform, and each belongs to its prescribed antipodal arc with probability \(q_n\). Disjoint pairs are also independent. Thus any two distinct defect indicators are independent. In particular,

\[
\mathbb E M_n=\binom n2 q_n=\frac\lambda2(1-1/n),\qquad
\mathbb E M_n^2=(\mathbb EM_n)^2+\binom n2q_n(1-q_n)=O_\lambda(1).
\]

Let \(A_n\) be the event that the defect graph is a matching. The expected number of pairs of defect edges sharing a vertex is exactly

\[
n\binom{n-1}{2}q_n^2=O_\lambda(n^{-1}).
\]

Consequently \(\Pr(A_n^c)=O_\lambda(1/n)\), and Cauchy--Schwarz implies \(\mathbb E[M_n\mathbf1_{A_n^c}]=O_\lambda(n^{-1/2})\).

**2. Poisson limit with all moments.** For any integer \(k\ge1\), expand the factorial moment \(\mathbb E(M_n)_k\) over ordered \(k\)-tuples of distinct potential edges. If their edge union is a forest of \(k\) disjoint single edges, there are \((n)_{2k}/2^k\) such ordered tuples and their joint defect probability is exactly \(q_n^k\). Any other union graph \(F\) has \(v\) nonisolated vertices and \(c\) connected components, with \(v\ge2c+1\). Joint occurrence of all its defect edges implies occurrence along any spanning forest, which has \(v-c\) edges. Expose each tree from a root outward: after the parent has been revealed, the child lies in its antipodal arc with conditional probability \(q_n\), giving the bound \(q_n^{v-c}\). For fixed \(k\), the number of labeled instances of each such edge-union type is \(O_k(n^v)\), so their aggregate contribution is \(O_{k,\lambda}(n^{2c-v})=O_{k,\lambda}(n^{-1})\). Hence

\[
\mathbb E(M_n)_k=\frac{(n)_{2k}}{2^k}q_n^k+O_{k,\lambda}(n^{-1})
\longrightarrow (\lambda/2)^k.
\]

The factorial-moment criterion proves \(M_n\Rightarrow Z\sim\operatorname{Pois}(\lambda/2)\). It also gives convergence of all fixed moments and, in particular, uniform bounds for arbitrarily high fixed moments. On the countable state space, this implies total-variation convergence of the count laws.

**3. Exchangeability and the complete matching law.** Conditional on \(M_n=m\) and \(A_n\), label exchangeability implies that \(D_n\) is exactly uniform over the

\[
N(n,m)=\frac{n!}{(n-2m)!\,2^m m!}
\]

matchings with \(m\) edges (for \(0\le m\le\lfloor n/2\rfloor\)). The independent-edge graph \(G(n,q_n)\) has the same conditional law and satisfies the same matching-probability estimate. Both edge-count laws converge to the same Poisson distribution, so their laws restricted to matching graphs approach one another in total variation; the nonmatching probabilities vanish. Thus \(d_{\mathrm{TV}}(D_n,G(n,q_n))\to0\).

**4. Entropy survives this approximation through the constant term.** Since \(A_n\) and \(M_n\) are functions of \(D_n\), the chain rule and the exact matching law give

\[
H(D_n)=H(M_n,A_n)+\mathbb E[\mathbf1_{A_n}\log_2 N(n,M_n)]
+\Pr(A_n^c)H(D_n\mid M_n,A_n^c).
\]

The last term lies between zero and \(2\log_2n\,\mathbb E[M_n\mathbf1_{A_n^c}]=o(1)\), since there are at most \(n^{2m}\) graphs with \(m\) edges. Also \(H(M_n,A_n)=H(M_n)+H(A_n\mid M_n)=H(M_n)+o(1)\), because \(H(A_n\mid M_n)\le h_2(\Pr(A_n^c))\to0\). For \(m\le n/4\),

\[
\log_2N(n,m)=2m\log_2n-m-\log_2(m!)+O(m^2/n).
\]

The uniformly bounded high moments of \(M_n\), together with \(\Pr(A_n^c)=O(1/n)\) and Cauchy--Schwarz, justify averaging this formula and discarding the tail \(m>n/4\), yielding

\[
\mathbb E[\mathbf1_{A_n}\log_2N(n,M_n)]
=2\mathbb E M_n\log_2n-\mathbb E M_n-\mathbb E\log_2(M_n!)+o(1).
\]

The integer count laws converge to \(Z\) in total variation, with uniformly bounded moments of all fixed orders, so entropy and the expectations of \(\log_2(M_n!)\) converge as well: \(H(M_n)\to H(Z)\) and \(\mathbb E\log_2(M_n!)\to\mathbb E\log_2(Z!)\). Finally, \(2\mathbb E M_n=\lambda+O_\lambda(n^{-1})\), and the Poisson identity

\[
H(Z)=\frac\lambda2\log_2e-\frac\lambda2\log_2(\lambda/2)+\mathbb E\log_2(Z!)
\]

reduces the entropy expansion to \(\lambda\log_2 n+(\lambda/2)\log_2(e/\lambda)+o(1)\), as asserted.

## Verification

`CHECK.py` performs finite exact-rational checks on uniform rational grids for the antipodal-arc probability and conditional pairwise independence, and verifies the exact matching enumerator. It prints the number of checked assertions. No finite check proves the infinite limit; Steps 1–4 above provide the proof. Run with `python CHECK.py` (Python standard library only).

## Relationship to prior work

The motivating source, Vippathalla, Coon and Badiu, *On the Entropy of a Random Geometric Graph* (arXiv:2601.10778, publicly released 2026-01-15), treats fixed distance thresholds, primarily giving \(n\log n\)-scale entropy bounds. The subsequent *Universal vertices and effective dimension in geometric-graph entropy* (anonymous, Evidence Press release 2026-10-27, version 1.1.0 candidate, DOI:10.5281/zenodo.23686157) proves an \(O(n)\) correction for fixed radii but explicitly lists shrinking radii as open; its theorems do not yield this \(O(\log n)\) entropy or the exact constant for \(r_n\uparrow1/2\). Penrose's *Inhomogeneous random graphs, isolated vertices, and Poisson approximation* (2018) provides general Poisson techniques for edge counts; the elementary Poisson mechanism itself is not claimed new. The focused contribution here is the combined **matching-valued law and exact constant-term graph entropy** in the geometry-dependent near-completeness window. In a similar sparse independent-edge graph, the same entropy expansion follows by a binary-entropy calculation, but that calculation is not directly valid for geometric edge dependence.

## Limitations

The finding assumes a fixed \(\lambda>0\), i.i.d. uniform locations, the one-dimensional circle and the exact scaling \(1-2r_n=\lambda/n^2\). It does not describe intermediate scaling windows, nonuniform sampling, higher-dimensional spaces or an efficient encoder. Exact constant-term entropy requires more than total-variation convergence on growing alphabets, which is why the matching entropy bound is included. A bounded literature/record search cannot establish global priority; related general Poisson-approximation principles may cover parts of the distributional assertion.

## References

- P. K. Vippathalla, J. P. Coon, M.-A. Badiu, *On the Entropy of a Random Geometric Graph*, arXiv:2601.10778 (first public 2026-01-15), https://arxiv.org/html/2601.10778v1 .
- Anonymous, *Universal vertices and effective dimension in geometric-graph entropy*, Evidence Press, release 2026-10-27, DOI:10.5281/zenodo.23686157, https://www.evidencepress.org/releases/geometric-graph-entropy/ (unrefereed candidate).
- M. D. Penrose, *Inhomogeneous random graphs, isolated vertices, and Poisson approximation*, Journal of Applied Probability (2018), https://doi.org/10.1017/jpr.2018.9 .
- M.-A. Badiu, J. P. Coon, *Structural Complexity of One-Dimensional Random Geometric Graphs*, arXiv:2107.13495, https://arxiv.org/html/2107.13495v2 .
