# Sharp Hilbert-space conditioning of the full and diagonal quadratic defects on odd finite abelian groups

## Finding

For any finite abelian group \(G\) of odd cardinality \(N\ge3\), the quadratic/parallelogram defect
\[
(Qf)(x,y)=f(x+y)+f(x-y)-2f(x)-2f(y)
\]
has the complete, group-independent singular-value list \(2\) (once) and \(\sqrt{10}\) (\(N-1\) times) on normalized complex \(L^2\) spaces. Thus its sharp inverse-on-range bound is
\[
\|f\|_{L^2(G)}\le\frac12\|Qf\|_{L^2(G^2)},
\]
with equality precisely for nonzero constant functions.

The restriction to diagonal observations \(D f(x)=(Qf)(x,x)\) is also invertible, but its stability is radically different. Let \(\ell_1,\ldots,\ell_c\) be the cycle lengths of the doubling permutation on \(G\setminus\{0\}\). Its **entire squared singular spectrum**, as a multiset, is
\[
\left\{\lambda_-,\lambda_+\right\}\cup
\left\{9\text{ (multiplicity }c-1)\right\}\cup
\bigcup_{j=1}^{c}\left\{17-8\cos\frac{2\pi k}{\ell_j}:1\le k<\ell_j\right\},
\]
where
\[
\lambda_\pm=\frac{N+12\pm\sqrt{N(N+24)}}2.
\]
The sharp inverse constant is \(\|D^{-1}\|=\lambda_-^{-1/2}\), with
\[
\lambda_-\sim\frac{36}{N},\qquad \|D^{-1}\|\sim\frac{\sqrt N}{6}.
\]
Its least-singular vector is unique up to a complex scalar and has one value at the group identity and a common other value on all nonidentity points. If \(f(0)\) is given separately and subtracted, the remaining diagonal measurements recover \(f\) on \(G\setminus\{0\}\) with a sharp universal lower singular-value bound \(3\); the bound is attained for every odd group with more than one doubling cycle.

## Assumptions and scope

\(G\) is finite, abelian, of odd cardinality \(N\ge3\). Functions take complex values. Both input \(L^2(G)\) and output \(L^2(G^2)\) carry normalized counting inner products, respectively \(N^{-1}\sum_x\) and \(N^{-2}\sum_{x,y}\). The restriction \(D:L^2(G)\to L^2(G)\) uses the same normalized counting measure on domain and range. All singular values include algebraic multiplicity. A double orbit means iteration of \(x\mapsto2x\), which is bijective on \(G\).

## Proof

**Full observations.** The characters of \(G\) are an orthonormal basis for normalized \(L^2(G)\). For the trivial character \(\mathbf1\), \(Q\mathbf1=-2\mathbf1\), of squared norm \(4\). For every nontrivial character \(\chi\),
\[
(Q\chi)(x,y)=\chi(x)(\chi(y)+\overline{\chi(y)}-2)-2\chi(y).
\]
Since \(G\) has odd order, \(\chi^2\ne\mathbf1\). Consequently \(\chi(y)\), \(\overline{\chi(y)}\) and \(\mathbf1\) are mutually orthogonal in the necessary moment calculations. Orthogonality in the \(x\) variable kills the cross term, yielding
\[
\|Q\chi\|^2=\|\chi+\overline\chi-2\|^2+4=6+4=10.
\]
For different nontrivial characters \(\chi\ne\psi\), the first parts are orthogonal by averaging \(x\), the second parts by averaging \(y\), and the mixed first/second parts have zero mean in \(x\). The constant image is similarly orthogonal to all nonconstant images. Hence \(Q^*Q\) has eigenvalues \(4\) and \(10\) in this basis, exactly as claimed. The smallest singular direction consists of constants.

**Diagonal observations.** Put \(S=G\setminus\{0\}\) and \(m=N-1\). From direct substitution,
\[
(Df)(0)=-2f(0),\qquad (Df)(x)=f(2x)-4f(x)+f(0)\quad(x\in S).
\]
In the orthonormal basis given by the unit coordinate vector at \(0\), the normalized constant vector \(h=m^{-1/2}\mathbf1_S\), and the subspace \(W=\{g\in\mathbb C^S:\sum_{x\in S}g(x)=0\}\), the operator is the orthogonal direct sum
\[
D\cong\begin{pmatrix}-2&0\\\sqrt m&-3\end{pmatrix}\oplus(P-4I)|_W,
\]
where \(P g(x)=g(2x)\) is a permutation unitary. Although the ambient function spaces use normalized counting measures, common input/output normalization cancels from singular values; the displayed vectors are orthonormal in ordinary coordinates and their normalized versions give the same matrix.

