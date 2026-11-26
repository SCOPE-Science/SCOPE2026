# Independent mathematical audit

## correctness

PASS

Lucas factors the binomial-cube sum digit by digit, including zero-padded digits since f(0)=1. All eleven digit values are units, and the two-digit convolution is positive at all ten units. In the cyclic exponent coordinate the autocorrelation polynomial reduces at primitive tenth roots to 9+2X-2X²+2X³-2X⁴ = 11−2Φ₁₀(X), and at primitive fifth roots to 5−2X²−2X³ after subtracting 24Φ₅(X). The remaining evaluations at 1 and −1 are 121 and 1. This gives the stated spectral multiplicities, and Parseval with normalization 1/10, deleting just the trivial character, yields the centered variance, also at r=0. Any aligned block is a permutation of the unit histogram by multiplication by its prefix value. Fourier inversion costs at most (9/10)11^(r/2) per block; up to ten blocks of each size and the geometric sum give the stated arbitrary-cutoff constant. The variance lower bound implies the 1/5 lower bound for at least one unit at each depth, not a lower bound for every fixed unit. An independent exact raw-residue transfer through depth 12 and direct binomial sums at all 121 indices below 11² passed; replay with python3 /workspace/audit_checks.py 4.

## originality

PASS

The supported distinct claim is the exact mod-11 variance spectrum and the sharp uniform-in-unit square-root exponent including arbitrary cutoffs. Neither the Lucas product nor the reusable convolution and Fourier framework is new. The primitive-order-ten constant modulus and the smaller nontrivial modes depend on the special Franel digit distribution, and are not implied without an exact spectral calculation by the prior structural results inspected.

## value

PASS

For a classical sequence and a small prime with a zero-free digit table, it is natural to ask how the unit residues balance and at what rate. The exact variance quantifies finite-block nonuniformity and reveals a four-mode spectral edge exactly at the square-root scale, which turns a qualitative digit recurrence into a sharp discrepancy exponent for arbitrary prefixes. This is more than recomputing a table or reporting a generic spectral-gap bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
