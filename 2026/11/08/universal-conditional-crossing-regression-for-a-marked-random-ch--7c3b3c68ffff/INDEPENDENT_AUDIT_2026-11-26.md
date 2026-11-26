# Independent mathematical audit

## correctness

PASS

After conditioning on e, all residual perfect matchings are uniform. For given t, choosing t vertices from each arc and bijecting them, then matching each even-sized residual arc, gives every feasible class and excludes all other degrees. Conditional arc-label symmetry applies to the four pair types in RESULT.md lines 27–42: two internal chords on one arc have one alternating pattern out of three pairings; an internal and bridge chord alternate iff the bridge endpoint is the middle of three exchangeable positions; two bridges have one alternating bijection out of two; internal chords on opposite arcs cannot alternate. With p=(a−t)/2 and q=(b−t)/2, this yields E[Y|D=t]=(p(p−1)+q(q−1))/6+t(p+q)/3+t(t−1)/4. The quadratic terms cancel and the linear coefficient is (a+b−1)/12=(2n−3)/12. Adding t correctly shifts the slope for K. This includes deterministic D. Counting one bridge or an ordered pair of disjoint bridges gives the factorial moments in lines 44–52 and their stated variance; the covariance then follows by conditional expectation. VERIFICATION.md and verify.py were inspected, not executed. The recorded exhaustive enumeration concerns n=3,…,7 only; the pair argument is all-size.

## originality

PASS

Relative to the checked evidence, the distinct result is the exact pointwise residual-crossing mean conditional on the specified chord and on every feasible degree, including its arc-independent slope. Neither separately known degree and global crossing moments nor the closest simple-chord enumerations give this general conditional first moment. This is not an absolute priority claim.

## value

PASS

This relates a natural local statistic of the random intersection graph (degree at a marked chord) to its residual global edge count. Changing the marked span changes the degree distribution and intercept but not the conditional slope. The exact all-feasible-degree statement is stronger than covariance, and the cancellation of the quadratic term across chord classes resolves a concrete finite and all-size prediction problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
