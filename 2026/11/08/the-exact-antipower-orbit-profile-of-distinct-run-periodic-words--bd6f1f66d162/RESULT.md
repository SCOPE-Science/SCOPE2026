# The exact antipower orbit profile of distinct-run periodic words

## Finding

Let \(q\ge 2\) and let \(c_0,\ldots,c_{q-1}\) be distinct letters. For positive integers \(a_0,\ldots,a_{q-1}\), put
\[
P=c_0^{a_0}c_1^{a_1}\cdots c_{q-1}^{a_{q-1}},\qquad W=P^\omega,\qquad L=\sum_i a_i,\qquad M=\max_i a_i.
\]
A length-\(m\) block is a contiguous factor of \(W\). A \(k\)-antipower at phase \(s\) is a concatenation of \(k\) pairwise distinct length-\(m\) blocks starting at positions \(s,s+m,\ldots,s+(k-1)m\), where the starting phase is taken modulo \(L\). Let \(K(m)\) be the largest positive integer \(k\) for which **all** \(L\) phases begin a \(k\)-antipower. Put
\[
g=\gcd(L,m),\quad T=L/g,\quad \delta_L(t)=\min(t\bmod L,(-t)\bmod L).
\]
Then, for every integer \(m\ge 1\),
\[
K(m)=\begin{cases}
\min\{j:1\le j\le T,\ \delta_L(jm)\le M-m\},&m<M,\\
T,&m\ge M.
\end{cases}
\tag{1}
\]
In particular,
\[
K(m)=T\ \Longleftrightarrow\ M-m<g, \tag{2}
\]
where the right side is understood literally (so it holds automatically if \(m\ge M\)). Moreover, for every \(m\) not divisible by \(L\), all phases begin a two-block antipower exactly when \(2m>M\).

