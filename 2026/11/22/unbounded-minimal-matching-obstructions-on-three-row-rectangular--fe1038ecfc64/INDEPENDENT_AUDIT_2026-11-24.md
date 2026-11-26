# Independent mathematical audit

## correctness

PASS

With the spine fixed, each remaining middle-row end can only be matched vertically in its own column. A boundary horizontal edge forces the vertical to the other outer row. The left free intervals (top start, bottom start) then have parity (even, odd) for A and (odd, even) for B; the right ends have parity (odd, even) for A and (even, odd) for B. Opposite parities give even lengths, including any empty row interval; same parities give odd lengths. Hence exactly 8 of the 16 proposed matchings do not extend. Removing one boundary edge permits the compatible vertical at that end. For an A-left/B-right obstruction with d_j removed, column 2j is available in the top even-to-even interval and column 2j+1 in the bottom odd-to-odd interval. Using verticals there splits both intervals into even lengths. For B-left/A-right the rows are exchanged. In each even-to-even interval column 2j lies between the left start 2 and right end at least 2n-2, and in each odd-to-odd interval column 2j+1 lies between the start at most 3 and end 2n-1, which checks both extreme j and n=2. Every one-edge deletion extends, so every proper subset extends. The eight sets are distinct and have n+1 edges, giving eight distinct squarefree minimal generators of that degree, not a complete global enumeration. Replay is by RESULT.md lines 13–33. The attached exhaustive finite solver was inspected, not executed; the proof supplies the all-n result without relying on that solver.

## originality

PASS

Best-of-knowledge pass for the sixteen-pattern boundary classification and the eight minimal obstructions of size n+1 for all n>=2. The same-grid preprint already uses the identical alternating spine and notes that three-edge bad matchings occur. That overlap does not furnish the boundary classifications or a family of unbounded size.

## value

PASS

The theorem exhibits a structural jump from width two, where minimal forbidden patterns have size two, to fixed width three with growing minimal-generator degree. The examples are boundary obstructions along a standard spine; every selected domino matters. This identifies genuinely nonlocal constraints on completion without overstating their global census or maximum size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
