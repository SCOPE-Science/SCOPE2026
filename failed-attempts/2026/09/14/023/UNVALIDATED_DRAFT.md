# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Quartic-slice census for D = 178: the solution set is empty

## Theorem
Let D = 178 = 2 · 89. There is no integer triple (x, y, n) with n ≥ 3,
4 | n, y > 1 and gcd(x, y) = 1 satisfying

    x^2 + 178 = y^n.

In other words, the complete list of such triples, up to the sign of x,
is the empty list.

In fact we prove a stronger statement: there is no integer solution
(x, y, n) with n ≥ 2 even and y > 1 at all (with or without the
coprimality condition, and regardless of the sign of x).

## Proof
Suppose, for contradiction, that integers x, y with y > 1 and an even
integer n ≥ 2 satisfy x^2 + 178 = y^n.

Write n = 2t with t ≥ 1 an integer, and put W = y^t. Then W > 1 is a
positive integer and

    W^2 − x^2 = 178.

Factoring the left side as a difference of squares,

    (W − x)(W + x) = 178.                                    (1)

To handle the sign of x, set a = W − |x| and b = W + |x|. Then a·b = 178
as well, a ≤ b, and a + b = 2W, which is even. Hence a and b have the
same parity (both even or both odd).

Moreover a·b = 178 > 0 and a + b = 2W > 0, so a and b are both strictly
positive integers (if a ≤ 0 then b = 2W − a > 0 would give a·b ≤ 0,
a contradiction). Thus (a, b) is a factor pair of 178 into positive
integers of the same parity.

But 178 ≡ 2 (mod 4): indeed 178 = 4·44 + 2. If a and b had the same
parity and their product were even, they would both have to be even
(two odd numbers multiply to an odd number). Two even numbers multiply
to a multiple of 4. Hence any same-parity factor pair has product either
odd or divisible by 4 — it can never be ≡ 2 (mod 4). Since 178 ≡ 2
(mod 4), no such pair (a, b) exists. This contradicts (1).

Explicitly, the positive factor pairs of 178 are (1, 178) and (2, 89),
both of mixed parity, confirming the obstruction directly.

Therefore no integer triple (x, y, n) with n ≥ 2 even and y > 1 satisfies
x^2 + 178 = y^n. In particular, there is no triple with n ≥ 3, 4 | n,
y > 1 and gcd(x, y) = 1. The solution set in the target range is empty,
and the empty list is the complete answer. ∎

## Remarks
- The argument uses only that D ≡ 2 (mod 4); it applies to any such D,
  but here it is applied with D = 178 = 2 · 89 as required.
- The coprimality hypothesis gcd(x, y) = 1 is not needed for the
  non-existence conclusion; the obstruction already rules out all
  integer x and all y > 1 with n even.
- Computational check: the accompanying script
  `output/artifacts/verify_empty.py` confirms D % 4 == 2, that both
  factor pairs of 178 have mixed parity, and that a brute-force search
  finds no solutions with y < 200 for n ∈ {4, 8, 12} and no solutions
  with n = 4 for y < 5000, consistent with the proved empty list.

## Self-checks performed
1. Verified D = 178 = 2·89 is squarefree context not needed; only
   D ≡ 2 mod 4 is used, and 178 = 4·44+2 is exact.
2. Checked the sign-of-x reduction: replacing x by |x| preserves the
   equation and the factors stay integral.
3. Checked positivity of the factors: a+b = 2W > 0 with ab > 0 forces
   a, b > 0, so the divisor/parity analysis over positive integers is
   legitimate.
4. Checked the parity lemma: same-parity pair with even product ⟹ both
   even ⟹ product divisible by 4. Contrapositive applied correctly to
   178 ≡ 2 mod 4.
5. Checked quantifier scope: every n with n ≥ 3 and 4 | n is even and
   ≥ 4, hence covered by the stronger "all even n ≥ 2" statement.
6. Ran the verification script successfully; brute force agrees with
   the theorem on the searched range.
