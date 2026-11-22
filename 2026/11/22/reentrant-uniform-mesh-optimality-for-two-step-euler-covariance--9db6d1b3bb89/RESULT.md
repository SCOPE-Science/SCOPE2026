# Reentrant uniform-mesh optimality for two-step Euler covariance under multiplicative noise

## Finding
Consider the scalar Itô equation
\[
 dX_t=-\lambda X_t\,dt+\sigma X_t\,dW_t,
\]
with \(\lambda>0\) and \(0<\sigma^2<2\lambda\). Let \(X_0\), independent of the Brownian motion, have zero mean and positive finite variance \(V_0\). For two Euler–Maruyama steps of nonnegative physical lengths adding to \(t_f>0\), set \(T=\lambda t_f\), \(h_i=\lambda\Delta t_i\), and \(d=2-\sigma^2/\lambda\in(0,2)\). The terminal numerical covariance is \(V_0G_d(h_1,h_2)\), with
\[
G_d(h_1,h_2)=(1-dh_1+h_1^2)(1-dh_2+h_2^2).
\]
The globally optimal split on the **closed** mesh simplex \(h_1+h_2=T\), \(h_i\ge0\), is determined exactly by
\[
z_*=\max\bigl\{0,\min\{T^2/4,(2-d^2+dT)/2\}\bigr\},\qquad
\{h_1,h_2\}=\left\{\frac{T-\sqrt{T^2-4z_*}}2,\frac{T+\sqrt{T^2-4z_*}}2\right\}.
\]
Only the order of the two steps is arbitrary. In particular, the regime of **small-noise reentrant equal-step optimality** is sharp:

* If \(0<d\le\sqrt2\), the equal split uniquely minimizes covariance for \(0<T\le T_+\), where \(T_+=d+\sqrt{4-d^2}\). Thereafter exactly two unequal ordered minimizers appear.
* If \(\sqrt2<d<2\), put \(T_c=d-2/d\) and \(T_\pm=d\pm\sqrt{4-d^2}\). Then \(0<T_c<T_-<T_+\). For \(0<T\le T_c\), precisely the collapsed splits \((0,T),(T,0)\) minimize on the closed simplex; for \(T_c<T<T_-\), there are precisely two strictly unequal interior optimizers; for \(T_-\le T\le T_+\), the equal split is the unique optimizer; for \(T>T_+\), two unequal interior optimizers return.

For the open mesh simplex \(h_1,h_2>0\), the collapsed regime has the same infimum but **no minimizer**. For every fixed \(d\in(0,2)\), the ratio of the equal-grid covariance to the optimum satisfies
\[
\frac{G_d(T/2,T/2)}{\min G_d}\sim \frac{T^2}{16(1-d^2/4)}\qquad(T\to\infty).
\]
The critical noise ratio \(\sigma^2/\lambda=2-\sqrt2\) also changes the sign of the small-time *one-step* numerical covariance bias: \((1-dT+T^2)-e^{-dT}=(1-d^2/2)T^2+O(T^3)\).

## Assumptions and scope
The result is for the two-step **standard Euler–Maruyama scheme**, not an exponential propagation method, an optimizer with an explicit mesh-ratio bound, or a general covariance-steering controller. It minimizes the **numerically predicted terminal covariance**, not error against the exact SDE, control energy, or an optimal-control objective. Both time steps see independent Brownian increments, of variances equal to the corresponding physical time lengths. Zero time steps are allowed only to characterize the closed-simplex optimizer/limit. The continuous process is mean-square stable because \(\sigma^2<2\lambda\); its exact terminal covariance is \(V_0e^{-dT}\).

## Proof
A single Euler–Maruyama update of dimensionless length \(h\) multiplies the current state by \(1-h+(\sigma/\sqrt\lambda)\sqrt h\,Z\), where \(Z\) is independent standard normal. Its conditional squared mean is the factor \(f_d(h)=1-dh+h^2\), strictly positive for \(d\in(0,2)\). Centering is preserved, and independence of the increments therefore gives \(\operatorname{Var}(Y_2)/V_0=f_d(h_1)f_d(h_2)\).

Let \(z=h_1h_2\). From \(h_1+h_2=T\) and \(h_1^2+h_2^2=T^2-2z\), direct expansion gives the exact identity
\[
G_d(h_1,h_2)=1-dT+T^2+(d^2-dT-2)z+z^2.
\]
Every \(z\in[0,T^2/4]\) corresponds to a feasible pair, with \(z=T^2/4\) only for the equal split and \(z=0\) only for the two collapsed splits. The objective is a **strictly convex quadratic in \(z\)**. Its unique unconstrained minimizer is \((2-d^2+dT)/2\), so projecting that number onto \([0,T^2/4]\) proves the optimizer formula and uniqueness statements (up to swapping the steps).

