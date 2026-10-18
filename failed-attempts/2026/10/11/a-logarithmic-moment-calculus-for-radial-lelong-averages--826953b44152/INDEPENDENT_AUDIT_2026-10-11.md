# Independent mathematical audit

## correctness

PASS

The classical logarithmic-radius spherical mean \(\phi(x)=S(u,e^x)\) is increasing convex with asymptotic slope \(\nu(u,0)\) at \(-\infty\). Convexity gives \(\phi(x)-\phi(x-s)\to\nu s\) for each \(s\ge0\), bounded uniformly by \(Cs\) for sufficiently negative \(x\). With \(s=-\log t\), the finite logarithmic kernel moment is an integrable dominating function. Dominated convergence yields \(S-A_\beta\to\nu L(\beta)\), and subtraction gives the result. A radial mollifier disintegrates into a positive probability density in the radius; for the uniform ball, \(2n\int_0^1(-\log t)t^{2n-1}dt=1/(2n)\). The argument is infinite-dimensional analytically and uses no numerical sampling.

## originality

FAIL

Implication-level coverage follows from the standard exact asymptotic slope theorem for spherical psh means, convexity in logarithmic radius, and the classical radial disintegration formula. The initiating Deng–Yang–You paper already uses a radial regularization expressed as a probability-weighted integral of spherical means and gives the uniform-ball mean gap exactly. The assigned generalization replaces one radial probability density by any distribution of shifts with integrable first moment: applying dominated convergence to standard fixed-shift limits is a routine measure-theoretic corollary, not a new structural lemma. No claim of full-text noncoverage is made; this rejection rests on the positive mathematical implication of already known prerequisites, not on the unavailable preprint or failed Resultary search.

## value

PASS

The radial-kernel logarithmic moment is a natural exact invariant, useful for relating mollifiers and spherical means and recovering the Lelong number from regularizations. It has independent expository and practical meaning even though the computation is already a routine corollary of established theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
