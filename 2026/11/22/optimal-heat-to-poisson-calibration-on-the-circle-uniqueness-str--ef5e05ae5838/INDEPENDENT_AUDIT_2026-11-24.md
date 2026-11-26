# Independent mathematical audit

## correctness

PASS

With probability Haar measure, Parseval gives twice the positive-frequency sum; the n=1 cross term forces center zero at r>0. For a=−log r, the derivative has the sign of G_t(a)−1. The decreasing Gaussian tilt lowers the mean of the law proportional to n exp(−an), so (log G_t)'≥2 coth a−coth(a/2)=tanh(a/2)>0. Its endpoint limits are 0 and ∞, and F'_t(t)<0 by every mode n≥2; r=0 has higher loss by strict increase past the root in a. At q→0, expanding r/(1−r²)²=q+2q⁴r+O(q⁹r²) gives q−2q³+11q⁵, with the residual O(q⁷) controlled by derivative bounded away from zero. For h=√t and c=a/h, monotone bracketing uses H(c)=4∫y exp(−y−y²/c²)dy, strictly increasing from 0 to 4. Uniform Euler–Maclaurin on compact positive c has h² coefficient c²(H(c)−1)/3 in G; the h⁴ coefficient at c_* is −c_*⁴/20−c_*²/30. Since H'(c_*)>0 this gives the displayed t^(5/2) correction and remainder. For the loss the first odd derivative at 0 vanishes and the third is −12c−6c³; J'(c_*)=0 absorbs the O(h⁴) movement of c, giving the t^(3/2) correction. At a=t the squared Poisson tail alone is t^(-1)+O(1), and the other terms are O(t^(-1/2)), proving the diverging comparison. Independently evaluated the three defining constants by bounded quadrature and scalar bisection: 1.077742254305174, 0.067380556580826, 0.090982449802525. The frozen CHECK.py was inspected, not executed; the VERIFICATION.md finite-check decimals are coarser than the theorem's constants, consistent with the explicit 10^(-8) tolerance rather than agreement to every digit printed.

## originality

PASS

Pass for the global L² calibration theorem, strict inward bias and sharp asymptotics, not the loss or stationary equation. The closest available distinct catalogue statement has the same kernels, uniqueness and sign but uses forward KL; its differing coefficients rule out merely relabeling the optimum. The closest cited L² prior work is Bailey's wrapped-normal mixture fitting, already credited for the loss and stationarity; the cited primary pages and related journal article could not be inspected independently. No inspected source establishes the stated L² global and asymptotic assertions. This is a bounded statement-level decision, not a priority certification.

## value

PASS

This unit-mass benchmark compares two standard circular kernels that are often calibrated by the first trigonometric moment. It proves that this natural calibration misses the actual optimum at every finite time and can cost an unbounded factor near the singular limit. The vanishing first correction and sharp positive irreducible L² coefficient specify more than numerical proximity or a textbook Fourier reduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
