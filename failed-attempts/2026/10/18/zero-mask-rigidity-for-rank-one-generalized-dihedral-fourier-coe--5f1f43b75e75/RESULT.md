# Zero-mask rigidity for rank-one generalized-dihedral Fourier coefficients

## Finding
Let \(A\) be a finite abelian group of order \(N\), let \(G=A\rtimes\langle s\rangle\) with \(s^2=1\) and \(sas=a^{-1}\), and fix \(\chi\in\widehat A\) with \(\chi\ne\chi^{-1}\). Define \(\eta=\chi^2\), \(H=\ker\eta\), and \(L=|\eta(A)|\ge2\). Let \(\rho_\chi\) be the corresponding irreducible two-dimensional induced representation. For every nonzero rank-one matrix coefficient \(f(g)=u^{\mathsf T}\rho_\chi(g)v\), write \(Z(f)=\{g\in G:f(g)=0\}\).

**Complete zero-mask classification.** The attainable sets \(Z(f)\), for this *fixed irreducible representation*, are exactly

1. \(\varnothing\);
2. either complete half \(A\) or \(sA\);
3. any single coset of \(H\) inside either \(A\) or \(sA\);
4. the union of any one \(H\)-coset in \(A\) and any one \(H\)-coset in \(sA\).

There are precisely \(L^2+2L+3\) distinct zero masks; no two listed types overlap because \(L\ge2\). Their exact attainable spatial-support cardinalities are
\[
\boxed{\{N,\ 2N-2N/L,\ 2N-N/L,\ 2N\}},
\]
with the first two values coinciding if and only if \(L=2\). Every coefficient has exactly one nonzero rank-one Fourier block and rank-weighted Fourier support \(2\).

**Zero-only projective identifiability.** A mask meeting both halves in proper nonempty sets determines precisely **two** complex projective rank-one coefficient functions, and these differ by changing the sign of the reflection-half values while keeping the rotation-half values fixed. Either full-half mask determines exactly two such projective coefficient functions. A single-fiber mask or the empty mask has infinitely many projective coefficient realizations. Thus the entire inverse fiber of the zero-observation map is classified, not merely its possible support sizes.

## Assumptions and scope
The characters are complex and unitary; \(A\) is written multiplicatively. We index the reflection half as \(as\) for \(a\in A\). A projective coefficient is a nonzero function considered up to multiplication by a nonzero complex scalar (not modulo translation or group-character multiplication). The vectors \(u,v\in\mathbb C^2\) are nonzero. No statement is made about sums of Fourier blocks, arbitrary rank-two coefficients, or coefficients of higher-dimensional irreducibles. If \(A\) is of exponent two there is no admissible \(\chi\), and this two-dimensional assertion has empty scope.

