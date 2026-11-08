# Higher commuting tuples in the minimal nilpotent matrix orbit: exact finite-field counts and image-span geometry

## Finding

Let \(q\) be a prime power, \(n\geq4\), \(r\geq3\), and \(V=\mathbb F_q^n\). Let \(\mathcal O\) be the conjugacy class of all nonzero rank-one square-zero endomorphisms of \(V\). For each integer \(d\), let \(C_{n,r,d}(q)\) count ordered \(r\)-tuples \((A_1,\ldots,A_r)\in\mathcal O^r\) such that \([A_i,A_j]=0\) for all \(i,j\) and \(\dim(\sum_i\operatorname{im} A_i)=d\).

Write \(\bigl[{n\atop d}\bigr]_q\) for the Gaussian binomial coefficient, and define
\[
T_{r,d}(q)=\sum_{j=0}^r(-1)^j\binom rj \prod_{i=0}^{d-1}(q^{r-j}-q^i),
\]
where the product is zero when \(r-j<d\). Then, for every \(1\leq d\leq\min(r,n-1)\),
\[
\boxed{C_{n,r,d}(q)=\biggl[{n\atop d}\biggr]_q T_{r,d}(q)\left(\frac{q^{n-d}-1}{q-1}\right)^r.}
\]
For all other \(d\), the count vanishes. The sum over \(d\) is the exact ordered commuting-tuple count, and division by \(|\mathcal O|^r\), with
\[
|\mathcal O|=\frac{(q^n-1)(q^{n-1}-1)}{q-1},
\]
gives the exact probability of pairwise commutation for independent uniform elements of this orbit.

Over an algebraically closed field, the corresponding reduced locally closed locus \(\mathcal S_d\) of ordered pairwise commuting, nonzero rank-one square-zero \(r\)-tuples whose joint image span has dimension \(d\) is smooth and irreducible, of dimension
\[
\dim\mathcal S_d=r(n-1)+d(n-d).
\]
Thus the whole (reduced) orbit-tuple commuting variety has dimension
\[
\boxed{r(n-1)+m_{n,r},\qquad m_{n,r}=\max_{1\leq d\leq\min(r,n-1)}d(n-d).}
\]
The number of its **maximal-dimensional** irreducible components is two exactly if \(n\) is odd and \(r\geq(n+1)/2\), and is one otherwise. This does **not** classify lower-dimensional irreducible components. For fixed \(n,r\), as \(q\) tends to infinity through prime powers, the total number of ordered commuting tuples is
\[
\kappa_{n,r}q^{r(n-1)+m_{n,r}}\bigl(1+O(q^{-1})\bigr),
\]
where \(\kappa_{n,r}\in\{1,2\}\) is the stated maximal-dimensional component count. Consequently the commuting probability is \(\kappa_{n,r}q^{m_{n,r}-r(n-1)}(1+O(q^{-1}))\).

## Assumptions and scope

All finite-field formulas hold in every characteristic, including two and for nonprime field orders. Matrices are labeled, tuples are ordered, and each entry is nonzero and has rank exactly one and square zero. The theorem's claimed scope is \(n\geq4\), \(r\geq3\); smaller parameters are verification boundaries only. Geometric statements concern the reduced underlying variety over an algebraically closed field and only the strata and maximal-dimensional irreducible components. No scheme-theoretic reducedness of the defining commutator equations is asserted.

## Proof

**Commuting is mutual annihilation.** Write a nonzero rank-one square-zero matrix as \(A=u\varphi\) with \(u\ne0\), \(\varphi\ne0\), \(\varphi(u)=0\), and similarly \(B=v\psi\). If \(AB=BA\ne0\), then the image lines \(ku\) and \(kv\) coincide, because the images of \(AB\) and \(BA\) respectively lie in those lines and are nonzero. Thus \(v=cu\) for some nonzero \(c\); both \(\varphi(v)\) and \(\psi(u)\) then vanish because both factors are square-zero. This contradicts \(AB\ne0\). Hence \([A,B]=0\) implies \(AB=BA=0\); the converse is immediate. The same conclusion applies simultaneously to every pair in the tuple.

**The joint image span.** Let \(U=\sum_i\operatorname{im}A_i\) and \(d=\dim U\). Since every \(A_iA_j=0\), every \(A_i\) kills \(U\). Consequently each \(A_i\) is a nonzero rank-one map in \(\operatorname{Hom}(V/U,U)\), and its image lines jointly span \(U\). Conversely, any \(d\)-dimensional subspace \(U\) and \(r\) such maps whose images span \(U\) yield pairwise mutually annihilating square-zero maps on \(V\). Necessarily \(1\leq d\leq\min(r,n-1)\). These choices of \(U\) are unique for a tuple, so the parameterization does not duplicate tuples across strata.

**Fixed-subspace enumeration.** For a fixed \(d\)-plane \(U\), each rank-one map is \(u_i\varphi_i\), where \(u_i\in U\setminus\{0\}\), \(\varphi_i\in(V/U)^*\setminus\{0\}\), modulo the free simultaneous rescaling \((u_i,\varphi_i)\mapsto(cu_i,c^{-1}\varphi_i)\) with \(c\in\mathbb F_q^\times\). Requiring the \(u_i\) to span \(U\) gives \(T_{r,d}(q)\) ordered nonzero spanning vectors: begin with all surjective maps \(\mathbb F_q^r\to U\), numbered by \(\prod_{i=0}^{d-1}(q^r-q^i)\), and apply inclusion-exclusion to the columns that are zero. Once these vectors are fixed there are \((q^{n-d}-1)^r\) choices of nonzero covectors. Divide by \((q-1)^r\). There are \(\bigl[{n\atop d}\bigr]_q\) choices of \(U\). This proves the exact formula for every permitted \(d\), including nonprime \(q\).

