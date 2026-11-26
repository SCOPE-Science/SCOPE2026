# Independent mathematical audit

## correctness

PASS

The local test uses the zero-padding convention at both open ends and checks precisely the vertices labeled zero. I independently recovered the displayed potential by shortest-path relaxation on pair states using column weight minus one. Checking all finite inequalities proves the lower bound at every length by telescoping, and alternating 01 and 10 attains it. A path attains equality exactly when all slacks are zero. Independent trimming left 12 states, 16 arrows, and connector states 12 and 28 as both initial and final. First-return excursions alternate connectors, with one of each length 1, 2 and 5 from either connector; this is bijective including the empty composition for n=2. The recurrence and displayed counts follow. For the growth rate the positive root of x+x²+x⁵=1 is simple; equality in the triangle inequality on its circle forces x positive since exponents 1 and 2 are present. Its reciprocal is 1.704902776041646… .

## originality

FAIL

Shown already covered: the distinct published Resultary record a9925f4ce2fb explicitly states the same optimum, open labeled ladder count and unique orientation-plus-{1,2,5}-composition classification under the same row and column conventions. This is direct equivalence of mathematical claims, not a title, catalogue-date or provenance inference.

## value

FAIL

The three-excursion classification is useful mathematics, but the frozen finding repeats an existing exact optimizer classification with the same graph, count, encoding and boundary conditions. Neither its recurrence and growth constant, which follow from the existing series, nor replay of the tight-walk certificate supplies an independently useful new result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
