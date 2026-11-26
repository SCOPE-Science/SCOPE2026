# Independent mathematical audit

## correctness

PASS

On V/K with K=L^perp the evaluations form a full q^2-point character matrix: a nonzero linear functional maps onto F, so composing with any fixed nontrivial additive character gives the requisite orthogonality even over an extension field. Pooling equal quotient rows gives q^2 m(y)/|S_j| for every coset, including zeros. The Gauss sums give the stated shell cardinality and binary level cardinality with the determinant of Q itself, not the unhalved polar form. For an isotropic line a hyperbolic pair gives Q=2tu+kappa r^2; u!=0 gives one solution, while u=0 contributes 1+sigma full fibers and q-1-sigma empty ones. For an anisotropic line the binary orthogonal complement has determinant class delta/s; q-epsilon singleton fibers and the total mass fix the zero/two counts. Counting nonzero vectors of each norm-square class and dividing by q-1 gives the projective class sizes. Subtracting the best anisotropic rank (epsilon=-1) from the isotropic rank gives (q-1)(q-3)/2 for sigma=1 and (q^2-2q-1)/2 for sigma=-1; in particular the claimed tie is the only one. Both anisotropic positive multiplicities are nonzero throughout the domain, and the condition numbers use square roots of Gram ratios. Independent exact quotient enumeration covered both discriminant and nonzero-radius classes and all directions over F3 and F9 (52 and 364 checks). At q=3,sigma=1 it gave four isotropic rank-eight directions with spectrum 0, (3/4) repeated six times, (9/4) twice; three anisotropic directions with 0, (3/4) repeated four times, (3/2) four times. Replay: /workspace/branches/41de8918-c138-4106-8532-c64e93897122/independent_fiber_enum.py and fiber_enum_q3.txt, fiber_enum_q9.txt in the same directory. This replay checks exact fibers, not complex floating-point Gram entries. The frozen CHECK.py was inspected, not executed.

## originality

PASS

Quadratic level counts, projective conic classes, and Fourier diagonalization on a subgroup are established ingredients. The supported distinct finding is the full symbolic orientation-by-orientation sampling spectrum and the resulting rank/conditioning classification. Exact pointwise Fourier kernels determine individual Gram entries, but the compared statements do not evaluate their restriction spectra and multiplicities across all directions; that requires the all-coset calculation or an equivalent transform and count. Same-day ordering is unresolved.

## value

PASS

For complete plane sampling, the precise rank and positive singular values matter to identifiability and stability. The theorem distinguishes a rank-maximizing orientation class from better conditioned orientations and identifies a sharp small-field exception. It resolves the full discrete design comparison with an explicit spectrum, not just a norm estimate or an isolated standard quadratic count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
