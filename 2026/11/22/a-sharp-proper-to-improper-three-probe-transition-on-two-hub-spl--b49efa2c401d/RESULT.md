# A sharp proper-to-improper three-probe transition on two-hub split resolvents

## Finding
Let \(q\ge4\) be an integer. On the unweighted complete split graph \(G=K_2\vee\overline{K_q}\), let \(L\) be its combinatorial Laplacian, \(\mu>0\), and \(B=(\mu I+L)^{-1}\). Partition its \(q+2\) vertices into exactly three nonempty classes and estimate \(\operatorname{tr}B\) using one **independent Rademacher quadratic form on each class**. Every such partition uses exactly three quadratic forms. Put
\[
H_q=\left\lfloor\frac{q^2}{4}\right\rfloor,\quad c=\frac1{\mu(\mu+q+2)},\quad \beta=\left(\frac2{\mu+2}\right)^2,\quad \mu_c=2(\sqrt{H_q}-1).
\]
There is an exact, universal transition at \(\mu=\mu_c\):

* If \(\mu>\mu_c\), every variance-optimal partition consists of the two adjacent, universal (clique) vertices **in separate singleton classes** and all \(q\) independent vertices in the third class. This is the proper three-coloring of \(G\), unique up to class-label permutations.
* If \(0<\mu<\mu_c\), every variance-optimal partition places **both adjacent universal vertices in the same class**. Let that class contain an additional \(x\) independent vertices, and let the other two class sizes be \(y,z\) (these contain only independent vertices). Then \(y+z=q-x\), \(y,z\ge1\), and \(\{y,z\}=\{\lfloor(q-x)/2\rfloor,\lceil(q-x)/2\rceil\}\). The exact permitted \(x\)'s are all the minimizers, over integers \(0\le x\le q-2\), of
\[
F_{q,\beta}(x)=1+2x+\beta\left[\binom x2+\binom{\lfloor(q-x)/2\rfloor}2+\binom{\lceil(q-x)/2\rceil}2\right].
\]
There are at most two permitted values of \(x\), and if two, they are adjacent. An exact test is given by the strictly increasing differences
\[
F_{q,\beta}(x+1)-F_{q,\beta}(x)=2+\beta\left[x-\left\lfloor\frac{q-x-1}{2}\right\rfloor\right],\quad0\le x\le q-3.
\]
* At \(\mu=\mu_c\), exactly two types of partition are optimal: the proper three-coloring just described, and the improper partition with the adjacent universal vertices together, no other vertices in their class, and the \(q\) independent vertices split as evenly as possible between the other two classes. Apart from relabeling vertices within the two graph orbits and relabeling the three classes, there are no further optima.

The exact minimum variance is
\[
V_*(q,\mu)=4c^2\begin{cases}
\beta\binom q2,&\mu\ge\mu_c,\\
\min_{0\le x\le q-2}F_{q,\beta}(x),&0<\mu\le\mu_c.
\end{cases}
\]
The two formulas agree at the transition. For \(q=4\), the sharp boundary is \(\mu_c=2\). More generally \(\mu_c=q-2\) for even \(q\) and \(\mu_c=\sqrt{q^2-1}-2\) for odd \(q\). Thus the natural proper coloring is *strictly* suboptimal throughout \(0<\mu<\mu_c\), at unchanged three-query cost.

## Assumptions and scope
All graph edges have unit weight. The two vertices of \(K_2\) are adjacent and joined to all \(q\) vertices of an independent set; the independent set has no internal edges. Every partition into precisely three nonempty classes is eligible, including non-proper graph colorings. Independently for each class, sample signs \(\pm1\) with equal probability on its vertices and put zero outside; sum the three quadratic forms. Exact arithmetic is assumed and the sole optimized criterion is estimator variance, with one quadratic form per class. The result does not optimize correlated probes, variable sample counts, wall-clock computation, or other graph families.

## Proof
**1. Resolvent entries and variance.** Set \(n=q+2\). Decompose the vertex space into constants, the \((q-1)\)-dimensional independent-set contrast subspace, and its orthogonal complement. The Laplacian eigenvalues are \(0\), \(2\) on the independent contrast, and \(n\) with multiplicity two. Hence
\[
B=\frac1{\mu+n}I+\left(\frac1{\mu+2}-\frac1{\mu+n}\right)P_{\mathrm{ind}}+\left(\frac1\mu-\frac1{\mu+n}\right)\frac{\mathbf1\mathbf1^{\mathsf T}}n,
\]
where \(P_{\mathrm{ind}}\) projects onto vectors supported on the independent vertices with zero sum. For distinct vertices, \(B_{ij}=c\) if at least one vertex belongs to the \(K_2\) clique, while \(B_{ij}=c\,2/(\mu+2)\) if both are independent. Independent Rademacher fourth moments show that the estimator variance is four times the sum of \(B_{ij}^2\) over unordered same-class pairs.

Let class \(j\) contain \(r_j\) clique vertices and \(s_j\) independent vertices. Here \(\sum r_j=2\), \(\sum s_j=q\), and \(r_j+s_j\ge1\). It follows exactly that
\[
\frac{\operatorname{Var}(T)}{4c^2}=\sum_{j=1}^3\left[\binom{r_j}{2}+r_js_j+\beta\binom{s_j}{2}\right]=:E.
\]
Because \(0<\beta<1\), no equality argument below degenerates for finite \(\mu>0\).

