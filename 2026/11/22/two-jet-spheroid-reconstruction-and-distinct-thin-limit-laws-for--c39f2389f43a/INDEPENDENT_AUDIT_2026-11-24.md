# Independent mathematical audit

## correctness

PASS

For the spheroid parametrization in RESULT.md 61–80, the meridional determinant divided by the dot product (one) gives tan(delta) = |r−1/r| sqrt(T(1−T)); the surface integral in x=cos(theta) gives total area 2πZ_r and the claimed density in T=x². Integrating on the two sublevel intervals produces the CDF; t=x² reduces the two primitives to integrals of 2 sqrt(r²+(1−r²)x²). Near zero, the equatorial branch starts at order u (H_r(t)=2r sqrt(t)+O_r(t^(3/2))) and the polar branch at order u² (w_r(1)=1). The endpoint identifies q and the scaled jet yields r=A_r/(2B_r); the informal 'their ratio' on line 86 means the ratio with the factor of 2 in the displayed formula. The r=1 atom is separate. At the upper endpoint, the symmetric integration interval has length sqrt(1−4u²); the odd density term cancels, and the angle change of variable gives 1−4u²=((4+q)/sqrt(q)) epsilon+O_r(epsilon²). For r→∞ dominate w_r/r by t^(−1/2); for r↓0 similarly dominate w_r. Normalization gives density limits (2/π)sqrt((1−t)/t) and 1 in L¹. The scaled complement converges locally uniformly in 0<t<1 to 1/sqrt(t(1−t)), which suffices with L¹ density convergence and no endpoint atoms. The two inverse branches of V=4t(1−t) yield 1/(π sqrt(v(1−v))) and 1/(2 sqrt(1−v)); their survival asymptotics after V↦2/sqrt(V) have the claimed constants and powers. Replay: RESULT.md 61–98 via these changes of variable. The supplied script is a finite recorded diagnostic, inspected but not run; it is not the proof.

## originality

PASS

Passes for the endpoint-calibrated inverse jet and contrasting thin-limit laws, not for the known normal geometry or general computation of surface patches. No inspected distinct source covers that scoped conclusion. This is not a historical priority certification.

## value

PASS

An inversion-symmetric endpoint hides which axis is longer, while the equatorial and polar lower-end orders together recover that information after calibration. The contrasting beta laws predict genuinely different powers for rare angular deficits under opposite extreme-area limits. These are structural results for natural area sampling, not new numerical values of the classical patch formula. No statistical stability or uniformity across the limits is proved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
