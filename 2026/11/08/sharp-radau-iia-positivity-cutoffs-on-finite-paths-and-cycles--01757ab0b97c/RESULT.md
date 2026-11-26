# Sharp all-step Radau IIA positivity on finite undirected cycles

## Finding

Let \(C_n\) be the unweighted simple undirected cycle on \(n\ge3\) vertices, and let \(L=D-A\) be its combinatorial Laplacian. The completed step of the ordinary two-stage Radau IIA method on \(u'=-Lu\) is \(T(h)=R(hL)\), where
\[
R(x)=\frac{1-x/3}{1+2x/3+x^2/6}.
\]
Then \(T(h)\) is entrywise nonnegative for every \(h\ge0\) if and only if \(3\le n\le9\). In this range every entry is strictly positive when \(h>0\), and the matrix is symmetric with row sums one. For \(n\ge10\), the previously known distance-five obstruction gives a negative entry for sufficiently small positive steps. The additional conclusion here is *all-step* positivity through nine vertices; positivity separately for small and large steps does not rule out an intermediate failure.

## Assumptions and scope

The edges of the undirected cycle have unit conductance and are counted once, including on \(C_3\). There is no boundary killing, reaction term, or mesh normalization. The result is about the completed step and arbitrary nonnegative input, not about internal stages or time steps on a different graph family.

## Proof

For \(3\le n\le9\) set
\[
Q(h)=I+2hL/3+h^2L^2/6,\qquad B(h)=I-hL/3.
\]
The eigenvalues of \(L\) are nonnegative, so \(Q(h)\) is positive definite for \(h\ge0\). The step \(T=Q^{-1}B\) is symmetric and circulant, hence it suffices to compute its entries \((0,j)\) for \(0\le j\le \lfloor n/2\rfloor\). In exact arithmetic reduce each to a rational fraction \(N_{n,j}(h)/D_{n,j}(h)\) with positive leading denominator coefficient. For the seven cycles the number of fractions per order is \(2,3,3,4,4,5,5\), respectively. The cycle blocks of `CERTIFICATE.json` supply all 26 fractions. Every numerator is nonzero with nonnegative coefficients; every denominator has nonnegative coefficients and positive constant term. The signs certify strict positivity for every \(h>0\), not just for a sample of steps. For example the distance-four entry for \(C_9\) is
\[
\frac{4h^4+36h^5+54h^6+20h^7+h^8}
{144+864h+2376h^2+3728h^3+3580h^4+2088h^5+708h^6+120h^7+9h^8}.
\]
The finite computation is reproducible by building \(L\) from the \(n\) cyclic edges, solving \(Qv=Be_0\) in \(\mathbb Q(h)\), canceling numerator and denominator of each component up to cyclic distance \(\lfloor n/2\rfloor\), and checking the described signs. At \(h=0\), \(T=I\); \(L\mathbf1=0\) and \(R(0)=1\) give the row-sum assertion.

For completeness, if \(n\ge10\), choose vertices \(u,v\) at distance five. The Taylor coefficients of \(R\) through order five are \(1,-1,1/2,-1/6,1/36,1/108\). No power \(L^j\) with \(j<5\) has a nonzero \((u,v)\) entry. Every five-edge walk contributing to that entry of \(L^5\) has sign \((-1)^5\), so \([T(h)]_{uv}=-\nu_5(u,v)h^5/108+O(h^6)\) with \(\nu_5(u,v)>0\). This reproduces the known exclusion and finishes the classification.

## Verification

Read the 26 cycle-distance rows of `CERTIFICATE.json` using ascending coefficient order. The accompanying `VERIFY.py` recomputes them over the rational-function field and checks the Taylor coefficient and the first excluded cycle. The package retains additional path calculations, which are not needed for the cycle theorem. The proof of all-step positivity rests on exact polynomial coefficient signs, not on a finite grid in \(h\).

## Relationship to prior work

*Ten-vertex small-step positivity barrier and oscillatory lattice tails for Radau IIA* (Resultary, 2026-10-13, record `cf8fc1888ee6`) gives the negative small-step conclusion for \(C_n\), \(n\ge10\), the positive small-step conclusion through \(C_9\), and eventual positivity for finite cycles. The all-step result above closes the gap between small and large steps for the seven listed cycles. *A diameter-five positivity obstruction and exact six-path recovery* (Resultary, 2026-10-26, record `79ccecc67e03`) gives the stronger obstruction for positive weighted graphs and the exact path cutoff. Neither the diameter obstruction nor the path cutoff is claimed as a contribution here. The cycle calculation is also distinct from general absolute-monotonicity radii and step restrictions for invariant polyhedra.

References for the related general settings: C. Bolley and M. Crouzeix, *Conservation de la positivité lors de la discrétisation des problèmes d'évolution paraboliques*, DOI:10.1051/m2an/1978120302371; L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, arXiv:1303.6651; Z. Horváth, Y. Song and T. Terlaky, *Steplength thresholds for invariance preserving of discretization methods of dynamical systems on a polyhedron*, arXiv:1406.6755.

## Limitations

This does not classify the recovery threshold for longer cycles or solve the corresponding problem with unequal conductances, orientations, reactions, or nonlinear dynamics. The all-step conclusion for the finite admissible set uses an exact rational certificate.
