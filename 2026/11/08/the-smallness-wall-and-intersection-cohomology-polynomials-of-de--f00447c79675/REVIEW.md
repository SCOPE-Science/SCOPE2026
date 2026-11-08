# Review of the quadric-cycle intersection-cohomology theorem

## Correctness
PASS. The proof uses the explicit proper projective-bundle parametrization from Chen--Hu--Ma and reconstructs every fiber dimension. Its double-plane locus has codimension \(n+\binom{k}{2}\), whereas its exceptional fibers have dimension \(n-k\); the precise small and semismall cutoffs follow by direct algebra. At equality, de Cataldo--Migliorini's projective semismall decomposition theorem gives one and only one shifted \(\operatorname{Gr}(k,n+1)\) contribution because its exceptional fibers are irreducible projective spaces. The two polynomial formulas follow from Schubert calculus and projective-bundle cohomology. The standalone checker confirms representative coefficients, symmetry, dimension constraints and Euler counts; finite checks are not substituted for the proof. Risks: the underlying published geometric fiber statement and semismall decomposition theorem are used as cited hypotheses/results.

## Originality
PASS, qualified. The inspected 2026 Chen--Hu--Ma manuscript computes ordinary cohomology of the full Chow variety, not middle-perversity intersection cohomology of the closed quadric-cycle image; its Proposition 3.1 gives the required fiber data but not the new dimension wall or relevant-stratum correction. The 2008/2010 Hu article gives virtual invariants and cycle decomposition; de Cataldo--Migliorini proves the general semismall theorem, with no special quadric-cycle computation. Targeted mathematical-record queries and published-literature searches found no statement giving the same exact wall and Gaussian correction. The result combines known tools and may be implicit in broader geometric machinery, so historical priority remains provisional.

## Mathematical value
PASS. The theorem identifies exactly where a canonical resolution of a natural singular algebraic-cycle locus changes from small to semismall and then to non-semismall, and computes all rational intersection Betti numbers throughout the first two regimes. The boundary correction detects a nontrivial topological contribution that ordinary Chow-variety cohomology does not isolate. It is a uniform structural classification in both cycle and ambient dimension, not a selected special-case computation.

Self-review: passed. Independent audit: not yet performed.
