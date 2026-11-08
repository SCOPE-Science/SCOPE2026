# Complete antisquare spectra of two-block periodic binary words

## Finding

A nonempty binary word is an **antisquare of order** \(k\ge 1\) if it is \(u\overline{u}\), where \(|u|=k\) and \(\overline{u}\) interchanges zeros and ones. For positive integers \(a,b\), consider the one-sided infinite periodic word
\[
X_{a,b}=(0^a1^b)^\omega,
\]
and let \(A_{a,b}(k)\) count **distinct** antisquare factors of order \(k\) in this word. Put \(s=\min(a,b)\), \(t=\max(a,b)\), and \(p=a+b\).

**Theorem (complete order spectrum).** For every \(a,b,k\ge 1\):

* If \(s<t\),
\[
A_{a,b}(k)=
\begin{cases}
2,&1\le k<s,\\
s+1,&k=s,\\
\max(0,2s-t+1),&k=t,\\
0,&\text{otherwise}.
\end{cases}
\]
(The cases \(k=s\) and \(k=t\) are disjoint because \(s<t\).)
* If \(s=t\),
\[
A_{s,s}(k)=
\begin{cases}
2,&1\le k<s,\\
2s,&k=s+2sm\text{ for an integer }m\ge0,\\
0,&\text{otherwise}.
\end{cases}
\]

Consequently the order generating function \(F_{a,b}(z)=\sum_{k\ge1}A_{a,b}(k)z^k\) is
\[
F_{a,b}(z)=
\begin{cases}
2\displaystyle\sum_{k=1}^{s-1}z^k+(s+1)z^s+\max(0,2s-t+1)z^t,&s<t,\\
2\displaystyle\sum_{k=1}^{s-1}z^k+\displaystyle\frac{2sz^s}{1-z^{2s}},&s=t.
\end{cases}
\]
In particular, **the complete distinct-antisquare language is finite if and only if** \(a\ne b\). In the unequal case the total number is exactly
\[
\sum_{k\ge1}A_{a,b}(k)=3s-1+\max(0,2s-t+1).
\]
The largest possible order is \(s\) when \(t>2s\), and is \(t\) when \(s<t\le2s\). In the equal case there are infinitely many orders, but precisely \(2s\) distinct antisquares at each order congruent to \(s\) modulo \(2s\), apart from the two antisquares at each smaller order.

## Assumptions and scope

All three parameters \(a,b,k\) are positive integers. Factors are **contiguous** finite words, not scattered subsequences. Two factors are identified if their letter strings are identical, even if they occur at multiple positions. The word is one-sided infinite, but its periodicity means that every starting phase in \(\mathbb Z/p\mathbb Z\) occurs at a nonnegative index. The theorem does not assert anything for nonbinary alphabets or periods with more than two runs.

## Proof

**1. Circular disagreement criterion.** Interchanging the two letters if necessary, let the shorter symbol-block consist of zeros, and index phases by \(\mathbb Z/p\mathbb Z\). The zero phases form one circular interval \(I\) of length \(s\); the other phases form a contiguous interval of length \(t\). For every integer \(k\ge1\), the length-\(2k\) factor beginning at phase \(i\) is an antisquare precisely if
\[
i,i+1,\ldots,i+k-1\in M_r,
\quad M_r=I\mathbin\triangle(I-r),\quad r\equiv k\pmod p,
\]
with all phase arithmetic modulo \(p\). Indeed the two halves disagree letterwise exactly when the corresponding phase belongs to the symmetric difference of the two zero-position sets. In the formula \(I-r\) denotes the translate of \(I\) by \(-r\).

**2. Exact geometry of the disagreement set.** For \(0<r<p\), inspection of the endpoints of the two circular intervals \(I\) and \(I-r\) gives:

* If \(1\le r<s\), the two components of \(M_r\) are disjoint circular intervals, each of length \(r\).
* If \(s<r<t\), the two components are disjoint intervals, each of length \(s\).
* If \(t<r<p\), the two components are disjoint intervals, each of length \(p-r\).
* At \(r=s\) or \(r=t\), the two intervals are adjacent, so \(M_r\) is one circular interval of length \(2s\) if \(s<t\). If \(s=t\), both endpoints coincide and \(M_s\) is all \(p=2s\) phases.

At \(r=0\), \(M_0\) is empty. These statements also cover vacant parameter ranges, such as \(s=1\) and \(t=s+1\). For example, in the first case the two translates overlap in a circular interval of length \(s-r\), and their two nonoverlapping tails each have length \(r\); in the middle case the translates are disjoint, and at the endpoints they touch and their two length-\(s\) pieces merge. The last case is the reflection of the first.

