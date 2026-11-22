# The annihilator-line strata of cubic exterior multipliers in characteristic two

## Finding
Let \(k\) have characteristic \(2\), let \(V\) be a \(k\)-vector space of dimension \(n\ge5\), and write \(E=\bigwedge_k V\). For a nonzero cubic \(f\in\bigwedge^3V\), put
\[
A_1(f)=\{v\in V:v\wedge f=0\},\qquad d_f(z)=f\wedge z.
\]
The locus \(\mathcal Z_n\) of cubics with \(A_1(f)\ne0\), including the zero cubic, is a closed irreducible subvariety of \(\bigwedge^3V\) of dimension \(\binom n2\). Every nonzero member belongs to exactly one of the following strata, indexed by \(1\le s\le\lfloor(n-1)/2\rfloor\):

* \(s=1\): \(f\) is decomposable, \(\dim A_1(f)=3\), and \(f\) is equivalent under \(\operatorname{GL}(V)\) to \(e_1\wedge e_2\wedge e_3\).
* \(s\ge2\): \(\dim A_1(f)=1\), and \(f\) is equivalent to
\[
f=e_1\wedge\sum_{i=1}^{s}e_{2i}\wedge e_{2i+1}.
\]

For every such \(f\), the complete graded multiplication-rank polynomial is
\[
\boxed{\sum_{j=0}^n\operatorname{rank}\bigl(d_f:\bigwedge^jV\to\bigwedge^{j+3}V\bigr)t^j
=\frac{(1+t)^{n-1}-(2t)^s(1+t)^{n-1-2s}}{1+t^2}.}
\]
(The quotient on the right is an integer polynomial.) In particular,
\[
\boxed{\operatorname{rank}(d_f)=2^{n-2}-2^{n-s-2}.}
\]

For \(k=\mathbb F_q\) with \(q\) a power of \(2\), the exact numbers of **labeled nonzero cubics** in these strata are
\[
\boxed{N_{n,q}(1)=(q-1){n\brack3}_q,\qquad
N_{n,q}(s)={n\brack1}_q{n-1\brack2s}_q\frac{|\operatorname{GL}_{2s}(\mathbb F_q)|}{|\operatorname{Sp}_{2s}(\mathbb F_q)|},\quad s\ge2.}
\]
Here \({a\brack b}_q\) is the Gaussian binomial coefficient. The nonzero \(s\ge2\) rank strata are smooth and geometrically irreducible, of dimensions \(n-1+s(2n-2s-3)\); the decomposable nonzero stratum has dimension \(3n-8\).

For illustration, in \(n=6\) every cubic outside \(\mathcal Z_6\) has total multiplication rank \(14\). Over \(\mathbb F_2\), the rank distribution on *all* \(2^{20}\) cubic elements is \(0:1,\ 8:1395,\ 12:54684,\ 14:992496\). This six-dimensional binary census is a consequence of older trivector-orbit work and is used as a consistency check, not as a separate priority claim.

## Assumptions and scope
All algebra and geometry statements are for fields of characteristic \(2\) and \(n\ge5\). We use the alternating exterior algebra, including in characteristic \(2\), where \(v\wedge v=0\) remains a defining relation. A cubic is **labeled** when its coefficients are counted with a fixed basis, without identifying scalar multiples or \(\operatorname{GL}(V)\)-orbits. The total rank is the rank of the linear map on the full \(2^n\)-dimensional exterior algebra, not the rank of the cubic tensor or of a single graded component. The Gaussian coefficient is \({a\brack b}_q=\prod_{i=0}^{b-1}(q^{a-i}-1)/(q^{b-i}-1)\), and \(|\operatorname{Sp}_{2s}(\mathbb F_q)|=q^{s^2}\prod_{i=1}^s(q^{2i}-1)\).

