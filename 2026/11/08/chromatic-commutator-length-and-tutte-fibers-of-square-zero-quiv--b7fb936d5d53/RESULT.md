# Chromatic commutator length and Tutte fibers of square-zero quiver algebras

## Finding

Let \(Q\) be a finite quiver with at least one vertex, no loop arrows, and arbitrary parallel arrows and orientations. Put \(n=|Q_0|\), \(m=|Q_1|\), and let \(k=\mathbb F_q\) be any finite field. Let \(J\) be the arrow ideal and \(A=kQ/J^2\). The underlying loopless undirected multigraph \(G\) has a distinct edge for every arrow of \(Q\). Thus \(\dim_k A=n+m\), \(J^2=0\), and \([A,A]=J\), where brackets denote additive associative-algebra commutators.

For \(z=\sum_{e\in Q_1}z_e e\in J\), let \(S(z)=\{e:z_e\ne0\}\), and let \(G_{S(z)}=(Q_0,S(z))\), retaining isolated vertices. Write \(\chi(G_{S(z)})\) for its vertex chromatic number, with \(\chi=1\) for an edgeless graph. Define \(\operatorname{cl}_A(z)\) as the minimum nonnegative number of additive commutators summing to \(z\). Then
\[
\boxed{\operatorname{cl}_A(z)=\left\lceil\log_{q^2}\chi(G_{S(z)})\right\rceil.}
\]
In particular, \(z\) is a single commutator precisely when \(\chi(G_{S(z)})\le q^2\), and the additive commutator width of \(A\) (the maximum of \(\operatorname{cl}_A(z)\) over \(z\in J\)) is exactly \(\lceil\log_{q^2}\chi(G)\rceil\). This includes the zero-width case of an edgeless quiver. For a complete graph on \(r\) vertices, the maximal length is \(\lceil\log_{q^2}r\rceil\), so the width is unbounded over any fixed finite field as the quiver grows.

The number \(N_A(z)=|\{(x,y)\in A^2:[x,y]=z\}|\) of labeled ordered representations depends on \(z\) only through its support \(S=S(z)\). If \(\sigma:Q_0\to k^2\) is a vertex coloring, write \(\mathrm{eq}_G(\sigma)=|\{e=uv\in Q_1:\sigma(u)=\sigma(v)\}|\), counting parallel edges separately. The complete fiber formula is
\[
\boxed{N_A(z)=q^m\sum_{\substack{\sigma:Q_0\to k^2\\\sigma(u)\ne\sigma(v)\ \forall uv\in S}}q^{\mathrm{eq}_G(\sigma)}.}
\]
Equivalently, for a subset \(F\subseteq E(G)\setminus S\), form a multigraph \(H_{F,S}\) by contracting every connected component of \((Q_0,F)\) to one vertex and retaining the edges in \(S\), including any resulting loops. Let \(P_H(t)\) denote the ordinary chromatic polynomial (zero when \(H\) has a loop). Then
\[
\boxed{N_A(z)=q^m\sum_{F\subseteq E(G)\setminus S}(q-1)^{|F|}P_{H_{F,S}}(q^2).}
\]
Thus the entire commutator distribution has a graph-polynomial description, not only the zero fiber.

In particular, writing \(\kappa(F)\) for the number of connected components of \((Q_0,F)\), the probability that two uniformly chosen elements of \(A\) commute is
\[
\boxed{\operatorname{cp}(A)=q^{-2n-m}\sum_{F\subseteq E(G)}(q-1)^{|F|}q^{2\kappa(F)}.}
\]
This is the Fortuin–Kasteleyn/Tutte partition function of \(G\) at vertex-state count \(q^2\) and edge weight \(q-1\), divided by \(q^{2n+m}\).

For a fixed loopless multigraph \(G\) as \(q\) ranges through prime powers, define
\[
 d(G)=\max_{F\subseteq E(G)}\bigl(|F|-2(n-\kappa(F))\bigr),
 \quad c(G)=\#\left\{F\subseteq E(G):|F|-2(n-\kappa(F))=d(G)\right\}.
\]
Then \(d(G)\ge0\), \(c(G)\ge1\), and
\[
\boxed{\operatorname{cp}(A)=c(G)q^{-m+d(G)}\bigl(1+O_G(q^{-1})\bigr).}
\]
By the Nash–Williams arboricity criterion, \(d(G)=0\) if and only if the edges of \(G\) can be partitioned into two forests. Thus the leading exponent of the algebraic commuting probability detects the two-forest density threshold; for example, \(d(K_5)=2\) but \(d(K_4)=0\).

## Assumptions and scope