**3. All possible orders and starting phases.** If \(s<t\), then \(|M_r|\le2s<p\) for every residue \(r\). Therefore no \(k\ge p\) can satisfy the disagreement criterion: a consecutive string of \(p\) phases covers the entire circle. For \(1\le k<p\), put \(r=k\). Two disjoint mismatch intervals of length exactly \(k\) give precisely two allowed starting phases when \(k<s\). At \(k=s\), a single mismatch interval of length \(2s<p\) contains exactly \(2s-s+1=s+1\) consecutive length-\(s\) subintervals. For \(s<k<t\), both mismatch components have length \(s<k\); there are no starts. At \(k=t\), the length-\(2s\) mismatch interval allows \(2s-t+1\) starts if \(t\le2s\), and none otherwise. For \(t<k<p\), the mismatch components have length \(p-k<s<k\), so no starts exist.

If \(s=t\), for \(1\le k<s\) there are the same two length-\(k\) mismatch components. At \(k=s\), every phase is allowed. For \(s<k<p\), every mismatch component is shorter than \(k\). For \(k\ge p\), any consecutive \(k\) phases cover a full period; therefore all of them must disagree. This happens exactly when \(r=s\pmod p\), and then every phase is allowed. Thus all possible orders and **numbers of starting phases** are as asserted.

**4. Distinct phases represent distinct antisquares.** The primitive period of \(X_{a,b}\) is \(p\): in each period there is exactly one transition of type \(01\) and one of type \(10\), so no smaller circular period can repeat the run pair. Hence two distinct phases cannot yield equal factors of length at least \(p\). This establishes distinctness automatically at \(k=t\) in the unequal case (since \(2t>p\)) and at every resonant \(k=s+2sm\) in the equal case (since \(2k\ge p\)). For \(1\le k<s\), the two factors are exactly \(0^k1^k\) and \(1^k0^k\), so they differ. At \(k=s<t\), the \(s+1\) factors are \(0^s1^s\) together with
\[
1^j0^s1^{s-j}\qquad(1\le j\le s),
\]
which are pairwise distinct by their initial run lengths. Therefore each counted starting phase corresponds to a distinct antisquare factor, proving the theorem.

Summing the finite spectrum yields \(2(s-1)+(s+1)+\max(0,2s-t+1)=3s-1+\max(0,2s-t+1)\). The generating functions and largest-order consequences follow directly.

## Verification

The standalone Python script `verify.py` independently computes each factor as an actual binary string from a sufficiently long periodic prefix, tests its two halves by direct bit comparison, counts distinct admissible strings, and separately checks circular mismatch indicators. It compares both computations with the closed formula for every \(1\le a,b\le22\) and every \(1\le k\le4(a+b)\), including all small-run, unequal-run and equal-run boundary cases. There are **44,528** tested parameter triples and **462** separate unequal-run total-count checks; all passed. Reproduce with `python3 verify.py`. The finite tests are corroboration only; Steps 1–4 prove the assertions for all positive integers.

For illustration, the unequal pair \((a,b)=(2,3)\) has order polynomial \(2z+3z^2+2z^3\) and seven distinct antisquares altogether. The balanced pair \((a,b)=(2,2)\) has \(2z+4z^2/(1-z^4)\) and infinitely many orders.

## Relationship to prior work

Antisquares and avoidance of all but a few distinct antisquares are studied by Baranwal, Currie, Mol, Ochem, Rampersad and Shallit [1], particularly the definitions and their classification of **minimal forbidden antisquares** (Theorem 11). Their result classifies antisquares minimal under the factor order, not all antisquare factors of a prescribed periodic host. Ng, Ochem, Rampersad and Shallit [2] classify possible **joint avoidance bounds** for squares and antisquares; these bounds are not an order-by-order count for \((0^a1^b)^\omega\). Hieronymi and coauthors [3] study antisquares in **aperiodic Sturmian words**, rather than these two-run periodic words. Thus the present classification addresses a distinct, host-specific enumerative question. Its phase-disagreement proof is self-contained; none of those general results is assumed. The earlier works are duly credited and the possibility of an unindexed equivalent special-case result is not excluded.

## Limitations

This theorem is restricted to periods consisting of exactly one nonempty run of each binary letter. It gives distinct factor counts, not the number of occurrences in a finite prefix; occurrences in an infinite periodic word are recurrent whenever the factor exists. It does not prove that no unindexed equivalent formula appears in earlier literature. It is not an independent scientific certification.

## References

1. A. Baranwal, J. Currie, L. Mol, P. Ochem, N. Rampersad, J. Shallit, *Antisquares and Critical Exponents*, arXiv:2209.09223 (first public version, 2022-09-19), Discrete Mathematics & Theoretical Computer Science 25:2 (2023), https://arxiv.org/abs/2209.09223.
2. T. Ng, P. Ochem, N. Rampersad, J. Shallit, *New results on pseudosquare avoidance*, arXiv:1904.09157 (2019-04-19), https://arxiv.org/abs/1904.09157.
3. P. Hieronymi, D. Ma, R. Oei, L. Schaeffer, C. Schulz, J. Shallit, *Decidability for Sturmian words*, arXiv:2102.08207 (2021-02-16), https://arxiv.org/abs/2102.08207.
