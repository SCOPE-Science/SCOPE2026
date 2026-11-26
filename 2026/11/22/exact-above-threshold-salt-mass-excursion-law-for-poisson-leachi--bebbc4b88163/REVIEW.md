# Independent mathematical audit

## correctness

PASS

For x>=h, conditioning on the first event gives f(x)=integral_0^infinity lambda exp[-(lambda+s)t] I(x+ct) dt, where I(x)=(h/x)^a+a*x^(-a)*integral_h^x y^(a-1) f(y) dy. Continuity of I justifies differentiation and the right boundary relation c f'(h+)=(lambda+s)f(h)-lambda, not absorption at h. Eliminating I gives the stated Kummer equation. For finite T the process up to T is bounded below by x times the positive product of all factors through T, so f decays at infinity and selects U over M. The U derivative normalizes the transform; a residual satisfying Q'=-aQ/x with Q(h+)=0 verifies recovery of the first-order equation. In the positive integral for U(A,a,z), the integral diverges as 1/A at the lower endpoint as s approaches zero, canceled by 1/Gamma(A), while U(A+1,a+1,z) remains finite. Thus f(h) tends to one and crossing is almost sure. The small-s slope also gives mean 1/lambda+(a/lambda)U(1,a+1,lambda*h/c), equivalent to the stated mean by integration by parts. On the same path the excursion cannot end before the first Poisson event E; conditional survival at E is 1-(1+cE/h)^(-a), giving the TV upper bound and asymptotic by coupling and domination by acE/h. Independent U-integral quadrature at the supplied sample gave 0.4223846030645711 (within 4.1e-11 of the recorded value); this is finite corroboration. The frozen simulation script was inspected, not run.

## originality

PASS

The model, stationary law, and mean are not credited as new. The supported distinct claim is the exact downward first-passage transform for the specified continuous multiplier family, together with the quantitative high-threshold first-event comparison. Same-model upward hitting and different-mark downward exits are substantial precedents, but the results inspected do not cover the stated law.

## value

PASS

Threshold-exceedance duration is not measured by the stationary gamma tail or by the mean duration alone. This exact transform determines the law and is available for computing moments or inverting to probabilities. The coupled first-event estimate quantifies when a simpler exponential waiting-time model is accurate, at a specified finite threshold. This is a benchmark for salt mass in the stipulated process, not a calibrated prediction of salinity exposure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
