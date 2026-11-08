# Sharp one-error cyclic binary pair-profile codes at quarter-multiple lengths

## Finding

Let \(A(n)\) denote the largest number of distinct messages representable by binary cyclic words of length \(n\), under the following observation channel: the receiver sees the *unordered multiset* of the \(n\) cyclic ordered adjacent pairs, and at most one observed pair label may be replaced by any other binary pair. Then for every integer \(m\ge1\),
\[
\boxed{A(4m)=m^2+2}.
\]
More generally, for every \(n\ge4\),
\[
\lfloor n/4\rfloor^2+2\le A(n)\le\lceil n/4\rceil^2+2,
\qquad A(n)=\frac{n^2}{16}+O(n).
\]
An explicit optimal code at length \(4m\) consists of the two constant words and one representative for each mixed pair-profile with coordinates \((k,t)\) satisfying \(k-2t\equiv0\pmod4\), with \(k\) the number of ones and \(t\) the number of cyclic \(01\) transitions.

## Assumptions and scope

Indices lie in \(\mathbb Z/n\mathbb Z\), so a read across the endpoint is included. A pair-profile is the four-count histogram \(p(w)=(p_{00},p_{01},p_{10},p_{11})\), ordered as shown. The receiver loses the positional labels of the reads. A single read corruption changes one *reported pair label* (not one underlying symbol), possibly yielding a histogram not realizable by any cyclic word. The receiver may also see the uncorrupted histogram. Distinct codewords with identical clean profiles cannot represent different messages.

For any cyclic word, set \(k=\sum_i w_i\), \(t=p_{01}=p_{10}\). The last equality follows by conservation of transitions around a cycle. Its profile is
\[
p(k,t)=(n-k-t,t,t,k-t).
\]
The complete feasible set consists of the constants \((0,0)\), \((n,0)\), and
\[
D_n=\{(k,t)\in\mathbb Z^2:1\le t\le\lfloor n/2\rfloor,\quad t\le k\le n-t\}.
\]
The necessity follows because a mixed binary cyclic word has \(t\) positive runs of each symbol. Conversely, for every \((k,t)\in D_n\), the cyclic word
\[
0^{n-k-t+1}(10)^{t-1}1^{k-t+1}
\]
has exactly that profile. These statements include all boundary values.

## Proof

**1. Read-error metric.** On four-coordinate nonnegative integer histograms of fixed total \(n\), changing one reported pair label moves one unit from one coordinate to another. The shortest number of such moves from \(p\) to \(q\) is \(\frac12\|p-q\|_1\). Two radius-one read-error balls intersect if and only if this distance is at most two: a two-step shortest path supplies a common intermediate histogram, whereas the triangle inequality excludes intersection at distance three or more. Using \(|a+b|+|a-b|=2\max(|a|,|b|)\), the induced distance is exactly
\[
\begin{split}
d((k,t),(\ell,u))
&=\frac12\|p(k,t)-p(\ell,u)\|_1\\
&=\max\{|k-\ell|,|t-u|\}+|t-u|.
\end{split}
\]
Consequently, a valid code chooses a subset of feasible points with pairwise distance at least three.

**2. Exact clique upper bound.** Fix \(n=4m\). The first two mixed rows \(t=1,2\) are partitioned by the following \(2m-1\) four-point sets. For every integer \(0\le j\le m-2\), take
\[
\begin{aligned}
B_j&=\{(4j+1,1),(4j+2,1),(4j+3,1),(4j+2,2)\},\\
E_j&=\{(4j+4,1),(4j+3,2),(4j+4,2),(4j+5,2)\}.
\end{aligned}
\]
Add the last set
\[
B_{m-1}=\{(4m-3,1),(4m-2,1),(4m-1,1),(4m-2,2)\}.
\]
Each set is a clique for pairwise distance at most two: the three same-row points differ in their \(k\)-coordinates by at most two, and the fourth point differs by at most one in \(k\) and by one in \(t\). The row ranges show the sets are disjoint and cover both rows exactly.

