# Independent mathematical audit

## correctness

PASS

For two nonnegative unit-demand bidders and two goods with pivot VCG (no reserves), total seller revenue equals max(a,b)+max(c,d)−max(a+d,b+c), or min(|S|,|T|) if ST>0 and 0 otherwise, S=a−b,T=c−d. A positive shock to d takes T→T−t. For iid item-exchangeable bidder vectors with atomless gaps, quadrant symmetry gives P(R'_0+=−1)=P(+1)=1/8 and P(0)=3/4, without independence inside each row. Symmetric unimodal gap density guarantees nondecreasing expected revenue by comparing translated window probabilities; the explicit two-peak continuous gap distribution violates the conclusion without unimodality. In the four-independent-Uniform(0,1) model, difference gaps have triangular density, yielding the stated exact finite-shock decline, positive-loss and mean-shift polynomials with joins at t=1,2. I independently verified SymPy gain/loss derivative identities and the mean at t=1 (7/120); independent package checker source confirms externality enumeration implementation but was not run unmodified. These analytic identities cover all t≥0; finite checks are only corroboration.

## originality

PASS

Hartline 2026 directly treats VCG revenue nonmonotonicity in the SAME two-bidder, two-good market, but demonstrates deterministic decreasing examples and the minimum Walrasian price mechanism, not an iid exchangeable distribution-free one-eighth local incidence, a symmetric-unimodal stochastic-order sufficient condition with atomless counterexample, or complete four-uniform-value shock laws. General gross-substitutes and bidder-entry revenue literature does not logically subsume these coordinate-shock statistical comparisons. Possible auction-risk literature with the same statistics remains a priority risk; search nonhits are not claimed proof of novelty.

## value

PASS

The prevalence and expected-cost size of the smallest VCG revenue-monotonicity anomaly are natural mechanism-design quantities. A distribution-free exact 1/8 incidence, a sufficient shape criterion for mean monotonicity, an atomless counterexample at its boundary, and entire finite-shock risk curves provide practically interpretable structural information distinct from the familiar deterministic example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
