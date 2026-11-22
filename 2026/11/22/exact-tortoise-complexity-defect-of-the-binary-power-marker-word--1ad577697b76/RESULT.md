# Exact tortoise-complexity defect of the binary power-marker word

## Finding

Let \(x=x_0x_1x_2\cdots\) be the binary infinite word with \(x_i=1\) if and only if \(i=2^j-1\) for some integer \(j\ge0\). Let \(F_x(n)\) be its set of distinct contiguous factors of length \(n\), and let \(\rho(n)=|F_x(n)|\). For a binary word \(w\), let \(\tau(w)\) be the one-step Defant--Kravitz *tortoise* operation, and put \(\rho_\tau(n)=|\{\tau(w):w\in F_x(n)\}|\).

**Theorem.** For every integer \(n\ge1\),
\[
\rho(n)-\rho_\tau(n)=n-1.
\]
More precisely, \(\rho(1)=\rho_\tau(1)=2\). For every \(n\ge2\), let \(k=\lfloor\log_2 n\rfloor\) and \(M(n)=\min\{n-2^{k-1},2^k\}\). Then
\[
\rho(n)=n+1+M(n),\qquad \rho_\tau(n)=2+M(n).
\]
The only non-singleton tortoise-equivalence class in \(F_x(n)\), for \(n\ge2\), consists of all \(n\) factors with exactly one \(1\). Every factor containing at least two \(1\)'s is uniquely determined by its tortoise image.

Consequently, \(\rho(n)\le2n+1\), so the source has linear factor complexity, but its tortoise-complexity defect diverges linearly. It is an exact boundary example for the bounded-one-gaps condition in Campbell--Rampersad's theorem on uniformly bounded tortoise defects.

## Assumptions and scope

All positions are indexed from zero. Factors are finite contiguous words; repeated occurrences of an identical factor are counted once. \(n\) is an arbitrary positive integer, with no finite bound. The source word is one-sided. Its marked positions are \(p_j=2^j-1\) for \(j=0,1,\ldots\), with successive distances \(p_{j+1}-p_j=2^j\).

For any binary word \(w=0^{a_0}1\,0^{a_1}1\cdots1\,0^{a_t}\) having exactly \(t\ge1\) ones (all \(a_i\) nonnegative integers), the one-step operation is
\[
\tau(w)=0^{a_0+a_1}1\,0^{a_2}1\cdots0^{a_t}1.
\]
If \(t=0\), set \(\tau(w)=w\). In particular \(\tau(0^a1\,0^b)=0^{a+b}1\). This is the binary specialization of the recursive tortoise map; the map preserves word length and number of ones.

## Proof

**1. Factors with zero or one marked positions.** Arbitrarily long gaps between successive \(1\)'s ensure that \(0^n\) is a factor. For each \(r\in\{0,\ldots,n-1\}\), the factor \(0^r1\,0^{n-r-1}\) occurs around some sufficiently isolated \(1\). These \(n\) distinct weight-one factors all map to \(0^{n-1}1\). The zero factor maps to \(0^n\). These images are different because the tortoise map preserves weight.

**2. Parameterization of factors with two or more marked positions.** Any such factor has a uniquely defined first marked position \(p_j\) and first-one offset \(r\) relative to the left end. The second one in the factor must occur at \(p_{j+1}\), a distance \(d=2^j\) from the first. For \(j=0\), the factor must start at zero and \(r=0\). For \(j\ge1\), the preceding marker is at \(p_{j-1}=2^{j-1}-1\), so having \(p_j\) as the first marker forces
\[
0\le r\le 2^{j-1}-1.
\]
Containment of the second marker requires \(r+d\le n-1\). Conversely, every pair \((j,r)\) satisfying these conditions determines an actual factor: start the length-\(n\) window at \(p_j-r\). The given first two markers occur, and all other symbols are fixed by \(x\). Thus for \(n\ge2\), the number of admissible parameter pairs is
\[
M_0(n)=1+\sum_{j\ge1}\max\{0,\min(2^{j-1},n-2^j)\}.
\]
The initial \(1\) is the \(j=0\) choice. Taking \(k=\lfloor\log_2 n\rfloor\), all terms with \(1\le j<k\) equal \(2^{j-1}\), the term at \(j=k\) is \(\min(2^{k-1},n-2^k)\), and terms with \(j>k\) vanish. Therefore
\[
M_0(n)=2^{k-1}+\min\{2^{k-1},n-2^k\}=\min\{n-2^{k-1},2^k\}=M(n).
\]
It remains to prove that distinct admissible pairs determine different factors, and that their tortoise images are all distinct. Both follow from the next step.

