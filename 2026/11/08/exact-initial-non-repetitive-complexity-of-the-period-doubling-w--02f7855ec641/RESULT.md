# Exact initial non-repetitive complexity of the period-doubling word

## Finding
Let \(p=p_0p_1p_2\cdots\) be the binary period-doubling fixed point of the substitution \(0\mapsto01\), \(1\mapsto00\), beginning with \(0\). For every positive integer \(n\), let \(R(n)\) be the number of consecutive length-\(n\) factors starting at positions \(0,1,\ldots\) that are pairwise different before the first factor equal to an earlier one. Then
\[
R(1)=2,\quad R(2)=3,\quad R(3)=4,\qquad
R(n)=2R(\lfloor n/2\rfloor)\quad(n\ge4).
\]
Equivalently, for the unique integer \(k\ge1\) satisfying \(2^k\le n<2^{k+1}\),
\[
R(n)=\begin{cases}
3\cdot 2^{k-1},&2^k\le n<3\cdot2^{k-1},\\
2^{k+1},&3\cdot2^{k-1}\le n<2^{k+1}.
\end{cases}
\]
In particular,
\[
\liminf_{n\to\infty}\frac{R(n)}n=1,
\qquad
\limsup_{n\to\infty}\frac{R(n)}n=\frac32.
\]

## Assumptions and scope
Positions are indexed starting at zero. A factor of length \(n\) beginning at position \(i\) is \(p_ip_{i+1}\cdots p_{i+n-1}\). A collision at index \(j\) means that some \(0\le i<j\) has the same factor. Thus \(R(n)\) is the **first repeated starting index**, not the length of a longest repeat-free factor beginning at an arbitrary position. The substitution is prolonged on \(0\), so the infinite fixed point exists. All assertions concern this fixed point and every positive length \(n\), with no claims about other initial shifts, other morphisms or the unrestricted non-repetitive complexity.

## Proof
**Step 1 (synchronizing parity).** From the substitution, for every integer \(j\ge0\),
\[
p_{2j}=0,\qquad p_{2j+1}=1-p_j.
\]
Consequently the word has no factor \(11\). It also has no factor \(0000\): four consecutive zeros would include two odd-indexed zeros, whose two parent symbols would both be \(1\), contradicting the absence of \(11\).

Suppose two factors of the same length \(n\ge4\) begin at positions of opposite parity. In the factor beginning at an even position every even-offset symbol is zero; in the factor beginning at an odd position every odd-offset symbol is zero. Equality forces every symbol of their first four positions to be zero, impossible. Therefore equal length-\(n\) factors can start only at positions of the **same parity**.

**Step 2 (decimation of equal factors).** Put \(r=\lfloor n/2\rfloor\) and \(s=\lceil n/2\rceil\). For any \(i,j\ge0\), comparison of the odd-offset symbols in factors beginning at the even positions \(2i,2j\) gives
\[
p_{2i}\cdots p_{2i+n-1}=p_{2j}\cdots p_{2j+n-1}
\quad\Longleftrightarrow\quad
p_i\cdots p_{i+r-1}=p_j\cdots p_{j+r-1}.
\]
The other positions in the two long factors are forced zeros. Likewise, comparison of the even-offset symbols in factors beginning at odd positions \(2i+1,2j+1\) gives
\[
p_{2i+1}\cdots p_{2i+n}=p_{2j+1}\cdots p_{2j+n}
\quad\Longleftrightarrow\quad
p_i\cdots p_{i+s-1}=p_j\cdots p_{j+s-1}.
\]
Thus the earliest repeated *even-start* length-\(n\) factor appears at starting position \(2R(r)\), and the earliest repeated *odd-start* one appears at \(2R(s)+1\).

**Step 3 (first collision).** Since length-\(m+1\) factor equality implies equality of their length-\(m\) prefixes, \(R(m)\le R(m+1)\) for every \(m\ge1\). For \(n\ge4\), Step 1 excludes cross-parity collisions, and hence the first collision is at
\[
\min\{2R(r),\,2R(s)+1\}=2R(r),
\]
which proves the recurrence. Direct inspection of the beginning \(010001010\cdots\) gives the three stated base values: the first repeated factors of lengths \(1,2,3\) start at positions \(2,3,4\), respectively.

**Step 4 (closed form).** For \(k\ge1\), repeated flooring divides \(n\) by two until it reaches either \(2\) or \(3\). If \(2^k\le n<3\cdot2^{k-1}\), then \(\lfloor n/2^{k-1}\rfloor=2\), so \(R(n)=2^{k-1}R(2)=3\cdot2^{k-1}\). Otherwise \(\lfloor n/2^{k-1}\rfloor=3\), so \(R(n)=2^{k-1}R(3)=2^{k+1}\). The lowest normalized values in the dyadic blocks approach one along \(n=2^{k+1}-1\), and the highest are exactly three halves at \(n=2^k\). Within each plateau \(R(n)/n\) decreases, proving the two limits.

## Verification
A standalone Python 3 checker, `verify.py`, generates the fixed point directly from the substitution and computes the first collision by exact comparison of complete byte factors, without probabilistic hashing. It recomputes \(R(n)\) for each length \(1\le n\le512\), compares both the recurrence and closed form, checks the parity identities and the absence of \(11\) and \(0000\) in its generated prefix, and makes 320 additional large-integer consistency checks of the formulas. It prints `VERIFY_OK` if all checks succeed. The proof above, not finite computation, establishes the assertion for unbounded \(n\).

## Relationship to prior work
Nicholson and Rampersad (2015, arXiv:1507.08206) define this initial non-repetitive complexity and determine it for the Thue–Morse, Fibonacci and Tribonacci fixed points, but not the period-doubling fixed point. Huang and Zhang (2014, arXiv:1408.5495) derive general occurrence and gap formulas for individual factors of the period-doubling word (especially Propositions 6.2 and 6.3); these are powerful background, but do not state the first-collision optimization over **all** factors of each length or its dyadic recurrence. Huang and Wen (2016, arXiv:1606.05150) develop individual-factor return-word formulas, again without this initial-complexity law. The OEIS entries A366462 and A367184 describe the **longest** all-distinct-factor window anywhere in the word and where such a window first occurs. Those statistics are different: already at length \(3\), the unrestricted longest-window entry is \(7\), while the initial word contains only \(R(3)+3-1=6\) symbols before repeating a three-letter factor. The formulas here are independent of full factor-complexity enumerations.

## Limitations
The theorem is specialized to the fixed point beginning at position zero. It gives no formula for longest no-repeat windows beginning at arbitrary positions, for all return words or for shifted fixed points. Available prior work on positions of individual factors could conceivably be developed into the same global first-collision formula; an independently audited historical-priority determination remains outstanding. The finite verification stops at length \(512\); the universal claim rests on the parity proof. No independent mathematical audit is claimed.

## References
1. Y. Huang and H. Zhang, *Envelope Word and Gap Sequence in Doubling Sequence*, arXiv:1408.5495, first posted 2014-08-23, https://arxiv.org/abs/1408.5495.
2. J. Nicholson and N. Rampersad, *Initial non-repetitive complexity of infinite words*, arXiv:1507.08206, first posted 2015-07-29, https://arxiv.org/abs/1507.08206.
3. Y. Huang and Z. Wen, *Envelope Words and Return Words Sequences in the Period-doubling Sequence*, arXiv:1606.05150, first posted 2016-06-16, https://arxiv.org/abs/1606.05150.
4. G. Joshi, OEIS A366462 and A367184, entries first contributed October–November 2023, https://oeis.org/A366462 and https://oeis.org/A367184.
