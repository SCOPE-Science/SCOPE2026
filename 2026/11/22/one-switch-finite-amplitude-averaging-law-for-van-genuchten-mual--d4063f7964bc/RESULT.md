# One-switch finite-amplitude averaging law for van Genuchten–Mualem soil conductivity

## Finding
For each \(0<m<1\) and real \(\ell>-2/m\), consider the normalized van Genuchten–Mualem conductivity
\[
K_{m,\ell}(s)=s^{\ell}\left[1-\left(1-s^{1/m}\right)^m\right]^2,\qquad 0<s<1,
\]
continued by \(K(0)=0\), \(K(1)=1\). Write \(r=\ell+2/m>0\). For a saturation half-contrast \(0<h<1/2\) and feasible mean \(h\leq a\leq1-h\), define the conductivity averaging difference
\[
J_h(a)=\frac{K(a-h)+K(a+h)}2-K(a).
\]
If \(r\geq1\), then \(J_h(a)>0\) for every feasible \(h,a\). If \(0<r<1\), define the two *endpoint tests*
\[
L_h=\frac{K(2h)-2K(h)}2,\qquad U_h=\frac{1-2K(1-h)+K(1-2h)}2.
\]
Exactly one of the following mutually exclusive possibilities holds for every fixed \(h\):

* \(L_h<0<U_h\): a unique \(a_h\in(h,1-h)\) satisfies \(J_h(a_h)=0\); the difference is negative below and positive above \(a_h\).
* \(L_h\geq0\): the difference is strictly positive throughout the open feasible interval.
* \(U_h\leq0\): the difference is strictly negative throughout the open feasible interval.

At the endpoints themselves, the signs are precisely \(L_h\) and \(U_h\); equality in an endpoint test gives an endpoint zero, not an additional interior zero. Hence a nonzero *negative-to-positive* finite-amplitude reversal is possible, but a positive-to-negative reversal or two reversals are impossible. In particular, the pair \(L_h>0, U_h<0\) cannot occur.

Moreover, in the regime \(0<r<1\), the conductivity has exactly one inflection saturation \(s_*\in(0,1)\), strictly concave below it and strictly convex above it. For all sufficiently small \(h>0\), the interior averaging crossover \(a_h\) exists and \(a_h\to s_*\) as \(h\downarrow0\).

## Assumptions and scope
The variable \(s\) denotes dimensionless effective liquid saturation, not absolute water content; \(K\) is normalized to saturated conductivity. The two subregions have equal weight and saturations \(a-h\), \(a+h\); no local water redistribution or effective-medium transport is asserted. The exponent \(\ell\) is unrestricted except for \(\ell>-2/m\), which ensures a finite dry-limit conductivity of zero. The model is mathematical and does not imply that all parameter combinations represent physically admissible soils.

## Proof
**1. Strict convexity versus one inflection.** Set \(z=s^{1/m}\). Since \(0<m<1\), the binomial expansion has strictly positive coefficients \(c_j=(-1)^{j+1}\binom m j>0\) for all positive integers \(j\), and
\[
1-(1-z)^m=\sum_{j=1}^{\infty}c_jz^j.
\]
Squaring, and collecting like powers, gives
\[
K(s)=s^r\sum_{j=0}^{\infty}d_js^{j/m},\quad d_j=\sum_{k=1}^{j+1}c_kc_{j+2-k}>0,\quad d_0=m^2.
\]
On each compact subinterval of \((0,1)\), the series and its derivatives converge absolutely, whence
\[
s^{2-r}K''(s)=d_0r(r-1)+\sum_{j=1}^{\infty}d_j(r+j/m)(r+j/m-1)s^{j/m}=:H(s).
\]
All terms with \(j\geq1\) are strictly positive and strictly increasing in \(s\), because \(1/m>1\) and \(r>0\). If \(r\geq1\), \(H(s)>0\) everywhere. If \(0<r<1\), \(H(0+) =d_0r(r-1)<0\), and \(H\) is strictly increasing. To see that it becomes positive, let \(u=1-s^{1/m}\). In \(K=s^\ell(1-u^m)^2\), the second derivative of \(-2u^m\) has a positive leading term proportional to \(u^{m-2}\), which dominates all other differentiated terms as \(s\uparrow1\), because \(0<m<1\). Thus \(K''(s)\to+\infty\), so \(H\) has exactly one zero \(s_*\), with the indicated signs.

**2. An order-preserving averaging kernel.** For \(a\in(h,1-h)\), Taylor's integral formula, valid also at the endpoints by integrable improper limits, gives
\[
2J_h(a)=\int_0^1(h-|a-s|)_+K''(s)\,ds,
\qquad (u)_+=\max(0,u).
\]
The triangular kernel \(T_h(v)=(h-|v|)_+\) is strictly log-concave wherever positive. Therefore its translates are strictly totally positive of order two on their common positive supports: whenever \(a_1<a_2\) and \(s_1<s_2\),
\[
T_h(a_1-s_1)T_h(a_2-s_2)\geq T_h(a_1-s_2)T_h(a_2-s_1),
\]
with strict inequality if the four factors are positive and the two arguments are distinct. This also follows directly by differentiating \(\log(h-|v|)\) on each side of zero and checking its decreasing slope across zero. Zeros outside the support follow by continuity.

