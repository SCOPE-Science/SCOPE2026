# Independent mathematical audit

## correctness

PASS

Independently, in the frozen exponent order a coefficient polynomial represents a Hamming codeword precisely when it is divisible by the degree-m minimal polynomial g of alpha. Its constant coefficient is 1, and cyclic wrapping is valid since g divides X^n−1. A nonzero word with a zero b-window has a unique maximal zero run of length at least b, since b>n/2; its complement is an arc of length ell≤n−b with both endpoints 1. Rotating this arc to start at zero yields a polynomial of degree ell−1 and constant coefficient 1. It equals g times a monic constant-one quotient of degree ell−1−m. For ell≤m this is impossible, for ell=m+1 the quotient is 1, and for ell=m+j with j≥2 there are 2^(j−2) independent choices. Conversely these words have a unique long zero run, and it contains exactly n−ell−b+1 zero windows. The weight is b+ell−1 and the n rotations do not duplicate each other because the unique run has a unique start. The sum of counts through j=t is n 2^(t−1); subtracting from 2^(n−m) after excluding zero gives the full coefficient. This checks t≤0, b=n and the exact (m,b)=(4,8) example. The phrase 'dimension-three case' is best read as field degree m=3; the corresponding Hamming code has dimension 4. The frozen verification script was inspected, not executed; its expected markers are not a run record.

## originality

FAIL

The nonfull-weight coefficients count the classical exactly-one-burst undetectable patterns in a primitive binary cyclic code, with their lengths relabelled by the number of zero windows. Their exact fixed-span counts follow from the inspected uniform-internal-bits burst fractions, and the only cyclic multiplicity is the n choices of a unique long gap's complement. The saturation branch is already a general cyclic-code theorem. No exact prior printing of this Hamming generating function is required for the implication, and none is asserted.

## value

FAIL

A complete b-symbol weight enumerator is a natural invariant, but this long-window regime is just the single-burst regime of a previously counted binary cyclic-code object, plus saturation. The Hamming field choice contributes no further case distinction or needed unknown invariant. The length-15 illustration and the residual full-weight coefficient do not form a surviving valuable repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
