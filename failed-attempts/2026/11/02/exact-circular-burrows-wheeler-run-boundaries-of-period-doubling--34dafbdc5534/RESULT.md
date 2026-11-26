# Exact circular Burrows–Wheeler run boundaries of period-doubling words

## Finding
For every integer \(k\ge2\), let \(P_k=\mu^k(0)\) for the binary substitution \(\mu(0)=01\), \(\mu(1)=00\). Sort the \(2^k\) cyclic rotations of \(P_k\) lexicographically, and concatenate the symbols immediately preceding those rotations to form the **sentinel-free circular Burrows–Wheeler transform** \(\operatorname{BWT}^{\circ}(P_k)\). Its number \(r_k\) of maximal equal-letter runs is exactly
\[
 r_k=2k-2. 
\]

There is an exact description of **each** run boundary. Put \(A_0=00\), \(B_1=0\) and recursively
\[
 A_{j+1}=\mu(A_j)0,\qquad B_{j+1}=\mu(B_j)0.
\]
For every adjacent pair of lexicographically sorted circular rotations whose BWT symbols disagree, take the longest common prefix of that pair. These \(2k-3\) longest common prefixes are distinct, and their complete set is
\[
 \{A_j:0\le j\le k-2\}\ \mathbin{\sqcup}\ \{B_j:1\le j\le k-2\}.
\]
The two families have lengths \(|A_j|=3\cdot 2^j-1\) and \(|B_j|=2^j-1\). In particular, the specification is finer than a count of runs.

## Assumptions and scope
All words are over the ordered alphabet \(0<1\). The substitution extends by concatenation, and \(P_0=0\). A circular length-\(d\) factor of a length-\(N\) word is read cyclically from a starting position, with \(0\le d<N\). A factor is *left-special* (respectively *right-special*) if it occurs with both predecessor symbols (respectively both successor symbols) in the cyclic word. A factor is *bispecial* if it is both. The empty word is included among possible factors. The circular BWT uses exactly one full period per rotation, **no terminator**, and its run count is linear (the first and last BWT symbols are not merged).