Suppose \(0<r<1\). Split the integral at its unique curvature sign change \(s_*\), into positive mass \(P(a)=\int_{s_*}^{1}T_h(a-s)K''(s)\,ds\) and negative mass \(N(a)=-\int_{0}^{s_*}T_h(a-s)K''(s)\,ds\). Both are nonnegative. For \(a_1<a_2\) with both masses nonzero, multiplying the strict two-by-two kernel inequality by the positive product of the two curvature weights and integrating yields
\[
P(a_2)N(a_1)>P(a_1)N(a_2).
\]
At zeros of \(J_h\), both masses must be positive, so two distinct zeros would give the contradiction \(0>0\). The same cross-product comparison shows that after a zero the difference is positive, and before it negative. When a kernel support lies wholly on one side of \(s_*\), its sign is clear. This proves the one-switch law including the possibility that a switch lies outside the feasible mean interval.

**3. Exhaustive endpoint test and small-contrast limit.** Direct substitution gives \(J_h(h)=L_h\) and \(J_h(1-h)=U_h\). Continuity plus the one-switch direction produces exactly the three alternatives stated, including endpoint equality. For sufficiently small \(h\), the two endpoints lie entirely in the respective negative and positive curvature regions (choose \(2h<\min\{s_*,1-s_*\}\)); hence \(L_h<0<U_h\). On any compact subinterval of \((0,1)\), Taylor expansion gives \(J_h(a)/h^2\to K''(a)/2\) uniformly. Any accumulation point of the unique roots must therefore be \(s_*\), proving \(a_h\to s_*\).

## Verification
The companion standalone `checker.py` evaluates the function at high precision, checks the predicted sign ordering over a broad parameter grid, independently evaluates the absolutely convergent coefficient expansion at selected points, and checks an illustrative crossover. It reports 9,768 successful numerical assertions; these sampled assertions are diagnostics, not substitutes for the infinite-parameter proof.

For \(m=1/2\) and \(\ell=-7/2\), we have \(r=1/2\) and
\[
K(s)=\frac{\sqrt{s}}{\left(1+\sqrt{1-s^2}\right)^2}.
\]
At \(h=1/10\), the endpoint differences are approximately \(-0.0224062230\) and \(0.2145644773\), respectively, and the unique interior reversal is \(a_h\approx0.3209402594744\). At the larger contrast \(h=2/5\), the left endpoint difference is approximately \(0.00250377766>0\), hence the model predicts a positive averaging difference for *every* feasible mean \(a\in[2/5,3/5]\). These numbers illustrate distinct branches of the exact endpoint test.

## Relationship to prior work
Van Genuchten (1980) introduced the underlying closed-form conductivity model; that equation is not claimed as new. Fuentes, Haverkamp and Parlange (1992), and de Jong van Lier, Dourado Neto and Metselaar (2009), studied physical admissibility and the established parameter constraint ensuring nonnegative conductivity curvature, including the boundary \(\ell=1-2/m\); that parameter threshold is **not** claimed as new. Brown, Johnstone and Macgibbon (1981), and later applications of total positivity, supply the general sign-variation principle; it is likewise not claimed as new. The finding here is the joint, sharp finite-amplitude saturation-pair averaging result for this specific conductivity law, including a proof of exactly one possible reversal and the two endpoint tests. Zhu and Mohanty (2002) studied spatial averaging of van Genuchten *parameters* and effective flow numerically; their studied quantity is different from the present fixed-parameter arithmetic mean of local conductivities.

## Limitations
Historical priority remains provisional: the full text of Fuentes et al. (1992), a particularly relevant early study, was not completely accessible for direct theorem-by-theorem comparison; an equivalent two-point mixing law in older constitutive or total-positivity literature cannot be excluded. The assertion concerns a constitutive arithmetic average at fixed local model parameters, **not** generally the effective conductivity of a heterogeneous soil or a full Richards-equation solution. The asymptotic and all-parameter statements are analytically proved but not externally audited. Values of strongly negative \(\ell\) may be hydraulically implausible in some soils.

## References
- van Genuchten, M. Th. (1980), *A Closed-form Equation for Predicting the Hydraulic Conductivity of Unsaturated Soils*, Soil Science Society of America Journal 44, 892–898. DOI: 10.2136/sssaj1980.03615995004400050002x.
- Fuentes, C., Haverkamp, R., Parlange, J.-Y. (1992), *Parameter constraints on closed-form soilwater relationships*, Journal of Hydrology 134, 117–142. DOI: 10.1016/0022-1694(92)90032-Q.
- de Jong van Lier, Q., Dourado Neto, D., Metselaar, K. (2009), *Modeling of transpiration reduction in van Genuchten–Mualem type soils*, Water Resources Research 45. DOI: 10.1029/2008WR006938.
- Zhu, J., Mohanty, B. P. (2002), *Spatial Averaging of van Genuchten Hydraulic Parameters for Steady-State Flow in Heterogeneous Soils: A Numerical Study*, Vadose Zone Journal 1, 261–272. DOI: 10.2136/vzj2002.2610.
- Brown, L. D., Johnstone, I. M., Macgibbon, K. B. (1981), *Variation Diminishing Transformations: A Direct Approach to Total Positivity and its Statistical Applications*, JASA 76, 824–832. DOI: 10.1080/01621459.1981.10477730.
- *Applications of total positivity theory to 1D prescribed curvature problems* (2015), J. Math. Anal. Appl. DOI: 10.1016/j.jmaa.2015.03.002.
