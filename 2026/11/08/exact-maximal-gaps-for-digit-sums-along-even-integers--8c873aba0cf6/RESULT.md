# Exact maximal gaps for digit sums along even integers

## Finding

Let \(q\ge2\) be an integer and \(s_q(m)\) the sum of the base-\(q\) digits of \(m\ge0\), with \(s_q(0)=0\). For each residue \(j\in\{0,\ldots,q-1\}\), define
\[
A_{q,j}=\{n\ge0:s_q(2n)\equiv j\pmod q\}.
\]
Write its members in increasing order as \(n_0<n_1<n_2<\cdots\). The set is infinite. The **exact maximal consecutive gap** is
\[
\boxed{\max_{r\ge0}(n_{r+1}-n_r)=
\begin{cases}
2q-1,&q\text{ even},\\[2pt]
(3q^2-1)/2,&q\text{ odd}.
\end{cases}}
\]
For every base and every target residue, the maximal gap occurs infinitely often. The parity transition is substantial: the extremal spacing grows linearly for even bases and quadratically for odd bases.

## Assumptions and scope

All bases \(q\) are integers at least two; primality is not assumed. Indices \(n\) include zero. The theorem concerns successive *indices*, not the number of occurrences in intervals and not the digit sum of \(n\) in place of \(2n\). Both the starting and ending points of a maximal gap belong to \(A_{q,j}\), while the intervening integer indices do not.

## Proof

**1. Even bases: a permutation in each aligned block.** Assume \(q\) is even and write \(n=qk+t\), with \(0\le t<q\). For \(0\le t<q/2\), adding the final digit gives
\[
s_q(2n)\equiv s_q(2k)+2t\pmod q.
\]
For \(q/2\le t<q\), there is one carry from \(2t\), giving
\[
s_q(2n)\equiv s_q(2k+1)+2t\pmod q.
\]
The last base-\(q\) digit of \(2k\) is even and at most \(q-2\), so adding one does not carry: \(s_q(2k+1)=s_q(2k)+1\). Hence the first half of the aligned block \(qk,\ldots,qk+q-1\) realizes each residue of the parity class of \(s_q(2k)\) exactly once, while the second half realizes each residue of the opposite parity class exactly once. Thus **each aligned block is a permutation of the \(q\) residue classes**. Since every block has exactly one occurrence of every \(j\), any two consecutive occurrences are separated by at most \(2q-1\).

To obtain equality, choose an even nonnegative integer \(M\) whose base-\(q\) digits (from low to high) consist of \(q-2\), followed by \(q-2\) copies of \(q-1\), followed by a zero. Explicitly, for any nonnegative integer \(H\), let
\[
M=(q-2)+\sum_{h=1}^{q-2}(q-1)q^h+Hq^q,
\qquad k=M/2.
\]
The low digits sum to \(q(q-2)\), so \(s_q(2k)\equiv s_q(H)\pmod q\). Adding two to \(M\) changes all displayed low digits to zero and carries one into the next zero, hence
\[
s_q(2k+2)-s_q(2k)=1-q(q-2)\equiv1\pmod q.
\]
Select \(H\) with \(s_q(H)\equiv j\pmod q\). In the aligned block numbered \(k\), residue \(j\) occurs at \(t=0\); in the following block numbered \(k+1\), it occurs at \(t=q-1\), since its residue there is \(s_q(2k+2)+1+2(q-1)\equiv j\). Their separation is \(2q-1\); no intervening index has residue \(j\), because the two blocks are permutations. Taking positive \(H\) with the required digit sum and replacing it by \(Hq^v\) for arbitrarily large \(v\) gives infinitely many such gaps. The construction also applies at \(q=2\) (empty sum convention).

**2. Odd bases: lift to the even digit-sum class modulo \(2q\).** Assume \(q\ge3\) is odd. Because \(q\equiv1\pmod2\), for every nonnegative integer \(m\) one has \(s_q(m)\equiv m\pmod2\). For each \(j\pmod q\), let \(r_j\) be the unique *even* residue \(0\le r_j<2q\) with \(r_j\equiv j\pmod q\), namely \(r_j=j\) when \(j\) is even and \(r_j=j+q\) otherwise. It follows that
\[
2A_{q,j}=\{m\ge0:s_q(m)\equiv r_j\pmod{2q}\}.
\]
Indeed the right side contains only even \(m\), and division by two is bijective.

