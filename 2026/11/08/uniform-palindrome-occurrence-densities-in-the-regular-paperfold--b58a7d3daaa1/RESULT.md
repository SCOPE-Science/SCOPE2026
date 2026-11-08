# Uniform palindrome occurrence densities in the regular paperfolding word

## Finding

Let \(p=p(0)p(1)\cdots\) be the one-sided binary regular paperfolding word, with \(p(n)=1\) when the odd part of \(n+1\) is congruent to \(1\) modulo \(4\), and \(p(n)=0\) otherwise. For each nonempty finite word \(u\), let its occurrence density (when it exists) be
\[
\delta(u)=\lim_{N\to\infty}\frac{1}{N}\#\{0\le i<N:p(i)p(i+1)\cdots p(i+|u|-1)=u\}.
\]

**Theorem.** There are exactly \(28\) distinct nonempty ordinary palindromic factors of \(p\). Their full list, along with the exact density of **each individual word** in the row, is:

| Length | Palindromic factors | Density of each |
|---|---|---|
| \(1\) | `0`, `1` | \(1/2\) |
| \(2\) | `00`, `11` | \(1/4\) |
| \(3\) | `000`, `010`, `101`, `111` | \(1/16\) |
| \(4\) | `0110`, `1001` | \(1/8\) |
| \(5\) | `00100`, `01110`, `10001`, `11011` | \(1/16\) |
| \(6\) | `001100`, `110011` | \(1/32\) |
| \(7\) | `0011100`, `0110110`, `1001001`, `1100011` | \(1/32\) |
| \(9\) | `001101100`, `011000110`, `100111001`, `110010011` | \(1/32\) |
| \(11\) | `00011011000`, `11100100111` | \(1/64\) |
| \(13\) | `0111001001110`, `1000110110001` | \(1/64\) |

There are no palindromic factors at any other positive length. Thus **all palindromes of a fixed length have equal natural occurrence density**, although this is false of arbitrary factors: at length \(3\), `001` has density \(3/16\), whereas `010` has density \(1/16\).

An additional exact position-level classification follows. Fix any \(1\le L\le15\), \(0\le r<32\), and \(b\in\{0,1\}\). Define the length-\(L\) word \(W_{r,b,L}\) by
\[
W_{r,b,L}(j)=
\begin{cases}
b,&16\mid(r+j+1),\\
1,&16\nmid(r+j+1)\text{ and }\operatorname{odd}(r+j+1)\equiv1\pmod4,\\
0,&\text{otherwise},
\end{cases}
\qquad0\le j<L,
\]
where \(\operatorname{odd}(m)=m/2^{\nu_2(m)}\). For a starting position \(i\ge0\), put \(r=i\bmod32\). If the window has a (necessarily unique) \(j_*\) with \(16\mid(i+j_*+1)\), set \(b=p(i+j_*)\); otherwise take either bit \(b\). Then the factor at \(i\) equals \(W_{r,b,L}\). Consequently the precise occurrence set of every listed palindrome \(u\) is the set of indices \(i\) for which \(W_{r,b,|u|}=u\), with \(r,b\) determined as above. This is an effective complete rule without a prefix-length cutoff.

## Assumptions and scope

Indices start at \(0\), factors are contiguous and nonempty, and densities count starting positions in \([0,N)\), not disjoint occurrences. The theorem treats the regular paperfolding instruction sequence (one of the two binary-complement conventions), not arbitrary variable folding instructions. A global letter complement swaps word labels but preserves the density assertion.

## Proof

**1. Automatic recursion.** From the odd-part definition, for every \(t\ge0\),
\[
p(2t)=\begin{cases}1,&t\equiv0\pmod2,\\0,&t\equiv1\pmod2,\end{cases}
\qquad p(2t+1)=p(t).
\]
If \(m\ge1\) is not divisible by \(16\), then \(\nu_2(m)\le3\), so the odd part of \(m\) modulo \(4\), hence its paperfolding symbol, is determined solely by \(m\bmod32\).

**2. Complete finite-state window lemma.** Fix \(1\le L\le15\). Any \(L\) consecutive positive integers contain at most one multiple of \(16\). Consequently, if a factor begins at \(i\equiv r\pmod{32}\), every symbol except at the possible multiple of \(16\) is determined by \(r\). The exceptional symbol is a single free bit \(b\), and the factor is exactly \(W_{r,b,L}\). Conversely every pair \((r,b)\) is realized: write \(i=r+32t\); if the exceptional index exists, its positive integer argument is \(16(s+2t)\) for a fixed positive integer \(s\). For odd \(s\), the odd part of \(s+2t\) alternates between the classes \(1,3\pmod4\). For even \(s\), write \(s=2s'\), so the odd part of \(s+2t\) is that of \(s'+t\). Both values therefore occur. Without an exceptional index, the two values of \(b\) represent the same word. This proves exhaustiveness of the \(32\times2=64\) states, not merely coverage of a sampled prefix.

