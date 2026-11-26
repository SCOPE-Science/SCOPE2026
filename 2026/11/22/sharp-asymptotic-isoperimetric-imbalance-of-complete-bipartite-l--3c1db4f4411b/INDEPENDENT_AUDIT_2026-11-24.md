# Independent mathematical audit

## correctness

PASS

The Laplacian acts invertibly on the sum-zero hyperplane; applying it to the translated coordinate simplex multiplies its intrinsic volume √N/(N−1)! by Nq^(p−1)p^(q−1). For a facet omitting Le_i, its inward covector in the inherited Euclidean metric is L†e_i: its pairing with L(e_i−e_j) is 1 for every j≠i. Thus the altitude is the reciprocal norm and the facet area is dV times that norm. The shore-contrast projectors have diagonal 1−1/p and 1−1/q on their respective shores. The remaining block-constant line has diagonal q/(pN) and p/(qN), and eigenvalue N. This gives squared norms (p−1)/(pq²)+q/(pN³) and its symmetric counterpart, exactly the two radicands after factoring. These arguments include stars. For uniformity, substituting a=p/N and b=q/N and using log Γ(N) gives log V − (N−1)(1+b log a+a log b)=1−½log(2π)−a log a−b log b+O(N⁻¹). The remainder is uniform down to a=1/N, and the two positive facet coefficients both have relative errors O(N⁻¹). For r=a/b the derivative of log H has sign of g=−log r−2(1−r²)/(1+r²); g decreases to √2−1 and then rises to g(1)=0, with g(1/2)<0 and g(0+)=+∞. This proves one strict interior maximum; compactness with uniform convergence proves convergence of every maximizing integer proportion, not uniqueness of each integer optimizer. The balanced and all p/N→0 regimes give e for the scaled quotient, not for the quotient itself. A bounded direct numerical maximization of H gave a≈0.12841927 and eH≈3.09551449198038. Reviewed the exact proof (RESULT.md lines 42–80), VERIFICATION.md and the Gram determinant checker in check.py without treating diagnostic finite tests as proofs.

## originality

PASS

Credit the full-column simplex construction and the standard determinant and pseudoinverse metric machinery. The exact volume is elementary from the spectrum or the Matrix-Tree theorem, not a priority claim. The supported distinct result is the uniform intrinsic boundary profile and its strictly unbalanced limiting optimizer, obtained via the specialized facet-area expression. The conclusion is conditional on the compared evidence, not historical uniqueness.

## value

PASS

Intrinsic boundary area at fixed volume is a natural Euclidean shape invariant, and the competing shore effects are not resolved by Laplacian eigenvalues or graph symmetry alone. The sharp optimizer is neither balanced nor a vanishing shore, despite those two regimes having the same scaled limit. The all-bipartition uniform estimate is needed to rule out a hidden stronger boundary regime and yields a precise limit for every maximizing sequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
