# Arithmetic gaps and exponential scarcity of compact biclique allocations

## Finding
Fix integers \(q\ge3\), \(n\ge1\), and \(a,b\ge1\) such that \(a+b=nq\). There are \(n\) distinguishable agents and \(a+b\) distinguishable indivisible goods, one for each vertex of the complete bipartite graph \(K_{a,b}\). Every agent values each good at one, and every good is allocated. Compactness always refers to the subgraph induced by that agent's bundle.

Write \(N_{\alpha,\beta}\) for the number of allocations that are both envy-free (EF) and have each bundle \((\alpha,\beta)\)-compact. Set \(t=(a-n)/(q-2)\). Then
\[
N_{1,1}=\begin{cases}
\displaystyle\binom nt\frac{a!b!}{((q-1)!)^n},&t\in\{0,1,\ldots,n\}\text{ is an integer},\\
0,&\text{otherwise},
\end{cases}
\]
while
\[
N_{1,2}=N_{2,1}=a!b!\,[x^a]\left(\sum_{j=1}^{q-1}\frac{x^j}{j!(q-j)!}\right)^n.
\]
Thus \((1,2)\)-compactness (equivalently \((2,1)\)-compactness here) is feasible exactly for \(n\le a\le n(q-1)\). Among the \(n(q-2)+1\) integral sizes of the first bipartition class in this interval, radius-one compactness is feasible at precisely \(n+1\) values and infeasible at exactly \(n(q-3)\) values. Consequently, \(q=4\) is the first bundle size exhibiting gaps.

In particular, for balanced \(K_{2n,2n}\) and \(q=4\), there are no EF \((1,1)\)-compact allocations if \(n\) is odd. If \(n\) is even, the exact fraction of EF \((1,2)\)-compact allocations that also meet \((1,1)\)-compactness is
\[
R_n=\frac{\binom n{n/2}}{[x^n](1+\tfrac32x+x^2)^n}
\sim\frac4{\sqrt7}\left(\frac47\right)^n,
\qquad n\to\infty\text{ through even integers}.
\]

## Assumptions and scope
A complete allocation means that the bundles assigned to labeled agents are disjoint and partition all vertices. For \(\alpha,\beta\) nonnegative integers, a bundle is \((\alpha,\beta)\)-compact if some at most \(\alpha\) of its vertices have closed radius-\(\beta\) neighborhoods in the **induced bundle graph** covering that graph. Shortest paths may use only goods assigned to the same agent. Agents have identical additive utility equal to the bundle cardinality. In this result the only compactness budgets considered are \((1,1)\), \((1,2)\), and \((2,1)\), and \(q\ge3\) throughout. Vertices and agents are labeled; no quotient by automorphisms or agent permutations is taken.

## Proof
**Equitability.** Identical unit values imply that EF holds if and only if all agents receive the same number of goods. Since all \(nq\) goods are allocated, every bundle has exactly \(q\) goods.

**Induced geometry.** A bundle with \(j\) vertices in the first graph class and \(q-j\) in the second induces \(K_{j,q-j}\). For \(q\ge3\), a monochromatic bundle is an edgeless graph with more than two vertices, which is not compact under any of the three stated budgets. When \(1\le j\le q-1\), the induced graph is connected and has diameter at most two, so it has a radius-two center; a pair of centers, one from each graph class, dominates at radius one. Such a bundle has a radius-one single center if and only if \(j=1\) or \(j=q-1\), because a universal vertex is necessary and sufficient. These implications give the precise bundle profiles for the three compactness budgets.

**Enumeration.** Let \(j_i\) be the number of first-class goods assigned to agent \(i\). For the two less restrictive budgets, every \(j_i\) may lie in \(\{1,\ldots,q-1\}\), with \(\sum_i j_i=a\). At a fixed profile the number of assignments is
\[
\frac{a!}{\prod_i j_i!}\frac{b!}{\prod_i(q-j_i)!}.
\]
Summing all profiles gives the coefficient formula. At radius one each \(j_i\) is either \(1\) or \(q-1\). If exactly \(t\) agents have the latter value, \(a=t(q-1)+(n-t)=n+t(q-2)\). An integer \(t\in[0,n]\) is therefore necessary and sufficient, and the same multinomial calculation, together with choosing those \(t\) agents, yields the stated \(N_{1,1}\). Since every value in the interval \([n,n(q-1)]\) is a sum of \(n\) integers in \([1,q-1]\), radius-two feasibility and both counts of permitted graph-class sizes follow.

