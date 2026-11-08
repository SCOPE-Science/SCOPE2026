# Scientific review

## Correctness — PASS

The theorem's quantifiers require integer dimension \(d\ge2\), integer radius \(m\ge1\), and at least two distinct integer parameters in the symmetric interval. Every moment-curve sample point is exposed by \(2t x_1-x_2\); convexity reduces the squared Euclidean diameter to vertex pairs. Same-sign pairs contribute at most \(S_{d,m}\). In odd dimension, paired consecutive coordinates are dominated by the corresponding odd-power endpoint contributions; strictness of the first coordinate gives the unique opposite endpoint pair. In even dimension, the critical pairwise inequality is proved for every integer \(0\le z\le w\le m\): the strict negative cross term when \(0<z<w\) uses \(w\ge z+1\), so the proof does not silently extend to real parameters. Summing the estimate gives exactly the asserted endpoint-zero equality cases. At \(m=1\), direct enumeration of the three available parameters proves the exceptional endpoint-endpoint case. The all-parameter proof is independent of the finite verifier.

The exact-arithmetic verifier successfully checked 46,920 unordered pairs in 240 parameter instances, 736 generated sparse samples, 14,240 direct integer-lemma tests, and 120 rational real-parameter perturbations. This is corroboration, not an infinite certificate.

## Originality — PASS, provisional historical priority

The full accessible texts of Konoike (arXiv:2609.28417v1, Sections 1–2 and Example 2.4) and Fu Liu (arXiv:math/0409337, Introduction and proof sections) were compared against the claimed *Euclidean metric* inequality. They address Ehrhart coefficients, volumes, finite differences, and lattice-point enumeration for the same integral cyclic polytopes. None of their inspected theorems asserts the endpoint extremal distances, the parity-controlled equality set, or the discrete-versus-continuous contrast.

The superficially closest diameter-named article, Maksimenko (2009), concerns the *ridge graph of the dual polytope* and cannot imply the metric theorem. Searches of contemporary mathematical records for integer moment curves, symmetric intervals, Euclidean diameter, furthest-point pairs, and parity showed no equivalent or stronger covering statement. Existing exact Euclidean-diameter results for partial permutohedra and other polytope families use different vertex sets. A missed equivalent geometric statement remains possible and no independent priority audit has been made.

## Mathematical value — PASS

The symmetric integer interval is the simplest normalization where the coordinate powers and parity compete. The result is a complete sharp upper-envelope and equality-pair classification across an infinite two-parameter family **and all sparse integer subsamples**, rather than just a single distance computation. Its even-dimensional extremal pair jumps from opposite endpoints at integer scale one to the endpoint-zero pairs at every larger integer scale; the ratio of endpoint competitor squared distances is \(4/(1+m^2)\). The integer-gap lemma and explicit real perturbation show the transition is genuinely arithmetic, not a consequence of continuous moment-curve monotonicity. The precise equality cases can screen extremal configurations without enumerating all vertex pairs.

## Limits and closest literature

Full-dimensional cyclic polytopes require at least \(d+1\) parameters. For sparse sets omitting extremal pairs, the theorem does not compute their smaller actual diameter. Arbitrary real parameters or coordinate reweightings are outside scope; continuous perturbations can violate the even-dimensional envelope. The record searches do not prove exhaustive historical uniqueness. Key literature: Konoike (2026), Liu (2004), and Maksimenko (2009).

Self-review: passed. Independent audit: not yet performed.
