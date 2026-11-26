# Independent mathematical audit

## correctness

PASS

Telescoping each shortest translation and summing over all start sites counts each cyclic edge h_n(d) times. Averaging with p proves the bound without reversibility. For a contiguous balanced arc the number of translated sites leaving the arc is exactly h_n(d) for each d, and the indicator residual has one sign inside and the opposite outside. Bistochasticity doubles the outflow and V=2, giving equality. If the kernel charges every nonzero d, cut equality forces all displacement bounds to be equalities. At m=floor(n/2), a cut with 2r boundary edges then satisfies rm<=min(|S|,n-|S|), so r=1 and the arc is balanced. The discrete coarea identity makes every superlevel cut of a real extremizer extremal; if two differ, opposite strict residual signs at a vertex in their difference make the counting-l1 triangle inequality strict. Thus the only nonconstant extremizers are those declared (p_0 may vanish). For heat, positivity at t>0 follows from the nearest-neighbor walk. The second difference of the distance is 2 delta_0 minus 2 delta_m for even n, or minus delta_m and delta_(m+1) for odd n. Its Fourier transform gives the negative nonconstant distance coefficients and the stated parity weights. Finite differentiation yields strict complete monotonicity of C_n', C_n'(0)=2 in the unnormalized convention, and the distance average as t tends to infinity. Independent replay `python3 /workspace/reproduce_frozen.py 1` made 6,504 exact signal/kernel checks (including three-level signals and zero weights) and 192 matrix-exponential derivative comparisons. The supplied checker was inspected, not executed; finite numerical checks are not universal proof.

## originality

PASS

Qualified to the finite-cycle result, in particular the balanced discrete equality classification for arbitrary nonzero-displacement support as specified and the finite parity-dependent heat spectrum. The heat kernel itself is classical. There is strong partial mathematical overlap with a same-day continuous-circle theorem: unit-cell embedding and atomic shifts (or density approximation) transfer its upper bound, and for even n a continuous half-circle is already a step-function extremizer. That transfer alone does not show odd-n attainment within the vertex-step subspace, does not establish rigidity for the discrete atomic kernels, and does not give the discrete parity spectrum. Same-day dates do not settle priority. The distinct supported contribution is not the general moment principle in isolation.

## value

PASS

The sharp coefficient and complete worst-case signal family describe integrated distortion for arbitrary stochastic cyclic filters, including asymmetric and sparse-support cases for the norm. The exact finite heat law identifies the time dependence, including all derivative signs and the role of cycle parity. The value lies in the finite discrete classification and exact sharp heat behavior, not in reprinting the classical kernel or upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
