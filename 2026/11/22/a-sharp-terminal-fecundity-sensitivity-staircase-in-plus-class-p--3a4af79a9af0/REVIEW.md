# Independent mathematical audit

## correctness

PASS

Independently eliminate lower rows to normalize the stable age vector by w_1=1. Then lambda=sum_j f_j w_j(lambda); implicit differentiation gives G_j=w_j/(1-sum_i f_i w_i'), a common positive denominator (the weights are nonincreasing functions of lambda>t). The lower-row multipliers are s_j/lambda through class n-1, and s_(n-1)/(lambda-t) at the terminal step, giving strict nonterminal descent in the stated growth regime and exactly the reported tail-product ratio. For terminal-only fertility F=lambda/w_n(lambda) increases strictly. The h_j used to compare ranks increase from 1-t to infinity on [1,infinity); equality P_j=1-t reaches replacement only. Eligible indices form a suffix, and at a crossing with j the terminal value is strictly above j+1, so that next crossing must occur later. This includes t=0 (no growing-regime crossing) and survival entries equal to one (crossings remain distinct). An independent scalar bisection reproduces the three growth and fertility crossings in the four-class example. Inspected but did not execute the frozen checker; the proof is symbolic. Absolute sensitivities and not elasticities are ranked.

## originality

PASS

Pass is limited to the explicit complete terminal-rank staircase and its all-ranks criterion, not the left/right Perron formula, the stable-age recurrence, or priority for the nonterminal ordering. The strongest inspected same-model rule stops at the penultimate class. The standard formula immediately gives the pointwise comparison, but the inspected work does not give the complete sequence of eligible and ordered crossings on a fertility path or the criterion for traversing all strict ranks.

## value

PASS

A modest structural contribution: S2 identifies a real missing terminal comparison in a standard demographic model. The criterion distinguishes fixed-survival populations whose adult plus class can pass every absolute-sensitivity rank from those where some ranks are structurally impossible. It gives all threshold and tie conditions rather than only recomputing a sensitivity or naming an example. Its use is to interpret the terminal exception and diagnose crossings in the stated one-parameter family, not to recommend conservation interventions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