All algebras are finite-dimensional, unital, associative, and defined over a finite field of arbitrary characteristic. The only structural restrictions are that the quiver has no loop arrows and that paths of length two vanish. Parallel arrows and oppositely oriented arrows are permitted, with each arrow a separate radical basis vector. The graph \(G\) is the undirected multigraph obtained by forgetting orientations but not multiplicities. The word "commutator" refers to \(xy-yx\) in an associative algebra; it does not refer to a group commutator. Chromatic numbers are those of ordinary vertex colorings, and a graph containing a loop has zero proper colorings.

## Proof

**1. Coordinates and the commutator.** Let \(e_v\) denote the primitive idempotent at vertex \(v\). Every element of \(A\) is uniquely \(x=\sum_va_ve_v+\sum_er_ee\). For \(y=\sum_vb_ve_v+\sum_es_ee\), the coefficient of \(e:u\to v\) in the additive commutator is
\[
 [x,y]_e=(a_u-a_v)s_e-(b_u-b_v)r_e.
\]
No diagonal or length-two term occurs. Since \(u\ne v\), each arrow is itself a commutator of a primitive idempotent with that arrow (up to sign), proving \([A,A]=J\) as a vector space.

**2. Exact commutator length.** Suppose \(z=\sum_{j=1}^{\ell}[x_j,y_j]\). At a vertex \(v\), collect the \(2\ell\) diagonal coefficients of the \(x_j,y_j\) into a label \(\lambda(v)\in k^{2\ell}\). If \(z_e\ne0\) on an arrow with endpoints \(u,v\), the displayed commutator coefficient forces \(\lambda(u)\ne\lambda(v)\). Hence the support graph has a proper labeling by at most \(q^{2\ell}\) colors and \(\chi(G_{S(z)})\le q^{2\ell}\).

Conversely, if \(G_{S(z)}\) has a proper coloring with at most \(q^{2\ell}\) colors, encode every color by a distinct element of \(k^{2\ell}\). Read the labels as the diagonal coefficients of \(\ell\) pairs of algebra elements. For each supported arrow, at least one of the \(2\ell\) endpoint differences is nonzero. Set exactly one arrow coefficient of the appropriate \(x_j\) or \(y_j\) to the value making its commutator contribution equal to \(z_e\), and all other arrow coefficients for that arrow to zero. The equations for different arrows are independent because \(J^2=0\). This constructs a decomposition of the required length. For \(z=0\), the empty sum works and the support graph is edgeless with chromatic number one. Taking the worst support gives the width statement.

**3. Fiber count.** Fix the \(2n\) diagonal coefficients of an ordered pair \((x,y)\), equivalently a labeling \(\sigma:Q_0\to k^2\). At an arrow \(e=uv\), the map from the two arrow coefficients \((r_e,s_e)\in k^2\) to the target \(z_e\) is the zero linear functional when \(\sigma(u)=\sigma(v)\), and a surjective nonzero linear functional otherwise. Therefore equal-label arrows admit \(q^2\) arrow-coefficient pairs only when \(z_e=0\), whereas unequal-label arrows admit exactly \(q\) pairs for every specified \(z_e\). Multiplication over arrows gives \(q^{m+\mathrm{eq}_G(\sigma)}\), subject to unequal labels on the support. Summing over all diagonal labels gives the first formula.

For every arrow outside \(S\), expand the equal-label factor as \(q^{\mathbf1_{\sigma(u)=\sigma(v)}}=1+(q-1)\mathbf1_{\sigma(u)=\sigma(v)}\). Expand the resulting product as a sum over subsets \(F\) of arrows outside \(S\). Each chosen edge in \(F\) forces its endpoints to have equal colors; the edges in \(S\) still force distinct colors. The count of such colorings is the chromatic polynomial of the graph formed by contracting all components of \((Q_0,F)\) and keeping \(S\). If a supported edge becomes a loop, its chromatic polynomial is zero. This proves the second formula. In the zero fiber \(S=\varnothing\), every contracted graph has \(\kappa(F)\) isolated vertices, giving \(q^{2\kappa(F)}\). Dividing the zero-fiber count by \(|A|^2=q^{2(n+m)}\) yields the commuting probability.

**4. Asymptotic and arboricity.** In the finite sum for \(\operatorname{cp}(A)\), the term indexed by \(F\) has leading degree \(|F|+2\kappa(F)\) as a polynomial in \(q\), with positive leading coefficient one. The largest exponent is \(2n+d(G)\); there are exactly \(c(G)\) subsets attaining it. No leading-term cancellation is possible, so division by \(q^{2n+m}\) gives the asserted asymptotic. Since \(F=\varnothing\) is permitted, \(d(G)\ge0\). The condition \(d(G)=0\) is equivalent to \(|F|\le2(n-\kappa(F))\) for every edge subset \(F\). By the standard Nash–Williams forest-partition criterion this is equivalent to decomposability of \(G\) into two forests. No assertion about exact coefficients at finite \(q\) is inferred from the asymptotic alone; those are already supplied by the exact state sum.

