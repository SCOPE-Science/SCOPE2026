# Independent mathematical audit

## correctness

PASS

Multiplication cancels both central blocks and yields XY'=X'Y, equivalently AB=0 for A=[X,-X'] and B=[Y';Y], an independent uniform rectangular pair. For fixed r-dimensional S, the number of A with rowspace S is the number of surjections onto S, the product of q^a-q^i for 0<=i<r. The number of B is q^{(m-r)c}. This proves (1); summing over S and dividing by q^{am+mc} gives (3). The exact count vanishes when r>a, including in characteristic two. For a>=m, the product divided by q^{ar} in the surjection count differs from 1 by at most q^{-a}(q^m-1)/(q-1) uniformly in r. Normalization preserves the order of this relative perturbation in total variation. On the diagonal this gives equal mass per subspace and (1,3,1)/5 for q=2,b=1. The ratios to the full-subspace weight for positive diverging a-c and to the zero-subspace weight for negative diverging a-c vanish for every competing dimension. RESULT.md lines 33–61 proves these facts independently of the nine archived small-field checks and six diagonal comparisons. VERIFICATION.md, verify.py and verify_output.txt were read; no supplied code was executed.

## originality

FAIL

The prior three-block result supplies exactly the same change of variables and one-sided zero-product mechanism, in its square regime. Its rank-stratum argument together with the published general rectangular matrix rank counts and nullspace count gives the frozen conditional law by direct substitution and division by the number of equal-dimensional spaces. The fixed-width tilt and extremes then follow immediately from finite products. This is coverage by implication, not a claim that an inspected source prints the fixed-width law verbatim.

## value

FAIL

The balanced equal-mass-per-subspace observation is a useful interpretation. As an independent finding, though, it is the constant-tilt case of a known elementary product after parameter substitution and a finite normalization; the rank-to-subspace lift is forced by symmetry. The extremes and stated error bound also come from that same finite-product calculation. No non-mechanical exact invariant remains to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
