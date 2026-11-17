# Universal cyclic Thiele winners and an exact triple-block counting law

## Finding
Fix integers \(n\ge 3\), \(1\le r\le n\), and \(0\le k\le n\). Consider \(n\) labeled candidates on a cycle and precisely \(n\) voters, with voter \(i\) approving the \(r\) consecutive candidates \(i,i+1,\ldots,i+r-1\) modulo \(n\). For any common strictly decreasing Thiele weight sequence \(a_1>\cdots>a_r\ge0\), **the entire family of optimal size-\(k\) committees is independent of the weights**: a committee is optimal if and only if every length-\(r\) cyclic block contains either \(\lfloor rk/n\rfloor\) or \(\lceil rk/n\rceil\) selected candidates. In particular, this exactly characterizes every Proportional Approval Voting (PAV) optimizer.

Let \(F(0)=0\), \(F(j)=\sum_{h=1}^j a_h\), \(q=\lfloor rk/n\rfloor\), and \(s=rk-nq\). The maximum total Thiele score is \(nF(q)\) when \(s=0\), and \((n-s)F(q)+sF(q+1)\) when \(s>0\).

For the **triple-block case** \(r=3\), write \(N(n,k)\) for the number of labeled optimal size-\(k\) committees (rotations are distinct unless their selected sets coincide). Define \(h=n-k\), and interpret out-of-range binomial coefficients as zero. Then, for every \(n\ge3\),

\[
N(n,k)=\begin{cases}
1, & k=0\text{ or }k=n,\\[2pt]
\displaystyle\frac{n}{k}\binom{n-2k-1}{k-1}, & 0<k<n,\ 3k\le n,\\[8pt]
\displaystyle\frac{n}{h}\binom{n-2h-1}{h-1}, & 0<k<n,\ 3h\le n,\\[8pt]
\displaystyle\sum_{t\ge1}\frac nt\binom{t}{k-t}\binom{t}{n-k-t}, & n<3k<2n.
\end{cases}
\]

Thus, for example, the winner counts for \(n=12\) as \(k\) ranges from \(0\) through \(12\) are
\[1,12,42,40,3,72,174,72,3,40,42,12,1.\]
At the one-third and two-thirds seat fractions, precisely three labeled committees win. The middle regime admits many additional winners characterized by forbidden cyclic runs.

## Assumptions and scope
A candidate is a labeled position in \(\mathbb Z/n\mathbb Z\). One approval ballot is present for each cyclic translate of a fixed \(r\)-consecutive candidate block; all voter weights are equal. The score of a committee \(W\) is \(\sum_i F(|W\cap A_i|)\). The common Thiele increments are strictly decreasing and nonnegative; the number of candidates, voters and ballots is exactly as specified. The counting formula applies to \(r=3\) only. With merely non-increasing increments, the locally balanced committees remain optimal, but there may be additional optima.

## Proof
**1. The global majorization bound.** Write \(x_j=1\) if candidate \(j\) is selected and zero otherwise. Let \(b_i=\sum_{j=0}^{r-1}x_{i+j}\), with cyclic subscripts. Each candidate belongs to exactly \(r\) ballots, whence \(\sum_i b_i=rk\). The Thiele score is precisely \(\sum_iF(b_i)\). Because the successive increments \(a_j\) strictly decrease, whenever integers \(u,v\) satisfy \(0\le u<v-1\le r-1\), replacing \((u,v)\) by \((u+1,v-1)\) increases the sum of scores by \(a_{u+1}-a_v>0\). Iterating gives the upper bound with exactly \(s\) block counts equal to \(q+1\) and the other \(n-s\) counts equal to \(q\). Equality holds only if all counts differ by at most one.

**2. Attainment for every admissible parameter.** Define a bi-infinite periodic binary sequence by
\[x_i=\left\lfloor\frac{(i+1)k}{n}\right\rfloor-\left\lfloor\frac{ik}{n}\right\rfloor.\]
Since \(0\le k/n\le1\), each \(x_i\) is zero or one. Periodicity follows from shifting \(i\) by \(n\); exactly \(k\) of its first \(n\) entries are one. Every cyclic length-\(r\) sum telescopes to
\[b_i=\left\lfloor\frac{(i+r)k}{n}\right\rfloor-\left\lfloor\frac{ik}{n}\right\rfloor\in\{q,q+1\}.\]
It attains the bound. The equality condition in Step 1 proves the claimed *if and only if* and independence from the strict Thiele weights, including the endpoint sizes \(k=0,n\).

