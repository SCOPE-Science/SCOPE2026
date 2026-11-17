# Exact one-limited domination polynomial of open ladders

## Finding
For the open ladder \(L_n=P_2\square P_n\), \(n\ge2\), a vertex set \(D\) is *one-limited dominating* when every vertex outside \(D\) has a neighbor in \(D\), and every vertex inside \(D\) has at most one neighbor outside \(D\). Define the full weight enumerator \(P_n(z)=\sum_{D} z^{|D|}\), with all vertices distinguished. Then its bivariate ordinary generating function has the following exact reduced-degree expression:

\[\sum_{n\ge2}P_n(z)t^{n-2}=\frac{N(t,z)}{Q(t,z)}.\]

\[Q(t,z)=1-z^2t-z^3t^2-(z^5+2z^4)t^3-(z^6+z^5+z^4)t^4-z^6t^5.\]

\[\begin{aligned}N(t,z)=z^2\big[&(z^2+4z+4)+(2z^3+5z^2+2z)t\\&+(z^5+5z^4+6z^3+4z^2)t^2\\&+(z^6+3z^5+5z^4+2z^3)t^3\\&+(z^6+2z^5)t^4\big].\end{aligned}\]

The minimum one-limited domination number is \(n\), as also follows from the established general Cartesian-product bound; the new complete enumeration shows that **all** minimum sets are exactly the two entire rails, and (when \(n\) is even) two alternating pairs of whole-column blocks. Thus \([z^n]P_n(z)=2\) for odd \(n\) and \(4\) for even \(n\), and \([z^j]P_n(z)=0\) for \(j<n\).

The total number \(P_n(1)\) grows as \(C\lambda^{n-2}\), where \(\lambda=2.29237024940527\ldots\) is the unique positive root of
\[\lambda^5-\lambda^4-\lambda^3-3\lambda^2-3\lambda-1=0,\]
and \(C=8.17943774264\ldots\).

## Assumptions and scope
All graphs are finite, simple and undirected, with labelled vertices \((r,i)\), \(r\in\{0,1\}\), \(1\le i\le n\). Edges join the two vertices in each column and vertices in the same row in successive columns. The boundary is *open*, not cyclic. A selected vertex may have zero or one unselected neighbors; an unselected vertex must have at least one selected neighbor. The polynomial counts every admissible vertex subset by its cardinality, not subsets up to automorphisms. All identities are identities in the polynomial or formal-power-series rings over \(\mathbb Z\), for each integer \(n\ge2\).

## Proof
**Transfer encoding.** Represent column choices by two-bit masks \(a,b,c\in\{0,1,2,3\}\); a set bit means the corresponding vertex belongs to \(D\). Define \(V(a,b,c)\) to hold when each of the two vertices in the middle column \(b\) satisfies the required domination/capacity rule against its rung neighbor and the existing same-row neighbors in columns \(a,c\). At either end, a missing neighbor is omitted from the test. Explicitly, if \(s\) is the selected bit and \(w\) is the sum of the selected statuses of the existing two or three neighbors, the condition is \(w\ge1\) for \(s=0\), and \(\deg-w\le1\) for \(s=1\).

Index sixteen states by ordered pairs \((a,b)\). Define the transition matrix, row boundary and column boundary by
\[T_{(a,b),(b,c)}=z^{\operatorname{pop}(c)}\mathbf{1}_{V(a,b,c)},\qquad L_{(a,b)}=z^{\operatorname{pop}(a)+\operatorname{pop}(b)}\mathbf{1}_{V(\varnothing,a,b)},\qquad R_{(a,b)}=\mathbf{1}_{V(a,b,\varnothing)}.\]
All other transition entries are zero. Exactly twenty-six transitions are nonzero. Since the local test is necessary and sufficient in each column and every configuration has a unique sequence of masks,
\[P_n(z)=L T^{n-2}R\quad(n\ge2).\]
In particular, the enumeration is not a conjecture extrapolated from initial coefficients.

**Exact rational reduction.** Write \(a_j=LT^jR\). Consider the following monic degree-sixteen polynomial in an auxiliary variable \(u\):
\[\begin{aligned}H(u,z)={}&u^8(u-z)(u^2-zu+z^3)B(u,z),\\ B(u,z)={}&u^5-z^2u^4-z^3u^3-(z^5+2z^4)u^2\\&-(z^6+z^5+z^4)u-z^6.\end{aligned}\]
Direct polynomial matrix multiplication over \(\mathbb Z[z]\) gives \(H(T,z)=0\). This is a *finite exact identity*, and a standalone, executable coefficient-arithmetic verification appears in `artifacts/verify.py`. Let \(q_0,\ldots,q_5\) be the consecutive coefficients of \(Q(t,z)\) in \(t\), with \(q_0=1\). Define \(r_j=\sum_{i=0}^5q_i a_{j+5-i}\). The annihilator identity implies that \(r_j\) satisfies the same homogeneous monic degree-sixteen recurrence as \(a_j\). Exact integer-polynomial multiplication shows \(r_0=\cdots=r_{15}=0\), so induction implies \(r_j=0\) for **every** \(j\ge0\). Calculation of the five initial coefficients of \(Q(t,z)\sum_{j\ge0}a_jt^j\) gives exactly \(N(t,z)\); the higher coefficients vanish by the established recurrence. This proves the rational identity for every ladder length. The certificate checks every polynomial entry of \(H(T,z)\), all sixteen initial residuals, and the five numerator coefficients, without numerical approximation or finite-size extrapolation.

