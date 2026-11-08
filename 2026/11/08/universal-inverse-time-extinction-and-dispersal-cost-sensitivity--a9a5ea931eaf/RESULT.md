# Universal inverse-time extinction and dispersal-cost sensitivity at the metapopulation threshold

## Finding
For the critical, positive, density-dependent Beverton–Holt dispersal family defined below, every nonzero population trajectory has a universal inverse-time extinction profile:

\[
\lim_{t\to\infty}t\,x(t)=\frac{v}{\alpha},\qquad
\alpha=\sum_{i=1}^{n}\sum_{j=1}^{n}w_i M_{ij}(a_j+b_{ij})v_j^2>0.
\]

The normalized spatial composition converges to the right Perron vector \(v\). Increasing any one density-dependent dispersal-cost coefficient \(b_{ij}\) strictly increases \(\alpha\), so strictly decreases every patch's limiting inverse-time amplitude, even though the entire linearized extinction matrix remains unchanged. In particular, cost coefficients can make the amplitude arbitrarily small while keeping the critical linear threshold exactly fixed.

## Assumptions and scope
Fix an integer \(n\ge2\). Choose \(p_{ij}>0\), \(R_j>0\), \(a_j>0\), and \(b_{ij}\ge0\) for all \(1\le i,j\le n\), and impose the dispersal-probability bounds \(\sum_i p_{ij}<1\) for every source patch \(j\). Let

\[
M_{ij}=p_{ij}R_j,\qquad\rho(M)=1,
\]

where \(\rho\) denotes spectral radius. Define the nonnegative discrete-time population map \(F:\mathbb R_+^n\to\mathbb R_+^n\) by

\[
F_i(x)=\sum_{j=1}^{n}\frac{p_{ij}R_j x_j}{(1+a_jx_j)(1+b_{ij}x_j)}.
\]

Thus patch \(j\) has bounded local reproduction \(f_j(z)=R_jz/(1+a_jz)\), and the fraction of its descendants reaching patch \(i\) is \(d_{ij}(z)=p_{ij}/(1+b_{ij}z)\). All such fractions are positive and their column sums are strictly below one. The theorem does not assume that \(F\) is coordinatewise monotone, and permits density-dependent self-retention as well as cross-patch dispersal.

Because \(M\) is strictly positive and critical, choose its strictly positive Perron right and left eigenvectors \(v,w\) so that

\[
Mv=v,\quad w^{\mathsf T}M=w^{\mathsf T},\quad
\sum_jv_j=1,\quad w^{\mathsf T}v=1.
\]

All limits are over integer times \(t\to\infty\) for **every** initial condition \(x(0)\in\mathbb R_+^n\setminus\{0\}\). For \(x(0)=0\), the trajectory is identically zero and the inverse-time limit statement is not asserted.

## Proof
**1. Global extinction.** Write \(V(x)=w^{\mathsf T}x\). Each factor in the denominators of \(F\) is at least one, and for every \(x\ne0\) at least one source coordinate is positive. Since \(a_j>0\) and every entry of \(M\) and \(w\) is positive, all components of \(F(x)\) are strictly below the corresponding components of \(Mx\). Therefore

\[
0<V(F(x))<w^{\mathsf T}Mx=V(x)\quad(x\ne0).
\]

The orbit remains in the compact simplex \(\{x\ge0:V(x)\le V(x(0))\}\). If the decreasing sequence \(V(x(t))\) had a positive limit, its accumulation points would lie in a compact annulus with \(V(x)\) bounded away from zero. On this annulus the continuous, strictly positive decrement \(V(x)-V(F(x))\) attains a positive minimum, contradicting convergence of \(V(x(t))\). Consequently \(V(x(t))\to0\) and, because all coordinates of \(w\) are positive, \(x(t)\to0\). Positivity of \(F\) keeps \(V(x(t))>0\) for all finite times.

**2. Convergence of patch proportions.** Taylor expansion at zero, uniform in the nonnegative cone near zero, gives

\[
F_i(x)=\sum_j M_{ij}x_j-\sum_j M_{ij}(a_j+b_{ij})x_j^2+O(\lVert x\rVert^3).
\]

Put \(V_t=V(x(t))\) and \(y_t=x(t)/V_t\), so \(w^{\mathsf T}y_t=1\). Since the set of such \(y_t\) is compact, the expansion yields

\[
V_{t+1}=V_t+O(V_t^2),\qquad
\frac{V_{t+1}}{V_t}=1+O(V_t),\qquad
y_{t+1}=My_t+O(V_t).
\]

The errors are uniform for \(y_t\ge0\) with \(w^{\mathsf T}y_t=1\). Define \(z_t=y_t-v\). Then \(w^{\mathsf T}z_t=0\). The subspace \(E=\{z:w^{\mathsf T}z=0\}\) is invariant under \(M\), and strict positivity of \(M\) implies every eigenvalue of \(M|_E\) has modulus strictly below one. In a suitable norm on \(E\), \(\lVert M|_E\rVert<1\). Therefore the stable forced recurrence \(z_{t+1}=Mz_t+o(1)\) has \(z_t\to0\): an elementary proof is to iterate its geometric contraction bound, splitting the forcing sum into a finite early part and a uniformly small late part. Hence \(y_t\to v\).

**3. Exact extinction amplitude.** Apply \(w^{\mathsf T}\) to the Taylor formula and use \(y_t\to v\):

