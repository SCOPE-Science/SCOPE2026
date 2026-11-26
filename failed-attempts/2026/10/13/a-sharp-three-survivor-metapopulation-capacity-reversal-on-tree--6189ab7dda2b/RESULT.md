# A sharp three-survivor metapopulation-capacity reversal on tree landscapes

## Finding

**Theorem.** Let \(n\ge4\) and let \(T=(V,E)\) be any finite simple undirected tree with \(|V|=n\). Choose a three-element subset \(S\subseteq V\) uniformly from the \(C=\binom{n}{3}\) possible subsets. Define the post-loss spectral capacity by
\[
\Lambda_T(S)=\rho\bigl(A(T[S])\bigr),\qquad W(T)=\sum_{v\in V}\binom{\deg_T(v)}2,
\]
where \(A(T[S])\) is the zero-diagonal, unit-weight adjacency matrix of the induced surviving-patch network and \(\rho\) is its largest eigenvalue (equal to its spectral radius for this nonnegative symmetric matrix).

The **complete conditional capacity law** is
\[
\begin{aligned}
\Pr(\Lambda_T=0)&=\frac{C-(n-1)(n-2)+W(T)}{C},\\
\Pr(\Lambda_T=1)&=\frac{(n-1)(n-2)-2W(T)}{C},\\
\Pr(\Lambda_T=\sqrt2)&=\frac{W(T)}{C}.
\end{aligned}
\]
No other capacity value is possible. For the species-specific, colonization-normalized extinction threshold \(\delta>0\), define the *spectral-threshold persistence indicator* to be \(\boldsymbol 1\{\Lambda_T>\delta\}\). Then
\[
\Pr(\Lambda_T>\delta)=
\begin{cases}
\displaystyle\frac{(n-1)(n-2)-W(T)}{C},&0<\delta<1,\\[5pt]
\displaystyle\frac{W(T)}{C},&1\le\delta<\sqrt2,\\[5pt]
0,&\delta\ge\sqrt2.
\end{cases}
\]
Among all \(n\)-patch tree dispersal networks, the **path uniquely maximizes** and the **star uniquely minimizes** this probability when \(0<\delta<1\); the **star uniquely maximizes** and the **path uniquely minimizes** it when \(1\le\delta<\sqrt2\). Uniqueness is up to graph isomorphism. Moreover,
\[
\mathbb E\Lambda_T=\frac{(n-1)(n-2)+(\sqrt2-2)W(T)}{C},
\]
so the path uniquely maximizes, and the star uniquely minimizes, the *mean* surviving capacity for every \(n\ge4\).

Three survivors are the **smallest possible survivor census** exhibiting a topology-dependent capacity law: with one survivor capacity is always zero, and with two survivors capacity is one with probability \(2/n\) and zero otherwise, independently of which \(n\)-vertex tree was used.

For \(n=4\), the path has \(W=2\) and the star \(W=3\). At thresholds strictly below one the two respective persistence-proxy probabilities are \(1\) and \(3/4\), while at thresholds between one and \(\sqrt2\) they are \(1/2\) and \(3/4\). The same networks and the same amount of habitat retention thus exchange their ordering at the exact threshold \(\delta=1\).

## Assumptions and scope

All original habitat patches have equal value, dispersal is symmetric, every original link has weight one, non-links have weight zero, and the original patch network is a connected tree. The three survivors are sampled *uniformly without replacement*, conditional on exactly three viable patches. The spectral capacity is a mathematical proxy: in the appropriate deterministic occupancy approximation, its comparison with a colonization-normalized extinction parameter gives a linear stability/persistence threshold. It does not assert that a finite stochastic occupancy process has a nonabsorbing stationary distribution. The post-loss induced graph may be disconnected or edgeless.

## Proof

**Step 1: classify all three-patch spectra.** An induced subgraph on three vertices of a tree is a forest, hence has exactly zero, one, or two edges. The corresponding isomorphism types are three isolates, one edge plus one isolate, and a three-vertex path. Their adjacency characteristic polynomials are respectively \(x^3\), \(x(x^2-1)\), and \(x(x^2-2)\); hence their largest eigenvalues are exactly \(0\), \(1\), and \(\sqrt2\).

