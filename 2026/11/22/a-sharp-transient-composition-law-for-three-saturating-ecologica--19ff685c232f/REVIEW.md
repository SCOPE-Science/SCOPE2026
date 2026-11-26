# Independent mathematical audit

## correctness

PASS

Canceling 1−q for q=e^(−λ₁t) gives a ratio of a constant and S_m,S_r, where S_v=(1−q^v)/(1−q). Differentiating under the integral gives S_v′=v(v−1)(1−q)^−2 ∫_q^1(1−y)y^(v−2)dy. Hence R=S_r′/S_m′ is proportional to a conditional tail mean of the strictly increasing y^(r−m) with positive weight. Its derivative is strictly positive since the tail mean exceeds the boundary value. For H=S_m R−S_r the S_m′R and S_r′ terms cancel, leaving H′=S_m R′>0. The limiting S_v and S_v′ give H(0)=0 and H(1)=r(r−m)/(m−1). The derivative of p with respect to time has the sign of cH(q)−a, so the strict monotonicity, unique interior optimizer and the decreasing equality case follow. Fixed-depth P_n is a strictly increasing function of p, so the optimizer is independent of b and n. Cross-multiplying endpoint shares gives (m−1)a=(r−m)c, strictly below the peak threshold when divided by c. Because S_m<m and a+bS_m+cS_r>a+b+c at interior q, p/p(∞)<m; the unique maximum is strictly above the equal endpoints. Under endpoint matching and fixed b,c, at q=1−r^(−1/2) one has S_m→m, S_r≤sqrt(r), and a asymptotic to cr/(m−1), so the evaluated ratio and therefore the peak ratio tend to m. The fixed-n read map is concave with zero intercept and linear to first order as p→0, transferring the strict bound and sharpness. Two distinct rates give a fixed-sign log-ratio derivative since z/(e^z−1) strictly decreases. The symmetric witness works exactly at q=√2−1; separate bisection of the time-domain quotient-rule numerator for (1,5,50) and (a,b,c)=(45/4,1,1) gives t≈0.1895724195 and p≈0.1722690570. The supplied checker was inspected, not executed.

## originality

PASS

The general shape and the derivative-sign phase criterion are covered by a prior Laplace-ratio unimodality theorem after an explicit indicator-function reduction and elementary endpoint evaluation. They are not credited as new general unimodality results or as a novel theorem merely because the rate cutoff has new notation. The original record also expressly states a distinct quantitative result not supplied by that theorem: the strict, optimal rate-ratio cap on transient gain with matched endpoint compositions, its sharp approach with fixed b,c, and the same sharp factor for every fixed usable read depth. The pass is for that material model-specific contribution already in the frozen Finding, not for priority of the shape criterion.

## value

PASS

The independently useful exact fact is the sharp rate-ratio gain when the early- and late-time compositions match. These endpoints can mask a substantial interior amplification even though every absolute yield increases, but under the model the amplification is constrained by λ₂/λ₁ rather than by the much faster third rate. Exact sharpness with fixed middle and fast plateaus and persistence under fixed-depth detection make this more informative than showing that one arbitrary composition curve has a peak. It is a diagnostic for model interpretation, not a field deployment prescription.

The dated certificate retains the supplied scientific assessment, sources and limitations.
