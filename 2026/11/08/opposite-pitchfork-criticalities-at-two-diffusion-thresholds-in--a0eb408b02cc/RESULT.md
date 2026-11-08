# Opposite pitchfork criticalities at two diffusion thresholds in a six-patch predator–prey model

## Finding
For the Ye–Zhou weak-Allee, hyperbolic-mortality networked predator–prey reactions, an explicit positive rational parameter set on the complete bipartite six-patch graph \(K_{3,3}\) has **two distinct simple stationary Turing crossings** as a common diffusion multiplier \(\tau\) increases. The lower crossing is a **subcritical pitchfork with locally unstable patterned equilibria**; the upper is a **supercritical pitchfork with locally asymptotically stable, strictly positive two-community patterned equilibria**. Both thresholds and the signs of the third-order normal-form coefficients are exact:

\[
\begin{array}{c|c|c|c}
&\tau_*&\lambda'(\tau_*)&c_*\\ \hline
\text{lower}&150/151&151/731220&97752677/6114949120\\
\text{upper}&152/151&-151/739480&-1844319/476770000
\end{array}
\]

Here \(\lambda'(\tau_*)\) is the derivative of the unique critical eigenvalue and \(c_*\) is the cubic coefficient of the symmetry-odd scalar center equation, with amplitude normalized so that the predator half-difference of the two communities is \(a+O(a^3)\). At each threshold the two nonhomogeneous branches exist for \(\tau<\tau_*\), have opposite signed community differences, and satisfy
\[
 a^2=-\frac{\lambda'(\tau_*)}{c_*}(\tau-\tau_*)+o(|\tau-\tau_*|).
\]
All stability statements are local, include perturbations that break within-community equality in the **full 12-dimensional network system**, and hold only sufficiently close to the indicated threshold. In particular, near the upper threshold the stable patterned equilibria have mean prey and predator populations strictly *below* the spatially homogeneous values.

## Assumptions and scope
At each node \(i\) put a prey density \(u_i>0\) and predator density \(v_i>0\), with \(i\) in one of the two size-three parts of \(K_{3,3}\). Both species diffuse on the same unweighted undirected graph with the combinatorial graph Laplacian \(L=A-\operatorname{diag}(\deg)\). Consider the exact smooth ODEs
\[
\begin{aligned}
\dot u_i&=f(u_i,v_i)+d_1\sum_jL_{ij}u_j,\\
\dot v_i&=g(u_i,v_i)+d_2\sum_jL_{ij}v_j,
\end{aligned}
\]
where
\[
 f(u,v)=\frac{u^2(1-u)}{5(u+1/5)}-\frac{uv}{5(1+2u)},\qquad
 g(u,v)=\frac{2uv}{1+2u}-\frac{4v^2}{7(14/25+v)},
\]
and
\[
 d_1=\frac{151}{47880}\tau,\qquad d_2=\frac{151}{1680}\tau,\qquad \tau>0.
\]
These are positive admissible values of the published reaction parameters \(\alpha=A=1/5\), \(\beta=2\), \(\gamma=4/7\), \(e=14/25\), \(\eta=1\). The spatially constant equilibrium is
\[
 z_*=(u_*,v_*)=(1/5,14/25).
\]
No claim is made concerning global basins, large-amplitude patterns, other graph families, or the biological calibration of these rational parameters.

## Proof
**1. Linear crossings.** Direct substitution verifies \(f(z_*)=g(z_*)=0\). The exact reaction Jacobian at this equilibrium is
\[
 J=\begin{pmatrix}3/70&-1/35\\4/7&-1/7\end{pmatrix},\quad
\operatorname{tr}J=-1/10,\quad\det J=1/98.
\]
The eigenvalues of \(-L\) for \(K_{3,3}\) are \(0\) (multiplicity one), \(3\) (multiplicity four), and \(6\) (multiplicity one). For the \(q\)-th graph mode set \(D_0=\operatorname{diag}(151/47880,151/1680)\); its Jacobian is \(M_q(\tau)=J-q\tau D_0\). Elementary exact arithmetic yields
\[
 \det M_q(\tau)=\det D_0\left(q\tau-\frac{900}{151}\right)
 \left(q\tau-\frac{912}{151}\right),
 \qquad \operatorname{tr}M_q(\tau)=-\frac1{10}-q\tau\operatorname{tr}D_0<0.
\]
Thus near \(\tau_-=150/151\) and \(\tau_+=152/151\), only the \(q=6\) mode has a zero eigenvalue, which is simple; all other eigenvalues have strictly negative real parts. In particular the \(q=3\) mode is strictly stable there. Between these two thresholds the homogeneous equilibrium has a positive eigenvalue, while it is stable immediately outside the interval. The critical graph eigenvector is constant within each part and has opposite signs in the two parts.

**2. Symmetric reduction.** The subspace in which all three nodes of each part have identical densities is invariant. Denote its two \(\mathbb R^2\) state vectors by \(z_A,z_B\), and write \(z=(z_A+z_B)/2\), \(h=(z_A-z_B)/2\), \(F=(f,g)^\mathsf T\). Its exact dynamics are
\[
 \dot z=\tfrac12(F(z+h)+F(z-h)),\qquad
 \dot h=\tfrac12(F(z+h)-F(z-h))-6\tau D_0h.
\]
Interchanging the two parts sends \(h\) to \(-h\) and fixes \(z\). Consequently the reduced center equation is odd in its scalar amplitude.

**3. Third-order coefficient.** Let \(B=D^2F(z_*)\), \(C=D^3F(z_*)\), interpreted as multilinear maps. At either threshold choose right and left zero eigenvectors \(r,\ell\), normalized so that the predator component of \(r\) and the second component of \(\ell\) both equal one. Along the small center branch write
\[
 z=z_*+m a^2+O(a^4),\qquad h=a r+O(a^3),\qquad
 m=-\tfrac12J^{-1}B(r,r).
\]
The cubic coefficient and eigenvalue derivative are therefore
\[
 c=\frac{\ell^\mathsf T[\frac16C(r,r,r)+B(r,m)]}{\ell^\mathsf T r},\qquad
 \lambda'=\frac{\ell^\mathsf T(-6D_0)r}{\ell^\mathsf T r}.
\]
Substitution into the *original rational reaction functions*, not merely their Jacobian, yields the exact certificates
\[
\begin{array}{c|c|c|c}
& r &\ell&m\\ \hline
\tau_- &(19/16,1)&(-95/4,1)&(-15849/17920,-17949/4480)\\
\tau_+ &(6/5,1)&(-24,1)&(-1499/1750,-13917/3500)
\end{array}
\]
and the two signed pairs \((\lambda',c)\) in the Finding. They can be checked both by symbolic derivative tensors and by directly expanding \(F(z_*+a r+a^2m)-F(z_*-a r+a^2m)\) to order three, as in the accompanying `verify.py`.

**4. Branch existence, ecological positivity, and stability.** The smooth \(\mathbb Z_2\)-equivariant center-manifold and implicit-function theorems, together with \(\lambda'\ne0\), \(c\ne0\), give the odd scalar normal form
\[
\dot a=\lambda'(\tau_*)(\tau-\tau_*)a+c_*a^3+
 O((\tau-\tau_*)^2|a|+|\tau-\tau_*||a|^3+|a|^5).
\]
The nontrivial equilibrium branches obey the stated square-root law and occur for \(\tau<\tau_*\) at each crossing. At the lower crossing \(\lambda'>0,c>0\); linearization about either branch gives the positive radial eigenvalue \(-2\lambda'(\tau_-)(\tau-\tau_-)+o(|\tau-\tau_-|)>0\). At the upper crossing \(\lambda'<0,c<0\); this eigenvalue is negative for \(\tau<\tau_+\). Every complementary mode is strictly stable at each crossing, and remains stable on these sufficiently small branches by continuity, proving full-network instability at the lower crossing and full-network asymptotic stability at the upper one. Because \(u_*,v_*>0\), all sufficiently small branches are positive and biological.

Finally, at the upper branch the community-average profile is
\[
 \overline u=\frac15-\frac{1499}{1750}a^2+O(a^4),\qquad
 \overline v=\frac{14}{25}-\frac{13917}{3500}a^2+O(a^4),
\]
so *both* means are strictly below their homogeneous equilibrium values for nonzero sufficiently small \(a\).

## Verification
Run `python verify.py` with `sympy` installed. It independently reconstructs the rational equilibrium, exact Jacobian, characteristic-polynomial factorization and entire \(K_{3,3}\) graph spectrum, and verifies the two eigenvector, quadratic-mean and cubic normal-form certificates using two algebraically different coefficient methods. It also checks strict stability of noncritical graph modes. Exact finite computations validate the stated coefficients, while the existence and stability of entire local branches follow from the analytic bifurcation argument above, not from numerical continuation.

## Relationship to prior work
Ye and Zhou (arXiv:2306.11818, first public version June 20, 2023) introduce and analyze this reaction–network model, especially the linear dispersion criterion and Turing instabilities on random networks. Shi, Zhou and Ye (2023) extend the model to multiplex networks; their accessible full manuscript gives the general linear mode condition and numerical spatial patterns. Those general *linear* criteria already imply the two **linear crossing locations** once the graph spectrum is supplied; those locations are not claimed as independently novel. The model-specific two opposite **nonlinear cubic signs**, their patterned-branch directions, full-network stability classification and mean-density shifts are not consequences of the linear mode criterion. Classical equivariant pitchfork theory supplies the method, not these reaction-specific exact signed coefficients. A source-specific matching nonlinear normal form was not identified in the inspected material, but inaccessible or unindexed equivalent work remains a possibility.

## Limitations
This is a local analytical result for one six-patch graph and explicit positive parameters; in particular no coexistence basin, global pattern persistence, experiment, ecological field prediction, or nonlinear behavior far from the crossings is proved. The available HTML of Ye–Zhou's initiating article supplied its reaction equations and section structure but did not permit a complete page-by-page read of all later sections; the related Shi–Zhou–Ye preprint was read through its mathematical and experimental sections. Novelty is therefore conditional on these documented access limits and is not an independent priority certification.

## References
1. Yong Ye and Jiaying Zhou, *Pattern formation in a predator-prey model with Allee effect and hyperbolic mortality on networked and non-networked environments*, arXiv:2306.11818v1 (June 20, 2023), https://arxiv.org/abs/2306.11818 .
2. Lei Shi, Jiaying Zhou and Yong Ye, *Pattern Formation in a Predator–Prey Model with Allee Effect and Hyperbolic Mortality on Multiplex Networks*, preprint posted June 27, 2023, https://www.preprints.org/manuscript/202306.1868 ; *Mathematics* 11 (2023), 3339, https://doi.org/10.3390/math11153339 .
3. H. G. Othmer and L. E. Scriven, *Instability and dynamic pattern in cellular networks*, *Journal of Theoretical Biology* 32 (1971), 507–537, https://doi.org/10.1016/0022-5193(71)90154-8 .
4. Thomas E. Woolley, *Boundary conditions cause different generic bifurcation structures in Turing systems*, *Bulletin of Mathematical Biology* 84 (2022), 101, https://doi.org/10.1007/s11538-022-01055-x .