**Minimum sets.** Put \(U=V(L_n)\setminus D\). Each vertex in \(U\) has at least one incident cross-edge to \(D\), and each vertex in \(D\) has at most one cross-edge to \(U\); thus \(|U|\le |D|\), or \(|D|\ge n\). Selecting an entire rail attains equality. When equality holds, cross-edges constitute a perfect matching of all vertices. If any rung is crossed, the unique-cross-edge condition forces the two rows to retain their respective selection statuses in every adjacent column, propagating along the ladder: the two rail choices result. Otherwise both vertices in any column have the same selection status. Every vertex must then have exactly one horizontal cross-edge; hence successive column-status changes alternate, starting and ending with a change. This is possible exactly when \(n\) is even, with exactly two choices for the initial column. These give the two additional minimum sets and prove the exhaustive classification.

**Asymptotics.** At \(z=1\), the numerator and denominator become \(N(t,1)=9+9t+16t^2+11t^3+3t^4\) and \(Q(t,1)=1-t-t^2-3t^3-3t^4-t^5\). The denominator has a unique smallest-modulus zero \(\rho>0\): the positive-coefficient relation \(\rho+\rho^2+3\rho^3+3\rho^4+\rho^5=1\) and the triangle inequality show that another zero on the same circle must have matching phases for its first and second powers, hence must be \(\rho\). The root is simple, and \(N(\rho,1)>0\). Singularity extraction yields \(P_n(1)\sim C\rho^{-(n-2)}\) with
\[C=-\frac{N(\rho,1)}{\rho\,\partial_t Q(\rho,1)}>0,\qquad\lambda=1/\rho.\]

## Verification
Run `python3 artifacts/verify.py` (standard library only). The program reconstructs the sixteen-state transfer, uses exact integer coefficient vectors for every matrix entry, checks the entire degree-sixteen annihilating identity, and confirms that the first sixteen residuals of the order-five recurrence vanish and that all five numerator coefficients agree. It independently enumerates every vertex subset for \(2\le n\le8\) and checks all polynomial coefficients; additional finite tests check optimum-set counts through \(n=79\). These finite samples corroborate, but are not the proof of, the unrestricted claims: unrestricted identities follow from the exact matrix certificate and recurrence, and the minimum classification has its own combinatorial proof.

## Relationship to prior work
Božović, Radić, Kovijanić-Vukićević and Tepeh introduced \(k\)-limited domination and its basic bounds; their September 2026 open-access article examines parameters of paths, stars, cliques and complete bipartite graphs. Tepeh's June 2026 paper on Cartesian products **already gives the numerical value** \(\gamma_1^\mathrm{L}(P_2\square P_n)=n\) via the general bound for grids with an even dimension. This numerical value is not claimed here as novel. The new object is the full cardinality polynomial of every admissible set, together with the exact boundary-sensitive transfer reduction, complete minimizer profile and total-count asymptotics. A 2013 paper entitled *\((1,2)\)-Domination in Some Harmonius Graphs* uses a different condition on omitted vertices and cannot be treated as a calculation of this polynomial. Related published work on perfect matching cuts concerns the extremal crossing-edge structure, not the full enumerator. The full polynomial of a **circular** ladder, in which the ends are joined, is also not a formula for an open ladder: it is given by a transfer trace rather than this pair of boundary vectors.

## Limitations
Only open two-row ladder graphs and the constraint one unselected neighbor per selected vertex are treated. The formula does not count modulo ladder automorphisms, nor does it cover larger grid widths or other capacities. The finite algebra certificate is executable rather than a hand-printed 256-entry matrix computation. Full historical priority is provisional because literature indexed under other terminology or inaccessible sources could include an equivalent polynomial. No independent mathematical audit has been conducted.

## References
1. D. Božović, G. Radić, Ž. Kovijanić-Vukićević and A. Tepeh, *On k-limited domination in graphs*, arXiv:2606.22422v1 (first public 2026-06-21); *Computational and Applied Mathematics*, published online 2026-09-11, DOI 10.1007/s40314-026-03902-2. https://arxiv.org/abs/2606.22422
2. A. Tepeh, *On k-limited domination: complexity and Cartesian products*, arXiv:2606.22428v1 (2026-06-21). https://arxiv.org/abs/2606.22428
3. N. Murugesan and D. S. Nair, *\((1,2)\)-Domination in Some Harmonius Graphs* (2013), using a distinct definition of \((1,2)\)-domination.
4. J. Bouquet and C. Picouleau, *The complexity of the perfect matching-cut problem* (2024), on related perfect crossing-edge partitions.
