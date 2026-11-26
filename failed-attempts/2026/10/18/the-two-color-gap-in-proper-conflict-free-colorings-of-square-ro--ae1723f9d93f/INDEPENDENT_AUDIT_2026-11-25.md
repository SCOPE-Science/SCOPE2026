# Independent mathematical audit

## correctness

PASS

The open neighborhood splits into the row and column with the center removed. In a proper coloring each half uses any color at most once, and the center color is absent from both halves. Thus the colors of multiplicity one are precisely the symmetric difference of the two full palettes. The sizes are m and n, so for m<n every proper coloring works; row cliques force n colors and addition modulo n gives a proper n-coloring. For a square, an n-color palette must be exhausted in every row and column. In an (n+1)-color palette, a color used f times occupies exactly f rows and f columns, hence is omitted in the same number of rows and columns. Choose a color that some row omits: that row and an omitting column then have identical palettes. For the (n+2)-construction in the frozen proof, the two omitted-color pairs have cyclic differences ±2 and ±1, which are disjoint for n+2≥4. The construction works at n=2 as well, and an isolated singleton takes one color. These deductions establish the full range without using the optional finite coloring tests as proof.

## originality

FAIL

Resultary fb9f4a963e44 states the same nontrivial rook formula and the same row/column palette criterion. Resultary 4827bdd1e654 additionally gives the identical result under odd coloring, which is equivalent on every proper rook coloring because every neighborhood color occurs at most twice. The excluded one-row case is a complete graph and the singleton is automatic, so neither supplies new mathematical content. This finding is materially covered regardless of priority between the same-day records or of the unresolved product-paper access.

## value

FAIL

The square-versus-rectangle phenomenon is mathematically meaningful, but the frozen article rederives both the known gap and the known structural characterization; changing from odd to PCF wording on a family where the tests coincide or adjoining the clique boundaries does not create a new invariant or useful extension. No distinct theorem survives the direct matches.

The dated certificate retains the supplied scientific assessment, sources and limitations.
