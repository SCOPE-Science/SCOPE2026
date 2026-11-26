# Independent mathematical audit

## correctness

PASS

RESULT.md lines 4–35 and 38–68 use the consistent physical-length mass. On an edge with nodal values x,y, the mass is at least h(|x|²+|y|²)/6 and the stiffness at most 2(|x|²+|y|²)/h; both are sharp only at y=−x. Since each vertex belongs to one edge of each length, their global quotient is bounded by 12(1/a+1/b)/(a+b)=12/(ab), with precisely the alternating equality pattern on the even cycle. Assembly across two-vertex cells and the discrete Fourier basis give the two stated Hermitian blocks at each of the m phases, with mass diagonal (a+b)/3 and off-diagonal magnitude at most (a+b)/6. The determinant therefore gives all eigenvalues with multiplicity. At phase 0 the two constant-in-cell modes give 0 and 12/(ab); at π the vectors (1,1) and (1,−1) give the two claimed inner edges. The determinant's c=cos θ derivative is strictly negative for λ≥0 and the λ-derivatives have opposite signs at ordered simple roots. A repeated Hermitian generalized root would require K=λM; the off-diagonal cancellation forces θ=π, and together with diagonal equality forces a=b. The resulting branch monotonicities extend continuously to that touching endpoint. The inner edges are sampled exactly when m is even, so the continuous gap/contrast formula must not be applied to the middle separation of an odd finite spectrum. Subtracting the inner edges and using (3a+b)(a+3b)=(a+b)²(4−δ²) gives the strictly increasing normalized gap. Example a=1,b=2,m=2: spectrum 0,6/5,12/7,6, normalized gap 3/35. The frozen checker.py and VERIFICATION.md were inspected, not executed; the code uses rational form tests and floating-point phase checks and is not an all-phase proof.

## originality

PASS

The distinct contribution supported by the comparison is the full alternating periodic P1 consistent-mass spectrum, including explicit gap edges and a normalized inverse contrast law. Generic local inverse estimates, Fourier reduction and the fact that two cells can split a folded band are not credited as new.

## value

PASS

The periodic alternating mesh is a natural minimal nonuniform case. Its exact top constant replaces a pessimistic minimum-cell bound, while the consistent-mass band formula separates an actual alternating-contrast gap from a finite sampling effect and gives a scale-free way to recover the contrast for the continuous dispersion or even periods. The precise band edges and finite-versus-continuous distinction are useful beyond the routine Fourier calculation, with no claim for general meshes or mass lumping.

The dated certificate retains the supplied scientific assessment, sources and limitations.
