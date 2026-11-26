# Independent mathematical audit

## correctness

PASS

Incrementing n flips exactly ν₂(n+1) trailing ones to zeros and one zero to one, yielding the given first-difference congruence. Every length-three window has one difference 1 because among its two transition indices one is odd. For its reverse to occur it must also have a difference −1; since 1 and −1 are distinct modulo every ℓ≥3, the two differences sum to zero and the original factor is a palindrome. At length four the two parity cases exhaust all windows. When the two outer transition indices are odd, the triple is (1,a,1); otherwise the middle difference is 1 and exactly one even outer transition index is 2 mod 4, guaranteeing an outer zero. Negative reversal of (1,a,1) has neither two outer ones nor an outer zero; negative reversal of the other pattern has middle −1 and an outer zero. Both are excluded from both types. Taking the length-four prefix and the corresponding suffix of the reversal proves the assertion for all longer factors, including the palindrome exclusion. The equivalence classes of factors therefore have no mergers at lengths ≥3. Separately, the replay used the substitution x↦x(x+1) modulo ℓ. For k=12 every output window of length ≤k comes from a parent window of length ≤k, so iterating the bounded factor-set map from 0 to a fixed point gives the exact languages up to that length. It confirmed both claims for ℓ=3,…,9 and the recorded six modulus-four pairs. The proof, not that bounded check, covers every ℓ and length.

## originality

FAIL

Verified full coverage, not merely possible overlap: distinct Resultary record f12270a0ea48, Finding and Proof §§2–3, treats the same digit-sum word and ordinary reversal. Set b=2, so gcd(b−1,m)=1 for every m; its theorem gives every frozen assertion, including modulus four and the exclusion of palindromic as well as nonpalindromic reversible length-four factors. Its base-two proof uses the same parity/difference obstruction. The coverage finding is independent of any inference about authorship or priority from dates. There is no distinct surviving central claim to repair.

## value

FAIL

The motivating question and the all-length obstruction are worthwhile mathematics. But this frozen contribution repeats the base-two theorem and the same local proof already available within a broader result. The finite computations are corroboration, not an additional invariant or use of the method, and the small examples do not supply an independent mathematical contribution. No substantive value survives as a distinct result requiring repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
