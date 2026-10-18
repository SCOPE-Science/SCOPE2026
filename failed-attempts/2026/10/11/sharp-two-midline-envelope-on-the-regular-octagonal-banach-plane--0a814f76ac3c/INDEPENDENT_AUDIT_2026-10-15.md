# Independent mathematical audit

## correctness

PASS

With z=x-y, all three unit constraints are x,z,x-z on the regular octagonal unit sphere. Dihedral symmetry reduces x to the vertical edge (1,a), -r<=a<=r, and z<->x-z swaps the two objective lengths. The three explicit edge-intersection branches in RESULT.md exhaust the two intersections of the octagonal boundary with its translate (apart from shared endpoint degeneracies). Their norm formulas are (c,sqrt(2)-a), ((2+r-a)/sqrt(2),(2+r+a)/sqrt(2)), (sqrt(2)+a,c) on the corresponding intervals, so each coordinate <=c=2sqrt(2)-1. The explicitly given pair x=(1,-r), y=(r^2,-1) satisfies all three unit conditions and both bounds at equality; direct independent numerical substitution reproduced c=1.82842712474619. Coordinatewise monotonicity produces M1=c, M2=c^2=9-4sqrt(2), M3=sqrt(c). The independent published full G_L proof supplies an alternate finite exhaustive edge-enumeration of the SAME two inequalities; no hypothesis on arbitrary Banach norms is asserted.

## originality

FAIL

DECISIVE COVERAGE: published 2026-10-11 Resultary exact generalized G_L profile for precisely the same regular-octagonal norm and equilateral domain explicitly proves both coordinatewise bounds and simultaneous sharpness. Its theorem directly implies all three constants; this is a covered corollary, not an independent original theorem.

## value

PASS

The common pointwise bound for both octagonal equilateral midline lengths is a natural structural estimate: it simultaneously controls several independently defined geometric constants, and gives an exact sharp witness. Such a bound is intrinsically useful as a lemma, although in this submission it is already contained verbatim in the inspected published generalized G_L theorem and therefore lacks originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
