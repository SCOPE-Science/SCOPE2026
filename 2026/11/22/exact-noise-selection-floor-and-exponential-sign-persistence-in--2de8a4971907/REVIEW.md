# Independent mathematical audit

## correctness

PASS

The reference in Finding line 16 to squared error a_{m,h} is a mean-square statement (explicitly defined and proved at lines 52–56), not a pathwise constant. Conditional on the entire past, counting the observations with the same sign as the nonzero current iterate gives J ~ Bin(m,1/2): the squared residual difference between a mismatching and a matching sign is 4|x|. Among the h eligible observations, min(J,h) agree. Conditional on the screen, an average of s independent uniform cached-label draws has second moment (1−1/s)(2 min(J,h)/h−1)^2+1/s. Fresh per-occurrence noise, even for repeated labels, has zero conditional cross terms. Odd sample sizes prevent the residual tie at x=0. Averaging each eligible value once, a genuinely different update even for s=h, flips the sign iff J≤(h−1)/2. The conditional flip probability is constant over histories, so the flip indicators are iid and runs are geometric. The law of large numbers and boundedness give the stated piecewise floor including q=1/2; the tail is between the largest included binomial mass and (1+(h−1)/2) times that mass, giving the stated strictly positive entropy rate by Stirling when 0<q<1. The exact m=5,h=s=3 illustration checks out.

## originality

PASS

The algorithms and qualitative benefit of re-querying are prior. The exact comparison and exponential sign-run law in this scalar iid-noise model survive comparison with the closest algorithmic primary source and with the published scalar SCOPE examples. This is a best-of-knowledge finding, not a priority claim over the same-day example.

## value

PASS

A condition-one, exactly consistent example isolates measurement reuse as a source of nonvanishing risk, rather than rank deficiency or static corruption. The exact fixed-quantile floor and persistence exponent give benchmark magnitudes and a separation between the sampled average and the full retained average, beyond the known qualitative warning. The sign law quantifies a time scale not controlled by a mean-square bound alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
