# First sixfold two-Abelian antipower in the Thue--Morse word and its exact density

## Finding
Let \(\mathbf t=t_0t_1\cdots\) be the binary Thue--Morse word, \(t_i\) equal to the parity of the number of ones in the base-two expansion of \(i\). Say two length-\(L\) words are **two-Abelian equivalent** if their first and last symbols and all four counts of adjacent pairs coincide. A *two-Abelian \(m\)-antipower of block length \(L\)* is a concatenation of \(m\) consecutive length-\(L\) blocks, every two having distinct two-Abelian signatures. Let \(M(L)\) be the largest \(m\ge1\) appearing in \(\mathbf t\) with that block length.

The exact initial sharp spectrum is
\[
(M(1),M(2),M(3),M(4),M(5))=(2,4,4,4,6).
\]
Thus **five is the smallest block length supporting six pairwise two-Abelian-inequivalent consecutive blocks**. At block length five, precisely **twelve distinct length-thirty factors** realize a sixfold two-Abelian antipower; each has natural occurrence frequency \(1/96\) in the Thue--Morse word. Consequently, the natural density of starting positions of these antipowers is exactly
\[
\boxed{1/8}.
\]
No sevenfold two-Abelian antipower of block length five exists. One length-thirty example, beginning at zero-based position three, is `010011001011010010110011010011`.

## Assumptions and scope
All factors and blocks are contiguous, linear, and over the alphabet `0`, `1`. Starting positions are zero based. Frequency means the limit of the number of starting positions \(0\le j<N\) carrying a given factor, divided by \(N\), as \(N\to\infty\); the same convention defines the density of qualifying starts. The maximum is taken over all starting positions in the **infinite** word, not a fixed prefix. Equal lengths make two-Abelian equivalence completely determined by the four-coordinate signature \((w_1,w_L,|w|_{00},|w|_{11})\), since the other adjacent-pair counts follow from the length and endpoints. The scope is the five smallest block lengths, with a detailed frequency classification only at length five.

## Proof
**1. Uniform finite-factor certificate.** Let \(\mu(0)=01\) and \(\mu(1)=10\). The word \(\mu^3(0)=01101001\) contains every binary two-letter factor (`00`, `01`, `10`, `11`). Every factor of \(\mathbf t\) of length at most \(64\) lies in two consecutive length-\(64\) aligned blocks, thus occurs inside some \(\mu^6(ab)\) with \(a,b\in\{0,1\}\). Every such \(ab\) appears in \(\mu^3(0)\); hence all these factors occur in \(\mu^9(0)\), a word of length \(512\). This rigorously reduces every finite test below to a complete finite language; an arbitrary long prefix would not suffice without this argument.

**2. Exactly enumerated signatures.** Exhaustively form all length-\(mL\) factors of \(\mu^9(0)\), for \(1\le L\le5\), and for \(2\le m\le7\) check that the \(m\) consecutive length-\(L\) substrings have pairwise distinct signatures. The complete table of numbers of *distinct qualifying factors* is

| \(L\) | \(m=2\) | \(m=3\) | \(m=4\) | \(m=5\) | \(m=6\) | \(m=7\) |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 0 | 0 | 0 | 0 | 0 |
| 2 | 8 | 8 | 4 | 0 | 0 | 0 |
| 3 | 14 | 12 | 2 | 0 | 0 | 0 |
| 4 | 20 | 24 | 12 | 0 | 0 | 0 |
| 5 | 28 | 36 | 30 | 16 | 12 | 0 |

All queried factor lengths are at most \(35\), covered by Step 1. The table is independently reproduced by two executable programs using different complete-factor generators and different adjacent-pair-count routines. For every \(L\), nonexistence of \(m=M(L)+1\) entails nonexistence at every larger exponent by dropping final blocks. The maximum-spectrum statement follows. At length five, the six distinct two-Abelian signatures among *all* Thue--Morse factors are all realized in each of the twelve qualifying length-thirty windows. There are \(90\) distinct length-thirty Thue--Morse factors altogether; exactly the following twelve qualify:

```text
001101001100101101001011001101
010011001011010010110011010011
010110011010011001011010010110
011001011001101001011010011001
011001101001011010011001011001
011010010110100110010110011010
100101101001011001101001100101
100110010110100101100110100110
100110100110010110100101100110
101001100101100110100101101001
101100110100101101001100101100
110010110011010010110100110010
```

