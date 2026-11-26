# Independent mathematical audit

## correctness

PASS

The Fubini kernel [y^n-(1-x)^n]/n! for [V,(V*)^n] is global because the common (y-x)_+^n terms cancel. Adjunction swaps orders. For m<n the telescoped sum factors into 2m separable pairs; their left degrees are j and n+j and their right degrees are m-1-j and n+m-1-j, 0<=j<m, with nonzero leading coefficients. Both families are independent; right moments are onto by the real polynomial Gram matrix, so the left span is exactly the range. This proves the repaired statement for all unequal positive orders, including m=1. Independently the original equal-order coefficient matrix has anti-diagonal with mirrored signs and factorial denominators; reversal gives determinant (-1)^m/(product_{r<2m} r!)^2. Multiplication by the Hilbert Gram matrix gives the quoted ratio and reflection pairs the signs. Inspected original verifier and recorded 205 assertions without execution. Newly written standard-library replay /workspace/repairs/1/verify_unequal.py returned PASS: 20 ordered unequal pairs, supporting but not replacing the proof.

## originality

PASS

The repaired contribution is specifically exact rank for unequal orders. The strongest matched fractional record covers the entire equal-order spectral component; that component was removed, not certified as new. No inspected distinct statement covers unequal-order ranks.

## value

PASS

The repaired theorem classifies how many independent directions survive a nonnormal finite-interval commutator at all distinct orders. The lower bound is not mechanical from the rank-two telescope: it shows that none of its 2 min(m,n) channels cancel in aggregate, even as the larger order changes. This is a useful exact structural invariant without reliance on the overlapping equal-order product.

The dated certificate retains the supplied scientific assessment, sources and limitations.
