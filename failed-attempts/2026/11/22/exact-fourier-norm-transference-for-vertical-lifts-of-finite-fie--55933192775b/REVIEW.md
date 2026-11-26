# Independent mathematical audit

## correctness

PASS

The vertical decomposition is unique; factoring the canonical trace-character sum gives the claimed multiset. For v nonzero, squaring the Gauss sum and substituting (x−y,x+y) gives q by orthogonality, since the trace pairing is nondegenerate. At v=0 only u=0 survives. The complex endpoint matrix norms are the absolute row/column sums of q^(−2) times the character sum. Independently, for a fixed common first-coordinate sum t, the difference of the sums of squares is 2(x−x′)(x+x′−t). The affine map to these factors is invertible in odd characteristic, so each nonzero prescribed difference has q−1 solutions and zero has 2q−1. Counting the fiber quadruples and summing over t gives q(q−1)|H|^4+q²E(H). For two fibers, the trace of vη covers each prime-field value q/p times; twice the symmetric cosine sum over residues −(p−1)/2,…,(p−1)/2 equals 2 csc(π/(2p)) by the finite geometric series. No odd-order root is −1, and the three distinct pair sums of a two-point set have multiplicities 1,2,1. These facts give the stated special norm, zeros, energy, and limits after division by the singleton norm. Independent Python replay /workspace/replay/audit_1.py checked the exact squared multiset and pair energy for all 511 nonempty GF(9) fibers (every two-point case has energy 1638 and eight zeros). This finite check supplements the proof. Reproducibility caveat: the frozen checker would print a counter of 100, but its prime-field loop increments by three even on singleton, three-point and full fibers, which have only two assertions. There are 82 comparison assertions by inspection, including repetitions; the counter does not certify 100 independent comparisons. No theorem depends on that count.

## originality

FAIL

No retrieved source was shown to print the full package verbatim. The claim is nevertheless covered as a direct combination of the known one-parabola spectrum with the Fourier product rule for vertical convolution, the standard endpoint and fourth-moment formulas, and, for the two-point specialization, the standard two-phase cosine calculation already used in close prior work. The arbitrary fiber is a pointwise multiplier, not a new spectral computation or a solution of the remaining one-dimensional norm problem.

## value

FAIL

The formulas are a convenient worked example, but the lift makes the spectrum a direct product with the known Gauss magnitudes and leaves the substantive arbitrary-fiber invariant as an unevaluated one-dimensional norm. Restricting to two points only inserts a standard trace average and a three-value pair-sum census; neither the endpoint constant nor the energy resolves a nontrivial remaining case of the fiber problem. No independently valuable remainder requiring a repair was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
