# Frobenius-quintic zero-rank locus for genus-seven cyclic trigonal curves

## Finding
Let \(k\) be an algebraically closed field of characteristic \(2\). Write
\[
f(x)=x^8+a_7x^7+a_6x^6+a_5x^5+a_4x^4+a_3x^3+a_2x^2+a_1x+a_0
\]
for any **squarefree** monic octic and let \(C_f\) be the smooth projective model of \(y^3=f(x)\). Put
\[
H=\begin{pmatrix}a_3&a_2\\a_7&a_6\end{pmatrix},\qquad
Q=H^{[4]}H,
\]
where \(H^{[4]}\) is the matrix obtained by taking the fourth power of **each entry** (not the usual fourth matrix power). Let \(\mathcal C\) denote the Cartier operator on the seven-dimensional space of regular differentials, and write \(r_n=\dim_k\operatorname{im}\mathcal C^n\).

There are exactly four mutually exclusive cases:

| Coefficient condition | Ranks \((r_1,r_2,r_3,r_4,r_5,\ldots)\) | Jacobian \(2\)-rank |
| --- | --- | --- |
| \(\det H\ne0\) | \((4,4,4,4,4,\ldots)\) | \(4\) |
| \(\det H=0,\ H\ne0,\ Q\ne0\) | \((4,3,2,2,2,\ldots)\) | \(2\) |
| \(H\ne0,\ Q=0\) | \((4,3,2,1,0,\ldots)\) | \(0\) |
| \(H=0\) | \((4,2,0,0,0,\ldots)\) | \(0\) |

The genus is \(7\), and the Jacobian \(a\)-number is **always \(3\)**; that initial Cartier-rank constancy follows already from the general cyclic-cover theorem of Elkin and is not claimed as new. Each of the four iterate profiles occurs for a squarefree octic.

Furthermore, in the affine eight-dimensional space of monic squarefree octics, the reduced Jacobian-\(2\)-rank-zero locus is **irreducible of codimension two**. In the four coefficients defining \(H\), it is the affine cone over the smooth rational quintic
\[
\varphi:\mathbb P^1\hookrightarrow\mathbb P^3,\qquad
[s:t]\longmapsto[st^4:t^5:s^5:s^4t]
\]
(in projective coordinate order \([a_3:a_2:a_7:a_6]\)), times the freely varying four remaining coefficient coordinates, intersected with the squarefree open locus. Its singular locus is exactly the intersection with \(H=0\). The rank-\(2\) stratum is the open complement of this cone within the irreducible hypersurface \(\det H=0\), and rank \(4\) is the dense open complement. This description concerns the marked affine polynomial family, not a coarse unmarked moduli quotient.

## Assumptions and scope
The field is algebraically closed, perfect, and of characteristic \(2\). The polynomial has exact degree \(8\), leading coefficient \(1\), and no repeated root. The smooth projective curve is the unique normalization of the affine model. The \(2\)-rank is the stable image dimension of Cartier (equivalently the geometric \(2\)-torsion rank of the Jacobian). The locus statements refer to the **reduced** algebraic subvarieties of the open coefficient space, not to an asserted scheme structure of a moduli-stack stratum.

## Proof
**Genus and differentials.** The separable Kummer cover \(C_f\to\mathbb P^1_x\) of degree \(3\) is totally ramified above the eight simple finite branch points and above infinity, since \(8\) is coprime to \(3\). Riemann–Hurwitz gives \(2g-2=3(-2)+9(3-1)=12\), hence \(g=7\). At infinity, \(x\) and \(y\) have pole orders \(3\) and \(8\); \(dx\) has order \(-4\) there. The differential basis is
\[
U=(dx/y,\ x\,dx/y),\qquad
V=(dx/y^2,\ x\,dx/y^2,\ldots,x^4dx/y^2),
\]
comprising \(2+5=7\) regular and independent forms. Away from infinity they are regular because all finite ramification is tame and \(f\) is squarefree.

