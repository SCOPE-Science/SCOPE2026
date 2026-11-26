# Independent mathematical audit

## correctness

PASS

Independent exact reproduction in evidence/3-quartic-census.js exhausts the 13 rational points and lines and finds no smaller nontrivial block, then 234 six-point blocks forming one orbit under the 5,616 projectivities, with stabilizer 24. It solves the six vanishings by meeting the two halves of the coefficient vector on their evaluation values rather than using the frozen row-reduction implementation, and finds a kernel of size 19,683, then 1,134 exact-locus vectors and 567 projective equations. Explicit substitutions partition the latter into 30 stabilizer orbits. Independent modular Buchberger tests on the three affine Jacobian ideals over F3 certify geometric, not merely rational, smoothness: a unit ideal excludes a common zero over the algebraic closure, and a proper ideal remains proper under field extension. The ten smooth representatives match all ten coefficient vectors in ORBIT_TABLE.json; their local sizes are nine 24s and one 6, and each excluded orbit has a rational singular point. Projectivities preserving two exact-B models must stabilize B, so the local classes are the global classes; multiplying the local sizes by 234 gives 51,948 projective equations. Adjunction supplies the canonical plane model of a smooth quartic, hence equivalence with F3-isomorphism classes. Only the stated field, degree and point-incidence condition are classified.

## originality

FAIL

The distinct same-date rational-inflection record contains the complete projective quartic representative census with exact geometric smoothness and orbit sizes; this is not merely a table of aggregate inflection counts. I decoded its complete TSV and imposed the elementary rational-line incidence filter. It gives the ten classes and the precise orbit-size and stabilizer breakdown, hence also the equation count. This is verified available coverage, not a conjecture based on the title and not a priority inference from the common date. The separately indexed November 8 record explicitly restates the census with additional arithmetic information. The frozen calculation is independently correct but does not establish a distinct scientific result beyond the mechanically filterable data.

## value

FAIL

The minimum blocking configuration is a naturally motivated slice, but the frozen deliverable is precisely the result of an elementary incidence filter on a complete existing orbit dataset. Neither the count, representatives nor stabilizer orders require a new invariant or mathematical obstruction beyond that table. The independent enumeration is useful validation, not a distinct contribution here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
