# Sharp parity-dependent capacity of length-bounded palindromic prefix codes

## Finding

Let \(q\ge2\) be an alphabet size and \(N\ge1\) a maximum permitted codeword length. A *palindromic prefix code* is a set of distinct, nonempty palindromes over a labeled \(q\)-symbol alphabet in which no member is a proper prefix of another. Define \(M_q(N)\) as the largest possible number of codewords. For a positive integer \(m\) and a set \(S\) of periods, construct a graph \(G(m,S)\) on positions \(0,\ldots,m-1\), joining each pair of reflected positions and each pair of positions at offset \(t\) for every \(t\in S\). Write \(c(m,S)\) for its number of connected components. Then

\[
M_q(N)=\sum_{m=\lfloor N/2\rfloor+1}^{N}\ \sum_{S\subseteq\{1,\ldots,N-m\}}(-1)^{|S|}q^{c(m,S)}.\tag{1}
\]

A canonical maximizing code consists of the terminal palindromes of the length-bounded palindrome-prefix forest. There may be other maximizing codes; uniqueness is not asserted.

For every fixed \(q\ge2\), as \(h\to\infty\),

\[
M_q(2h)=\frac{2q}{q-1}q^{h}+O_q(hq^{h/2+1}),\qquad
M_q(2h+1)=\frac{q+1}{q-1}q^{h+1}+O_q(hq^{h/2+1}).\tag{2}
\]

The corresponding relative gain over using all palindromes at the single maximal length tends to \(2q/(q-1)\) for even \(N\), and \((q+1)/(q-1)\) for odd \(N\). In particular, for binary codes these limits are four and three respectively.

## Assumptions and scope

The alphabet is finite, labeled and unrestricted; palindromes are ordinary reversal-fixed strings, with the empty word excluded. Prefix-freeness is the only mutual-codeword restriction. Any prefix-free collection of palindromes is also suffix-free, because reversal converts suffix relations to prefix relations. The codeword length is in \(\{1,\ldots,N\}\); no prescribed length distribution, equal probabilities or substitution-distance constraints are assumed.

A positive integer \(t<m\) is a *period* of a word \(w\) of length \(m\) if its symbols in positions \(i\) and \(i+t\) agree for all \(0\le i<m-t\). All positional indices begin at zero.

## Proof

**1. Prefix-forest reduction.** The finite set of nonempty palindromes of length at most \(N\), ordered by being a prefix, is a rooted forest, since the proper prefixes of any fixed word form a chain. Let \(\mathcal L\) be its set of terminal nodes. Distinct terminals are incomparable, so \(\mathcal L\) itself is a prefix code. Every node has a terminal descendant, and descendants of distinct codewords in a prefix code are disjoint. Therefore assign to every codeword one of its terminal descendants injectively, proving that no code is larger than \(|\mathcal L|\) and \(M_q(N)=|\mathcal L|\).

**2. Palindromic extension versus a period.** Let \(w\) be a palindrome of length \(m\). If it has a palindromic extension \(v\) of length \(m+t\) with \(0<t<m\), then \(v\) has \(w\) both as prefix and as suffix. Their overlap implies that \(t\) is a period of \(w\). Conversely, if \(t<m\) is a period, append to \(w\) its final \(t\) symbols. The result has \(w\) as prefix and suffix; because these copies overlap and both are palindromes, the entire result is palindromic. Thus such an extension exists if and only if \(w\) has period \(t\).

For \(m\le \lfloor N/2\rfloor\), the word obtained by appending another copy of \(w\) is palindromic (\(ww\) is the concatenation of identical palindromes) and length at most \(N\), so \(w\) is not terminal. For \(m>N/2\), every possible extension has offset \(1\le t\le N-m<m\). Consequently the terminal nodes are exactly the palindromes of lengths \(m>N/2\) with no period in \(\{1,\ldots,N-m\}\).

**3. Exact count.** For \(S\subseteq\{1,\ldots,N-m\}\), the palindromes having *all* periods in \(S\) are precisely the symbol assignments constant on connected components of \(G(m,S)\). There are exactly \(q^{c(m,S)}\) such words. Inclusion–exclusion over the forbidden periods gives the terminal count for each length \(m\). Summing proves (1).

