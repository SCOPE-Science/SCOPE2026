# Complete power-domination census and irredundant spectrum of crown graphs

## Finding

For every integer \(n\ge4\), let \(\operatorname{Cr}_n=K_{n,n}-M_n\) be the crown graph with two labeled vertex classes \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), where \(a_i\) is adjacent to \(b_j\) precisely when \(i\ne j\). A vertex set is *power dominating* when its closed neighborhood is observed initially and the rule that an observed vertex observes its unique unobserved neighbor is repeated until no further change is possible.

**Classification.** A subset \(S\subseteq V(\operatorname{Cr}_n)\) is power dominating if and only if either it meets both \(A\) and \(B\), or it is entirely in one class and contains at least \(n-2\) vertices.

Let \(\mathcal P_n(x,y)\) count power-dominating sets, weighting a set by \(x^{|S\cap A|}y^{|S\cap B|}\). Then
\[
\boxed{\mathcal P_n(x,y)=\big((1+x)^n-1\big)\big((1+y)^n-1\big)+\sum_{k=n-2}^{n}\binom nk(x^k+y^k).}
\]
In particular, the ordinary cardinality polynomial and total number are
\[
\boxed{\mathcal P_n(z,z)=\big((1+z)^n-1\big)^2+2\sum_{k=n-2}^{n}\binom nk z^k,}
\qquad
\boxed{\mathcal P_n(1,1)=4^n-2^{n+1}+n^2+n+3.}
\]

The inclusion-minimal power-dominating sets are exactly the \(n^2\) pairs \(\{a_i,b_j\}\), with arbitrary \(i,j\), and the \(\binom n2\) subsets of size \(n-2\) within each class. Hence the bivariate and univariate inclusion-minimal-set polynomials are
\[
\boxed{\mathcal M_n(x,y)=n^2xy+\binom n2(x^{n-2}+y^{n-2}),}
\qquad
\boxed{\mathcal M_n(z,z)=n^2z^2+n(n-1)z^{n-2}.}
\]
The minimum power-domination number is \(\gamma_P(\operatorname{Cr}_n)=2\); the upper power-domination number, the largest size of an inclusion-minimal power-dominating set, is \(\overline{\gamma}_P(\operatorname{Cr}_n)=n-2\). Thus the gap is \(n-4\), and for \(n\ge6\), exactly \(n-5\) intermediate integer sizes are absent from the inclusion-minimal spectrum. Within this domain, all inclusion-minimal power-dominating sets have the same cardinality if and only if \(n=4\).

## Assumptions and scope

All graphs are finite, simple, undirected and labeled. The theorem covers every integer \(n\ge4\); it concerns standard one-neighbor power domination, not generalized \(k\)-power domination or ordinary zero forcing. The two indeterminates count vertices chosen from the individually labeled bipartition classes. The empty set is excluded automatically. An inclusion-minimal power-dominating set need not be minimum-cardinality; its defining condition is that no proper subset remains power dominating.

For context, \(\operatorname{Cr}_3\) is the six-cycle, and its power-domination polynomial follows from the previously published cycle formula [1]. The asserted infinite-family enumeration and maximality classification are stated for \(n\ge4\).

## Proof

**Step 1: any mixed set succeeds.** By monotonicity of the observed-vertex process, it suffices to start with \(S=\{a_i,b_j\}\). If \(i=j\), this set dominates every vertex: its two closed neighborhoods together are all of \(V\). If \(i\ne j\), its closed neighborhoods cover all vertices except possibly \(a_j\) and \(b_i\). Choose an index \(k\notin\{i,j\}\), possible because \(n\ge4\). Both \(a_k\) and \(b_k\) are observed. The observed vertex \(a_k\) is adjacent to the sole unobserved \(B\)-vertex \(b_i\), and \(b_k\) to the sole unobserved \(A\)-vertex \(a_j\). Each has exactly one unobserved neighbor, so both remaining vertices are observed by the forcing rule. Additional initially selected vertices cannot prevent success.

**Step 2: one-class sets.** By symmetry take \(S\subseteq A\), and write \(s=|S|\). If \(s=0\), no vertex is initially observed. If \(s=1\), say \(S=\{a_i\}\), the initial observed set comprises \(a_i\) and all \(B\)-vertices except \(b_i\). Every observed \(b_j\) with \(j\ne i\) has exactly \(n-2\ge2\) unobserved neighbors in \(A\); the observed \(a_i\) has no unobserved neighbor. Therefore no forcing occurs, and this selection fails.

Suppose \(s\ge2\). Initially all vertices of \(B\) are observed, and precisely the vertices \(W=A\setminus S\) remain unobserved. Put \(w=|W|=n-s\). For each observed \(b_j\), the number of its unobserved neighbors is \(w-1\) when \(a_j\in W\), and \(w\) otherwise. Selected vertices of \(A\) have no unobserved neighbors. If \(w\ge3\), every observed vertex has either zero or at least two unobserved neighbors; thus propagation stops with \(W\ne\varnothing\). If \(w=0\), all vertices were observed initially. If \(w=1\), choose any index outside \(W\); its corresponding observed \(b_j\) forces the unique vertex of \(W\). If \(w=2\), an observed \(b_j\) whose index lies in \(W\) has precisely one unobserved neighbor (the other member of \(W\)), which it forces; the last unobserved vertex is then forced by some \(b_k\) with \(k\) outside its index. Therefore, for \(s\ge2\), success is equivalent to \(w\le2\), or \(s\ge n-2\). Because \(n\ge4\), this also includes the previously checked failure of \(s=1\). Symmetry proves the statement for \(S\subseteq B\).

