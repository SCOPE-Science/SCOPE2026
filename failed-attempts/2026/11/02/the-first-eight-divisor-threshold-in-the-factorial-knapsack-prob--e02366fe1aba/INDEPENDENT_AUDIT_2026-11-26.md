# Independent mathematical audit

## correctness

PASS

Recomputed the whole finite domain independently (python3 /tmp/opencode/factorial_review_exhaust.py {1..12}). Enumerated divisors by integer factor pairs up to the square root. Maintained at-most-k reachability directly, initialized with zero in every layer, and updated layers downward with the union of the old layer and the old next-lower layer shifted by the current divisor. This encodes exactly the two choices to omit or include that divisor once. Positive summands justify discarding sums above N. The first full layer and the complement size in the preceding layer reproduced all twelve rows, including the n=1 boundary; zero is always covered. At 12!, all 792 divisors were processed and all 479001601 positions were covered at layer 8. The layer-7 complement was read in ascending order and matched EXTREMAL_TARGETS.json entry by entry. Its 175 targets are odd and have endpoints 475785157 and 479001547. The frozen C++ cross-check only treats n=8 through 11 and is not needed for that final comparison. No result for n≥13 follows.

## originality

FAIL

The earlier Resultary record 034373a7dea0 explicitly gives the same exact profile and counts, the first threshold at 12!, and the complete 175-element exceptional layer. Its accompanying sorted list has the stated endpoints and consists solely of odd targets. This is direct coverage of the scientific finding, not an inference from an inaccessible classical text or from a matching threshold alone.

## value

FAIL

The first eight-divisor boundary and its complete obstruction set are meaningful objects for this classical invariant. But the frozen work recomputes an already available exact table and list, with the oddness read off that list. It provides no new arithmetic explanation, additional threshold, or other substantive scientific remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
