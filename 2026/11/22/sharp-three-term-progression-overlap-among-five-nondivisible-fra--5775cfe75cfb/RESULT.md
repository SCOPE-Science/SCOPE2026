# Sharp three-term progression overlap among five-nondivisible Franel indices

## Finding
Let \(F_n=\sum_{j=0}^{n}\binom nj^3\) for \(n\ge0\), and let \(E=\{n\ge0:5\nmid F_n\}\). For every fixed positive integer \(h\), the normalized triple-progression frequency
\[
T(h)=\lim_{r\to\infty}4^{-r}\#\{0\le n<5^r:n,n+h,n+2h\in E\}
\]
exists. It satisfies the **sharp all-shift theorem**
\[
0\le T(h)\le\frac13,\qquad T(h)=\frac13\quad\Longleftrightarrow\quad h=a5^j\quad(a\in\{1,2,3,4\},\ j\ge0).
\]
Thus the largest conditional three-term progression overlap is exactly one third, and the only maximizing steps have one nonzero base-five digit. Ordinary natural density is zero, making the sparse-set normalization essential.

## Assumptions and scope
All indices are nonnegative integers and \(h\) is held fixed as \(r\to\infty\); the indices \(n+h,n+2h\) are **not** reduced modulo \(5^r\). A base-five digit is *allowed* when it is in \(A=\{0,1,3,4\}\). The number of allowed starting indices in \([0,5^r)\) is exactly \(4^r\). The theorem concerns simultaneous nondivisibility by five, not the signed quadratic-character correlation or numerical distribution modulo higher powers of five.

## Proof
**1. The digit restriction.** Lucas's binomial theorem applied to every term of the Franel sum gives, for \(n=\sum_{i\ge0}n_i5^i\),
\[
F_n\equiv\prod_{i\ge0}F_{n_i}\pmod5.
\]
The five initial Franel values are \(1,2,10,56,346\), congruent to \(1,2,0,1,1\) modulo five. Therefore \(n\in E\) if and only if every base-five digit of \(n\) is allowed. In particular, there are exactly \(4^r\) such indices below \(5^r\).

**2. A finite carry process.** Select the digits of \(n\) independently and uniformly from \(A\), reading least significant first. At one digit place, let \(a\in\{0,1,2,3,4\}\) denote the digit of \(h\), and keep the state \(s=(c_1,c_2,t)\in\{0,1\}^3\). Here \(c_1\) and \(c_2\) are carries into the additions \(n+h\) and \(n+2h\), and \(t\) is the carry into the doubling of \(h\). Put \(b=(2a+t)\bmod5\), \(t'=\lfloor(2a+t)/5\rfloor\). For each allowed starting digit \(d\in A\), set \(x=d+a+c_1\), \(y=d+b+c_2\). Retain the choice only if \(x\bmod5,y\bmod5\in A\); the next state is \((\lfloor x/5\rfloor,\lfloor y/5\rfloor,t')\). All carries remain zero or one. Define \(\mathcal T(s,a)\) to be the multiset of retained next states, counting the different allowed \(d\) separately.

Let the integer potential \(w(s)\) equal \(3\) for \(s=000\) and \(s=111\), and equal \(2\) for the remaining six states. The complete finite computation of \(\sum_{s'\in\mathcal T(s,a)}w(s')\), with columns in order \(a=0,1,2,3,4\), is

| State \(s\) | \(w(s)\) | \(a=0\) | \(a=1\) | \(a=2\) | \(a=3\) | \(a=4\) |
|---|---:|---:|---:|---:|---:|---:|
| 000 | 3 | 12 | 4 | 4 | 4 | 4 |
| 001 | 2 | 8 | 5 | 6 | 5 | 8 |
| 010 | 2 | 8 | 5 | 6 | 5 | 8 |
| 011 | 2 | 7 | 5 | 5 | 7 | 8 |
| 100 | 2 | 8 | 7 | 5 | 5 | 7 |
| 101 | 2 | 8 | 5 | 6 | 5 | 8 |
| 110 | 2 | 8 | 5 | 6 | 5 | 8 |
| 111 | 3 | 4 | 4 | 4 | 4 | 12 |

Each entry is at most \(4w(s)\). The table follows by the four explicitly specified digit choices, with a standalone exhaustive reproducer in `verify.py`. For an infinite all-zero digit suffix of \(h\), let \(q(s)\) be the probability that all subsequent three digit streams remain allowed. Solving \(q(s)=\frac14\sum_{u\in\mathcal T(s,0)}q(u)\), with \(q(000)=1\), gives in state order \(000,001,010,011,100,101,110,111\) the values \(1,2/3,2/3,7/12,2/3,2/3,2/3,1/3\). This solution is the actual infinite-tail probability, since a nonzero carry persists under consecutive zero digits only when each new starting digit is the maximal allowed digit, an event of vanishing probability. All eight values satisfy \(q(s)\le w(s)/3\). Applying the finite table inequality backwards from this **verified zero-tail boundary** through the finitely many nonzero digits of the integer step \(h\) establishes that the entire remaining acceptance probability from state \(s\) is at most \(w(s)/3\). No incorrect finite-horizon terminal bound is used.

