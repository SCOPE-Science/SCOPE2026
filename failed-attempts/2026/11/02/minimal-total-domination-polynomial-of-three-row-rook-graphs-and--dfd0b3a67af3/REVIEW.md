# Independent mathematical audit

## correctness

PASS

The stated labeled polynomial and size gaps are correct. A set must occupy all rows or all columns and induce no isolated selected cell. In full coverage, a selected cell cannot be the only cell of both its row and column (it would be isolated), so any deletion leaves one side covered. All private witnesses are selected, forcing the induced graph to be disjoint edges. In row-only coverage, a cell of a nonsingleton row likewise needs a selected degree-one witness. A row with at least three cells would need at least three singleton rows, which is impossible. With three rows of size at most two, a row of size two must either have two private horizontal witnesses in singleton columns (each cell witnesses the other), or two vertical singleton-row witnesses. Thus the row patterns give a vertical triple, a four-set with two singleton rows sharing a third column or attached in distinct columns to a doubled row, or three horizontal pairs in distinct columns; the (2,2,1) case is impossible. The full-coverage boundary cases are included in these counts. In column-only coverage, singleton columns give the one-row and two-row partitions with no isolated selected cell. To justify the claim in RESULT.md line 45, if one occupied row were a singleton in a doubled column, its only selected neighbor would have at least two selected neighbors because all n>=3 columns are covered by those two rows. Then the singleton cell cannot have a selected private witness; no outside witness is possible since its deletion preserves full column coverage. With both row counts at least two, each doubled-column cell must have a private same-row cell in a singleton column, forcing both row counts to be two and n=3. This gives the extra 18 sets. Independent finite check: python3 /workspace/branches/rook_independent.py evaluates open-neighborhood unions and single deletions for every nonempty subset for n=3 through 7; it reproduced (6,45), (4,93), (5,150,63), (6,270,243), (7,441,630,339) in increasing degree. The finite enumeration does not establish the all-order result. The frozen verify.py was inspected, not executed.

## originality

FAIL

A distinct Resultary finding already gives the full size-graded polynomial of the same labeled objects on every rectangle. The frozen polynomial, including small-order cases, and its sparse support are mechanical consequences of that finding's component classification; the exact formula can be correct without constituting a distinct result. This is a determination of coverage, not of historical priority or authorship.

## value

FAIL

A sparse spectrum for a connected family is a motivated invariant, but the frozen contribution is a direct three-row coefficient extraction from a known all-rectangle classification. The size gap is immediate from the resulting exponents; no further structural result beyond that classification was demonstrated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
