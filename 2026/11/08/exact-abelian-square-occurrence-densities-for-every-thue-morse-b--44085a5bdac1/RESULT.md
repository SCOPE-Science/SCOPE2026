# Exact Abelian-square occurrence densities for every Thue–Morse block length

## Finding

Let \(t(j)\) be the classical binary Thue–Morse word, with \(t(j)\) equal to the parity of the number of ones in the binary expansion of the nonnegative integer \(j\). A factor of length \(2n\) is an *Abelian square of block length* \(n\) if its first and last length-\(n\) blocks have the same number of zeros and of ones. For each integer \(n\ge1\), let \(A_n(i)\) be the indicator of this property at zero-based position \(i\), and put

\[
\delta(n)=\lim_{M\to\infty}\frac1M\sum_{i=0}^{M-1} A_n(i),
\]

provided the limit exists.

**Theorem.** Every density \(\delta(n)\) exists. Define \(\eta(0)=1\), \(\eta(1)=-1/3\), and, for integers \(r\ge1\),

\[
\eta(2r)=\eta(r),\qquad
\eta(2r+1)=-\frac{\eta(r)+\eta(r+1)}2.
\]

Then, for all integers \(n\ge1\),

\[
\boxed{\delta(n)=
\begin{cases}
\dfrac{1-\eta(n)}4,&n\text{ odd},\\[4pt]
\dfrac{5+3\eta(n/2)}8,&n\text{ even}.
\end{cases}}
\]

The following bounds and their equality cases are sharp:

- If \(n\) is even, \(1/2\le\delta(n)\le3/4\). Equality on the left holds exactly when \(n=2^{k+1}\), and on the right exactly when \(n=3\cdot2^{k+1}\), for integers \(k\ge0\).
- Among odd lengths, \(\delta(1)=1/3\), \(\delta(3)=1/6\), and for every odd \(n\ge5\), \(5/24\le\delta(n)\le7/24\). Equality at the lower bound holds exactly when \(n\in\{9,15\}\), and at the upper bound exactly when \(n\in\{11,13\}\).

Consequently the unique global minimum is \(\delta(3)=1/6\), whereas the global maximum \(3/4\) is attained precisely at block lengths \(6\cdot 2^k\) for \(k\ge0\).

There is also an exact *pointwise* description of all Abelian-square occurrences:

- At even block length \(n=2r\), every even starting position qualifies. An odd position \(i=2q+1\) qualifies exactly when \(t(q)=t(q+r)=t(q+2r)\).
- At odd block length \(n\), no even starting position qualifies. An odd position \(i=2q+1\) qualifies exactly when \(t(q)\ne t(q+n)\).

All equality cases concern natural densities of indexed starting positions, **not** counts of distinct factor spellings.

## Assumptions and scope

The alphabet is \(\{0,1\}\); factors are contiguous, start at zero-based nonnegative positions, and may overlap. Abelian equivalence refers to the two-letter Parikh vector. The block length \(n\) is fixed before the limit over initial starting positions \(M\to\infty\). The theorem covers every positive integer block length, with no unproved computational cutoff.

For convenient signed notation define \(s(q)=(-1)^{t(q)}\). The identities \(t(2q)=t(q)\) and \(t(2q+1)=1-t(q)\) follow immediately from binary digit parity. In particular, each aligned pair \(t(2q)t(2q+1)\) contains exactly one occurrence of each letter.

## Proof

**1. Exact local conditions.** For a block of length \(2r\) starting at an even position, each of its \(r\) aligned two-letter pairs is balanced, so it has exactly \(r\) ones. Hence any two consecutive blocks of that length starting at an even position have identical Parikh vectors.

For a block of length \(2r\) starting at \(2q+1\), the first letter is \(1-t(q)\), the last letter is \(t(q+r)\), and the middle consists of \(r-1\) balanced pairs. Its number of ones therefore equals

\[
r+t(q+r)-t(q).
\]

The adjacent block has \(r+t(q+2r)-t(q+r)\) ones. Equality of these two counts is equivalent to

\[
2t(q+r)=t(q)+t(q+2r).
\]

Because the three quantities are binary, this equation holds if and only if all three are equal. This proves the even-length pointwise criterion.

