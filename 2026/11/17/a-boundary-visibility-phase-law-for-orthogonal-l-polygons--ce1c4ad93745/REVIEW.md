# Independent mathematical audit

## correctness

PASS

Decomposed the six boundary edges into right/lower group H, upper/left group V, and left/bottom remainder. Only opposite-group pairs can be blocked; their line segment crosses the excluded northeast notch exactly when ad>bc, as follows by comparing horizontal y=B and vertical x=C crossing times. Direct elementary integration over the four nonconstant edge-pair products plus the automatically blocked baseline 3AD+AC+BD gives the two stated logarithmic branches of J. The ordered pair probability is 2J/[2(A+B+C+D)]^2, strictly in (0,1/2) because the blocked set is a strict subset of opposite-group pairs. Independently expanded both rational-log branches with SymPy, confirming their common first jet at AD=BC and transverse second derivative difference -D(C-D)^2/(BC^2); for A=D=1-t,B=C=t verified J(1/2)=7/4, fourth derivative difference 1024 and visibility jump -128 with matching derivatives through order 3. The symbolic equalities support the all-parameter integral proof; Monte Carlo checker is not relied on as a continuum proof.

## originality

PASS

The exact related four-parameter notched parallelogram theorem is for two-dimensional AREA-uniform endpoints and derives a different affine-invariant Beer index; the audited measure is one-dimensional arclength on six edges and is singular relative to area, so its exact law and C1/C3 cusps are not specializations. García-Pelayo treats lines sampled by invariant line measures, another non-equivalent boundary endpoint law. Other cited visibility algorithms and Beer-index treatments similarly do not state the perimeter-pair law. Priority remains provisional against older specialized boundary visibility calculations.

## value

PASS

Independently arclength-uniform boundary endpoints represent a canonical geometric visibility observable, distinct from the familiar area Beer index. The all-positive-length formula yields a global sharp probability interval and an actual loss-of-smoothness hypersurface, including a measurable fourth-order cancellation in the natural symmetric square-notch one-parameter family. These provide motivated exact geometric benchmarks instead of a random selected numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
