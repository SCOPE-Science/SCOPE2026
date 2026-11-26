# Independent mathematical audit

## correctness

PASS

A cyclic word with all five-bit windows gives an Euler tour of the directed overlap graph; the first bits of the consecutive edges recover the word. The unique 00000 edge fixes the rotation, so the edge search counts each labelled necklace once and uses no reversal or complement quotient. Each tour also gives a bijection of the two arrivals and two departures at each of the 16 vertices, and conversely a choice of these bijections giving a single 32-edge orbit is a tour. Thus both searches exhaust the intended class. In each linear cut, a partition ends in some nonempty palindromic suffix, so prefix optimum plus one minimized over suffix starts is exact. Center-ordered updates are valid because any palindrome in a partition of the prefix before the one currently being processed ends strictly before the current palindrome starts. Fresh bounded code independently compared both cycle searches and both palindrome calculations on all 65536 roots. It reproduced the seven rooted frequencies 384,3554,18266,29118,12138,2030,46 in order from 4 through 10, the 14 joint min–max cells summing to 2048, and both canonical minimum-nine strings, each with 29 cuts of length nine and 3 of length ten and exchanged by bit complement up to rotation. All joint cells have unequal minimum and maximum; the first table is the histogram of optimal partitions of individual cuts, not the histogram of minima over a cycle. Replay: python3 /workspace/branches/d2257b3c-59e3-428d-9843-dc1da9c0d978/independent_recheck.py, with full.json and smoke.json in that directory. The original verify.py and its reported output were read, not executed. This is an exhaustive result for order five only.

## originality

FAIL

A distinct indexed Resultary record explicitly gives the same 7 rooted and 14 joint cells and names the same two extremal necklaces on exactly the same input family. Its circular-optimum wording is equivalent to minimizing the linear optimum over all cuts, and its additional circular histogram is the marginal of the joint table. The catalogue path has a later calendar label; this assessment is about demonstrable matching coverage and not an inference about which result came first, provenance, or who discovered it. The two exception-specific 29/3 cut splits were not established as printed in the match, but are immediate tallies at its already identified extremes using its same exhaustive per-cut calculation; they do not make the frozen census distinct.

## value

FAIL

An exhaustive finite benchmark of how palindromic length varies with the cut on de Bruijn cycles is mathematically meaningful in itself. Here the benchmark, cut sensitivity and sharp extremal necklaces are already supplied by the matched record. The residual multiplicity detail on two known necklaces is a small readout of their existing per-cut optimum calculation with no separate mathematical question or demonstrated need. Correct and reproducible does not make this a distinct valuable census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
