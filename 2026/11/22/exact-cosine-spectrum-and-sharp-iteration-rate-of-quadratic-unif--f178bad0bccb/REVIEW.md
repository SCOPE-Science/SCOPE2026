# Independent mathematical audit

## correctness

PASS

The clamped endpoint rows of the Greville collocation matrix are the endpoint coordinate rows. At the first cell midpoint, writing u=nx, the outer spline is (1−u)^2 and the spline two indices to its right is u²/2; the middle value follows from partition of unity. Thus the first interior row is (1/4,5/8,1/8), with its reflection at the other end. A regular interior cell midpoint has (1/8,3/4,1/8) by the uniform quadratic recurrence. The first and last formulas both apply at n=2. The restricted matrix T on the zero-endpoint coefficients is symmetric with off-diagonal entries 1/8 and diagonal entries 5/8 at both ends, 3/4 elsewhere. Set v_0=−v_1 and v_{n+1}=−v_n, making every row the same three-term stencil. The sin((i−1/2)jπ/n) vectors satisfy both boundary conditions and the recurrence, with distinct eigenvalues (3+cos(jπ/n))/4 for j=1,…,n. They form a basis; their squared norms are n/2 for j<n and n for j=n. Evaluation at the distinct Greville nodes is onto via continuous interpolation, and the coefficient-to-spline map is injective. The n nontrivial eigenfunctions plus the two affine eigenfunctions span the image. Since the restriction on that image is invertible, the ambient space splits into the image and the infinite-dimensional kernel, so this also determines the full complex spectrum. Subtracting Lf leaves zero endpoint samples; the first iterate gives the interior sample coefficients, then m−1 steps apply T. The stated power expansion follows and normalizing by γ_n^(m−1) leaves a nonzero bounded rank-one limit; the lower bound on the sharp rate also follows by testing the leading sine spline. Taylor expansion gives the claimed π²/8 constant. The independent replay python3 /workspace/checks/frozen_math_checks.py 5 uses de Boor evaluation of each proposed coefficient spline, testing 170 modes for n=2,…,18 without calling the supplied basis-code checker.

## originality

PASS

The finite collocation reduction and abstract geometric convergence are known, and the sine diagonalization of a constant-coefficient stencil is standard. What survives the inspected comparisons is the specific clamped quadratic operator identification, including its boundary entries, exact eigenvalues and eigenfunctions, and the sharp degree-two gap coefficient. The related exact cubic findings do not give these quadratic statements.

## value

PASS

A fixed-degree fine-mesh spectral question for this natural positive spline operator was explicitly posed independently of the computation. The exact quadratic spectrum explains both iterates on fixed meshes and the sharp shrinking-gap constant, and supplies actual spline modes rather than a numerical range. This is useful in choosing and interpreting iteration scales and goes beyond the qualitative limit or a generic stencil calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
