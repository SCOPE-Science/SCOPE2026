# Independent mathematical audit

## correctness

PASS

Embed g(x)=(I+N)x+v as a homogeneous matrix. For h=2 or 4 in characteristic two, (g−I)^h has upper blocks N^h,N^{h−1}v and g^h=I+(g−I)^h. Fixed points exist exactly when v∈im N, which is contained in ker N^{h−1}. For a partition with h padded columns, rank N^{h−1}=c_h and rank N=n−c₁, so the two translation counts are q^{n−c_h} and q^{n−c_h}−q^{n−c₁}. The endomorphism ring for the nilpotent module has dimension ∑c_i² and semisimple quotient ∏ M_{c_i−c_{i+1}}(F_q); counting its units gives the stated Z_h(c). Thus subtracting the h=2 counts gives exact order four. There is no such element at n=1, and for n≥2 a size-two nilpotent block and a translation with Nv≠0 give one. Since ∑c_i²≥n²/h, the order-two total is negligible compared with the contribution of the balanced h=4 partition, with relative bound O_q(q^{−n²/4+O(n)}). With c_i=a+d_i, the common factor is q^{−4a²−2as+3a+s}; the only further denominator is Φ_{a+d₄}, converging to Φ_∞ for each d. Extending by zero when a+d₄<0 gives domination by a constant times q^{−E(d)}, where E=∑d_i²+d₄≥(1/2)∑d_i²−1/2. The allowed-translation multiplier is 1−q^{−(d₁−d₄)}. This proves the convergent theta quotient at fixed q. An extreme-to-extreme unit transfer when the spread is at least two drops the squared norm by at least 2 and raises the minimum by at most 1. Hence the balanced tuple of s ones uniquely minimizes E, with E=s. For s=0 the unique tuple at E=1 must transfer directly to zero, so it is (1,0,0,−1); the balanced tuple contributes nothing to the numerator. For s>0 the balanced multiplier is 1−q^{−1}; the total relative weight of the other tuples is O(q^{−1}) and their multiplier differences are at most q^{−1}. The gaps in integer exponents and Gaussian domination uniform for q≥2 yield the claimed O(q^{−2}) error bounds. Independent bounded replay with node /workspace/reviews/evidence/exact-crosschecks.js explicitly enumerates affine permutations and checks g⁴, g² and fixed points on their point sets: all six frozen finite pairs agree, including (420,252) and (43680,18480) at q=2,n=3,4. The supplied checker was inspected, not run. These counts test the normalization and order conditioning, not the infinite limits; no interchange of the two limits has been shown.

## originality

PASS

Pass is for the fixed-field residue-class theta limits of the conditional probability and the subsequent large-field separation, not for any finite enumerative formula. Fulman's framework and Spiga's reported subject overlap at the finite-count level. The primary comparisons that were possible and the nearby indexed work do not establish the two-limit result. The exact Spiga paper was not available for a full comparison; that is an explicit historical-priority risk, not evidence that it lacks the result.

## value

PASS

The order restriction is natural in the study of prime-power affine derangements. The conditional law has a sharp qualitative dependence on dimension modulo four that cannot be read from the general finite enumerator alone. The theta limits describe the full fixed-q probabilities, and the balanced shape's zero multiplier in the divisible-by-four case gives a structural explanation for the opposite large-q regimes. This is not a parameter swap in an unconditioned affine derangement law or an inference from small tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
