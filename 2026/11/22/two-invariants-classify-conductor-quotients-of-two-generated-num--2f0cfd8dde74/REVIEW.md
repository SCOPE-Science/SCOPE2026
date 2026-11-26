# Independent mathematical audit

## correctness

PASS

Sylvester symmetry gives c/2 elements of the semigroup below c when zero is included; replacing zero by the absorber leaves that size unchanged. The minimal positive summand is a, so the first length at which all words vanish is ceil(c/a); when a=c=2 the quotient is just the absorber and the formula is still correct. For the reconstruction, c >= a(a-1), and if h=ceil(c/a), then c/a <= h < c/a+1 <= c/(a-1), whence a=ceil(c/h) and b=1+c/(a-1). This independently verifies the frozen strict reconstruction. For a=2, b is absent and any nontrivial quotient is monogenic. For a>=3 both generators are present and are precisely the indecomposables; the powers of b first vanish at a-1, whereas the powers of a first vanish at length >=a if b>=a+2. Thus no exchange is then possible. For b=a+1 all nonempty monomials through degree a-2 survive, those of degree >=a-1 vanish, and the small monomials are distinct because a relation between a and a+1 needs exponent changes divisible by a+1 and a, respectively. Exchange is therefore an actual order-two automorphism, not just a candidate permutation. Inspected the frozen finite checker and recorded output without executing the checker; the uniform proof does not depend on either.

## originality

PASS

The distinct supported contribution is uniform recovery of both generators from the two elementary quotient invariants, together with the explicit automorphism classification. The Frobenius/symmetry count, quotient nilpotency formula and general presentation criterion are established ingredients, not independent novelty claims. Neither the inspected finite tables nor the general criterion supplies the uniform inequality and exact exceptional family.

## value

PASS

A natural unbounded class of quotients from the symmetric-semigroup rigidity conjecture is completely classified by two inexpensive intrinsic invariants, and the exact nonrigid automorphism family is identified. This supplies a reusable reconstruction criterion and a sharp structural boundary, without claiming the general conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
