# Exact idempotent-derivation rank spectrum and a nonsplit limiting mass for finite matrix algebras

## Finding

For an integer \(n\ge2\) and a prime power \(q\), set \(A=M_n(\mathbb F_q)\), and let \(\mathcal I_n(q)\) be the set of all \(\mathbb F_q\)-linear derivations \(D:A\to A\) with \(D^2=D\). Derivation rank always means the \(\mathbb F_q\)-linear rank of \(D\), *not* the rank of a representing matrix.

If \(q\) is odd, \(\mathcal I_n(q)=\{0\}\). If \(q\) is even, write \(G_s(q)=\prod_{i=0}^{s-1}(q^s-q^i)\), with \(G_0(q)=1\), and \({n\brack r}_q\) for the Gaussian binomial coefficient. For each integer \(0\le r<n/2\), exactly
\[
{n\brack r}_q q^{r(n-r)}
\]
distinct derivations have rank \(2r(n-r)\). If \(n=2m\), then exactly
\[
\frac12\left({2m\brack m}_q q^{m^2}+\frac{G_{2m}(q)}{G_m(q^2)}\right)
\]
additional derivations have rank \(2m^2\); there are no other ranks. In particular, for every even \(q\),
\[
|\mathcal I_n(q)|=\frac12\left(\sum_{r=0}^n{n\brack r}_q q^{r(n-r)}+{\boldsymbol 1}_{2\mid n}\frac{G_n(q)}{G_{n/2}(q^2)}\right).
\]
The last summand counts the nonsplit quadratic type and is included only for even \(n\).

For fixed \(q\) even and \(n=2m\to\infty\), put
\[
\Delta_q=\prod_{i=1}^{\infty}(1-q^{-i}),\qquad \Theta_q=\sum_{k\in\mathbb Z}q^{-2k^2},\qquad \beta_q=\frac{\Delta_q^2}{\prod_{i=1}^{\infty}(1-q^{-2i})}.
\]
Then
\[
|\mathcal I_{2m}(q)|\sim\frac{q^{2m^2}}{2\Delta_q}(\Theta_q+\beta_q),
\qquad
\Pr(\text{nonsplit type})\longrightarrow\frac{\beta_q}{\Theta_q+\beta_q}>0.
\]
If \(D\) is uniform on \(\mathcal I_{2m}(q)\), the rank deficit \(2m^2-\operatorname{rank}D\) converges in total variation to the law with mass \((1+\beta_q)/(\Theta_q+\beta_q)\) at \(0\) and mass \(2q^{-2k^2}/(\Theta_q+\beta_q)\) at \(2k^2\) for every integer \(k\ge1\). There is no mass elsewhere. The nonsplit limit is approximately \(0.07435748735\) when \(q=2\), and \(0.31099575290\) when \(q=4\).

## Assumptions and scope

All derivations are \(\mathbb F_q\)-linear and satisfy the associative Leibniz rule. The matrix algebra is unital. The count is of **distinct operators on the fixed algebra**, not of isomorphism classes of gradings or similarity classes of their generators. An idempotent derivation gives a \(\mathbb Z/2\mathbb Z\)-grading in characteristic two by its zero and one eigenspaces. These gradings and their split/nonsplit *types* were studied previously; the contribution here is their complete **labeled rank distribution** and quantitative limiting law.

The label “split” means the associated quadratic polynomial has a root in \(\mathbb F_q\) after scalar translation, and “nonsplit” means it is irreducible. This distinction is invariant under replacing the inner generator by a scalar matrix. No nonsplit type exists for odd \(n\).

## Proof

**1. Reduction to inner generators.** Every derivation of \(M_n(\mathbb F_q)\) is inner. For completeness, with matrix units \(E_{ij}\), the matrix \(B=\sum_k D(E_{k1})E_{1k}\) satisfies \(D(E_{ij})=[B,E_{ij}]\) by applying the Leibniz rule to products of matrix units; linearity gives \(D=\operatorname{ad}_B\). The map \(B\mapsto\operatorname{ad}_B\) has kernel the scalar matrices, since these are precisely the central matrices.

