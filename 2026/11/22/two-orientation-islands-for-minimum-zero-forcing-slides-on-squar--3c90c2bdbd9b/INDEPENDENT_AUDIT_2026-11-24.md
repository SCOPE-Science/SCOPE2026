# Independent mathematical audit

## correctness

PASS

For a blue cell, the white-neighbor count is the sum of the degrees of its row and column in the white-edge graph. Hence the first force requires an isolate and a leaf on opposite sides; edges of any initial cycle can never be the first edge removed from that cycle. At most 2n-2 white edges are possible, and equality forces a single tree plus an isolate. If the isolate is a row, the 2n-2 degree sum on n columns forces a leaf column. Its removal creates a column isolate too, and a forest with isolates on both sides can be eliminated by leaf deletions; transpose for the other type. The bipartite tree formula gives the stated component sizes. A slide is a shared-endpoint white-edge exchange. If it touches the previously isolated row via the added edge, the common endpoint must be a column, so no column degree changes and no cross-type slide can result. For a fixed missing row, insert edges from a chosen active row to each missing adjacent column and drop the last edge of the original tree path to that column; this preserves the tree and shares the column. All other active rows then have degree one and can be pivoted to one column, producing the double star. A center row distinct from two missing rows exists for n>=3, and transferring the leaf edge at the center column connects the two double stars by a slide. A jump can instead delete a leaf column edge and attach the previously missing row to a different column, producing a tree on all rows and all other columns. At n=2 the rook graph is C4: exactly the four adjacent pairs are optimal, a slide produces an opposite pair, and a jump connects the adjacent pairs cyclically. The proof is uniform without enumeration. I inspected the frozen brute force and tree-support programs and recorded checks for n=2,3,4 without executing them; they are corroboration, not an all-size certificate.

## originality

PASS

The distinct claim is the structure of valid constrained moves on the already known minimum supports, including the contrast with unrestricted jumps. The known optimum, support classification, and count are credited. No inspected distinct source covers the exact move theorem; same-day records were compared without assuming publication order.

## value

PASS

On a standard graph family, an explicit geometric invariant gives two large connected mobility classes for local moves even though unrestricted moves connect all optima. Legal within-class paths and the exceptional 2-by-2 boundary make this stronger than disconnection alone or a recount of known states.

The dated certificate retains the supplied scientific assessment, sources and limitations.
