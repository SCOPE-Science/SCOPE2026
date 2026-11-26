# Sharp quadratic leading constant for neighborhood traces in finite circle graphs

## Finding
Let \(\mathcal C\) be the class of all finite circle graphs, meaning intersection graphs of chords with distinct endpoints on a circle. Define the *adjacency shatter function* by
\[
\pi_{\mathcal C}(m)=\max_{G\in\mathcal C}\ \max_{A\subseteq V(G),\ |A|=m}\left|\{N_G(v)\cap A:v\in V(G)\}\right|.
\]
For every integer \(m\ge5\),
\[
\boxed{2m^2-4m+1\ \le\ \pi_{\mathcal C}(m)\ \le\ 2m^2-m+1.}
\]
Consequently, the sharp quadratic leading coefficient exists and equals
\[
\boxed{\lim_{m\to\infty}\frac{\pi_{\mathcal C}(m)}{m^2}=2.}
\]
In fact, the lower bound is attained *exactly* as the trace count of an explicitly specified family of marked chord diagrams of every size \(m\ge5\). This is not a claim that the lower bound equals \(\pi_{\mathcal C}(m)\) for all \(m\).

## Assumptions and scope
All graphs are finite, simple and undirected. Chord endpoints in a representation are distinct, and two chords cross if their endpoints alternate. The neighborhood \(N_G(v)\) is **open**: \(v\notin N_G(v)\). The cardinality in the displayed definition includes traces contributed by vertices outside and inside \(A\). Graph size outside \(A\) is unrestricted, so all possible query chords can be added separately to a common marked diagram.

For \(m\ge5\), arrange the endpoints of marked chords in the following cyclic double-occurrence word, with labels \(0,\ldots,m-1\): begin with \(0,1,2,0\); for each integer \(j\) from \(3\) through \(m-1\) append \(j,j-2\); finally append \(m-2,m-1\). Call the resulting word \(w_m\). It contains exactly two occurrences of every label. Let \(T(w_m)\) be the number of distinct crossing patterns a further chord can have with the marked chords. The exact construction statement is
\[
\boxed{T(w_m)=2m^2-4m+1\quad(m\ge5).}
\]

## Proof
**1. Gap-parity identity and universal bound.** Fix any circular representation of \(m\) marked chords and its \(2m\) cyclic endpoint gaps, numbered \(0,\ldots,2m-1\). Define \(S_i\subseteq\{0,\ldots,m-1\}\) as the set of marked labels encountered an odd number of times while moving from gap \(0\) to gap \(i\). An added chord whose endpoints lie in gaps \(i,j\) crosses precisely the labels in the symmetric difference \(S_i\mathbin{\triangle}S_j\). This follows because crossing is equivalent to exactly one endpoint of a marked chord lying in the arc between the query endpoints. The same-gap choice yields the empty pattern. There are at most \(\binom{2m}{2}\) distinct unordered *different-gap* pairs and one empty pattern; hence \(T\le\binom{2m}{2}+1=2m^2-m+1\).

This bound includes traces of the marked vertices themselves: for a marked chord with endpoints \(a,b\), take query endpoints immediately after \(a\) and immediately before \(b\) in the same cyclic orientation. The order is \(a,a',b',b\), so the query chord does not cross the marked chord itself. The order relative to every other marked chord endpoint is unchanged, preserving its other crossings. Thus the original open-neighborhood trace belongs to the gap-parity family. Conversely, every gap-pair pattern can be realized by adjoining a query chord with endpoints in its specified gaps. Add one such query chord for each distinct pattern, choosing distinct endpoints in each gap; because crossings among new chords are unrestricted, all patterns occur together in a finite circle graph. Thus this gap-parity calculation is exact for the largest possible trace family extending a fixed marked diagram.

