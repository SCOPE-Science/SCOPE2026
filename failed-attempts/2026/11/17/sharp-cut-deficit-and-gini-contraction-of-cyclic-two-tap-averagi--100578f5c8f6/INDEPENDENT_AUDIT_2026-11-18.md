# Independent mathematical audit

## correctness

PASS

Directly counted opposite nonzero signs for pairs of consecutive binary gradients: each of r 0->1 transitions conflicts with each of r 1->0 transitions, each inducing loss 2 min(theta,1-theta), so exact deficit is 2mu r^2. Since r>=1 and k(n-k)<=floor(n^2/4), balanced contiguous cuts attain the coefficient. Coarea/layer-cake plus pairwise subadditivity extends it to every real input; endpoints theta=0,1 are permutation/identity, while n=2,3 also fit. Independently tested 6078 exact (n,theta,cut) combinations for n=2..10 and theta=1/4,1/2,3/4. This is correctness PASS, not originality.

## originality

FAIL

FAIL: a previously published same-model stronger heterogeneous-kernel theorem explicitly proves the IDENTICAL homogeneous two-tap cut formula (its equation (1)) for every n>=4 and theta in (0,1), and the exact perturbation defect with epsilon=0. Because G(x)<=floor(n^2/4) osc(x), that theorem gives the submitted operator norm bound; balanced single arcs realize equality via its equation (1). Endpoint theta and n=2,3 are elementary exceptions that do not rescue originality. Both records have date 2026-11-17; no within-day order claimed. A separate prime boxcar theorem also includes m=2 for prime n. Entire claimed finding is implied by already published same-object mathematical evidence.

## value

FAIL

FAIL as an independent new contribution: the formula, cut identity, extremal geometry and oscillation contrast are correct but already part of the stronger heterogeneous-kernel bound (with trivial endpoint additions) and a prime boxcar exact table. No remaining new motivated invariant or sharp boundary survives the comparison; reproducing a known exact subcase does not meet V even when clearly proved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