**Step 2: enumerate each type exactly.** Every two-edge triple is a path of length two centered at one vertex. Thus its number is \(W(T)=\sum_v\binom{\deg_T(v)}2\). Every edge belongs to exactly \(n-2\) vertex triples, so summing the number of edges over all triples gives \((n-1)(n-2)\), since a tree has exactly \(n-1\) edges. A two-edge triple contributes twice and a one-edge triple once. Thus the one-edge count is \((n-1)(n-2)-2W(T)\). Subtracting these two counts from \(C\) yields the zero-edge count. Dividing by \(C\) proves the full law and both threshold formulas.

**Step 3: sharp wedge extremizers.** Put \(a_v=\deg_T(v)-1\). Because all tree degrees are at least one, \(a_v\ge0\) are integers and \(\sum_v a_v=n-2\). We have
\[
W(T)=\tfrac12\sum_v(a_v^2+a_v).
\]
Since \(a_v^2\ge a_v\) for integer \(a_v\ge0\), \(W(T)\ge n-2\), with equality only if every \(a_v\in\{0,1\}\). A connected tree of maximum degree two is a path. Conversely, the path attains the bound. At the other extreme, \(\sum_v a_v^2\le (\sum_v a_v)^2=(n-2)^2\), with equality only if at most one \(a_v\) is nonzero. Because \(n\ge4\), equality forces one vertex of degree \(n-1\), hence the star. This gives \(W(T)\le\binom{n-1}2\) with unique equality in the star.

**Step 4: optimize persistence probabilities and the mean.** On \(0<\delta<1\), the threshold probability is strictly decreasing in \(W\); on \(1\le\delta<\sqrt2\), it is strictly increasing in \(W\). Step 3 proves the sharp, uniquely attained optimizer reversal. Because \(\sqrt2-2<0\), the mean is strictly decreasing in \(W\). All assertions hold for every integer \(n\ge4\), with no numerical or asymptotic approximation.

**Step 5: prove the sharp survivor-census boundary.** With one retained vertex the adjacency matrix is zero. With two retained vertices it has capacity one exactly when the sampled pair is an edge. Every tree has \(n-1\) edges, so that event has probability \((n-1)/\binom n2=2/n\), the same for all trees. For three survivors and \(n\ge4\), Step 3 gives distinct path and star wedge counts, hence distinct capacity laws. This proves sharpness.

## Verification

Run the complete accompanying standalone Python file `verify.py` with Python 3. It enumerates every labeled tree through seven vertices using Prüfer codes, counts every induced three-patch network, verifies all three exact counting formulas and wedge extremizers, checks two-patch topology independence, and independently expands the symbolic characteristic polynomials of a sample of induced adjacency matrices. Its actual recorded output is

`VERIFY_OK labeled_trees=18247 three_patch_samples=615482 symbolic_charpoly_checks=2701`

These finite checks corroborate, but do not replace, the all-order proof in the preceding section.

## Relationship to prior work

Hanski and Ovaskainen introduced metapopulation capacity as a leading eigenvalue of a landscape matrix and used it to study fragmentation. Ovaskainen subsequently examined individual-patch destruction through eigenvector–eigenvalue relations. Grilli, Barabás, and Allesina studied spectral persistence criteria in randomly positioned landscapes, including patch removal. The theorem here concerns a different, deliberately discrete intervention: conditioning a *fixed tree dispersal network* on exactly three uniformly retained patches. Its contribution is the complete capacity law, the sharp smallest survivor census, and the reversal of globally optimal tree topologies at the species-dependent threshold one. The underlying spectral persistence criterion and elementary tree-degree identities are not claimed as new.

## Limitations

The result is for unweighted trees and equal-quality patches. It does not automatically extend to weighted dispersal kernels, cyclic original networks, more than three surviving patches, correlated habitat loss, or stochastic extinction times. The spectral threshold describes the specified deterministic approximation, not guaranteed survival of a finite stochastic metapopulation. No empirical effectiveness or claim about realistic spatial embedding is inferred.

## References

1. Hanski, I., and Ovaskainen, O. (2000). *The metapopulation capacity of a fragmented landscape*. Nature 404, 755–758. DOI: 10.1038/35008063. Public date: 2000-04-13.
2. Ovaskainen, O. (2003). *Habitat destruction, habitat restoration and eigenvector–eigenvalue relations*. Mathematical Biosciences 181, 165–176. DOI: 10.1016/S0025-5564(02)00150-5.
3. Grilli, J., Barabás, G., and Allesina, S. (2015). *Metapopulation Persistence in Random Fragmented Landscapes*. PLOS Computational Biology 11, e1004251. DOI: 10.1371/journal.pcbi.1004251.
