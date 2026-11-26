# Independent mathematical audit

## correctness

PASS

Each nonconstant target needs a distinct exact length-two center with equal flanking letters; constant targets need separate runs of length at least four. The run surplus is therefore at least q(q-1)+3q. Each edge in the cyclic skeleton must support both opposing backtracks, which requires at least three occurrences unless the skeleton is a whole two-run circle. That exception is impossible even for q=2, whose dedicated runs require at least four. The skeleton's degrees are even, forcing q/2 extra edges for even q, and attaining that bound gives exactly a matching. The proposed Euler expansion triples the first traversal of each edge without merging neighboring runs, gives separate center runs and leaves an original occurrence per symbol for its long run. This proves equality and all asserted profiles. Equality in the surplus bound forces all other runs to be singletons and the designated long runs to have length four. Independently reproduced the binary and ternary minima with exact subset DP on cyclic orders of chosen target starts and proper suffix-prefix overlaps, and checked both printed examples directly.

## originality

FAIL

The all-q minimum formula is an exact statement match in the indexed ordinary length-four result. The extra length-four signature is not explicitly stated there, but every component follows directly from the length-three indexed minimum and the equality cases of its loop and transition counts by a reversible change in designated run lengths. This is demonstrable indexed coverage, not a determination of which result was obtained first or a claim of external publication priority.

## value

FAIL

The natural cover problem and the matching obstruction are meaningful, and the frozen proof is valid. As a standalone finding, however, the length computation is exactly covered and the profile is inherited from the length-three optimum by a one-letter edit at each otherwise forced run. The exact required excess and the run signature are immediate once those counts are saturated. No independent new extremal obstruction or classification survives this comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
