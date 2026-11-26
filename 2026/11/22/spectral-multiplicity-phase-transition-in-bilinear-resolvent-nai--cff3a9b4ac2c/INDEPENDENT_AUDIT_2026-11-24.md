# Independent mathematical audit

## correctness

PASS

Independently checked the ingredients and rank calculation in RESULT.md lines 14–117. Put A₀=A−aI and B₀=B−bI. For M=I+xA+yB+xyC, its two factorizations are (I+yB)(I+xA)−γxyR and (I+xA)(I+yB)−γxyR*. Since RA₀=R*B₀=0, multiplying the proposed numerator I−xA₀(I+xA)^−1−yB₀(I+yB)^−1 on the left by M gives (1+ax+by+cxy)I; the product identities cancel the remaining operator terms. In the p decomposition, the equation for the lower block is D(B|_{p⊥}−bI)=γI, forcing invertibility, and the null vector of A₀ forces the upper diagonal Schur term z*D^−1z. Computing the Schur inverse of A leaves K₀=(a/σ)ww* plus a lower block cA₁^−1B₁^−1. Thus K₀ has rank one at c=0 and is coercive at c>0 (the lower term controls p⊥ and w has nonzero p coordinate). Termwise nonnegative gamma integration of (2) yields c/[(b+cx)(a+cy)−γ]=1/(1+ax+by+cxy), normalizing the kernel. At c=0 the scalar kernel instead lies precisely on the exponential ray. The two operator convolutions add one positive coordinate with a spectral exponential kernel; changing variables yields exactly (7)–(8). The gap above each simple isolated minimum makes the corresponding density positive and boundedly invertible on its orthogonal complement at any interior wedge point, with no extra boundary mass. For c>0 convolution preserves absolute continuity and the unsmoothed term gives W≥f_cK₀ pointwise, hence full multiplicity. In the weighted indicator-section dilation, multiplying sections by W^1/2 and testing orthogonality against each indicator times a countable dense set gives exactly the fibers closure ran W^1/2, minimal by construction; the measure can be taken as Lebesgue measure plus the ray probability measure in the critical case. These arguments cover infinite separable dimension. A continuous-spectrum example is obtained by taking D as multiplication by x on L²[1,2] with z=1; polynomials make p cyclic for A, B has a continuous block, and the simple b-eigenprojection plus cyclicity exclude a proper common reducing subspace. A fresh exact complex 3×3 check verified rank and the resolvent product at both c=0 and c>0 with noninteger transform arguments (replay `OPENBLAS_NUM_THREADS=1 python /tmp/opencode/frozen-review-diagnostics.py`, check 4). The frozen checker was inspected, not executed; neither finite calculation proves the infinite-dimensional ranks.

## originality

PASS

Credit the completion criterion, resolvent decomposition and measure ingredients to Tian and the appearance of a rank-one curve and change of measure type in the specific 2×2 jump predecessor. Credit the general rank-to-fiber construction separately. The supported contribution is the complete stratified multiplicity for the full stated spectral-and-cyclicity class, including the arbitrary-dimensional coercivity and critical wedge kernels. The strongest available source comparisons support that distinction, with targeted-access qualifications.

## value

PASS

The spectral multiplicity of the smallest joint dilation is a natural invariant of the representing measure, different from the spectra of A and B. The calculation isolates the geometric source of the new rank-one component and gives the entire rank on each stratum even with infinite-dimensional operators. This is a structural answer beyond detecting a discontinuity in variation or reproducing existence of a POVM.

The dated certificate retains the supplied scientific assessment, sources and limitations.
