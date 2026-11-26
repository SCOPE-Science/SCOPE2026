# Independent mathematical audit

## correctness

PASS

For k <= c(lambda), choose k increasing positions outside the prescribed values since 2k <= n. The required arrows are vertex-disjoint two-label blocks. A cycle of size ell accepts any t <= floor(ell/2) such blocks and ell−2t spare labels: allocate within these capacities and close each list cyclically. This works for all cycle sizes and yields the exact word and falling-factorial cell counts. There are no relative cells below dimension c. A nullhomotopy of an i-sphere in the ambient space can be deformed into the common (c−1)-skeleton when i+1 <= c−1 by relative cellular approximation; paths give path connectivity for c >= 2. The ambient wedge theorem was checked in arXiv:1908.03394, Theorem 1.2; reduced homology vanishes in the range with any coefficient group. Each transposition contributes at most one letter to an increasing subsequence. This proves the sharp skeleton cutoff, not sharp connectivity. Reviewer-authored `python3 /workspace/independent_reproduction.py perm` (Python 3.12.3) compared exact word sets through n=8 and longest increasing subsequences over all perfect matchings at n=2,4,6,8,10,12 (10,395 matchings at n=12). The frozen verifier searches for absence only through n=8; its last two printed sharpness lines cover witness construction, not exhaustive absence. The proof does not rely on finite checks.

## originality

PASS

Earlier positive-probability extension of acyclic constraints covers the short-word existence conclusion for types with every part at least k+1, in particular the corresponding range for one long cycle. It does not cover arbitrary short cycles, fixed points, or the uniform capacity and its exact involution boundary. No equivalent or dominating result for the combined general statement was identified in the inspected sources. The ambient theorem and the elementary direction of the involution obstruction are not claimed as separate innovations.

## value

PASS

A computable cycle-type condition controls every exact-letter cell in a growing range and gives nontrivial integral and homotopical connectivity in a naturally defined family. The bound works with a mix of long and short parts and provides a sharp skeletal cutoff for an infinite class, rather than extrapolating a finite homology census. It does not determine higher groups or claim that the connectivity bound is sharp.

The dated certificate retains the supplied scientific assessment, sources and limitations.
