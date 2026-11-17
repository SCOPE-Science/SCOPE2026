# A subcritical localized pitchfork in a four-oscillator mixed-order path

## Finding
Consider four identical phase oscillators with attractive pairwise coupling on the path \(1-2-3-4\) and the unrestricted-index asymmetric all-to-all triadic interaction specified below. In the co-rotating frame, the balanced antipodal configuration \((0,0,\pi,\pi)\) undergoes a **subcritical pitchfork on the phase quotient** when the triadic-to-per-edge gain ratio passes \(2\). Specifically, with \(\delta=\tau/\kappa-2\), for every sufficiently small \(\delta>0\) there are two distinct nearby non-antipodal equilibrium circles represented by
\[
 (a_\pm,b_\pm,\pi-b_\pm,\pi-a_\pm),\qquad
 b_\pm=\pm\sqrt{\delta}+O(\delta^{3/2}),\quad
 a_\pm=\pm\frac14\delta^{3/2}+O(\delta^{5/2}).
\]
Each of these circles has exactly one unstable transverse eigenvalue, while the antipodal circle is exponentially attracting for \(\delta>0\). The antipodal circle is **nonlinearly unstable at equality** \(\delta=0\); it has one positive transverse eigenvalue for \(\delta<0\). There are no other nonzero reflection-symmetric equilibrium branches sufficiently near this configuration when \(\delta\le0\). The two different displacement exponents show that the bifurcating saddles initially move their two inner vertices at square-root scale while their outer vertices move only at three-halves-power scale. This is a local result, not a global attractor or basin census.

## Assumptions and scope
For \(\kappa>0\) and \(\tau\ge0\), the exact phase ODE on \((\mathbb R/2\pi\mathbb Z)^4\) is
\[
 \dot\theta_i=\kappa\sum_{j:\,|j-i|=1}\sin(\theta_j-\theta_i)
 +\frac{\tau}{16}\sum_{j=1}^4\sum_{\ell=1}^4\sin(2\theta_j-\theta_\ell-\theta_i),
 \qquad i=1,2,3,4.
\]
Both summation indices of the triadic term range independently over all four vertices, including repeated indices. All natural frequencies are identical and have been removed by a common rotating frame. Common phase translation is quotiented out when describing attraction, eigenvalues or instability. The graph has three unit edges; in the mean-degree normalization of Sharma and collaborators, \(\kappa=K_1/(3/2)\) and \(\tau=K_2\). Thus the critical condition is \(K_2/K_1=4/3\), whose **linear** stability aspect was already known for the more general balanced barbell family. Only the nonlinear critical behavior and localized saddle-branch asymptotics are the present finding.

## Proof
**Linear boundary (background, recomputed to fix normalization).** Put \(s=(1,1,-1,-1)^{\mathsf T}\). Differentiating at \(\Theta_*=(0,0,\pi,\pi)\) gives the pairwise signed graph Laplacian contribution plus the rank-one triadic contribution \(-\tau ss^{\mathsf T}/4\). Explicitly the full Jacobian is
\[
J=\begin{pmatrix}
-\kappa-\tau/4&\kappa-\tau/4&\tau/4&\tau/4\\
\kappa-\tau/4&-\tau/4&-\kappa+\tau/4&\tau/4\\
\tau/4&-\kappa+\tau/4&-\tau/4&\kappa-\tau/4\\
\tau/4&\tau/4&\kappa-\tau/4&-\kappa-\tau/4
\end{pmatrix}.
\]
Direct factorization yields
\[
\det(\lambda I-J)=\lambda(\lambda+2\kappa)
 [\lambda^2+\tau\lambda+\kappa\tau-2\kappa^2].
\]
The zero eigenvalue is common phase translation. The three remaining eigenvalues have negative real part exactly for \(\tau>2\kappa\); below this threshold one is positive. At \(\tau=2\kappa\) the zero eigenvalue is double and both remaining eigenvalues equal \(-2\kappa\). This paragraph alone is not the novelty claim.

**Exact invariant reduction.** The reflection-and-inversion symmetry preserves the two-dimensional slice
\[
\mathcal M=\{(a,b,\pi-b,\pi-a):\ |a|,|b|\text{ small}\}.
\]
Writing \(z_1=\frac14\sum_j e^{i\theta_j}=ih\) and \(z_2=\frac14\sum_j e^{2i\theta_j}=Q\) on \(\mathcal M\), we have
\[
h=\frac{\sin a+\sin b}{2},\qquad Q=\frac{\cos 2a+\cos 2b}{2}.
\]
The triadic vector field is exactly \(\tau\operatorname{Im}(z_2\overline{z_1}e^{-i\theta_i})\). Consequently \(\mathcal M\) has the exact equations
\[
 \dot a=\kappa\sin(b-a)-\tau hQ\cos a,\qquad
 \dot b=\kappa[-\sin(b-a)+\sin2b]-\tau hQ\cos b.
\]
Both components are odd under \((a,b)\mapsto(-a,-b)\). Rescale time to \(u=\kappa t\), and set \(\delta=\tau/\kappa-2\). The linearization at the origin of this reduced system is
\[
\begin{pmatrix}-2-\delta/2&-\delta/2\\-\delta/2&-\delta/2\end{pmatrix}.
\]
At \(\delta=0\) the first direction contracts with eigenvalue \(-2\), while the second is central.

