# Exact embedding-distortion frontier for positive sketched harmonic Ritz values

## Finding
Let \(A\in\mathbb R^{n\times n}\) be symmetric positive definite, with spectral condition number \(\kappa=\lambda_{\max}(A)/\lambda_{\min}(A)\ge1\). Its **exact universal squared-norm embedding-distortion threshold** for positivity of sketched harmonic Ritz values is
\[
\boxed{\varepsilon_\star(A)=\frac{2\sqrt\kappa}{\kappa+1}.}
\]
For every starting vector and every full-rank Krylov basis, every sketched harmonic Ritz value lies in the open right half-plane whenever \(0\le\varepsilon<\varepsilon_\star(A)\). The threshold is sharp for each nonscalar \(A\), even with one Krylov vector: at equality its reduced Gram factor can be singular, and at every larger distortion below one it can have a negative Ritz value. For scalar positive matrices, every admissible distortion below one is safe.

In comparison with the sufficient distortion \(\varepsilon<\kappa^{-1}\) in the motivating analysis, the exact SPD positivity frontier scales as \(2/\sqrt\kappa\), not \(1/\kappa\). This statement concerns Ritz-value location, not the entire convergence rate of a restarted algorithm.

## Assumptions and scope
Fix any integer \(n\ge1\), any real SPD matrix \(A\in\mathbb R^{n\times n}\), any nonzero \(b\in\mathbb R^n\), and any \(m\ge1\) for which the polynomial Krylov subspace
\[
\mathcal K_m(A,b)=\operatorname{span}\{b,Ab,\ldots,A^{m-1}b\}
\]
has dimension \(m\). Let \(B\in\mathbb R^{n\times m}\) be any full-column-rank basis of that space, \(Z=AB\), and \(S\in\mathbb R^{s\times n}\) any real matrix satisfying the squared-norm subspace embedding
\[
(1-\varepsilon)\|v\|_2^2\le\|Sv\|_2^2\le(1+\varepsilon)\|v\|_2^2
\qquad(v\in\mathcal K_{m+1}(A,b)),\quad0\le\varepsilon<1.
\]
Define the sketched harmonic pencil
\[
G=(SZ)^{\mathsf T}SB,\qquad F=(SZ)^{\mathsf T}SZ.
\]
When \(G\) is nonsingular, the sketched harmonic Ritz values are the eigenvalues of \(H=G^{-1}F\), equivalently the generalized eigenvalues of \((F,G)\). Here \(\kappa\) denotes the actual spectral condition number, not merely an upper bound. A prescribed upper bound \(\kappa\le K\) yields the sharp uniform sufficient threshold \(2\sqrt K/(K+1)\).

## Proof
**1. Sharp SPD angle.** Scale \(A\) so its spectrum is contained in \([1,\kappa]\). Every spectral value \(\lambda\) satisfies
\[
\lambda^2\le(\kappa+1)\lambda-\kappa.
\]
For a nonzero complex vector \(w\), write \(r=(w^*Aw)/(w^*w)\in[1,\kappa]\). The spectral theorem gives
\[
\frac{\|Aw\|_2^2}{\|w\|_2^2}\le(\kappa+1)r-\kappa,
\qquad
\frac{\Re(w^*Aw)}{\|Aw\|_2\|w\|_2}
\ge\frac{r}{\sqrt{(\kappa+1)r-\kappa}}
\ge\frac{2\sqrt\kappa}{\kappa+1}.
\]
The last inequality follows by minimizing the displayed one-variable function on \([1,\kappa]\); its minimum is attained at \(r=2\kappa/(\kappa+1)\). Thus the angular bound also holds for complex vectors used as eigenvectors of real pencils. At \(\kappa=1\), it reads one.

**2. Embedding and accretivity.** Let \(T=\mathcal K_{m+1}(A,b)\). Because \(A\mathcal K_m\subseteq T\), both \(w=By\) and \(Aw\) belong to the complexification of \(T\) for every \(y\in\mathbb C^m\). The embedding inequality says that the compression to \(T\) of \(E=S^{\mathsf T}S-I\) has Hermitian operator norm at most \(\varepsilon\). By polarization, including complex vectors,
\[
|u^*Ev|\le\varepsilon\|u\|_2\|v\|_2\qquad(u,v\in T_{\mathbb C}).
\]
For \(y\ne0\), set \(w=By\ne0\). Applying the angular bound,
\[
\Re(y^*Gy)=\Re((Aw)^*S^{\mathsf T}Sw)
\ge(\varepsilon_\star-\varepsilon)\|Aw\|_2\|w\|_2>0.
\]
Therefore the Hermitian part of \(G\) is positive definite and \(G\) is invertible. The embedding also gives \(y^*Fy=\|SAw\|_2^2>0\). If \(Hy=\theta y\), then \(Fy=\theta Gy\) and
\[
\theta=\frac{y^*Fy}{y^*Gy};
\]
the numerator is strictly positive real and the denominator has strictly positive real part, so \(\Re\theta>0\). This holds for all admissible Krylov dimensions and basis choices.

