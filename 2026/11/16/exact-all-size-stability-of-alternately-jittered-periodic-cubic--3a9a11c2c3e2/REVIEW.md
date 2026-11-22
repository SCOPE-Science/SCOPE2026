# Independent mathematical audit

## correctness

PASS

Substituting cubic B-spline values gives exact four-tap sampled stencil with a=(4-6delta²+3delta³)/6, e=delta³/6, b=(4-6(1-delta)²+3(1-delta)³)/6, c=(1-delta)³/6, summing to one. Cyclic two-cell DFT exactly diagonalizes the N-by-N collocation operator into blocks [[a+e z,b+c/z],[b+c z,a+e/z]]. This conjugate-symmetric block has singular values |a+ez|±|b+cz|. For delta<1/2, bc-ae=(1-2delta)(3delta^4-6delta³+delta²+2delta+1)/36>0, and a+e-b-c=gamma>0, forcing |a+ez|>|b+cz|. Differentiating U(t)-V(t) against t=cos θ shows it strictly decreases and the unique minimum is gamma at t=1; U+V has unique maximum 1 there. The r=0 Fourier modes are constant/checkerboard, extremizers simple. At delta=1/2 the two moduli coincide and one singular value per block vanishes, while a>e keeps the other positive, hence rank N/2. Delta-to-boundary expansion gives kappa~1/(1/2-delta). Independently constructed periodized full matrices at N=4,6,8,10 and δ=0,.25,.4,.5 and matched SVD, including collision. The infinite all-even-N theorem rests on the algebraic Fourier proof.

## originality

PASS

Prior cardinal cubic B-spline collocation conditioning is highly relevant: Novaković–Singer–Singer (2010) full arXiv long version was read, not merely its publisher abstract. It treats symmetric Toeplitz collocation at the knot averages with no alternating point jitter and derives estimates/large-N behavior; not this periodic two-cell exact singular spectrum, though the δ=0 condition-3 limit overlaps. Yu–Townsend addresses trigonometric interpolation, and earlier Resultary two-periodic linear-spline projections use L∞ projection rather than cubic coefficient-to-point ℓ2 singular values. A classical Bloch/Floquet cubic spline analysis might yet yield the full specialization; this is the residual priority risk.

## value

PASS

Alternating sample jitter is a natural structured perturbation in periodic spline collocation. A dimension-independent sharp stability constant, exact full bands, unique checkerboard weakest mode and precisely half-rank node collision describe a meaningful practical stability boundary for all even sample counts. This is more than merely reporting a few small matrices, despite the elementary 2x2 Fourier calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
