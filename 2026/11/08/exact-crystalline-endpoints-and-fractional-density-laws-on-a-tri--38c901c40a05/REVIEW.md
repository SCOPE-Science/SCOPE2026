# Independent mathematical audit

## correctness

PASS

The graph has n>=4 cyclic rungs, vertical/horizontal edges and one lower-to-next-upper diagonal. State alphabet 0,A,B, allowed neighboring transitions, and the stated domination constraints at empty center produce exactly the displayed six pair states and 10 allowed edges. Independently constructed characteristic determinant t[t^5-2zt^3-z^2t^2-z^2t-z^2], with cycle weights z on occupied new columns; Z_n=tr(T^n) follows from closed-walk bijection. Checked each of 10 edges against both integer potential inequalities, giving |I|>=ceil(2n/5) and <=floor(2n/3). Equality cycles are uniquely periods five and three, with 5/3 shifts when divisibility permits; concatenations of 2-, 3-, 5-cycles attain rounded bounds for all n>=4. Positive-activity transfer is irreducible with 2- and 3-cycles, so primitive; simple positive Perron root is analytic. Implicit function theorem in z^(1/5) and z^(-1/3), respectively, produces the claimed root and density coefficients 2/5,2/25,2/3,-2/9. Independently enumerated all vertex subsets for n=4..10, compared exact Z_n polynomials and bounds; finite check corroborates, not proves infinite n.

## originality

PASS

The best-of-knowledge comparison finds no result deriving the exact maximal-independent-set partition recurrence, every-period sharp occupancy bounds/multiplicities, or the 1/5 and 1/3 fractional activity corrections for the specific two-row triangular strip with a single oriented diagonal. Wang–Barg–Kashyap work on full 2D triangular lattice, whose local geometry has six neighbors per site and whose periodic ground-state density bounds 1/7..1/3 per SITE; they do not logically determine this degree-three/four finite-width strip or its 6-state transfer. Barg–He–Wang give broad conditions for crystalline phase coexistence on periodic lattices, not explicit formulas for this finite-width strip; only abstract material was accessible for that second paper, retained as priority risk. General Perron/transfer-matrix methods are credited, not claimed novel.

## value

PASS

A width-two oriented triangular strip is a canonical exactly solvable finite-width specialization of the maximal hard-core lattice gas; occupation endpoints, equality multiplicities, and exact partition polynomial form a complete natural classification, not an arbitrary slice. The distinct sparse/dense commensurate patterns and z^(1/5),z^(-1/3) endpoint susceptibility corrections are precise benchmark invariants for constrained statistical mechanics and clarify finite-width analytic crossover versus planar coexistence. These specific answers are not implied by the generic transfer-matrix method alone without a new local-state analysis. No paper-sized general theorem is required for this self-contained exact family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