**3. Exact weights.** Among positive integers, the two odd-part classes \(1\) and \(3\pmod4\) each have natural density \(1/2\): for each valuation \(v\ge0\), either class has density \(2^{-(v+2)}\), and the sum over \(v\) is \(1/2\). Conditional on any start residue \(r\pmod{32}\), the exceptional symbol therefore takes each value on a set of relative density \(1/2\), by the explicit odd/even \(s\) cases above. The residue \(r\) itself has density \(1/32\). Hence each of the \(64\) state pairs carries weight \(1/64\), counting two identical realizations when the window has no exceptional index. In particular, for any \(L\le15\) and factor \(u\) of length \(L\),
\[
\delta(u)=\frac1{64}\#\{(r,b):0\le r<32,\ b\in\{0,1\},\ W_{r,b,L}=u\}.
\]
This also proves that all required limits exist for these lengths.

**4. Exhaustive residue calculation.** Compute the \(64\) words \(W_{r,b,L}\) for each \(1\le L\le15\) from the explicit integer congruences. Retain a word exactly when it equals its reversal. The complete resulting words are displayed in the theorem table. The respective numbers of state pairs per listed palindrome are \(32,16,4,8,4,2,2,2,1,1\) for lengths \(1,2,3,4,5,6,7,9,11,13\). There are no palindrome states at lengths \(8,10,12,14,15\). The standalone `verify_paperfolding.py` implements exactly these finite loops and asserts the entire dictionary of words and state counts (including all zero rows); it is a transparent certificate for the \(960\) finite state-length cases, not a finite-prefix extrapolation.

**5. No longer palindromes.** Repeatedly deleting the first and last symbols from any palindrome of even length at least \(14\) produces a length-\(14\) palindrome; the analogous deletion from any odd-length palindrome at least \(15\) produces a length-\(15\) palindrome. Since both lengths are absent by the exhaustive window lemma, all longer palindromes are absent. The table therefore classifies every length, with \(28\) distinct words in total. Steps 2 and 3 also establish the claimed exact occurrence positions and densities.

## Verification

Execute `python3 verify_paperfolding.py` in the directory containing this file and the script. The supplied code requires only the Python standard library. It checks each of the \(960=64\cdot15\) residue/bit/length cases, asserts all \(28\) palindrome words and their state multiplicities, checks the missing lengths, and independently tests \(786432\) windows of the actual odd-part sequence to detect indexing or model errors. The reported success was `VERIFY_OK 2adic_states=64 lengths=15 state_cases= 960 palindromic_factors=28 direct_windows= 786432`. The full infinite assertion is justified by the window and frequency lemmas, not by the supplementary direct-window tests alone.

## Relationship to prior work

Allouche, Baake, Cassaigne and Damanik (2001/2003) record the absence of ordinary palindromes of length at least \(14\) in paperfolding words, but not this per-palindrome frequency table or exact residue occurrence rule. Frid, Laborde and Peltomäki (first public 2020) use the regular paperfolding word (in the bit-complement convention) and its known longest-palindrome length \(13\) to calculate *prefix palindromic length*, a different function. Burns (2022) calculates the *appearance function*, the first time every factor has appeared, rather than natural frequencies of all occurrences. Fici, Shallit and Simpson (2024) calculate *palindromic periodicities*, a broader factor class, but their stated results for paperfolding do not imply individual palindrome densities. None of these claims provides the state-count theorem above. The paperfolding result is not an implication of prior results for the distinct Rudin–Shapiro word.

## Limitations

No result for arbitrary folding instructions, arbitrary automatic words, frequencies of all nonpalindromic factors, or higher-order correlations is asserted. The finite residue computation is an exact exhaustive sublemma with a readable checker; no independent external audit has been performed. A separately published equivalent per-factor density table not indexed by the searched sources remains a possible originality risk.

## References

1. A. E. Frid, E. Laborde, J. Peltomäki, *On prefix palindromic length of automatic words*, arXiv:2009.02934, first submitted 2020-09-07; https://arxiv.org/abs/2009.02934.
2. J.-P. Allouche, M. Baake, J. Cassaigne, D. Damanik, *Palindrome complexity*, arXiv:math/0106121, 2001; https://arxiv.org/abs/math/0106121.
3. R. Burns, *The appearance function for paper-folding words*, arXiv:2210.14719, first submitted 2022-10-22; https://arxiv.org/abs/2210.14719.
4. G. Fici, J. Shallit, J. Simpson, *Some Remarks on Palindromic Periodicities*, arXiv:2407.10564, first submitted 2024-07-15; https://arxiv.org/abs/2407.10564.
