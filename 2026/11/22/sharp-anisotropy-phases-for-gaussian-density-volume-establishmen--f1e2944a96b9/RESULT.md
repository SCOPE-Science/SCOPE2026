# Sharp anisotropy phases for Gaussian density–volume establishment screens

## Finding
Fix an integer \(d\ge2\), a dispersion second-moment budget \(\tau>0\), a finite anisotropy ceiling \(K\ge1\), a local density cutoff \(\alpha>0\), and a required occupied volume \(V>0\). A point introduction of \(N>0\) individuals disperses to a spatial density \(n_{N,\Sigma}(x)=N(2\pi)^{-d/2}(\det\Sigma)^{-1/2}\exp[-x^{\mathsf T}\Sigma^{-1}x/2]\) on \(\mathbb R^d\). The covariance \(\Sigma\) ranges over real symmetric positive-definite matrices satisfying \(\operatorname{tr}\Sigma=\tau\) and \(\lambda_{\max}(\Sigma)/\lambda_{\min}(\Sigma)\le K\). The **screening criterion** is that the Lebesgue volume of \(\{x:n_{N,\Sigma}(x)\ge\alpha\}\) is at least \(V\). This criterion is a static density-and-extent screen, **not** a theorem of long-term ecological persistence.

Let \(v_d=\pi^{d/2}/\Gamma(1+d/2)\), \(D=(\det\Sigma)^{1/2}\), and \(D_+=(\tau/d)^{d/2}\). For \(K=1\) set \(D_-=D_+\). For \(K>1\), define
\[
D_-=\min_{1\le k\le d-1}\frac{\tau^{d/2}K^{k/2}}{[d+k(K-1)]^{d/2}},\qquad
D_0=\frac{V}{v_d d^{d/2}},\qquad
D_*=\max\{D_-,\min\{D_0,D_+\}\}.
\]
Then the exact minimum founder number (treated continuously; round upward for integer founders) meeting the screen over all admissible covariances is
\[
N_{\min}=\alpha(2\pi)^{d/2}D_*\exp\!\left[\frac12\left(\frac{V}{v_dD_*}\right)^{2/d}\right]. \tag{1}
\]
**Every** optimal covariance has exactly \(\det\Sigma=D_*^2\), with the specified trace and anisotropy bound; there are no other optimizers. Thus for \(K>1\) there are three sharp volume regimes: maximally determinant-reducing dispersion when \(V\le v_dd^{d/2}D_-\), an intermediate determinant-matched regime when \(v_dd^{d/2}D_-<V<v_d\tau^{d/2}\), and isotropic dispersion when \(V\ge v_d\tau^{d/2}\). In the intermediate regime (1) simplifies to the exact linear law
\[
N_{\min}=\alpha V\,\frac{(2\pi e/d)^{d/2}}{v_d}.
\]
At the lower regime, the minimizing covariance spectra have exactly \(k\) eigenvalues \(K\tau/[d+k(K-1)]\) and \(d-k\) eigenvalues \(\tau/[d+k(K-1)]\), where \(k\) minimizes the finite list defining \(D_-\). The minimizing integers can be located by comparing the floor and ceiling of \(k_0=d/\log K-d/(K-1)\), clipped to \(1,\ldots,d-1\), with any exact ties retained. The large-volume optimum is uniquely \(\Sigma=(\tau/d)I_d\). For \(K=1\), isotropy is mandatory at all volumes.

## Assumptions and scope
All parameters and quantifiers are as given above. The Gaussian kernel is centered and untruncated on the whole \(d\)-dimensional Euclidean space; the total expected number of dispersers is \(N\). The fixed trace is the exact mean squared dispersal displacement, and the finite spectral condition-number cap controls admissible anisotropy. The indicator \(n_{N,\Sigma}(x)\ge\alpha\) defines a *local density screen*, and the volume criterion defines an additional, independently imposed *spatial extent screen*. Real population viability may depend on local growth, patch diameter, perimeter-to-area ratio, stochasticity, habitat boundaries, and shape-dependent critical nuclei, none of which are decided here.

The result concerns the continuous threshold \(N_{\min}\). For discrete releases, the least integer is \(\lceil N_{\min}\rceil\) provided unit density is consistently interpreted. All equalities at either regime boundary are included. For \(K>1\) the determinant minimizer may have more than one optimal high-eigenvalue multiplicity at isolated parameter values. The formula identifies all of them without claiming unique orientation.

