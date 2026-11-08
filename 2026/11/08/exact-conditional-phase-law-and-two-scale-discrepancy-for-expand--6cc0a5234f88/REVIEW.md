# Scientific review

## Correctness — PASS

For normalized Haar initial probability and integers \(b\ge2\), \(1\le n<m\), the two self-displacements are the integer multipliers \(M=b^n-1\), \(N=b^m-1\). The gcd identity in Kirsebom–Kunde–Persson reduces the two-coordinate pushforward to coprime multiplication \(u,v\). Conditioning the later phase, the \(v\) inverse branches are equiprobable; coprimality makes the early phases a uniformly shifted \(v\)-grid. Every circular arc therefore contains \(q=\lfloor vL\rfloor\) grid points plus exactly one on the residual arc of size \(\theta=\{vL\}\). Bayes gives the conditional density \((q+\mathbf1_J(uy))/(vL)\). Its exact positive part integrates to \(\theta(1-\theta)/(vL)\). Its signed primitive oscillates by precisely \(\theta(1-\theta)/(uvL)\), establishing the all-arc sharp bound, including wrapping arcs. Both sharp suprema and the criterion \(vL\in\mathbb Z\) follow without asymptotic arguments. Standalone checker: 914 rational direct-pushforward comparisons; these do not replace the unrestricted proof.

## Originality — PASS within inspected sources

Kirsebom–Kunde–Persson, arXiv:2003.01361, §6.1 Lemma 6.2 and equations (6.3)–(6.4), studies essentially the same pair of integer self-displacement phases. It establishes gcd/Fourier resonance structure to bound correlations of symmetric shrinking targets, and is therefore closely related. Its inspected full text does not state an arbitrary-arc conditional phase density, the exact all-target and arc discrepancies, the factor \(u\), or the complete zero-discrepancy resonances. He–Liao, arXiv:2302.05149, proves broader recurrence laws and estimates but not this exact joint-phase classification. The full published *Sharp second-moment inflation for expanding circle-map pair correlations* proves a Bernoulli-polynomial covariance formula for equal-radius symmetric circular intervals and a sharp aggregate variance. That exact covariance is prior work and is explicitly excluded from the originality claim; it does not state the present full arbitrary-arc conditional density or two sharp target-class discrepancies. Other indexed results are not covering. A complete priority search cannot rule out an unindexed equivalent result; the previously known Fourier method may yield these identities with further calculation.

## Mathematical value — PASS

The source literature seeks effective control of correlations between self-return events. Here the two-time dependence is completely determined, not only bounded: the theorem identifies exactly when there is literal independence, precisely which disconnected later targets maximize dependence, and how much smaller an optimal connected target's correlation is. The arbitrarily large factor \(u\) separates two common notions of decorrelation, a structural distinction obscured by aggregate Fourier upper bounds. A single exact conditional distribution answers a coherent question for every arc and every pair of times, not a selected numerical example.

## Scope and limits

No claim is made for non-Haar initial distributions, noninteger expanding maps, simultaneous conditioning on more than one earlier phase, or statistical independence of the random variables \(U,Y\) themselves. In fact full random-variable independence is excluded by their common one-dimensional source; only the stated event-level independence resonances hold. This is a self-review, not independent validation or a certification of publication priority.

Self-review: passed. Independent audit: not yet performed.
