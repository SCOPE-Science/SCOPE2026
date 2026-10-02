# E_{6,3}(|x| on [-1,1]) <= 0.02 via explicit certified even rational approximant

## Context

The uniform rational approximation of f(x)=|x| on [-1,1] is a classical benchmark stemming from Newman (1964), with sharp diagonal asymptotics by Stahl and high-precision diagonal tables by Varga-Ruttan-Carpenter. Rectangular (non-diagonal) finite thresholds are separately motivated by modern barycentric Remez implementations that handle m != n. The admitted target asks for a decision on E_{6,3}(f) <= 0.02, where E_{6,3} is the minimax error over real rationals p/q with deg p <= 6, deg q <= 3 and q nonzero on [-1,1].

## Definitions

Let f(x)=|x| on [-1,1]. Let R_{6,3} be real rationals p/q with deg p <= 6, deg q <= 3, q != 0 on [-1,1]. Define E_{6,3}(f)=inf_{r in R_{6,3}} max_{[-1,1]}|f-r|. Let t=x^2, P(t)=a0+a2 t+a4 t^2+a6 t^3 with a0=0.016343, a2=8.675825, a4=15.597868, a6=-1.619264, Q(t)=1+b2 t with b2=21.310264, and R(x)=P(x^2)/Q(x^2).

## Result

R is of rectangular type (6,3): numerator degree 6 in x (even powers only), denominator 1+b2 x^2 of degree 2 <= 3, with Q >= 1 on [-1,1] hence admissible. Certified uniform error: max_{[-1,1]}||x|-R(x)| <= 0.016533 < 0.02. Hence E_{6,3}(|x|) <= 0.02 is TRUE, resolving the target affirmatively via its exhibit-plus-certificate branch.

## Proof / evidence

By evenness it suffices to bound [0,1]. With S(t)=(P'(t)Q(t)-P(t)Q'(t))/Q(t)^2, R'(x)=2x S(x^2). Let U(t)=P'Q-PQ'=U0+U1 t+U2 t^2+U3 t^3 with U0=a2-b2 a0, U1=2 a4, U2=3 a6+a4 b2, U3=2 a6 b2 (exact decimals as rationals). Since U''(t)=2U2+6U3 t is decreasing with min 2U2+6U3 ~ 240.99 > 0, U' increases from U1 > 0, so U increases and U(0)=U0 > 0 gives U > 0 on [0,1]. For [l,r] subset [0,1], sup|R'| <= 2r U(r^2)/(1+b2 l^2)^2 =: M_k, so E(x)=x-R(x) has Lipschitz constant L_k=1+M_k. Subdividing [0,1] into M=8000 uniform intervals with midpoints m_k, sup_{[l_k,r_k]}|E| <= |E(m_k)|+L_k/(2M)=:B_k, all evaluated in exact Fraction arithmetic. The computation yields max B_k = 0.01653276... <= 1/50, worst interval k=583 (x ~ 0.0729), exact fraction 382674935548485862282153958194276058610491236008249093/23146461393541367776078750330936500490264576000000000000. Even extension preserves the bound on [-1,1].

## Limitations

Computer-assisted certificate with 8000 exact rational evaluations; sound but requires running the script. Approximant is machine-optimized with no closed-form derivation. No lower bound or optimality claimed.

## Reproducibility

Run `python3 output/artifacts/verify_certificate.py` (integers/Fractions only, no floats); asserts sup <= 1/50 and prints PASS. Coefficients and U data in `output/artifacts/certificate.json`. Independent re-run confirmed PASS with worst interval 583.

## References

H. Stahl, Best uniform rational approximation of x^alpha on [0,1], arXiv:math/9301217; R. S. Varga, A. Ruttan, A. J. Carpenter, Numerical results on best uniform rational approximation of |x| on [-1,+1], Math USSR-Sb 74 (1993) 271-290, doi:10.1070/sm1993v074n02abeh003347; S.-I. Filip et al., Rational minimax approximation via adaptive barycentric representations, arXiv:1705.10132; Chebfun RationalAbsx minimax example.