There is also an **exact census of phases attaining the entire orbit of \(T\) distinct blocks**. Write \(b_i=\sum_{j<i}a_j\), and define
\[
I_i(m)=\begin{cases}\{b_i,b_i+1,\ldots,b_i+a_i-m\},&a_i\ge m,\\\varnothing,&a_i<m.\end{cases}
\]
For each residue \(r\in\{0,\ldots,g-1\}\), put \(n_{i,r}(m)=\#\{s\in I_i(m):s\equiv r\pmod g\}\). The number \(H(m)\) of phases beginning a \(T\)-antipower is
\[
\boxed{H(m)=T\,\#\{r\bmod g:\ n_{i,r}(m)\le1\text{ for every }i\}.}\tag{3}
\]
Thus the worst-phase spectrum depends only on \((L,M)\), while the full-orbit phase census retains arithmetic information about the individual run locations.

## Assumptions and scope

All runs are nonempty, every displayed symbol is different from all the others, and there is exactly one cyclic run of each symbol per period. The word is right-infinite and exactly periodic. Since \(q\ge2\), each cyclic boundary digram \(c_i c_{i+1\bmod q}\) appears exactly once modulo \(L\), so \(L\) is a fundamental period. The block length \(m\) is any positive integer, including \(m\ge L\). The maximum \(K(m)\) permits \(k=1\); a nontrivial antipower has \(k\ge2\). Counts are of starting phases, not of distinct concatenated output strings.

## Proof

**Factor-collision lemma.** For every \(m\ge1\), if two distinct phases support identical length-\(m\) factors, both factors are monochromatic and the phases belong to the same interval \(I_i(m)\). Indeed, a nonmonochromatic factor contains an adjacent unequal pair \(c_i c_{i+1\bmod q}\). This ordered boundary pair occurs only once in each period, so its position within the factor determines its starting phase uniquely. A monochromatic factor \(c_i^m\) can only start at the integers in \(I_i(m)\); for \(m\ge L\) such intervals are empty. This proves the lemma in both directions.

Fix a positive separation \(j\). Any two blocks whose indices differ by \(j\) start at phases separated by \(jm\) modulo \(L\). For \(m<M\), the collision lemma implies that such a pair can be equal for *some* starting phase if and only if one run contains two admissible starting positions separated by \(jm\), which is equivalent to \(\delta_L(jm)\le M-m\). For \(m\ge M\), no two distinct phases have equal factors. The phase orbit under addition by \(m\) has exact order \(T=L/g\), and its \((T+1)\)-st block repeats its first block. The earliest positive separation that can produce a collision at some phase is therefore the minimum in equation (1), or \(T\) if no distinct-phase collision is possible. Any \(k\) at most this value has all pairwise block separations smaller than the first collision separation, whereas at \(k\) one larger, a collision occurs at some starting phase. This establishes (1).

Among the nonzero elements of the phase-step subgroup \(g\mathbb Z/L\mathbb Z\), the smallest positive circular distance is \(g\) when \(T>1\). Therefore there is no collision during the entire first orbit exactly if \(M-m<g\), proving (2) for \(m<M\). When \(m\ge M\), no different-phase collision exists, and since \(M-m\le0<g\), the equivalence still holds. The case \(T=1\) is covered because \(m\) is then a multiple of \(L\) and hence exceeds \(M\).

For the two-block assertion assume \(L\nmid m\). If \(m\ge M\), distinct phases produce distinct factors and \(2m>M\). Otherwise \(m<M<L\). The two factors can collide for some phase precisely when \(\delta_L(m)\le M-m\). If \(m\le L/2\), this condition is \(2m\le M\); if \(m>L/2\), it is false because \(L>M\). This proves the threshold.

Finally, the first \(T\) block starts visit exactly the \(T\) phases congruent to \(s\pmod g\), once each. By the factor-collision lemma, those factors are all different if and only if that residue orbit intersects each monochromatic-start interval \(I_i(m)\) at most once. This condition is exactly \(n_{i,r}(m)\le1\) for all \(i\), where \(r=s\bmod g\). Each qualifying residue class contributes \(T\) starting phases, yielding (3), including the empty-interval case \(m\ge M\).

## Verification

The accompanying standard-library script `check.py` constructs all actual length-\(m\) blocks independently of the formulas, and tests the worst-phase threshold, full-orbit phase counts, the gcd criterion and the two-block boundary. It passed 31,840 exhaustive instances for \(2\le q\le5\), all run lengths in \(\{1,2,3,4\}\) and \(1\le m\le2L\); 1,600 further seeded cases with up to seven letters and longer runs also passed. This finite corroboration is not substituted for the unrestricted proof above.

For example, for run lengths \((7,3,2)\) and \(m=3\), one has \(L=12\), \(g=3\), \(T=4\), \(K(3)=1\), yet equation (3) gives \(H(3)=4\): four phases support all four distinct blocks even though not all phases support two.

## Relationship to prior work

Kociumaka, Radoszewski, Rytter, Straszyński, Waleń and Zuba develop general algorithms for enumerating and counting finite-word antipowers and weak powers, using runs and gapped repeats. Their theorems apply to arbitrarily long finite prefixes of the present periodic sources, but do not state the exact arithmetic \((L,M)\) classification or the cyclic residue-class phase count in (1)–(3). Garg studies the existence and bounded block length of antipowers in aperiodic morphic and Fibonacci words. Berger and Defant study antipowers in aperiodic recurrent words. These are related but do not supply the periodic distinct-run profile. The result is a structural closed form, not a claim that antipowers were previously uncountable by general-purpose algorithms.

## Limitations

Distinct symbols and one cyclic run per symbol are essential to the unique-boundary-digram proof. Repeated symbols in disjoint cyclic runs can give nonmonochromatic factor collisions and invalidate (1)–(3). The theorem concerns exact equality of blocks, not Abelian equivalence or partial-match distance. It classifies entire phase orbits, not necessarily the number of different antipower output strings. General enumeration algorithms can compute individual instances, so the contribution is the closed-form infinite-family classification and structural explanation. Bibliographic coverage cannot exclude an unindexed equivalent formulation; no independent scientific audit is claimed.

## References

1. T. Kociumaka, J. Radoszewski, W. Rytter, J. Straszyński, T. Waleń, and W. Zuba, *Efficient Representation and Counting of Antipower Factors in Words*, arXiv:1812.08101 (first publicly posted 2018-12-19), https://arxiv.org/abs/1812.08101 .
2. S. Garg, *Antipowers in Uniform Morphic Words and the Fibonacci Word*, arXiv:1907.10816 (first publicly posted 2019-07-25), https://arxiv.org/abs/1907.10816 .
3. A. Berger and C. Defant, *On Anti-Powers in Aperiodic Recurrent Words*, arXiv:1902.01291 (first publicly posted 2019-02-05), https://arxiv.org/abs/1902.01291 .
4. G. Fici, A. Restivo, M. Silva, and L. Q. Zamboni, *Anti-Powers in Infinite Words*, arXiv:1606.02868 (background only; first publicly posted 2016-06-09), https://arxiv.org/abs/1606.02868 .
