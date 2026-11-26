# Independent mathematical audit

## correctness

PASS

PASS for the repaired product-sampling model in /workspace/repairs/1, not for the literal frozen assumptions. Mutual independence of types does not imply independence of the type vector from R. For N=2 take two iid fair type indicators, set R=3/4 on odd parity and R=1/4 otherwise, and use tau=1/2 and independently generated fair auxiliary draws. Each type individually is independent of R, s=1/2, h=3/4 and expected contribution costs match. At quorum 2, shared achievement and saved risk are both zero (high risk occurs only with one adaptive agent), but independent-randomization achievement is 1/16 and its saved risk is 1/64. Thus even the upper endpoint ranking can fail under the frozen wording. The repair explicitly makes the type vector independent of risk and the auxiliary draws independent of both. The conditional binomial and saved-loss factorizations then follow, with both costs cancelling. Positive-count likelihood ratios have common step multiplier (1-sx)/(s(1-x))>1, so dropping the first term of the conditional tail average strictly increases L_m. Strict convexity of (1-xz)^N gives L_1<1 and L_N=s^(1-N)>1; the welfare cutoff is well defined and no later (it can start at quorum 1). On the Nq+z sqrt(N) scale the shared Bin(N,x) tail tends to one because q<x; the independent tail tends to the Gaussian upper tail. Bracketing each first crossing on both sides of its limiting quantile establishes the o(sqrt(N)) expansions; strict-versus-weak endpoints affect only O(1) indices and full quorum is outside the band eventually. Independent exact replay with python3 -B /workspace/repairs/1/checker.py gave 240 quorum comparisons, the rational witness -85/4096 and +827/8192 per unit b, and the parity counterexample. These are checks on finite identities, not on the CLT theorem.

## originality

PASS

Best-of-knowledge pass for the repaired joint comparison and its explicit two-cutoff Gaussian width, not for shared threshold response, finite binomial mixtures, likelihood-ratio ordering techniques or the binomial CLT. The repair restricts the sampling hypotheses to the actual law used in the proofs.

## value

PASS

Success frequency and risk-weighted protected endowment are distinct, independently useful measures of a threshold public-good protocol. The repaired result proves their exact ordered crossings and a growing positive-width band of strict disagreement despite equal expected charges, not an isolated payoff recomputation. It deliberately does not identify a pure correlation effect, compare equally informative signals, infer equilibria, or claim policy impacts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