## Proof
**Annihilator dichotomy.** If \(0\ne v\in A_1(f)\), choose a splitting \(V=kv\oplus W\), and uniquely write \(f=v\wedge\omega+\tau\) with \(\omega\in\bigwedge^2W\) and \(\tau\in\bigwedge^3W\). Wedge multiplication by \(v\) is injective on \(\bigwedge^3W\), so \(v\wedge f=0\) forces \(\tau=0\). If another vector \(w\) independent of \(v\) annihilates \(f\), the same splitting argument gives \(f=v\wedge w\wedge u\). Since \(f\ne0\), \(u,v,w\) are independent, and the annihilator is exactly their three-space. Conversely, if the bivector \(\omega\) has rank greater than \(2\), then it is not decomposable, and no second independent annihilator can exist. Every bivector over a field has an alternating normal form of even rank \(2s\), which gives the displayed canonical cubics and uniqueness of \(s\).

**Graded multiplication ranks.** Write \(f=v\wedge\omega\) as above, with \(\dim W=m=n-1\). The direct decomposition \(\bigwedge V=\bigwedge W\oplus v\wedge\bigwedge W\) shows that \(d_f\) has precisely the ranks of \(d_\omega:z\mapsto\omega\wedge z\) on \(\bigwedge W\), shifted into the second summand. Choose symplectic pairs in \(W\), so \(\omega=\sum_{i=1}^{s}x_i\wedge y_i\), plus \(m-2s\) unused generators. The complex \((\bigwedge W,d_\omega)\) is the tensor product, over \(k\), of \(s\) four-dimensional complexes with differential \(1\mapsto x_i\wedge y_i\) and homology represented by \(x_i,y_i\), together with an exterior algebra on \(m-2s\) inactive generators. The tensor differential is the sum of the local differentials because the characteristic is \(2\). The Künneth theorem over a field gives graded homology series \(H(t)=(2t)^s(1+t)^{m-2s}\). If \(R(t)\) records ranks from degree \(j\) to \(j+2\), the equality \(\dim\bigwedge^jW=R_j+H_j+R_{j-2}\) implies \((1+t)^m=H(t)+(1+t^2)R(t)\). This proves the polynomial and its specialization at \(t=1\), since \(d_\omega^2=0\).

**Finite-field counts.** Nonzero decomposable cubics are indexed by three-spaces and their nonzero top-wedge scalars, giving \((q-1){n\brack3}_q\). For \(s\ge2\), the annihilating line \(L=A_1(f)\) is uniquely determined. For fixed \(L\), choosing any generator \(v\) identifies the vector space of divisible cubics with \(\bigwedge^2(V/L)\). Rank-\(2s\) alternating bivectors on the \((n-1)\)-dimensional quotient are counted by first choosing the radical \((n-1-2s)\)-space and then a nondegenerate alternating form on the quotient. The count is \({n-1\brack2s}_q|\operatorname{GL}_{2s}|/|\operatorname{Sp}_{2s}|\). There are \({n\brack1}_q\) choices of \(L\), with no overlap between them.

**Geometry.** The incidence locus \(\{(L,f):L\in\mathbb P(V),\ L\wedge f=0\}\) is a vector bundle with fiber \(L\otimes\bigwedge^2(V/L)\), of rank \(\binom{n-1}{2}\). Its image in \(\bigwedge^3V\) is closed because projection from \(\mathbb P(V)\times\bigwedge^3V\) is proper; it is irreducible. For \(n\ge5\), a dense open set has bivector rank at least \(4\), hence a unique annihilator line, so the image has dimension \(n-1+\binom{n-1}{2}=\binom n2\). On each rank-\(2s\) stratum with \(s\ge2\), its inverse line \(A_1(f)\) varies algebraically as the kernel of a constant-rank linear map, making the stratum isomorphic to the rank-\(2s\) alternating-bivector bundle over \(\mathbb P(V)\). Its fibers are smooth geometrically irreducible alternating-form orbits of dimension \(s(2(n-1)-2s-1)\). The cone of nonzero decomposable cubics is the complement of the zero section in the tautological line bundle over \(\operatorname{Gr}(3,V)\); its dimension is \(3(n-3)+1\).