For an odd block length \(n=2r+1\), a block starting at \(2q\) has \(r+t(q+r)\) ones, and the next block has \(r+1-t(q+r)\) ones. They can never agree. A block starting at \(2q+1\) has \(r+1-t(q)\) ones, while the next block, now starting at \(2(q+r+1)\), has \(r+t(q+n)\) ones. The two counts agree precisely when \(t(q+n)=1-t(q)\), proving the odd-length pointwise criterion.

**2. The two-point correlation and existence of its natural limit.** Define for integers \(h\ge0\)

\[
\eta(h)=\lim_{M\to\infty}\frac1M\sum_{q=0}^{M-1}s(q)s(q+h).
\]

We first establish existence. Put

\[
B_j(h)=2^{-j}\sum_{q=0}^{2^j-1}s(q)s(q+h),\qquad j\ge0.
\]

Splitting the sum into even and odd \(q\), and using \(s(2q)=s(q)\), \(s(2q+1)=-s(q)\), gives the *exact finite recursions* for \(j\ge1\):

\[
B_j(2r)=B_{j-1}(r),\qquad
B_j(2r+1)=-\frac{B_{j-1}(r)+B_{j-1}(r+1)}2.
\]

Here \(B_j(0)=1\). In particular \(B_j(1)=-(1+B_{j-1}(1))/2\), so \(B_j(1)\to-1/3\). Strong induction on \(h\) through the displayed recursions proves that \(B_j(h)\) converges for every fixed \(h\); the limits obey the stated recurrence for \(\eta\).

To pass from dyadic lengths to all \(M\), consider a dyadically aligned interval \([a2^j,(a+1)2^j)\) with \(2^j>h\). For every offset \(0\le u<2^j-h\), digit additivity without carrying across the dyadic boundary gives

\[
s(a2^j+u)s(a2^j+u+h)=s(u)s(u+h).
\]

Thus the sum of these products over the aligned interval differs from the corresponding length-\(2^j\) prefix sum by at most \(2h\), because only the final \(h\) terms can differ and each product has magnitude one. Decompose \([0,M)\) into its at most \(1+\lfloor\log_2 M\rfloor\) aligned binary blocks. Given \(\varepsilon>0\), choose \(J\) so that \(|B_j(h)-\eta(h)|<\varepsilon\) for all \(j\ge J\). Large blocks contribute at most \(\varepsilon M+O_h(\log M)\) discrepancy, while all smaller blocks together contain fewer than \(2^J\) positions. Division by \(M\) and then \(\varepsilon\to0\) proves the ordinary natural-limit formula.

**3. Conversion from correlations to occurrence densities.** For binary signs \(x,y,z\in\{-1,1\}\), the indicator that all three are equal is

\[
\mathbf{1}_{x=y=z}=\frac{1+xy+yz+xz}{4}.
\]

With \(x=s(q)\), \(y=s(q+r)\), and \(z=s(q+2r)\), its natural mean equals

\[
\frac{1+2\eta(r)+\eta(2r)}4
=\frac{1+3\eta(r)}4.
\]

Half of all starting indices are even and therefore always give Abelian squares of even block length \(2r\). The other half obey the triple-equality condition, giving

\[
\delta(2r)=\frac12+\frac12\cdot\frac{1+3\eta(r)}4
=\frac{5+3\eta(r)}8.
\]

For odd block length \(n\), only odd starts can qualify, and their conditional probability is the limiting frequency of opposite letters at separation \(n\), which is \((1-\eta(n))/2\). Hence \(\delta(n)=(1-\eta(n))/4\). Both limits exist by Step 2.

**4. Sharp extrema and equality cases.** The correlation recurrence gives by strong induction

\[
-\frac13\le\eta(h)\le\frac13\quad(h\ge1).
\]

Indeed the first positive argument has value \(-1/3\), even arguments inherit smaller ones, and an odd argument greater than one is minus the mean of two smaller positive-argument correlations.

We next prove the exact classification

\[
\eta(h)=-\frac13\iff h=2^k,\qquad
\eta(h)=\frac13\iff h=3\cdot2^k
\quad(h\ge1,\ k\ge0).
\]

It holds at \(h=1,2,3\). For even \(h\), halve the index. For odd \(h=2r+1\ge3\), attaining the positive extreme requires both \(\eta(r)\) and \(\eta(r+1)\) to equal \(-1/3\), so \(r,r+1\) must be consecutive powers of two. The only such positive pair is \((1,2)\), yielding \(h=3\). Attaining the negative extreme would require two consecutive numbers of the form \(3\cdot2^k\), which is impossible. Induction completes the classification. Substitution into the formula for even \(n\) yields the even-length bounds and all equality cases.

