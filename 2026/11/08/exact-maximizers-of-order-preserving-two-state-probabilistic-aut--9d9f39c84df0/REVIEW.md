# Scientific review

## Correctness — PASS
The state-1 mass of a two-state PFA obeys a one-dimensional affine update. A nonnegative transition determinant makes every update nondecreasing. Greedy maximization/minimization then yields a monotone orbit and a monotone sequence of active-line slopes, forcing distinct constant runs. Conversely, the specified rational lines have strictly increasing slopes and ordered crossing thresholds between consecutive baseline states; the quantitative perturbation bound is smaller than half the minimum baseline spacing. Every desired run is therefore the unique greedy choice. All transition endpoints lie strictly inside the unit interval. The counting formula follows by choosing an injective sequence of run labels and a composition of length. The standalone rational checker passed finite independent checks; the proof covers all lengths and alphabets.

## Originality — PASS against inspected evidence
Gill (arXiv:2402.13376, Theorem 4.1 and §4.4) classifies unrestricted binary witnesses and discusses enlargement of the ambient alphabet, which does not imply this all-alphabet order-preserving two-state classification. Kjos-Hanssen (arXiv:2607.26275) proves the universal three-state result and introduces an explicit affine construction but does not state the restricted two-state classification in the inspected material. Index, primary-source, and historical-claim searches located no equivalent statement or stronger theorem implying it. Residual risk: an older source on affine control/envelope dynamics could implicitly contain the argument; accessible later sections of the 2026 paper could not all be re-opened.

## Value — PASS
This is a complete structural classification for a natural restriction of probabilistic automata, with a concrete positive rational witness for every admitted word. It answers a precise multiletter state-minimization question outside the binary-only classification, and its exact formula exposes polynomial rather than exponential growth in the number of uniquely isolatable words for fixed alphabet size. The restriction is essential: arbitrary two-state PFAs may have negative-determinant transitions and exhibit alternating maximizers.

Self-review: passed. Independent audit: not yet performed.
