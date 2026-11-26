# Independent mathematical audit

## correctness

PASS

For n≥2 a nonempty hub-free fort must select both endpoints and have no adjacent omissions; the hub then sees at least two selected vertices. These path conditions are upward-closed among subsets, so testing individual deletions here suffices: an interior 1 can be removed exactly when flanked by 1's. With the hub selected, the remaining selected path set must dominate the path. A minimal dominator can contain a path fort only by being that fort. In a path fort no omitted vertex is private to a selected vertex; minimal domination therefore requires every selected vertex to be isolated among selected vertices. This leaves precisely the odd endpoint-to-endpoint alternating word. For the dominator series, singleton runs self-witness, while each end of a doubleton run needs a private zero: an internal gap incident to such a run has length 2, and an external gap incident to it has length 1. All remaining gaps are those permitted by domination. The resulting two-state transfer matrix has determinant 1−z²−z³−z⁴+z⁶ and gives the stated series; the one-or-two 1-block construction gives F. The declared n=0,1 conventions also agree with the series. Independent adjacency/proper-subset enumeration over all 262121 nonempty fan subsets for 2≤n≤16 matched both exact families; independent private-neighborhood tests and series coefficients matched at those orders, giving minimal-fort totals 3,2,6,5,10,12,18,24,34,47,65,90,125,173,240. Replay: python3 /workspace/reproductions/check_fan_crown_skew.py fan. The supplied code's expansion to 100 is not comparison to independent counts past 16; neither bounded run proves the general theorem.

## originality

FAIL

The earlier exact membership theorem for fan zero forcing and existing component enumerators mechanically give the frozen split and rational count. This is demonstrated implication, not an assertion that the exact formula was printed verbatim or that the frozen mathematics is false.

## value

FAIL

An explicit minimal-fort census is convenient, but the frozen narrow invariant is mechanically extractable from the prior exact fan membership characterization, known path counts and a direct overlap test. The audited claim does not supply a separate nonroutine unknown result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
