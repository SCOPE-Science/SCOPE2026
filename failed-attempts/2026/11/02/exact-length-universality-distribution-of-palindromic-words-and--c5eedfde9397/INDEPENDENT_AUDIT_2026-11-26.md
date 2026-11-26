# Independent mathematical audit

## correctness

PASS

The asserted formulas and extremizer families are true. In RESULT.md 32–45, greedy complete-alphabet blocks give a unique half-word decomposition. Each block ends in its previously missing letter; deleting that last letter gives exactly a remainder missing one letter, so S=A/y. Arbitrary incomplete remainders have series R by inclusion-exclusion. For half H with t arches, let m be the sequence of their last letters. The earliest embedding of m and the rightmost embedding of its reverse bound the intervening letters to R R^rev or R c R^rev, where R here denotes the literal remainder. A missing letter gives an absent length-(2t+1) witness if that interior is incomplete; if the center fills its unique missing letter c, the interior has only one c, so m c c m^rev is absent. The separate full-alphabet blocks supply the matching lower bounds, also at t=0. The extremal proof's line 47 overstates the condition on the remainder of an odd host of index at least 2t+1: it applies only with exactly t half-arches. With t+1 or more the odd host already has length at least 2q(t+1)+1, exceeding the claimed optimum. With exactly t the missing-letter condition forces q−1 residual positions and the equality classification follows; the even/odd competing parity bounds are strict as stated. This local proof slip does not invalidate the result. Independent bounded replay: python3 /workspace/branches/independent_math_checks.py, computing the index by a first-match suffix recurrence and comparing the whole histograms for q=2,3,4 through lengths 15,11,9, respectively. The uploaded verifier was inspected, not run; finite histograms are corroborative only.

## originality

FAIL

The all-length series is exactly the combination of the two parity distributions in a distinct Resultary record. Its displayed later date is not evidence of earlier publication or derivation, so that match alone is not the reason for historical rejection. Independently, the exact all-length claim is a routine specialization of the published palindrome-index characterization and complete-arch enumerator; the extra shortest-host assertions are the immediate minimum-length equalities in that same characterization. No distinct mathematical remainder is established.

## value

FAIL

The distribution is useful as a compact reference for symmetric subsequence hosts, but the offered increment is the direct bookkeeping of a known word-by-word parity rule with the ordinary arch enumerator, and the extremizers are its immediate least-size cases. No new structural or enumerative work survives as a separate valuable claim. Correcting the local extremal proof sentence would not change that judgment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