All remaining mixed points have \(t\ge3\) and are exactly the image of \(D_{4(m-1)}\) under \((k,t)\mapsto(k+2,t+2)\). Induction, starting from the empty mixed set at length zero, gives a partition of all of \(D_{4m}\) into
\[
(2m-1)+(m-1)^2=m^2
\]
disjoint four-point conflict cliques. At most one code point can be taken from each, and at most two more from the two constant profiles. This proves \(A(4m)\le m^2+2\).

**3. Attaining the upper bound.** In each displayed clique the residues \(k-2t\pmod4\) run through \(\{0,1,2,3\}\) exactly once. This property persists under the simultaneous translation by two of both coordinates, so holds inductively for *every* clique. Select precisely the point with residue zero in every mixed clique; add the two constants. This yields exactly \(m^2+2\) profiles.

The chosen profiles have minimum distance three. On a fixed row \(t\), two selected points differ by at least four in \(k\). On adjacent rows, their residue equation forces \(|\Delta k|\ge2\), so the distance formula gives at least three. Rows separated by two or more have distance at least four. A mixed selected point has distance \(k+t\ge3\) from the all-zero profile: for \(t=1\), its smallest possible selected \(k\) is two; for \(t\ge2\), \(k\ge t\) gives at least four. By the symmetric inequality for \(4m-k+t\), it is also at distance at least three from the all-one profile. The two constant profiles are separated by \(4m\ge4\). Thus their corruption balls are disjoint. The explicit word representatives from the previous section produce a code attaining the bound.

**4. General lengths.** For \(N\ge n\), send every mixed coordinate \((k,t)\) of a code at length \(n\) to the same coordinate at length \(N\), keep \((0,0)\) fixed and send the all-one coordinate \((n,0)\) to \((N,0)\). All images are feasible. The displayed metric shows that mixed-to-mixed and zero-to-mixed distances remain equal, while distances involving the all-one point weakly increase. Thus \(A(n)\le A(N)\). Sandwich \(n\) between adjacent multiples of four to obtain both general bounds and \(n^2/16+O(n)\).

## Verification

Run `python3 verify.py` using standard-library Python 3.10 or later. The checker enumerates all binary words of lengths one through thirteen to verify the feasible-profile description and representatives; independently recomputes half-\(\ell_1\) distances; checks the entire recursive clique partition, all clique-residue properties and the chosen-profile cardinality for sixty values of \(m\); and directly computes independent-set optima at lengths four and eight. It prints `THEOREM_CHECKS_OK`. These are finite corroborations; the proof above establishes the infinite family without relying on finite experiments.

## Relationship to prior work

Kiah, Puleo and Milenkovic (2014, revised 2015) develop the noisy-substring-profile framework, the asymmetric histogram distance and general code constructions/asymptotic-order results. Jacquet, Knessl and Szpankowski (2010) enumerate clean Markov types, which are balanced adjacent-pair frequency matrices. Those general results do not, in the inspected material, supply the present sharp \(m^2+2\) upper bound, matching residue construction, or exact sharp noisy-profile leading coefficient \(1/16\). Previously recorded work on linear binary adjacent-pair multispectra counts clean linear observations; research on cyclic symbol-pair distance concerns positional read vectors, not an unordered histogram. Historical-priority verification remains open.

## Limitations

The result concerns binary cyclic words, ordered two-symbol read labels, and at most one arbitrary read-label corruption in the resulting unordered multiset. An error to a *source symbol* can affect two reads and is not covered. Other alphabet sizes, longer windows, dropped reads, and exact off-multiple-of-four optimal sizes are not established. Codebook representatives are not asserted to be unique. The proof and finite checks have not received independent scientific review; no claim of exhaustive literature priority is made.

## References

1. H. M. Kiah, G. J. Puleo, O. Milenkovic, *Codes for DNA Storage Channels*, arXiv:1410.8837, first public version 2014-10-31, https://arxiv.org/abs/1410.8837 .
2. P. Jacquet, C. Knessl, W. Szpankowski, *Counting Markov Types*, DMTCS Proceedings AM (2010), DOI:10.46298/dmtcs.2768, https://doi.org/10.46298/dmtcs.2768 .
