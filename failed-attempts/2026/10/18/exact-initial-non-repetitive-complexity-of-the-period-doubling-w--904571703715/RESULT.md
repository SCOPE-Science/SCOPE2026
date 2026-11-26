# Exact initial non-repetitive complexity of the period-doubling word at every length

## Finding

Let \(p=p_0p_1\cdots\) be the infinite fixed point beginning in \(0\) of the substitution \(\sigma(0)=01\), \(\sigma(1)=00\). For positive integers \(n\) and nonnegative integers \(s\), put \(F_n(s)=p_sp_{s+1}\cdots p_{s+n-1}\). Define

\[
R(n)=\min\{r\ge 1:\text{some }0\le q<r\text{ satisfies }F_n(q)=F_n(r)\}.
\]

Thus \(R(n)\) is the number of consecutive pairwise distinct length-\(n\) factors seen before the first repetition; this is the *initial non-repetitive complexity*. Denote by \(Q(n)\) the unique earlier starting index \(q<R(n)\) of the first repeated factor.

**Theorem.** One has \(R(1)=2\) and \(Q(1)=0\). For every integer \(n\ge2\), let \(k=\lfloor\log_2 n\rfloor\), so \(k\ge1\). Then

\[
(R(n),Q(n))=
\begin{cases}
(3\cdot 2^{k-1},2^k),&2^k\le n<3\cdot2^{k-1},\\[2mm]
(2^{k+1},0),&3\cdot2^{k-1}\le n<2^{k+1}.
\end{cases}
\]

In particular, the normalized complexity oscillates with the sharp extrema

\[
\liminf_{n\to\infty}\frac{R(n)}n=1,\qquad
\limsup_{n\to\infty}\frac{R(n)}n=\frac32.
\]

## Assumptions and scope

All occurrences are contiguous in the infinite one-sided word \(p\) and are indexed starting at zero. The equality of factors is literal equality as binary strings. A repeated factor is counted when the later occurrence starts, even if its two occurrences overlap. The result concerns all positive lengths, not only powers of two.

## Proof

**1. Decimation.** The substitution gives, for every \(j\ge0\),

\[
p_{2j}=0,\qquad p_{2j+1}=1-p_j.
\]

Consequently no two consecutive entries of \(p\) are both \(1\). Every length-\(n\) factor with \(n\ge4\) contains at least two globally odd positions, corresponding to consecutive entries of \(p\). At least one of these entries is \(0\); hence at least one globally odd position has \(p\)-value \(1\). Every \(1\) of \(p\) is at a globally odd position. Therefore, for \(n\ge4\), factors starting at positions of opposite parity cannot be equal: their \(1\)s occur at opposite parities of local coordinates.

**2. Even length.** Let \(n=2m\ge4\). The alternating zero coordinates in \(F_{2m}(2a)\) and \(F_{2m}(2a+1)\) completely determine these factors. The remaining coordinates, in order, equal the complements of \(p_ap_{a+1}\cdots p_{a+m-1}\). For starts of either one fixed parity, equality of length-\(2m\) factors is therefore equivalent to equality of the corresponding length-\(m\) factors of \(p\). Opposite parities cannot collide, by step 1. The first repeated factor is consequently at \(2R(m)\), and its earlier partner at \(2Q(m)\):

\[
R(2m)=2R(m),\qquad Q(2m)=2Q(m).
\]

**3. Odd length.** Let \(n=2m+1\ge5\). At even starting positions \(2a\), equality is equivalent to equality of \(F_m(a)\), because the factor contains \(m\) globally odd positions. At odd starting positions \(2a+1\), equality is equivalent to equality of \(F_{m+1}(a)\), because the factor contains \(m+1\) globally odd positions. Thus the first possible collision in the even-start class is at \(2R(m)\), while the first possible collision in the odd-start class is at \(2R(m+1)+1\). Since equality of length-\(m+1\) factors implies equality of their length-\(m\) prefixes, \(R(m+1)\ge R(m)\). Hence the even-start collision is strictly earlier, giving

