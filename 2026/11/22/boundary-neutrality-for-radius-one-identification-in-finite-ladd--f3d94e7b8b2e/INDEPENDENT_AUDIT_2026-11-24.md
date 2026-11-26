# Independent mathematical audit

## correctness

PASS

Closed signatures in a column only use it and its immediate neighbors. Nonempty signatures at column distance at least three are disjoint, so domination and pairwise separation of columns at relative distance 0, 1 or 2 suffice. Testing at the leftmost column of each pair requires precisely masks from relative positions -1 to +3. With fixed zero padding and omission of nonexistent vertices, this gives the length-four initialization, a single interior transition on four-mask states upon each append, and a fixed terminal predicate for the three remaining centers. Independent exact reproduction found 256 states and 737 interior transitions, recovered the terminal mask, and verified every component of v_6=3+1_{a=3}+wt(b)+wt(c)+wt(d) and v_13=v_6+6. A fixed min-plus transition commutes with the addition of 6, so the exact componentwise equality propagates to every n>=6, including after the same terminal minimization. Terminal bases and separate exhaustive direct enumeration of all subsets at n=2 through 9 give the initial minima (3,3,4,5,6,6,8,9,9,10,11) at widths 2 through 12. This establishes the asserted formula for every n>=2. At n=1 there are closed twins. Proposition 2 of the cited primary circular paper gives the same formula in its width domain n>=5, so the comparison is exact for cardinalities, without requiring any code to remain identifying after adding edges.

## originality

PASS

The supported distinct content is the evaluated all-length finite open ladder optimum and its resulting equality with the circular optimum. The circular expression, infinite density and general pseudo-five-local transfer-graph framework are already present in prior work. In particular, the closest paper does not merely discuss circular strips: it gives the equivalent fixed-height min-plus method and stability for open strips. Its general stability and shortest-path statements do not give the specific transient and residue values without solving the open-boundary instance.

## value

PASS

The optimum cardinality for the simplest open square strip is a natural exact invariant. Boundary changes can affect the code both through domination and signature collisions, so equality with the circular optimum at every comparable width is a substantive answer, not preservation of candidate solutions or just the known infinite density. The full residue correction, including the exceptional excess in two residue classes, matters for finite networks. A small componentwise certificate explains why the next seven-column block always costs the same amount; scalar numerical agreement out to a fixed length would not establish that fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
