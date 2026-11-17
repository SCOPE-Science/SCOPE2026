# Sharp weighted Huber-location star-variation modulus and mass-balance discontinuity

## Finding
Fix \(m\ge2\), positive weights \(w_1,\ldots,w_m\), and \(\delta>0\). Define the Huber loss
\[
\rho_\delta(t)=\begin{cases}t^2/2,&|t|\le\delta,\\ \delta|t|-\delta^2/2,&|t|>\delta.\end{cases}
\]
Let \(c_w(x_1,\ldots,x_m)\) be the arithmetic midpoint of the (possibly degenerate) interval minimizing \(\sum_i w_i\rho_\delta(x_i-c)\). On the star with hub indexed by zero, put \(E_w(x_0,x_1,\ldots,x_m)=(c_w(x_1,\ldots,x_m),x_1,\ldots,x_m)\) and \(V(h)=\sum_{i=1}^m|h_i-h_0|\).

For every nonempty \(I\subseteq\{1,\ldots,m\}\), put \(W_I=\sum_{i\in I}w_i\) and let \(s_i\in\{-1,1\}\) for \(i\notin I\). Define
\[
Q(w)=\max\left\{\frac{w_j}{W_I}:j\in I,\quad \left|\sum_{i\notin I}s_iw_i\right|<W_I\right\}.
\]
The collection is nonempty (take all indices in \(I\)). Then the **sharp, attained**, two-input coefficient is
\[
\sup_{V(x-y)>0}\frac{V(E_wx-E_wy)}{V(x-y)}=1+(m-2)Q(w).
\]
For \(w_i=1\), this is \(m-1\) when \(m\) is odd and \(m/2\) when \(m\) is even. For every even \(m\ge4\), the perturbed weights \((1+\varepsilon,1,\ldots,1)\), with arbitrary \(\varepsilon>0\), give coefficient \(m-1\): hence the operator norm as a function of weights has a genuine discontinuity at equal masses.

## Assumptions and scope
All observations are real, every weight and threshold is strictly positive, and exactly one weighted Huber location estimate replaces the hub. The minimizer-interval midpoint convention is essential on data configurations with a flat objective. The denominator compares differences of inputs, not the variation of either signal individually. Translation invariance lets us measure perturbations relative to the input-hub coordinate. The result applies to all finite \(m\ge2\) and all positive weights without genericity assumptions.

## Proof
Write \(\psi_\delta(t)=\max\{-\delta,\min(t,\delta)\}\). A center is a zero of the nondecreasing continuous score \(g_x(c)=\sum_i w_i\psi_\delta(c-x_i)\). This score has a bounded closed zero interval because the loss is coercive. Its midpoint is a continuous, translation-equivariant, piecewise-affine function of the leaf data: the finitely many break hyperplanes correspond to ordering the breakpoints \(x_i\pm\delta\); the root is affine on each resulting chamber, including chambers with a flat zero interval.

On a full-dimensional chamber with a unique root and a nonempty set \(I\) of strictly unsaturated observations, the outside residuals have fixed signs \(s_i\in\{-1,1\}\). The score condition gives \(\sum_{i\in I}w_i(c-x_i)+\delta\sum_{i\notin I}s_iw_i=0\). The inside inequalities imply \(\big|\sum_{i\notin I}s_iw_i\big|<W_I\). Differentiating yields \(dc=\sum_{j\in I}(w_j/W_I)\,dx_j\). Thus the gradient is a probability vector \(q\), with \(\max q_j\le Q(w)\).

On a full-dimensional chamber whose score is zero throughout a nondegenerate interval, there are no unsaturated observations. Equal positive weight lies on either side. The endpoints of the zero interval are \(x_\ell+\delta\) and \(x_r-\delta\) for one left and one right observation, respectively; the selected center derivative is then \((dx_\ell+dx_r)/2\). This gradient is again a probability vector, with largest entry \(1/2\le Q(w)\): choose \(I=\{\ell,r\}\), retain signs of all other observations, and use the equal-mass balance on both sides to obtain \(\big|\sum_{i\notin I}s_iw_i\big|=|w_\ell-w_r|<w_\ell+w_r\). The case of zero-dimensional transition faces follows by continuity and integration across adjacent chambers.

