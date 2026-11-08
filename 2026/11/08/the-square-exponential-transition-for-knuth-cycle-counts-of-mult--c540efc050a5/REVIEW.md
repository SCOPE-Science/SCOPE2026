# Self-review

## Correctness — PASS

The theorem fixes uniform multiset-word sampling and Knuth's canonical cycle statistic. Source [1], Sections 3–4, proves exact independence and negative-hypergeometric formulas for the increments; these are the only external nontrivial probabilistic inputs. The proof establishes moment-uniform convergence of an individual normalized increment to an exponential, then proves endpoint-weight asymptotics. When \(1<\beta<2\), a diverging number of comparable summands makes the Lyapunov ratio vanish. At \(\beta=2\) the endpoint weights converge to a geometric sequence, and a uniform geometric-tail bound justifies the infinite independent-exponential limit in moments. When \(\beta>2\), all older increments are negligible in \(L^r\). The package's rational and numerical checks passed 347 assertions; none is used as an infinite proof. Boundary assumptions \(c>0\), \(\beta>1\), and \(\theta=1\) are essential to the claim.

## Originality — PASS (subject to historical priority)

The fully inspected Stark paper [1] proves a central limit theorem for \(n_t=O(N_{t-1})\) and exhibits \(n_t=\lceil e^{t^3}\rceil\) as a non-normal example. Those results neither cover the Gaussian regime with diverging multiplicity ratio nor identify the square-exponential critical distribution. The separately inspected Buchanan–Burghart–Wagner–Yin article [2] treats functional-digraph cycles, not Knuth's canonical cycles, so its cycle counting does not imply this statement. Targeted indexed research-record comparisons did not locate the three-regime theorem; the closest ordinary-permutation and multinomial results address different objects. Search failure is not a proof of novelty. Generic triangular-array limit theory and undiscovered equivalent treatments remain genuine priority risks.

## Mathematical value — PASS

The exact independent-increment representation naturally invites asking how fast symbol multiplicities may grow before the normal law fails. A one-off cubic-exponential counterexample does not settle the boundary. This result gives a complete power-exponential classification for every fixed \(c>0\) and \(\beta>1\), discovers a non-Gaussian infinite-product critical family, and specifies the normal fluctuation scale and non-Gaussian moments. These are structurally distinct regimes, not arbitrary finite parameter slices.

## Scope, nearest literature and limits

The factorization and moment formulas come from [1], not from this finding. The conclusion depends on the canonical Knuth cycle definition; another natural notion of multiset cycles is studied in [2]. The claimed asymptotics do not cover \(\beta\le1\), cycle-weight parameters other than one, or varying exponents. Independent mathematical validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
