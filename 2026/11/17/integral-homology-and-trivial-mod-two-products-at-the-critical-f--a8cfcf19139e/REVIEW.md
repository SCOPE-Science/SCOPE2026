# Independent mathematical audit

## correctness

PASS

The graph is simple and the neighborhood is open. In the frozen certificate a free face with just one immediate coface has no higher cofaces and the pair can be removed by a genuine simplicial collapse. The checked 999 pairs leave face counts (16,98,243,255,102) and dimensions at most four; the reduced signed boundaries have unit Smith ranks (15,83,153,101). Independently of that collapse, `/workspace/branches/reproduce_critical_c16.py` enumerates lexicographically ordered nonempty tuples via the common-neighbor predicate and reduces the full signed boundary matrices over Z. Replay with `python3 /workspace/branches/reproduce_critical_c16.py`: the original f-vector is (16,120,432,784,784,432,128,16), and all nonzero Smith factors are units, with ranks (15,105,320,463,320,112,16). A ±1 pivot splits off a unit by column and row operations, and every residual matrix reduces to zero. The resulting images are saturated, so ker ∂i / im ∂(i+1) has no torsion. The Betti ranks are (1,0,7,1,1,0,0,0). Over F2 on the full complex, independent elimination gives a seven-element degree-two cohomology basis and a generator of degree-four homology. Alexander–Whitney pairs the first and last triangles of each increasing 4-simplex with their common middle vertex. All 49 products evaluate to zero on that generator. This is the entire positive-degree multiplication: H^1 is zero and degrees above four vanish. A separate recomputation of the collapse and pairing likewise verified the frozen collapse counts and obtained zero with a different nonbounding four-cycle, of support 98 rather than 102. These are exhaustive finite calculations for the specified graph, not a homotopy classification.

## originality

PASS

The exact integral groups and degree-two mod-two pairing are supported as distinct at n=16. Two closely related, earlier indexed results state stable-range hypotheses that exclude this object; the exact indexed match is the assigned record itself. The standard Alexander–Whitney formula and homology algorithms are not originality claims.

## value

PASS

The circumference 16 is the first omitted case of the stable fourth-power theorem, not an arbitrary small graph. It witnesses a sharp failure of the stable additive description and isolates a new possible degree-two multiplication that is not settled by the ranks. The exact integral groups and complete mod-two multiplication are useful baseline invariants for extending the stable analysis across the boundary without claiming a full homotopy decomposition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