\[
V_{t+1}=V_t-\alpha V_t^2+o(V_t^2),\quad
\alpha=\sum_{i,j} w_i M_{ij}(a_j+b_{ij})v_j^2>0.
\]

Since \(V_{t+1}/V_t\to1\), reciprocation gives

\[
\frac1{V_{t+1}}-\frac1{V_t}
=\frac{V_t-V_{t+1}}{V_tV_{t+1}}\longrightarrow\alpha.
\]

Summing these increments and taking their arithmetic means yields \(1/(tV_t)\to\alpha\). Therefore \(tV_t\to1/\alpha\) and \(t x(t)=(tV_t)y_t\to v/\alpha\), as claimed.

**4. Strict cost sensitivity.** With \(p,R,a\) fixed, neither \(M\) nor \(v,w\) depends on \(b\). Hence

\[
\frac{\partial\alpha}{\partial b_{ij}}
=w_iM_{ij}v_j^2>0.
\]

Increasing one or more \(b_{ij}\), at least one strictly, increases \(\alpha\) strictly and multiplies every patch's limiting amplitude by \(\alpha_{\mathrm{old}}/\alpha_{\mathrm{new}}<1\). Sending any one cost to infinity sends \(\alpha\to\infty\) while \(\rho(M)=1\) remains fixed.

## Verification
A completely rational two-patch example uses

\[
p=\begin{pmatrix}1/2&1/4\\1/4&1/2\end{pmatrix},\quad
R_1=R_2=4/3,\quad a_1=a_2=1,\quad
M=\begin{pmatrix}2/3&1/3\\1/3&2/3\end{pmatrix}.
\]

The column sums of \(p\) equal \(3/4\), and \(M\) has eigenvalues \(1\) and \(1/3\), with \(v=(1/2,1/2)^{\mathsf T}\) and \(w=(1,1)^{\mathsf T}\). All-zero costs give \(\alpha=1/2\) and \(t x_i(t)\to1\). Replacing costs with

\[
b=\begin{pmatrix}0&1\\2&3\end{pmatrix}
\]

gives \(\alpha=5/4\) and \(t x_i(t)\to2/5\), for each patch \(i\), without changing any entry of \(M\). The exact ratio of new to old amplitudes is \(2/5\). The standalone Python standard-library program `verify.py` checks these rational identities, a heterogeneous three-patch rational Perron-eigenvector and cost-derivative example, 1,755 rational Taylor-component comparisons across positive mixing matrices of dimensions two through four, and illustrative long-time trajectories. Run from the package root with `python3 verify.py`; its final line must be `VERIFY_OK`. The finite checks illustrate the claims but the proof above establishes every dimension and every admissible parameter choice.

## Relationship to prior work
McGrane-Corrigan, Mason and de Andrade Moral (2024) introduced the encompassing model of bounded local Kolmogorov reproduction and costly density-dependent dispersal. Their Proposition 2 gives global extinction under a **strict** subcritical spectral-radius condition and additional transport restrictions, while their Theorem 5.1 and Theorem 5.2 address positive equilibria and persistence when the spectral radius exceeds one. The exact equality case and its global inverse-time profile are not among those stated results. Their model definition also permits the dispersal functions used here.

Kirkland, Li and Schreiber (2006) treat constant dispersal in patchy landscapes and include extinction results at or below threshold; those results are prior coverage of qualitative extinction in a narrower regime, not an inverse-time amplitude for density-dependent dispersal. Cushing and Farrell (2020) analyze local bifurcation coefficients and stability of equilibria for general nonlinear matrix models, so the Perron-projected quadratic coefficient is not presented as a new normal-form technique. The result here instead establishes a **global, initial-state-independent trajectory limit** and an exact, strictly monotone derivative of that limit with respect to density-dependent dispersal cost. Closely related generic critical-map theory may imply parts of the proof; publication-priority uniqueness is not asserted.

## Limitations
This is a deterministic density model with positive, all-to-all mixing at zero density; it does not address stochastic demographic extinction, sparse or reducible transport networks, discontinuous functions, or time-varying patches. Strict competition \(a_j>0\) guarantees a nonzero quadratic damping coefficient. The limit does not establish a uniform convergence rate in initial state or any finite-time ordering of trajectories for different costs. Larger dispersal costs can change intermediate transients even though the asymptotic amplitude is monotone. Higher-order corrections are unproved. Originality is subject to possible unindexed general nonlinear Perron–Frobenius or center-manifold results.

## References
1. B. McGrane-Corrigan, O. Mason and R. de Andrade Moral, *A density-dependent metapopulation model: Extinction, persistence and source-sink dynamics*, arXiv:2405.04505, first public May 7, 2024. https://arxiv.org/abs/2405.04505
2. S. Kirkland, C.-K. Li and S. J. Schreiber, *On the Evolution of Dispersal in Patchy Landscapes*, SIAM Journal on Applied Mathematics, 2006, DOI:10.1137/050628933. https://doi.org/10.1137/050628933
3. J. M. Cushing and A. P. Farrell, *A bifurcation theorem for nonlinear matrix models of population dynamics*, Journal of Difference Equations and Applications 26 (2020), 25–44, DOI:10.1080/10236198.2019.1699916. Author manuscript: https://math.arizona.edu/~cushing/general-bifurcation-theorem-JDEA2019.pdf
