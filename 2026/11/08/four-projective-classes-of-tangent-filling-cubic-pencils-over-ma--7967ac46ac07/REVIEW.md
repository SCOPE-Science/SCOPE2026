# Independent mathematical audit

## correctness

PASS

An independent exact replay (branches/replay_01.py, NumPy integer arithmetic and SymPy over F3) tested 29,524 normalized forms by evaluating all 13 incidences and their gradients, obtaining 3,744 tangent-filling forms. Enumerating 1,790,112 eligible reduced-row-echelon generator pairs counts each eligible two-space exactly once, giving 22,464 pencils. Elementary generator substitutions generate PGL3(F3) of order 5,616; the four computed orbits each have that size and match every generator row. The three profile/base-count combinations occur 11,232, 5,616 and 5,616 times as stated. Each representative has 3,740 tangent-filling candidate third generators, and at most six of their nine new projective points pass in any candidate; transport by the group rules out all nets and hence larger systems. Exact affine Jacobian unit ideals on the three charts prove geometric smoothness for all three form-orbit representatives and all thirteen displayed member codes; the separate four-pair rank test makes every base intersection transverse. Distinct smooth plane cubics share no component, so the base has geometric length nine. Scope is rational pencil members only. The frozen base_reduced.py had a nonportable absolute dependency and only printed booleans rather than failing on a nonunit ideal. The portable replacement in repairs/1 is self-contained apart from SymPy, fails on any of the twelve nonunit chart ideals, and was independently executed successfully. The complete corrected RESULT.md and VERIFICATION.md distinguish the homogeneous partials restricted to each chart from derivatives of a dehomogenized equation and give portable replay instructions. The repaired proof also justifies independence after chart restriction by Euler's identity. No scientific counts or claims of scope changed. The frozen source was not executed or changed.

## originality

PASS

The curve-level census is already covered and is explicitly credited to 91eb1857066d in the repaired result. The supported distinct claim is the complete pencil incidence, projective orbit, base and sharp no-net classification. The strongest distinct matches do not supply that classification. The exact matching indexed record is this same finding, not independent coverage.

## value

PASS

A sharp bound on the dimension of systems satisfying a fixed geometric condition, a full and free orbit classification, and exact base-scheme information are useful for choosing pencil representatives and knowing which tangent-filling cubics coexist in one system. Group inequivalence despite the same rational count profile is structural information not provided by the curve-level census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
