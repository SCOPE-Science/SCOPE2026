# Independent mathematical audit

## correctness

PASS

Let C=b^c+1 and B=b^d+1. Then B=2 mod C, C is odd, and B,C are coprime. The proposed coefficient attains the product divisibility by (B+b^c)b^(d-c)+1=B(b^(d-c)+1). Independently, reducing n modulo 2d gives k=±b^j+sB (0≤j<d), with n+j divisible by d, hence by 2c. Multiplying kb^n+1 by b^j shows that the C congruence is s=0 mod C on the minus branch, and s=−b^j mod C on the plus branch. The minus branch needs s≥C and already exceeds B+b^c; the plus branch needs s≥1, and j<c requires s≥2 because 1≤b^j<b^c=C−1. For j≥c the plus branch is at least B+b^c. This independently excludes all smaller positive k even when either factor is composite. The observed verification metadata does not represent an independent audit; verify.py was inspected rather than executed, and its finite parameter range is not needed for the proof.

## originality

PASS

Supported distinct claim is the uniform two-designated-factor least positive coefficient under the stated nested even-ratio hypothesis. The strongest exact catalogue hit is the frozen item itself. The primary abstracts support the distinction from sharp single-Fermat-prime bounds and Carmichael classifications; no distinct equivalent pair minimum was substantiated in the inspected evidence.

## value

PASS

This gives the exact first coefficient forcing two prescribed plus-one factors to coexist, a natural strengthening of single-factor restrictions in the sequence k b^n+1. It distinguishes an exact joint threshold and explicit attaining exponent from separate size obstructions, and treats composite factors as well. Solving the simultaneous signed-residue optimization is more than restating CRT or substituting an exponent into a single-factor bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
