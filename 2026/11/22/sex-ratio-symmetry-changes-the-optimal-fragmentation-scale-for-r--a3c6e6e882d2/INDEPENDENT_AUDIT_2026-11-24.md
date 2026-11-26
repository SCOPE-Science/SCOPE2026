# Independent mathematical audit

## correctness

PASS

Independent Poisson splitting yields the binomial law. The Markov bound on success tends to zero with site count at fixed pressure, so a positive maximum is attained. At r=1, the event of exactly one founder of each sex assigned to different sites has positive probability for every k>1, giving strict one-site dominance. For r≥2 let m=r−1, t=L/k and h=log(1+e^(−δt)(1−e^(−at))). The j=0 and j=m summands separately bound the failure from below; on the localized scales the successive backward ratios are O_r(q/(kp)), so the last summand gives the asymptotic. In balance the lower bound h≥c min(t,1) rules out k≫√L, while the term mat rules out k≪√L. Uniformly on compact positive ranges of x=k/√L, the normalized log correction tends to m/(2x)+x log 2, whose unique minimum gives both constants. At fixed imbalance, the rounded-down trial k=floor(δL/log L) gives t=log L/δ+O((log L)^2/L) and kh=o(1). Smaller t by a fixed relative factor incurs an exponentially larger kh, and larger t by a fixed factor increases the lower bound m(at+log L−log t)+O_r(1), since at−log t is increasing there. This localizes every optimizer and the same last-term lower bound matches the trial through order log L. The numerical verifier was inspected but is not needed for these asymptotic or strict claims.

## originality

PASS

The distinct result is the optimized rare-failure asymptotic for a fixed target of at least two distinct two-color boxes with a growing number of boxes, including the sharp change under a fixed imbalance. The binomial split, finite same-box collision model and r=1 reasoning are not credited as the main advance.

## value

PASS

The natural redundancy goal forces a balance between opening more sites and losing local co-occupancy. The exact model exhibits a singular change in the optimal order at symmetry, with sharp optimizer constants and failure-log corrections; it is more informative than the finite binomial formula or the r=1 boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