**Six generators.** For \(n=6\), every cubic with \(A_1(f)=0\) gives an injective \(V\to\bigwedge^4V\). Wedge-pairing with the top degree identifies the \(\bigwedge^2V\to\bigwedge^5V\) block with its dual, so both blocks have rank \(6\); the degree-zero and degree-three blocks each have rank \(1\), giving total rank \(14\). Subtracting the two finite-field annihilator strata and zero from \(q^{20}\) gives the residual count, which for \(q=2\) agrees with the displayed direct census.

## Verification
The standalone file `verify_cubic.py` calculates exterior multiplication directly in monomial bases over \(\mathbb F_2\), independently of the tensor-product proof. It exhausts all \(2^{20}\) six-generator cubic elements to count ranks of their degree-one wedge-annihilator maps, checks all three nonzero multiplier-rank profiles in dimension six, and tests divisible-cubic profiles in dimensions \(5\) through \(8\). Execute `python3 verify_cubic.py` and compare the output to `verification_output.txt`. The run terminates in `CUBIC_EXTERIOR_DIRECT_GF2_PASS`. These finite computations are independent checks of concrete instances, not a proof over all dimensions or fields.

## Relationship to prior work
Gow (1997) established middle-degree homology for a symplectic contraction differential on exterior powers in characteristic two. Maliakas's arXiv preprint (2006) discusses that result and analyzes a different differential on the divided-power algebra. We use the established two-form phenomenon as motivation, but the exact all-dimensional cubic **annihilator-line strata**, their finite-field populations, and graded exterior multiplication profiles are distinct claims. Revoy's classification of six-dimensional trivectors, restated and extended by De Bruyn and Kwiatkowski (2011), and Shaw's work on the five binary six-dimensional trivector orbits cover the six-dimensional orbit structure; hence the binary example is explicitly not asserted to be a historically new census. De Bruyn (2011) studies arbitrary-dimensional polyvectors and projective Grassmannian hyperplanes, emphasizing the six-dimensional classification, not the uniform cubic multiplier-rank and counting formulas here. A literature and published-results search found no direct statement of the combined all-dimensional theorem, but priority is not certified and a broader unnoticed source remains possible.

## Limitations
The theorem classifies cubic multipliers with a **nonzero degree-one wedge annihilator**; it does not classify all cubics for \(n\ge7\), nor the singularity or scheme structure of the closed divisibility locus. The \(n=6\) full rank census is an independently checked consequence of the narrower theory and pre-existing orbit classification, not an original orbit theorem. No independent mathematical audit or exhaustive historical-priority certification has occurred.

## References
1. R. Gow, *Contraction of Exterior Powers in Characteristic 2 and the Spin Module*, Geometriae Dedicata 64 (1997), 283–295. DOI: 10.1023/A:1004961421891.
2. M. Maliakas, *On the Divided Power Algebra and the Symplectic Group in Characteristic 2*, arXiv:math/0606074v1, publicly posted 2006-06-03. https://arxiv.org/abs/math/0606074.
3. B. De Bruyn and M. Kwiatkowski, *On the trivectors of a 6-dimensional symplectic vector space*, Linear Algebra and its Applications 435 (2011), 289–306. DOI: 10.1016/j.laa.2011.01.028. Open manuscript: https://biblio.ugent.be/publication/2027021/file/2027033.pdf.
4. B. De Bruyn, *On polyvectors of vector spaces and hyperplanes of projective Grassmannians*, Linear Algebra and its Applications 435 (2011), 1055–1084. DOI: 10.1016/j.laa.2011.02.031. Open manuscript: https://biblio.ugent.be/publication/2027054/file/2027058.pdf.
5. R. Shaw, *Trivectors and cubics: PG(5, 2) aspects*, Journal of Geometry 99 (2011), 167–178. DOI: 10.1007/s00022-011-0060-8.
