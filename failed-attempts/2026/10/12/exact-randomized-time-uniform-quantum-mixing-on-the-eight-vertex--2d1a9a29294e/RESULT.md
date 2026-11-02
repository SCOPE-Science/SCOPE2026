# Exact randomized-time uniform quantum mixing on the eight-vertex path

## Finding

Let \(P_8\) be the simple unweighted path with vertex set \(\{1,\ldots,8\}\), and let \(A\) be its adjacency matrix. Put \(U(t)=\exp(itA)\) and \(M(t)_{ij}=|U(t)_{ij}|^2\). There are nonnegative real numbers \(t_1,\ldots,t_s\), positive weights \(p_1,\ldots,p_s\), and \(s\le17\), such that
\[
\sum_{a=1}^{s}p_a=1,\qquad \sum_{a=1}^{s}p_aM(t_a)=\frac18J_8.
\]
The existence is exact, not merely an arbitrarily close approximation. The mathematical witness is a strictly positive, 64-point **phase-torus** probability distribution and a 16-dimensional affine-span certificate. The phase-torus support points are not asserted to be attainable at exact physical times.

## Assumptions and scope

The walk is continuous-time, coherent, unweighted and governed by the **adjacency** Hamiltonian, rather than the Laplacian or a discrete-time coin. The observation time may be chosen by any Borel probability measure on \([0,\infty)\). The statement concerns the single graph \(P_8\), not all paths. All probabilities are classical mixtures of projective measurement probabilities, not amplitudes.

## Proof

**Spectral reduction.** The eight path eigenvalues and normalized real eigenvectors are
\[
\lambda_k=2\cos(k\pi/9),\quad v_k(i)=\sqrt{2/9}\sin(ik\pi/9),\quad 1\le k,i\le8.
\]
For \(1\le k\le4\), define \(w_k(i,j)=v_k(i)v_k(j)\). Eigenvalue conjugate pairing gives
\[
U(t)_{ij}=\begin{cases}2\sum_{k=1}^4w_k(i,j)\cos(\lambda_kt),&i+j\equiv0\pmod2,\\ 2i\sum_{k=1}^4w_k(i,j)\sin(\lambda_kt),&i+j\equiv1\pmod2.\end{cases}
\]
The exact relations \(\lambda_1=\lambda_2+\lambda_4\), \(\lambda_3=1\), and \(\lambda_4=\lambda_2^2-2\) hold. The number \(\lambda_2\) has irreducible polynomial \(X^3-3X+1\) over \(\mathbb Q\), hence \(1,\lambda_2,\lambda_4\) are linearly independent over \(\mathbb Q\). Kronecker's theorem therefore makes the positive-time trajectory dense in the three-torus of phases
\[
(\phi_1,\phi_2,\phi_3,\phi_4)=(a+b,a,c,b)\pmod{2\pi}.
\]

**Exact phase-torus probability law.** Let \(a,b,c\) take values in \(\{0,\pi/2,\pi,3\pi/2\}\). Assign probability \(W_{abc}/256\), where the 64 **strictly positive integers** \(W_{abc}\) are the 4-by-4-by-4 array literally included in `verify.py` (each displayed innermost four-tuple runs over \(c\)). That standalone file is part of this result. Its integer checks prove \(\sum W_{abc}=256\) and \(\min W_{abc}=1\).

Write \(C_k=\cos\phi_k\), \(S_k=\sin\phi_k\), and \(s=(1,-1,1,-1)\). Summation over the 64 explicit atoms, by integer arithmetic, yields
\[
\mathbb E[C_kC_\ell]=\frac{9\delta_{k\ell}-1}{16},\qquad
\mathbb E[S_kS_\ell]=\frac{9\delta_{k\ell}-s_ks_\ell}{16}.
\]
The eigenprojector products satisfy the exact identities
\[
\sum_{k=1}^4w_k(i,j)^2=\frac1{18}+\frac{[i=j]+[i+j=9]}{36},
\]
\[
\sum_kw_k(i,j)=\frac{[i=j]}2\quad(i+j\ \text{even}),\qquad
\sum_ks_kw_k(i,j)=\frac{[i+j=9]}2\quad(i+j\ \text{odd}).
\]
Here \([P]\) is 1 when statement \(P\) holds and 0 otherwise. For even \(i+j\), substituting the first moment matrix into the squared cosine amplitude gives
\[
\mathbb E[M_{ij}]=\frac94\sum_kw_k(i,j)^2-\frac14\Big(\sum_kw_k(i,j)\Big)^2=\frac18.
\]
For odd \(i+j\) the sine moment matrix and signed sum give the identical value \(1/8\). The exact cyclotomic-field verification of all 64 entries is reproduced by `verify.py`.

