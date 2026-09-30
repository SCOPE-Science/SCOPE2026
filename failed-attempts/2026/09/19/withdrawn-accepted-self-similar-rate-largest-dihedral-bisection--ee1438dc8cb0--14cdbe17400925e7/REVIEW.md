# Same-model review

## Correctness — PASS

The source recurrence was rederived from the published formulas and analyzed as an asymptotically autonomous contraction. On the invariant interval, the limiting map has derivative magnitude strictly below one. Its unique fixed point is equivalent to the cubic \(7t^3-12t^2+4=0\), whose unique root in \((3/4,4/5)\) is \(0.783553337513463\ldots\). The finite-\(b\) perturbation is uniformly \(O(b^2)\), while the source invariant gives geometric decay of \(b_n\), which yields convergence of \(t_n\), summability of its fixed-point error, and the convergent-product asymptotic for \(b_n\).

The second-order coefficient follows from a Taylor expansion at the fixed point. The exact identity \(F_0'(\tau)=-1/2\) was checked algebraically from the cubic, and \(\tau^2>1/2\) gives the stated forced asymptotic \((t_n-\tau)/b_n^2\to K\). The inradius formula was independently obtained from volume divided by total face area. Consecutive-ratio limits then follow directly. The verification artifact reproduces the fixed point, second-order coefficient, inradius limit, quality growth, and limiting dihedral relation for the published seed and additional invariant-family initial conditions.

Adversarial checks included distinguishing the exact asymptotic statement from the source's one-sided bounds, checking that the diameter tends to one rather than introducing an additional exponential factor, and checking the sign and denominator in the inradius formula. The limiting angle identity was reduced to the same cubic rather than inferred from numerical coincidence.

## Originality — PASS, to the best of our knowledge

The invariant LAB family, exact recurrence, tie-free selected edge, conforming construction, and coarse degeneration bounds are prior results of Korotov and Michaud and are excluded from the novelty claim. Projective/similarity-class dynamical analyses of longest-edge bisection are also prior art and concern a different selection rule.

The accepted contribution is restricted to the LAB recurrence of arXiv:2609.18788: convergence of every initial condition in the published invariant region to one algebraic self-similar profile, the exact asymptotic contraction/growth bases, the second-order shape correction, and the induced sharp asymptotics for inradius, quality ratio, vanishing face angle, volume, and limiting dihedrals.

Searches covered the motivating title and arXiv identifier with fixed-point, self-similar, attractor, asymptotic-rate, mesh-degeneration, and tetrahedral-bisection terminology. The motivating paper was inspected through its full arXiv HTML theorem, recurrence, proof, and references; it states the invariant recurrence and coarse bounds but no fixed-point or sharp asymptotic-rate result. No overlapping SCOPE record was located by source identifier, largest-dihedral-angle terminology, or tetrahedral-bisection terminology.

The most relevant residual risks are the 2026 projective-dynamics paper of Adiprasito–Kalmanovich–Solomon and the 2025 paper on convergence of an R1+ longest-edge-bisection family. Their accessible statements concern longest-edge bisection rather than LAB; the former full PDF and the latter full journal text were not inspected end-to-end here. They could contain reusable general dynamical lemmas, but the available evidence does not indicate the source-specific cubic, LAB attractor, or geometric constants reported here. Because the motivating preprint is very recent, an unindexed contemporaneous follow-up or later revision is also a residual originality risk.

## Value — PASS

The source proves degeneration for one seed using invariant-range estimates. The present result identifies a universal attractor for the whole invariant family and replaces the interval bounds \(3/4\le t_n\le4/5\) by an exact asymptotic shape and rate. This yields a sharp quality-growth base \(1.276237\ldots\), rather than only the published lower-bound base \(1.25\), and gives a closed asymptotic description of all principal degeneration metrics. The fixed limiting dihedral profile also explains how the branch can become arbitrarily ill-shaped while its dihedral geometry itself converges to nonextreme values.

## Limitations

The result is confined to the explicit invariant family of arXiv:2609.18788 and does not establish a basin of attraction in the full tetrahedral shape space. It does not repair LAB, prove behavior for every branch, or provide a finite-element error estimate. The amplitude \(C\) depends on the initial tetrahedron and is represented by a convergent product.

Same-model review: passed. Independent audit: not yet performed.
