# Universal prime-field self-Fourier injectivity on determinant-one matrices

## Finding
For every prime \(p\), put \(G=\mathrm{SL}_2(\mathbb F_p)\), let \(\psi:\mathbb F_p\to\mathbb C^\times\) be any nontrivial additive character, and index the square matrix \(H\) by \(G\) in both coordinates:
\[
H(X,Y)=\psi\left(\sum_{i,j=1}^2 X_{ij}Y_{ij}\right).
\]
**Theorem.** The complex matrix \(H\) is invertible for every prime \(p\). Equivalently, a complex function supported on the determinant-one matrices over \(\mathbb F_p\) is determined uniquely by its ambient additive Fourier transform evaluated on the same determinant-one matrices. There are \(p(p^2-1)\) samples and unknowns. The theorem does not assert this for nonprime finite fields.

## Assumptions and scope
The Fourier transform is the *ambient four-coordinate additive* transform, not the matrix-coefficient Fourier transform of the nonabelian group. A nontrivial additive character is necessarily \(\psi(t)=\exp(2\pi i c t/p)\) for some \(c\in\mathbb F_p^\times\). We use no normalization factor; multiplying the matrix by any nonzero scalar does not affect invertibility. All groups and representations below are finite-dimensional over \(\mathbb C\). The result concerns linear complex reconstruction, not phase retrieval or numerical condition numbers.

## Proof
**1. Conversion to central convolution.** The bijection \(G\to G\), \(X\mapsto g=X^{-T}\), changes the matrix entry to
\[
H(X,Y)=\psi(\operatorname{tr}(g^{-1}Y))=f(g^{-1}Y),\qquad f(h)=\psi(\operatorname{tr}h).
\]
Since trace is constant on conjugacy classes, \(f\) is central on \(G\). Thus row permutation transforms \(H\) into the convolution operator by \(f\). On an irreducible \(G\)-representation \(V_\rho\) of degree \(d_\rho\), its convolution Fourier multiplier is a scalar proportional to
\[
\Lambda_\rho=\sum_{h\in G}\psi(\operatorname{tr}h)\chi_\rho(h).
\]
The possible replacement of \(\chi_\rho\) by its dual under the choice of convolution convention does not affect the test that every scalar be nonzero. The regular representation contains every irreducible, so it suffices to prove \(\Lambda_\rho\ne0\) for all \(\rho\).

**2. The cyclotomic coefficient field, for odd \(p\).** Write
\[
A_\rho(t)=\sum_{\substack{h\in G\\\operatorname{tr}h=t}}\chi_\rho(h),\qquad K=\mathbb Q(\zeta_{p^2-1}).
\]
For \(t\ne2,-2\), the characteristic polynomial of \(h\) has distinct roots, so \(h\) is split or nonsplit semisimple and has order dividing \(p-1\) or \(p+1\). Every complex representation character value on such an element belongs to \(K\). The exceptional trace values are handled in step 3. Hence \(A_\rho(t)\in K\) for every \(t\). Since \(\gcd(p,p^2-1)=1\), the cyclotomic polynomial \(\Phi_p(z)=1+z+\cdots+z^{p-1}\) remains irreducible over \(K\). Therefore, for any nonzero \(c\in\mathbb F_p\),
\[
\sum_{t\in\mathbb F_p}A_\rho(t)\zeta_p^{ct}=0
\quad\Longleftrightarrow\quad
A_\rho(0)=A_\rho(1)=\cdots=A_\rho(p-1).
\]
Indeed a polynomial of degree at most \(p-1\) over \(K\) can vanish at \(\zeta_p^c\) only if it is a scalar multiple of \(\Phi_p\).

**3. Nonzero exceptional trace coefficient.** For each line \(L\subset\mathbb F_p^2\), let \(U_L\) be the order-\(p\) subgroup of unipotent matrices fixing \(L\) pointwise. Every nonidentity element of trace \(2\) lies in exactly one such subgroup. Thus, as a group-algebra identity,
\[
\sum_{\operatorname{tr}h=2}h
=\sum_{L\in\mathbb P^1(\mathbb F_p)}\sum_{u\in U_L}u-p\,e.
\]
Let \(r_\rho=\dim V_\rho^{U_L}\), independent of \(L\), and \(d_\rho=\dim V_\rho\). Taking representation traces, and using that \(p^{-1}\sum_{u\in U_L}\rho(u)\) projects onto \(V_\rho^{U_L}\), yields the exact integer identity
\[
A_\rho(2)=p\big((p+1)r_\rho-d_\rho\big).
\]
The classical irreducible representation classification of \(\mathrm{SL}_2(\mathbb F_p)\) gives \(d_\rho\le p+1\), and every irreducible of degree \(p+1\) is a generic principal series \(\operatorname{Ind}_B^G\eta\) from a character of the upper triangular Borel subgroup. Such an induced representation has precisely **two** independent \(U_L\)-fixed vectors: the restriction of its induced-function model to \(U_L\) has two orbits on \(G/B\cong\mathbb P^1(\mathbb F_p)\), a fixed point and the remaining \(p\)-point orbit, and the Borel character is trivial on the unipotent stabilizer of the fixed point. Thus \(r_\rho=2\) when \(d_\rho=p+1\). If \(d_\rho<p+1\), the integer \((p+1)r_\rho-d_\rho\) cannot be zero because \(r_\rho\ge0\) is integral and \(d_\rho>0\); if \(d_\rho=p+1\), the integer equals \(p+1\). In all cases \(A_\rho(2)\ne0\). The trace \(-2\) coefficient is also integral: multiplication by the central element \(-I\) bijects its trace fiber with trace \(2\) and acts in an irreducible representation by a sign.

