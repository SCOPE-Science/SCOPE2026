# Independent mathematical audit

## correctness

PASS

Vertex switching on nine vertices preserves each cycle sign because every Hamiltonian cycle has degree two at every vertex; fixing eight root-star signs reduces each orbit to 28 internal-edge signs with 256 lifts. Removing the root gives a bijection with the 8!/2=20160 unoriented Hamiltonian paths on eight vertices. I compiled and executed an independently written C++ permutation-reversal encoder and complete 28-stage exact integer Walsh transform across all 268435456 reduced frequencies. Its 38-bin histogram agrees every line with the frozen spectrum_counts.txt: 52179336 zero frequencies, smallest positive |W|=32, largest 20160, reduced nonzero 216256120, exact Parseval sum 5411658792960. Multiplying zero/nonzero by 256 gives the claimed rank/nullity in dimension 2^36; ratio 20160/32=630. The source offers independent forced-path forest contraction and subset-zeta computation; I read and checked its formula H(F)=2^(r-1)(8-t)! for admissible nonempty forced forests and its finite loops (but did not separately rerun this source zeta program). This is exhaustive finite arithmetic, not an infinite statement.

## originality

PASS

Best-of-knowledge originality: actual Resultary searches, relevant published statements and accessible primary text reveal no matching or stronger theorem implying this exact final claim; source-specific residual risks remain, and a search miss is never treated as novelty proof. One null character and sign coexistence do not imply the count 52179336, sharp min positive multiplier 32, or condition 630; all require joint exhaustive signed-count histogram with switching quotient.

## value

PASS

The complete rank defect and smallest surviving singular multiplier of the natural K9 Hamiltonian-cycle edge-orbit convolution are exact invariants of a major finite combinatorial class. An earlier example of one zero at n=9 does not supply the huge exact rank, full spectrum, or sharp recovery gap. The 256-fold switching reduction and independent path-count transform make the nontrivial 2^36 operator spectrum tractable. The result is valuable as a complete natural finite-order spectral census, without pretending to generalize all n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