**3. Exact frequency computation.** The Thue--Morse substitution is primitive; hence each finite factor has a natural frequency. The frequencies of aligned two-symbol input blocks are exactly
\[
f(00)=f(11)=\frac16,\qquad f(01)=f(10)=\frac13.
\]
To verify these values directly, use \(t_{2j}=t_j\) and \(t_{2j+1}=1-t_j\): even-start pairs are always unequal, and odd-start pairs are equal exactly when the corresponding original adjacent pair is unequal. If the frequency of equal pairs is \(e\), then \(e=(1-e)/2\), giving \(e=1/3\); complement symmetry and the equality of transition flows give the four displayed values.

For any factor \(v\) of length at most \(64\), count its occurrences in the first \(64\) start positions of \(\mu^6(ab)\) by
\[
c_{ab}(v)=\#\{0\le j<64:\ \mu^6(ab)[j:j+|v|]=v\}.
\]
The aligned-block decomposition of the infinite word, with disjoint sets of possible starting positions, proves the **exact** identity
\[
f(v)=\frac1{64}\sum_{ab\in\{00,01,10,11\}} f(ab)c_{ab}(v).
\]
One independent checker evaluates this finite integer formula using exact rational arithmetic and finds \(f(v)=1/96\) for each of the twelve displayed words. A second checker independently computes the same frequencies via the morphism's even/odd preimage recursion; both agree. These twelve factors are disjoint alternatives at any given starting position, so their frequencies sum to \(12/96=1/8\). This establishes the infinite-word density without extrapolating from any empirical prefix.

## Verification
Run `python3 verify_factors.py` and `python3 independent_check.py`, using Python 3 with standard-library modules only. The first constructs the complete length-\(512\) prefix, checks all qualifying factors, lists the twelve length-thirty witnesses, and recursively computes their exact factor frequencies. The second forms all factors separately from the four length-\(128\) concatenations \(\mu^6(ab)\), obtains signatures with an independent digram counter, and evaluates the direct aligned-superblock frequency formula. Both scripts explicitly assert the sharp five-entry spectrum, twelve witnesses, and density \(1/8\), and exit nonzero if a check fails. Both passed in the supplied environment. These are finite, auditable computations with a mathematical completeness justification in Steps 1 and 3, not samples purporting to prove an infinite assertion.

## Relationship to prior work
Greinecker [1] and Parreau--Rigo--Rowland--Vandomme [2] study two-Abelian factor signatures and their **number** along the Thue--Morse word, not runs of six *consecutive* inequivalent fixed-length factors or their occurrence density. Fici--Restivo--Silva--Zamboni [3] and Defant [4] study antipowers in the stricter **literal unequal-block** sense; literal inequality does not imply two-Abelian inequivalence. A related published dyadic-length two-Abelian factor-class census [5] evaluates sizes of individual ambiguity classes only at lengths \(2^k\), not consecutive block profiles at the non-dyadic length five. A published uniform Thue--Morse antipower-radius result [6] concerns literal antipowers and cannot determine this stronger profile-distinguishability threshold. The claim's novelty is the joint sharp sixfold threshold, twelve precise co-occurrence types, and exact infinite starting density; it is not a claim of having originated two-Abelian equivalence, antipowers, or Thue--Morse factor frequencies.

## Limitations
The maximal-exponent spectrum is proved only for block lengths one through five. The exact density is established only for sixfold two-Abelian antipowers of block length five. This does not classify all larger block lengths, other fixed points, other equivalence orders, or all literal antipowers. The original mathematics and the present exact finite certificates are distinguishable from bibliographic priority: unknown unindexed earlier computations could overlap this classification. No independent mathematical audit has been performed.

## References
[1] F. Greinecker, *On the 2-Abelian Complexity of the Thue--Morse Word*, first posted April 15, 2014, https://arxiv.org/abs/1404.3906.

[2] A. Parreau, M. Rigo, E. Rowland, E. Vandomme, *A new approach to the 2-regularity of the \(\ell\)-abelian complexity of 2-automatic sequences*, first posted May 14, 2014, https://arxiv.org/abs/1405.3532.

[3] G. Fici, A. Restivo, M. Silva, L. Q. Zamboni, *Anti-Powers in Infinite Words*, first posted June 9, 2016, https://arxiv.org/abs/1606.02868.

[4] C. Defant, *Anti-Power Prefixes of the Thue--Morse Word*, first posted July 20, 2016, https://arxiv.org/abs/1607.05825.

[5] *Dyadic two-Abelian ambiguity spectra of Thue--Morse factors*, publicly indexed scientific record, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-dyadic-two-abelian-ambiguity-spectra-of-thue-morse-factors--7a92ede06e81/RESULT.md.

[6] *Exact initial uniform antipower radii of the Thue--Morse word*, publicly indexed scientific record, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-initial-uniform-antipower-radii-of-the-thue-morse-word--fbaddb762fd5/RESULT.md.
