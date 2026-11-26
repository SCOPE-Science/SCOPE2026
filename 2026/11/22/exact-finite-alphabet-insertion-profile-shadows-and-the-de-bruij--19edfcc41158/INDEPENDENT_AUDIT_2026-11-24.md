# Independent mathematical audit

## correctness

PASS

Subtracting the fixed source profile reduces equality to equality of increments. If the inserted symbol equals either letter bordering an interior gap, exactly a unit loop remains, and the loops realized this way or at endpoints are precisely those of present symbols. Otherwise the three coordinates are distinct and the sole negative coordinate identifies the old bigram. For an old nonloop ab only the positive coordinate starting with a can be ax; for aa the two positive coordinates are ax and xa, which also uniquely recover x. The endpoint nonloop sets intersect in exactly the coordinate w_n w_1 when the endpoints differ, and otherwise do not intersect. This includes n=1, where there are no interior gaps. For q>=3 each incidence coefficient is strictly positive, so maximizing requires full bigram support and equal endpoints. At minimum length there are exactly q^2 gaps between letters and the bigrams form an Euler tour; the complete directed graph with loops admits one. With a particular starting edge fixed, BEST gives q^(q-2)*((q-1)!)^q tours by Cayley arborescences and local orders; all q^2 rotations give different indexed words because every edge appears once. This gives (q!)^q. For n>=2 endpoint equality has probability 1/q; maximality differs from that event only if some bigram is absent. Independent disjoint adjacent blocks bound each absence probability and a union bound gives the displayed estimate. Independent literal profile enumeration over all 59,049 ternary length-10 inputs (1,948,617 insertion operations) confirmed the formula and found exactly 216 maximizers of size 19.

## originality

PASS

The binary law and the Euler-tour count are expressly old. The supported distinct finding is the complete nonbinary one-insertion profile formula, whose positive oriented-nonloop term gives the sharp insertion capacity and forces shortest maximizers to be de Bruijn linearizations. Neither the inspected general edit coding result, the exact binary law, nor the neighboring deletion and substitution results supply that term and consequence in this channel.

## value

PASS

The statistic answers a natural ambiguity question after loss of global order in a bigram-profile channel. Counting insertion sites alone cannot provide it. The oriented nonloop term is visible only beyond binary and makes full directed bigram coverage a necessary extremal property. It gives a sharp capacity, the exact saturation onset and a structural characterization of all shortest witnesses, together with a simple finite-length bound toward the random-word limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