## Verification

The supplied standard-library scripts are `verify_commutator.py`, `verify_width.py`, and `verify_gf4.py`. Execute each from the directory containing the package files with `python verify_commutator.py`, `python verify_width.py`, and `python verify_gf4.py`. The respective complete reference outputs are `check_output.txt`, `width_output.txt`, and `gf4_output.txt`. The scripts reconstruct commutators from coordinates, not from the proposed partition-function formula. Their direct finite enumerations compare every target fiber in multiple small loopless quivers, including parallel arrows, and independently evaluate the zero-fiber subset expansion. A separate script enumerates all support subsets of complete graphs through five vertices over \(\mathbb F_2\), constructs explicit decompositions, and verifies the chromatic threshold. The extension-field script uses \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\) and checks every target fiber for a three-vertex path (over a million ordered algebra pairs).

The marker on successful completion is `COMMUTATOR_SUPPORT_AND_FK_DIRECT_PASS`, `CHROMATIC_COMMUTATOR_WIDTH_PASS`, and `GF4_DIRECT_FIBERS_PASS`. Exhaustive finite examples serve as checks, not proofs of the general theorems. The proof above is field-uniform and does not depend on these examples.

## Relationship to prior work

Bleher, Chinburg, and Huisgen-Zimmermann study module varieties for finite-dimensional algebras with square-zero radical (arXiv:1407.3045v1, 2014). Their framework supplies a natural archival algebra class; their statements concern tops, socles, and module-variety irreducible components, not additive commutator lengths or commutator fiber distributions.

Sokal's 2005 survey (arXiv:math/0503607v1) supplies the established Fortuin–Kasteleyn/Tutte state sum and its proper-coloring specialization. The graph polynomial and the forest-partition theorem are credited prior mathematics. They do not by themselves identify the additive commutator fibers of a square-zero quiver algebra; that identification follows from the coordinate argument above.

The already published classification of commutator fibers for the two-vertex generalized Kronecker path algebras (published-finding corpus, "Commutator fibers and commuting probabilities of finite Kronecker path algebras") is a special case of the present formula, not a new consequence claimed independently. Indeed, for \(r\) parallel arrows the graph has two vertices and \(r\) parallel edges, and substitution yields the published fiber counts. This earlier result does not cover general loopless quivers, support-dependent chromatic obstructions, unbounded commutator width, or the two-forest asymptotic transition.

The distinguishing contribution assessed here is the general support/chromatic characterization and its exact elementwise commutator length, alongside the full Tutte/chromatic fiber law for arbitrary loopless square-zero quiver algebras. A more general statement about commutator images or graphs of bilinear maps might be available under alternate terminology; this remains a historical-priority limitation.

## Limitations

The theorem does not apply without modification to loop arrows (which are central modulo the radical square), to nonzero radical-square products, or to a non-split semisimple quotient. It concerns additive commutators, not multiplicative commutators of units or group-theoretic stable commutator length. Counts of individual fibers and their asymptotic limits are exact only under the displayed hypotheses. No assertion of independent mathematical or historical-priority certification is made.

## References

1. Frauke M. Bleher, Ted Chinburg, and Birge Huisgen-Zimmermann, “The geometry of finite dimensional algebras with vanishing radical square,” arXiv:1407.3045v1, first public version 2014-07-11, https://arxiv.org/abs/1407.3045.
2. Alan D. Sokal, “The multivariate Tutte polynomial (alias Potts model) for graphs and matroids,” arXiv:math/0503607v1, first public version 2005-03-25, https://arxiv.org/abs/math/0503607. Theorem 2.3 is the Fortuin–Kasteleyn graph-state-sum identity.
3. C. St. J. A. Nash-Williams, “Decomposition of finite graphs into forests,” *Journal of the London Mathematical Society* 39 (1964), 12; the classical forest-partition criterion. See also M. Chen, S.-J. Kim, A. Kostochka, D. B. West, and X. Zhu, “Decomposition of sparse graphs into forests: The Nine Dragon Tree Conjecture for \(k\le2\),” arXiv:1502.04755v1, first public version 2015-02-17.
4. “Commutator fibers and commuting probabilities of finite Kronecker path algebras,” published-finding corpus (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-commutator-fibers-and-commuting-probabilities-of-finite-kronecke--75cb49b6c27d.