**Exact Cartier matrix.** In characteristic \(2\), \(\mathcal C(h^2\omega)=h\mathcal C(\omega)\), \(\mathcal C(x^i dx)=0\) for even \(i\), and \(\mathcal C(x^{2j+1}dx)=x^jdx\). Since \(dx/y=f(x)dx/y^4\) and \(dx/y^2\) has a squared denominator, the matrix of the \(2^{-1}\)-linear map \(\mathcal C\), on ordered basis \((U,V)\), is
\[
M=\begin{pmatrix}0&B\\A&0\end{pmatrix},\quad
B=\begin{pmatrix}0&1&0&0&0\\0&0&0&1&0\end{pmatrix},\quad
A=\begin{pmatrix}
 a_1^{1/2}&a_0^{1/2}\\
 a_3^{1/2}&a_2^{1/2}\\
 a_5^{1/2}&a_4^{1/2}\\
 a_7^{1/2}&a_6^{1/2}\\
 0&1
\end{pmatrix}.
\]
Squarefreeness implies \(f'\ne0\), hence at least one of \(a_1,a_3,a_5,a_7\) is nonzero. Thus \(A\) has rank \(2\) (the second column has last entry \(1\)); \(B\) has rank \(2\). Hence \(r_1=4\) and \(a(C_f)=7-4=3\).

**Every iterate.** For a matrix \(R\), the notation \(R^{[1/2^j]}\) means entrywise successive unique square roots. Matrices of iterates are
\[
M_n=M\,M^{[1/2]}\cdots M^{[1/2^{n-1}]}.
\]
Put \(T=B A^{[1/2]}=H^{[1/4]}\). The injectivity of \(A\), surjectivity of \(B\), and direct block multiplication give
\[
r_2=2+\operatorname{rank}T,\quad
r_3=2\operatorname{rank}T,\quad
r_4=\operatorname{rank}T+\operatorname{rank}(TT^{[1/4]}),\quad
r_5=2\operatorname{rank}(TT^{[1/4]}).
\]
If \(T\) is invertible, the rank stabilizes at \(4\). If \(T=0\), the third iterate vanishes. For a nonzero rank-one semilinear \(2\times2\) matrix, either \(TT^{[1/4]}=0\), after which the fifth iterate vanishes, or that product is nonzero and every later twisted product has rank one. Indeed writing \(T=uv^\top\) yields \(TT^{[1/4]}=u(v^\top u^{[1/4]})v^{[1/4]\top}\); if its middle scalar is nonzero, the successive twisted middle scalars remain nonzero (each is a fractional Frobenius power of that scalar). Finally, \(TT^{[1/4]}=0\) if and only if \(H^{[4]}H=0\), by raising each matrix entry to the sixteenth power. This proves all rank sequences and stable ranks.

**Geometry of the zero-rank locus.** If \(Q=0\) and \(H\ne0\), then \(H\) cannot be invertible, hence \(H=uv^\top\) has rank one. The condition becomes \(v^{[4]\top}u=0\), whence \(u\) is proportional to \((v_1^4,v_0^4)^\top\). Projectivizing produces the displayed map \(\varphi\). It is a closed immersion: on \(t\ne0\), the coordinate \(s/t\) is recovered as \(a_3/a_2\); on \(s\ne0\), the coordinate \(t/s\) is recovered as \(a_6/a_7\), giving inverse regular parameters and nonvanishing differentials. The pullback of a hyperplane is \(\mathcal O_{\mathbb P^1}(5)\), so the image is a smooth, nondegenerate rational quintic. Its affine cone is irreducible of dimension two, smooth outside its vertex, and singular at the vertex (embedding dimension four). Taking its product with the four free coefficient coordinates, then intersecting with the squarefree open, gives an irreducible codimension-two locus with precisely the asserted singular locus.

For any prescribed \(H\), this intersection is nonempty: choose \(a_1=1\) and \(a_5=0\), so \(f'=1+a_3x^2+a_7x^6\ne0\), then choose \(a_0\) outside the finite set making \(f\) vanish at a root of \(f'\). In particular, the cone, its nonvertex portion, and the complementary rank-one and invertible strata all meet the squarefree open. The determinant hypersurface is irreducible because the generic \(2\times2\) determinant is irreducible. Thus all stated geometric strata are nonempty, and the full assertions follow.

## Verification
The self-contained program `verify.py` computes over fields of sizes \(2\), \(4\), and \(8\), implements polynomial squarefreeness, the displayed semilinear Cartier matrix, eight twisted powers, and exact Gaussian elimination. It exhausts all \(2^8=256\) monic octics over \(\mathbb F_2\) and all \(4^8=65536\) over \(\mathbb F_4\), and checks a deterministic sample of \(2400\) octics over \(\mathbb F_8\). Every squarefree input agrees with the algebraic classification.

The resulting squarefree counts are respectively \(128\), \(49152\), and \(2062\) in the two exhaustive sets and the sample. For the exhaustive \(\mathbb F_4\) census the counts by classes (rank \(4\), rank \(2\), rank-\(0\) nonvertex, rank-\(0\) vertex) are \((34560,11520,2880,192)\). These are checks in the stated fields, **not** a proof of any general finite-field count or additional claimed theorem.

Run `python3 verify.py`. It requires only the Python standard library. The provided `verify_output.txt` records the reproducible output and final success marker. The general proof above does not rely on exhaustive computation over an infinite field.

## Relationship to prior work
Elkin, *The Rank of the Cartier operator on cyclic covers of the projective line* (first submitted 2007-08-02), establishes a general explicit Cartier formalism and shows that for characteristic-two Kummer covers the first Cartier rank depends only on ramification data. This already accounts for the constant \(a\)-number \(3\). The explicit higher-power ranks, the four differential profiles, and the codimension-two Frobenius-quintic rank-zero locus are the assessed specialization and geometric refinement, not the general Cartier formalism.

England, *Higher Genus Abelian Functions Associated with Cyclic Trigonal Curves* (first submitted 2010-03-22), studies the same complex cyclic \((3,8)\)-curve and its differentials and Abelian functions, not characteristic-two Cartier-iterate strata. Bouw, *The p-Rank of Ramified Covers of Curves* (2001), develops generalized Hasse–Witt methods and generic-rank results for cyclic covers, but the inspected results do not give this exact coefficient stratification or the nonlinear rank-zero geometry. Özman–Pries–Weir, *The boundary of the p-rank 0 stratum of the moduli space of cyclic covers of the projective line* (2019 preprint), proves a trielliptic realization theorem for **odd** primes congruent to \(2\) modulo \(3\) and considers moduli-space boundaries; it does not supply the asserted characteristic-two coefficient locus. Earlier explicit degree-five and degree-seven characteristic-two cubic-cover calculations involve different genus and different smooth rank-zero loci; the present degree-eight locus instead has an irreducible quintic-cone singularity and an additional Cartier nilpotence profile.

## Limitations
This result does not determine the full Ekedahl–Oort types, Newton polygons, or the scheme structure of a compactified or unmarked moduli stratum. It does not claim novelty for the general Kummer Cartier formula, constant initial rank, or the existence of a Frobenius graph as an abstract algebraic curve. Historical priority remains provisional: an older specialist computation of the same genus-seven family may be unindexed. Computational checks are corroboration only, not independent mathematical certification.

## References
1. A. Elkin, *The Rank of the Cartier operator on cyclic covers of the projective line*, arXiv:0708.0431 (v1 2007-08-02), https://arxiv.org/html/0708.0431v2.
2. M. England, *Higher Genus Abelian Functions Associated with Cyclic Trigonal Curves*, SIGMA 6 (2010), 025, arXiv:1003.4144, https://arxiv.org/html/1003.4144v2.
3. I. I. Bouw, *The p-Rank of Ramified Covers of Curves*, Compositio Math. 126 (2001), 295–322, https://doi.org/10.1023/A:1017513122376.
4. E. Özman, R. Pries, and C. Weir, *The boundary of the p-rank 0 stratum of the moduli space of cyclic covers of the projective line*, arXiv:1907.05684, https://arxiv.org/abs/1907.05684.
