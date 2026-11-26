# Independent mathematical audit

## correctness

PASS

n=1 has only one calendar. For n≥2, the trace sums closed stage histories. Each adult-to-juvenile event at i uses f_i and forces maturation at i+1, so such seasons form a cyclically nonadjacent set S; every such S specifies exactly one history with weight s^{|S|}t^{n−2|S|}∏f_i. This includes the two-season case. At equal multiset the determinant is fixed at (−s)^n∏f_i. Every product of at least two matrices is entrywise positive (the two-step product is positive and each further factor preserves positivity), and at fixed determinant its Perron root (T+sqrt(T²−4det))/2 is strictly increasing in its positive trace. The nth root also preserves order. For n=2,3 only the size-zero and size-one terms occur; these do not depend on arrangement. For n=4,5 only the size-two nonadjacent-pair sum can change, multiplied by positive s²t^{n−4}. At n=6 the size-three term sums the two alternating triples. Switching the middle 3 and 4 in the example increases the pair sum by 3 relative to the original, while the original alternating triple sum 63 exceeds the switched sum 56. Thus original minus switched is s²(7s−3t²). For s=1/4 the crossover sqrt(7/12) is admissible and the two exact trace gaps are 1/16 and −17/400. This argument also covers multisets with repetitions in the no-reversal part. Independent symbolic product replay at all distinct-label permutations through six seasons: python3 /workspace/independent_checks.py 3; the universal positive-real assertion comes from the proof, not the sampled labels.

## originality

PASS

The supported claim is the exact six-season threshold for two calendars that reorder only a fixed fecundity multiset, with s,t strictly positive and common across seasons, as a common survival parameter varies. Periodic-product theory and cyclic matching/independence trace expansions are background. The inspected nearby seasonal studies use different forcing or ranking comparisons; the closest exact Resultary examples do not force or contradict the new lower bound. Priority remains bounded by the unavailable older full texts.

## value

PASS

Fixed survival across seasons and a fixed multiset isolate the effect of reproductive timing. For this natural controlled comparison, the proof pinpoints when the preferred ordering can depend on a common survival parameter, and gives an interior switch between two explicit calendars. The lower bound gives robustness of every pairwise order through five; the six-season construction shows that this robustness cannot be extrapolated. This is neither a global optimization algorithm nor an inference about real species or nonlinear persistence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
