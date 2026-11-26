# Independent mathematical audit

## correctness

PASS

For each claimed torus weight the homogeneous complexified Laplacian cancels adjacent radial coefficients; Q(0)=1 ensures that its rational polynomial is nonzero. The character weights correspond bijectively to the side-(ℓ+1) square in (m+n,m−n) coordinates and span by dimension. At nonnodal s the evaluation columns are nonzero multiples of Fourier columns, proving the rank and inversion statements; e^(−1) avoids every rational-polynomial zero. Put L=ℓ+1. For even ℓ the stated primitive winding gives consecutive nonoverlapping frequency blocks Li−j, hence all L² residues. For odd ℓ at critical size L², inversion on the nonzero weights has no fixed points, so cannot be in equivariant bijection with the residues 0 and L²/2 fixed by inversion there. At L²+1 the given (1,L) winding gives a collision equation (L+1)A−(L−1)B=r(L²+1) with r=0,±1. For r=0 coprimality forces A=B=0; for r=1 and L≥4 the only possible A are 1 and 2−L and yield B=−L and −2L−1, outside the allowed square. Negating proves r=−1 impossible; for L=2 the four residues are ±1,±2 modulo five. The unique unused residue of any optimal injective odd rule is zero by inversion symmetry. Independently built harmonic-projector evaluation matrices over finite fields have full rank for ℓ=1–7, and all critical-count residue windings were exhausted for odd ℓ=1,3,5. Replay: python3 /workspace/reproductions/frozen_math_checks.py 1; output /workspace/reproductions/record-1.txt. Those exact finite tests do not prove the all-degree result, and nothing here establishes stable conditioning or recovery at nodal radii.

## originality

PASS

Credit the harmonic basis and exceptional-radius treatment to the rectangular Hopf-grid predecessor, and the reconstruction criterion and DFT formula to general rank-one lattice theory. The supported distinction is the exact all-winding sample minimum in the one-trajectory architecture, including the parity obstruction and explicit attaining primitive windings. Neither a product-grid minimum, a fixed-winding rank theorem, nor a criterion testing a supplied rank-one lattice gives that exact optimum. The degree-one five-site (1,2) example is prior coverage of that instance. This is a bounded judgment about the all-degree theorem, not a priority claim for all of its ingredients.

## value

PASS

The scalar sample budget for exact harmonics along a single path is a natural acquisition invariant. The result determines when the dimension bound is attainable and resolves the odd case with a sharp obstruction and a matching construction, substantially improving on a rectangular design when that is used as a benchmark. The explicit inversion and characterization of the sole missing Fourier coordinate make the exact optimum usable without asserting numerical robustness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
