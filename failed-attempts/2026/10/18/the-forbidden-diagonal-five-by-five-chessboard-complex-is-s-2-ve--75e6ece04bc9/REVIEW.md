# Independent mathematical audit

## correctness

PASS

A fresh tuple-based enumeration gave face counts 20,130,320,265,44. The prescribed sequence gives 382 discrete-Morse pairs, one critical vertex, one critical 2-cell and thirteen critical 3-cells; an independent topological sort visited all 779 nonempty faces with all 2,500 incidences. Fraction-free integer elimination gave rational ranks 19,111,208,44, so b_3=13. The only possible nonzero Morse CW differential is the integer row from the thirteen 3-cells into the single 2-cell. Its rational rank is zero, hence it vanishes integrally. The two-skeleton is S²; each attaching map has degree zero and is nullhomotopic. This proves the wedge, not just its homology.

## originality

FAIL

The advertised wedge is true but is a routine consequence of published results for the very same ordinary complex, not just a match to a nearby complex. In Shareshian–Wachs §8, Theorem 8.1 gives simple connectivity at n=5 (nu_10=2), and Table 8.1 explicitly gives integral H_2=Z, attributing both to Björner–Welker. Every 4-simplex has free 3-faces: a four-rook matching has at most one possible completion to five rooks. Collapsing each 4-simplex along one such face leaves a simply connected 3-complex. Inclusion–exclusion over forbidden diagonal squares gives the f-vector and chi=−11, hence H_3=Z^13 because it is a subgroup of the free top chain group. Choose a sphere representing the H_2 generator by Hurewicz. The pair of the complex and this sphere (included by mapping cylinder) is 2-connected; relative Hurewicz and the homotopy exact sequence give a surjection pi_3(X) onto H_3(X), since pi_2(S²) maps isomorphically onto pi_2(X). Representatives of an H_3 basis and the H_2 sphere give a homology equivalence from the asserted wedge, and simple connectivity gives a homotopy equivalence. Thus the exact homotopy result follows from the existing table and connectivity theorem by a free-face observation, elementary counting and standard topology. This is an implication judgment, not an assertion that the old paper prints the wedge verbatim.

## value

FAIL

The board and its comparison with full-board torsion are mathematically natural, but the changed bottom group was already tabulated. The remaining exact wedge classification follows mechanically from the same board's published connectivity, routine enumeration, and standard topology as above. An independent computational certificate confirms it but does not supply a surviving distinct mathematical invariant, general theorem, or equivariant refinement in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
