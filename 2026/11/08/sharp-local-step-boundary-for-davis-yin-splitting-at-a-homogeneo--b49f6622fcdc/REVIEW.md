# Mathematical review: local graph-splitting stability frontier

## Correctness (PASS)

The fixed point is checked directly, including its positive radius restriction. The derivative of Euclidean normalization is the orthogonal tangent projection divided by the radius; the cubic derivative at the uniform vector is a scalar. This makes the full Jacobian simultaneously diagonalizable with the connected symmetric graph Laplacian. Its radial multiplier is strictly within the unit disk; its nonconstant multipliers have the exact rational expression in RESULT.md. Multiplying \(1+m_\lambda\) by its positive denominator gives the stated quadratic \(P_\lambda\). The coefficient of the graph eigenvalue changes sign at \(\gamma=1/(2(a+b))\), which establishes the maximal-frequency boundary for positive killing. For zero killing, exact factorization forces every transverse multiplier to hit \(-1\) together. Eigenvalues beyond the boundary have modulus greater than one. These algebraic implications prove strict local attraction and linear instability in the indicated open ranges, but do not prove the nonlinear boundary case.

An exact-rational three-vertex instance and 1,208 supplementary symbolic, spectral, finite-difference, and parameter-case assertions ran from the packaged standalone script. The infinite-dimensional quantifier over all finite connected graphs is discharged by the analytic spectral proof, not by sampling.

## Originality (PASS; qualified by priority uncertainty)

Li–Zheng–Zhang [1] give the algorithm and prove global convergence for conservative step restrictions, plus a local Lyapunov rate within those restrictions; they do not state the complete explicit local Jacobian spectrum and its sharp change from contraction to instability for the homogeneous graph case. Zheng–Zhang [2] develop local spectral rates for Riemannian gradient descent, not the DYS I map. Existing general operator-splitting and spectral graph methods may enable a specialist to derive the threshold, but their standard conclusions do not directly subsume the exact phase boundary and simultaneous all-mode crossing at zero killing. Searches for the exact map, graph ground-state aliases, spectral radius, eigenvalue crossing and step threshold found no matching theorem. This is evidence for originality, not a proof of historical uniqueness.

## Value (PASS)

Uniform graph ground states are canonical finite discretizations and benchmarks for defocusing nonlinear eigenvalue optimization. A graph-independent simultaneous transverse \(-1\) crossing, and its splitting under positive uniform killing, identify an exact local step-selection boundary not supplied by the source's conservative global guarantee. The result distinguishes loss of attraction at the maximal graph frequency from global solver behavior and provides a reproducible diagnostic for explicit cubic treatment despite an implicit graph resolvent. No claim is made of full nonlinear bifurcation, global convergence at larger steps or improved performance in inhomogeneous physical traps.

## Closest literature and limitations

[1] Li–Zheng–Zhang, *Global convergence of an efficient splitting method for the defocusing Gross–Pitaevskii ground state problem*, arXiv:2609.13509v1, equations (1.6), (3.15), Theorems 3.4 and 5.1.

[2] Zheng–Zhang, *Riemannian Hessian analysis of Sobolev gradient flows for the Gross–Pitaevskii ground state problem*, arXiv:2610.12833v1, Sections 1.3 and 4.1.

Risks: an unindexed specialized graph iteration or a more general operator-splitting linearization theorem might contain an equivalent implication. The source's strictly coercive spatial assumptions do not include zero-killing Neumann graphs; the new result explicitly handles that algebraic extension. All statements are exact-arithmetic and local, and no independent mathematical validation has been performed.

Self-review: passed. Independent audit: not yet performed.
