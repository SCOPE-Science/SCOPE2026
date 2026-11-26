# Independent mathematical audit

## correctness

PASS

Pinned the primary source to arXiv:1407.2966v1 as explicitly cited. Unlike a later version with shorter Klein coverage, v1 §4.1 pp. 9–10 actually prints all 21 line triples, the 21 quadruple and 28 triple coordinates, and the 21×49 incidence array. Independently extracted the first 21 columns and compared the 21 sorted line blocks: all agree with /workspace/reproduction/klein_check.log, whose implementation reconstructs the intersections at both roots modulo a large split prime. Since a projective equality test is a reduced linear polynomial in a with tiny integer coefficients compared to that prime, equality at both distinct roots certifies the characteristic-zero projective classes. Gévay–Pokora §2.1 independently prints the same line and point coordinates. The incidence gives 4-regularity on both parts and 84 edges; the exact characteristic polynomial has zero with multiplicity one, proving connectedness and cycle rank 43. Independently computed an exact reduced determinant of 1426415078790162284544 and modular ranks 24,34,36,35 at 2,3,7,23 respectively. The determinant exponents 18,7,5,6 with rank deficiencies 17,7,5,6 force at 2 sixteen valuations 1 and one 2, and at each other prime only valuations 1 among the nonunit local factors. Reassembling sorted valuations gives 24 units, ten 2s, 6, 138, four 966s, and 1932. This is independent of a direct Smith implementation. The stable-curve application uses a separate graph realization of rational components, four marked points each, so it is stable and has genus 43. The critical-group identification is conditional on regular semistable smoothing with unit thickness; no incorrect identification with just a partial plane blow-up is needed.

## originality

PASS

The configuration, table and real incidence-equivalent realization are prior. The checked distinct records concern different Klein incidence graphs or larger boundaries, and the inspected passages for the exact configuration supply geometry and incidence rather than its critical group. The supported distinct claim is the integral invariant of this precise 42-vertex graph and its conditional application.

## value

PASS

This is the full torsion group of a canonical quartic-related incidence graph, not a fit to numerical data or a graph chosen for easy Smith forms. The precise 2-primary exponent and 23-primary multiplicity refine known incidence data and determine the geometric component group in the natural genus-43 unit-thickness nodal realization. The restricted quadruple graph is geometrically distinguished and the full boundary's group cannot stand in for it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
