# Independent mathematical audit

## correctness

PASS

Legendre gives the valuation as the digit-sum excess in adding md and m(q−d), divided by p−1. Cyclic carrying of the digit weights modulo r preserves residue modulo m=p^r−1 and decreases the weight by p−1 until a positive r-digit multiple of m remains, necessarily m. More directly on the claimed finite row range, every t from 1 through b=p^r has mt=(t−1)b+(b−t), a pair of complementary r-digit blocks. Thus for 2≤q≤b, all three digit sums at t=d,q−d,q equal r(p−1), so in fact every selected coefficient has valuation r. At q=b+1, the row is p^(2r)−1; subtraction of any selected lower argument involves no borrow and every such coefficient has valuation zero. This proves the GCD result, the least failure, and the scope at both endpoints. Global maximality of r also follows from Fairfax-Ball's bound, or by subtracting the proper selected index mp^(k−r) with k the largest occupied base-p position of N=mq: its r-digit block immediately below position k can induce at most r borrows, ending at or before that nonzero digit. `python3 /workspace/branches/independent_checks.py 1` checked 28,068 exact carry counts at six prime/exponent pairs; this is corroboration, not proof of unbounded quantifiers. The uploaded checker was inspected, not executed.

## originality

FAIL

The claimed new all-index lower bound does not survive implication-level comparison with the exact single-index law that the record itself credits as known. Those laws are equivalent on the plateau by factorial telescoping, and the collapse is the immediate all-digits-p−1 case of Kummer/Lucas. Moreover the Oct. 12 cross-row GCD proof supplies the carry ranges for the single-index law, with a direct residue check showing those ranges exhaust the carries in the pure prime-power specialization. This is substantive coverage by mechanical implication, not a claim that the earlier paper or catalogue entry literally states the new plateau sentence. The exact bibliographic attribution of the single-index congruence was not recovered, but the positive implication and earlier specialized carry analysis are checkable without it.

## value

FAIL

The least-failure question is natural in the extremal-row framework, and the identity can be useful when tabulating examples. For this specific family, however, the apparent extra all-coefficient invariant is mechanically obtained from the antecedent single-index valuation by factorial cancellation, and the zero boundary is the standard all-digits-p−1 row. Compared with that evidence it is a concise corollary, not an independent structural increment. The record establishes no separately motivated new regime beyond that prefix; the universal digit-sum lemma is ancillary and no distinct repaired finding was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
