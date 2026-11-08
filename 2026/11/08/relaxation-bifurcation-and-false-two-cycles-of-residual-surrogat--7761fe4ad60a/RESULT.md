# Relaxation bifurcation and false two-cycles of residual surrogate-hyperplane projection

## Finding
The direct residual-surrogate-hyperplane projection can develop a precisely classifiable false periodic orbit on inconsistent least-squares systems, even when every column of the coefficient matrix is orthogonal to every other column and all nonzero singular values are equal. For the iteration defined below, unit relaxation yields an exact two-cycle from **every** nonoptimal starting point. Every fixed relaxation strictly between one and two instead yields a globally attracting nonzero two-cycle; adjacent-iterate averaging converges to the unique least-squares solution. The relaxation \(\omega=3/2\) gives quadratic attraction to the **incorrect** two-cycle, rather than to the solution.

## Assumptions and scope
Let \(m>n\ge1\), \(A\in\mathbb R^{m\times n}\), and \(A^{\mathsf T}A=\lambda I_n\) with \(\lambda>0\). Fix \(x_\star\in\mathbb R^n\), nonzero \(z\in\ker A^{\mathsf T}\), and fixed data \(b=Ax_\star+z\). The unique least-squares solution is \(x_\star\). Put \(c=\|z\|_2^2/\lambda>0\).

For a fixed \(\omega\in[1,2)\), consider the **unextended, full-residual** relaxed surrogate-hyperplane projection
\[
 r_k=b-Ax_k,\qquad
 x_{k+1}=x_k+\omega\frac{\|r_k\|_2^2}{\|A^{\mathsf T}r_k\|_2^2}A^{\mathsf T}r_k,
 \qquad x_0\ne x_\star.
\]
The update is well-defined for every finite iterate under these assumptions. This is a stand-alone deterministic algorithmic model: it is not the double/triple extended normal-equation algorithm and does not state anything about its convergence.

Write \(v=(x_0-x_\star)/\|x_0-x_\star\|_2\) and \(\rho_k=\|x_k-x_\star\|_2\). Then:

1. At \(\omega=1\), the exact identities \(x_{k+2}=x_k\) and \(\rho_{k+1}=c/\rho_k\) hold for all \(k\ge0\). The cycle is nontrivial because \(x_{k+1}-x_\star\) always has the opposite sign to \(x_k-x_\star\), even when the two radii coincide.
2. At every \(1<\omega<2\), set \(\rho_\star=\sqrt{\omega c/(2-\omega)}\). Then
\[
 x_{2j}\longrightarrow x_\star+\rho_\star v,
 \qquad x_{2j+1}\longrightarrow x_\star-\rho_\star v,
 \qquad \frac{x_k+x_{k+1}}2\longrightarrow x_\star.
\]
The scalar radius map has local multiplier \(2\omega-3\). For \(\omega\ne3/2\), every nonstationary orbit converges to the radius at asymptotic linear rate \(\lvert2\omega-3\rvert\), except the possibility of landing on the fixed radius in finitely many steps.
3. At \(\omega=3/2\), the radius iteration is **exactly** the Babylonian square-root iteration for \(\rho_\star=\sqrt{3c}\):
\[
 \rho_{k+1}=\tfrac12\left(\rho_k+\frac{\rho_\star^2}{\rho_k}\right),
 \qquad \rho_{k+1}-\rho_\star=\frac{(\rho_k-\rho_\star)^2}{2\rho_k}.
\]
Consequently the radius converges quadratically (after at most one iterate); whenever it is not already stationary, the adjacent-iterate average also converges quadratically to \(x_\star\).

## Proof
For \(e_k=x_k-x_\star\), the exact orthogonal decomposition \(r_k=z-Ae_k\) implies
\[
 A^{\mathsf T}r_k=-\lambda e_k,\qquad
 \|r_k\|_2^2=\|z\|_2^2+\lambda\|e_k\|_2^2,
 \qquad \|A^{\mathsf T}r_k\|_2^2=\lambda^2\|e_k\|_2^2.
\]
Substituting into the update gives the exact vector recurrence, for every \(e_k\ne0\),
\[
 e_{k+1}=-\left(\omega-1+\frac{\omega c}{\|e_k\|_2^2}\right)e_k.
 \tag{1}
\]
Its scalar coefficient is strictly negative for \(\omega\ge1\), so no iterate can equal zero, the direction alternates, and \(\rho_{k+1}=(\omega-1)\rho_k+\omega c/\rho_k\). At \(\omega=1\), equation (1) becomes \(e_{k+1}=-c e_k/\rho_k^2\), immediately yielding \(e_{k+2}=e_k\), proving the first assertion.

