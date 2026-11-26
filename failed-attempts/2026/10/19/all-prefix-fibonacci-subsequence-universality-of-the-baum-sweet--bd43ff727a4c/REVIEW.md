# Independent mathematical audit

## correctness

PASS

For n>0 with b(n)=1, incrementing n either shortens a terminal even zero run by one or, at the carry through terminal ones, shortens the preceding even zero run by one. The sole surviving case is an all-ones expansion of even length, plus the pair at zero. Greedy arches characterize the universality index: one symbol can be taken from each arch; the sequence of arch-ending symbols followed by a symbol missing from the tail fails even under earliest-position matching. After 110|110|01 the count is three arches for five ones. The initial next bit b(8) is zero. For j>=2 the adjacent pair ends at 4^j and the two following bits are zero: 4^j+1 has a zero run of length 2j-1, and 4^j+2 has a final zero run of length one. The second zero is the elementary detail needed after the arch that consumes the first zero after a pair, so later isolated ones resume closing arches with a zero already seen. Thus the one extra unfinished contribution occurs exactly at the specified cutoffs. The dyadic count follows by tiling the suffix after the leading 1 by tokens 1 and 00, including the separate zero index; the Fibonacci summation and initial list agree.

## originality

FAIL

A distinct indexed Resultary record dated 2026/10/12 states the same all-prefix formula under the same indexing, actually extending the uniform range to N>=4. It also gives the claimed dyadic counts over wider ranges. This is demonstrated equivalent/stronger coverage, not a negative inference from general arch theory or a search failure. The catalogue dates are not used to infer publication provenance.

## value

FAIL

The exact all-prefix invariant and its sparse exceptional set are mathematically meaningful in themselves, but this record repeats a stronger indexed result. The alternate digit-carry verification is elementary and does not supply a separately established structural or computational contribution beyond that coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
