# Exact nonlinear complexity and full complexity spectrum of two-spike periodic words

## Finding

Fix an integer \(q\ge3\), an alphabet \(\mathcal A=\{0,1,\ldots,q-1\}\), and an integer \(n\ge4\). Let \(w\in\mathcal A^n\) have exactly two nonzero entries, with nonzero values \(\alpha,\beta\), and let \(w^\infty\) be its right-infinite periodic repetition. Write \(M(w)\) for the least positive length of an unrestricted, deterministic feedback shift register generating \(w^\infty\). Put \(d\) equal to the smaller cyclic distance between its two nonzero positions and \(L=n-d\), so \(1\le d\le L\).

**Exact complexity.** For every such word,
\[
M(w)=\begin{cases}
\max\{L-1,2d\},&d<L,\ \alpha=\beta,\\
L-1,&d<L,\ \alpha\ne\beta,\\
d-1,&d=L,\ \alpha=\beta,\\
d,&d=L,\ \alpha\ne\beta.
\end{cases}
\]
In particular, for equal nonzero symbols the generic answer undergoes a sharp change at \(3d=n-1\), while antipodal equal symbols yield a shorter primitive period and a separate exceptional value.

**Exact period-word distribution.** Define \(P_{n,q}(z)=\sum_w z^{M(w)}\), summing over all length-\(n\) indexed words with exactly two nonzero entries. With \(D=\lfloor(n-1)/2\rfloor\),
\[
\begin{aligned}
P_{n,q}(z)={}&n(q-1)\sum_{d=1}^{D}z^{\max\{n-d-1,2d\}}\\
&+n(q-1)(q-2)\sum_{d=1}^{D}z^{n-d-1}\\
&+\mathbf 1_{2\mid n}\,\frac n2\left((q-1)z^{n/2-1}+(q-1)(q-2)z^{n/2}\right).
\end{aligned}
\]
Thus the coefficient of \(z^k\) is the exact number of such length-\(n\) words whose nonlinear complexity is \(k\). For instance, \(P_{12,3}(z)=12z^5+36z^6+24z^7+72z^8+48z^9+72z^{10}\); its coefficients total \(\binom{12}{2}(3-1)^2=264\).

## Assumptions and scope

A feedback shift register of length \(k\) has a state containing the preceding \(k\) symbols and a deterministic map \(f:\mathcal A^k\to\mathcal A\) that outputs the next symbol. The feedback map is arbitrary, not restricted to linear or nonsingular maps. The sequence has period dividing \(n\), not necessarily least period \(n\). Positions and symbols are indexed; cyclic rotations are counted as distinct length-\(n\) words unless their coordinates agree. Exactly two nonzero positions are required. The formula also holds for \(q=2\) after setting \(\alpha=\beta=1\), although the stated full alphabet claim uses \(q\ge3\).

## Proof

**1. Successor-conflict criterion.** For any periodic word \(w\), a length-\(k\) register exists precisely when every pair of cyclic length-\(k\) factors that agree have the same next symbol. Necessity is immediate: a deterministic feedback map cannot assign different successors to the same state. Sufficiency follows by defining the map on every encountered factor by its unique successor and assigning arbitrary outputs on unencountered factors. Consequently, \(M(w)=1+H(w)\), where \(H(w)\) is the largest length of a pair of equal cyclic factors with different successors. The empty factor has length zero.

By cyclic rotation we may put the nonzero positions at \(0,d\) with \(1\le d\le n/2\). The two intervening zero-run lengths are \(d-1\) and \(L-1\). A cyclic factor pair has *different phases* if its starting residues modulo the least period differ. Identical phases have identical successors and never contribute to \(H(w)\).

**2. Unequal nonzero symbols.** If \(\alpha\ne\beta\), each nonzero value occurs at only one residue modulo \(n\). Therefore two distinct phases cannot agree on any factor containing a nonzero symbol; such a factor would align the same unique nonzero value and force identical phases. Every conflicting pair must consist entirely of zeros.

When \(d<L\), a zero factor followed by another zero can have length at most \(L-2\), whereas a zero factor followed by a nonzero symbol can have length at most \(L-1\). For a conflict at least one successor is zero, or the successors are two different nonzero values. In the latter case both factors lie at the ends of different zero runs, so the common length is at most \(d-1\le L-2\). Hence \(H(w)\le L-2\). The long zero run contains two overlapping occurrences of \(0^{L-2}\), one with next symbol zero and the other with next symbol nonzero. Since \(L\ge3\) for \(n\ge4\) and \(d<L\), these witness \(H(w)=L-2\). Thus \(M(w)=L-1\).

When \(d=L\), both zero runs have length \(d-1\). Their entire blocks of \(d-1\) zeros have successors \(\alpha\) and \(\beta\), respectively, and no zero factor is longer. Thus \(H(w)=d-1\), yielding \(M(w)=d\).

