# Three strict one-sweep energy tiers for all Gauss–Seidel orders on a screened four-cycle

## Finding

On the uniform four-node periodic screened-Poisson quadratic, the exact worst-case **one complete sweep** squared-energy error factor depends on the order in three strictly separated tiers. For every \(0<t<1/2\), all 24 permutations split into eight interlaced, eight cyclic, and eight red–black orders, and
\[
\boxed{F_{\mathrm{interlaced}}(t)<F_{\mathrm{cyclic}}(t)<F_{\mathrm{redblack}}(t).}
\]
The sharp optimum and worst factor are
\[
\boxed{F_{\mathrm{interlaced}}(t)=2t^2\left(1+t^2+t\sqrt{2+t^2}\right),\qquad F_{\mathrm{redblack}}(t)=4t^2.}
\]
The intermediate factor is the largest real root of
\[
\lambda^3-(t^6+4t^4+4t^2)\lambda^2+(2t^6+4t^4)\lambda-t^6=0.
\]
Despite the sharp finite-sweep gap, the red–black and interlaced orders have **the same** asymptotic spectral radius \(4t^2\); every cyclic order has strictly larger spectral radius. The sharp red–black penalty obeys
\[
\frac{F_{\mathrm{redblack}}}{F_{\mathrm{interlaced}}}=
\frac{2}{1+t^2+t\sqrt{2+t^2}}\longrightarrow2\quad(t\downarrow0).
\]

## Assumptions and scope

Number the vertices of \(C_4\) as \(0,1,2,3\) in cyclic order and set \(A=I_4-t\operatorname{Adj}(C_4)\) for real \(0<t<1/2\). Its eigenvalues are \(1-2t,1,1,1+2t\), hence it is strictly positive definite. A sweep is an exact scalar coordinate minimization **once at each coordinate** in a prescribed permutation \(\pi=(\pi_1,\ldots,\pi_4)\). For an error vector \(e\), each update multiplies by \(U_i=I_4-e_ie_i^{\mathsf T}A\); the completed error matrix is \(G_\pi=U_{\pi_4}U_{\pi_3}U_{\pi_2}U_{\pi_1}\).

The observable is the worst-case relative squared energy after one sweep,
\[
F_\pi=\sup_{e\ne0}\frac{e^{\mathsf T}G_\pi^{\mathsf T}AG_\pi e}{e^{\mathsf T}Ae}.
\]
Equivalently, it is the largest generalized eigenvalue of \((G_\pi^{\mathsf T}AG_\pi,A)\). This is not the spectral radius \(\rho(G_\pi)\) and is not an assertion about all individual initial errors. The three representative orderings are interlaced \((0,1,3,2)\), cyclic \((0,1,2,3)\), and red–black \((0,2,1,3)\).

## Proof

**Symmetry reduction.** The dihedral automorphism group of the square acts freely on four-element permutations. Its orbits through the three displayed representatives each have eight distinct elements; an explicit orbit calculation shows they are disjoint, hence exhaust all 24 permutations. Since the automorphisms preserve \(A\), both generalized energy spectra and ordinary sweep spectra are constant on each orbit. Therefore checking one representative from each orbit is exhaustive.

**Exact energy polynomials.** Write \(u=t^2\), \(\lambda\) for a generalized squared-energy eigenvalue, and \(B_\pi=G_\pi^{\mathsf T}AG_\pi\). Direct multiplication yields the following factorizations of \(\det(B_\pi-\lambda A)/(1-4u)\):
\[
\begin{array}{ll}
\mathrm{redblack}:&\lambda^3(\lambda-4u),\\
\mathrm{interlaced}:&\lambda^2[\lambda^2-4u(1+u)\lambda+4u^2],\\
\mathrm{cyclic}:&\lambda[\lambda^3-(u^3+4u^2+4u)\lambda^2+(2u^3+4u^2)\lambda-u^3].
\end{array}
\]
All generalized roots are nonnegative since \(B_\pi\) is positive semidefinite and \(A\) positive definite. The first two factorizations yield the stated red–black and interlaced factors. In particular the larger interlaced root is
\[
L=2u\left(1+u+\sqrt{u(u+2)}\right).
\]

**Cyclic strictly better than red–black.** For the cyclic representative, compute \(K=4uA-G_{\mathrm{cyclic}}^{\mathsf T}AG_{\mathrm{cyclic}}\). Its four leading principal minors are
\[
\begin{aligned}
&4u,\\
&4u^2(u^3+3u^2-2u+3),\\
&4u^3(8u^3+26u^2-19u+9),\\
&4u^4(1-4u)^2(4u+15).
\end{aligned}
\]
All are strictly positive for \(0<u<1/4\): the second parentheses exceeds \(3-2/4\), the third exceeds \(9-19/4\), and the remaining factors are positive. Sylvester's criterion makes \(K\) positive definite. Hence \(F_{\mathrm{cyclic}}<4u=F_{\mathrm{redblack}}\).

