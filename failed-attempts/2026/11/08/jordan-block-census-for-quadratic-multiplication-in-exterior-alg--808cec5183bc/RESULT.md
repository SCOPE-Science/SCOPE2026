# Jordan-block census for quadratic multiplication in exterior algebras

## Finding
Let \(k\) be a field of prime characteristic \(p\), let \(V\) have dimension \(n\geq 0\), and fix \(h\in\bigwedge^2_k V\). Let \(2r\) be the rank of the alternating bilinear coefficient matrix of \(h\), so \(0\leq r\leq\lfloor n/2\rfloor\). Consider exterior multiplication \(M_h:\bigwedge V\to\bigwedge V\), \(a\mapsto h\wedge a\). The operator is nilpotent with \(M_h^p=0\). For \(1\leq s<p\), the number \(b_s\) of size-\(s\) nilpotent Jordan blocks is
\[
 b_s=2^{n-2r}(T_p^r)_{s,1},\qquad
 T_p=2I_{p-1}+A(P_{p-1}),
\]
where \(A(P_{p-1})\) is the ordinary adjacency matrix of the path graph on \(p-1\) vertices (the single-vertex path when \(p=2\)). The remaining multiplicity is exactly
\[
 b_p=\frac{2^n-\sum_{s=1}^{p-1}s b_s}{p}.
\]
All multiplicities are nonnegative integers. In particular, Jordan type depends only on \((n,p,r)\), not on further coefficients of \(h\).

Over \(k=\mathbb F_q\) (\(q\) any power of \(p\)), there are exactly
\[
 N_{n,r}(q)=\binom{n}{2r}_q\,q^{r(r-1)}\prod_{i=1}^r(q^{2i-1}-1)
\]
homogeneous quadratic elements of alternating rank \(2r\); here the bracket denotes the Gaussian binomial coefficient. Consequently, the displayed pairs of formulas give the complete population distribution of the Jordan types of \(M_h\) for all quadratic \(h\) in every finite-field exterior algebra. If two ranks happen to yield the same Jordan type, their populations are added.

For \(n\geq 2r\), the fraction of the vector-space dimension lying in length-\(p\) Jordan blocks is
\[
 F_p(r)=\frac{p b_p}{2^n}=1-4^{-r}\sum_{s=1}^{p-1}s(T_p^r)_{s,1}.
\]
For fixed \(p\) this tends to \(1\) as \(r\to\infty\); more precisely, for \(p>2\) its deficit is asymptotic to a positive constant depending only on \(p\), multiplied by \(\bigl((2+2\cos(\pi/p))/4\bigr)^r\). At \(p=2\), the deficit is exactly \(2^{-r}\).

## Assumptions and scope
The characteristic \(p\) is prime and positive; this result holds over arbitrary fields of that characteristic, with additional counting over finite fields. The alternating rank of \(h\) is even over every field, including characteristic two. The Jordan blocks refer to the underlying ungraded linear map, although \(M_h\) raises exterior degree by two. Empty products are one, and \(T_p^0=I\). When \(r=0\), the formula gives \(2^n\) size-one blocks. No divided-power structure, coefficients of any extension field, or choice of symplectic basis is built into the statement.

## Proof
**Step 1: Alternating normal form.** Elementary alternating-form reduction gives a basis \(x_1,y_1,\ldots,x_r,y_r,z_1,\ldots,z_{n-2r}\) such that \(h=\sum_{i=1}^r x_i\wedge y_i\). This includes \(p=2\) because exterior generators still square to zero. The exterior algebra is the graded tensor product of \(r\) four-dimensional two-generator exterior factors and one exterior factor on the unused generators. As each \(x_i\wedge y_i\) has even degree, its multiplication commutes with multiplication on other factors without signs. The unused factor contributes multiplicity \(2^{n-2r}\).

**Step 2: The basic four-dimensional module.** Let \(J_s\) denote a nilpotent Jordan block of size \(s\), regarded as a module for \(k[t]/(t^p)\) with \(t\) acting by the block. On \(\bigwedge(x_i,y_i)\), multiplication by \(x_i\wedge y_i\) carries \(1\) to \(x_i\wedge y_i\) and kills \(x_i\), \(y_i\), and \(x_i\wedge y_i\). Thus the local module is \(J_2\oplus 2J_1\). On tensor products, \(t\) acts by the sum of local actions. In characteristic \(p\), its \(p\)-th power vanishes because the commuting local actions each square to zero (or directly because \(h^p=p!\) times the wedge of \(p\) distinct local terms, hence zero).

**Step 3: The key modular two-block rule.** For \(1\leq s<p\),
\[
 J_s\otimes J_2\simeq J_{s+1}\oplus J_{s-1},\qquad J_0:=0,
\]
and \(J_p\otimes J_2\simeq2J_p\), for the primitive/additive action. Indeed, on \(k[x,y]/(x^s,y^2)\), multiplication by \(x+y\) represents the tensor action. Its kernel has dimension two if \(s>1\), and one if \(s=1\); moreover \((x+y)^s=sx^{s-1}y\neq0\) for \(s<p\), giving a block of length \(s+1\) and the complementary block of length \(s-1\) by dimension and kernel dimension. When \(s=p\), the operator has \(p\)-th power zero and kernel dimension two, so its two blocks, of total dimension \(2p\), both have length \(p\). The \(J_1\) tensor factor acts trivially and preserves every block.