**4. Nontrivial and trivial representations.** If \(\rho\) is not the trivial representation, character orthogonality gives \(\sum_t A_\rho(t)=0\). Were the \(p\) coefficients all equal, their common value would be zero, contrary to step 3. Hence \(\Lambda_\rho\ne0\) by step 2. For the trivial representation, the trace-fiber count is
\[
A_{\mathbf1}(t)=p\left(p+\left(\frac{t^2-4}{p}\right)\right),
\]
where the Legendre symbol is zero when its argument is zero. This follows by writing a trace-\(t\) matrix as \(\begin{psmallmatrix}a&b\\c&t-a\end{psmallmatrix}\), counting solutions of \(bc=a(t-a)-1\), and solving \(a^2-ta+1=0\). In particular \(A_{\mathbf1}(2)=p^2\) whereas \(A_{\mathbf1}(0)=p(p+\left(\frac{-4}{p}\right))\ne p^2\). They are not all equal, so \(\Lambda_{\mathbf1}\ne0\).

**5. Characteristic two.** At \(p=2\), \(G\cong S_3\) and \(\psi(t)=(-1)^t\). The central function \(f(g)=(-1)^{\operatorname{tr}g}\) equals \(+1\) at the identity and three involutions, and \(-1\) at both elements of order three. Its convolution multipliers on the trivial, sign, and standard representations are respectively \(2,-4,2\), the last scalar acting on the two-dimensional standard representation. All are nonzero. Together with steps 1–4, this proves the theorem for every prime.

## Verification
The standalone source `check_sl2.py` constructs the entire square sampling matrix for \(p\in\{2,3,5,7\}\) and verifies full rank **exactly** over an auxiliary finite field \(\mathbb F_\ell\) for which \(p\mid\ell-1\). In each case a primitive \(p\)-th root of unity in \(\mathbb F_\ell\) replaces the complex root of unity, and row elimination uses modular inverses. This exact reduction is a valid consistency test for those four finite parameters, not a proof of invertibility for arbitrary primes. The checker prints `exact_modular ... full True` in all four cases, with dimensions \(6,24,120,336\). The all-prime conclusion rests on the proof above, particularly the cyclotomic and representation-theoretic steps.

## Relationship to prior work
Prasad's notes give the irreducible representation classification and induced-series dimensions used in step 3; those representation-theoretic facts are classical, not claimed as new. Li and Hu evaluate the ambient additive Fourier transform of the determinant-one indicator as a function of a single frequency matrix. In particular, their formula can determine the row sum of the square restricted matrix, but not the nonvanishing of every nonabelian irreducible central-convolution multiplier needed for invertibility. Lafferty and Rockmore develop computational Fourier analysis and representations of the finite special linear group; their numerical group transforms are not the same as the ambient additive character kernel here. Relevant previously published finite-field sampling results on determinant-one matrices treat the constant and one-coordinate Fourier characters, a rectangular \(4p-3\)-column family rather than the square \(p(p^2-1)\)-column matrix. No claim of exhaustive historical priority is made.

## Limitations
The prime-field hypothesis is essential to the **method**: irreducibility of \(\Phi_p\) over a field containing semisimple character values is used critically and no extension-field conclusion is asserted. No explicit determinant, condition number, or inverse formula is obtained. The argument uses the classical complete complex representation-degree classification of \(\mathrm{SL}_2(\mathbb F_p)\) as an input. Earlier broad character-table or association-scheme results could conceivably imply this nonvanishing theorem; the literature comparison is bounded and not an independence certification. The finite modular tests are separate from and weaker than the proof; no independent mathematical audit has been performed.

## References
1. Amritanshu Prasad, *Representations of GL2(Fq) and SL2(Fq), and some remarks about GLn(Fq)*, arXiv:0712.4051v1, first publicly submitted 2007-12-25, especially Chapters 2.4–2.5 and 3.6. https://arxiv.org/abs/0712.4051
2. Yan Li and Su Hu, *Gauss sums over some matrix groups*, arXiv:1105.4513v1, first publicly submitted 2011-05-23, especially Theorem 2.4. https://arxiv.org/abs/1105.4513
3. John D. Lafferty and Daniel N. Rockmore, *Fast Fourier Analysis for SL₂ over a Finite Field and Related Numerical Experiments*, Experimental Mathematics **1** (1992), 115–139. https://www.cs.cmu.edu/afs/cs/usr/lafferty/www/pub/sl2.pdf