\[
R(2m+1)=2R(m),\qquad Q(2m+1)=2Q(m).
\]

**4. Bases and closed form.** From the initial prefix \(010001010\cdots\), the successive length-one factors start with \(0,1,0\), so \((R(1),Q(1))=(2,0)\). The first length-two collision is \(00\) at starts \(2\) and \(3\), so \((R(2),Q(2))=(3,2)\). The first length-three collision is \(010\) at starts \(0\) and \(4\), so \((R(3),Q(3))=(4,0)\). Steps 2 and 3 show, for every \(n\ge4\),

\[
(R(n),Q(n))=2\,(R(\lfloor n/2\rfloor),Q(\lfloor n/2\rfloor)).
\]

For \(2^k\le n<2^{k+1}\), applying this recurrence exactly \(k-1\) times reduces \(n\) to \(\lfloor n/2^{k-1}\rfloor\). This is \(2\) in the first stated interval and \(3\) in the second. Multiplication of the corresponding base pairs by \(2^{k-1}\) gives the asserted formula for both the collision position and its uniquely determined earlier partner.

Finally, in each first interval the ratio \(R(n)/n\) is largest at \(n=2^k\), where it equals \(3/2\), and it tends to \(1\) at \(n=3\cdot2^{k-1}-1\). In the second interval the ratio is between \(1\) and \(4/3\), and tends to \(1\) at \(n=2^{k+1}-1\). This proves both limiting extrema. \(\square\)

## Verification

The accompanying standalone script `verify_period_doubling_inr.py` generates the word independently by substitution and by parity of the \(2\)-adic valuation of \(j+1\). It compares the generated words and uses literal, collision-free strings to locate the first repeated factor and its earlier partner. It exhaustively checks every length \(1\le n\le256\), together with eighteen additional lengths through \(8192\), including both sides of major formula breakpoints. The program also checks the decimation recurrence. The executed check returned `VERIFY_OK`.

These finite computations are cross-checks, not the proof for unbounded lengths; the preceding induction is the infinite proof.

## Relationship to prior work

Nicholson and Rampersad introduced systematic computations of initial non-repetitive complexity and proved explicit formulas for the Thue–Morse, Fibonacci, and Tribonacci words. Their Thue–Morse theorem differs from the present period-doubling formula away from dyadic lengths. The period-doubling sequence itself and its valuation description are classical and are recorded as OEIS A096268.

OEIS A366462 records the **maximum**, over all starting positions, of the length of a factor whose length-\(n\) subfactors are all distinct. OEIS A367184 records a starting position attaining this maximum and explicitly remarks that the prefix attains it for dyadic lengths. Thus the dyadic case already has substantial prior coverage in these tables; it is **not** offered as an isolated novelty claim. The present theorem instead gives an all-length prefix-collision law, the precise earlier partner of each first collision, and sharp oscillatory asymptotics. Global maxima and their dyadic attainment do not by themselves imply these nondyadic prefix statements.

## Limitations

This is a statement about the fixed starting prefix, not the maximum unique-factor interval anywhere in the sequence. It does not classify all repeated factors or all factor occurrence frequencies. The comparison with available literature and databases does not exclude every unindexed equivalent formulation. No independent scientific audit has been performed.

## References

1. OEIS A096268, *Period-doubling sequence*, original entry 22 June 2004, https://oeis.org/A096268.
2. J. Nicholson and N. Rampersad, *Initial non-repetitive complexity of infinite words*, arXiv:1507.08206, first posted 29 July 2015, https://arxiv.org/abs/1507.08206.
3. OEIS A366462, *Length of the longest word in the period-doubling sequence with unique length-n factors*, https://oeis.org/A366462.
4. OEIS A367184, *First position of a longest word with unique length-n factors in the period-doubling sequence*, https://oeis.org/A367184.