**Step 4: Recurrence and completeness.** Tensoring with \(J_2\oplus2J_1\) sends a nonprojective block \(J_s\), \(1\leq s<p\), to \(J_{s-1}\oplus2J_s\oplus J_{s+1}\), interpreting \(J_0=0\) and retaining \(J_p\) as projective. Existing projective blocks \(J_p\) produce only projective blocks. Hence, starting from one \(J_1\), the column of multiplicities of \(J_1,\ldots,J_{p-1}\) after \(r\) factors is exactly \(T_p^r e_1\). The leftover dimension consists exclusively of length-\(p\) blocks, proving the formula for \(b_p\) and its integrality and nonnegativity.

**Step 5: Counting forms.** To produce an alternating matrix of rank \(2r\) over \(\mathbb F_q\), choose its radical, an \((n-2r)\)-dimensional subspace, in \(\binom{n}{2r}_q\) ways. A nondegenerate alternating form on the \(2r\)-dimensional quotient can be chosen in exactly \(|\operatorname{GL}_{2r}(q)|/|\operatorname{Sp}_{2r}(q)|=q^{r(r-1)}\prod_{i=1}^r(q^{2i-1}-1)\) ways. Pullback from the quotient is bijective. Exterior quadratics correspond bijectively to alternating coefficient matrices, proving the census.

**Step 6: Asymptotic saturation.** The symmetric tridiagonal matrix \(T_p\) has eigenvectors with entries \(\sin(sj\pi/p)\) and eigenvalues \(2+2\cos(j\pi/p)\), for \(j=1,\ldots,p-1\). Its largest eigenvalue \(\lambda_1=2+2\cos(\pi/p)\) is strictly less than four, simple, and has a strictly positive eigenvector. The spectral expansion of \(\sum_s s(T_p^r)_{s,1}\) therefore has positive leading coefficient at \(\lambda_1^r\) and strictly smaller remaining eigenvalue terms. Dividing by \(4^r\) proves the sharp geometric-rate statement; for \(p=2\), \(T_2=(2)\) gives the exact deficit.

## Verification
Two independent standard-library Python checkers accompany this result. `candidate_check.py` directly constructs the full exterior-multiplication matrix, including graded signs, for **every** quadratic coefficient vector over prime fields in seven small cases: \((p,n)=(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(5,4)\), totaling \(17{,}479\) forms. For each form it compares all powers against an independent subset-incidence rank formula and independently counts alternating-matrix ranks. It also checks finite-field form totals over \(q=2,3,4,5,8,9\), with \(1\leq n\leq11\). `tridiag_check.py` cross-checks the path-power formula against the subset-incidence expression for \(605\) parameter triples \((n,r,p)\), with \(0\leq n\leq20\) and \(p\in\{2,3,5,7,11\}\), and verifies the free-block dimension fractions in additional cases. The recorded outputs end with `QUADRATIC_EXTERIOR_JORDAN_WILSON_PASS` and `QUADRATIC_EXTERIOR_TRIDIAGONAL_PASS`. These finite tests are not used in place of the unrestricted proof.

## Relationship to prior work
Nguyen (arXiv:1406.0489, 2014), especially Theorem 1.1 and its proof, supplies the quadratic exterior-algebra context and already uses the rank normal form to characterize when the quotient by a quadratic is Koszul; neither the normal form nor the Koszul criterion is claimed new here. Glasby, Praeger and Xia (arXiv:1403.4685, 2014) study modular Jordan partitions under tensor products, with earlier Green-ring tensor rules summarized in their introduction; no novelty is claimed for these elementary modular tensor decompositions. The present finite-field **population by exterior-multiplication Jordan type** and the path-power and sharp free-block saturation formulas are the assessed contributions. Theorem 1.1 in Nguyen concerns Koszulness rather than the complete Jordan populations; the modular tensor results classify given tensor-block pairs rather than counting alternating forms across dimensions. Cook (arXiv:1111.4979) studies positive-characteristic Lefschetz properties of monomial complete intersections, and Carlson--Friedlander--Pevtsova (arXiv:1106.4474) study Jordan types of elementary abelian group representations; their settings motivate care about modular ranks but are not being restated as new results. A stronger, unidentified theorem on modular symplectic Lefschetz modules or Green-ring exterior powers might imply this entire statement; historical priority is not independently certified.

## Limitations
The theorem treats exterior multiplication by homogeneous degree-two elements, not arbitrary inhomogeneous multipliers or higher-degree forms. It concerns ordinary (ungraded) Jordan multiplicities; graded block starting degrees are not determined here. The asymptotics fix the characteristic while alternating rank grows and do not assert uniformity as the prime varies. The novelty assessment is literature-based and not a proof that all prior mathematical literature has been excluded. There has been no independent mathematical audit.

## References
1. Hop D. Nguyen, *Koszul hypersurfaces over the exterior algebras*, arXiv:1406.0489 (first submitted 2014-06-02), https://arxiv.org/abs/1406.0489.
2. S. P. Glasby, C. E. Praeger, B. Xia, *Decomposing modular tensor products: Jordan partitions, their parts and p-parts*, arXiv:1403.4685 (first submitted 2014-03-19), https://arxiv.org/html/1403.4685v2.
3. D. Cook II, *The Lefschetz properties of monomial complete intersections in positive characteristic*, arXiv:1111.4979, https://arxiv.org/abs/1111.4979.
4. J. F. Carlson, E. M. Friedlander, J. Pevtsova, *Representations of elementary abelian p-groups and bundles on Grassmannians*, arXiv:1106.4474, https://arxiv.org/abs/1106.4474.
5. A. Iarrobino, P. Macias Marques, C. McDaniel, *Artinian algebras and Jordan type*, arXiv:1802.07383, https://arxiv.org/html/1802.07383v6.