## Proof
1. **Exact threshold footprint.** Put \(D=\sqrt{\det\Sigma}\). If \(N\le\alpha(2\pi)^{d/2}D\), the nonempty-superlevel volume is zero. Otherwise the set \(\{n_{N,\Sigma}\ge\alpha\}\) is the ellipsoid \(x^{\mathsf T}\Sigma^{-1}x\le2\log[N/(\alpha(2\pi)^{d/2}D)]\). The coordinate change \(x=\Sigma^{1/2}y\) shows its volume is \(v_dD\{2\log[N/(\alpha(2\pi)^{d/2}D)]\}^{d/2}\). Thus volume at least \(V>0\) is equivalent to
\[
N\ge F(D):=\alpha(2\pi)^{d/2}D\exp\left[\frac12(V/(v_dD))^{2/d}\right]. \tag{2}
\]
2. **Exact feasible determinant interval.** By AM–GM on the \(d\) positive eigenvalues summing to \(\tau\), the largest determinant square root is \(D_+=(\tau/d)^{d/2}\), uniquely at isotropy. For \(K>1\) minimize \(\log\det\Sigma=\sum_i\log\lambda_i\) over the convex trace polytope \(\lambda_i>0\), \(\sum_i\lambda_i=\tau\), and \(\lambda_i\le K\lambda_j\) for all \(i,j\). This polytope is compact and strictly positive. Strict concavity puts every minimum at a vertex. A vertex must attain the ratio cap and cannot have any intermediate eigenvalue strictly between its minimum and maximum: an intermediate value participates in no tight ratio constraint, leaving a nonzero trace-preserving feasible perturbation. Conversely, every spectrum with \(k\in\{1,\ldots,d-1\}\) eigenvalues at \(K a\) and the rest at \(a\), with \(a=\tau/[d+k(K-1)]\), is such a vertex. This gives the finite minimum \(D_-\) stated above. Since the feasible covariance class is convex, the path from a determinant minimizer to the isotropic matrix remains admissible, and its continuous determinant traverses every value of \([D_-,D_+]\). Hence that entire interval, and only it, is feasible.
3. **Scalar minimization.** Differentiating (2),
\[
\frac{d\log F(D)}{dD}=\frac1D\left[1-\frac1d\left(\frac{V}{v_dD}\right)^{2/d}\right].
\]
This derivative is negative for \(D<D_0=V/(v_dd^{d/2})\) and positive for \(D>D_0\); consequently the unique optimal feasible determinant is \(D_*\), the projection of \(D_0\) onto \([D_-,D_+]\). This proves (1), the equality cases, and the three regimes. At interior \(D_0\), one has \((V/(v_dD_0))^{2/d}=d\), giving the linear expression. At \(D_+\) AM–GM forces the sole isotropic covariance.
4. **Finding the minimum spectrum.** For \(K>1\), the logarithm of the \(k\)-th vertex determinant, up to a constant, is \(g(k)=k\log K-d\log[d+k(K-1)]\). On real \(k\), \(g''(k)=d(K-1)^2/[d+k(K-1)]^2>0\); the unique real minimum is at \(k_0=d/\log K-d/(K-1)\). Therefore comparing the adjacent integers (clipped to the permissible range), including a possible tie, locates exactly the minimizers. Their orientations are arbitrary orthogonal conjugates. This finishes the complete classification.

## Verification
Run \(\texttt{python verify_gaussian_footprint.py}\) with NumPy and SciPy. Its deterministic checks compare the exact determinant bounds with thousands of admissible random spectra, the analytic minimum with an independent bounded scalar numerical optimizer, and the volume inversion with the exact ellipsoid formula for dimensions \(2\) through \(9\). These tests are diagnostics, not the proof. The supplied checker passed 24,692 assertions during the reviewed execution.

For example, in two dimensions with \(\tau=2\), \(K=9\), \(\alpha=1\), and \(V=\pi\), the optimal covariance eigenvalues are \((0.2,1.8)\), giving \(D_*=0.6\). Formula (1) gives \(N_{\min}=8.674474745899\ldots\), compared with \(10.359221263698\ldots\) for the isotropic covariance: an exact-model reduction of about \(16.263\%\). The finite-cap threshold volumes here are \(1.2\pi\) and \(2\pi\).

## Relationship to prior work
Vercken, Kramer, Tobin and Drake (2010) provide empirical support for separate density and critical-area effects in spatial populations with strong Allee effects. Soboleva, Shorten, Pleasants and Rae (2003) study nonradial critical nuclei and reaction–diffusion gene invasion; this is a stronger *dynamical* setting but does not state the static trace-and-condition-number-constrained Gaussian superlevel-volume extremum. Goodsman and Lewis (2016) analyze minimum founding populations for an isotropic Gaussian dispersal kernel coupled to explicit nonlinear reproduction; their persistence threshold differs fundamentally from the **screening threshold** optimized here. Those models and classical determinant/ellipsoid facts supply context and known ingredients, not an equivalence to the complete covariance phase diagram (1). No novelty claim is made for Gaussian ellipsoid volume, the AM–GM inequality, or the one-variable derivative rule in isolation.

## Limitations
The area-based screen is a deliberately limited necessary/heuristic metric, not sufficient for invasion, establishment, population growth, or any environmental intervention. In particular, a very elongated superthreshold ellipsoid may fail to contain the compact critical nucleus required by a reaction–diffusion Allee model even when its volume exceeds \(V\). The positive mass is an idealized expected count; integer rounding does not alter the covariance optimization below a count-rounding tie, but multiple covariances may then meet the same rounded count. No field data, anisotropy limit estimates, or external independent review are claimed. The structural theorem uses only continuous Gaussian spatial density and an exogenously specified volume target; it does not model offspring, time, finite habitats, or sampling noise. Historical coverage of equivalent spectral inequalities outside ecological literature cannot be ruled out.

## References
- Vercken, E., Kramer, A. M., Tobin, P. C., and Drake, J. M. (2010). *Critical patch size generated by Allee effect in gypsy moth, Lymantria dispar*. Ecology Letters. First publicly posted 2010-12-08. https://doi.org/10.1111/j.1461-0248.2010.01569.x ; full text https://pmc.ncbi.nlm.nih.gov/articles/PMC3064761/
- Goodsman, D. W., and Lewis, M. A. (2016). *The minimum founding population in dispersing organisms subject to strong Allee effects*. Methods in Ecology and Evolution. First publicly posted 2016-04-05. https://doi.org/10.1111/2041-210X.12573 ; full text https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210X.12573
- Soboleva, T. K., Shorten, P. R., Pleasants, A. B., and Rae, A. L. (2003). *Qualitative theory of the spread of a new gene into a resident population*. Ecological Modelling 163, 33–44. https://doi.org/10.1016/S0304-3800(02)00357-5
