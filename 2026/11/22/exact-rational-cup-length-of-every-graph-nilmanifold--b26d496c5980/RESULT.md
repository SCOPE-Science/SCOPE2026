# Exact rational cup-length of every graph nilmanifold

## Finding

**Theorem.** Let \(G=(V,E)\) be a finite simple loopless graph with \(|V|=n\ge1\), and let \(N(G)\) be any compact Dani–Mainkar nilmanifold associated with \(G\). Denote by \(\operatorname{cl}_{\Bbbk}(N(G))\) the maximum number of strictly positive-degree cohomology classes (with coefficients \(\Bbbk\)) whose cup product is nonzero. For \(\Bbbk=\mathbb Q\) or \(\mathbb R\),

\[\operatorname{cl}_{\Bbbk}(N(G))=n.\]

In particular, this invariant is independent of the edge set: it has the same value for the torus associated with the edgeless graph and for the nilmanifold of the complete graph on the same vertex set. Choosing one endpoint for each edge gives \(n\) explicit real classes whose product generates top cohomology. A product of \(n\) rational classes generating rational top cohomology exists for every lattice, without identifying those classes with the displayed invariant forms.

## Assumptions and scope

The graph is simple, with no loops or parallel edges. Isolated vertices are permitted. All generators in the exterior cochain algebra have cohomological degree one, and the differential is the usual graded derivation with \(d^2=0\). Coefficients have characteristic zero. The nilmanifold is a compact quotient of the simply connected real nilpotent Lie group associated with the graphical Lie algebra, using any lattice. Nomizu’s comparison identifies the **real** de Rham cohomology ring with the real Chevalley–Eilenberg model. For an arbitrary lattice, the particular invariant forms below need not individually represent rational cohomology classes; equality of rational and real cup-length instead follows by change of coefficients and multilinearity.

Put \(V=\{1,\ldots,n\}\), and let \(m=|E|\). For the invariant-form calculation set \(\Bbbk=\mathbb R\). The Chevalley–Eilenberg differential graded algebra is

\[A_G=\big(\Lambda_{\Bbbk}(x_1,\ldots,x_n,y_e\ (e\in E)),d\big),\qquad dx_i=0,\quad dy_{\{i,j\}}=x_i\wedge x_j\quad(i<j),\]

with an immaterial consistent choice of signs for edge generators. Its real cohomology algebra is \(H^*(N(G);\mathbb R)\), and the manifold has dimension \(n+m\). Replacing \(\mathbb R\) by \(\mathbb Q\) in the displayed graph presentation need not give the rational cohomology ring for an arbitrary lattice. The rational cup-length follows instead from Step 4.

## Proof

**Step 1: no nonconstant closed element has a pure-edge component.** Let \(P=\Lambda_{\Bbbk}(y_e:e\in E)\) and \(I=(x_1,\ldots,x_n)\subset A_G\). As vector spaces, \(A_G=P\oplus I\). Consider a monomial \(y_S=\bigwedge_{e\in S}y_e\), with nonempty \(S\subseteq E\) and a fixed total edge order. In \(d(y_S)\), for every \(e=\{i,j\}\in S\) there is a nonzero signed term

\[\pm x_i\wedge x_j\wedge y_{S\setminus\{e\}}.\]

Each such target monomial uniquely identifies the edge \(e\), because distinct edges of a simple graph have different pairs \(\{i,j\}\). It then uniquely identifies \(S\) through its remaining edge factors. Therefore the sets of target monomials arising from different nonconstant basis monomials \(y_S\) are disjoint, and no term cancels even within a fixed \(d(y_S)\). Consequently \(d:P^{>0}\to A_G\) is injective.

Moreover, \(d(P)\) has exactly two vertex factors in each nonzero term, whereas \(d(I)\) has at least three vertex factors in each nonzero term (a term with an already present vertex factor acquires two more, possibly vanishing by repetition). Thus the degree-two-in-vertex contribution of \(d(p+u)\), with \(p\in P^{>0}\) and \(u\in I\), is precisely \(dp\). If \(p+u\) is a closed positive-degree cochain, then \(dp=0\); injectivity forces \(p=0\). Every positive-degree cohomology class therefore has a closed representative inside \(I\) (indeed every positive-degree cocycle belongs to \(I\)).

**Step 2: upper bound.** Since an exterior monomial can contain each \(x_i\) at most once, \(I^{n+1}=0\) inside the differential graded algebra. Products of \(n+1\) cocycles of strictly positive degree are therefore zero even before passing to cohomology. Hence \(\operatorname{cl}_{\Bbbk}(N(G))\le n\).

**Step 3: explicit classes attaining the bound.** Choose arbitrarily an endpoint \(a(e)\in e\) for each edge \(e\). For each vertex \(i\), write \(E_i=\{e\in E:a(e)=i\}\), and form the cochain

