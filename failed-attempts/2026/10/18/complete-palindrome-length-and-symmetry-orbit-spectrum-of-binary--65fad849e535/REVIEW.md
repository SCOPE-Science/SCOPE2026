# Independent mathematical audit

## correctness

PASS

The finite search is exhaustive: a canonical rotation has its unique all-zero length-five window first; following the successive five-bit windows gives a directed Hamiltonian cycle of the shift graph on the 32 distinct windows. Conversely every such tour starting with 0 and closing back to 0 spells one canonical cycle by reading leading bits. An independent exact search in /workspace/review-checks/debruijn5.py used this state graph, tracked visited windows, checked closure, and tested each circular substring against the corresponding substring of the reversed doubled word. It produced all eight rows of the frozen cycle and orbit-size table, the total 2048 cycles and 528 orbits (32 size-two, 496 size-four, none size-one), and both extremal witnesses and their exhibited palindromes. The computation also found exactly 64 reverse-complement-fixed rotation classes; neither reversal nor complement alone fixes a class. A palindrome is tested by literal reversal, never reverse-complement, and all starts and lengths up to 32 are included. Distinctness of the unique five-zero factor forces a one on either side, giving a separate analytic lower bound of seven. The frozen script was inspected, not executed.

## originality

FAIL

The distinct indexed joint census 8196e282ed1c states the identical maximum-length distribution and provides a per-word exact table containing both canonical cycle_bits and longest. Its stronger table mechanically supplies even the frozen symmetry refinement: for each row, test the three involutions modulo rotation, take the resulting orbit size and group by the already tabulated longest column. The joint paper does not print this grouping, but no additional palindrome calculation, cycle enumeration or mathematical criterion is needed. This is a judgment of coverage in the present indexed corpus, not attribution of priority; the covering record's displayed date is later.

## value

FAIL

In the absence of the published inventory, the order-five symmetry-sensitive census would represent a reasonable finite benchmark. As a distinct result now, the longest-length table is already present and the remaining orbit-size split is a routine grouping of known canonical words and their tabulated values. Merely retaining that split would repackage the existing census rather than establish a non-mechanically-implied exact invariant or a new structural theorem about palindromes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
