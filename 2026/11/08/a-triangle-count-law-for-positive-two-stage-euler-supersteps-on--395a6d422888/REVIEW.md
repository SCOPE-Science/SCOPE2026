# Review of the sharp two-stage Euler graph-positivity theorem

## Correctness

**PASS.** For a fixed finite connected unweighted regular graph, the exact diagonal, edge and nonedge entries of the quadratic Euler polynomial are reconstructed from \(L=dI-A\). The minimum edge common-neighbor count is the only active edge constraint. For noncomplete graphs, the diagonal and edge inequalities imply an exact finite upper bound on normalized cumulative time. Explicit feasible positive substeps cover every total below the bound; simultaneous equality at the bound proves uniqueness up to order. The extremal matrix is nonnegative and stochastic entry by entry. Complete graphs are handled by a separate rank-one projection, and the scalar-discriminant boundaries are verified. The exact-arithmetic standalone checker tested 173 connected labeled regular graph cases and 8,304 rational step pairs; this is supplementary, not an infinite proof.

## Originality

**PASS on inspected material, with publication-priority risk.** The closest direct antecedent is Alexiades–Amiez–Gremaud (1996): it uses the *same product of Euler factors* but optimizes spectral stability via Chebyshev arguments. That does not assert endpoint entrywise positivity or identify the minimum-edge-triangle invariant and the sharp stochastic kernel. Gottlieb–Shu–Tadmor (2001) give sufficient strong-stability-preserving conditions built from individually stable stages; the new extremizer permits an overlarge stage and does not follow from their stagewise condition. Cheng et al. (2015) use nonnegative random-walk polynomial coefficients, whereas the present extremal adjacency polynomial is signed. Meyer–Balsara–Aslam (2012) treat a different Legendre method, but only the abstract was accessible and hidden specialist comparisons cannot be excluded. No directly covering statement appeared in the inspected published research records. A failed search alone is not a proof of priority.

## Value

**PASS.** Super-time-stepping is an established acceleration technique, but spectral stability alone does not protect positivity of diffusion state variables. The theorem gives a complete exact answer for *all* connected regular simple graphs, reducing a global two-step matrix inequality to a local triangle statistic, including a sharp finite/unbounded transition, unique optimal durations, and an explicit probabilistic interpretation of the boundary transition. In particular, on balanced multipartite graphs the extreme superstep becomes a within-part jump, and on triangle-free graphs it becomes the nonbacktracking two-walk. These are structural classifications, not a numerical improvement of an arbitrary parameter choice. Practical accuracy at the large sharp bound remains unaddressed.

## Closest literature and limitations

See Alexiades et al. (1996), Gottlieb et al. (2001), Meyer et al. (2012), and Cheng et al. (2015), with identifiers and inspected sections in `RESULT.md` and `AUDIT.json`. The conclusion is endpoint-only, unweighted, regular, autonomous and first-order as an Euler composition. Publication priority is provisional in view of incomplete access to some specialist literature.

Self-review: passed. Independent audit: not yet performed.