**First gap and sharp limiting proportion.** For \(q=4\) and \(a=b=2n\), the radius-one equation is \(2n=n+2t\), hence \(t=n/2\) and it is feasible exactly when \(n\) is even. Direct substitution into the preceding formulas gives
\[
N_{1,1}=\binom n{n/2}\frac{((2n)!)^2}{6^n},\quad
N_{1,2}=\frac{((2n)!)^2}{6^n}[x^n](1+\tfrac32x+x^2)^n.
\]
Let \(X\) take values \(-1,0,1\) with probabilities \(2/7,3/7,2/7\). This centered span-one lattice variable has variance \(4/7\), so
\[
[x^n](1+\tfrac32x+x^2)^n=(\tfrac72)^n\Pr(X_1+\cdots+X_n=0).
\]
One may obtain the precise central probability from Fourier inversion: its characteristic function \(\phi(\theta)=(3+4\cos\theta)/7\) satisfies \(|\phi(\theta)|<1\) away from zero on \([-\pi,\pi]\), and \(\phi(\theta)=1-2\theta^2/7+O(\theta^4)\) at zero. The Gaussian integral therefore yields
\[
\Pr(X_1+\cdots+X_n=0)\sim\sqrt{\frac7{8\pi n}}.
\]
Together with the central-binomial estimate \(\binom n{n/2}\sim 2^n\sqrt{2/(\pi n)}\) for even \(n\), this gives \(R_n\sim(4/\sqrt7)(4/7)^n\).

## Verification
The accompanying standalone script `verify_compact.py` implements the compactness predicate by breadth-first searches on the **induced graph of each bundle**, independent of the structural formulas. It exhaustively compares all three exact-count formulas with direct allocation enumeration on 51 parameter settings, covering 1,506,716 equitable labeled assignments. In particular, \(K_{6,6}\) allocated to three agents in bundles of four has zero radius-one but \(29{,}700\) radius-two allocations; \(K_{8,8}\) with four such agents has \(7{,}526{,}400\) and \(47{,}745{,}600\), respectively. Finite enumeration supports the proof but does not establish the infinite result, which follows from the preceding combinatorial and analytic arguments. Run `python3 verify_compact.py` from the directory containing this document.

## Relationship to prior work
Madathil [1] introduces the compact-bundle model and studies existence and computational complexity under fairness criteria. The star-partition analysis of van Bevern et al. [2], especially Section 4, **already derives the unique bipartition center-count equations**; the radius-one arithmetic feasibility obstruction in this theorem is an elementary specialization of that prior result and is **not presented as novel by itself**. The contribution assessed here is the exact labeled census for each compactness budget, the equality of radius-two and two-center counts for this entire family, and the first-gap parity and asymptotic prevalence law. No covering statement for that combined enumeration and limiting comparison was found in the examined sources; independent literature priority remains open.

## Limitations
The theorem assumes identical strictly positive unit value for every vertex, complete allocations, exactly equally sized nonempty bundles, and labeled agents. It does not extend to heterogeneous utilities, partial allocations, general bipartite graphs or general compactness budgets without a new proof. The asymptotic proportion is conditional on uniform choice among eligible radius-two allocations and takes only even \(n\); it is not a statement about randomly generated valuations. The star-factor feasibility core is covered by earlier literature, including a general induced-star-factor existence theorem [3]. This work has no independent external audit.

## References
[1] Jayakrishnan Madathil, *Fair Division of a Graph into Compact Bundles*, arXiv:2305.06864v1, first public May 11, 2023. https://arxiv.org/abs/2305.06864

[2] René van Bevern, Robert Bredereck, Laurent Bulteau, Jiehua Chen, Vincent Froese, Rolf Niedermeier, and Gerhard J. Woeginger, *Partitioning Perfect Graphs into Stars*, arXiv:1402.2589, Section 4 (2014 preprint; later revisions). https://arxiv.org/abs/1402.2589

[3] Y. Egawa, M. Kano, and Alexander K. Kelmans, *Star Partitions of Graphs*, Journal of Graph Theory 25 (1997), 185–190; full author-hosted open text: https://gorogoro.cis.ibaraki.ac.jp/web/papers/kano1997-a.pdf