**3. Equal nonzero symbols at unequal gaps.** Suppose \(\alpha=\beta\) and \(d<L\). The two-point support \(\{0,d\}\subset\mathbb Z/n\mathbb Z\) has no nonzero translational stabilizer: an interchange of its two points would require \(2d=n\), which is excluded. Consequently two distinct cyclic phases can align at most one nonzero symbol. If a common factor contains such an aligned nonzero symbol, then one of the two copies has only \(d-1\) consecutive zeros before that symbol, and the other has only \(d-1\) consecutive zeros after it. Hence a conflicting common factor containing a nonzero symbol has length at most \(2d-1\). If it contains no nonzero symbol, its conflicting length is at most \(L-2\), by the preceding zero-run argument with equal successor labels. Thus
\[
H(w)\le\max\{L-2,2d-1\}.
\]
Both terms are sharp: two overlapping zero factors inside the longer zero run produce a conflict of length \(L-2\); and the factors beginning \(d-1\) positions before each of the two nonzero symbols agree for exactly \(2d-1\) letters (\(d-1\) zeros, one common nonzero symbol, then \(d-1\) zeros), after which one has a nonzero successor and the other has zero. Hence \(H(w)=\max\{L-2,2d-1\}\) and \(M(w)=\max\{L-1,2d\}\).

**4. Equal nonzero symbols at equal gaps.** If \(d=L\) and \(\alpha=\beta\), the word has least period \(d\) and contains exactly one nonzero symbol per least period. Two different phases of this shorter period can agree only on zero factors. The unique zero run has length \(d-1\), and its two overlapping zero factors of length \(d-2\) give successors zero and nonzero. Every conflicting pair of zero factors has length at most \(d-2\). Therefore \(M(w)=d-1\). The assumption \(n\ge4\) ensures \(d\ge2\) here.

**5. Spectrum.** For every \(d<n/2\), there are exactly \(n\) unordered position pairs of smaller cyclic spacing \(d\); for even \(n\) there are precisely \(n/2\) antipodal pairs. At each pair there are \(q-1\) assignments with equal nonzero symbols and \((q-1)(q-2)\) assignments with unequal nonzero symbols. Inserting the four complexity cases proves the displayed generating polynomial. Every indexed word is counted once, including those with smaller primitive period. Its value at \(z=1\) is \(\binom n2(q-1)^2\), confirming the full population count. \(\square\)

## Verification

The standalone standard-library Python program `checker.py` independently computes the minimum register length from successor consistency for every two-nonzero word with \(4\le n\le23\) and \(2\le q\le4\); it compares the exact distribution to the generating-polynomial coefficients. It also performs a separate cyclic-phase-pair test for \(4\le n\le17\) and three choices of spike labels. Its observed result is `CHECK_OK complete-word tests 28280 histograms 60 pairwise-rotation cases 210`. These exhaustive finite checks support the algebra and index handling but are not a substitute for the preceding proof for arbitrary parameters. Execute `python3 checker.py` from the extracted folder with no dependencies.

## Relationship to prior work

The successor-conflict characterization is classical (Jansen and Boekee) and is used here, not claimed new. Yuan, Li and Zeng (first released February 1, 2026) classify high-nonlinear-complexity **binary** periodic sequences and enumerate their unconstrained classes; their inspected statements do not give the present two-nonzero \(q\)-ary distance-and-color classification or its full low-weight generating polynomial. Yuan et al. (2024) provide general generation algorithms for binary periodic sequences with prescribed nonlinear complexity, but do not provide the claimed \(q\)-ary two-spike spectrum. A 2024 survey describes general \(q\)-ary bounds and the successor-conflict criterion without establishing these explicit weight-two counts. The existing general tools imply an algorithm to calculate a given sequence's complexity; extracting the closed form, distinguishing spike colors, and exactly enumerating every length-\(n\) two-spike word are the substantive specialized results.

## Limitations

The result concerns unrestricted deterministic feedback functions and two nonzero positions, not LFSR linear complexity, feedback-with-carry registers, or multiple nonzero positions. The existence of a short register is not a cryptographic security guarantee. The polynomial counts indexed words, not rotation orbits or primitive necklaces. The general priority search cannot exclude a previously unindexed equivalent specialization; independent validation has not been performed.

## References

- Q. Yuan, C. Li, X. Zeng, *The structure and enumeration of periodic binary sequences with high nonlinear complexity*, arXiv:2602.01134, initial public version February 1, 2026. https://arxiv.org/html/2602.01134v1
- Q. Yuan, C. Li, X. Zeng, T. Helleseth, D. He, *Further Investigations on Nonlinear Complexity of Periodic Binary Sequences*, arXiv:2404.16313, April 25, 2024. https://arxiv.org/abs/2404.16313
- *A Survey on Complexity Measures for Pseudo-Random Sequences*, Cryptography 8 (2024), article 25. https://www.mdpi.com/2410-387x/8/2/25