**3. Exact sharpness.** For any \(\kappa>1\), take the two-dimensional choice
\[
A=\operatorname{diag}(1,\kappa),\qquad b=(\sqrt\kappa,1)^{\mathsf T},
\qquad S^{\mathsf T}S=\begin{pmatrix}1&-\varepsilon\\-\varepsilon&1\end{pmatrix}.
\]
For every \(0\le\varepsilon<1\), the specified Gram matrix is positive definite and possesses a real square root \(S\). Its eigenvalues are \(1-\varepsilon\) and \(1+\varepsilon\), so the embedding distortion on the full two-dimensional space is exactly \(\varepsilon\). At \(m=1\), using \(B=b\) (normalization cancels), direct multiplication gives
\[
G=2\kappa-\varepsilon\sqrt\kappa(\kappa+1)
=\sqrt\kappa(\kappa+1)(\varepsilon_\star-\varepsilon),
\qquad F=\kappa(\kappa+1-2\varepsilon\sqrt\kappa)>0.
\]
Thus at \(\varepsilon=\varepsilon_\star<1\), the reduced Gram factor \(G\) is singular and \(H\) is undefined; for every \(\varepsilon_\star<\varepsilon<1\), its scalar Ritz value \(F/G\) is negative. The same witness can be built within the extreme-eigenvector plane of any nonscalar SPD matrix, so the threshold is exact for each matrix, not just uniformly over all matrices of condition number \(\kappa\). If \(\kappa=1\), \(A\) is a positive scalar multiple of the identity, and \(G\) is positive definite for every embedding with \(\varepsilon<1\). This finishes the classification.

## Verification
The supplementary `VERIFY.py` performs deterministic two-dimensional sign and Gram-matrix identities over seven condition numbers, an exact rational boundary identity at \(\kappa=9\), four angle-equality checks, and 750 randomized five-dimensional SPD/Krylov/pencil tests. It returned `VERIFY_OK 783 checks`. Reproduce with `python VERIFY.py` and NumPy. Finite tests are supplementary; the proof above establishes the universal statement.

## Relationship to prior work
Güttel, Liu and Nyman (arXiv:2607.10354v2, Section 5.3) define exactly the sketched harmonic pencil above and derive the sufficient right-half-plane condition \(\varepsilon\|A^{-1}\|_2<\min_{\|v\|_2=1}\Re(v^*A^{-1}v)\); for SPD matrices this is \(\varepsilon<\kappa^{-1}\). Their restarted convergence theorem additionally requires a separate residual-contraction condition. The present result replaces only their Ritz-positivity criterion by the exact, sharp SPD threshold \(2\sqrt\kappa/(\kappa+1)\), without asserting the other conditions follow.

Timsit, Grigori and Balabanov (arXiv:2302.07466v3, Proposition 3.1) analyze a different sketched Petrov–Galerkin quasi-optimality guarantee under a sufficient condition of order \(\kappa^{-1/2}\), not this exact harmonic-pencil positivity frontier. De Damas, Grigori, Simunec and Timsit (arXiv:2512.15455v1) review randomized Krylov projections and Ritz procedures but do not state this sharp classification. The angle inequality itself is a classical Kantorovich/antieigenvalue fact; its use here and the sharp sketch counterexample are the claimed contribution. A prior one-step Gaussian-sketch Ritz sign law addresses random-sketch probabilities, not worst-case arbitrary embeddings or every Krylov dimension; no Gaussian law is claimed here.

## Limitations
This result assumes a **real symmetric positive-definite** matrix, exact arithmetic, and the specified embedding holding on the whole next Krylov space. It does not extend automatically to nonnormal positive-real matrices, to finite-precision loss of independence, or to sketches without the embedding guarantee. A single deterministic signed Gram perturbation supplies sharpness; a random sketch need not attain it. The conclusion concerns the open right half-plane and existence of the harmonic reduced pencil; it does not prove that a restarted iteration contracts, since that requires additional hypotheses. Standard angle inequalities are preexisting, and exhaustive historical priority is not certified.

## References
1. S. Güttel, J. Liu and L. Nyman, *Sketch-and-Restart: Randomized Sketching in Quadrature-Based Restarting for Matrix Functions*, arXiv:2607.10354, initial public version 11 July 2026; revision 27 October 2026, especially Section 5.3 and Theorem 9. https://arxiv.org/html/2607.10354v2
2. E. Timsit, L. Grigori and O. Balabanov, *Randomized Orthogonal Projection Methods for Krylov Subspace Solvers*, arXiv:2302.07466v3 (2023), especially Proposition 3.1. https://arxiv.org/html/2302.07466v3
3. J.-G. de Damas, L. Grigori, I. Simunec and E. Timsit, *Randomized orthogonalization and Krylov subspace methods: principles and algorithms*, arXiv:2512.15455v1 (2025), Sections 5–7. https://arxiv.org/html/2512.15455v1
4. S. Güttel and M. Schweitzer, *Randomized sketching for Krylov approximations of large-scale matrix functions*, arXiv:2208.11447v3 (2023), Section 3. https://arxiv.org/html/2208.11447v3
