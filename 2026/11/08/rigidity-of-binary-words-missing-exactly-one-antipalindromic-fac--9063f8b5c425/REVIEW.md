# Independent mathematical audit

## correctness

PASS

Any shorter antipalindromic suffix of the longest such suffix is also its prefix, so only the longest can be new and the shortfall cannot decrease on extension. An antipalindrome is encoded by its initial bit and a palindromic odd edge string with center zero. For A and B extended by zero, the new longest alternating suffix either exceeds the previous longest alternating run or occurs at the opposite phase from its only prior possible start. A terminal one after A produces no valid suffix. After B, appending one permits a new suffix only when the full edge string is odd; its center is then zero and the whole word is new. After C or D, an appended zero permits at most a singleton with center zero (the 010 suffix has center one), and that singleton's corresponding ordered pair has already occurred in the long alternating run. An appended one gives no new valid suffix: the final 11 cannot start an earlier matching odd suffix. In P an alternating continuation has a valid suffix of letter length at least n-2, and the four phases are distinct already on length four, so an earlier occurrence cannot start in any of the other at most three starting positions. Breaking the edge alternation rules out a longer suffix by its repeated final edges; either differing pair already occurs. The length-seven base was independently exhausted and matches the ten frozen words. Induction gives 2 words of shortfall zero and 8/10 of shortfall one. C and D are terminal states of the bounded-shortfall extension graph, giving exactly 2+2+4 infinite paths. `python3 /workspace/branches/independent_math_replay.py 4` checked 16,256 words at n=7..13 by direct reverse-complement substring sets, and extensions from n=7..41. The latter is only corroboration. Minor clarification outside the Finding: the prefix bound actually implies the same bound for every nonempty factor, since reversal preserves the statistic and the shortfall is therefore nondecreasing under both left and right extension. RESULT.md's line 57 should not be read as a contrary assertion.

## originality

PASS

The maximum and its two alternating extremizers are prior, as is the general defect-increment principle. The distinct claim is the finite defect-one classification and exact counts, with its consequence for infinite prefix paths. No inspected source already supplies those results.

## value

PASS

This is the first stability layer below an established sharp bound on a natural word statistic. It gives a complete finite classification, a parity effect, and exactly eight possible infinite continuations, not merely an additional computed count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