## Proof
**1. Distinctness of rotations and local constraints.** Write \(Q=P_{k-1}\), so \(P_k=\mu(Q)\). The number of ones in \(P_1\) is odd; since every substituted zero produces one one and every substituted one produces none, its successor is \(2^{k-1}-\#_1(P_{k-1})\), again odd. A binary word of power-of-two length that is a nontrivial power repeats its ones count an even number of times. Thus every \(P_k\) for \(k\ge1\) is primitive and all its circular rotations are different. Each substituted block begins with zero; hence no \(P_k\) has a cyclic occurrence of \(11\). Each cyclic occurrence of a length-three factor in \(P_k\) lies in
\[
 \{000,001,010,100,101\}.
\]
At positions of even parity, a length-three factor is \(0\,\overline{q_i}\,0\), while at odd parity it is \(\overline{q_i}\,0\,\overline{q_{i+1}}\). Here \(\overline a=1-a\), and indices of \(Q\) are cyclic. Since \(Q\) has no cyclic \(11\), each occurrence of \(000\) is preceded and followed by \(1\). Every occurrence of \(001\) is preceded and followed by \(0\); likewise for \(100\) and \(101\). Thus any length-three factor with a variable predecessor or a variable successor must be \(010\), which begins at an even position.

**2. Complete bispecial language.** Directly in \(P_2=0100\), the circular bispecial words of length less than \(4\) are exactly \(\epsilon,0,00\). For each \(k\ge3\), the only bispecial factors of length one or two are \(0,00\): all other short factors have a fixed predecessor or successor by the parity description. If a bispecial word \(u\) has length at least three, its length-three prefix must have a variable predecessor, and its length-three suffix must have a variable successor. Both are therefore \(010\), forcing the first and final positions of \(u\) to be even and its length to be odd. It can consequently be written uniquely as \(u=\mu(v)0\) with \(v\) a nonempty circular factor of \(Q\). Every occurrence of \(u\) starts at an even substituted-block boundary and corresponds bijectively to an occurrence of \(v\) in \(Q\); both extension symbols are the complements of the corresponding extension symbols of \(v\). Hence \(u\) is bispecial exactly when \(v\) is. Inducting from \(P_2\) gives the complete circular bispecial set
\[
 \operatorname{BS}(P_k)=\{\epsilon\}\ \sqcup\ \{A_j:0\le j\le k-2\}\ \sqcup\ \{B_j:1\le j\le k-1\}.
\]
Indeed, the length-one factor \(0\) and length-two factor \(00\) are present and bispecial at each rank, and every longer factor is an image of a nonempty prior bispecial factor. The displayed families are disjoint by their distinct lengths: \(|A_j|=3\cdot2^j-1\), \(|B_j|=2^j-1\).

**3. From bispecial factors to BWT run boundaries.** In any primitive binary circular word, a right-special factor \(u\) determines exactly one adjacency across the lexicographic cut between rotations with prefix \(u0\) and those with prefix \(u1\): the greatest \(u0\) rotation and the least \(u1\) rotation. That pair has longest common prefix exactly \(u\). Conversely every adjacent pair of distinct sorted rotations has such a right-special longest common prefix. Define \(I_k(u)=1\) if the two predecessor symbols across that cut differ, and \(0\) otherwise. Necessarily \(I_k(u)=0\) for a right-special factor that is not left-special. Therefore the number of linear BWT run boundaries is the sum of \(I_k(u)\) over the circular bispecial factors \(u\).

**4. Transport of boundaries through the substitution.** For a nonempty bispecial \(v\) of \(Q\), let \(u=\mu(v)0\). All occurrences of \(u\) begin at even positions. Lexicographic ordering of the even-start rotations of \(\mu(Q)\) is precisely **reversed** from the ordering of the corresponding rotations of \(Q\): at the first unequal letter, \(\mu\) turns \(0<1\) into \(01>00\). The next symbol after \(u\) is the complement of the symbol after \(v\), and the preceding symbols are complemented as well. Thus the cut \(u0\mid u1\) is the reverse-complement image of \(v0\mid v1\). In particular,
\[
 I_k(\mu(v)0)=I_{k-1}(v).
\]

**5. The three elementary cuts.** For \(k\ge2\), the lexicographically smallest rotation beginning with \(0\) begins with \(000\), and hence has predecessor \(1\). For \(k\ge2\), the greatest rotation beginning with \(0\) begins with \(01\) and must be an even-start \(\mu\)-rotation; it corresponds to the least zero-start rotation of \(P_{k-1}\), hence has predecessor \(0\). (At rank one, the greatest zero-start rotation of \(01\) has predecessor \(1\).) The least one-start rotation has predecessor \(0\), since every one is at an odd position. Thus the BWT cut for \(\epsilon\) has identical predecessor letters for all \(k\ge2\): \(I_k(\epsilon)=0\).

For the factor \(00\), the greatest \(000\)-rotation has predecessor \(1\), while the least \(001\)-rotation has predecessor \(0\). Hence \(I_k(00)=1\). For the factor \(0\), the greatest \(00\)-rotation starts \(001\) and has predecessor \(0\). The least \(01\)-rotation corresponds, by reverse ordering of even-start rotations, to the greatest zero-start rotation of \(P_{k-1}\), with the preceding symbol complemented. Consequently, \(I_2(0)=0\), whereas \(I_k(0)=1\) for every \(k\ge3\).

**6. Counting and identifying every boundary.** The base word \(P_2\) has only the nonzero boundary indicator \(I_2(A_0)=1\). At each higher rank, transport preserves the indicators attached to all older nonempty bispecial factors, while the two new short factors \(00\) and \(0\) each contribute a new boundary. The empty-factor indicator remains zero. Equivalently, every \(A_j\) is active, and among the \(B_j\), precisely \(B_1,\ldots,B_{k-2}\) are active; the current highest \(B_{k-1}\) is inactive. There are \((k-1)+(k-2)=2k-3\) active cuts. A linear binary word has one more run than the number of unequal neighboring pairs, proving \(r_k=2k-2\) and the complete boundary-prefix classification.

## Verification
The standalone Python 3 program `checker.py` reconstructs the words and uses two independent circular-BWT sorting algorithms for ranks \(2\) through \(9\). It directly enumerates bispecial circular factors through rank \(7\), and verifies the complete boundary-prefix set and run formula through rank \(14\) (length \(16384\)). All assertions pass when run with `python3 checker.py`. Finite enumeration is a consistency check, not the infinite proof given above.

## Relationship to prior work
The 1994 Burrows–Wheeler report introduced the cyclic-rotation sorting transform. Currie–Rampersad–Saari–Zamboni study extremal infinite morphic words, including period-doubling extremal subshift representatives, but their results do not give this finite circular BWT boundary language. Brlek–Frosini–Mancini–Pergola–Rinaldi examine BWT of several morphic families, notably Thue–Morse and related words, without supplying the period-doubling formula above. Frosini–Mancini–Rinaldi–Romana–Sciortino establish general logarithmic-run phenomena for purely morphic families and discuss bispecial factors, but their available statements do not identify these exact cuts or the coefficient \(2\) for the present dyadic family. Fici–Romana–Sciortino–Urbina treat worst-case BWT-run sensitivity of morphisms; that extremization differs from BWT of these fixed substitution iterates. This is an assessment of the specifically inspected literature, not a claim of exhaustive historical priority.

## Limitations
The theorem concerns complete dyadic substitution iterates, the ordered binary alphabet, and **circular, sentinel-free** BWT. It does not claim formulas for arbitrary prefixes, sentinel-terminated BWT, or all finite factors of the infinite period-doubling sequence. The proof is self-contained but has not received independent mathematical audit; further unindexed literature might bear on priority.

## References
- M. Burrows and D. J. Wheeler, *A Block-sorting Lossless Data Compression Algorithm*, Technical Report 124, Digital Systems Research Center, May 10, 1994. https://www.cl.cam.ac.uk/teaching/2425/Bioinfo/papers/burrows_wheeler.pdf
- J. Currie, N. Rampersad, K. Saari, and L. Q. Zamboni, *Extremal words in morphic subshifts*, 2013, arXiv:1301.4972. https://arxiv.org/pdf/1301.4972
- S. Brlek, A. Frosini, S. Mancini, E. Pergola, and S. Rinaldi, *Burrows–Wheeler transform of words defined by morphisms*, 2019. https://flore.unifi.it/retrieve/e398c380-dd2e-179a-e053-3705fe0a4cff/BWT-morphism_%20Last.pdf
- A. Frosini, S. Mancini, S. Rinaldi, M. Romana, and M. Sciortino, *Logarithmic equal-letter runs for BWT of purely morphic words*, 2022, arXiv:2202.02609. https://arxiv.org/pdf/2202.02609
- G. Fici, M. Romana, M. Sciortino, and E. Urbina, *Morphisms and BWT-run Sensitivity*, 2025, arXiv:2504.17443. https://arxiv.org/html/2504.17443v1
