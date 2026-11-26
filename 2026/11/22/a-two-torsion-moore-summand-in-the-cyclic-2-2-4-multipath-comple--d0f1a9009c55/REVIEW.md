# Independent mathematical audit

## correctness

PASS

Reconstructed the directed-path face predicate as at most one selected incoming/outgoing arc per vertex and no directed cycle. Independent exhaustive enumeration of all subsets up to seven arcs (an eight-vertex acyclic path forest cannot have more) reproduced the face vector (20,154,560,976,720,144). The stated toggle sequence gives 1269 matching pairs; independent topological sorting of all oriented Hasse incidences verified acyclicity. It leaves one critical 0-cell, five 3-cells and thirty 4-cells with the listed masks. Independent signed gradient elimination reproduced the entire 5x30 matrix. Its columns generate u and 2v where u=(-1,0,0,1,0) and v=(0,1,-1,0,1); the span of u,v is saturated since their first two rows have a unit minor. Thus Smith factors are (1,2). Full simplicial boundary ranks independently give reduced Betti (4,29) in degrees (3,4) over F2 and (3,28) over F3, F5 and F7. Homotopy is stronger than the field checks: the Morse 3-skeleton is a wedge of five 3-spheres, Hurewicz identifies attaching maps with their degrees, and unimodular row and column operations are realized by self-equivalences of target and attaching sphere wedges before taking the homotopy cofiber. The unit cofiber is contractible and the degree-two one gives the stated Moore space, leaving three S^3 and twenty-eight S^4. Replay: RESULT.md lines 23–62; frozen VERIFICATION.md, verify.py, and verify_output.txt inspected as evidence only. Independent replay and output: branches/6fbd391e-c418-408c-98ca-1c6ba0d69643/independent_check.py and independent_check_output.txt. No extrapolation to other shores or claim of minimality.

## originality

PASS

The supported distinct claim is the integral homotopy type of the specific complete cyclic tripartite orientation with shores (2,2,4), not the general existence of multipath torsion. The inspected neighbors differ in an invariant of the defining digraph or in hypotheses and do not determine this homotopy type.

## value

PASS

This is a natural complete cyclic tripartite orientation with small repeated shores, adjacent to torsion-free cases and outside the acyclic matching reduction. The exact integral classification records a genuine Moore summand that rational homology misses, with a reusable explicit Morse certificate; it is a useful reference example of torsion in this cyclic family, independent of any future whole-family census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
