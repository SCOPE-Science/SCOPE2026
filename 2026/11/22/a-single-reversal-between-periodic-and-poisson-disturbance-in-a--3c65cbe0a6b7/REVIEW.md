# Independent mathematical audit

## correctness

PASS

Independent cycles reset both stages; the sample-path renewal-reward ratio gives the almost-sure suitable fraction. The periodic and exponential age weights are 1_{0≤t<m}/m and e^{-t/m}/m. With the two-exponential suitability probability these give the stated formulas and the exact unequal-rate difference a[g(am)-g(bm)]/(a-b). For B(x)=1-(1+x)e^{-x}, differentiating x²e^{-x}/B(x) gives the sign of -J(x), with J(0)=0 and J'=B>0. The elasticity r=xg'/g therefore strictly decreases from 1 to -2, giving the strictly monotone dilation ratio and the unique positive maximum z. The equality point is strictly between z/max(a,b) and z/min(a,b). The coinciding-rate limit is am g'(am), not a ratio test at a=b. Independently, p(t) is proportional to e^{-min(a,b)t}(1-e^{-|a-b|t}) for unequal rates and t e^{-at} for equal rates, hence has decreasing logarithmic elasticity. In the rescaled reward integral the weight e^{-x}-1_{x<1} has one sign change; increasing m reweights strictly towards the negative part via the decreasing ratio p(m₂x)/p(m₁x). This corroborates uniqueness. Independent bisection of 3 log(1+z)-z-log(1+2z) and of the direct reward difference with 2,048-panel Simpson quadrature give z≈0.868863198403742 and m*(1,2)≈0.607586231915717. RESULT.md §§Assumptions and Proof are the replay path for the exact result; VERIFICATION.md and check.py were inspected, not executed. Finite diagnostics do not certify the universal claim.

## originality

PASS

The supported distinct result is the all-rate matched-mean reversal and exact characterization of its threshold for a transient suitability window, not renewal reward, the Markov balance equations, or a claim about population persistence. The closest inspected results share a clock comparison, a one-crossing property, or a biological setting, but not the same observable and assumptions. The decision is bounded by the inspected material, not a priority certificate.

## value

PASS

Matching mean disturbance intervals removes a major confound but does not order habitat suitability: young patches have not matured and old patches have already senesced. The theorem completely resolves the sign and brackets its switch over all positive rates, including exactly coincident rates. This is a useful model benchmark for temporary suitability under reset variability, rather than a generic claim about persistence or management outcomes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