**2. Exclusion of most separated-clique partitions.** If the two clique vertices occupy distinct classes, let the numbers of independent vertices in these classes be \(u\le v\), and the remaining class contain \(w=q-u-v\ge1\). If \(u\ge1\), move one independent vertex from the first clique class to the second, then move the second clique vertex to the first class. The new coloring has both clique vertices together, remains three-class and nonempty, and its energy difference equals
\[
E_{\mathrm{new}}-E_{\mathrm{old}}=-(1-\beta)(v-u+1)<0.
\]
If \(u=0\) and \(v\ge2\), moving the second clique vertex to the first class instead changes energy by \(1-v<0\). Thus a global optimum with separated clique vertices must have \((u,v)=(0,0)\) or \((0,1)\). Their respective energies are
\[
E_{A_0}=\beta\binom q2,\qquad E_{A_1}=1+\beta\binom{q-1}2.
\]
The coloring with the two clique vertices together and the independent vertices split evenly into two other classes has energy
\[
E_{B_0}=1+\beta\left[\binom{\lfloor q/2\rfloor}2+\binom{\lceil q/2\rceil}2\right].
\]
For every \(q\ge4\), \(E_{A_1}>E_{B_0}\): the difference is strictly positive by the elementary binomial identity or convexity of \(\binom{s}{2}\). Therefore \(A_0\) is the **only** separated-clique configuration that could be optimal.

**3. Complete joined-clique classification.** If the clique vertices share a class with \(x\) independent vertices, the other two classes must have positive sizes \(y,z\), with \(x+y+z=q\). Their energy is \(1+2x+\beta[\binom x2+\binom y2+\binom z2]\). Since \(\beta>0\), for fixed \(x\), minimizing requires \(|y-z|\le1\) and gives \(F_{q,\beta}(x)\). The displayed first-difference formula follows by one binomial cancellation. The differences are strictly increasing in \(x\), so at most two adjacent integer minimizers exist, with the exact criterion in the finding.

**4. Sharp change of global topology.** Write \(H_q=\lfloor q^2/4\rfloor\). Direct binomial subtraction yields
\[
E_{A_0}-E_{B_0}=\beta H_q-1.
\]
When \(\beta\le1/H_q\), the difference \(F(1)-F(0)=2-\beta\lfloor(q-1)/2\rfloor\) is strictly positive because \(H_q\ge\lfloor(q-1)/2\rfloor\). All later differences are even larger, so \(B_0\) is the unique joined-clique minimizer. Hence when \(\beta<1/H_q\), \(A_0\) is uniquely globally optimal; at equality precisely \(A_0,B_0\) tie. When \(\beta>1/H_q\), \(B_0\) already strictly defeats \(A_0\), and step 2 excludes every other separated-clique case; consequently *all* global optima are exactly the joined-clique minimizers of \(F\). Solving \(\beta=(2/(\mu+2))^2=1/H_q\) yields the stated \(\mu_c\). This proves the classification and exact variance formula for every integer \(q\ge4\), every \(\mu>0\), and all admissible partitions.

## Verification
`python verify_split3.py` requires only Python 3's standard library. It independently constructs and rationally inverts shifted graph Laplacians for \(4\le q\le8\), compares every two-orbit off-diagonal entry with the spectral formula, and checks the actual pair-sum variance for all class-count profiles. It also exhaustively enumerates both possible clique-class patterns for \(4\le q\le15\) at rational parameter values, and verifies 47 exact critical identities. The recorded complete test run passed 9,808 rational score comparisons, 760 direct inverse/variance comparisons and 47 exact critical identities. These finite checks support the algebra; they are not used as proof for unbounded \(q\) or real \(\mu\).

## Relationship to prior work
Frommer, Rinelli and Schweitzer, arXiv:2308.07722 (2023), Theorem 3.3 and Lemma 3.5, give the general **fixed-partition** stochastic-probing variance formula, on which step 1 relies. Their analyzed designs largely use distance colorings; they do not state a global optimization over three possibly nonproper classes for the two-hub split graph, nor the exact parameter threshold or the complete optimizer description above. Earlier lattice-oriented hierarchical-probing methods use different graph families and criteria. A published two-color optimization for complete bipartite shifted resolvents determines optimal partitions into **two** classes on a different graph; its weighted-cut formula does not settle this three-class split-graph problem. Similarly, an equal-part multipartite two-probe classification does not cover three classes on a graph with singleton parts. Standard convex balancing is used in the proof but does not itself decide the sharp proper-versus-improper topology switch.

## Limitations
The result is an exact mathematical design benchmark for the first nontrivial two-hub split family, not a claim of practical speedup: the inverse is explicitly tractable on this symmetric graph. Only \(q\ge4\), positive finite shift, independent Rademacher signs, exactly one sample on each of exactly three nonempty classes, and variance are considered. The theorem does not establish a new general-purpose graph coloring algorithm or universal optimality beyond the stated estimator family. Historical prior art on weighted three-state cut models could contain an equivalent threshold; publication priority remains provisional.

## References
1. A. Frommer, M. Rinelli, M. Schweitzer, *Analysis of stochastic probing methods for estimating the trace of functions of sparse symmetric matrices*, arXiv:2308.07722v1, first posted 15 August 2023; particularly Theorem 3.3, Lemma 3.5, and Section 3.2. https://arxiv.org/abs/2308.07722
2. H. M. Switzer, A. Stathopoulos, E. Romero, J. Laeuchli, K. Orginos, *Probing for the trace estimation of a permuted matrix inverse corresponding to a lattice displacement*, DOI:10.1137/21M1422495 (2022). https://doi.org/10.1137/21M1422495
3. J. Laeuchli and A. Stathopoulos, *Extending hierarchical probing for computing the trace of matrix inverses*, DOI:10.1137/18M1176427 (2019). https://doi.org/10.1137/18M1176427
