# Boundary and interior factors of the stationary discriminant for scroll rulings

## Finding

Let \(d\ge2\) and let \(n_1,\ldots,n_d\ge2\) be integers. Consider the curve of ruling \((d-1)\)-planes of the rational normal scroll \(S(n_1,\ldots,n_d)\). Its Euclidean-distance objective for an arbitrary complex symmetric data matrix \(Q\) is the trace pairing \(F_Q(t)=\operatorname{tr}(P(t)Q)\), where \(P(t)\) is the orthogonal projection associated with the ruling parametrized by \(t\).

Put
\[s_i(t)=\sum_{a=0}^{n_i}t^{2a},\quad L(t)=\operatorname{lcm}_{1\le i\le d}s_i(t),\quad m=\deg L,\]
and denote the distinct roots of the monic polynomial \(L\) by \(r_1,\ldots,r_m\). The integer \(m\) is at least four. Decompose the trace objective uniquely as
\[F_Q(t)=c_0+\sum_{j=1}^m\frac{c_j}{t-r_j}.\]
The linear map from symmetric data \(Q\) to the residue vector \((c_1,\ldots,c_m)\) is surjective. Define the cleared stationary polynomial
\[H_c(t)=-L(t)^2F'_Q(t)=\sum_{j=1}^m c_j\prod_{k\ne j}(t-r_k)^2.\]
For its discriminant **as a binary form of prescribed degree** \(2m-2\), there is a nonzero constant \(\kappa\), depending only on the poles, such that
\[\boxed{\operatorname{Disc}_{2m-2}(H_c)=\kappa\left(\prod_{j=1}^m c_j\right)R(c_1,\ldots,c_m).}\]
The polynomial \(R\) is geometrically irreducible and reduced, with
\[\boxed{\deg R=3m-6.}\]
The coordinate hyperplanes are pairwise distinct simple discriminant components. A general point of \(R=0\) outside these hyperplanes has exactly one finite stationary double root away from all poles; the collision is ordinary. A general point of \(c_j=0\) yields one double root of the *uncanceled cleared numerator* at the pole \(r_j\), rather than an interior stationary collision. The same irreducible-factor profile holds after pulling back via the surjective linear residue map to the full symmetric-data space.

## Assumptions and scope

The base field is \(\mathbb C\); the input parameters are integers as above, and the data space is the whole affine space of complex symmetric matrices, **not** the smaller variety of fixed-rank orthogonal projectors. Multiplicities, irreducibility and hypersurface degrees are geometric, over \(\mathbb C\). Discriminants use the homogeneous binary form of degree \(D=2m-2\), so a single simple root at infinity is not a discriminant zero. At the pole coordinates the full cleared polynomial is retained without first canceling denominators. The genericity assertions mean complements of proper Zariski-closed subsets in the indicated component.

## Proof

**1. Simple poles and independent residue data.** The denominators obey
\[s_i(t)=\frac{t^{2(n_i+1)}-1}{t^2-1}.\]
They are squarefree in characteristic zero and have no zero at \(t=\pm1\). Thus their least common multiple \(L\) is monic and squarefree. The projection matrix in the source's scroll parametrization is block diagonal, and its trace objective is
\[F_Q(t)=\sum_{i=1}^d\frac{f_i(t)}{s_i(t)},\qquad f_i(t)=v_i(t)Q_iv_i(t)^{\mathsf T},\quad v_i(t)=(1,t,\ldots,t^{n_i}).\]
Every polynomial of degree at most \(2n_i\) occurs as \(f_i\) for some symmetric block \(Q_i\): each monomial of that degree is obtained from one symmetric matrix entry. For every root \(r_j\), choose an index \(i\) for which \(s_i(r_j)=0\). Evaluation of arbitrary \(f_i\) at the distinct roots of \(s_i\) can be prescribed independently by polynomial interpolation. Assigning each root to one such index and setting its values on all other blocks to zero allows arbitrary prescribed residues at all \(m\) roots simultaneously. Hence the residue map is surjective. Partial fractions give the displayed formula for \(H_c\); its generic degree is \(D=2m-2\), with leading coefficient \(\sum_jc_j\).

**2. Irreducible interior incidence.** Work first for any fixed \(m\ge4\) distinct complex poles. Away from the poles, \(H_c(t)=H'_c(t)=0\) is equivalent to
\[\sum_j\frac{c_j}{(t-r_j)^2}=0,\qquad \sum_j\frac{c_j}{(t-r_j)^3}=0.\]
The two linear equations on \(c\) are independent because the numbers \((t-r_j)^{-1}\) are distinct. Their projective solution spaces form a \(\mathbb P^{m-3}\)-bundle over the irreducible punctured affine line \(\mathbb A^1\setminus\{r_j\}\); the incidence is thus irreducible of dimension \(m-2\). A nonzero residue vector cannot give identically zero \(H_c\): this would make \(F'_Q=0\) and every residue vanish. Each fiber of projection to coefficient space is therefore finite. The image closure \(Z\subset\mathbb P^{m-1}\) is an irreducible hypersurface. The incidence has a point with all residues nonzero: otherwise a fixed coordinate functional would lie in the span of the two displayed coefficient rows at every \(t\), requiring a nonzero linear combination to vanish at the other \(m-1\ge3\) distinct pole positions, which is impossible. Thus \(Z\) differs from every coordinate hyperplane.

**3. Generic collision is unique and ordinary.** The additional triple-root condition is \(\sum_jc_j/(t-r_j)^4=0\). The three evaluation rows with powers two, three and four are linearly independent: after nonzero column rescaling this is a Vandermonde matrix in the distinct values \((t-r_j)^{-1}\). The triple-root incidence therefore has dimension \(m-3\), strictly below \(\dim Z=m-2\).

For two different off-pole points \(t,u\), consider the four rows with denominators \((t-r_j)^2,(t-r_j)^3,(u-r_j)^2,(u-r_j)^3\). They have generic rank four: as \(u\to t\), suitable normalized row differences yield the four independent powers two through five, again a Vandermonde family. The rank can never drop below three. Indeed, rank at most two would express the row with denominator \((u-r_j)^2\) as a linear combination of the two rows at \(t\). Clearing denominators would give a polynomial of degree at most three in \(r_j\) vanishing at \(m\ge4\) distinct values, hence an identity of rational functions with distinct pole locations \(t\) and \(u\), a contradiction. The rank-three pairs lie in a proper closed subset of the two-dimensional \((t,u)\)-space, hence have base dimension at most one. For rank-four pairs the coefficient fiber is \(\mathbb P^{m-5}\) if nonempty, while for rank-three pairs it is \(\mathbb P^{m-4}\). Therefore the total locus of coefficients admitting two distinct double roots has dimension at most \(m-3\). Thus a general point of \(Z\) has precisely one double root and no triple root. Varying any residue changes the value of \(H_c(t)\) at this root by a nonzero multiple of \(\prod_{k\ne j}(t-r_k)^2\), so this simple double-root collision produces discriminant multiplicity one. Consequently \(Z\) is defined by a reduced irreducible factor \(R\).

**4. Pole factors and completeness.** On \(c_j=0\), every term of \(H_c\) is divisible by \((t-r_j)^2\). For general coefficients on that hyperplane, the quotient is squarefree and nonzero at \(r_j\), so the root at \(r_j\) has multiplicity exactly two. A perturbation of \(c_j\) changes the constant term of the local quadratic by a nonzero multiple of \(c_j\); its root difference has square proportional to \(c_j\). Therefore the discriminant contains the factor \(c_j\) with multiplicity exactly one. These hyperplanes are distinct and differ from \(Z\).

Any multiple projective root of \(H_c\) lies at a pole, an off-pole finite point, or infinity. The first two cases were classified. A double root at infinity requires both of the top coefficients of \(H_c\) to vanish. These conditions are \(\sum_jc_j=0\) and \(\sum_jr_jc_j=0\), two independent linear equations because the poles are distinct; hence this locus has codimension two and supplies no further hypersurface factor. Thus the complete discriminant divisor consists precisely of the \(m\) pole hyperplanes and \(Z\), each reduced.

**5. Degree and pullback.** The binary discriminant of a degree-\(D\) form has coefficient degree \(2D-2=4m-6\). As the coefficients of \(H_c\) depend linearly on residues and the \(m\) pole hyperplanes are degree one, the remaining factor must have degree \((4m-6)-m=3m-6\). The residue map from symmetric matrix coordinates is a surjective complex-linear map. After choosing a linear splitting, pulling back \(R\) amounts to adjoining independent extra variables, preserving its geometric irreducibility; the distinct hyperplanes also remain distinct. This proves the assertion for every indicated scroll.

## Verification

The accompanying `verify.py` performs exact symbolic checks using SymPy. For four fixed poles \(0,1,2,3\), the degree-six stationary polynomial has discriminant factor degrees \(1,1,1,1,6\), all with exponent one, and total degree ten. The three-pole check gives degrees \(1,1,1,3\). For the actual scroll \(S(2,2)\), where \(L(t)=1+t^2+t^4\), exact elimination in the numerator coefficients gives rational factor degrees \(2,2,6\) (the first two quadratics split into the four pole hyperplanes over \(\mathbb C\)); their total degree is ten. A four-by-four confluent evaluation determinant is checked to be nonzero at one rational specialization. Running `python verify.py` with SymPy reports `CERTIFICATE_OK`.

These finite calculations corroborate the formulas and protect the normalization; they are not proofs of the irreducibility and factorization for all parameters. Those rely on Steps 1–5.

## Relationship to prior work

Friedman, Hoşten and Rosana, *Euclidean Distance Optimization Within the Grassmannian* (arXiv:2610.02018), Example 2.1 and Theorem 2.2, supply the scroll projector parametrization and the generic stationary-root count \(2m-2\). Their Section 3 describes the ED discriminant of the **whole** projection Grassmannian using repeated eigenvalues of the symmetric data matrix; it does not give the stationary-numerator factorization for scroll ruling curves. This result derives the complete component structure, degrees and geometric meaning of the factors, not another ED-degree count.

Kayser, Kretschmer and Telen, *Logarithmic Discriminants of Hyperplane Arrangements* (arXiv:2410.11675), Section 5, study critical points of logarithmic master functions with equations involving simple denominators \(\sum_j u_j/(t-r_j)\) and obtain a reduced irreducible logarithmic discriminant of degree \(2(m-2)\) for \(m\) points. Here the stationary equation uses **squared** denominators \(\sum_jc_j/(t-r_j)^2\); its off-pole discriminant has degree \(3m-6\) and the ordinary polynomial discriminant carries additional pole factors. Neither stated result implies this factorization. General facts about discriminants, projective duality and fixed-pole rational functions may provide alternate historical formulations and must be checked before a priority claim is made.

## Limitations

The factorization is for the full vector space of complex symmetric data and the fixed-degree homogeneous discriminant of the *uncanceled* stationary polynomial. The pole hyperplanes encode collisions in that cleared polynomial, not necessarily collisions of legitimate critical points on its regular domain. The result does not assert the same factorization under the nonlinear constraint that the data matrix be an idempotent of fixed rank, nor does it classify exceptional higher-codimension intersections, reality of critical points, or minimum values of the distance objective. A simple critical root at infinity need not annihilate the binary discriminant. Historical priority is provisional; no independent mathematical audit has been performed.

## References

Friedman, H.; Hoşten, S.; Rosana, A., *Euclidean Distance Optimization Within the Grassmannian*, arXiv:2610.02018, first public version October 1, 2026; especially Example 2.1, Theorem 2.2 and Section 3. https://arxiv.org/html/2610.02018v2

Kayser, L.; Kretschmer, A.; Telen, S., *Logarithmic Discriminants of Hyperplane Arrangements*, arXiv:2410.11675, first public version October 15, 2024; especially Sections 5–6. https://arxiv.org/html/2410.11675v2