We use
\[
\rho_\chi(a)=\begin{pmatrix}\chi(a)&0\\0&\chi(a)^{-1}\end{pmatrix},\qquad
\rho_\chi(s)=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
As \(\chi\ne\chi^{-1}\), its two eigenspaces are exchanged by \(s\), so \(\rho_\chi\) is irreducible. Both halves contain \(N\) points, and every \(H\)-coset has \(N/L\) points.

## Proof
**Step 1: rank-one coefficient variety.** Set
\[
U=u_1v_1,\quad V=u_2v_2,\quad W=u_1v_2,\quad X=u_2v_1.
\]
Then \(UV=WX\) and
\[
f(a)=U\chi(a)+V\chi(a)^{-1},\quad
f(as)=W\chi(a)+X\chi(a)^{-1}.\tag{1}
\]
Conversely, every *nonzero* quadruple \((U,V,W,X)\) with \(UV=WX\) is an outer product and therefore gives a rank-one coefficient. This is the determinant-zero cone of \(2\times2\) matrices, with entries arranged as \(\left(\begin{smallmatrix}U&W\\X&V\end{smallmatrix}\right)\). Distinct coefficient quadruples give distinct functions, because \(\chi\) and \(\chi^{-1}\) are linearly independent on \(A\).

**Step 2: necessary zeros.** If \(U,V\ne0\), equation (1) vanishes precisely on the fiber
\[
\eta(a)=-V/U.\tag{2}
\]
It is either empty or one coset of \(H\), of cardinality \(N/L\). If exactly one of \(U,V\) is nonzero, there are no zeros on \(A\); if both vanish, the whole of \(A\) vanishes. The identical statement with \(W,X\) holds on \(sA\).

If one half vanishes completely, say \(U=V=0\), then \(uv^{\mathsf T}\ne0\) and \(WX=0\). Therefore exactly one of \(W,X\) is nonzero, and the other half has no zeros. If neither half vanishes identically and one half has a proper nonempty zero fiber, its two coefficients are nonzero; the rank-one identity \(UV=WX\) then forces both coefficients on the *other* half to be nonzero as well. Hence no unlisted mixture, such as a whole half together with a proper fiber, is possible. This proves exhaustiveness.

**Step 3: realization.** Let \(\alpha,\beta\in\eta(A)\). To realize prescribed fibers \(\eta(a)=\alpha\) on \(A\) and \(\eta(a)=\beta\) on \(sA\), choose a nonzero \(z\in\mathbb C\) with \(z^2=\alpha/\beta\) and set
\[
(U,V,W,X)=(1,-\alpha,z,-\beta z).\tag{3}
\]
The determinant identity holds because \(WX=-\beta z^2=-\alpha=UV\). Both fibers therefore occur, with no additional zeros. To realize only the rotation-half fiber use
\[
(U,V,W,X)=(1,-\alpha,2,-\alpha/2).
\]
Its reflection-half terms have unequal moduli and cannot cancel. To realize only the reflection-half fiber use
\[
(U,V,W,X)=(2,-\beta/2,1,-\beta),
\]
whose rotation-half terms similarly cannot cancel. The empty mask is attained by \((1,0,1,0)\). Masks \(A\) and \(sA\) are attained by \((0,0,1,0)\) and \((1,0,0,0)\), respectively. All these quadruples are nonzero and satisfy \(UV=WX\).

**Step 4: exact inverse fibers.** For a mask with nonempty fibers on both halves, equation (2) and its reflection counterpart force \(V=-\alpha U\) and \(X=-\beta W\). Since all four coefficients are nonzero, projectively normalize \(U=1\). Rank one then forces
\[
W^2=\alpha/\beta,
\]
which has exactly two distinct complex roots, giving precisely the two classes (3). Their values on \(A\) coincide and on \(sA\) differ by sign, so they are not scalar multiples. For the whole-\(A\) zero mask, the only projective quadruples are \((0,0,1,0)\) and \((0,0,0,1)\), and likewise for \(sA\). For one specified rotation fiber \(\alpha\), normalize \(U=1\), set \(V=-\alpha\), and choose any \(W\in\mathbb C^\times\) with \(-X/W=\alpha/W^2\notin\eta(A)\), setting \(X=-\alpha/W\). This gives infinitely many distinct projective functions with the same rotation-half-only mask. Reflection-fiber cases follow symmetrically. The empty mask has infinitely many realizations \((1,0,t,0)\) as \(t\in\mathbb C^\times\) varies. These exhaust all projective classes in each fiber.

**Step 5: counting, supports, Fourier rank.** Each half contains exactly \(L\) fibers, and the possible masks contribute respectively \(1\), \(2\), \(2L\), and \(L^2\), proving the count. Their sizes are \(0,N,N/L,2N/L\), yielding the four listed support sizes. With normalized finite-group Fourier transform
\[
\widehat f(\pi)=\frac1{|G|}\sum_{g\in G}f(g)\pi(g)^*,
\]
Schur orthogonality annihilates every irreducible except \(\rho_\chi\). At that block it gives a nonzero scalar multiple of the rank-one outer-product matrix (up to transpose/conjugation and the chosen convention). Its rank is one and its degree is two, so \(\sum_{\pi\in\widehat G}(\dim\pi)\operatorname{rank}\widehat f(\pi)=2\). No appeal to enumeration is needed.

## Verification
The accompanying standalone `verify.py` enumerates the squared-character fibers on twelve finite abelian test groups (including noncyclic kernels), checks the \(L^2+2L+3\) mask count and all attainable support cardinalities, and checks the determinant identity and both double-fiber witnesses using exact modular character exponents. On the ordinary dihedral group of order eight it also exhaustively checks 2,304 nonzero coefficient pairs over a small Gaussian-integer alphabet, with exact Gaussian-integer arithmetic. Its output includes `CHECK_OK characters 80 pair_witnesses 3192 gaussian_rank_one_vectors 2304`. This finite test corroborates the symbolic argument; it is not an exhaustive proof for all groups or arbitrary complex coefficients.

## Relationship to prior work
Alagic and Russell (2006) establish the general compact-group rank-weighted uncertainty inequality and formalize the Fourier support measure used here. Their theorem constrains the size of a support but does not determine any exact zero masks or the projective coefficient multiplicities. The standard representation formulas for dihedral groups appear in the Durham representation notes cited below; those formulas alone are not a zero-mask classification. Results on maximal-spanning vectors for two-dimensional dihedral irreducibles and on endpoint norms of generalized-dihedral Fourier isotype projections address orbit-projector spanning and convolution norms, respectively. Neither statement implies the support-mask or two-to-one zero-observation theorem. Likewise, a three-tap generalized-dihedral convolution-nullity census concerns zero sets of determinants of convolution Fourier blocks rather than zero sets of single rank-one matrix coefficients. Führ and Oussa (2023) define the maximum proportion of coefficient zeros with a fixed analysis vector, an extremal cardinality statistic rather than a classification of exact support masks and their projective inverse fibers. These are mathematical comparisons of conclusions, not claims that the underlying representation theory is new.

## Limitations
The theorem is a complete classification within one fixed two-dimensional irreducible Fourier block, not for arbitrary functions on \(G\). The proof uses standard induced-representation matrices, elementary binomial zero fibers, and a rank-one determinant constraint; these components are known. A source under broader representation-theoretic or finite-group zero-set terminology might imply the classification implicitly; no claim of exhaustive literature certification is made. Rank-weighted Fourier support alone does not distinguish the listed masks. The exact computational replay covers only the stated finite examples; the all-group conclusion rests on the algebraic proof.

## References
1. G. Alagic and A. Russell, *Uncertainty Principles for Compact Groups*, arXiv:math/0608702, first posted 2006-08-28. https://arxiv.org/pdf/math/0608702
2. Representation Theory notes, Durham University, Lecture 3, dihedral-group matrices and irreducibility proof. https://www.maths.dur.ac.uk/users/jamie.j.mason/RepresentationTheoryNotes-michaelmas/Ch1.S3.html
3. *Exact maximal-spanning vectors for two-dimensional dihedral irreducibles*, result and proof, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-maximal-spanning-vectors-for-two-dimensional-dihedral-irre--254536e7d971/RESULT.md
4. *Exact endpoint norms of nonlinear isotype projections on generalized dihedral groups*, result and proof, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-exact-endpoint-norms-of-nonlinear-isotype-projections-on-general--bae7b21bfb6b/RESULT.md
5. *Complete three-tap Fourier-rank census on elementary generalized dihedral groups*, result and proof, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-complete-three-tap-fourier-rank-census-on-elementary-generalized--7d6c365ba4ff/RESULT.md
6. H. Führ and V. Oussa, *Phase Retrieval for Nilpotent Groups*, *J. Fourier Anal. Appl.* 29 (2023), article 47, https://link.springer.com/article/10.1007/s00041-023-10031-5
