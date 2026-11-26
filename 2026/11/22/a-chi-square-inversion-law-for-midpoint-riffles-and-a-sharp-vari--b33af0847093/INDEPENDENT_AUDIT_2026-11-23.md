# Independent mathematical audit

## correctness

PASS

At every nonempty cut, reflecting both midpoint grids changes x and y to 1−x and 1−y. This pairs the strictly inverted and strictly noninverted cross pairs; ties are disjoint, and a tie coin affects only the order of its tied pair. Empty cuts give zero. For odd deck sizes midpoint equality is impossible by parity and the cut masses combine two at a time, since k(n−k) is strictly increasing on the lower half of the cut range. The centered cut W has E(W²)=n/4 and Var(W²)=n(n−1)/8. Total variance gives the stated n(n−1)/32 plus E(T)/4, and T≤n gives L²-negligible coin noise on scale n; the cut CLT gives (1−Z²)/8 with the exact centering. For GSR the label-word probability is 2^(−n) for every word, as the binomial probability of the cut cancels the uniform-interleaving denominator. Expanding the pair count gives the indicated linear weights and centered quadratic term. Odd moments give orthogonality; the sum of squared linear coefficients gives variance n(n²−1)/48, and the quadratic variance is n(n−1)/32. Their sum and the normalized Lindeberg bound give the stated comparison. Independently constructed exact enumeration passed 220 midpoint and 18 GSR checks for sizes 2–10. The frozen checker was read, not run; bounded enumeration is corroboration only.

## originality

PASS

The best-of-knowledge finding is the midpoint inversion distribution and the associated change of scale and limit relative to GSR. The shuffle, tie formula and classical comparator are prior. No covering result for the distinctive midpoint distribution was identified in the inspected material.

## value

PASS

Inversions are a natural quantitative measure of departure from an ordered deck. Holding the entire random cut law fixed isolates the effect of the midpoint interleaver: exact cancellation of all strict within-cut inversion fluctuations leaves only the squared cut fluctuation and smaller tie noise, giving a one-sided limit and a precise order-n reduction in variance compared with GSR. This is useful as an observable distinguishing these two models without claiming a mixing consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
