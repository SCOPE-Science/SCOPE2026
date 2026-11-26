# Independent mathematical audit

## correctness

PASS

The frozen rank-one reduction is incorrect: proof step 4 drops 2r(1-r)u, and verify_sine_b2.py line 14 omits the r term in z, so it encodes the same error. The complete repair is in /workspace/repairs/4; the finding is unchanged. In coordinates t and u=sqrt(t(1-t)) at largest eigenvalue one, the correct change from the rank-one row is 2u(1-2t-2u)r-[(1-t)(3-2t+2u)+2u]r^2. I independently re-expanded both derivative rows and verified this identity modulo u^2=t(1-t). For t>=3/20 the linear term is nonpositive. For t<=3/20 the increasing rank-one function C(t) is bounded above by 633/1000, the linear coefficient is at most 18/25, and the quadratic coefficient in magnitude exceeds 2. Completing the square bounds this full region below 7/10<C(1/4). The off-diagonal row at eigenvalues 1,r increases with |y| up to (1-r)/2, where its excess is -3r^2. Homogeneity handles smaller largest eigenvalues. For the quartic, the exact Sturm sign lists at 0 and 2/3 are (+,+,-,+,-) and (-,-,+,+,-), giving precisely one root in the interval; signs of the quartic at 0 and 1/2 and positivity of the unsquared numerator there ensure no spurious maximizing root. I recover t*=0.2835546102890608... and kappa=0.11878243509575646.... Convexity, density of interior points and the uniform power-series tail give equality of the global Lipschitz coefficient and supremum of derivative norms, with an O(b^4) remainder. Short interior segments recover the boundary orientation without asserting a maximizer at fixed b. An independent eigendecomposition finite-difference check at b=0.1, 0.05, 0.025 supported the leading term; the proof, not those checks, is uniform. The frozen uploaded script was inspected, not executed.

## originality

PASS

The supported distinct result is the sharp positive quadratic excess and its optimal rank-one direction for sine in the specified real 2-by-2 maximum-entry norm. Derivative calculus is prior art; the proof repair changes neither the claim nor its comparison parameters. The checked sources do not give the extremum by theorem specialization or by a matching entry; historical priority is not certified.

## value

PASS

This is the first nontrivial matrix dimension in which the scalar sine contraction might fail in the maximum absolute-entry norm. The proof gives not just a finite-pair failure but the exact optimized excess at leading order, and explains why a diagonal row and rank-one positive spectral endpoint are responsible. This is useful as a sharp low-dimensional benchmark; it makes no higher-dimensional or all-band claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
