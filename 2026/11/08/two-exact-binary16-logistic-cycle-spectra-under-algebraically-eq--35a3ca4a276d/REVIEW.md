# Independent mathematical audit

## correctness

PASS

The domain comprises precisely unsigned encodings 0x0000..0x3c00 (15361 states), each represented by exact integer 2^24 x. The nearest-even binary16 rounding rule is reconstructed from adjacent scaled integers and ties to even; signed 2x−1 can be squared by absolute value. Independently calculated all 15361 successors for both F and G using a separate exact-integer grid/rounding implementation, traversed each full functional graph, obtained cycles F [(1,15236),(1,8),(5,117)] with max 109 and G [(1,15048),(1,3),(8,310)] with max 70, and exactly 12513 different outgoing edges. SHA-256 of little-endian complete edge arrays F=262e0316d1e5e82c3b1c694ecde3dde9b8c6a8a24956d407f6b6b008c2d116af; G=e065cfc9bbb55cbf264c7517149dbf2a3a6dae7d7f89b00f2dc0502fc9b6dac0, both match frozen CENSUS.json. An exhaustive finite graph proof applies only to these exact finite maps, not real logistic chaos.

## originality

PASS

Best of knowledge: the once-rounded F census is fully pre-existing and not claimed new. The completed-square staged rounding G eight-cycle and complete 310/15048/3 basins, together with the 12513-edge F/G comparison, are separate mathematically defined finite invariants not implied by the inspected previous exact tables.

## value

PASS

Finite-precision chaotic maps depend sharply on arithmetic-expression evaluation. The completed-square binary16 functional graph is a natural reproducible exact invariant for numerical dynamics, with its eight-cycle and 310-state basin differing sharply from the already known five-cycle/117-basin once-rounded graph. This exact comparison is useful even without a precision-asymptotic theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
