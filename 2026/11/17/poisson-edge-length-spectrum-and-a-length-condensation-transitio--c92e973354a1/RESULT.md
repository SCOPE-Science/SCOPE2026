# Poisson edge-length spectrum and a length-condensation transition in partial permutohedra

## Finding
For integers \(m\ge 2\) and \(n\ge m\), set
\[
\mathcal P(m,n)=\operatorname{conv}\{x\in\{0,1,\ldots,n\}^{m}:\text{the positive entries of }x\text{ are distinct}\}.
\]
Write \(F_k=m!/(m-k)!\), \(N_m=\sum_{k=0}^{m}F_k\), \(d=n-m\), and \(E_s=\sum_{j=0}^{s}1/j!\). Its full Euclidean one-skeleton contains precisely the following disjoint classes of edges:

- \(A_m=((m-2)N_m+2)/2\) edges of length \(\sqrt2\), obtained by exchanging consecutive positive entries;
- for each \(j\in\{1,\ldots,m\}\), exactly \(m!/(j-1)!\) edges of integer length \(d+j\), obtained by inserting or deleting the smallest positive entry.

In particular the number of edges is \(mN_m/2\), independent of \(n\ge m\), but the total Euclidean length is exactly
\[
\mathscr L_{m,n}=\frac{\sqrt2}{2}\big((m-2)N_m+2\big)
+m!\big((d+1)E_{m-1}+E_{m-2}\big).
\]
Let \(\pi_{m,n}\) denote the proportion of \(\mathscr L_{m,n}\) contributed by insertion/deletion edges. If \(d/m\to c\in[0,\infty]\) as \(m\to\infty\), then
\[
\pi_{m,n}\longrightarrow \frac{2c}{\sqrt2+2c},
\]
with the value \(1\) when \(c=+\infty\). This is a length-condensation transition: insertion/deletion edges always form only \(2/m+O(1/(mN_m))\) of the edge *count*, yet occupy positive limiting total Euclidean length when \(n-m\) grows linearly with \(m\). For \(d=o(m)\), the sharper estimate is \(\pi_{m,n}\sim \sqrt2(d+2)/m\).

Conditionally on choosing an insertion/deletion edge uniformly by *count*, its length minus \(d\) has exactly the distribution of \(1+Y\), conditional on \(Y\le m-1\), where \(Y\sim\operatorname{Poisson}(1)\). Its total-variation distance from the unconditioned \(1+\operatorname{Poisson}(1)\) law equals \(\Pr(Y\ge m)\). For fixed \(d\), conditionally sampling an insertion/deletion edge proportionally to its length instead yields the limiting mixture \(\frac{d+1}{d+2}(1+Y)+\frac1{d+2}(2+Y)\) (mixture of distributions, with \(Y\sim\operatorname{Poisson}(1)\)).

## Assumptions and scope
Ambient Euclidean distances are used, with the displayed unrescaled integer coordinate model. All edges refer to the actual one-dimensional faces of the polytope, not to a minimum spanning tree of its vertex set, graph-geodesic distances, or arbitrary vertex pairs. The regime \(n\ge m\ge2\) is essential to the stated positive-label formulas; no claim is made for \(n<m\). The endpoint \(c=+\infty\) means \((n-m)/m\to\infty\). No simultaneous independent audit or general-dimensional computer enumeration is claimed.

## Proof
**1. The vertices and edge types.** Fix \(m,n\) in scope. An exposed maximizer of a generic linear functional \(u\cdot x\) places \(n,n-1,\ldots,n-k+1\) on the \(k\) positive coordinates of \(u\), in decreasing order of those coefficients, and sets all coordinates with negative coefficients to zero. This follows directly from the rearrangement inequality: assigning a larger positive label to a larger coefficient increases the objective, and all of the \(m\) possible labels are strictly positive because \(n\ge m\). Every choice of ordered support is exposed, giving \(F_k\) vertices of support size \(k\).

At a generic normal vector, a change of maximizing vertex across a codimension-one normal-cone boundary can happen only when (i) two *adjacent* positive coefficients exchange order, or (ii) one coefficient crosses zero. In case (i), two consecutive positive labels exchange positions; in case (ii), the smallest available positive label is inserted or deleted. Conversely each such equality can be isolated while maintaining strict inequalities among all other coefficients, so each gives a genuine edge; no other one-dimensional face occurs. This recovers the previously known adjacency criterion, independently from its coordinate definition. The difference vectors are respectively \(e_a-e_b\) and \((n-k)e_a\) when the lower endpoint has rank \(k\); hence the two lengths are exactly \(\sqrt2\) and \(n-k\). The strict separation of integer and irrational lengths prevents ambiguity of classes.