**2. Prefix masks of the explicit word.** For \(w_m\), direct traversal gives exactly the following \(2m\) *distinct* prefix masks:
\[
\mathcal F_m=\{\varnothing,\{0\},\{m-1\}\}\ \cup\ \bigl\{\{i,i+1\}:0\le i\le m-2\bigr\}\ \cup\ \bigl\{\{i,i+1,i+2\}:0\le i\le m-3\bigr\}.
\]
Indeed its successive prefixes are empty, \(\{0\}\), the blocks \(\{0,1\}\) and \(\{0,1,2\}\), alternating consecutive length-two and length-three blocks with increasing left endpoints, then \(\{m-1\}\). So the set of all possible crossing traces is exactly \(\mathcal F_m\mathbin{\triangle}\mathcal F_m=\{B\mathbin{\triangle}C:B,C\in\mathcal F_m\}\).

**3. Exhaustive run classification.** View a subset of \(\{0,\ldots,m-1\}\) as a binary word; a *run* is a maximal consecutive block of ones. The symmetric difference of two members of \(\mathcal F_m\) has at most two runs. For \(m\ge7\), all of its possible run-length types, and their numbers of distinct placements, are listed below. The symbol \((a,b)\) indicates two separated runs, first of length \(a\), second of length \(b\).

| Run-length type | Number |
|---|---|
| Empty | \(1\) |
| One run of length \(\ell\), each \(1\le\ell\le6\) | \(m-\ell+1\) |
| \((1,1)\) | \(2m-4\) |
| \((1,2)\) or \((2,1)\), each | \(2m-7\) |
| \((1,3)\) or \((3,1)\), each | \(m-4\) |
| \((2,2)\) | \(\binom{m-3}{2}\) |
| \((2,3)\) or \((3,2)\), each | \(\binom{m-4}{2}\) |
| \((3,3)\) | \(\binom{m-5}{2}\) |

For one run, length one can be obtained by removing an end two-block from a three-block; lengths two and three use the empty mask, and lengths four through six use adjacent blocks of lengths two or three. This realizes every placement. For two separated runs with both lengths in \(\{2,3\}\), all placements with at least one zero between the runs arise from disjoint blocks. For lengths \(a,b\) there are \(\binom{m-a-b+1}{2}\) placements, by counting the nonnegative empty lengths before and after the runs and the excess over one in the middle gap.

For a type involving a singleton run, write \((i,j)\) for the two starting indices. Equal overlapping blocks shifted by one give \((1,1)\) at \((i,i+2)\) for \(0\le i\le m-3\) or \((i,i+3)\) for \(0\le i\le m-4\); the two endpoint singleton masks give the exceptional \((0,m-1)\). Two unequal blocks overlapping in one position give \((1,2)\) at \((i,i+2)\) for \(0\le i\le m-4\), or \((2,1)\) at \((i,i+3)\) in the same index range. Using one endpoint singleton and a separated block adds \((1,2)\) at \((0,j)\), \(2\le j\le m-2\), overlapping the previous list just at \((0,2)\); it adds \((2,1)\) by reflection. The types \((1,3)\) and \((3,1)\) arise only from a separated endpoint singleton and three-block; the former occurs at \((0,j)\), \(2\le j\le m-3\), and the latter follows by reflection.

For exhaustiveness, the remaining proper overlap of equal blocks (two three-blocks shifted by two) gives \((2,2)\), already counted in the disjoint placement list. For containment, equal masks cancel, and a two-block inside a three-block leaves one singleton. A singleton used with a block may be separated as above, adjacent (one run), or contained (it shortens the block at its end since the singleton is at an endpoint of the label interval). Every difference has at most six elements, so no additional one-run length can occur.

Adding the entries gives
\[
1+\sum_{\ell=1}^{6}(m-\ell+1)+(2m-4)+2(2m-7)+2(m-4)+\binom{m-3}{2}+2\binom{m-4}{2}+\binom{m-5}{2}
=2m^2-4m+1.
\]
For \(m=5,6\), the same explicit family \(\mathcal F_m\) has respectively ten and twelve masks. Directly comparing their \(45\) and \(66\) unordered different-mask pairs plus the empty mask gives respectively \(31\) and \(49\) distinct symmetric differences, equal to the displayed polynomial. The complete exact calculation is independently reproducible by `verify.py`; these are finite boundary computations, not evidence for the all-size case.

