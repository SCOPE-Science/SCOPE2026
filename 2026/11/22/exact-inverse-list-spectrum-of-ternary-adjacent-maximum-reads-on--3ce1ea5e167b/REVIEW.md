# Independent mathematical audit

## correctness

PASS

For the linear indexed proper-source map in RESULT.md lines 5–39, partition the source symbols into the low class {0,1} and the high class {2}. Read 1 is a low-to-low step whose endpoints alternate 0 and 1; read 2 switches classes. Once a read 1 is present it forces the two classes there and consequently throughout the word. Thus every internal run of 2s must be even and the outside runs are unrestricted. Each stretch of consecutive low sites has two choices of its first low symbol and all subsequent low choices there are forced. Every internal pair of 2s introduces one more such low stretch, and each outside run of length r adds floor(r/2) stretches; equivalently the two equal low endpoint counts and the high count transform by (a,b)↦(a,0) or (b,2a), and squaring the 2 transition multiplies both counts by 2. This proves the formula, including infeasibility and the factor two for reduced boundary cases. For 2^m the two alternating class patterns have free low symbols, giving 3·2^{m/2} for even m and 2^{(m+3)/2} for odd m. An outside run contributes (1+z)/(1−uz²), an inside run 1/(1−uz²); summing the factors for one or more reads 1 gives the claimed histogram series. At u=1 add all-2 words to obtain 1/((1−z)(1−z−z²)), hence F_{m+3}−1. One representative per nonempty fiber realizes this exact zero-error size. A fiber with a 1 cannot exceed 2^{1+floor((m−1)/2)}, strictly below the all-2 value. The minimum occurs when every run of 2 has length at most one, leaving only optional single 2s at the ends, with the stated m=1,2 boundary counts. Summing sizes counts the 3·2^m sources. At m=3 the histogram is one empty, four of size 2, two of size 4 and one of size 8. The frozen VERIFICATION.md and verify.py were inspected, not executed: the script compares full direct histograms and extrema through m=14; the loop through m=100 checks coefficients, mass and image totals rather than independently enumerating fibers or extrema at those lengths. The all-length derivation does not rely on those diagnostics.

## originality

PASS

Credit is limited to this channel's explicit finite preimage law and histogram (including the exceptional all-2 fiber), with their concrete extrema and code implications. The output language itself is the classical even shift at finite lengths and its total word counts are already known. The statement does not claim priority for that language, the Fibonacci sequence, generic graph counting or generic sliding-block coding.

## value

PASS

A proper ternary source and overlapping positional maximum form a natural small deterministic channel that loses distinctions between low symbols. Identifying a known even-shift image alone would only give its size. The weighted classification instead answers exactly how much ambiguity remains for each read and why the all-maximum read is exceptional, with sharp finite benchmarks for injective coding. This delivers an exact invariant of the specified channel, not a new Fibonacci sequence or a claim about a physical sensor.

The dated certificate retains the supplied scientific assessment, sources and limitations.
