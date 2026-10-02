# Corrected even–odd variance oscillation for the cubic trace in the symmetric two-cut quartic model

## Context

For a regular multi-cut beta ensemble, Borot–Guionnet and Shcherbina describe linear-statistic fluctuations as a continuous Gaussian contribution plus a discrete filling-fraction contribution. The submitted record evaluated this structure at V(x)=x^4/4-2x^2 for Tr M^3, but it used the wrong coefficient for coupling the observable to filling fluctuations. This repair replaces that coefficient by the filling derivative required by the general theorem and updates the numerical limits.

## Definitions

Let mu_N(dM) be proportional to exp(-N Tr(M^4/4-2M^2)) dM on N x N Hermitian matrices and set v_N=Var(Tr M^3). The equilibrium support is [-sqrt(6),-sqrt(2)] union [sqrt(2),sqrt(6)]. Let f_A be the positive-cut period

f_A = int_{sqrt(2)}^{sqrt(6)} dx / sqrt((x^2-2)(6-x^2)).

## Result

The full limit of v_N does not exist. The corrected subsequential limits are

v_even = 20.2871870788979633035608585359060421...,
v_odd  = 75.7128129211020366964391414640939579...,

so the gap is 55.4256258422040733928782829281879157... .

The decomposition is

v_parity = V_G + c0^2 V_parity^d,

with

V_G = 18.1635555366147126586888073471534065...,
c0 = 4*pi/f_A = 15.1709297058687187194852754685943464...,
V_even^d = 0.009226877933258117650758080697734286...,
V_odd^d  = 0.250043363202924644602914874282106697... .

The period ratio and nome remain

t = 1.70916888655748708829376210287026546...,
q = exp(-pi t) = 0.00465640113540246601503593808154580... .

## Why the original coefficient was wrong

The multi-cut fluctuation theorem couples a test statistic to the discrete filling variable through the derivative of its equilibrium expectation with respect to filling fractions. It is not, in general, the difference of the two conditional per-cut means at the unperturbed equilibrium. The original record used the latter quantity, c0≈16.37807472315768, and therefore overstated both variance limits.

For the symmetric genus-one curve y^2=(z^2-2)(z^2-6), the infinitesimal signed change that increases the positive-cut filling and decreases the negative-cut filling is represented by the normalized holomorphic differential (pi/f_A) dz/y. Expanding at infinity,

1/y = z^-2 (1 + 4 z^-2 + O(z^-4)),

so the derivative of the cubic moment is exactly c0=4*pi/f_A. Substitution into the discrete-Gaussian formula gives the corrected pair above.

## Other constants

The equilibrium endpoints a^2=2 and b^2=6, the genus-one zero-A-period kernel constant c≈0.2704444420768390823, and hence V_G=8c+16 are unchanged. The even/odd discrete variances are also unchanged; only the observable/filling coupling was corrected.

## Originality boundary

The Gaussian-plus-discrete-Gaussian structure and its filling-derivative coupling are prior theory. A targeted literature search did not locate this explicit corrected evaluation for the cubic statistic at the reference quartic point. The retained contribution is the numerical/exact-special-function evaluation and the resulting explicit nonconvergence datum, not the general fluctuation theorem.

## Limitations

The general o(1) multi-cut expansion is cited rather than reproved. Numerical constants are high-precision quadrature values rather than formal interval enclosures; the separation between the two limits is large and stable under the displayed precision.

## Reproducibility

Run `python3 artifacts/compute_values.py`. The script evaluates the periods, nome, zero-A-period Gaussian constant, corrected filling derivative c0=4*pi/f_A, discrete theta variances, and both subsequential limits at 80-digit precision.

## References

- G. Borot and A. Guionnet, Asymptotic expansion of beta matrix models in the multi-cut regime, Forum of Mathematics, Sigma 12 (2024), e13, DOI 10.1017/fms.2023.129.
- M. Shcherbina, Fluctuations of linear eigenvalue statistics of beta matrix models in the multi-cut regime, J. Stat. Phys. 151 (2013), arXiv:1205.7062.
