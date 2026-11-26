# Independent mathematical audit

## correctness

PASS

Reviewed RESULT.md:3–65, VERIFICATION.md and checker.py. With immediate independent fresh rotations, the mean time is I=integral_0^T S and the reward is T^p S(T) plus the salvage-weighted integral against the event density hS. Renewal reward gives N_s/I, including its finite limit s η^(p−1) C_(p,m) as T tends to infinity. Differentiation gives R_s'=S H_s/I², H_s=Ig_s−N_s and H_s'=Ig_s', with g_s=T^(p−1)[p−(1−s)m(T/η)^m]. For s<1, g_s' changes sign from positive to negative precisely at T_peak, H_s is asymptotic to (p−1)T^p at zero, and H_s(T_0)=−N_s(T_0)<0. This establishes a single root in the stated bracket and a strict global maximum, also beating the limit at infinity. The partial derivative of H_s in s is the S-weighted integral of h(T)T^p−h(t)t^p>0; H_s'<0 at the root, so T_* increases strictly, including from s=0. At s=1 the strictly increasing g_1 makes H_1 positive for every finite age: T=infinity is the unique extended maximizer. For δ=1−s tending to zero the lower bracket already forces x=T_*/η to infinity; the scaled reward/time converges to C, and x^(p−1)[p−δmx^m] tends to C. Therefore x/X tends to one and writing x=X(1−ε) gives mp ε ~ C X^(1−p), including p<2, p=2, and p>2. For p=m=2 the correction is 1/(2 sqrt(pi)). Independent bounded replay: python3 /workspace/branches/replay_frozen_review.py 3 solved in the scaled gap variable at 65 decimal digits for four (p,m) pairs spanning these regimes and δ=10^−5,10^−12,10^−24; relative coefficient errors decreased to below 10^−5. No all-parameter inference is made from those numerical checks.

## originality

PASS

The renewal-reward objective and its derivative, age-dependent catastrophe risk, and salvage are prior ingredients. The supported distinction is the full stationary policy classification and explicit near-complete-salvage correction in the zero-discount, all-shape Weibull and superlinear power-value model. Located primary passages and closest Resultary comparisons do not establish that combined result. Older full-text access gaps leave priority provisional.

## value

PASS

The finite/infinite policy switch is a meaningful boundary of an age-replacement model with salvage; the full theorem says which side is finite for every Weibull shape and gives the scale and first correction of the diverging age. It isolates an actual sensitivity of the unbounded convex value assumption. It is an analytical benchmark for that assumption, not empirical advice to delay forest harvesting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