**Interlaced strictly better than cyclic.** Define the signed cyclic cubic
\[
q(\lambda)=-\lambda^3+(u^3+4u^2+4u)\lambda^2-(2u^3+4u^2)\lambda+u^3.
\]
Division by the interlaced quadratic gives \(q(L)=u^3[P(u)+Q(u)\sqrt{u(u+2)}]\), where
\[
P(u)=1-4u+16u^3+8u^4,\qquad Q(u)=4u(2u^2+2u-1).
\]
For \(0<u<1/4\), \(P(u)>0\), \(Q(u)<0\), and the exact identity
\[
P(u)^2-u(u+2)Q(u)^2=(1-4u)^2>0
\]
implies \(q(L)>0\). Since \(q(\lambda)\to-\infty\) as \(\lambda\to+\infty\), a cyclic generalized eigenvalue exceeds \(L\). Thus \(F_{\mathrm{interlaced}}<F_{\mathrm{cyclic}}\), completing the unique-orbit optimum classification.

**Spectral-radius comparison.** Both red–black and interlaced sweep matrices have ordinary characteristic polynomial \(\lambda^3(\lambda-4u)\). The cyclic matrix has polynomial \(-\lambda q_s(\lambda)\) where
\[
q_s(\lambda)=-\lambda^3+(u^2+4u)\lambda^2-2u^2\lambda+u^2.
\]
At \(\lambda=4u\), \(q_s(4u)=u^2(1-4u)^2>0\), while \(q_s(\lambda)\to-\infty\) as \(\lambda\to+\infty\). Therefore the cyclic matrix has a positive eigenvalue strictly above \(4u\), proving the asserted asymptotic separation. The ratio formula and limit follow directly from the two explicit energy factors.

## Verification

The self-contained symbolic checker `verification/verify_fourcycle_energy.py` constructs all 24 sweep matrices, confirms the dihedral orbit partition, verifies all three complete generalized characteristic polynomials, all required spectral identities, all four Sylvester minors and the polynomial square identity, and performs supplementary rational-parameter numerical cross-checks. Invoke `python verification/verify_fourcycle_energy.py` after installing versions of SymPy and NumPy compatible with `requirements.txt`; the recorded output is `verification/check_output.txt`. The algebraic identities and sign arguments above establish every parameter and every permutation, independently of those finite samples.

## Relationship to prior work

Varga (1959) proves global *spectral-radius* optimality of consistent orderings for symmetric nonnegative Jacobi matrices, a result applicable to this family. Its conclusion does not compare the finite-sweep \(A\)-energy operator norms among spectrally tied orderings and therefore does not imply the strict three-tier classification here. Harrar (1993) studies structural consistent-order tests and multicoloring; the available abstract identifies no sharp one-sweep energy comparison, but complete-text exclusion was not possible. Dessalew and collaborators (2021), in accessible full text, analyze refined Gauss–Seidel on consistently ordered two-cyclic matrices, primarily using asymptotic convergence relations, not exhaustive single-sweep energy norms. Xiao, Xiao and Sun (arXiv:1910.04366, 2019), in accessible full text, analyze global worst-case complexity of symmetrized orders, not all 24 single-sweep permutations on the screened four-cycle.

A published study of exact worst-case energy norms for arrowhead matrices and a published study of randomized contiguous-block updates on cyclic screened-Poisson matrices concern different sparsity patterns or different sampling/optimization objectives; their full relevant claims were compared. The present claim is the explicit *fixed-permutation, all-order, one-sweep* classification for a four-cycle. No general priority or other-graph result is asserted.

## Limitations

The statement is restricted to four vertices, a uniform symmetric nearest-neighbor coupling, exact arithmetic, unrelaxed single-coordinate sweeps and worst-case one-sweep squared \(A\)-energy. Optimizing this factor need not minimize runtime: red–black orders permit two parallel color stages, whereas interlaced orders use more serial dependency stages. Nothing is claimed for arbitrary weighted cycles, larger grids, randomized schedules, or later-sweep optimality. Some related historical full texts were not accessible, so independent mathematical and historical-priority review remains necessary.

## References

1. R. S. Varga, *Orderings of the Successive Overrelaxation Scheme*, Pacific Journal of Mathematics 9 (1959), 925–939, https://msp.org/pjm/1959/9-3/pjm-v9-n3-p28-p.pdf .
2. D. L. Harrar II, *Orderings, Multicoloring, and Consistently Ordered Matrices*, SIAM J. Matrix Anal. Appl. 14 (1993), 259–278, https://doi.org/10.1137/0614021 ; https://authors.library.caltech.edu/records/re6d0-rax94 .
3. G. Dessalew, T. Kebede, G. Awgichew and A. Walelign, *Generalized Refinement of Gauss–Seidel Method for Consistently Ordered 2-Cyclic Matrices*, Abstract and Applied Analysis (2021), article 8343207 (first published 2021-06-01), https://doi.org/10.1155/2021/8343207 .
4. P. Xiao, Z. Xiao and R. Sun, *Understanding Limitation of Two Symmetrized Orders by Worst-case Complexity*, arXiv:1910.04366 (first posted 2019-10-10), https://arxiv.org/abs/1910.04366 .
5. C.-C. J. Kuo and T. F. Chan, *Two-Color Fourier Analysis of Iterative Algorithms for Elliptic Problems with Red/Black Ordering*, SIAM J. Sci. Stat. Comput. 11 (1990), https://doi.org/10.1137/0911045 .
