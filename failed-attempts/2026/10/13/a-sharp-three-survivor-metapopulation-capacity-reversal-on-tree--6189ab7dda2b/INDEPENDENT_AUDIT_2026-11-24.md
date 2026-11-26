# Independent mathematical audit

## correctness

PASS

For each induced three-vertex forest with j edges, the adjacency characteristic polynomial is t³−jt, so capacity is 0, 1, or sqrt(2). The two-edge count is W, and summing edge incidences gives one-edge count (n−1)(n−2)−2W; subtraction gives the zero-edge count. Dividing by the uniform subset count is the specified conditional law. Setting a_v=deg(v)−1 gives sum a_v=n−2, and W=(sum a_v²+n−2)/2. At its minimum a_v is 0 or 1 for every v (path); at its maximum all excess is at one vertex (star). The low-threshold probability and mean strictly decrease with W, the high-threshold probability strictly increases, and strict comparison omits capacity 1 at delta=1 and all capacities at delta=sqrt(2). At n=4 the two distinct wedge counts give the quoted probabilities. For one survivor the capacity is zero; for two, the edge probability is 2/n for every tree. The theorem is conditional on uniform retention in an unweighted tree and uses a deterministic spectral proxy, not a stochastic persistence probability. Replay: python3 -B /workspace/branches/frozen_math_replay.py (capacity; SymPy for the three characteristic polynomials). Independent edge-subset/connectivity enumeration checked all labeled trees on 4, 5 and 6 vertices (16, 125, 1296); it is corroboration only. Frozen verify.py was inspected, not executed.

## originality

FAIL

The graph statistic and its strict optimizing trees are exact prior results: the count of pairs of incident edges is M1/2−m, and Theorem 1 of Gutman–Das identifies the unique tree extrema of M1. In a tree the induced two-edge triple and incident pair are in bijection. The rest of the law is fixed by the edge incidence total and the three possible three-vertex forests. The stated threshold, mean optima and minimum census are direct translations of that coverage, not a new tree-extremal or spectral law requiring another structural result. The ecological phrasing is not asserted to appear in the Zagreb-index paper.

## value

FAIL

The survival proxy is motivated and the distinction between mean and exceedance is valid, but in the fixed three-survivor unweighted-tree setting it adds only a translation of an established invariant and its extremizers. The three tiny spectra turn the objectives into affine functions of the same known wedge count; neither the optimizer reversal nor the census observation requires a new structural fact. The result could be a useful illustration or benchmark, but not an independently valuable exact finding at this scope. No remaining claim is rescued by rewording.

The dated certificate retains the supplied scientific assessment, sources and limitations.