**4. Sharp density.** The universal upper and explicit lower bounds differ by only \(3m\); dividing by \(m^2\) and letting \(m\) tend to infinity yields the claimed leading constant \(2\).

## Verification
Run `python3 verify.py` using Python 3 without external libraries. The executable reconstructs the cyclic word and its prefix masks independently of the closed-form family, checks every gap-pair crossing via its actual endpoint positions, checks the exact trace count for each \(5\le m\le36\), and verifies every run-type multiplicity for \(7\le m\le36\). It also enumerates all \(11{,}464\) chord matchings of sizes \(1\) through \(6\), recording maximal trace counts \(2,4,8,16,31,49\). Its success marker is `VERIFY_OK`. These finite checks support reproducibility; the arbitrary-size result follows from the run classification, not finite extrapolation.

## Relationship to prior work
A previous 2026 study, *Four-query static shattering and logarithmic adaptive depth in circular two-block partitions*, proves that the corresponding binary pair-separation concept class has VC dimension four, including an exhaustive five-query chord-matching calculation. Indeed its two-cut response vectors correspond to **nonempty-gap-pair** crossing traces used here, and its size-five calculation already implies the five-chord \(31\)-trace example after adjoining the empty pattern. Neither the VC-dimension result nor the finite five-query histogram gives the exact all-size sliding-word trace census or its asymptotically sharp leading coefficient.

Another prior computation, *Sharp quadratic type growth of Simon's generic chord quotient* (2026), counts labelled chord-insertion **types** up to dihedral symmetries; it obtains the number of pairs of insertion gaps as a type-growth upper bound. The present invariant instead identifies insertion pairs having the same **Boolean crossing neighborhood**, a substantially coarser quotient. Knowing the number of chord-insertion types does not establish a large image for the neighborhood map, hence does not imply the lower bound proved here.

General VC-density work on Johnson and Hamming graphs gives the shatter-function framework, not this circle-graph value. The 2026 paper on clique-guarded first-order logic with counting establishes general structural bounds and learning connections on sparse classes, not a sharp adjacency-trace coefficient for circle graphs. A contemporary full-text circle-graph recognition paper supplies chord and consecutive-set definitions but does not calculate the present extremal trace function.

## Limitations
The global maximum \(\pi_{\mathcal C}(m)\) is proved only between the stated bounds; the exact lower-bound construction is not asserted to be a global extremizer for all sizes. The result concerns open neighborhoods, not closed neighborhoods or higher-radius balls. The all-size proof uses elementary exhaustive interval-type analysis; its program independently tests only finite sizes. Previously unlocated work on the same shatter function could affect historical priority; searching and comparison cannot establish absolute uniqueness. No independent external mathematical audit is claimed.

## References
1. S. van Bergerem, J. F. Lange, N. Schweikardt, *Complexity of Clique-Guarded First-Order Logic with Counting*, arXiv:2606.24848, first public 2026-06-23; MFCS 2026, DOI 10.4230/LIPIcs.MFCS.2026.20. https://arxiv.org/abs/2606.24848
2. *Four-query static shattering and logarithmic adaptive depth in circular two-block partitions* (2026), public result and proof: https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-four-query-static-shattering-and-logarithmic-adaptive-depth-in-c--68dbb5ccd296/RESULT.md
3. *Sharp quadratic type growth of Simon's generic chord quotient* (2026), public result and proof: https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-sharp-quadratic-type-growth-of-simon-s-generic-chord-quotient--fffb4c5764ff/RESULT.md
4. *Vapnik–Chervonenkis dimension and density on Johnson and Hamming graphs*, Discrete Applied Mathematics, DOI 10.1016/j.dam.2021.09.017.
5. *Circle Graphs Can Be Recognized in Linear Time*, STACS 2026: https://drops.dagstuhl.de/storage/00lipics/lipics-vol364-stacs2026/html/LIPIcs.STACS.2026.72/LIPIcs.STACS.2026.72.html
6. H. Acan, *On a uniformly random chord diagram and its intersection graph*, Discrete Mathematics 340 (2017), DOI 10.1016/j.disc.2016.11.004.
