# Exact locality-two functional batch code lengths at six and seven requests

## Finding

Let \(L_2(3,t)\) be the least length of a full-rank binary linear code of dimension three that serves **every** multiset of \(t\) nonzero linear-form requests using pairwise disjoint recovery sets containing at most two stored coordinates each. Then the complete two-parameter profile is
\[
\boxed{L_2(3,6)=12,\qquad L_2(3,7)=13.}
\]
Both optima are attained by explicit submultisets of the doubly replicated binary simplex columns. The lower bounds hold for arbitrary binary linear generator matrices, including matrices with repeated or zero columns.

## Assumptions and scope

Work over \(\mathbb F_2\). Represent each nonzero vector of \(\mathbb F_2^3\) by its integer bit pattern in \(\{1,2,3,4,5,6,7\}\), with vector sum represented by bitwise XOR. Let \(G\) be a \(3\)-row matrix of \(n\) columns, of rank \(3\). A recovery set for request \(a\) is a nonempty set of at most two distinct column indices whose XOR equals \(a\). For any multiset of \(t\) nonzero requests, a feasible recovery assignment has disjoint recovery sets, one per request, allowing repeated requests. Columns cannot be reused across requests, and recovery-set size is uniformly at most \(2\). No requirement is placed on efficient on-line decoding or on locality beyond this upper bound.

## Proof

**Lower bounds.** Zero generator columns cannot contribute to a nonzero request from a set of size at most two: a singleton zero recovers zero, and a pair containing zero can be replaced by the other singleton. Delete all zero columns. For each label \(a\in\{1,\ldots,7\}\), let \(x_a\) be its column multiplicity, so \(\sum_a x_a=n\). The maximum number of pairwise disjoint sets of size at most two that recover \(a\) is exactly
\[
M_a=x_a+\sum_{\substack{1\le b<c\le7\\ b\oplus c=a}}\min(x_b,x_c).
\]
There are precisely three unordered pairs of distinct nonzero labels with XOR \(a\). For a fixed \(a\), these three pairs do not share any label, and no pair uses \(a\); therefore this expression is achievable and maximal. Every batch of \(t\) identical requests of type \(a\) requires \(M_a\ge t\).

Each unordered pair of distinct nonzero labels contributes to the sum for exactly one \(a\), namely its XOR. Consequently,
\[
\sum_{a=1}^7 M_a
 =n+\sum_{1\le b<c\le7}\min(x_b,x_c)
 =4n-\frac12\sum_{1\le b<c\le7}|x_b-x_c|.
\]
Write \(n=7h+r\), where \(0\le r\le6\). By balancing integer components (transfer one unit from a larger component to a component at least two smaller), the pairwise absolute-difference sum is minimized when \(r\) components equal \(h+1\) and the remaining \(7-r\) equal \(h\). Its minimum is \(r(7-r)\). Thus a necessary condition for any \(t\)-request locality-two functional batch code is
\[
7t\le 4n-\frac{r(7-r)}2,\qquad r=n\bmod 7.
\]
At \(n=11\), the right-hand side is \(44-6=38<42=7\cdot6\). Hence a six-request code requires at least \(12\) columns. At \(n=12\), the right-hand side is \(48-5=43<49=7\cdot7\). Hence a seven-request code requires at least \(13\) columns. These exclusions also rule out smaller lengths, because any code of shorter length can be padded by extra nonzero columns without losing its recovery property.

**Upper bounds.** At six requests take the multiset of twelve columns
\[
G_6=(1,1,2,2,3,3,4,4,5,5,6,6),
\]
and at seven requests take thirteen columns
\[
G_7=(1,1,2,2,3,3,4,4,5,5,6,6,7).
\]
Each generator has rank three, since it contains the basis \(1,2,4\). In both cases, every nonzero requested symbol has exactly \(t\) pairwise disjoint recovery sets of size at most two when requested repeatedly. This equal-request condition is necessary but not by itself sufficient for functional batch recovery. Sufficiency for arbitrary *mixed* request multisets is established by the finite exhaustive certificate described next.