**Geometry of strata.** Let \(\mathcal G_d=\operatorname{Gr}(d,V)\) and \(\mathcal U\) be its tautological bundle. Over \(\mathcal G_d\) consider the bundle \(\operatorname{Hom}(V/\mathcal U,\mathcal U)^r\). In each summand take the nonzero rank-one locus, then impose the open condition that the images of its \(r\) entries span \(\mathcal U\). The resulting relative locus is isomorphic to \(\mathcal S_d\), because the joint image span is recovered regularly on its constant-rank locus (e.g. via nonvanishing minors and Pluecker coordinates). A nonzero rank-one \(d\)-by-\((n-d)\) matrix locus is smooth and irreducible of dimension \(d+(n-d)-1=n-1\): it is the quotient of pairs of nonzero vectors and covectors by a free one-dimensional multiplicative scaling. The product of \(r\) such loci is smooth and irreducible, and the spanning condition is nonempty and open when \(d\leq r\). Locally trivializing the tautological and quotient bundles therefore proves that \(\mathcal S_d\) is smooth and irreducible with dimension \(d(n-d)+r(n-1)\).

**Top dimensions and asymptotics.** There are finitely many strata. Every maximal-dimensional irreducible component must be the closure of a maximal-dimensional stratum. Distinct strata of equal maximal dimension yield distinct component closures because each is locally closed, dense in its own closure, and the disjoint strata cannot each contain the generic point of the same irreducible component. The concave quadratic \(d(n-d)\) has one maximizing integer for even \(n\), or two adjacent maximizing integers \((n-1)/2\) and \((n+1)/2\) for odd \(n\), provided the upper candidate is within \(d\leq r\). This proves the component count. For fixed parameters, the Gaussian coefficient has leading term \(q^{d(n-d)}\), the nonzero spanning-vector count has leading term \(q^{rd}\), and \(((q^{n-d}-1)/(q-1))^r\) has leading term \(q^{r(n-d-1)}\). Each stratum thus contributes leading coefficient one and degree \(r(n-1)+d(n-d)\), proving the displayed asymptotics. The orbit-size formula follows by counting \((u,\varphi)\) with \(\varphi(u)=0\) modulo nonzero scaling.

## Verification

The bundled standalone script `verify_minimal_orbit_tuples.py` (Python standard library only) constructs the orbit by literal outer products over finite fields, directly multiplies matrices to test pairwise commutation versus mutual annihilation, enumerates ordered commuting tuples using admissibility bitsets, computes their image-span dimensions by row reduction, and compares **each** stratum count with the displayed formula. The bundled `verification_output.txt` records six passed cases, including the in-scope case \((n,r,q)=(4,3,2)\), with distribution \((5145,22680,2520)\) at image-span dimensions \((1,2,3)\) and total \(30345\). Boundary cases test dimension two, dimension three, and the extension field \(\mathbb F_4\). These tests corroborate, but cannot replace, the unrestricted proof.

## Relationship to prior work

Britnell and Wildon, *On types and classes of commuting matrices over finite fields* (2010 preprint), treat commuting **pairs of similarity classes** and which classes admit commuting representatives; their theorem statements do not give labeled ordered \(r\)-tuple counts for the fixed minimal nilpotent orbit. Ngo's *Commuting varieties of r-tuples over Lie algebras* (2012) treats multiple restricted commuting varieties, including the subregular orbit closure in \(\mathfrak{sl}_3\), but not the present all-\(n\geq4\), all-\(r\geq3\) finite-field stratum formula. Sharma (2014) counts simultaneous-conjugacy classes of arbitrary commuting tuples, a different equivalence quotient from the labeled orbit-tuple cardinalities here. Levy, Ngo and Šivic (2022), particularly Lemma 3.3, use the common-image-span/annihilator mechanism to establish dimension bounds for broad matrix varieties: this is important antecedent technique, but not the rank-one orbit-stratified exact finite-field count or its leading component multiplicity. Huang (2021) treats mutually annihilating matrix **pairs**, whereas the present higher-tuple count requires a joint image-span classification. Novelty versus every possible special case or a broader unstated consequence of this literature is not independently certified.

## Limitations

The formula is limited to ordered tuples of **nonzero rank-one square-zero** matrices. It does not count tuples allowing zero matrices or higher matrix ranks, does not classify lower-dimensional irreducible components, and does not resolve the nonreduced defining scheme. The geometric assertions are for reduced varieties, not scheme structures. No independent review or exhaustive historical-priority certification has occurred. Published methods using Grassmannian incidence are a genuine overlap risk; the asserted distinction is the complete fixed-minimal-orbit higher-tuple rank-span count together with its precise top-dimensional multiplicities.

## References

1. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811, first posted 2010-01-06; Journal of the London Mathematical Society (2011), DOI:10.1112/jlms/jdq088.
2. N. V. Ngo, *Commuting varieties of r-tuples over Lie algebras*, arXiv:1209.1659, first posted 2012-09-07.
3. U. B. Sharma, *Simultaneous Similarity Classes of Commuting Matrices over a Finite Field*, arXiv:1409.2698, first posted 2014-09-07; Linear Algebra and its Applications (2016).
4. P. D. Levy, N. V. Ngo and K. Šivic, *Commuting varieties and cohomological complexity theory*, Journal of the London Mathematical Society (2022), DOI:10.1112/jlms.12650, open-access full text.
5. Y. Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity*, arXiv:2110.15566 (2021). Only abstract-level comparison performed.
