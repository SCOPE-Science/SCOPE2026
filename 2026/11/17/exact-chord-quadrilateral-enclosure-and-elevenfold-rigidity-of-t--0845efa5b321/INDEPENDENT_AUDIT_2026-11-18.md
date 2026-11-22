# Independent mathematical audit

## correctness

PASS

Reconstructed chord-direction reduction: regular P11 chords have oriented outward normals n_k at k*pi/11 for k mod22; h_k=1 at even k and cos(pi/11) at odd k. Translating four enclosing lines inward to supports never increases area. A bounded support intersection requires each cyclic normal gap <11. The support-length/area formula sums [h_i*h_j-(h_i^2+h_j^2)cos(g*pi/11)/2]/sin(g*pi/11) around the polygon, allowing zero length edges; redundant even support constrained by adjacent odd supports is treated as three-support case. Inspected complete chord11_checker.py blob 77bcd8380a7da40e600f3e2edb0e37fa8912dd41: rational enclosing intervals for pi (Machin alternating series) and sin/cos (Taylor remainders), fixed scale 10^28, all 3674 bounded nonredundant four-normal sets, 330 bounded triangles, 11 redundant fours, exact strict >0.008 margin for every nonwinner. Independently enumerated all admissible index sets in floats, reproducing 3674,330,11, eleven rotated winners with next gap 0.008464051366; float check is only diagnostic, not a certificate. The eleven winners have all odd normals with gaps (4,6,6,6), hence area cos^2(pi/11)*(tan(2pi/11)+3tan(3pi/11)); proof strictly distinguishes saturated discrete gap from arbitrary translated quadrilaterals.

## originality

PASS

Best-of-knowledge no exact P11 chord-restricted enclosing quadrilateral and full elevenfold equality classification found in inspected published sources. Full heptagon and nonagon papers give natural analogous finite instances, but do not imply P11 values/optimizer symmetry, and the nonagon requires one diagonal direction unlike P11 all-edge winners. Vígh (2026) treats general conjectural enclosure bounds; its complete full text could not be lawfully obtained, so potential detailed P11 discussion remains an explicit priority risk.

## value

PASS

The regular hendecagon is a natural fixed-input benchmark in the established chord-quadrilateral enclosure problem. Exact optimum and all eleven optimizer directions, with a rigorous discrete positive gap and the return to edge-only support after the nonagon diagonal phase, classify a meaningful finite invariant and its structural combinatorics. It is valuable as a sharp small-n test even without an all-n quadrilateral theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