**From torus phases to actual times.** Let \(F:\mathbb T^3\to\mathbb R^{36}\) list the upper-triangular entries of the corresponding symmetric mixing matrix. Every coordinate of \(F\) is a constant plus a real linear combination of the 16 harmonics \(\cos(2\phi_k)\), \(\cos(\phi_k+\phi_\ell)\), and \(\cos(\phi_k-\phi_\ell)\), with \(k<\ell\). Thus the affine hull of \(F(\mathbb T^3)\) has dimension at most 16.

The 64 grid images have affine dimension **at least 16**, proved by exact reduction modulo 109 of a cyclotomic-field matrix of differences and modular Gaussian elimination (`verify.py`, assertion `mod109_affine_rank=16`). Because 109 is prime and coprime to all coefficient denominators in that reduction, nonzero modular minors imply nonzero characteristic-zero minors. Hence these 64 images have the same full 16-dimensional affine hull as the complete torus image.

All 64 weights are strictly positive, so the target \(J_8/8\) lies in the relative interior of the convex hull of the grid images, and hence in the relative interior of \(\operatorname{conv}F(\mathbb T^3)\). For a dense subset \(D\) of a compact subset \(K\) in a finite-dimensional affine space, \(\operatorname{relint}\operatorname{conv}K\subseteq\operatorname{conv}D\) when the affine hulls agree: a small enclosing finite simplex or crosspolytope survives sufficiently close approximation of its vertices by points of \(D\). Applying this elementary stability fact to the dense **positive-time** orbit proves that the target is in the convex hull of actual physical-time mixing matrices. Finally, Carathéodory's theorem in affine dimension 16 bounds the required support by 17 times. This proves the claim.

## Verification

Run `python3 verify.py` from the embedded package. It checks the complete exact 64-atom probability table, all 32 real cosine/sine second moments, every one of the 64 matrix entries using exact arithmetic in \(\mathbb Q[\zeta_{18}]\), and the modular affine-rank certificate. Expected output: `VERIFY_OK pmf=64 exact_moments=32 exact_projector_entries=64 mod109_affine_rank=16`. The last check is not a floating-point rank test; it is exact reduction modulo 109. Physical-time support is established through a convex-density theorem, not numerical time search.

## Relationship to prior work

Baptista, Coutinho and Marques (arXiv:2308.16378, initially public on 2023-08-31) introduce generalized average mixing matrices under arbitrary sampling measures, demonstrate uniform expected mixing for the three- and four-vertex paths, and ask for more examples. A later study (arXiv:2609.14463, initial 2026-09-13) gives positive arithmetic families when the path order plus one is prime, a power of two, or twice a prime, and has explicit negative families. The present claim concerns the first odd-composite-square case \(8+1=9\), not one of the positive families described in that paper's publicly accessible abstract. The abstract cannot exclude more comprehensive results in its inaccessible body, so literature-overlap risk is expressly retained. The standard infinite-time Cesàro average is not the arbitrary sampling law here.

## Limitations

This is a theorem for one specific eight-vertex graph, not a universal classification. The 64-atom law is a **spectral phase** witness; actual observation times and weights exist but are not explicitly enumerated, nor is any time-magnitude upper bound proved. The result does not assert perfect instantaneous uniform mixing. The possibly stronger 2026 preprint could not be compared beyond its accessible abstract; further specialist literature review remains warranted. Finite algebraic and modular checks certify only the identified finite identities; Kronecker density, relative-interior transfer, and Carathéodory support reduction are separate analytical arguments.

## References

1. P. Baptista, G. Coutinho, and V. Marques, *Unexpected Averages of Mixing Matrices*, arXiv:2308.16378v1 (public 2023-08-31), https://arxiv.org/abs/2308.16378.
2. M. Kang, *Arithmetic of Bohr Frequencies Governs Uniform Mixing in Randomly Timed Quantum Spin Chains*, arXiv:2609.14463v1 (public 2026-09-13), https://arxiv.org/abs/2609.14463. Abstract inspected; complete full text was unavailable.
3. Exact standalone computational witness and reproduction instructions: accompanying `verify.py`.
