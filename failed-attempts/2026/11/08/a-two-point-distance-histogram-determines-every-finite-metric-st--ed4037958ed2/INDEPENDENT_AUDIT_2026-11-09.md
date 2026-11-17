# Independent mathematical audit

## correctness

PASS

Direct same-arm and distinct-arm convolution gives f(t)=2/L² sum (a_i-t)_++2/L² sum_{i<j}[t_+-(t-a_i)_+-(t-a_j)_++(t-a_i-a_j)_+]. At t=0, f(0)=2/L and f′_+(0)=k(k-3)/L². The second distributional derivative on (0,infinity) is -(k-2)sum delta_{a_i}+sum_{i<j}delta_{a_i+a_j} after scaling L²/2. The least residual atom after subtracting known arms is a negative singleton of smallest remaining length, since pair sums involving an unknown arm are strictly larger. Repetition correctly handles collision/cancellation. k=1,2 is an interval. Independently verified exact signed-atom peeling on four collision cases; source check_star.py inspected.

## originality

FAIL

FAIL: the published October 25 full primary theorem and November 1 replication cover precisely the same full pair-distance law, all k>=3 and all positive arm-length multisets including ties and cancellations, with identical f(0), f′(0), signed curvature atoms and greedy peeling. Both also describe k<=2 interval degeneracy. There is no narrower surviving novel claim or changed hypothesis.

## value

FAIL

FAIL for independent mathematical contribution: the inverse invariant and cancellation-safe reconstruction were already completely established in October 25 and November 1. The problem is naturally motivated, but this package is a rederivation rather than a new structural or exact fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
