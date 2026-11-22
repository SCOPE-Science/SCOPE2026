# Full product monodromy and exact branch divisors for complete-bipartite enharmonic covers

## Finding

Let \(m\ge 2\) and \(n\ge 3\), and put \(d=n-1\). Consider the complete bipartite graph \(K_{m,n}\), with its \(n\) boundary vertices carrying distinct values \(b_1,\ldots,b_n\) and its \(m\) interior vertices carrying unknown potentials \(x_1,\ldots,x_m\). Assign algebraically independent, nonzero edge energies \(E_{ij}\). The fixed-energy enharmonic equations are
\[
\sum_{j=1}^{n}\frac{E_{ij}}{x_i-b_j}=0 \qquad (1\le i\le m).
\]
Over the rational parameter function field \(K=\mathbb Q(b_1,\ldots,b_n,E_{11},\ldots,E_{mn})\), the Galois closure of the degree-\(d^m\) solution cover has **geometric and arithmetic Galois group exactly**
\[
\operatorname{Gal}(L/K)\cong (\mathfrak S_d)^m,
\]
acting in its natural product action on the \(d^m\) ordered solution tuples. In particular the \(m\) coordinate polynomial splitting fields are jointly linearly disjoint.

There is also a precise global ramification statement on the open parameter scheme \(B\) where the \(b_j\) are pairwise distinct, all \(E_{ij}\) are nonzero, and every row sum \(a_i=\sum_j E_{ij}\) is nonzero. Put
\[
F_i(T)=\sum_{j=1}^n E_{ij}\prod_{k\ne j}(T-b_k),\quad P_i(T)=F_i(T)/a_i,\quad \Delta_i=\operatorname{disc}_T(P_i).
\]
Let \(\pi:Y\to B\) be the finite flat degree-\(d^m\) cover cut out by the monic equations \(P_i(x_i)=0\). Then the reduced branch divisor is **exactly** the union of the \(m\) distinct geometrically irreducible divisors \(\Delta_i=0\). With the standard ordered monomial basis of the finite algebra \(\pi_*\mathcal O_Y\), its trace-pairing discriminant is precisely
\[
\operatorname{disc}_{\mathrm{tr}}(Y/B)=\prod_{i=1}^m\Delta_i^{\,d^{m-1}}.
\]
At a generic point of \(\Delta_i=0\), inertia is a single transposition in the \(i\)-th \(\mathfrak S_d\) factor and acts on the \(d^m\) ordered solution tuples as \(d^{m-1}\) disjoint transpositions.

## Assumptions and scope

All statements concern characteristic zero, with the base field \(\mathbb Q\) and its algebraic closure for geometric monodromy. The boundary values and energy coordinates are independent indeterminates, subject only to the stated open conditions for the branch-divisor assertion. This is **generic** monodromy, not a claim that every rational specialization has full group. A fixed graph has independent energy parameters on every edge; imposing extra relations between rows may lower the group. The term "geometrically irreducible" for a branch divisor means irreducible after base change of the open parameter scheme to \(\overline{\mathbb Q}\).

The finite algebra is the coordinate ring
\[
R[x_1,\ldots,x_m]/(P_1(x_1),\ldots,P_m(x_m)),
\]
where \(R\) is the coordinate ring of \(B\). Since each \(P_i\) is monic of degree \(d\), it is a free \(R\)-module with ordered basis \(\prod_i x_i^{e_i}\), \(0\le e_i<d\).

## Proof

**1. Polynomial reconstruction from energies.** Fix a base field containing \(b_1,\ldots,b_n\), with the \(b_j\) pairwise distinct. Evaluating at a boundary value gives
\[
F_i(b_j)=E_{ij}\prod_{k\ne j}(b_j-b_k).
\]
The diagonal factors are units. Degree-\(d\) polynomials have \(n=d+1\) coefficients, and their evaluations at the \(n\) distinct boundary values form an invertible Vandermonde map. Hence \((E_{i1},\ldots,E_{in})\mapsto F_i\) is a linear isomorphism between row-energy space and the affine space of all degree-at-most-\(d\) polynomials. The coefficient of \(T^d\) in \(F_i\) is \(a_i\), so inverting \(a_i\) gives the universal **generic degree-\(d\) polynomial**, together with a free leading coefficient. These coefficient changes for distinct rows are independent over the common boundary-value field.

**2. Full product Galois group.** Over \(k=\overline{\mathbb Q}(b_1,\ldots,b_n)\), introduce algebraically independent roots \(z_{i1},\ldots,z_{id}\) and leading coefficients \(a_i\), and set \(F_i(T)=a_i\prod_{h=1}^d(T-z_{ih})\). The fundamental theorem of symmetric polynomials identifies the independent coefficient field with the invariants of \((\mathfrak S_d)^m\) acting on these root variables separately. Its full root field is rational in the \(z_{ih},a_i\) and has precisely that product as its Galois group. The same presentation works with \(\mathbb Q\) in place of \(\overline{\mathbb Q}\). Since the root variables and the boundary variables are algebraically independent, there is no reduction when the common boundary parameters vary. Thus both arithmetic and geometric groups are \((\mathfrak S_d)^m\), and the coordinate splitting fields are jointly linearly disjoint. The point stabilizer in the product action has index \(d^m\), giving the asserted solution-cover degree.