For the first block, \(B^*B\) has trace \(N+12\) and determinant \(36\), giving eigenvalues \(\lambda_\pm\). The permutation \(P\) has cycles of lengths \(\ell_j\). On each cycle its eigenvalues are the roots \(e^{2\pi i k/\ell_j}\). The vectors constant on each individual cycle span a \(c\)-dimensional \(P=I\) eigenspace, of which one direction is \(h\); the remaining \(c-1\) directions contribute squared singular value \(9\) on \(W\). Every nonconstant cycle Fourier mode contributes
\[
|e^{2\pi i k/\ell_j}-4|^2=17-8\cos(2\pi k/\ell_j).
\]
The multiplicities sum to \(2+(c-1)+\sum_j(\ell_j-1)=N\), so the list is exhaustive.

Since \(\lambda_-\lambda_+=36\) and \(\lambda_+\ge12\) for \(N\ge3\), we have \(0<\lambda_-\le3<9\). All other squared singular values are at least \(9\), giving the unique least-singular block direction and the optimal inverse bound. It is characterized by \(f|_S\) constant and the relation
\[
\frac{f(x)}{f(0)}=\frac{N+3-\lambda_-}{3(N-1)}\quad(x\ne0),
\]
with \(f(0)\ne0\). Expanding the quadratic radical gives \(\lambda_-\sim36/N\), establishing the sharp asymptotic. Finally, with \(f(0)\) independently known, restriction to unknown coordinates \(S\) is simply \(P-4I\); its minimum singular value is at least \(3\), because every eigenvalue of \(P\) has modulus \(1\). It equals \(3\) when \(c\ge2\), since then a cycle-constant zero-sum vector exists.

## Verification

The attached stand-alone Python diagnostic constructs both matrices directly for odd cyclic groups of orders \(3,5,7,9,11,13,15,17,19,21\) and the products \(C_3^2\), \(C_3\times C_5\), and \(C_3^3\). It compares eigenvalues of the actual Gram matrices with the complete predicted multisets. Numerical checks corroborate but do not replace the Fourier and invariant-subspace proof above. Run `python check_spectra.py` with Python 3 and NumPy. Expected terminal marker: `DIAGNOSTIC_OK 2976`.

## Relationship to prior work

Stability of the quadratic functional equation is a classical topic; the 2025 work by Tamilvanan and collaborators examines fixed-point and direct stability techniques in quasi-Banach settings. Jamneshan and Thom classify abstract quadratic maps, including the finite-abelian case, via group constructions. Li's 2026 affine-orbit matrix-recovery paper demonstrates the importance of exact least singular values in finite-group measurement systems. The later Popa–Rus work (first publicly posted 19 November 2026, hence not the motivating source for the dated research cohort) directly treats the same parallelogram defect on general abelian groups and already gives qualitative injectivity on finite groups and reconstruction from doubling orbits (Example 8.9). Those facts are explicitly prior coverage, not novel claims here. None of these inspected sources computes the **complete normalized Hilbert singular spectra** of both full and diagonal data or the exact stability gap. The present comparison is by operator formula, input/output normalization, and conclusions, not only by titles. No claim is made that diagonal or full finite-group defects were previously unstudied.

## Limitations

This is a finite, odd-order, complex Hilbert-space result; it does not establish an analogous formula for groups with even order, for other target Banach norms, for nonlinear measurement maps, or for partial noisy identity measurements. Numerical checks cover only listed small groups; universal validity follows from the proof. Bibliographic noncoverage is evidence-based rather than a guarantee against unindexed equivalent work.

## References

1. K. Tamilvanan, F. Özger, S. A. Mohiuddine, N. Ahmad, M. J. Kabeto, *Fixed Point Technique: Stability Analysis of Quadratic Functional Equation in Various Quasi-Banach Spaces*, Journal of Mathematics (first published 13 June 2025), DOI: 10.1155/jom/6689441. https://onlinelibrary.wiley.com/doi/full/10.1155/jom/6689441
2. A. Jamneshan and A. Thom, *Quadratic maps between non-abelian groups*, arXiv:2412.14908 (first public 19 December 2024), https://arxiv.org/abs/2412.14908
3. D. Li, *Sharp Conditioning for Matrix Recovery by Finite Affine Orbits*, arXiv:2609.09619 (first public 9 September 2026), https://arxiv.org/abs/2609.09619
4. D. Popa and M. D. Rus, *A constructive inverse for the Jordan–von Neumann operator on abelian groups*, arXiv:2611.26471 (first posted 19 November 2026, subsequent to the eligible dated source), https://arxiv.org/abs/2611.26471