Put \(B=q^2\). In every aligned block \(Bk\le m<B(k+1)\), write \(m=Bk+t\), \(0\le t<B\), so \(s_q(m)=s_q(k)+s_q(t)\). As \(t\) runs through its two base-\(q\) digits, its digit sum attains **each** integer from \(0\) through \(2q-2\). Therefore the block contains every residue class modulo \(2q\) *except possibly one*, namely \(s_q(k)-1\pmod{2q}\). Two consecutive aligned blocks cannot both omit a fixed residue: \(s_q(k+1)-s_q(k)\) is odd, because \(q\) is odd, and in particular is not zero modulo \(2q\).

Consequently, any open interval between consecutive hits of a fixed digit-sum residue cannot contain two consecutive complete blocks of length \(B\). If two successive hits were at distance at least \(3B\), the two aligned blocks immediately following the block of the first hit would both be wholly contained between them, a contradiction. Thus successive hits in the \(m\)-sequence differ by at most \(3q^2-1\), and dividing by two gives the desired bound \((3q^2-1)/2\) for indices \(n\).

For sharpness, take any even \(r=r_j\) and a nonnegative integer \(H\) with \(s_q(H)=r\), which is automatically even. Put
\[
M_0=Hq^3,\qquad M_1=M_0+(3q^2-1).
\]
The number \(3q^2-1\) has the three base-\(q\) digits \(2,q-1,q-1\), whose sum is \(2q\). Since \(3q^2-1<q^3\), the two endpoints satisfy \(s_q(M_0)=r\), \(s_q(M_1)=r+2q\), so both lie in the even target class. For each *even* \(u\) with \(0<u<3q^2-1\), we have \(0<s_q(u)<2q\) (the largest possible digit sum before that threshold is \(2q-1\)), and \(s_q(u)\) is even. Therefore it is neither \(0\) nor \(q\) nor \(2q\); in particular \(s_q(u)\not\equiv0\pmod q\). There is no intervening target hit at \(M_0+u\). Dividing endpoints by two yields a gap of exactly \((3q^2-1)/2\). To produce infinitely many, take any positive \(H\) with \(s_q(H)\equiv r\pmod{2q}\), and shift its digits to arbitrarily high positions before appending the same three-digit pattern; this changes neither the intervening exclusion nor the endpoint congruences.

Both cases prove the assertions for all \(q\ge2\) and all \(j\).

## Verification

The standalone Python 3 script `verify_gap.py` independently evaluates base-\(q\) digit sums using integer division. It tests the exact sharpness construction for every residue in every base \(2\le q\le31\); directly checks each intervening index, aligned-block permutations for even bases, and the missing-residue exclusion for consecutive blocks in odd bases. It also checks every directly observed consecutive gap for \(2\le q\le17\) over the first \(120000\) indices per base. One local successful run reported:

```text
VERIFY_OK bases=2..31 residues=all witness_interiors=205280 block_cases=5400 direct_consecutive_gap_checks=1919848
```

Run `python3 verify_gap.py`. These are finite consistency tests; the unrestricted theorem rests on the two digit arguments above.

## Relationship to prior work

Boreico, El-Baz and Stoll study precisely the sequence \(s_q(2n)\bmod q\), motivated by Dekking's conjecture. Their Theorem 1.2 establishes oscillation of counting discrepancies, with bounded errors for a different congruence setup and unbounded errors in another. Their proof obtains root-of-unity formulas for counts, but does not classify consecutive-occurrence gaps or distinguish their exact parity-dependent maxima. The present extremal result concerns the recurrence/covering geometry of occurrence sets, not discrepancy signs or asymptotic counts. The standard general theory of automatic sequences provides context but no covering exact gap formula was established in the sources examined.

## Limitations

This is restricted to the multiplier two and to digit sums reduced modulo the base itself. It does not classify the multiplicities of each shorter gap, general multipliers, or the maximum discrepancy of residue counts. Historical priority beyond the inspected source and targeted literature checks is not independently certified; similar gap results could exist under generalized Thue–Morse or uniform-recurrence terminology.

## References

- I. Boreico, D. El-Baz, T. Stoll, *On a conjecture of Dekking: The sum of digits of even numbers*, arXiv:1305.1017v1, first posted 2013-05-05; inspected full text in arXiv:1305.1017v2, https://arxiv.org/html/1305.1017v2 .
- F. M. Dekking, *On the distribution of digits in arithmetic sequences*, Séminaire de Théorie des Nombres de Bordeaux, exposé 32 (1983), referenced by Boreico–El-Baz–Stoll (not inspected in full).
- J.-P. Allouche and J. Shallit, *Automatic Sequences: Theory, Applications, Generalizations*, Cambridge University Press (2003), broad background reference (not inspected in full).
