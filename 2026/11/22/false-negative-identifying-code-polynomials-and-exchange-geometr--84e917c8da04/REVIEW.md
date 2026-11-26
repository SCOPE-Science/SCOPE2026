# Independent mathematical audit

## correctness

PASS

Both closed neighborhoods have size 7. The directed differences have size 3 for adjacent vertices (two shared open neighbors plus the two endpoints in the closed intersection) and 5 for nonadjacent vertices. Failure needs two omissions in each adjacent difference, or four in each nonadjacent difference; the latter is impossible with at most seven omissions. This proves the forbidden-four-set reduction, together with exclusion of six or more omissions from any closed neighborhood. Failure at every seven-omission subset excludes larger omission sets by monotonicity. A separately written checker, /workspace/branches/15cb035d-f66d-4b89-954d-533a58a6310e/independent_check.py with independent_check.json, directly tested two-domination and asymmetric separation on all 65,536 detector subsets of each labelled graph. In sizes 10 through 16 it reproduced rook coefficients (720,1920,1496,560,120,16,1) and Shrikhande coefficients (256,1392,1424,560,120,16,1), with zero smaller admissible sets. In the rook graph the rows and columns are the maximal four-cliques; their intersection graph is K_4,4, so the row/column permutations and transpose exhaust the group of order 1152. In Shrikhande the six neighbors of zero induce C_6. The nine other nonzero vertices are distinguished by their two-neighbor signatures on that cycle (also directly checked), giving an upper bound 16·12 on the group; 12 maps preserving the connection set and 16 translations attain it. Orbit sizes were reproduced as (144,288,288) and (16,48,48,48,96). Independently computed exchanges yielded a connected 3312-edge rook graph of diameter 6 (144 vertices of degree 6 and 576 of degree 10) and a 624-edge Shrikhande graph with 16 isolates, six 16-vertex rook components (exact isomorphisms checked), and one component of size 144, with populations (16,48,96,96) at degrees (0,4,5,6). The domain and graph scope are exactly those stated; the uploaded checkers were not executed.

## originality

PASS

The same strongly regular pair has previously been compared using ordinary identifying-code optima and exchanges, and the two-domination/asymmetric-separation characterization itself is standard. Those are substantive overlaps, but the checked evidence does not give the two labelled error-detecting-code polynomials, the full optimum orbit census, or the optimum exchange geometry under this exact criterion. Distinct same-day findings were considered on their hypotheses, not ordered by date.

## value

PASS

Rook and Shrikhande are the canonical nonisomorphic pair sharing the same strongly regular parameters; comparing them controls neighborhood size and pairwise intersection data. Their common minimum 10 conceals substantial multiplicity and reconfiguration differences, from a connected exchange graph to many components including isolates. These exact counts and structures supply a useful discriminating invariant for the false-negative model, beyond recomputing an ordinary minimum or a single number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