**Nonlinear critical instability.** Smooth center-manifold invariance and Taylor expansion of the exact reduced vector field at \(\delta=0\) yield the center graph
\[
a=\frac12 b^3+O(b^5),
\]
and, on that graph,
\[
 \frac{db}{du}=\frac12 b^3+O(b^5).
\]
The positive cubic coefficient implies that the antipodal orbit is Lyapunov unstable at the critical parameter: initial values on a local center manifold with small nonzero \(b\) move away from the origin in forward time. This excludes treating the critical zero eigenvalue as stable by continuity.

**Bifurcating saddles and localization.** Since the derivative of the first reduced equation with respect to \(a\) is \(-2\) at the critical point, the implicit-function theorem solves its equilibrium equation for an analytic odd function \(a=\phi(b,\delta)\). Expansion gives
\[
\phi(b,\delta)=-\frac{\delta b}{4}+\frac{b^3}{2}
+O(\delta^2|b|+|\delta||b|^3+|b|^5).
\]
Substitution in the second equilibrium equation gives, after division by the nonzero \(b\),
\[
0=-\frac\delta2+\frac{b^2}{2}
+O(\delta^2+|\delta|b^2+b^4).
\]
This equation has a unique small solution \(b^2=\delta+O(\delta^2)\) when \(\delta>0\), and none with \(b\ne0\) when \(\delta\le0\). Odd symmetry yields the two branches. Substituting them into \(\phi\) gives the asserted \(\delta^{3/2}/4\) law for \(a\). In the two-dimensional slice, the slow eigenvalue on either nonzero branch is \(\kappa\delta+O(\kappa\delta^2)>0\), while the fast eigenvalue approaches \(-2\kappa\). In the full four-node phase quotient the remaining transverse eigenvalue also approaches \(-2\kappa\). Hence each nonzero branch is a hyperbolic index-one saddle modulo rotation. This confirms a subcritical, not supercritical, pitchfork.

## Verification
`checker.py` independently evaluates the full 64-term asymmetric interaction (four focal indices, 16 double-sum terms each), checks its order-parameter representation and the invariant slice on 200 random configurations, checks the full Jacobian against central differences, symbolically factors the four-dimensional characteristic polynomial, and symbolically checks the cubic coefficients. Numerical nonlinear root solves at six positive small \(\delta\) verify the two distinct localization exponents and the index-one saddle property. All checks passed. The analytic center-manifold and implicit-function arguments above, rather than the finite numerical tests, establish the theorem.

## Relationship to prior work
Sharma et al. (arXiv:2611.09564v1, November 6, 2026) study the same asymmetric global triadic interaction combined with sparse pairwise graph coupling, primarily numerically across random graphs; their equations (1) and (4) supply the model. Costa, Novaes and de Aguiar (arXiv:2501.05670v1) analyze this asymmetric interaction in the all-to-all thermodynamic setting and derive order-parameter bifurcations, including other subcritical transitions. Existing finite barbell stability analysis already determines the **strict linear gain threshold** \(\tau/\kappa=2\) for the four-node path and records an additional zero eigenvalue at equality. None of those statements implies the positive cubic coefficient, critical nonlinear instability, exact local pair of saddle branches, or the distinct \(1/2\) and \(3/2\) vertex-displacement exponents proved here. General signed-Laplacian effective-resistance criteria likewise apply to linear stability but not to these nonlinear coefficients. Standard center-manifold methodology is used, not claimed as a new technique.

## Limitations
The assertion is local near one antipodal configuration in the identical-frequency four-node path. It does not classify other equilibria, other graph families, full basin volumes, heterogeneity, noise, or the random-network thermodynamic limit. The outer-node \(3/2\)-power coefficient depends on the unweighted path and the unrestricted-index asymmetric triadic convention; replacing it with a distinct-index or symmetric three-body sum changes the model. Scientific priority relative to uncatalogued work remains uncertain; no independent validation has been performed.

## References
1. A. Sharma, A. Suman, M. Anvari, M. D. Shrimali, C. I. del Genio, and S. Jalan, *Synchronization transitions in Kuramoto oscillators with mixed interactions*, arXiv:2611.09564v1, first public November 6, 2026. https://arxiv.org/html/2611.09564v1
2. G. S. Costa, M. Novaes, and M. A. M. de Aguiar, *Exact solutions of the Kuramoto model with asymmetric higher order interactions of arbitrary order*, arXiv:2501.05670v1, January 10, 2025. https://arxiv.org/html/2501.05670v1
3. W. Chen et al., *Characterizing the Positive Semidefiniteness of Signed Laplacians via Effective Resistances*, 2016. https://eeqiu.people.ust.hk/wp-content/uploads/2021/09/Characterizing-the-Positive-Semidefiniteness-of-Signed-Laplacians-via-Effective-Resistances.pdf (linear background only; the full document was not used to assert exclusion of nonlinear results).
4. A. Suman and S. Jalan, *Finite-size effect in Kuramoto oscillators with higher-order interactions*, *Chaos* 34, 101101 (2024), DOI: 10.1063/5.0234070. https://pubmed.ncbi.nlm.nih.gov/39393186/
