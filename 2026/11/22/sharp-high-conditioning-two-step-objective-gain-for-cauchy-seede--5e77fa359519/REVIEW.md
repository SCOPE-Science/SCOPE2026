# Independent mathematical audit

## correctness

PASS

For the two-mode SPD quadratic with κ>1 and r=v²/u²>0, compute F_j=(g_{j,1}²+g_{j,2}²/κ)/2. The Cauchy step multiplies g_0 modes by (κ−1)r/(1+κr) and −(κ−1)/(1+κr). Its secant is parallel to g_0, so the second step a has a²=(1+r)/(1+κ²r), in (1/κ²,1), and multiplies the modes by 1−a,1−κa. Substitution gives the displayed ratio. Bounding the two squared factors by 1 and κ²a² respectively and using κ²r a²<1+r bounds the ratio by κ²(κr²+1+r)/[(1+κr)²(κ+r)]. The denominator less κ(κr²+1+r) is r(2κ²−κ+1)+r²(κ³−κ²+2κ)+κ²r³>0. Nonnegativity follows from the squared energy. For r=κ^(−3/2) the first energy ratio is asymptotic to κ^(−1/2), a is asymptotic to κ^(−1/4), and the next ratio is asymptotic to κ^(3/2), squeezing the rescaled supremum to one. Exact replay using g_0=(sqrt(63),1), κ=9 gives step lengths 8/9,2/3 and energies 284/9,28/9,5516/81, hence all three rational ratios. The argument proves neither a finite-κ optimizer nor later-step control; absent-mode or stationary seeds are excluded as stated. Frozen VERIFICATION.md, artifacts/verify_two_step.py and artifacts/verification.txt were inspected; the script was not run. The text output is recorded evidence only, distinct from the independent mode and rational-energy calculations.

## originality

PASS

Best-of-knowledge pass only for the sharp initial-to-final amplification coefficient for the exact pair of updates. The spectral step and adaptive estimators are established prior rules, and the existence of objective overshoots for broader classes is not credited as new. The closest same-metric prior uses a different second rule; the closest same-class prior bounds a different ratio and cannot imply the sharp coefficient.

## value

PASS

A practitioner using the natural exact-search warm-up and established curvature rule cannot infer net progress from first-step decrease or asymptotic convergence. The sharp initial-to-final coefficient quantifies how much progress can be lost and identifies an adverse scale for the starting spectral mixture, going beyond an example of overshoot or a loose previous-iterate bound. The result is deliberately only about two exact updates on the stated two-mode model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
