# Power domination polynomial of crown graphs
## Finding
For every integer \(n\ge 3\), let \(\operatorname{Cr}_n=K_{n,n}-M_n\) have bipartition \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), where \(a_i b_i\) is the deleted perfect-matching nonedge. A set \(S\subseteq V(\operatorname{Cr}_n)\) is power dominating if and only if either it meets both bipartition classes, or it is contained in one class and has at least \(n-2\) vertices.

Therefore the power domination polynomial is
\[
\mathcal P(\operatorname{Cr}_n;x)=\big((1+x)^n-1\big)^2+2\left(\binom n2x^{n-2}+nx^{n-1}+x^n\right).
\]
In particular,
\[
\mathcal P(\operatorname{Cr}_n;1)=4^n-2^{n+1}+n^2+n+3.
\]
The minimum layer is: \(\gamma_P(\operatorname{Cr}_3)=1\) with six minimum sets; \(\gamma_P(\operatorname{Cr}_4)=2\) with twenty-eight minimum sets; and, for every \(n\ge5\), \(\gamma_P(\operatorname{Cr}_n)=2\) with exactly \(n^2\) minimum sets, the pairs having one vertex in each bipartition class.

## Assumptions and scope
Graphs are finite, simple, and undirected. Power domination uses one domination step, in which the closed neighborhood of the initial set becomes observed, followed by repeated forcing steps in which an observed vertex with exactly one unobserved neighbor observes that neighbor. The theorem concerns the ordinary power-domination process on \(\operatorname{Cr}_n\) for all integers \(n\ge3\); it does not assert a formula for generalized \(k\)-power domination.

## Proof
Write \(S_A=S\cap A\) and \(S_B=S\cap B\).

First suppose \(S_A\ne\varnothing\) and \(S_B\ne\varnothing\). If both \(|S_A|\ge2\) and \(|S_B|\ge2\), every vertex is observed in the domination step: each vertex on either side has a selected neighbor on the opposite side with a different matching index. If exactly one side contributes one selected vertex and the other contributes at least two, the domination step leaves at most one vertex unobserved, and a neighboring observed vertex then forces it. It remains to consider \(|S_A|=|S_B|=1\). If the two selected vertices have the same matching index, their closed neighborhoods already cover the graph. If they have distinct indices, say \(S=\{a_i,b_j\}\) with \(i\ne j\), the only vertices unobserved after domination are \(a_j\) and \(b_i\). Since \(n\ge3\), choose \(\ell\notin\{i,j\}\). The observed vertex \(b_\ell\) has \(a_j\) as its unique unobserved neighbor and forces it; then an observed neighbor of \(b_i\) forces \(b_i\). Hence every set meeting both sides is power dominating.

Now suppose \(S\subseteq A\); the case \(S\subseteq B\) is symmetric. Put \(k=|S|\) and \(r=n-k\). When \(k\ge2\), the domination step observes all of \(B\), while exactly the \(r\) unselected vertices of \(A\) remain unobserved. For \(b_j\in B\), the number of its unobserved neighbors is \(r-1\) if \(a_j\notin S\), and \(r\) if \(a_j\in S\). Thus if \(r\ge3\), every observed vertex has either zero or at least two unobserved neighbors and the process stalls. If \(r=2\), a vertex \(b_j\) whose matching partner \(a_j\) is one of the two omitted vertices has exactly the other omitted vertex as an unobserved neighbor and forces it; the last omitted vertex is then forced. The cases \(r\le1\) are immediate. Therefore for \(k\ge2\), a one-side set is power dominating exactly when \(k\ge n-2\).

For \(k=1\), the same conclusion holds. When \(n=3\), one selected vertex leaves two vertices in its own side unobserved after domination, and one observed opposite-side vertex forces one of them, after which the other is forced. When \(n\ge4\), at least three vertices of the selected vertex's side are unobserved after domination; every observed vertex on the opposite side has at least two unobserved neighbors, so no forcing step is possible. The empty set never power dominates. This proves the classification.

The mixed power-dominating sets contribute \(\big((1+x)^n-1\big)^2\): independently choose a nonempty subset of each side. The one-side power-dominating sets are disjoint from the mixed sets and, on each of the two sides, have sizes \(n-2,n-1,n\), contributing \(\binom n2x^{n-2}+nx^{n-1}+x^n\). This gives the polynomial. Substitution \(x=1\) gives the total count. The minimum-layer statements follow directly from the same classification.

## Verification
The standalone checker `verify.py` independently constructs \(\operatorname{Cr}_n\), simulates the domination and forcing rules for every subset, compares the simulation with the stated classification, and compares every polynomial coefficient and the minimum layer. Exhaustive checks for \(3\le n\le8\) returned:

`VERIFY_OK n_range=3..8 subset_checks=87360 coefficient_checks=66 total_checks=6 minimum_checks=6 max_order=16`

The computation is a finite stress test, not the proof for arbitrary \(n\); the infinite claim rests on the case analysis above.

## Relationship to prior work
Benson, Ferrero, Flagg, Furst, Hogben, Vasilevska, and Wissman publicly posted *Power domination and zero forcing* on 2015-10-08; its subject classification includes 05C69 and it develops the general relationship between power domination and zero forcing. Brimkov, Patel, Suriyanarayana, and Teich introduced the power domination polynomial in arXiv:1805.10984v1 and explicitly set out to characterize and count power-dominating sets of all cardinalities. Their full text gives general structural identities and formulas for several graph families; a full-text search found no occurrence of “crown”.

Chandrasekaran and Sulthana's 2019 paper *k-Power Domination of Crown Graph* is the closest same-object source. The indexed first page and abstract state that it investigates the power-domination problem in a biclique crown graph and focuses on the power domination number and minimum power-dominating sets. The remaining pages were not machine-readable in the accessible copy, so the scalar minimum statements above are not asserted to be original. The retained claim is the complete all-set classification and its exact power-domination polynomial. No inspected source stated or implied that classification or polynomial directly.

## Limitations
The result is specific to ordinary power domination on crown graphs. It does not classify generalized \(k\)-power-dominating sets, propagation times, polynomial roots, or graphs determined uniquely by this polynomial. The closest same-object 2019 source could not be inspected beyond indexed first-page material; this leaves a residual literature risk that its inaccessible portion contains a stronger enumeration than its abstract and visible material indicate. The finite verifier covers orders through sixteen vertices only and is supplementary to the proof.

## References
1. Katherine F. Benson, Daniela Ferrero, Mary Flagg, Veronika Furst, Leslie Hogben, Violeta Vasilevska, Brian Wissman, *Power domination and zero forcing*, arXiv:1510.02421v1, first posted 2015-10-08.
2. Boris Brimkov, Rutvik Patel, Varun Suriyanarayana, Alexander Teich, *Power domination polynomials of graphs*, arXiv:1805.10984v1, first posted 2018-05-28.
3. S. Chandrasekaran and A. Sulthana, *k-Power Domination of Crown Graph*, International Journal of Applied Engineering Research 14(13) (2019), 3066–3068, https://www.ripublication.com/ijaer19/ijaerv14n13_11.pdf.