For odd \(n\ge5\), write \(n=2r+1\) with \(r\ge2\), and set \(C(r)=\eta(r)+\eta(r+1)\). For \(j\ge1\), the recurrence implies

\[
C(2j)=\frac{\eta(j)-\eta(j+1)}2,\qquad
C(2j+1)=\frac{\eta(j+1)-\eta(j)}2.
\]

Therefore \(|C(r)|\le1/3\) and \(|\eta(n)|\le1/6\). Equality requires two adjacent positive indices with opposite extreme correlations, which, by the preceding classification, occur only as the pairs \((2,3)\) and \((3,4)\). These produce precisely the four odd indices \(9,11,13,15\). Direct substitution gives

\[
\eta(9)=\eta(15)=\frac16,\qquad
\eta(11)=\eta(13)=-\frac16.
\]

Thus the odd-length bounds and exact equality cases follow. The exceptional initial values \(\eta(1)=-1/3\), \(\eta(3)=1/3\) give \(\delta(1)=1/3\) and \(\delta(3)=1/6\). Comparing the odd and even ranges yields the global extrema claimed. \(\square\)

## Verification

The standalone script `verify.py` uses only the Python standard library. It checks the exact starting-position criterion against direct Parikh counts for block lengths \(1\) through \(128\) and the first \(2048\) starts, compares empirical frequencies over the first \(65536\) starts against the rational formulas, and tests correlation-extremizer conditions for offsets through \(8192\). From the delivered script, the reproduced output is:

```
VERIFY_OK local_and_density_tests=295046
first_16_densities=1/3,1/2,1/6,1/2,1/4,3/4,1/4,1/2,5/24,5/8,7/24,3/4,7/24,5/8,5/24,1/2
```

The finite computations are consistency tests, not a substitute for the infinite proof above. No numerical experiment establishes the limiting density or the all-period extremizer claim.

## Relationship to prior work

Fici, Mignosi and Shallit's *Abelian-Square-Rich Words* (first posted January 4, 2017) establishes uniform Abelian-square richness of Thue–Morse, counts **distinct** Abelian-square factor spellings by length, and constructs an automaton deciding whether a given indexed factor is an Abelian square. This paper's event predicate and the ability to decide its individual instances therefore predate the present result. The contribution here is instead a closed rational **natural-density sequence over starts at every block length** and a sharp, exhaustive classification of the lengths attaining the extremal frequencies.

Aedo, Grimm, Nagai and Staynova (first posted January 6, 2021) study existence and maximal lengths of monochromatic arithmetic progressions for given differences, including the Thue–Morse word; their results do not give the two-point-correlational frequency distribution used here. Cassaigne, Richomme, Saari and Zamboni study the existence and distributional questions for Abelian powers in words with bounded Abelian complexity, without stating the present closed fixed-period frequencies. Classical Thue–Morse two-point autocorrelations and their recursions are prior tools, not claimed as new.

A previously published all-index decision automaton may in principle be used to recover the same individual occurrence set; an unindexed explicit density/extremizer calculation, or a previously unnoticed corollary of such methods, remains a bibliographic risk. No priority or independence beyond the demonstrated comparison is asserted.

## Limitations

Only Abelian squares, not higher Abelian powers, are classified. The density counts indexed start positions, not distinct word factors or finite-prefix counts exactly. The source comparison cannot rule out an equivalent result outside the inspected literature and records. The standalone computations verify finite instances only; all infinite assertions are supplied by the proof.

## References

1. G. Fici, F. Mignosi, and J. Shallit, *Abelian-Square-Rich Words*, arXiv:1701.00948, first version January 4, 2017. https://arxiv.org/abs/1701.00948
2. I. Aedo, U. Grimm, Y. Nagai, and P. Staynova, *On Long Arithmetic Progressions in Binary Morse-Like Words*, arXiv:2101.02056, first version January 6, 2021. https://arxiv.org/abs/2101.02056
3. J. Cassaigne, G. Richomme, K. Saari, and L. Q. Zamboni, *Avoiding Abelian powers in binary words with bounded Abelian complexity*, arXiv:1005.2514 (2010). https://arxiv.org/abs/1005.2514
4. M. Baake and U. Grimm, *The singular continuous diffraction measure of the Thue–Morse chain*, Journal of Physics A 41 (2008), 422001. https://doi.org/10.1088/1751-8113/41/42/422001
