# Independent mathematical audit

## correctness

PASS

For j<p, either the maximizing mean at j is at most f(j+1), or it uses r≥1. The ball at j+1 of radius r−1 has the same clipped right endpoint; the only removed sites lie at or to the left of j and have values below the old mean. Hence Mf cannot decrease before p; reflection gives the other branch. Singleton values and the global maximum give Mf(p)=f(p), including every permissible p on a plateau. Both variations then telescope. The prefix and suffix through p lift the endpoint values by at least A/(p+1) and B/(n−p). Subtracting (A+B)/n gives the exact claimed lower bound on the deficit. For nonconstant data an interior p makes that lower bound strictly positive. If the peak is the first endpoint, equality forces the global mean at the opposite endpoint to attain its baseline-plus-one-spike lower bound, which forces every nonpeak value to be the baseline; reflection handles the last endpoint. A spike realizes equality. A decrease followed by an increase prevents unimodality and yields separated boundary or interior peaks (allowing plateaux). For signed inputs apply the inequality to the modulus and use the reverse triangle inequality, without extending the equality classification. The exact finite checker was inspected, not executed; it selects the first maximum, so the all-permissible-index assertion rests on the proof.

## originality

FAIL

Distinct Resultary entries 12b332db5c97 and 2ffb5fd973e3 already cover the full unimodal factor and the exact peak-location deficit and rigidity; the latter also expressly preserves the peak and gives a stronger zero-endpoint fixed-peak result. Their indices 1 through n are equivalent to indices 0 through n−1. Thus the main finding is not distinct in the compared catalogue. Historical publication order and derivation are not established by the paths, which in fact carry later dates than the frozen source path. The monotone-only precursor is a proper restriction, not the basis for this failure.

## value

PASS

A peak-preserving structural lemma makes the variation telescope, proves a meaningful all-length case of the full path conjecture, and excludes any unimodal modulus from counterexample searches. The explicit dependence on peak location and rigidity explain quantitatively why interior peaks cannot attain the conjectured constant. This is intrinsic value despite equivalent catalogue coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