For \(t=6\), there are \(\binom{12}{6}=924\) multisets of requests chosen from seven labels; for \(t=7\) there are \(\binom{13}{7}=1716\). The artifact `certificates/recovery_witnesses.json` specifies, for each multiset in lexicographic combination-with-replacement order, \(t\) disjoint, nonempty column subsets with no more than two columns each. Every subset is encoded by a bit mask. The independent verifier checks each request's XOR exactly and checks disjointness and cardinality. Thus both generators are functional batch codes with the required locality. Together with the lower bounds, this proves the displayed exact profile. \(\square\)

## Verification

From the artifact directory run `python3 verify.py` (Python 3.10 or later). The program independently reconstructs all \(924+1716=2640\) request multisets, verifies every supplied recovery witness against the literal generator columns, and verifies the two integer lower-bound inequalities. It also exhaustively checks the balancing minimum over all \(12{,}376\) weak compositions of \(11\) and all \(18{,}564\) weak compositions of \(12\) into seven parts. The analytic balancing argument above proves the unbounded integer inequality; these finite checks are consistency checks rather than a substitute for that argument.

Expected terminal conclusion: `ALL_CERTIFICATES_OK`. The program reads no network resources, and the witness data and code are supplied as complete standalone files.

## Relationship to prior work

Oksner, Hollmann, Riet and Skachek (2026; arXiv:2601.12302) study functional batch codes with small recovery sets and provide generic bounds and numerical examples, including a fourteen-column double-simplex construction at eight requests in dimension three. Their Table 2 does not contain these six- and seven-request exact lengths. The published double-simplex construction is *not* claimed as new. Yohananov and Yaakobi (2021; arXiv:2101.06722) establish earlier Hadamard-based functional batch constructions, notably the double-simplex eight-request result. Kılıç, Ravagnani and Salizzoni (2025; arXiv:2508.02586) examine minimum functional batch length generally, without imposing the present size-two recovery restriction in their stated minimum-length problem. Lember and Riet (2024; arXiv:2405.02107) analyze repeated requests and double-simplex service properties; their asymptotic claims and double-simplex construction do not, as stated, imply the two punctured-code optima proved here. An equivalent unindexed finite calculation or a non-obvious general reduction might predate these explicit statements; historical priority is not certified.

## Limitations

Only binary, three-dimensional, linear codes and request counts \(t\in\{6,7\}\) are covered, with recovery-set size at most two and no further constraints on encoding or decoding. The finite certificate proves service for the two displayed generators but does not classify all optimal generators or give an efficient uniform construction for higher dimensions. Independent mathematical audit has not been performed. No assertion of universal historical novelty follows from the bibliography search.

## References

- K. Oksner, H. D. L. Hollmann, A.-E. Riet, V. Skachek, *On the Minimum Length of Functional Batch Codes with Small Recovery Sets*, arXiv:2601.12302, first public January 18, 2026, https://arxiv.org/abs/2601.12302.
- L. Yohananov, E. Yaakobi, *Almost Optimal Construction of Functional Batch Codes Using Hadamard Codes*, arXiv:2101.06722, first public January 17, 2021, https://arxiv.org/abs/2101.06722.
- A. B. Kılıç, A. Ravagnani, F. Salizzoni, *The Length of Functional Batch and PIR Codes*, arXiv:2508.02586, first public August 4, 2025, https://arxiv.org/abs/2508.02586.
- J. Lember, A.-E. Riet, *Equal Requests are Asymptotically Hardest for Data Recovery*, arXiv:2405.02107, first public May 3, 2024, https://arxiv.org/abs/2405.02107.
- H. D. L. Hollmann, K. Khathuria, A. Riet, V. Skachek, *On some batch code properties of the simplex code*, arXiv:2110.07421, first public October 14, 2021, https://arxiv.org/abs/2110.07421.