For an input difference \(h\), let \(d_i=h_i-h_0\). Translation equivariance makes the output-hub difference between two inputs equal to \(\sum_i q_id_i\) infinitesimally. The induced star variation map is \(d\mapsto(d_i-\sum_jq_jd_j)_{i=1}^m\). The sum of absolute entries of its column \(j\) is \((1-q_j)+(m-1)q_j=1+(m-2)q_j\). Hence every chamber derivative has induced \(\ell^1\) norm at most \(1+(m-2)Q(w)\). Integrating the piecewise-affine derivative on any segment proves the global upper bound.

For sharpness choose a maximizing feasible \(I,j,s\), write \(S=\sum_{i\notin I}s_iw_i\), and prescribe leaf values \(x_i=\delta S/W_I\) for \(i\in I\), and \(x_i=-Bs_i\) otherwise with sufficiently large \(B>\delta\). The score at center zero is zero, the inliers are strictly inside the quadratic branch, and outliers are strictly saturated. Perturb only leaf \(j\) by a sufficiently small \(\eta>0\). The center moves by exactly \(q_j\eta\), with \(q_j=w_j/W_I\). The input variation change is \(\eta\); output variation change is \([1+(m-2)q_j]\eta\). This attains the formula with finite distinct inputs.

At equal weights a singleton \(I\) is feasible precisely for odd \(m\), because the complement then has even size and can have zero signed sum. For even \(m\), any feasible \(I\) has size at least two, and \(I\) of size two with balanced outside signs is feasible, so \(Q=1/2\). If \(m\ge4\) is even and one weight becomes \(1+\varepsilon\), taking this index as the sole inlier and assigning signs to the odd number of unit-weight outliers with signed sum \(1\) gives strict feasibility \(1<1+\varepsilon\). Then \(Q=1\), its maximum possible value.

## Verification
Run `python3 check_weighted_huber.py` using Python's standard library. The checker constructs exact rational minimizing-center intervals and independently enumerates feasible inlier/sign states; it verifies attained sharp coefficients, exact rational two-input inequalities for numerous weighted instances, the equal-weight parity law, and the arbitrarily small positive mass-perturbation branch. The finite checks are corroboration, not a replacement for the chamber proof covering every dimension, real input and positive weight.

## Relationship to prior work
Huber's 1964 work introduced robust location M-estimation; Hampel, Hennig and Ronchetti analyze smoothing of Huber location M-estimators, including score and smoothing properties, rather than graph edge-variation sensitivity. Li–Swetits investigate linear \(\ell^1\) estimation and Huber parameter perturbation. These do not supply the exact weighted star-variation modulus, signed subset-feasibility formula, or discontinuous mass-balance transition. The derivative score and piecewise linearity are standard; the claimed contribution is their sharp operator-norm consequence for star variation.

## Limitations
The result is deterministic for a star with one estimated hub, not statistical risk, asymptotic efficiency or robustness against contamination. It does not characterize general graph extensions, iterated Huber filters, or regularized Huber estimators with hub data also penalized. Priority is provisional because some historically relevant full texts were not available for inspection.

## References
1. P. J. Huber, *Robust Estimation of a Location Parameter*, Annals of Mathematical Statistics 35 (1964), 73–101. https://doi.org/10.1214/aoms/1177703732
2. F. R. Hampel, C. Hennig, and E. Ronchetti, *A smoothing principle for the Huber and other location M-estimators*, Computational Statistics & Data Analysis 55 (2011), 324–337. https://doi.org/10.1016/j.csda.2010.05.001
3. W. Li and J. J. Swetits, *The Linear l1 Estimator and the Huber M-Estimator*, SIAM Journal on Optimization 8 (1998). https://doi.org/10.1137/S1052623495293160
