# Jacobi–cyclic fiber control and a sharp robust budget for anisotropic square grids

## Finding

**Theorem (optimal consecutive-fiber actuation).** Let \(m\ge2\), \(q\ge1\), and let \(A\in\mathbb R^{m\times m}\) be a real symmetric tridiagonal matrix whose off-diagonal entries satisfy \(A_{k-1,k}=A_{k,k-1}=-c_k\), with \(c_k>0\) for \(1\le k<m\). Let \(B\in\mathbb R^{q\times q}\) be symmetric, and suppose the coordinate vector \(e_h\) is cyclic for \(B\): the span of \(e_h,Be_h,\ldots,B^{q-1}e_h\) is all of \(\mathbb R^q\). For every \(t>0\) put

\[
H_t=A\otimes I_q+tI_m\otimes B,
\quad
r(t)=\max_{\lambda\in\sigma(H_t)}\dim\ker(H_t-\lambda I).
\]

Among input matrices consisting of distinct coordinate columns, exactly \(r(t)\) inputs are necessary and sufficient to control \(\dot z=-H_tz+E_Su\). The consecutive fiber

\[
S_t=\{(0,h),(1,h),\ldots,(r(t)-1,h)\}
\]

is optimal. More explicitly, if \(\alpha_0<\cdots<\alpha_{m-1}\) and \(\beta_0<\cdots<\beta_{q-1}\) are the eigenvalues of \(A\) and \(B\), then

\[
r(t)=\max_{\lambda}\#\{(i,j):\alpha_i+t\beta_j=\lambda\}.
\]

At any eigenvalue of multiplicity \(s\), enumerate the distinct contributing first-factor indices \(i_1<\cdots<i_s\) and their uniquely matched second-factor indices \(j_1,\ldots,j_s\). Let \(u_i,v_j\) be any real unit eigenvectors of the two factors. The \(s\times s\) modal observation matrix on the first \(s\) fiber coordinates has the **exact nonzero determinant**

\[
\det M_\lambda=(-1)^{s(s-1)/2}
\frac{\prod_{\ell=1}^{s}u_{i_\ell}(0)v_{j_\ell}(h)}
{\prod_{k=1}^{s-1}c_k^{s-k}}
\prod_{1\le\ell<a\le s}(\alpha_{i_a}-\alpha_{i_\ell}).
\]

**Sharp parameter-uniform consequence.** For every integer \(n\ge3\), give horizontal edges of the Cartesian square grid \(P_n\square P_n\) conductance \(1\) and vertical edges a *common* conductance \(t>0\). One and the same set of \(n-1\) consecutive boundary vertices,

\[
S=\{(0,0),(1,0),\ldots,(n-2,0)\},
\]

controls its full Laplacian dynamics for **every** \(t>0\). No fixed set with fewer coordinates can do so. In particular, the exact parameter-uniform coordinate-actuator budget is \(n-1\), even though a whole boundary row of \(n\) vertices is a standard zero-forcing choice.

## Assumptions and scope

The state is the entire \(mq\)-dimensional product-network state. Each selected coordinate receives its own unrestricted real-valued control input. Controllability means classical finite-dimensional Kalman controllability, equivalently the Popov–Belevitch–Hautus (PBH) test. The first-factor tridiagonal structure is irreducible, and the second-factor root is cyclic. For connected weighted-graph applications, \(A\) can be the Laplacian of a positively weighted path and \(B\) the Laplacian of any undirected weighted graph whose chosen root is cyclic. The square-grid corollary allows a single unknown common vertical weight, not arbitrary independent changes to every edge.

The determinant formula applies to exact eigenvalue coincidences, including resonant values of \(t\). It concerns algebraic controllability, not uniform conditioning or minimum control energy as \(t\) varies.

## Proof

**1. Jacobi endpoint polynomials.** For any eigenvector \(u\) of \(A\) with eigenvalue \(\alpha\), its first coordinate cannot vanish: the first tridiagonal row would then force the second coordinate to vanish, and induction would force the entire vector to vanish. Define \(p_0(x)=1\), \(p_1(x)=(A_{00}-x)/c_1\), and, for \(1\le k<m-1\),

\[
p_{k+1}(x)=\frac{(A_{kk}-x)p_k(x)-c_kp_{k-1}(x)}{c_{k+1}}.
\]

The eigenvector equation yields \(u(k)=u(0)p_k(\alpha)\). Each \(p_k\) has degree exactly \(k\) with leading coefficient \((-1)^k/(c_1\cdots c_k)\). An irreducible symmetric tridiagonal matrix has distinct real eigenvalues; alternatively, the displayed recurrence shows every eigenspace has dimension one, and symmetry rules out nontrivial Jordan blocks.

**2. Cyclic root and modal splitting.** The cyclicity of \(e_h\) for symmetric \(B\) is equivalent to simple eigenvalues and \(v_j(h)\ne0\) for every normalized eigenvector \(v_j\). Eigenvectors of \(H_t\) are the tensor products \(u_i\otimes v_j\), with eigenvalues \(\alpha_i+t\beta_j\). At a fixed product eigenvalue, every first-factor index occurs at most once because the spectrum of \(B\) is simple. The analogous assertion holds for second-factor indices.

**3. Sharp determinant and PBH.** For a product eigenvalue \(\lambda\) of multiplicity \(s\), restriction of its product-eigenvector basis to \((k,h)\), \(0\le k<s\), gives

\[
(M_\lambda)_{k+1,\ell}=p_k(\alpha_{i_\ell})\,u_{i_\ell}(0)\,v_{j_\ell}(h).
\]