**2. Odd characteristic.** The pairing \(\langle X,Y\rangle=\operatorname{tr}(XY)\) is nondegenerate on the matrix algebra, and every inner derivation \(D\) is skew-adjoint: \(\langle DX,Y\rangle=-\langle X,DY\rangle\). If \(D^2=D\), then \(A=\ker D\oplus\operatorname{im}D\), and \(\operatorname{im}D\) is orthogonal to \(\ker D\) and, because \(2\ne0\), also to itself. Hence \(\operatorname{im}D\) is orthogonal to all of \(A\), so \(D=0\).

**3. Characteristic two classification.** In characteristic two, a direct expansion gives \(\operatorname{ad}_B^2=\operatorname{ad}_{B^2}\). Thus \(D^2=D\) is equivalent to \(B^2+B=cI\) for some \(c\in\mathbb F_q\). Replacing \(B\) by \(B+tI\) replaces \(c\) by \(c+t^2+t\). The additive subgroup \(\{t^2+t:t\in\mathbb F_q\}\) has index two. If \(c\) lies in it, translate \(B\) to an idempotent \(P\). The two idempotents with the same adjoint derivation are \(P\) and \(P+I\); their vector-space ranks add to \(n\). If \(c\) is outside that subgroup, fix one such \(c_0\). Every relevant \(B\) can be translated to solve \(B^2+B=c_0I\). The polynomial \(T^2+T+c_0\) is irreducible and separable, so \(\mathbb F_q^n\) becomes a vector space over \(\mathbb F_{q^2}\); therefore \(n=2m\) and all these \(B\) belong to a single \(\mathrm{GL}_{2m}(q)\)-conjugacy class with centralizer \(\mathrm{GL}_{m}(q^2)\). In this fixed polynomial class each derivation has exactly two representatives, \(B\) and \(B+I\), because the roots of \(t^2+t\) in the base field are exactly \(0,1\).

**4. Counts and ranks.** A rank-\(r\) idempotent \(P\) is uniquely an ordered direct-sum decomposition \(\mathbb F_q^n=\operatorname{im}P\oplus\ker P\). Choose its image in \({n\brack r}_q\) ways and choose a complementary subspace in \(q^{r(n-r)}\) ways. The commutant of \(P\) consists of its two diagonal endomorphism blocks, so \(\operatorname{rank}(\operatorname{ad}_P)=n^2-r^2-(n-r)^2=2r(n-r)\). The involution \(P\mapsto P+I\) identifies ranks \(r\) and \(n-r\), pairing all idempotents without fixed points. For \(n=2m\), the middle rank therefore contributes half the number of middle-rank projectors. A nonsplit generator has centralizer algebra \(M_m(\mathbb F_{q^2})\), of base-field dimension \(2m^2\), and so contributes derivation rank \(4m^2-2m^2=2m^2\). Orbit–stabilizer and the two scalar representatives yield \(G_{2m}(q)/(2G_m(q^2))\). All stated exact formulas follow.

**5. Sharp limiting distribution.** Set \(n=2m\). Standard product expansion gives
\[
{2m\brack m+k}_q q^{(m+k)(m-k)}=q^{2m^2-2k^2}\frac{\prod_{i=m-k+1}^{2m}(1-q^{-i})}{\prod_{i=1}^{m+k}(1-q^{-i})}
\]
for \(-m\le k\le m\). For fixed \(k\) the product ratio tends to \(1/\Delta_q\), and uniformly it is at most \(1/\Delta_q\). The summable dominating sequence \(q^{-2k^2}/\Delta_q\) therefore permits dominated convergence over the moving rank range. Independently,
\[
\frac{G_{2m}(q)}{G_m(q^2)}=q^{2m^2}\frac{\prod_{i=1}^{2m}(1-q^{-i})}{\prod_{i=1}^{m}(1-q^{-2i})}
\sim q^{2m^2}\frac{\Delta_q}{\prod_{i\ge1}(1-q^{-2i})}.
\]
Insert these into the exact count, divide by \(q^{2m^2}/(2\Delta_q)\), and obtain \(\Theta_q+\beta_q\). The split pair \(m\pm k\) has deficit \(2k^2\); the nonsplit class has deficit zero. Dividing each contribution by the total yields the asserted mass function and nonsplit probability. The same uniform summable bound, with the nonsplit contribution treated separately, implies convergence of the entire discrete distribution in total variation.