**3. Tortoise separation.** Suppose \(w\in F_x(n)\) has at least two ones and parameter pair \((j,r)\). The first two ones in \(w\) have the gap of \(d-1\) zeros. By the explicit tortoise formula, the position of the **first** one in \(\tau(w)\), indexed from zero, is
\[
K=r+d-1.
\]
If \(j=0\), then \(K=0\). If \(j\ge1\), the range of all possible \(K\)'s lies in the integer interval
\[
[2^j-1,\,3\cdot2^{j-1}-2].
\]
These intervals are pairwise disjoint: the upper endpoint for \(j\) is strictly below the lower endpoint \(2^{j+1}-1\) for \(j+1\), and the \(j=0\) singleton is disjoint from the \(j=1\) interval. Therefore \(K\) uniquely recovers \(j\), and then \(r=K-2^j+1\). Since \((j,r)\) fixes the source factor, the tortoise map is injective on factors with at least two ones. Distinct such factors indeed correspond to distinct parameter pairs.

**4. Counting.** For \(n\ge2\), there are exactly \(n\) weight-one factors, exactly one weight-zero factor, and exactly \(M(n)\) factors of weight at least two. Hence \(\rho(n)=n+1+M(n)\). The tortoise images have exactly one weight-one word, one weight-zero word, and \(M(n)\) different words of weight at least two. Hence \(\rho_\tau(n)=2+M(n)\), and the difference is \(n-1\). For \(n=1\) there are only \(0\) and \(1\), and both are fixed by \(\tau\); this verifies the boundary. Finally \(M(n)\le2^k\le n\), so \(\rho(n)\le2n+1\), while the distances between consecutive ones tend to infinity. This finishes the proof. \(\square\)

## Verification

Two independent standalone standard-Python checkers accompany this result. `verify_direct.py` enumerates actual factors from a binary power-marker prefix longer than sixteen factor lengths, evaluates the tortoise map by literal string decomposition, checks the exact formulas at each \(n=1,\ldots,160\), and verifies the predicted inverse-fiber structure. It checked \(20{,}426\) distinct factor instances and passed.

`verify_structural.py` independently constructs all possible multiple-marker factors from their marker-gap positions for \(n=2,\ldots,320\), checks their tortoise first-one offsets, the disjointness of the relevant intervals, and the dyadic counting formula. It checked \(29{,}450\) multiple-marker factor instances and passed. These finite tests are consistency checks, not proof of the universally quantified formula; that proof is in the previous section. Each script is self-contained and uses Python's standard library.

## Relationship to prior work

Defant and Kravitz introduced the tortoise map on words [1]. Campbell and Rampersad defined tortoise factor complexity, and their Theorem 1 proves that a binary word with linear factor complexity and **bounded gaps between ones** has uniformly bounded ordinary-minus-tortoise complexity [2, Sections 3--4]. They give exact analyses for paperfolding and Thue--Morse factors [2, Sections 5--6]. The present theorem treats the different sparse power-marker word, for which gaps are unbounded. It shows that dropping the bounded-gap assumption cannot preserve the uniform-defect conclusion, even among words with explicit linear factor complexity. No converse or general classification of unbounded-gap words is asserted.

## Limitations

The theorem concerns exactly **one** tortoise application and a single sparse one-sided binary word. It does not assert an all-word characterization, a converse to the bounded-gaps theorem, or formulas for multiple tortoise iterates. Direct computations cover only the stated finite ranges, though the mathematical argument covers every positive length. The literature comparison supports priority only relative to the examined texts and searchable records, not against undiscovered or unindexed literature; independent validation has not been conducted.

## References

[1] C. Defant and N. Kravitz, *Stack-sorting for words*, Australasian Journal of Combinatorics **77** (2020), 51--68; first preprint 2018-09-24, arXiv:1809.09158. https://arxiv.org/abs/1809.09158.

[2] J. M. Campbell and N. Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811, first submitted 2026-04-28; inspected revision v2 (2026-10-05), especially Sections 3--7. https://arxiv.org/html/2604.25811v2.
