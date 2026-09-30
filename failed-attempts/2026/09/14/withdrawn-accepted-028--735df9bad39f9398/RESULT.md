# Misere Dawson's Kayles: Single-Row P-Positions for 0 <= n <= 36

## Context
Dawson's Kayles (octal game 0.07) is the take-and-break game played on rows of pins, and the first cousin of Dawson's Chess (octal 0.137): a Dawson's Kayles heap of n+1 acts like a Dawson's Chess heap of n. Its normal-play Grundy sequence (period 34) was settled by Guy and Smith, but misere play resisted solution for over 70 years. Plambeck and Siegel's misere-quotient theory extended the misere analysis of 0.07 only to heap size 33 with a partial quotient of order 638 whose presentation was omitted as too messy; unpublished genus-theory work by Ferguson reached heap size 24. No prior source publishes an explicit certified single-row misere outcome census to n = 36.

## Definitions
A single row has n pins. A move chooses an adjacent pair at 0-indexed positions (k, k+1) with 0 <= k <= n-2, and deletes that pair together with the immediate neighbours k-1 and k+2 when present. The remainder is the disjunctive sum of a left row of length max(k-1, 0) and a right row of length max(n-k-3, 0) (zero means no row). Play is misere: a player with no legal move in any component wins (the last move loses). A position is P (previous-player win) if the player to move loses with best play, else N (next-player win). A general sum is a multiset of rows; moves act in exactly one component. Terminal sums (no legal move in any component, including the empty sum, (1,), (1,1,...)) are N under misere play.

## Result
Among single rows 0 <= n <= 36, the misere P-positions are exactly

P = {2, 3, 4, 10, 11, 12, 18, 24, 25, 26, 32, 33, 34} (13 positions).

Every other n in range is N:

N = {0, 1, 5, 6, 7, 8, 9, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 27, 28, 29, 30, 31, 35, 36}.

In particular rows 0 and 1 are terminal hence N; rows 2, 3, 4 are P with only N successors; and the head of the range is P, P, P, N, N at n = 32, 33, 34, 35, 36.

## Proof / Evidence
Exhaustive memoized misere outcome recursion over canonical sorted tuples of positive row lengths: win(state) = any(not win(option) for option in moves), with terminal states returning True (N). Every option strictly decreases the pin total, so recursion terminates; all queried sums total at most 36 pins. The main program evaluated 939 memoized states. Certificate: each N position carries an explicit winning move to a P-sum (e.g. n=9 via [1,4] to (1,4); n=17 via [1,12] to (1,12); n=19 via [2,13] to (2,13)); each P position lists every distinct option sum, each confirmed N (e.g. n=12 options (9),(8),(1,7),(2,6),(3,5),(4,4); n=34 options (31),(30),(1,29),...,(15,15)). The auditor independently re-executed the recursion and reproduced the P-list exactly, verified every certificate entry option-by-option, and confirmed bottom-up dynamic programming over all 99133 multisets of rows totaling at most 36 pins (not just reachable ones) yields the identical singles P-set. Move arithmetic L+R+removed == n was checked for every (n,k), confirming the encoded rule matches the stated deletion rule. Normal-play recomputation gives P = {0,1,7,13,23,31,33}, sharply different, confirming the misere census is not mechanically implied by normal play.

## Limitations
Exhaustive only to n = 36 as specified; no periodicity or beyond-36 claim is made. Correctness rests on the stated Dawson's Kayles deletion rule and the misere terminal-win convention. The result certifies single-row outcomes; general sums are used only as auxiliary positions in the recursion.

## Reproducibility
Run `python3 output/artifacts/misere_dawson.py` to recompute outcomes.json and certificate.json; `python3 output/artifacts/verify_misere.py` for the independent reachable-closure plus bottom-up plus certificate check; `python3 output/artifacts/full_partition_check.py` for the exhaustive all-partitions check over 99133 states. Artifacts copied to output/artifacts: misere_dawson.py, verify_misere.py, full_partition_check.py, outcomes.json, certificate.json.

## References
T. E. Plambeck and A. N. Siegel, Misere Quotients for Impartial Games (arXiv math/0609825), Dawson's Kayles analysis to heap 33; Supplementary Material (arXiv 0705.2404), status chart and detailed quotients; T. E. Plambeck, Daisies, Kayles, and the Sibert-Conway decomposition in misere octal games, TCS 96 (1992); A. Flammenkamp, Sprague-Grundy Values of Octal-Games database (normal play); R. K. Guy and C. A. B. Smith, The G-values of Various Games (1956).