Fix \(1<\omega<2\), put \(a=\omega-1\in(0,1)\), and define \(s_k=\rho_k/\rho_\star>0\). The unique positive fixed point of the radius recurrence is \(\rho_\star\), and its normalized map reads
\[
 s_{k+1}=a s_k+(1-a)s_k^{-1}.
 \tag{2}
\]
For any \(s>0\) with \(s\ne1\), equation (2) places \(s'\) strictly between \(s\) and \(1/s\). Thus \(\lvert\log s'\rvert<\lvert\log s\rvert\). The sequence \(\lvert\log s_k\rvert\) decreases to a nonnegative limit. Were that limit positive, compactness of the closed interval bounded by \(s_0\) and \(1/s_0\), together with strictness and continuity, would give a uniform positive decrement, a contradiction. Hence \(s_k\to1\). Alternating signs in (1) give the exact two subsequence limits. Because \(e_k+e_{k+1}=(-1)^k(\rho_k-\rho_{k+1})v\), their midpoint tends to zero error.

Differentiating the radius map \(f(\rho)=a\rho+\omega c/\rho\) at its fixed point yields
\[
 f'(\rho_\star)=a-\frac{\omega c}{\rho_\star^2}=2\omega-3.
\]
This multiplier is of modulus strictly below one. Unless an orbit lands exactly at the fixed radius, the usual one-dimensional Taylor expansion yields the asserted asymptotic linear rate for \(\omega\ne3/2\). At \(\omega=3/2\), substitution of \(\rho_\star^2=3c\) gives the displayed exact squared-error identity. The midpoint error is half the difference between two successive signed radii, so it has the same quadratic asymptotic convergence as the radius, unless its error vanishes finitely. This proves all assertions.

## Verification
`verify.py` checks the symbolic fixed-point and derivative identities, the exact rational involution, the exact quadratic Babylonian identity, and 4,320 direct vector updates compared against the radial recurrence across three column scalings, six relaxations, and four initial radii. It also checks representative global limits. The program returns `VERIFY_OK 4320 direct vector steps, symbolic and exact rational identities`. The proof above, not this finite sampling, establishes all-dimensional statements.

## Relationship to prior work
Wang and Yin (2023) studied surrogate-hyperplane Kaczmarz for **consistent** systems; Wang, Yin and Zhao (2024) explicitly printed the residual-weighted hyperplane update for a sparse, constrained variant. Dai and Zhang (2026) addressed **extended** normal equations with distinct double/triple Kaczmarz algorithms capable of handling inconsistency. An extended correction changes the algorithm, and its convergence theorem does not apply to the unextended projection analyzed here. Earlier extended Kaczmarz papers address related but distinct iterations. The result above specifies an exact **global dynamical bifurcation**, a Newton-type false-attraction rate, and a midpoint-recovery mechanism for the unextended map, rather than merely noting the need for an extended method.

## Limitations
The analysis is for fixed inconsistent data, equal-norm orthogonal columns, exact arithmetic, and \(1\le\omega<2\). It does not prove a corresponding classification for general coefficient matrices, stochastic row sampling, refreshed independent noise, sparsity-proximal postprocessing, or the double/triple extended algorithms. The unconstrained least-squares solution \(x_\star\) is used solely to describe error and need not be known to run the update. Historical priority relative to unpublished or inaccessible classical analyses of inconsistent surrogate projections remains unverified. The accessible abstract and publication record for the motivating 2026 paper do not replace inspection of its complete text.

## References
- S. Dai and J. Zhang, *Residual-based surrogate hyperplane double and triple Kaczmarz algorithms for solving extended normal equations*, Mathematica Numerica Sinica 48 (2026), 123–140; first public date stated by the publisher: 2026-01-29. https://doi.org/10.12286/jssx.j2025-1306
- Z. Wang and J.-F. Yin, *A surrogate hyperplane Kaczmarz method for solving consistent linear equations*, Applied Mathematics Letters 144 (2023), 108704. https://doi.org/10.1016/j.aml.2023.108704
- Z. Wang, J.-F. Yin and J.-C. Zhao, *The sparse Kaczmarz method with surrogate hyperplane for the regularized basis pursuit problem*, preprint (2024). https://arxiv.org/abs/2406.15082
- K. Zhang, X.-X. Chen and X.-L. Jiang, *A residual-based surrogate hyperplane extended Kaczmarz algorithm for large least squares problems*, Calcolo (2024). https://doi.org/10.1007/s10092-024-00605-0
- Z. Dong, Z. Wang, G. Yin and J.-F. Yin, *A surrogate hyperplane Bregman–Kaczmarz method for solving linear inverse problems*, Journal of Scientific Computing 102 (2025). https://doi.org/10.1007/s10915-024-02737-5
