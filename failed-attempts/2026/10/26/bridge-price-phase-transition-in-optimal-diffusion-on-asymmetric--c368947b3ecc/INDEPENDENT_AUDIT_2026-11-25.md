# Independent mathematical audit

## correctness

PASS

On the mean-zero subspace, L≥λ₂P. A positive semidefinite Q vanishing on constants and with edge squared distances (1,s²,1) therefore gives λ₂≤B/tr Q for all individual allocations. In the line regime the centered positions (0,1,1+s,2+s) give this Q as xxᵀ; the leaf equations and one hub equation give the stated conductances and Lx=(B/C_line)x. In the split regime x has positions (−h,0,s,s+1), with ph=q+(q+1)s; the correction p(1−h²)/(p−1) times the left-contrast projector makes every left spoke's Q-distance squared one. It raises tr Q from ph²+s²+q(1+s)² to C_split. The proposed split weights solve Lx=(B/C_split)x and have budget B by p+q(1+s)+s²(1+q+q/s)=C_split. An independent quotient inertia check confirms both gaps: write λ=B/C, decompose into left and right contrasts and the class-constant block, and study the latter after subtracting λI. For s>s_c both leaf pivots are positive. The remaining two-hub Schur complement has a zero direction from x and a negative eigenvalue in its inertia because constants give a negative direction in the quotient. When s≤s_c, b>λ and a=λ. After eliminating the positive right leaf pivot, the left average and U form an invertible two-by-two pivot of negative determinant −pa². The final scalar is zero because x is an eigenvector. Thus there is one quotient eigenvalue below λ and one at λ in both cases, with p−1 additional left contrasts at λ exactly when a=λ. All candidates are positive. Equality of the trace forces (L−λP)Q=0, so Lx=λx; all individual leaf rates and then the bridge are forced by the nonzero jumps. Finally, measuring the positions from 1 gives squared sum C_split; centering them at their mean μ subtracts N(μ−1)², giving the claimed denominator identity. At the positive threshold the weights match with μ=1, the gap is C¹, and its right minus left second derivative is 2B(q+1)²/(NC²)>0 at the common denominator C. For p=q only the strict line regime occurs.

## originality

FAIL

The all-price theorem, including both allocations, the threshold, multiplicities, positivity and uniqueness among unrestricted edge weights, is stated in the earlier indexed record ce2d9d2c11c2. Its price variable is t=s² and its budget is one; homogeneity exactly accounts for the arbitrary positive budget here. The denominator identity and differentiability are direct algebraic consequences of the same branches, not a separate unexplained transition law.

## value

FAIL

As a mathematical law, the threshold illustrates a meaningful change of eigenspace without edge deletion. But the evaluated allocation and this interpretation already follow from the same earlier law. Changing budget and price variables and writing out the derivative mismatch adds no distinct useful exact invariant in this submission.

The dated certificate retains the supplied scientific assessment, sources and limitations.
