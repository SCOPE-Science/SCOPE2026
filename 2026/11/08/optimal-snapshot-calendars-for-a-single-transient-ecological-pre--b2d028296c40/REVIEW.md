# Independent mathematical audit

## correctness

PASS

The first detection decomposition has disjoint arrival windows and term e^(-r u_(i-1))*g_r(h_i), g_r(h)=r(e^-h-e^(-r h))/(r-1), or h e^-h for r=1. Memorylessness makes the Bellman value b_k=max_h(g_r(h)+e^(-r h)b_(k-1)); derivative has one positive root for b<1, yielding the stated unique recurrence and reverse-index optimal gaps. b_k grows to 1 and epsilon_(k+1)=epsilon_k-(r/2)epsilon_k^2+O(epsilon^3) yields n epsilon_n->2/r; sum of gap asymptotics yields terminal time. For equal gaps H_r(h)=g_r(h)/(1-e^(-r h))=1-h/2+O(h^2); comparison of e^(-rnh) and h/2 produces sharp miss ~log n/(2rn). Independent numerical recurrence and direct first-detection probability summation match across r=.5,1,2,3 and n=1,2,4,6, including r=2 n=6 b=6/7. Explicit no-horizon, one irreversible episode and no imperfect detection boundary.

## originality

PASS

Related Markov-availability visits and general occupancy allocation models use different observation/detection dynamics or finite horizons. Moore–McCarthy full article optimizes survey effort rather than intercepting a single exponential interval with n noiseless snapshots. Kendall et al. directly motivate staggered arrival and departure, but its full text was inaccessible and could in principle contain a related schedule; best-of-knowledge assessment is qualified. The exact all-n recurrence plus equal-grid logarithmic penalty was not implied by the inspected published results.

## value

PASS

Optimal interception of a transient interval is a natural discrete survey design problem; strict uniqueness, increasing gap structure, rational special case and asymptotic cost of equal spacing are reusable mathematically precise design facts, not merely one simulated timetable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
