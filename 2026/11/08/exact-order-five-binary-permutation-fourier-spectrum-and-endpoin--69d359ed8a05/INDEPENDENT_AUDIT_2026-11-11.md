# Independent mathematical audit

## correctness

PASS

The stated Fourier transform is exactly the integer permanent of a 5x5 sign matrix, by expanding the 120 permutation monomials. Row and column sign operations preserve absolute permanent and give precisely 2^9=512 matrices per normalized first-row/first-column +1 representative. The 2^16 remaining entries are exhaustively enumerated, not extrapolated: exact Ryser inclusion-exclusion gives absolute counts 20200,29820,11640,3050,600,200,25,1 for values 0,8,16,24,32,48,72,120. Their sum is 65536, first absolute moment 33045/4096, zero proportion 2525/8192; convolution norm equality follows from finite-group point mass and phase-aligned extremizers. Independent fresh exact Python Ryser enumeration on all 65536 cases plus separate matching formula checks corroborated the coefficients. This is a genuinely finite exhaustive certificate, not an infinite-dimension assertion.

## originality

PASS

The exact order-five sign-permanent multiplicity census and resulting M5(F2) permutation-spectrum endpoint norm are not included in the inspected Wanless possible-values/minimum-positive permanent results, Tao–Vu asymptotic Bernoulli permanent work, or the nearby Resultary Fourier-minor, signed-hafnian and permutation-resonance records. Thus best-of-knowledge priority PASS confined to this natural finite n=5 distribution and its projection interpretation; cannot assert global historical novelty.

## value

PASS

The first nontrivial large-order finite exact absolute-permanent distribution is a natural enumerative invariant of independent random sign matrices, simultaneously computing Fourier support and an exact operator norm for a distinguished permutation-orbit frequency set. Complete unbiased classification over all 2^25 inputs via a proved 512-to-one normalization is independently useful and is not a small arbitrary subset or known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
