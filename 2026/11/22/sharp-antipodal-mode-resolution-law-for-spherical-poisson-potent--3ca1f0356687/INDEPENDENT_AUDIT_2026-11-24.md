# Independent mathematical audit

## correctness

PASS

Write U=G(x) where x=ξ·e. Each reciprocal power is strictly convex on [−1,1]. G′ is strictly increasing, G′(1)>0, and G′(−1)=0 exactly at p/(1−p)=A^k/B^k, equivalent to q_c=tanh((d+2)atanh r). The angular derivative vanishes at both poles and otherwise exactly at roots of G′. If G′(−1)<0 the poles are strict maxima and the unique interior critical coordinate is the global minimizing latitude, at two points on the circle and a (d−2)-sphere otherwise. If G′(−1)≥0 the profile is strictly increasing off the endpoint; the weak pole is a minimum, and is nondegenerate unless equality holds. The height difference has the sign of q. Solving G′=0 gives a−bx₀=2at/(1+t), a+bx₀=2a/(1+t); the terms combine as t^(k−γ)+1=1+t, yielding the stated valley value. The endpoint values follow directly, and inversion of the strictly increasing threshold gives the stated r_c and its dimension asymptotic. For δ=q_c−q, put D=cγb(A^(−k)+B^(−k))/2 and E=cγkb²(A+B)/(AB(A^k+B^k)); then G′(−1)=−Dδ and G″(−1) at threshold is E>0. The implicit root shift is (D/E)δ+O(δ²), the quadratic contrast is (D²/(2E))δ²+O(δ³), and 1−cos θ=θ²/2+O(θ⁴) gives the angular distance and the threshold term (E/8)θ⁴. These are the printed constants, at fixed d,r, and include p=1/2 and threshold equality. RESULT.md lines 66–106 are supported by this analytic reconstruction. CHECK.py was inspected without running the submitted numerical tests.

## originality

PASS

The known Poisson-kernel model and its wrapped-Cauchy representation in d=2 are credited. The bounded literature comparison supports as distinct the two-antipodal angular classification, closed threshold and valley formulas, and explicit weak-peak collapse constants across all indicated dimensions. Nearby same-day results on other point configurations are not treated as nonexistent or presumed later; their mathematics differs. The identity of the frozen record with its own catalogue listing is not independent prior evidence.

## value

PASS

Two distinct source atoms need not create two detectable angular modes. This natural exact classification says precisely how a weaker source loses its peak, how increasing dimension changes the resolution threshold, and on what angular and contrast scales the peak becomes hard to distinguish. The quantitative critical constants and the latitude degeneracy give more information than component identifiability or a one-off numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