**2. Multiplicities.** At a rank-\(k\) vertex there are \(k-1\) adjacent-label swaps; each swap edge is counted at both endpoints, so
\[
A_m=\frac12\sum_{k=2}^{m}(k-1)F_k.
\]
A lower-rank vertex of rank \(k\) admits \(m-k\) insertion edges, each counted once at its lower endpoint. Their number is \((m-k)F_k=F_{k+1}\), and their length is \(n-k=d+(m-k)\). Writing \(j=m-k\), this gives \(m!/(j-1)!\) edges of length \(d+j\). The identity \(\sum_{k=0}^{m-1}F_{k+1}=N_m-1\), together with \(\sum_{k=2}^{m}(k-1)F_k=(m-2)N_m+2\) (obtained by changing variables \(j=m-k\) and using \(\sum_{j=1}^{m}j/j!=E_{m-1}\)), yields the counts. Consequently \(2(A_m+N_m-1)=mN_m\), consistent with every vertex having degree \(m\).

**3. Weighted length and transition.** The insertion/deletion contribution is
\[
L_B=\sum_{j=1}^{m}(d+j)\frac{m!}{(j-1)!}
=m![(d+1)E_{m-1}+E_{m-2}].
\]
The swap contribution is \(L_A=\sqrt2 A_m\), proving the exact total-length formula. As \(m\to\infty\), \(E_m\to e\), \(N_m=m!E_m\), and hence \(L_B/N_m=(d+2)(1+O(1/m!))\) uniformly for all nonnegative \(d\), while \(L_A/N_m=(\sqrt2/2)(m-2+o(1))\). Taking the ratio proves all three regimes \(c=0\), finite positive \(c\), and \(c=\infty\), as well as the \(d=o(m)\) refinement. The *count* fraction equals \((N_m-1)/(mN_m/2)=2/m-2/(mN_m)\).

**4. Poisson laws.** The conditional insertion-length probabilities under edge-count sampling are
\[
\Pr(J=j)=\frac{1/(j-1)!}{E_{m-1}},\qquad 1\le j\le m.
\]
These are exactly the probabilities of \(1+Y\) given \(Y\le m-1\) for \(Y\sim\operatorname{Poisson}(1)\); the exact total-variation distance to the unconditioned law is its excluded tail \(\Pr(Y\ge m)\). Under length bias, multiply this probability by \(d+j\) and normalize by its mean. For fixed \(d\), \(\mathbb E(d+J)\to d+2\); decomposing \(d+j=(d+1)+(j-1)\) gives the stated mixture of \(1+Y\) and \(2+Y\). No finite enumeration has been used as a substitute for these all-parameter arguments.

## Verification
Run `python verify_edges.py` using Python 3 and SymPy. The standalone program generates all candidate vertices for \(m=2,3,4\) and both \(n=m\) and \(n=m+2\); it independently enumerates the facet-defining inequalities, declares a vertex pair an edge exactly when its common tight-facet normals have rank \(m-1\), and compares the resulting edge set and exact squared-length multiplicities with the derived formulas. It also checks the \(m\)-regular one-skeleton. The run prints `PARTIAL_PERMUTOHEDRON_EDGE_PASS`. These checks cover six finite instances and do not establish the infinite theorem without the analytic proof above.

## Relationship to prior work
Heuer and Striker introduced partial permutohedra, their inequalities and combinatorial face structure. Behrend and collaborators explicitly characterized the general anti-blocking permutohedron's edge adjacency in Proposition 5.7 and identified partial permutohedra as a special case in Corollary 5.8. **The two combinatorial edge types are therefore not claimed as new.** The present statement concerns their complete *Euclidean edge-length multiplicity measure* and its count-versus-length asymptotic separation, with a sharp linear-offset transition and a conditional Poisson law. The known adjacency classification is a premise of the new metric calculation; it does not report this limiting weighted geometric law. Vertex-cloud minimum spanning-tree length multisets are different metric summaries: the tree uses only \(N_m-1\) selected edges and does not determine the \(mN_m/2\)-edge facial length measure.

## Limitations
The novelty assessment is provisional, especially because the proof uses an existing combinatorial adjacency criterion. No independent audit or external priority certification is claimed. The result is restricted to nonnegative integer labels \(n\ge m\), standard unscaled coordinates, and the all-edge Euclidean 1-skeleton measure. The Poisson statement for the fixed-\(d\) length-biased sample is weak convergence and not a uniform assertion for arbitrary varying \(d\).

## References
1. D. Heuer and J. Striker, *Partial permutation and alternating sign matrix polytopes*, arXiv:2012.09901, first posted 2020-12-17, Sections 5.1–5.2, https://arxiv.org/html/2012.09901v3.
2. R. E. Behrend, F. Castillo, A. Chavez, A. Diaz-Lopez, L. Escobar, P. E. Harris, and E. Insko, *Partial permutohedra*, arXiv:2207.14253, first posted 2022-07-28, especially Proposition 5.7, Corollary 5.8 and Remark 5.9, https://arxiv.org/abs/2207.14253.
