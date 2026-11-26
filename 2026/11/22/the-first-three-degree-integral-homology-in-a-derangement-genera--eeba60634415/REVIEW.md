# Independent mathematical audit

## correctness

PASS

I reconstructed the semi-simplicial cellular chain model: ordered subsequences are distinct basis cells, and deletion in position j has sign (-1)^j. Generating derangements by forbidden-position backtracking and recursively taking deletion faces, I built the exact integral matrices independently. Replay python3 /workspace/branches/reproduce_derangement.py (python-flint): direct Smith normal forms have only unit nonzero factors; every composite including the augmentation is zero. At n=6 the cell counts are (6,30,120,351,574,265), the five boundary ranks are (5,25,95,255,245), and reduced Betti numbers in degrees 0–5 are (0,0,0,1,74,20). For n=2–5 the independently computed Betti vectors are (0,0), (0,1,0), (0,0,3,1), (0,0,0,13,3). Each boundary image is primitive, so the relevant chain quotient is free and its cycle subgroup quotient is torsion-free. This supplies the claimed integral table, not just modular ranks, and handles nonempty reduced degree zero and the maximal dimension. No assertion at larger n, about equivariance, or about homotopy type is established.

## originality

PASS

The exact integral homology and the first occurrence of three positive degrees for the derangement-generated ordered-subsequence complex survive the strongest inspected comparisons. Earlier general results on the ordered-word chain model and the smallest cases are not counted as new.

## value

PASS

Removing full generators according to the natural fixed-position restriction yields a genuinely different injective-word topology. The earliest alphabet size where homology leaves the two highest degrees is useful as a sharp constraint on any future general account; exact unit Smith factors separately rule out a torsion-only or mod-p effect. The result is appropriately limited to the finite threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
