# Independent mathematical audit

## correctness

PASS

The theorem and exact formulas hold. At entrance, the middle m=M−1 letters are uniformly onto N=n−1 colors other than the new color, which is absent from both the middle block and the outgoing draw. Prescribing r singleton positions leaves (N−r)! S(m−r,N−r) words for each ordered choice of their distinct colors, so the count ratio is S(m−r,N−r)/S(m,N). The generating-function identity gives (N)_r/(m)_r times [τ/(exp(τ)−1)]^r times the ratio of the two zero-truncated-Poisson local masses. The numerator and denominator departures from their respective means are both bounded: they are (r+1)(a−1)−{an} and (a−1)−{an}. This corrects the incidental r(a−1)+o(1) expression in line 60; boundedness is what the span-one local limit uses. Thus the ratio tends to one, and the joint singleton probabilities tend to exp(−rτ). For the collision bound, the supremum local mass for a sum of N−1 copies is O(N^{−1/2}) by Fourier inversion, and the conditioning denominator is Θ(N^{−1/2}). The conditional second factorial moment is therefore bounded by a constant times the unconditional one, giving an O(1/n) fixed-pair collision probability. A rescue of any of the first k departing singleton colors costs at most k²/n. With neither event, survival through k is exactly absence of singletons in the first k positions. The immediate-exit formula is the r=1 singleton probability multiplied by (n−1)/n. Stationarity partitions onto time into runs, which have finite start and end almost surely by independence of disjoint windows and the positive chance of a monochromatic window. Summing over the time elapsed from the last entry gives onto mass = entrance flux × conditional mean. Their exact counts give the finite mean and their Stirling ratio tends to a(exp(τ)−1)/τ=exp(τ) by the same local limit. The finite boundary M=n=2 uses S(0,0)=1; k=0 is automatic.

## originality

FAIL

The exact fixed-a geometric wording was not found as a stated theorem in the compared sources. Nevertheless the prior indexed singleton-clock proof already gives the exact entrance law, conditional exchangeability of singleton locations given their number, and a finite-horizon sandwich for the first loss, not just a logarithmic-window exponential limit. Applying these existing, finite-n steps with Long's local bound at fixed density mechanically yields the geometric law. The mean is already covered by the earlier exact flux formula and its asymptotics, and the immediate-exit expression is the singleton calculation at the first position followed by a nonmatching replacement. The failure is lack of a materially distinct result, not a claim that Long's first-hitting theorem has the same statement.

## value

FAIL

Entrance-conditioned duration at linear density is a natural quantity and the reported limit is correct. But this record adds no nonroutine argument or exact invariant beyond the established singleton-clock mechanism at fixed horizon: conditional singleton positions are already a uniform subset, and fixed positive density makes the geometric consequence immediate with existing occupancy bounds. The finite mean is old, and the first-step exact probability is a direct singleton count. No substantive surviving extension (for example, a new uniform range of horizons or parameters) is established here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