**4. Parity-dependent asymptotics.** There are \(q^{\lceil m/2\rceil}\) palindromes of length \(m\). Summing this over the candidate lengths \(m>N/2\) gives \(\frac{2q}{q-1}q^h+O_q(q^{h/2+1})\) when \(N=2h\) and \(\frac{q+1}{q-1}q^{h+1}+O_q(q^{h/2+1})\) when \(N=2h+1\). These are just finite geometric sums with parity-paired terms.

For a palindrome of length \(m\) having period \(t<m\), the word is determined by its \(t\) residue classes modulo \(t\), and reversal imposes equality under the involution \(r\mapsto m-1-r\pmod t\). This involution has at most two fixed residues; the number of symbol orbits is at most \(\lfloor t/2\rfloor+1\). Hence at most \(q^{\lfloor t/2\rfloor+1}\) palindromes of length \(m\) have period \(t\). Summing this upper bound over \(m>N/2\) and \(1\le t\le N-m\) gives \(O_q(hq^{h/2+1})\). Subtracting these nonterminal candidates from the geometric sums yields (2). The estimate holds uniformly in \(h\) for fixed \(q\); no assertion uniform in growing \(q\) is made.

## Verification

The standalone Python files `verify_direct.py` and `verify_period.py` independently check the claim. The first directly constructs the palindrome-prefix forest and evaluates the maximum-antichain dynamic-programming recurrence on its immediate child relations; it agrees with the terminal count for 28 listed cases. The second computes (1) by disjoint-set unions and independently enumerates palindromes excluded by periods: agreement holds for binary \(N\le14\), ternary \(N\le10\), and quaternary \(N\le8\). These computations corroborate the finite identities but do not replace the all-parameter proof above.

Binary values for \(N=1,\ldots,14\) are \(2,2,4,6,10,16,26,38,62,88,140,194,304,418\). Ternary values through \(N=10\) are \(3,3,9,15,33,57,123,195,411,639\). Run with `python3 verify_direct.py` and `python3 verify_period.py` under Python 3, no external dependencies.

## Relationship to prior work

The problem belongs to symmetric fix-free or reversible-variable-length coding: palindromic prefix codes are automatically suffix-free. Earlier coding work addresses constructing reversible codebooks for assigned source probabilities or a given sequence of codeword lengths, not the exact maximum number of arbitrary-length codewords under a common length ceiling. Abedini, Khatri and Savari (2010) give a SAT formulation for specified length sequences and enumerate *dominant length sequences for a fixed number of source symbols*. Their tabulated values should not be mistaken for the values in (1). The 1996 reversible-code patent details probability-driven symmetric code construction. The period-exclusion characterization, exact length-ceiling count, and parity-dependent capacity constants are the precise additional claims here.

## Limitations

The inclusion–exclusion formula may be exponential-time to evaluate when the length ceiling grows; it is an exact finite formula, not a claimed polynomial-time algorithm. No count of *all* maximum codebooks is given, and no distance/noise-correction guarantee is implied by prefix-freeness. The literature assessment cannot exclude an unindexed older equivalent formula, particularly in specialized symmetric-code construction articles. Independent mathematical audit has not been performed.

## References

1. U.S. Patent 5,488,616, *System for providing reversible variable length codes*, issued 1996-01-30. https://patents.justia.com/patent/5488616
2. N. Abedini, S. P. Khatri and S. A. Savari, *A SAT-Based Scheme to Determine Optimal Fix-free Codes*, Data Compression Conference (2010), DOI 10.1109/DCC.2010.22. https://www.mit.edu/~medard/Itpaperaward/A%20SAT-Based%20Scheme.pdf
3. H.-W. Tseng and C.-C. Chang, *Construction of Symmetrical Reversible Variable Length Codes Using Backtracking*, The Computer Journal 46(1) (2003), 100–105. https://academic.oup.com/comjnl/article-abstract/46/1/100/415459
