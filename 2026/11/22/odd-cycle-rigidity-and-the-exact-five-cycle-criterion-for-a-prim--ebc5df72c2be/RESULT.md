# Odd-cycle rigidity and the exact five-cycle criterion for a prime-shift map

## Finding
For each positive **odd** integer \(k\), define \(\varphi_k\) on the integers \(n\ge2\) by
\[
\varphi_k(n)=\begin{cases}n+k,&n\text{ is prime},\\P^+(n),&n\text{ is composite},\end{cases}
\]
where \(P^+(n)\) is the largest prime divisor. A primitive cycle is an orbit of least period equal to its number of distinct states, counted once up to cyclic rotation.

**Odd-cycle rigidity:** Every primitive cycle avoiding the prime \(2\) has even period. In particular, for any fixed odd \(k\), there is **at most one** primitive cycle of odd period, namely the periodic orbit containing \(2\), if that orbit has odd period.

**Complete five-cycle classification for odd shifts:** Put \(q=P^+(k+1)\). A primitive cycle of least period five exists if and only if all three conditions hold:
\[
\boxed{\quad k+2\text{ is prime},\qquad q>2,\qquad k+q=2^t\text{ for some integer }t\ge2.\quad}
\]
When it exists, it is unique and is precisely
\[
\boxed{2\ \longrightarrow\ k+2\ \longrightarrow\ 2k+2\ \longrightarrow\ q\ \longrightarrow\ k+q\ \longrightarrow\ 2.}
\]
For example, \(k=5\) gives the five-cycle \(2\to7\to12\to3\to8\to2\). The first qualifying odd parameters through \(200001\), exhaustively checked in that *finite* interval, are \(5,21,51,59,1365,16271,87381\).

## Assumptions and scope
All primes are positive rational primes. The map is deterministic and defined only on integers at least two. The period counts every composite intermediate state, rather than just prime entries. No prime-factor function is evaluated at one because \(k+1\ge2\). The theorem covers every positive odd shift without any unproved assumptions about prime distribution. The finite parameter list is explicitly bounded and does not claim to be all solutions.

## Proof
First, every composite \(c\ge4\) maps to its largest prime factor. Thus two composite states cannot be adjacent in a cycle, including across the cyclic boundary. For odd \(k\), every odd prime \(p\) maps to the even integer \(p+k\ge4\), which is composite. Hence, in any cycle not containing \(2\), every prime state is followed by a composite and every composite is followed by a prime. Its length must therefore be even. More generally, the only possible prime-to-prime edge in the entire map for odd \(k\) is \(2\to k+2\) when \(k+2\) is prime; this is the only way that a cycle can have odd length. Thus every odd-period cycle contains \(2\). Two distinct primitive cycles for one deterministic function cannot both contain the same state, proving the uniqueness assertion.

Suppose a primitive five-cycle exists. Rotate it so that it starts at \(2\). A five-cycle cannot alternate prime and composite states throughout, because five is odd. Its sole possible prime-to-prime transition is therefore \(2\to k+2\), forcing \(k+2\) to be prime. The next state is \(2k+2\), an even composite. The fourth state is consequently \(q=P^+(2k+2)=P^+(k+1)\), a prime. If \(q=2\), the orbit has returned to \(2\) after three steps, contrary to primitive period five. Hence \(q>2\). The fifth state is \(q+k\), a composite because \(q\) and \(k\) are odd. Returning to \(2\) at the sixth displayed state is equivalent to \(P^+(q+k)=2\), and an integer greater than two has largest prime factor two precisely when it is a power of two. This yields \(q+k=2^t\) with \(t\ge2\).

Conversely suppose the three stated arithmetic conditions. Direct substitution gives the five indicated arrows. The second and fourth entries are primes, while \(2k+2\) and \(k+q\) are even composites. They cannot coincide with each other because equality would give \(q=k+2\), impossible since \(q\le k+1\); they cannot coincide with prime entries; and \(q\ne2\) by assumption, while \(q\ne k+2\) for the same inequality. Thus all five states are distinct, and the displayed orbit has least period five. Any other period-five orbit would also contain \(2\) and hence coincide with this one.

This case distinction proves the theorem for arbitrarily large odd \(k\). No numerical enumeration is used to infer an infinite statement.

## Verification
The standalone Python 3 program `verify.py` builds an exact largest-prime-factor sieve and independently compares the three-condition arithmetic test with five applications of the defining map, checking that the five starting states are pairwise distinct. This comparison passes for every one of the \(100001\) odd shifts \(1\le k\le200001\). It finds exactly seven shifts in that interval and prints all corresponding five-state orbits; saved output is in `verification_output.txt`. For example, the orbit at \(k=21\) is \(2\to23\to44\to11\to32\to2\).

The finite regression is a boundary check, not a substitute for the symbolic necessity-and-sufficiency proof above. The uniqueness of odd-period cycles is an all-parameter structural argument, not a computation.

## Relationship to prior work
Das [1] introduced the map, proved eventual periodicity, bounded its number of cycles for each shift, and reported finite data for attainable periods. Those results do not supply the arithmetic condition for an uncompressed primitive period-five orbit or the stated odd-cycle uniqueness. Dubickas [2] proved broader boundedness and eventual periodicity for related maps and studied the prime-compressed recurrence; neither the boundedness bounds nor its compressed periods imply the present five-state classification.

The published short-cycle classification [3] gives necessary and sufficient arithmetic descriptions for all primitive cycles of periods one through four, including the Fermat-prime condition for period three. Its classification stops at four. The present theorem treats the next odd primitive period for odd shifts, and the parity-rigidity assertion explains why this orbit must be anchored at the prime two. A published finite computation exhibiting many cycles at a fixed shift [4] counts cycles without determining this all-odd-parameter criterion. Matching the same arithmetic map does not itself make a different cycle-length theorem equivalent.

## Limitations
Even shifts are deliberately excluded: adding an even shift to an odd prime can produce another odd prime, so the alternation proof does not apply. The theorem does not classify primitive cycles of even period or odd periods greater than five. It does not establish whether infinitely many odd shifts satisfy the three arithmetic tests. An unindexed equivalent period-five criterion remains a bibliographic possibility. The finite computation enumerates parameters only through \(200001\) and is not claimed as global exhaustion.

## References
1. Angsuman Das, *A Family of Iterated Maps on Natural Numbers*, arXiv:2312.06629v1, publicly submitted 11 December 2023, full HTML https://arxiv.org/html/2312.06629v1; *Experimental Mathematics* 33 (2024), 776–780.
2. Artūras Dubickas, *A Class of Bounded Iterative Sequences of Integers*, *Axioms* 13 (2024), article 107, DOI https://doi.org/10.3390/axioms13020107; publicly readable full text https://www.researchgate.net/publication/377990485_A_Class_of_Bounded_Iterative_Sequences_of_Integers.
3. *Exact short-period classification for a shifted largest-prime-factor map*, public research record (8 November 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-short-period-classification-for-a-shifted-largest-prime-fa--9c96b12d92f9.
4. *Thirty-six distinct loops for Das's map at \(k=20735\)*, public research record (4 October 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-thirty-six-distinct-loops-for-das-s-map-at-k-20735--c588f79a1e3b.
