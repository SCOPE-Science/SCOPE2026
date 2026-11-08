# Scientific review

## Correctness — PASS

The objective is precisely the mean size of the percolation component of a uniformly selected surviving seed after removing exactly one vertex from a finite tree. The unique-path identity in RESULT.md gives the mean as a distance-pair polynomial, without an infinite-limit inference. Exact breadth-first distance counts and exhaustive Prüfer enumeration of every labelled tree of orders two through seven establish one universal maximum-degree optimizer for each tree. Each difference is certified nonnegative for all \(0\le p\le1\) using integer-scaled Bernstein coefficients; the witness's explicit distance polynomials and their strict comparisons yield a unique crossing \(p^2+p^3=1\). The standalone verifier was run from this package, producing 18,248 tree checks and 40 exact independent full-edge-state calculations. Rechecking a finite exhaustive certificate is distinct from relying on a random sample.

## Originality — PASS within reviewed evidence

Britton–Janson–Martin-Löf (2007), Preciado and collaborators (2013), and Altarelli and collaborators (2013) provide mathematical and optimization frameworks but not this exact eight-vertex first-switch classification. Holme (2017) is the strongest close comparison and computes exact vaccination importance for all connected graphs on three through seven vertices. Holme's work covers calculation of these smaller-graph averages, but does not present an eight-vertex example or the global same-vertex assertion for every tree up to seven. The novelty claim is confined to the explicit sharp first-tree-order statement, not the foundational model or the method of enumerating Prüfer sequences. Residual risk: another source might contain an equivalent degree-versus-fragmentation crossover or a stronger tree-specific ordering theorem. Priority has not been independently audited.

## Value — PASS

The optimal single-vaccine choice trades local degree against how deletion fragments long infection paths. Determining the smallest tree where the choice actually changes with transmissibility is a motivated structural boundary: the low-transmission degree heuristic is universally compatible with optimality through seven vertices but can fail already at eight. The sharp algebraic switch and complete small-tree certificate provide a reproducible reference for finite-network intervention heuristics, while making no field-policy or arbitrary-network claim.

## Scope and limitations

The model assumes uniform independent edge transmission, one perfect pre-epidemic vaccination, a uniformly selected surviving seed, and a tree. The mean outbreak size does not determine the outbreak-size distribution or broader control objectives. The computational classification is an exact, finite exhaustive proof only through seven vertices. References are compared by claim and scope; no claim of independent priority certification is made.

Self-review: passed. Independent audit: not yet performed.