For the regime classification, \(z_*\) is at zero exactly when \(T\le d-2/d\), which can occur for positive \(T\) exactly when \(d>\sqrt2\). The equal split is optimal exactly when
\[
\frac{2-d^2+dT}{2}\ge\frac{T^2}{4}
\quad\Longleftrightarrow\quad
(T-d)^2\le4-d^2,
\]
i.e. \(T\in[T_-,T_+]\), intersected with \((0,\infty)\). When \(d\le\sqrt2\), \(T_-\le0\); when \(d>\sqrt2\), both endpoints are positive, and
\[
T_- -T_c=2/d-\sqrt{4-d^2}>0
\]
because \((d^2-2)^2>0\). These strict inequalities exhaust the feasible regimes; at every boundary the stated optimizer remains unique in \(z\). For \(0<T\le T_c\), \(z=0\) is excluded by strictly positive time steps, so the open-simplex infimum is not attained.

For fixed \(0<d<2\) and large \(T\), the unconstrained vertex lies inside the feasible interval and satisfies \(z_*=(dT+2-d^2)/2\). The two roots of \(h^2-Th+z_*=0\) therefore have smaller root \(h_{\rm small}=d/2+O(T^{-1})\) and larger root \(T-d/2+O(T^{-1})\). Hence \(\min G_d=(1-d^2/4)T^2+O(T)\) and \(G_d(T/2,T/2)=T^4/16+O(T^3)\), proving the claimed sharp ratio. Taylor expansion of \(e^{-dT}\) proves the final bias sign.

## Verification
The standalone standard-library file `verify.py` checks the exact polynomial identity and lower bound using rational arithmetic over 5,000 deterministic sampled rational parameter triples, plus 60 grid-versus-global-minimum checks across six noise ratios and multiple horizon regimes. It prints `VERIFY_OK 10060`. These checks support but do not replace the algebraic proof. Reproduction: `python verify.py` in a directory containing the standalone file.

A concrete instance is \(d=7/4\), equivalently \(\sigma^2/\lambda=1/4\), with \(T_c=17/28\), \(T_-=(7-\sqrt{15})/4\), and \(T_+=(7+\sqrt{15})/4\). At \(T=1/2\) the infimum is attained only by collapsed steps; at \(T=1\) the optimizer is equal; at \(T=3\) it is unequal again. The exact continuous covariance remains \(V_0e^{-7T/4}\) regardless of the mesh.

## Relationship to prior work
Pilipovsky (2026) develops a broad adaptive-time-dilation covariance-steering framework for SDEs with multiplicative noise, with a first-order diffusion linearization and a different (integrating-factor-based) discrete update. Its full accessible text does not identify this exact two-step Euler–Maruyama covariance-mesh classification. Hoel, Häppölä and Tempone (2014) develop mean-square-**error** adaptive Euler–Maruyama quadrature; their geometric-Brownian example finds uniform steps optimal for a leading-order *solution-error* objective. That theorem does not imply this covariance-minimization result: the objectives differ, and this result deliberately exposes the mismatch. Related indexed analyses of randomized timesteps and variable-step BDF2 concern different propagators and optimization criteria. The results here are self-contained algebraic facts; historical novelty beyond the inspected literature is not independently certified.

## Limitations
A two-step scalar covariance benchmark cannot predict optimal accuracy or mesh choice in high-dimensional controlled diffusions. In particular, minimizing numerical covariance can be scientifically undesirable because it may prefer a collapsed grid or severely understate true uncertainty. No finite-step error bound against the exact covariance or positive lower-step constraint is claimed.

## References
1. J. Pilipovsky, *Free Final Time Adaptive Mesh Covariance Steering via Sequential Convex Programming*, arXiv:2603.14868 (first public release 2026-03-16), https://arxiv.org/abs/2603.14868 . Accessible full text: https://www.researchgate.net/publication/402482064_Free_Final_Time_Adaptive_Mesh_Covariance_Steering_via_Sequential_Convex_Programming .
2. H. Hoel, J. Häppölä, and R. Tempone, *Construction of a Mean Square Error Adaptive Euler--Maruyama Method with Applications in Multilevel Monte Carlo*, arXiv:1411.5515 (2014), https://arxiv.org/abs/1411.5515 . Accessible full text: https://www.researchgate.net/publication/268525726_Construction_of_a_Mean_Square_Error_Adaptive_Euler--Maruyama_Method_with_Applications_in_Multilevel_Monte_Carlo .
3. W. Fang and M. B. Giles, *Adaptive Euler–Maruyama Method for SDEs with Nonglobally Lipschitz Drift*, Ann. Appl. Probab. 30 (2020), 526–560, https://doi.org/10.1214/19-AAP1507 (general adaptive strong-error and moment guarantees; not this fixed-budget objective).
