# Self-review

## Correctness (PASS)

The domain is explicit: \(k\ge2\), positive stage and direct rates, and viability factors \(0<a<b\le1\), with fixed deadline \(T>0\). Erlang completion and independent viability justify the probability formulas. The normalized CDF quotient is proved strictly one-peaked for faster per-stage transit using the exact derivative identities \(U'=Bh'\) and \(R'=e^{-x}U/B^2\). Its supremum is attained uniquely; strict monotonicity of its peak in speed produces the threshold and all crossing equality cases. A nondegenerate peak yields the square-root coalescence law. Compact-uniform and tail controls yield the large-speed constant, and the law of large numbers with the sharp bound \(u_k>k-1\) yields \(kc_k\to1\). The slower-mean example is proved using rational Taylor bounds. The standalone code passed 2,547 supplementary finite assertions, which are not a substitute for proof.

## Originality (PASS on inspected literature; priority provisional)

The published habitat-matrix experiment of Szojka and Germain (2024) and the multi-step stepping-stone connectivity framework of Saura, Bodin and Fortin (2013) motivated the model but do not establish the all-stage finite-deadline phase frontier in inspected full text. Pinelis's derivative-quotient monotonicity approach is a known ingredient and is not claimed to be new. Indexed research on density peaks for two-route transit mixtures, spectral connectivity and diffusive first-passage crossings concerns different statements, not a strictly stronger theorem covering the entire speed/viability classification, slower-mean reversal, critical saddle-node and stage asymptotics. Residual risk: some general stochastic comparison literature may contain an equivalent specialized result; none was demonstrated by actual searches. The claim is not certified historically unique.

## Value (PASS)

Connectivity assessments often rank routes by eventual reachability or mean travel time, even though suitable target habitat can expire. The proved two-crossing window shows exactly how both rankings can be misleading, under a transparent and testable serial travel law; the unique critical rate and the \(kc_k\to1\) scaling quantify natural speed and stage costs. No downstream empirical performance or ecological intervention efficacy is claimed.

## Closest literature and limitations

Szojka and Germain, *Ecosphere* (2024), DOI 10.1002/ecs2.4814; Saura, Bodin and Fortin, *Journal of Applied Ecology* (2013 online), DOI 10.1111/1365-2664.12179; Pinelis, *L'Hospital-Type Rules for Monotonicity*. The model assumes independent equal-rate exponential stages and independent terminal viability, with one direct exponential alternative, one individual and a fixed deadline. Unknown empirical parameters, reproduction, environment feedback and general transit kernels are outside scope. No independent scientific audit has been performed.

Self-review: passed. Independent audit: not yet performed.