## Verification

The standalone file `verify.py` enumerates every scalar-equivalence class of candidate inner generators for \((n,q)=(2,2),(3,2),(4,2),(2,4)\), using \(B_{11}=0\) as a unique scalar-class representative. It independently checks the quadratic equation, builds the full \(n^2\times n^2\) matrix of the induced commutator derivation, checks its idempotence directly, and computes rank by finite-field Gaussian elimination. Complete observed histograms were respectively \(\{0:1,2:4\}\), \(\{0:1,4:28\}\), \(\{0:1,6:120,8:336\}\), \(\{0:1,2:16\}\), exactly as predicted; the program prints `VERIFY_OK`. These finite checks corroborate but do not establish the all-dimension theorem. The infinite claims are proved in the preceding steps.

## Relationship to prior work

Ayupov and Arzikulov (2017) study local and inner derivations of associative matrix rings; they do not enumerate idempotent derivations. Eick and Moede (2022), Section 2.1, use \(\operatorname{ad}_x^2=\operatorname{ad}_x\) in characteristic two to construct \(\mathbb Z_2\)-gradings of Lie algebras, and present an enumeration algorithm for certain small simple Lie algebras. The fundamental correspondence between idempotent derivations and characteristic-two gradings is **not new**. Caenepeel, Dăscălescu and Năstăsescu (2001) already classify matrix-algebra cyclic gradings up to isomorphism using descent; their Theorem 3.4 and Example 3.8 explicitly identify the split/nonsplit quadratic distinction in characteristic two. Diniz and Pellegrino (2020) count **isomorphism classes** of matrix-algebra gradings, not fixed-algebra derivations sampled uniformly. The present statement concerns exact numbers at each **operator rank** over all finite binary fields, including a positive limiting fraction of nonsplit gradings. Previously known grading types and the underlying orbit-stabilizer method are credited as input, not claimed as original.

## Limitations

The result concerns ordinary \(\mathbb F_q\)-linear associative derivations of full matrix algebras. It does not classify arbitrary derivations of other algebras or arbitrary gradings over infinite fields. Asymptotics require a fixed field order \(q\) and even matrix size tending to infinity. A recent paper, Diniz et al. (2026), *Identities and isomorphisms of finite graded matrix algebras* (arXiv:2610.20113), was located at abstract level but its full text was not accessible. This creates a residual priority risk, especially as complete classification of grading types is long established. More comprehensive novelty verification and independent mathematical audit remain outstanding.

## References

1. S. Ayupov and F. Arzikulov, *Two-Local derivations on associative and Jordan matrix rings over commutative rings*, arXiv:1705.09910, initial public version 2017-05-28. https://arxiv.org/abs/1705.09910
2. B. Eick and T. Moede, *Computing subalgebras and \(\mathbb Z_2\)-gradings of simple Lie algebras over finite fields*, arXiv:2205.03155, 2022. https://arxiv.org/html/2205.03155v2
3. S. Caenepeel, S. Dăscălescu, and C. Năstăsescu, *On gradings of matrix algebras and descent theory*, arXiv:math/0107148, 2001. https://arxiv.org/abs/math/0107148
4. D. Diniz and D. Pellegrino, *On the Number of Gradings on Matrix Algebras*, arXiv:2004.02285, 2020. https://arxiv.org/abs/2004.02285
5. D. Diniz et al., *Identities and isomorphisms of finite graded matrix algebras*, arXiv:2610.20113, 2026 (abstract available, full text not inspected). https://arxiv.org/abs/2610.20113
