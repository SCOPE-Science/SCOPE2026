# Independent mathematical audit

## correctness

PASS

Literal scan of all 15 masks (choose(6,4)) and all 2^16 two-by-eight binary arrays gives 12 spanning masks with the identical 64 solutions and three two-column masks with zero solutions. A two-column mask contains both sites in each of its two columns, forcing duplicate all-zero windows on swapping row translation. Exact 16-site, four-bit windows constitute an exhaustive bijection test. Translation orbits of 64 arrays split 16×4; complementation/reversal merge them into two 32-member classes, and row-XOR alternation was independently confirmed. Source's verify_direct.py was read, plus independent clean enumeration of the finite domain.

## originality

PASS

PASS best-of-knowledge: Horan and Stevens study general locating arrays and de Bruijn torus constructions, including connected-tree and cycle criteria, not a complete census of all 2×8 arrays for all 15 literal four-site masks. The 12 masks have identical 64 realizing arrays, including disconnected geometries, a stronger simultaneous exact finite assertion not implied by those construction/existence results.

## value

PASS

The 2×8 torus with sixteen translations and binary four-pixel windows is the natural smallest perfect-location scale (2^4 windows). Classifying every four-site local mask, all successful arrays and their symmetry orbit structure is a motivated complete finite design result, not an arbitrary numerical table. It identifies a universality equivalence across distinct masks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