**3. Exact branch components.** On \(B\), the independent coefficient change remains invertible. A monic degree-\(d\) generic polynomial has an irreducible discriminant hypersurface: its dense open subset consists of polynomials with exactly one double root and \(d-2\) other simple roots. This subset is irreducible because it is dominated by the irreducible space parameterizing a double-root position and a residual monic degree-\(d-2\) polynomial. The discriminant is generically reduced there (local roots split as a square-root of a transverse parameter), and no other repeated-root mechanism forms a divisor. The localization requiring nonzero energies does not discard the generic double-root polynomial: one may choose it so that no boundary value is a root. Consequently each \(\Delta_i=0\) is a nonempty geometrically irreducible divisor in \(B\). For different \(i\), these are distinct divisors since their coefficients are independently variable. The Jacobian of \(P_i(x_i)\) with respect to \(x_i\) is \(P_i'(x_i)\), so the cover is étale exactly where every \(\Delta_i\) is invertible. Near a generic \(\Delta_i\), the double root has simple local ramification and exchanges two roots of row \(i\) while all other rows remain unramified. This proves the branch and inertia assertions.

**4. Trace discriminant.** For each \(i\), let \(A_i=R[T]/(P_i(T))\). The finite algebra of \(Y\) is \(A_1\otimes_R\cdots\otimes_R A_m\). Multiplication by pure tensors has traces that multiply; therefore its trace pairing is the Kronecker product of the \(m\) row trace pairings. Each has determinant \(\operatorname{disc}(P_i)=\Delta_i\) in the standard power basis. Applying \(\det(U\otimes V)=\det(U)^{\mathrm{size}(V)}\det(V)^{\mathrm{size}(U)}\) gives exactly \(\prod_i\Delta_i^{d^{m-1}}\), with no unspecified scalar factor. The reduced branch support agrees with the trace discriminant support.

**5. Positive real energies.** If the \(b_j\) are increasing real numbers and every \(E_{ij}>0\), the left side of row \(i\)'s equation decreases strictly on each gap \((b_j,b_{j+1})\), diverging from \(+\infty\) to \(-\infty\). It has one simple root in each of the \(d=n-1\) gaps and none on the two outer rays. Therefore all \(d^m\) solutions are real, one per choice of gap for each interior vertex. This provides a geometric interpretation of the product permutation action; it is not needed for the generic Galois argument.

## Verification

The accompanying dependency-free `checker.py` verifies the interpolation identity on several integer parameter sets and independently checks an exact rational specialization with \(m=2,n=4\), boundary values \((0,1,2,3)\) and positive energy rows \((2,3,5,7)\) and \((1,2,3,4)\). The respective numerators are
\[
17T^3-68T^2+69T-12,\qquad 10T^3-40T^2+40T-6.
\]
They are irreducible cubics over \(\mathbb Q\), with nonsquare discriminants \(688908=2^2\cdot3\cdot11\cdot17\cdot307\) and \(94800=2^4\cdot3\cdot5^2\cdot79\). Their distinct quadratic discriminant fields force the two \(S_3\) splitting fields to be linearly disjoint: a nontrivial common Galois subextension of two \(S_3\)-extensions would contain their unique quadratic subextensions. Thus this explicit specialization has group \(S_3\times S_3\). The general theorem is proved by the invariant-field argument above, not by this example or a finite test.

Run: `python3 checker.py`. It uses only the Python standard library.

## Relationship to prior work

Finkel's *Galois Actions on Energy-Harmonic Functions* (arXiv:2611.00990v1, 31 October 2026), Section 5.1, Proposition 15, gives the same decoupled equations and proves only that the generic group lies in a product of symmetric groups; Example 16 identifies \(K_{2,3}\) with \(V_4\). The theorem here proves the upper bound is **always attained** for all \(m\ge2,n\ge3\) with independent generic energies and additionally determines the irreducible reduced branch divisors, their inertia and the trace-discriminant multiplicities. The case \(K_{2,3}\), and the general equation/decoupling itself, are not claimed as new.

Abrams and Kenyon's *Fixed-energy harmonic functions* (arXiv:1505.05785, 2015) proves existence, orientation correspondence and totally-real properties for general fixed-energy Dirichlet networks. Betti, Borovik, Finkel, Sturmfels and Zacovic's *Graphical Scattering Equations* (arXiv:2511.07316v1, 2025) studies a distinct graph-constrained scattering setup with momentum-conservation conditions, not this unconstrained coefficient family. The fundamental theorem for generic polynomial splitting fields is a classical input and is not claimed as new.

## Limitations

The result applies to the universal independent-energy family in characteristic zero, not to arbitrary correlated energy specializations or other graphs. The repeated-root branch description is on the stated nonzero, distinct-boundary, nonzero-row-sum open; boundary and degree-drop loci of its compactification are not classified. Exact arithmetic Galois groups at rational parameter values can be smaller than the generic group, even when every energy is positive. The proof has had self-review, but no independent expert audit or priority certification. Literature indexing can omit equivalent prior calculations.

## References

1. B. Finkel, *Galois Actions on Energy-Harmonic Functions*, arXiv:2611.00990v1, publicly submitted 2026-10-31. https://arxiv.org/html/2611.00990v1
2. A. Abrams and R. Kenyon, *Fixed-energy harmonic functions*, arXiv:1505.05785, 2015. https://arxiv.org/abs/1505.05785
3. B. Betti, V. Borovik, B. Finkel, B. Sturmfels and B. Zacovic, *Graphical Scattering Equations*, arXiv:2511.07316v1, 2025. https://arxiv.org/html/2511.07316v1
