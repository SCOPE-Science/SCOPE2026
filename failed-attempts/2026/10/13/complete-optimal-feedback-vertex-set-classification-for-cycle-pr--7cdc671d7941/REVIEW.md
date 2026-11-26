# Independent mathematical audit

## correctness

PASS

Each adjacent column square forces the occupied deletion columns to cover the cyclic column graph. Given a cover, contracting surviving rungs gives exactly the column cycle with double-deleted vertices removed and with edges at opposite-rail singleton pairs removed. No parallel edges are created even for n=3, and contraction preserves components and cycle rank. When there are only singleton deletions, the complement is a forest exactly when there is at least one cut, and then the cut count equals the component count. An odd minimum cover has one adjacent occupied pair, and its r complementary independent vertices have cyclic gaps of one unselected vertex each with one extra unselected vertex. This gives 2r+1 covers; the one cut imposes one independent rail constraint, so (2r+1)2^r trees. In even order, budget r forces alternating single deletions and no cut; at budget r+1 either one double in an alternating cover gives a path, or the singleton cover has two adjacent occupied pairs. The cyclic positive-gap count for its r-1 complementary independent vertices is (2r/(r-1))*binom(r,r-2)=r^2, including r=2. The two prescribed cut bits give independent constraints since the induced graph on the occupied columns is a forest, even if the pairs share a column. Each fixed bit pattern admits 2^(r-1) assignments; the patterns with one and two cuts occur twice and once, respectively. Adding the 2r*2^(r-1) one-double choices gives all three stated counts and attained induced-tree order.

## originality

FAIL

Verified distinct Resultary coverage includes the minimum, all labeled minimum-set patterns and the parity-split total counts. The even component split also follows directly from its degree identity c+e(S)=2k-n and the given pattern counts, so the lack of a displayed separate T or Q formula there does not leave an additional scientific claim. The distinct record's displayed UTC date is later; the finding is one of equivalent existing coverage, not a determination of historical priority or dependence.

## value

PASS

This is a natural complete classification of extremizers in a basic cubic family, not just a minimum-size or small-instance computation. The reduction to a column cycle explains the obstructions, distinguishes connected and disconnected extremizers, and parametrizes all optimal subsets. This is useful structural mathematical content independent of the originality failure; the component formulas alone are not an additional contribution beyond the matched structural theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
