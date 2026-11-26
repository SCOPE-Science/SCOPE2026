# Independent mathematical audit

## correctness

PASS

For a chosen row u and exact column v in each fiber, the doubly excluded assignments E must be deleted by the approximate side, and assignments H off u but on v can be put solely on the exact side. The canonical lax cover keeps every row-u assignment on the approximate side, including its overlap with the chosen column. For any other witness with those retained row and exact column values, h assignments of H on the approximate side cost at least h extra deletions and increase its possible size by at most h; from e+h≤p(N−b+h) one obtains e≤p(N−b) for p∈[0,1]. This works also for empty sides and gives the stated independent max per fiber. With c=1−p=s/(rs−r+1) the mean score over the rs crosses is exactly cN_a in each fiber, so the criterion holds; full rectangles give exactly the stated positive deletion ratio for every choice. For saturation all occupied fibers must have constant scores (otherwise the strict score surplus persists for slightly smaller p). Comparing two columns and summing over r rows forces equal column sums, then constant row entries across columns. Equality across rows forces them all full in an occupied fiber since the score changes by s−c between a full and an empty row. The hypotheses of distinct triples and r,s≥2 enter this argument. The finite rational candidate set and the score computation give the stated polynomial algorithms; empty teams satisfy all p, and a singleton dependent alphabet gives universal threshold zero.

## originality

PASS

The zero-error cross-coverability criterion was already present in the exact size enumerator, and the same exact split has established four-coherence and a close minimal-obstruction classification. The supported distinct result is the positive relative-error criterion with its sharp bound and full extremizer classification. The closest relative-error primary theorem concerns distinct determinants and does not subsume it.

## value

PASS

The relative budget makes a lax split genuinely different from exact cross-coverability or approximate satisfaction on the whole team. For a natural common-determinant fragment the result simultaneously gives exact model checking, the worst-case tolerance that works uniformly over named alphabets, and a complete description of the hard inputs. The asymmetry and denominator of the threshold are explained by the canonical witness rather than by a finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