\[z_i=x_i\wedge\bigwedge_{e\in E_i}y_e\in A_G^{1+|E_i|}.\]

The empty wedge is \(1\). As \(dx_i=0\) and every \(dy_e\) for \(e\in E_i\) contains \(x_i\) as a factor, the graded Leibniz rule gives \(dz_i=0\). The sets \(E_i\) partition \(E\), so

\[z_1\wedge\cdots\wedge z_n=\pm x_1\wedge\cdots\wedge x_n\wedge\bigwedge_{e\in E}y_e=\pm\Omega.\]

This is a nonzero basis monomial of maximal total degree \(n+m\), hence closed. It is not exact: the differential of any monomial decreases the number of \(y\)-generators by one, so no differential can contain a term with all \(m\) distinct \(y\)-generators. Thus \([\Omega]\ne0\). The product of the \(n\) positive-degree classes \([z_i]\) is nonzero, proving \(\operatorname{cl}_{\Bbbk}(N(G))\ge n\).

**Step 4: rational coefficients.** A compact manifold has finite-dimensional rational cohomology, and \(H^*(N(G);\mathbb Q)\otimes_{\mathbb Q}\mathbb R\cong H^*(N(G);\mathbb R)\) as graded rings. If a product of \(n\) positive-degree real classes is nonzero, expanding each factor in a rational basis shows at least one product of \(n\) positive-degree rational basis classes is nonzero. Conversely, a vanishing \((n+1)\)-fold product over the reals implies vanishing over the rationals. Thus the real calculation establishes the same exact rational cup-length for every lattice. The explicit forms \(z_i\) are asserted to give **real**, not necessarily rational, cohomology classes for an arbitrary choice of lattice.

Combining the bounds proves the theorem. \(\square\)

## Verification

The accompanying `check.py` independently implements the exterior-algebra differential with exact integer signs. It tests **all 1,099 labelled simple graphs with between one and five vertices**, verifying (i) injectivity witness uniqueness on every nonconstant pure-edge monomial, (ii) closure of the explicit \(n\) cochains, and (iii) that their product is the unique top exterior basis monomial. It distinguishes **198,316 differential target monomials** across those graphs. Execute `python3 check.py`. These finite checks are supplementary; the all-graph proof uses the injective target identification and nilpotent vertex ideal, not finite enumeration.

The limiting cases are included: for an edgeless graph all \(z_i=x_i\), yielding the ordinary \(n\)-torus cup-length; for a single vertex the result is \(1\). No positive-degree product of length \(n+1\) is asserted merely from dimension; it is killed by the strictly stronger vertex-ideal argument.

## Relationship to prior work

The Dani–Mainkar graphical Lie algebra and its compact quotient are standard constructions. Aldi, Bevins, Chatzitheodoridis, Da Silva, Frias and Mejía Gómez (first public 12 November 2026) give explicit Poincaré polynomials for path-graph nilmanifolds and establish a diameter-dependent bound for total Betti numbers. Their §2.1 records the exact graphical Chevalley–Eilenberg differential used above; the present statement instead computes a *multiplicative* invariant, for all finite simple graphs, without computing individual Betti numbers. Pouseele and Tirao (2009) study second cohomology and symplectic/contact structures of graphical nilmanifolds, not an all-graph cup-length formula in the material accessible for comparison. General graph-simplicial-complex cup-length is a different invariant of a different space. The proof does not assert that prior authors lacked the ingredients, nor does it establish priority over all uncatalogued sources.

## Limitations

The formula is for the rational or real ordinary cup-length of Dani–Mainkar nilmanifolds associated with finite **simple** graphs; parallel edges, general two-step nilpotent Lie algebras, and other coefficient fields are outside the stated theorem. The manifold dimension \(n+m\) can be much larger than cup-length \(n\), so the result does not compute Lusternik–Schnirelmann category, nilpotency of unrelated rings, or the complete cohomology ring. Unindexed equivalent literature remains a possible originality risk. Independent mathematical review has not yet been performed.

## References

1. M. Aldi, S. Bevins, E. Chatzitheodoridis, S. Da Silva, Q. Frias and T. Mejía Gómez, *Poincaré polynomials of nilmanifolds associated with path graphs*, arXiv:2611.17014v1, first posted 12 November 2026. https://arxiv.org/html/2611.17014v1
2. S. G. Dani and M. G. Mainkar, *Anosov automorphisms on compact nilmanifolds associated with graphs*, Transactions of the American Mathematical Society 357 (2005), 2235–2251.
3. K. Nomizu, *On the cohomology of compact homogeneous spaces of nilpotent Lie groups*, Annals of Mathematics 59 (1954), 531–538.
4. H. Pouseele and P. Tirao, *Compact symplectic nilmanifolds associated with graphs*, Journal of Pure and Applied Algebra 213 (2009), 1788–1794, DOI:10.1016/j.jpaa.2009.01.014. https://doi.org/10.1016/j.jpaa.2009.01.014