**3. Sparse triple blocks.** When \(0<3k\le n\), the winning condition is that no three consecutive candidates contain two selected ones. Equivalently, the cyclic distance from each chosen position to the next is at least three. Enumerate the \(k\) directed cyclic gaps; they are positive integers at least three and sum to \(n\). The number of ordered gap lists is \(\binom{n-2k-1}{k-1}\) by stars and bars. Choosing the position of the designated first chosen candidate has \(n\) possibilities, while each labeled committee is counted exactly \(k\) times. This yields \(\frac nk\binom{n-2k-1}{k-1}\), including equality \(3k=n\).

**4. Dense triple blocks.** Taking complements exchanges selected and unselected candidates, and maps every local count \(b_i\) to \(3-b_i\). Therefore the dense case \(0<3(n-k)\le n\) has the sparse count with \(h=n-k\).

**5. Intermediate triple blocks.** If \(n<3k<2n\), the required local counts are one or two. Thus a winning cyclic binary word has neither \(000\) nor \(111\) as a cyclic consecutive triple, and conversely. All maximal runs of zeros and ones must have lengths one or two. Let \(t\) be the common number of one-runs and zero-runs. The \(k\) selected positions can be distributed among \(t\) one-runs in \(\binom{t}{k-t}\) ways, choosing the runs with length two; likewise the \(n-k\) unselected positions yield \(\binom{t}{n-k-t}\). Choose the labeled starting point of a designated one-run in \(n\) ways. Each labeled cyclic word is enumerated \(t\) times, once for each of its one-runs, giving the displayed finite sum. Invalid binomial choices vanish, and no run-length configuration is omitted or counted with an incorrect multiplicity.

## Verification
The standalone standard-library program `checker.py` evaluates scores by exact integers, independently of the counting argument. It exhaustively checks all \(131064\) committees for \(3\le n\le16\) in the triple-block PAV model against both the score bound and the exact winner-count formula. It also checks \(24064\) additional committee-rule evaluations across smaller \(n\), several block lengths, and two distinct strictly decreasing weight sequences. All these tests passed. Execute with `python checker.py` from the directory containing the extracted files. This finite enumeration is a consistency check, not the proof for arbitrary \(n\).

## Relationship to prior work
Janeczko and Faliszewski, *Ties in Multiwinner Approval Voting* (2023), previously established general hardness of PAV winner counting and empirically investigated interval-profile ties; their interval experiments are not the full cyclic rotation profile and provide no exact three-regime count. Ai, *The Complexity of Membership, Uniqueness, and Counting for Optimal Proportional Approval Voting Committees* (2026), proves general complexity classifications for membership, uniqueness, and counting. The present result gives a complete exact all-winner structure and closed counting formula for a cyclically translation-invariant structured profile, not a general-complexity claim. Peters and Lackner, *Preferences Single-Peaked on a Circle* (2020), establish polynomial-time computation of a single optimal committee for the broader circle single-peaked domain, but their general linear-programming theorem does not state the all-optimizer local-balance classification or triple-block count. Manurangsi and Sornat (2026) give a polynomial algorithm for Voter Interval elections; Lassota and Sornat (2026) give further structural/parameterized algorithms. Existence and efficient optimization on some larger classes do not by themselves enumerate every optimal committee in this cyclic instance. The strict-scoring universality and explicit three-regime counts are the additional assertions assessed here.

## Limitations
This statement applies only to *full rotation profiles* with exactly one equally weighted ballot for every consecutive block, not arbitrary circular-interval elections or arbitrary voter weights. The exact closed count is restricted to triple blocks, although the exact winner characterization and score formula hold for all block lengths. Strict decrease is required for the necessity direction. A local-balance characterization is not a computational hardness classification. The literature comparison cannot exclude undiscovered equivalent formulations, including in combinatorics of binary circular words; independent publication-priority assessment has not been performed.

## References
- Y. Janeczko and Faliszewski, *Ties in Multiwinner Approval Voting* (2023), previously established general hardness of PAV winner counting and empirically investigated interval-profile ties; their interval experiments are not the full cyclic rotation profile and provide no exact three-regime count. Ai, *The Complexity of Membership, Uniqueness, and Counting for Optimal Proportional Approval Voting Committees*, arXiv:2609.08884v1, first submitted 2026-09-08, https://arxiv.org/abs/2609.08884.
- D. Peters and M. Lackner, *Preferences Single-Peaked on a Circle*, Journal of Artificial Intelligence Research 68 (2020), 463–502, https://doi.org/10.1613/jair.1.11732, https://www.dominik-peters.de/publications/spoc-journal.pdf.
- P. Manurangsi and K. Sornat, *Polynomial-Time Algorithm for Thiele Voting Rules with Voter Interval Preferences*, arXiv:2604.05953v1, first submitted 2026-04-07, https://arxiv.org/abs/2604.05953.
- A. Lassota and K. Sornat, *Algorithms for Structured Elections under Thiele Voting Rules*, arXiv:2607.28575v1, first submitted 2026-07-30, https://arxiv.org/abs/2607.28575.
