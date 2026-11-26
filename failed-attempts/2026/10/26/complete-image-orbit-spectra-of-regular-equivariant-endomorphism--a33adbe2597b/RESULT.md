# Complete image-orbit spectra of regular equivariant endomorphisms of finite abelian group sets

## Finding
Let \(G\) be any finite abelian group, including the trivial group, and \(X\) a finite \(G\)-set. For each subgroup \(H\leq G\), let \(m_H\) be the number of labeled \(G\)-orbits of \(X\) isomorphic to \(G/H\), and let \(w_H=[G:H]\). Fix integers \(0\leq r_H\leq m_H\) and set
\[
B_H(\mathbf r)=\sum_{K\supsetneq H} w_Kr_K.
\]
The number of **von Neumann regular** \(G\)-equivariant endomorphisms \(f:X\to X\) whose image contains exactly \(r_H\) entire orbits with stabilizer \(H\), simultaneously for every \(H\), is
\[
\boxed{N_G(\mathbf m;\mathbf r)=\prod_{H\leq G}\left[\binom{m_H}{r_H}\sum_{j=0}^{r_H}(-1)^{r_H-j}\binom{r_H}{j}\bigl(B_H(\mathbf r)+w_Hj\bigr)^{m_H}\right]}
\]
The convention is \(0^0=1\). Thus the multivariate image-orbit polynomial of the regular part of \(\operatorname{End}_G(X)\) is
\[
\sum_{0\leq\mathbf r\leq\mathbf m}N_G(\mathbf m;\mathbf r)\prod_{H\leq G}z_H^{r_H}.
\]
The empty \(G\)-set gives the constant polynomial \(1\). Image cardinality is recovered by the substitution \(z_H=t^{w_H}\).

For \(G=C_p\) of prime order \(p\), suppose \(X\) has \(a\geq1\) fixed points and \(b\geq0\) free orbits. The total number of regular endomorphisms is
\[
\boxed{R_{p,a,b}=\sum_{r=1}^{a}\binom ar r!S(a,r)(r+pb)^b,}
\]
where \(S(a,r)\) denotes a Stirling number of the second kind. Out of \(a^a(a+pb)^b\) endomorphisms, the limiting regular proportion as \(b\to\infty\) is
\[
\boxed{\frac{1}{a^a}\sum_{r=1}^a\binom ar r!S(a,r)\exp\bigl((r-a)/p\bigr).}
\]
For example, at \(p=a=2\) this limit equals \((1+e^{-1/2})/2\), strictly between zero and one. This persistence does not follow from the total-monoid cardinality alone.

## Assumptions and scope
All sets, groups, and subgroup lattices are finite. Abelianity makes each orbit stabilizer constant along the orbit and each subgroup uniquely index its transitive orbit type. The tuple \(\mathbf r\) is indexed over **all** subgroups, with zero counts allowed. An endomorphism is von Neumann regular when some \(g\in\operatorname{End}_G(X)\) satisfies \(fgf=f\); it is not required to be an idempotent or bijection.

## Proof
**1. Equivariant orbit maps.** A map \(G/H\to G/K\) is \(G\)-equivariant if and only if \(H\subseteq K\), and then the image of the identity coset can be any of the \(w_K\) cosets in \(G/K\). Every such map is surjective. Consequently, an endomorphism is uniquely specified by choosing one target point for each source orbit among the admissible target orbits.

**2. Regularity criterion.** Let \(Y=\operatorname{im}f\). If \(fgf=f\), then \(f(g(y))=y\) for every \(y\in Y\); equivariance makes \(g\) an equivariant section of \(f\) on \(Y\). Thus every image orbit with stabilizer \(H\) has a preimage orbit with equal stabilizer \(H\): if \(f(x)=y\), then \(G_x\subseteq G_y\), and equivariance of the section gives the reverse inclusion for the selected section point. Conversely, suppose each image orbit admits an equal-stabilizer preimage orbit. The restriction of \(f\) to that preimage orbit is an equivariant isomorphism; its inverse specifies \(g\) on the image orbit. Define \(g\) to be the identity on orbits outside \(Y\). The resulting equivariant map satisfies \(fgf=f\). This known criterion is used as a lemma, not claimed to be new (Castillo-Ramírez and Gadouleau, Theorem 3, for finite full shifts).

