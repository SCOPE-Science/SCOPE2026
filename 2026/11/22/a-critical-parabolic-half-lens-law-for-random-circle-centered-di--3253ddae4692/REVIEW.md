# Scientific review: critical parabolic half-lens law

## Correctness — PASS

The event of a containing semicircle is exactly the existence of a unique circular gap above \(\pi\). The Dirichlet law of uniform cyclic spacings gives its probability and the exact conditional beta survival of its slack; the scaled slack is exponentially distributed in the limit. For the rare semicircle configuration, every right-half-plane point satisfies the complete disk intersection if and only if it satisfies the **two extreme** disk inequalities. Multiplication by \(n^2\) yields the exact finite-\(n\) endpoint inequality (1) in `RESULT.md`. The center lying near the short-arc bisector with overwhelming conditional probability excludes a negative horizontal region of nonvanishing scaled width, leaving a compact parabolic half-lens. Integrating its vertical sections gives the claimed evaluated area transform. The proof verifies the \(\gamma=0\) and \(\gamma>0\) boundaries, including the proper conditional quantifier.

The reproducibility checker independently tests the circular-gap identity, direct radial area integration, several finite-size crossover configurations and sampled rare-event probabilities. These computations support the formula but are not substitutes for the exact geometric argument. A risk is that additional uniform error estimates would be required to assert convergence rates or simultaneous growth of \(\gamma\), neither of which is claimed.

## Originality — PASS, provisional priority

Three particularly close public comparisons were performed against full or substantive published mathematical text, and searches included equivalences, boundary-layer and semicircle terminology. The **exact circular-gap area identity for every fixed \(b>1\)** is already known from *Exact circular-gap area laws and Gaussian fluctuations for intersecting congruent disks*. That identity is genuinely broader in its finite-configuration area domain and therefore is a serious prior source, not an irrelevant analogy. It gives a representation for every finite \(b_n>1\), but not the stated conditional **joint anisotropic Hausdorff limit**, the half-plane cutoff created by many centers, or its evaluated critical random area law as \(b_n-1\asymp n^{-2}\). These latter statements, not the old finite identity, comprise the precise originality assertion.

The *Anisotropic semicircle containment and the Gaussian–von Mises crossover for random enclosing disks* establishes the classical exponential gap mark and related minimum-enclosing-circle geometry, but not an intersection-body area/shape law. *A critical-window law for the two-vertex event in random disc-polygons* has the same radius scale but samples interior points and addresses a different geometric event. Paouris–Pivovarov's archive-period paper and Fodor–Kevei–Vígh's work concern distinct ambient-distributed center or hull models. The \(b=1\) exact lens and Wendel probability are explicitly credited background; novelty is not claimed from those alone.

Historical-priority risk: another treatment of the known all-radius circular-gap formula may already have extracted this conditional critical asymptotic and anisotropic set limit without using identical language. Semantic search and full-text comparisons cannot certify exhaustive priority, and independent audit is outstanding. No known inspected statement directly covers the marked half-lens limit.

## Mathematical value — PASS

There is a natural singular radius at one: intersection of all sampled unit disks is typically a single point, but on the rare event of semicircle containment it becomes a small lens. Conditional slack of order \(n^{-1}\) competes with the squared radius excess \(b_n-1\) exactly at order \(n^{-2}\). This determines a genuine geometric crossover with two different coordinate scales, a nontrivial random limiting body and an explicit area law. The result resolves the natural marked, near-critical behavior not described by fixed-radius expected-area/central-limit theorems; it is not a mere numerical improvement or arbitrary slice.

## Limits and independence

The proof covers independent circle-uniform centers, fixed \(\gamma\ge0\), and the rare-event conditional law. It does not prove unconditional area scaling, nonuniform densities, arbitrary radii or error rates. The historical comparison is provisional rather than an independence or exhaustive-priority certificate.

Self-review: passed. Independent audit: not yet performed.