**3. First nonzero digit and the sharp upper bound.** An initial zero digit of \(h\) leaves state \(000\) unchanged and accepts all four choices for \(n\). At the first nonzero digit \(a\), the state \(000\) has exactly two retained choices. For \(a=1,2\), their next states are \(010\) and \(110\); for \(a=3,4\), they are \(001\) and \(101\). All four states have potential \(2\). The future acceptance probability is therefore at most
\[
\frac14\left(\frac23+\frac23\right)=\frac13.
\]
This holds for every finite positive step \(h\).

**4. Equality and strictness.** If \(h=a5^j\) with \(a=1,2,3,4\), all later digits of \(h\) are zero. For each of the four states \(001,010,101,110\), repeated zero-step transitions have exact eventual acceptance probability \(2/3\): their transitions lead twice to \(000\) and once to either \(010\) or \(110\), and these latter states satisfy \(q=(2+q)/4\). Hence \(T(a5^j)=\frac13\).

Conversely, suppose \(h\) has a second nonzero digit. Before that digit, zero-step transitions from the four initial states either reach \(000\) or remain in those four states; every one of these possibilities is realized with positive probability. At a second nonzero digit \(a=1,2,3\), the table inequality is strict in every such state. At \(a=4\), the inequality is strict in state \(000\); from each of the four other states, a retained transition with positive probability enters \(111\). For state \(111\), equality of the potential inequality is possible only when each next digit of \(h\) is \(4\). Since \(h\) is a finite integer, an eventual zero digit makes the inequality strict. Positive-probability paths with strict inequality prevent equality in the initial bound. Therefore no shift with two nonzero base-five digits attains \(1/3\), completing the proof.

**5. Existence of the limit.** Extend the random allowed digits of \(n\) to an infinite product measure on the five-adic digit space. Finite-prefix acceptance probabilities decrease to the probability of full simultaneous membership in the allowed-digit set. For a fixed \(h\), once past its most significant digit, any nonzero carry in the addition must traverse a string of maximal starting digits to persist. Such a string of length \(q\) has probability at most \(4^{-q}\). Thus the difference between the finite \(n<5^r\) count (with zeros above position \(r-1\)) and the infinite-product acceptance probability tends to zero as \(r\to\infty\). This establishes existence and identifies the limit calculated above.

## Verification
Running `python3 verify.py` checks all forty entries of the exhaustive carry table and its superharmonic inequalities, computes exact zero-tail acceptance probabilities, tests all first-nonzero-digit transitions, and independently compares the derived bound and equality cases with direct digit tests for finite blocks and numerous shifts. The computations verify the finite table used in the unrestricted proof; they are not treated as an infinite extrapolation.

## Relationship to prior work
The classical Franel-number identities and congruences are documented by Sun (2011). Schulte, VanSchalkwyk and Yang (2014, Theorem 2.24) already prove the precise forbidden-digit characterization for nondivisibility by five; it is a premise, **not** claimed as new. Existing evaluated signed two-point Franel correlations, including their complete shift spectrum, concern pairs \((n,n+h)\), not the simultaneous three-term progression \((n,n+h,n+2h)\). The new contribution is the sharp universal triple-intersection bound and its complete extremizer classification. Likewise, results about intersections of a different three-adic Cantor set under multiplication do not imply this additive three-point fifth-adic theorem. An unindexed general theorem on multi-point digit-Cantor correlations could still subsume the claim.

## Limitations
The result is for the prime five and the third binomial-power sum, and does not give the full distribution of triple overlaps across all shifts or higher-power Franel valuations. The proof uses a special eight-state finite carry inequality rather than a universal theorem for arbitrary digit alphabets. The historical-priority survey is not exhaustive; no independent mathematical review is asserted.

## References
1. Z.-W. Sun, *Congruences for Franel Numbers*, arXiv:1112.1034, first public version 2011-12-05, https://arxiv.org/abs/1112.1034.
2. A. Schulte, S. VanSchalkwyk and A. Yang, *On the divisibility and valuations of the Franel numbers*, MSRI-UP Research Reports (2014), pp. 127–161, especially Theorem 2.24 and Theorem 2.25. https://slmath-production-assets.sfo3.digitaloceanspaces.com/system/cms/files/81/files/original/Research_Reports_2014_MSRI-UP_%28Single_File%29.pdf.
3. E. Rowland and R. Yassawi, *Automatic congruences for diagonals of rational functions*, arXiv:1310.8635, first version 2013-10-31, https://arxiv.org/abs/1310.8635.