**3. Choose images and count.** For a prescribed \(\mathbf r\), independently select the \(r_H\) image orbits of each type \(H\) in \(\binom{m_H}{r_H}\) ways. For each source orbit of type \(H\), a target point can lie in a selected strict-supergroup orbit (\(B_H(\mathbf r)\) choices), or in one of the \(r_H\) selected equal-type orbits (\(w_Hr_H\) choices). An image \(H\)-orbit has an equal-stabilizer preimage exactly when at least one source \(H\)-orbit maps to it. Inclusion–exclusion over the \(r_H\) mandatory equal-type target orbits counts the allowable choices for the \(m_H\) source \(H\)-orbits as
\[
\sum_{j=0}^{r_H}(-1)^{r_H-j}\binom{r_H}{j}(B_H(\mathbf r)+w_Hj)^{m_H}.
\]
The events factor across distinct source stabilizer types. Their product is the stated formula. Each resulting function has exactly the selected image orbits, since all selected orbits receive equal-type source images and no unselected target orbit is used. Conversely every regular endomorphism yields one and only one such set of selections and source-orbit maps; no overcounting occurs.

**4. Prime cyclic specialization.** There are \(a\) fixed source points and \(b\) free source orbits. A regular map's fixed-point restriction has a nonempty image of size \(r\), counted by \(\binom ar r!S(a,r)\). Each free source orbit may independently map to any of the \(r\) selected fixed points or one of the \(b\) free target orbits with \(p\) phases, giving \((r+pb)^b\). Any free orbit in the image automatically has an equal-type antecedent, so these choices are precisely the regular maps. The unrestricted count is \(a^a(a+pb)^b\); division and \((r+pb)^b/(a+pb)^b\to\exp((r-a)/p)\) establish the limit. For \(a=0\), all equivariant endomorphisms of the free \(G\)-set are regular; the displayed asymptotic fraction is asserted only for \(a\geq1\).

## Verification
A separate finite exhaustive checker constructs cosets and actions for small abelian groups, enumerates every equivariant map by its images on orbit representatives, and independently tests regularity using a full search for a witness \(g\) satisfying \(fgf=f\). The resulting orbit-image histograms equal the formula in all tested cases: \(G=C_2\) with \((m_G,m_1)=(2,1)\) and \((2,2)\); \(G=C_4\) with one orbit of each stabilizer order \(4,2,1\); and \(G=C_2\times C_2\) with two fixed orbits and one orbit of each other stabilizer type. In aggregate the checker enumerates \(3253\) equivariant endomorphisms, \(1793\) of them regular. It also independently checks the unrestricted-count normalization. The proof, not this finite enumeration, establishes the arbitrary-size theorem. Run \(\texttt{python3 verify_regular_gsets.py}\) using the bundled standard-library Python script.

## Relationship to prior work
Castillo-Ramírez and Gadouleau (2017, Theorem 3) established the regularity criterion for cellular automata on finite full shifts. Castillo-Ramírez and Ruiz-Medina (2022) determined relative generating ranks of finite \(G\)-set endomorphism monoids, not regular-element image spectra. Ruiz-Medina (2025, Theorem 5) gives total cardinalities of these monoids, not the regular-stratum distribution. The present contribution is the simultaneous complete subgroup-indexed **enumeration** and its nontrivial prime-cyclic limiting proportion. These results are compatible with the cited structural results but do not follow as numerical identities from their displayed totals; the image-selection and occupancy calculation is essential.

## Limitations
This formula concerns **finite abelian** groups and finite \(G\)-sets. It does not count regular elements of arbitrary nonabelian equivariant transformation monoids. The prime-cyclic limiting statement holds for fixed \(p,a\) as \(b\) tends to infinity; it is not a joint large-group limit. Searches and source inspections do not constitute exhaustive priority certification, and an equivalent unindexed enumeration could exist. Computational tests cover only explicitly listed finite cases. No independent audit has been performed.

## References
- A. Castillo-Ramírez and M. Gadouleau, *Von Neumann Regular Cellular Automata*, arXiv:1701.02692, first public 2017-01-10; see Theorem 3.
- A. Castillo-Ramírez and R. H. Ruiz-Medina, *The relative rank of the endomorphism monoid of a finite G-set*, arXiv:2203.12158, first public 2022-03-23; see Theorem 1 and Section 2.
- R. H. Ruiz-Medina, *Cardinalities in finite monoids of G-equivariant functions*, arXiv:2503.03772, first public 2025-03-04; see Theorems 5 and 7.
- R. H. Ruiz-Medina and V. M. Lara-Gómez, *Green relations over finite monoids of G-equivariant functions*, arXiv:2503.14511, first public 2025-03-10.
