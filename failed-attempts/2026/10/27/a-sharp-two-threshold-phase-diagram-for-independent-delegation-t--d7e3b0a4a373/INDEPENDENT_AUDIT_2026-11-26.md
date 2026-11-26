# Independent mathematical audit

## correctness

PASS

Conditioning on the Bin(4,d) count gives P₀,P₁,q,q,q. Switching a single fixed ballot from direct to delegated changes the conditional accuracies by Δ₀=B−A=3p(1−p)[q(1−p)²−(1−q)p²] and Δ₁=−B=q(1−p)³−(1−q)p³. The remaining successive differences vanish. Differentiation gives F′(d)=4(1−d)²[(1−d)Δ₀+3dΔ₁]. The bracket is affine, with strict sign inside each monotonic region including the boundary q=Q₂ or Q₃; both endpoints cannot vanish simultaneously. In the open middle region it has exactly one zero, (B−A)/(4B−A), with strict gains over both endpoints. Odds powers give Q₂<Q₃; for one voter there is no choice, and for three only the first successive difference can be nonzero, giving a monotone or constant polynomial. This proves both uniqueness and sharp minimality. The frozen exact verifier was inspected, not run. The independent /workspace/branches/independent_replay.py counts correct profiles by expanding actual ballots and reproduces the exact witness and representative behaviors at both thresholds and inside. The proof establishes universality, not the finite samples.

## originality

FAIL

The exact phase diagram is mechanically implied by the prior single-expert pivotality formulas in Dhillon et al., arXiv:2306.03960, Proposition 3 and Appendix A.1.3, not just analogous to their equilibrium result. Their model in that section has the same odd electorate with one superior expert and homogeneous independent nonexperts. In the appendix the payoff from switching an ordinary vote is the pivotal event probability times expert posterior correctness minus ordinary correctness. They give both conditional pivotal probabilities. In the present notation, for N=5 and t=0,1 existing delegates, write a_t=Pr(pivotal|expert correct), b_t=Pr(pivotal|expert incorrect). Their formulas give (a₀,b₀)=(3p(1−p)²,3(1−p)p²) and (a₁,b₁)=((1−p)²,p²). Hence Δ_t=(1−p)q a_t−p(1−q)b_t yields the exact two differences above, not merely their signs. The appendix also identifies the payoff plateau once the expert dictates. The elementary binomial/Bernstein derivative then gives F′=4(1−d)²[(1−d)Δ₀+3dΔ₁] and immediately yields both thresholds, all equality cases and the closed optimizer. For N=3 the same prior formula plus the dictator plateau leaves only one difference, so the lower-size minimality check also follows mechanically. Taking flat binary priors in the prior paper does not restrict this implication: in the stated symmetric competence model correctness conditional on either truth is identical. No assertion is made that the prior paper explicitly states or labels a Bernoulli-rate optimizer.

## value

FAIL

Calibration of an anonymous randomized rate is meaningful as an application, but here the purported contribution is entirely a binomial reweighting of already available exact pivotal probabilities and the zero-increment plateau. The thresholds and minimality, not just the qualitative benefit, follow from a linear bracket, and the exact example illustrates that deduction without an independent new structural result. No valuable distinct remainder of the frozen theorem was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