By subtracting lower-degree rows, the determinant of the polynomial-evaluation matrix is the ordinary Vandermonde determinant multiplied by the product of the leading coefficients. This is precisely the formula in the Finding section. It never vanishes because every endpoint/root factor is nonzero, all \(c_k>0\), and the first-factor eigenvalues are distinct. Consequently the first \(s\) fiber coordinates separate the whole \(\lambda\)-eigenspace, and the first \(r(t)\) separate every eigenspace. The symmetric-matrix PBH criterion proves controllability. Conversely, an eigenspace of dimension \(r(t)\) cannot inject into fewer than \(r(t)\) coordinate observations, so fewer input columns cannot control the system.

**4. Exact all-weight square-grid budget.** For \(P_n\) with unit conductances, the eigenvalues are

\[
\gamma_i=2-2\cos(\pi i/n),\qquad 0\le i<n.
\]

At \(t=1\), the \(n-1\) distinct pairs \((i,n-i)\), \(1\le i<n\), all have eigenvalue \(4\), since \(\gamma_i+\gamma_{n-i}=4\). Hence any actuator set that works for all \(t>0\) has size at least \(n-1\).

We show no product eigenspace has dimension \(n\) for any \(t>0\). Were that possible, every first-factor spectral index would be paired to a second-factor index under one common sum. Since both factor spectra are strictly increasing, that pairing must be order-reversing, so

\[
\gamma_i+t\gamma_{n-1-i}=\lambda\quad(0\le i<n).
\]

Compare \(i=0\) and \(i=n-1\): \(t=1\) and \(\lambda=\gamma_{n-1}\). But, writing \(c=\cos(\pi/n)\in(0,1)\), the \(i=1\) equation would require an equality contradicted by

\[
\gamma_1+\gamma_{n-2}-\gamma_{n-1}=4c(c-1)<0.
\]

Thus \(r(t)\le n-1\) for every \(t>0\). The theorem's consecutive-fiber construction, enlarged to \(n-1\) vertices, controls every member of the family, proving the sharp robust equality. The same argument applies to observability by coordinate measurements because the Laplacians are symmetric.

## Verification

Run `python verify.py` with Python's standard library. The program uses exact `fractions.Fraction` Gaussian elimination on full Kalman controllability matrices, rather than approximate eigenvalue thresholds. It tests the designated \(n-1\) boundary placements on square grids for \(n=3,4,5\) and \(t\in\{1,1/2,2/3,2\}\); it also checks failure of \(n-2\) boundary actuators at \(t=1\). As a nongrid base test it checks \(P_3\) times a triangle with weighted edges \(1,1,2\), whose simple spectrum is \(\{0,3,5\}\) and whose vertex numbered \(1\) is cyclic, and a nonuniform weighted path times that triangle. The observed verifier output is `VERIFY_OK exact_fraction_cases= 25`.

These finite calculations are reproducibility checks, not a substitute for the all-size proof. No infinite or uniform-in-\(t\) result is inferred from finite enumeration.

## Relationship to prior work

Parlangeli and Notarstefano's grid-controllability analysis (first public version 2012) already supplies the Kronecker eigenvector method, path-coordinate polynomial recurrence, and a determinant condition for arbitrary multiplicity on **unweighted grid graphs**. In particular, the unweighted-grid determinant tests are prior work, not a new contribution here. The present exact theorem treats an **arbitrary rooted cyclic symmetric second factor** (not necessarily a path), an **arbitrary irreducible Jacobi first factor**, and all positive couplings, with an explicitly factorized nonvanishing determinant and a fixed optimal consecutive-fiber design. The parameter-uniform square-grid budget then exploits, separately, the exact spectral obstruction at isotropic coupling.

Monshizadeh, Zhang and Camlibel (2014) characterize leader sets that control an entire qualitative class through zero forcing. That robust-to-*independently variable matrix entries* requirement is stronger than this result's all-positive-*one-parameter anisotropy* family. The usual maximum-eigenspace-multiplicity lower bound by itself does not guarantee that coordinate actuators attain it; the determinant proof is the needed attainment step.

## Limitations

The cyclic-root hypothesis for the second factor is essential to this particular construction: a non-simple second-factor eigenvalue or a zero root component can invalidate the determinant. The theorem does not address arbitrary independent edge-weight perturbations, nonsymmetric generators, uniform smallest singular values, Gramian conditioning, or energy-optimal control. The difference between an explicit new formulation and an implicit extension of the earlier grid polynomial-determinant approach remains a literature-priority risk; independently checked publication priority is not claimed.

## References

- G. Notarstefano and G. Parlangeli, *Controllability and observability of grid graphs via reduction and symmetries*, arXiv:1203.0129, originally public March 1, 2012, especially Sections III and V, Lemma 5.2, Theorem 5.3 and Remark 5.4. https://arxiv.org/abs/1203.0129
- N. Monshizadeh, S. Zhang and M. K. Camlibel, *Zero forcing sets and controllability of dynamical systems defined on graphs*, arXiv:1403.4868, first public March 19, 2014, especially Theorem IV.4 and Corollary IV.6. https://arxiv.org/abs/1403.4868
- Z. Yuan et al., *Exact Controllability of Complex Networks*, arXiv:1310.5806 (2013), for the general unrestricted-input eigenvalue-multiplicity framework. https://arxiv.org/abs/1310.5806
- F. A. Taklimi, S. Fallat and K. Meagher, *On the Relationships between Zero Forcing Numbers and Certain Graph Coverings*, arXiv:1311.7064 (2013), for grid zero-forcing background. https://arxiv.org/abs/1311.7064
