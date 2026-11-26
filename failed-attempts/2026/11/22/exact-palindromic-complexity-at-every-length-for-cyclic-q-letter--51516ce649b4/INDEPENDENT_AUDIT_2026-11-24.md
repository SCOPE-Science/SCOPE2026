# Independent mathematical audit

## correctness

PASS

In positive indexing write the center c=2^r m with odd m. For offsets of valuation unequal to r both side valuations are their minimum with r. For t=2^r z with odd z, one side's additional valuation is 1 and the other must be 1 modulo q to match. If offsets 2^r and 3·2^r both occur, the first matching forces m congruent to ±1 modulo 8, and at the second the additional valuations are 1 and 2, which do not match. Thus only r>=k+1, r=k, and possibly r=k-1 survive for 2^k<=h<2^(k+1). Large r gives all q different center letters in the same offset profile. r=k gives one exceptional profile; r=k-1 gives another precisely when k>=1 and h<3·2^(k-1). In both exceptional cases m=1+2^(q+1) is large enough for c>h and realizes the needed match; the changed offset at 2^(k-1) separates the latter profile from the former and baseline. The h=1 case simply has no negative r. Equal adjacent letters must both be zero with the even position of valuation a positive multiple of q, so the outer even neighbor has valuation 1 and the outer odd neighbor has valuation 0. That proves the length-two and no-longer-even claims, and powers of two realize all singleton letters. This counts words, not their occurrences.

## originality

FAIL

Demonstrably covered as a direct counting corollary of Barro–Kaboré–Bognini (2022), Theorems 3.1–3.2 and their note on even palindromes. The previous paper need not print the closed form: it gives the exact distinct-word desubstitution from which that form follows by elementary halving. The frozen result's valid valuation proof is an alternative proof of the covered count, not evidence the invariant was previously undetermined.

## value

FAIL

The complete palindrome complexity is a natural invariant and the arithmetic proof is valid, but the frozen finding is the count and sharp profile already obtained by routine length bookkeeping from the published morphism theorem. It does not establish an independently new structural or quantitative remainder beyond that covered census. A clearer proof of a covered exact invariant does not on its own rescue the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
