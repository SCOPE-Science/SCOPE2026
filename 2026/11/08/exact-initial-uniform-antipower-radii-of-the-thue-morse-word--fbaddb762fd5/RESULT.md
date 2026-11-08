# Exact initial uniform antipower radii of the Thue–Morse word

## Finding

Let \(\mathbf t=t_0t_1\cdots\) denote the infinite binary Thue–Morse word, with \(t_j\) the parity of the binary digit sum of \(j\). For integers \(j\geq0\), \(k\geq3\), let \(\gamma_j(k)\) be the least positive integer \(m\) such that the \(k\) consecutive length-\(m\) blocks beginning at position \(j\) in \(\mathbf t\) are pairwise distinct. Define the uniform radius \(R(k)=\sup_{j\geq0}\gamma_j(k)\).

The first eight nontrivial uniform radii are exactly

\[
\bigl(R(3),R(4),R(5),R(6),R(7),R(8),R(9),R(10)\bigr)
=(5,7,9,11,11,11,13,13).
\]

In particular, the uniform radius first differs from the prefix-only radius at \(k=4\), where the former is \(7\) but the latter is \(5\). The uniform radii exhibit consecutive plateaus at \(k=7,8\) and \(k=9,10\).

## Assumptions and scope

Indices start at zero, words are linear factors of the one-sided infinite Thue–Morse word, and \(m\) is unrestricted apart from being a positive integer (it need not be odd). Distinctness means literal equality of binary blocks, not equality of multisets or a different equivalence relation. The maximum across starting positions is well-defined for the eight specified values because the proof gives a uniform finite upper bound and an attaining starting position for each value.

The Thue–Morse word is the fixed point beginning in \(0\) of the length-two morphism \(\mu(0)=01\) and \(\mu(1)=10\). A \(k\)-antipower is a concatenation of \(k\) pairwise unequal blocks of a common length.

## Proof

**Finite-factor completeness lemma.** Every factor of \(\mathbf t\) of length at most \(256\) occurs in the prefix \(\mu^{11}(0)\), of length \(2048\). Indeed, write \(\mathbf t\) as consecutive length-\(256\) blocks \(\mu^8(t_i)\). A factor of length at most \(256\) is contained in the concatenation \(\mu^8(t_i t_{i+1})\) of at most two adjacent blocks. The finite word \(\mu^3(0)=01101001\) contains all four binary adjacent pairs \(00,01,10,11\). Consequently \(\mu^{11}(0)=\mu^8(\mu^3(0))\) contains an occurrence of \(\mu^8(ab)\) for every possible adjacent pair \(ab\), including the pair \(t_i t_{i+1}\). This proves the lemma without assuming that sampling a long prefix is normally exhaustive.

For each \(k\) in the specified range, let \(r\) be its claimed radius and \(L=kr\). The maximum \(L\) is \(130\), hence all relevant factors are represented in that single prefix. The following finite exhaustive certificate has two components.

First, generate the \(2048\) symbols \(t_j\) exactly from binary digit-sum parity, enumerate **every distinct** factor \(f\) of length \(L\) in that prefix, and test all lengths \(m=1,\ldots,r\) until the first \(k\) consecutive blocks of length \(m\) are pairwise distinct. All factors succeed. The enumerated factor counts at the eight values of \(k\) are respectively \(44,86,144,196,240,284,360,388\). The completeness lemma therefore establishes \(\gamma_j(k)\le r\) simultaneously for all \(j\ge0\).

Second, the following table provides actual zero-based starting positions \(j\) for which none of the lengths \(m=1,\ldots,r-1\) gives an antipower. These finite checks use the bits \(t_{j},\ldots,t_{j+k(r-1)-1}\), computed directly by the parity-of-binary-digit-sum definition.

| \(k\) | Claimed \(r\) | Upper-factor count | Lower witness \(j\) |
|---:|---:|---:|---:|
| 3 | 5 | 44 | 0 |
| 4 | 7 | 86 | 16 |
| 5 | 9 | 144 | 16 |
| 6 | 11 | 196 | 10 |
| 7 | 11 | 240 | 0 |
| 8 | 11 | 284 | 0 |
| 9 | 13 | 360 | 64 |
| 10 | 13 | 388 | 53 |

The two certificates together establish both \(R(k)\le r\) and \(R(k)\ge r\), proving the complete displayed statement.

## Verification

Run `python3 verify.py` and `python3 independent_check.py` with the files supplied alongside this document. Both use only the Python standard library and stop with an error if any proposed value fails. `verify.py` checks the factors in the exact \(2048\)-symbol prefix and the lower witnesses. `independent_check.py` generates all factors separately from the four expanded two-letter words \(\mu^h(ab)\), with \(2^h\ge L\), and independently tests the witnesses by binary digit parity. All eight radii, the factor counts, and the witness obstructions were rechecked. Their finite exhaustive coverage is justified by the morphism lemma above; the numerical output by itself would not constitute a proof for all starting positions.

## Relationship to prior work

Fici, Restivo, Silva, and Zamboni introduced antipowers in a publicly posted June 2016 preprint and gave a table of shortest **prefix** antipowers of the Thue–Morse word. For \(k=3,\ldots,10\), their corresponding minimum block lengths are \(5,5,5,5,11,11,11,11\). Those values concern only start \(j=0\), not a worst case over all starts. Defant's 2016 preprint, Narayanan's 2017 preprint and Gaetz's 2018 preprint study prefix or fixed-start antipower lengths and asymptotic behavior. Berger and Defant's later uniform linear existence bound covers the fact that \(R(k)\) is finite, but does not give the exact eight values above. The exact finite uniform initial spectrum is the new claim under comparison; no general asymptotic novelty is asserted.

## Limitations

Only \(3\le k\le10\) is classified. No formula or bound sharper than the cited general literature is claimed for arbitrarily large \(k\). The exhaustive finite certificate has a proven factor-completeness reduction; it does not certify claims outside its explicitly checked range. Priority beyond accessible searches and inspected publications is not independently certified.

## References

- G. Fici, A. Restivo, M. Silva, and L. Q. Zamboni, *Anti-Powers in Infinite Words*, arXiv:1606.02868, first publicly posted 2016-06-09. https://arxiv.org/abs/1606.02868
- C. Defant, *Anti-Power Prefixes of the Thue-Morse Word*, arXiv:1607.05825 (2016). https://arxiv.org/abs/1607.05825
- S. Narayanan, *Functions on Antipower Prefix Lengths of the Thue-Morse Word*, arXiv:1705.06310 (2017). https://arxiv.org/abs/1705.06310
- M. Gaetz, *Anti-power j-fixes of the Thue-Morse word*, arXiv:1808.01528 (2018), *DMTCS* 23:1 (2021). https://arxiv.org/abs/1808.01528
- A. Berger and C. Defant, *On Anti-Powers in Aperiodic Recurrent Words*, arXiv:1902.01291 (2019). https://arxiv.org/abs/1902.01291
