# Independent mathematical audit

## correctness

PASS

Rule 178 flips a site iff it has a different neighbor, including the fixed exterior zero at each endpoint. Both ends of an interior wall therefore flip and the wall persists. Inside a run with two interior walls, the end cells flip while the interior cells stay, reducing the central run length by two per step. The odd run ends without an equal pair; an even run leaves a pair whose cells flip together forever between persistent walls. At a path endpoint the behavior is different: a zero run erodes one cell at a time from its interior wall, while a one run initially erodes from both ends. Boundary one runs of length one leave no equal pair and length two transiently becomes boundary zeros; lengths at least three leave a two-wall core of length r−2, bad precisely for even r. The uniform zero word is fixed; the uniform one word erodes from both exterior zeros and enters iff n is odd. Full interior wall occupancy is exactly the two alternating words and each maps to the other. More generally a nonzero word eventually oscillates: every nonuniform word has a permanent wall, the finite wall vector stabilizes, and once stable the word must complement each step; uniform ones for n≥3 becomes nonuniform. To count the target basin, opposite boundary colours contribute 2AR times the even geometric series in O; same colours contribute (A²+R²)O times that series; add O for uniform odd ones. Independently expanding gives the displayed rational function. An equivalent series is 2(2−z)/(1−z−z²)−2/(1−z)+z⁷(1−z²)/(1−3z²+z⁴)−2+z−2z²+z³+z⁵, which directly checks the small exceptions and the odd-index Fibonacci shift n−6. Binet's formulas give the displayed parity constants for B_n/φ^n and division by 2^n gives the basin probability.

## originality

PASS

Qualified for the explicit selected-basin enumeration and its parity law. The local erosion mechanism and the existence, number and periods of attractors are not claimed as new. The closest same-boundary historical paper is an access-limited priority risk; the independent comparison does not certify noncoverage of that paper's uninspected Section 3.35.

## value

PASS

The fully alternating cycle is selected by a natural extremal property—every interior edge is a wall—and its basin population is an independently meaningful statistic even without a full basin census. The model has almost all words ending in period two, yet this particular oscillator has exponentially small selection probability with different parity constants. The boundary exception and the parity correction cannot be inferred from the stated prior attractor counts or bulk erosion alone. No claim is made that this is the largest basin or that these formulas extend to a different update or boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
