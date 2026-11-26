# Independent mathematical audit

## correctness

PASS

Product Laplacian separation gives a_t(0)=1 and (L_h+2tI)a_t=0 off the origin for a face Walsh character of weight t; the grounded Dirichlet system is invertible. At t=0 the multiplier is constant. At t>0 it is the resolvent column divided by its diagonal. Cubical Walsh orthogonality gives G_t(0,0)=2^(−h)Σ_j binom(h,j)/(2(j+t)) and (G_t²)(0,0)=2^(−h)Σ_j binom(h,j)/(4(j+t)²); their normalized ratio is exactly the stated Gram eigenvalue. The killed-walk representation gives strict decrease in t off the origin, since the first hit is finite and strictly positive there. The constant sector has squared norm factor 2^h. Parseval host analysis leaves the Gram unchanged. In the remaining t=1 maximization, cross-multiplying F_(n+1)<F_n with z=2^n gives C_nT_n>R_n. Summing the quadratic truncation of 1/(n−r) with weights 2^(n−r)−1 gives the stated U_n; expanding U_nC_n−R_n and using 2^n≥n³/2 gives the positive bound in the proof for n≥8 (the negative parenthesis is bounded above by 43). Exact small values then give the unique maximum at h=4. An independent radial solve there gives a_0 through a_4 equal to (1,13/62,8/93,3/62,1/31); summing binomial-weighted squares gives 3548/2883. All nonzero equality data are in the weight-one sector at h=4; the zero input of course gives trivial equality at any h. Finite rational replay independently reproduced all seven low-codimension values. The supplied NumPy checker was inspected, not executed.

## originality

PASS

The exact positive-weight-one spectral family, including 3548/2883 at one dimension, has a demonstrable same-day indexed equivalent in the leaf-contrast space of cubical star completion. No date-based priority claim is made. The distinct supported content is the sharp all-codimension upper bound and nonzero cubical-face equality classification, not discovery of that scalar value or of the shifted Green formula.

## value

PASS

The result separates the unbounded constant-sector amplification from uniformly controlled mean-zero stability in a motivated graph-to-host lift. The optimal constant and exact equality tell which embedding depth and which face modes give the worst amplification, independent of k and of the host Parseval representation. The nontrivial new maximization over infinitely many codimensions, rather than merely the known scalar table or general harmonic completion, supplies that benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