**Step 3: inclusion-minimality.** Every mixed successful set contains a mixed pair, and a mixed pair is inclusion-minimal because no singleton succeeds for \(n\ge4\). Within one class, the successful sets are precisely those of size at least \(n-2\), so the inclusion-minimal ones have exactly \(n-2\) vertices. These two types cannot be confused, and there are no additional types.

**Step 4: exact enumeration and boundaries.** Nonempty selections from both classes contribute \(\big((1+x)^n-1\big)\big((1+y)^n-1\big)\). The disjoint pure-class families contribute the indicated binomial sums. Inclusion-minimal pairs yield \(n^2xy\), while a pure-class minimum threshold set is determined by its two omitted indices, yielding \(\binom n2\) in each class. Specializing \(x=y=z\) proves both univariate formulas. Substitution \(x=y=1\) gives the total-count identity. The only inclusion-minimal sizes are \(2\) and \(n-2\), coincident at \(n=4\); this establishes all asserted extremal parameters, the unbounded cardinality gap, and the exact count of missing interior sizes.

## Verification

The standalone Python 3 checker `verification/crown_power_domination_check.py` constructs the graph from the adjacency definition and computes the closure of each selected set using the closed-neighborhood step followed by all available unique-white-neighbor forcing steps. It does not use the classification to determine whether a set succeeds. For every \(4\le n\le8\), it examines all \(2^{2n}\) vertex subsets, checks the necessary-and-sufficient condition, counts by both selected-side cardinalities, tests inclusion-minimality by removing each selected vertex, and compares the resulting coefficient tables and total counts with the theorem. The checks all passed: the total number of examined vertex subsets over the five orders is \(87,296\). These finite computations corroborate the stated general proof; they are not substitutes for the universal argument.

To reproduce: run `python3 verification/crown_power_domination_check.py` from the extracted package root. The program uses only the Python standard library and prints `ALL_CHECKS_PASSED` upon success.

## Relationship to prior work

Brimkov, Patel, Suriyanarayana and Teich [1] introduced the power-domination polynomial and established general identities and formulas for cycles, complete graphs, stars, threshold graphs and certain graph operations. Their published cycle formula already covers the \(n=3\) crown, which is therefore excluded from the new domain. Their inspected formulas and decomposition results do not yield the crown-graph bivariate census for \(n\ge4\) without the new side-occupancy classification.

Dorbec, Varghese and Vijayakumar [2] explicitly use matching-deleted complete bipartite graphs as examples for generalized power-domination numbers and edge sensitivity, and in particular discuss the scalar minimum for such graphs. The minimum value \(2\) is credited as known where applicable. Their inspected treatment does not provide the exact ordinary power-domination enumerator or the complete inclusion-minimal classification. Chandrasekaran and Sulthana [3] have a directly relevant 2019 title concerning power domination of crown graphs; accessible indexed material advertises minimum-number results, but its full paper could not be read, so a definitive noncoverage assertion for that paper is **not** made. Bjorkman et al. [4] develop the general framework of minimum versus inclusion-minimal power-dominating sets and their reconfiguration; their inspected complete-bipartite example is for the undeleted graph, and no crown-specific census was identified.

The exact bivariate census, inclusion-minimal polynomial and unbounded upper-minus-lower cardinality gap are the assessed contribution; the power-domination process, cycle case and previously established scalar bounds are not represented as new.

## Limitations

The theorem covers only the standard power-domination process on complete bipartite graphs with **all** edges of one perfect matching deleted. It does not claim a formula for arbitrary partial matching deletion, generalized propagation parameter, or arbitrary bipartite graphs. Originality comparison rests on the accessible primary text and indexed records described above. A plausible 2019 paper on the identical graph class was not readable in full, and unindexed equivalent treatments remain a priority risk; this is not an independently audited finding.

## References

[1] B. Brimkov, R. Patel, V. Suriyanarayana and A. Teich, *Power domination polynomials of graphs*, arXiv:1805.10984v1 (first posted 2018-05-28), https://arxiv.org/abs/1805.10984 .

[2] P. Dorbec, S. Varghese and A. Vijayakumar, *Heredity for generalized power domination*, arXiv:1603.07243 (first posted 2016-03-23), https://arxiv.org/abs/1603.07243 .

[3] S. Chandrasekaran and A. Sulthana, *k-Power Domination of Crown Graph*, International Journal of Applied Engineering Research **14**(13), 3066–3068 (2019), publisher record https://www.ripublication.com/ijaer19/ijaerv14n13_11.pdf . Full article not retrieved; indexed opening excerpt only.

[4] B. Bjorkman, C. Bozeman, D. Ferrero, M. Flagg, C. Grood, L. Hogben, B. Jacob and C. Reinhart, *Power Domination Reconfiguration*, La Matematica **5**, article 8 (2026), https://doi.org/10.1007/s44007-025-00187-5 .
