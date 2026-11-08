# Dyadic-period Abelian-power rigidity and exact occurrence frequencies in the period-doubling word

## Finding

Let \(p=p_0p_1\cdots\) be the one-sided binary period-doubling word, the fixed point beginning in \(1\) of \(\delta(1)=10\), \(\delta(0)=11\). For every \(k\ge 0\), set \(m=2^k\), \(b_k=1-(k\bmod 2)\), and
\[
W_k=p_0p_1\cdots p_{m-2}b_k,
\]
where the displayed initial prefix is empty when \(m=1\). Let \(\operatorname{rot}_r\) denote left rotation through \(r\) positions. For each integer exponent \(e\ge2\), a length-\(em\) factor of \(p\) is an Abelian \(e\)-power of block length \(m\) if and only if it is an ordinary \(e\)-power of that block length. Its complete factor set is
\[
\mathcal A_{k,e}=\begin{cases}
\{(\operatorname{rot}_r W_k)^e:0\le r<m\},& e=2,3,\\
\varnothing,&e\ge4.
\end{cases}
\]
The \(m\) displayed words are pairwise distinct. Hence there are exactly \(m\) distinct Abelian squares, exactly \(m\) distinct Abelian cubes, and no Abelian fourth or higher powers with prescribed period \(m\). For every fixed \(r\), the natural frequency of \((\operatorname{rot}_r W_k)^2\) as a factor starting at an integer index is \(1/(3m)\); that of \((\operatorname{rot}_r W_k)^3\) is \(1/(6m)\). Consequently the densities of starting indices of dyadic-period Abelian squares and cubes are \(1/3\) and \(1/6\), independently of \(k\).

## Assumptions and scope

Indices start at zero. An Abelian \(e\)-power of block length \(m\) has exactly \(e\) consecutive, nonempty, length-\(m\) blocks with the same number of \(1\)'s. An ordinary \(e\)-power has these blocks equal as words. Distinct factors means distinct contiguous binary strings, not occurrences; densities are limits over starting indices \(0\le i<N\) as \(N\to\infty\). This theorem fixes the proposed block period to a power of two; it makes no assertion about other periods.

## Proof

**Arithmetic description.** The fixed point satisfies
\[
p_i=1-\bigl(\nu_2(i+1)\bmod2\bigr)\qquad(i\ge0).
\]
Indeed, its odd-indexed entries are zero and its even-indexed entries are the complements of the preceding substitution's source letters; equivalently, \(p_{2j}=1\) and \(p_{2j+1}=1-p_j\), agreeing with the valuation formula. Here \(\nu_2(t)\) is the exponent of two dividing the positive integer \(t\).

**Dyadic one-coordinate rigidity.** Fix \(m=2^k\). If the positive integer \(i+1\) is not divisible by \(m\), then \(\nu_2(i+1)=\nu_2(i+m+1)\), so \(p_i=p_{i+m}\). Each consecutive length-\(m\) block therefore has precisely the same letters as the next block except possibly at its unique position whose global index plus one is a multiple of \(m\). The exceptional relative position is identical in each block of a fixed partition. Two such adjacent blocks thus have the same number of ones if and only if their exceptional letters agree; that is equivalent to literal equality. By applying this to every adjacent pair of blocks, Abelian \(e\)-powers and ordinary \(e\)-powers coincide for this prescribed length \(m\).

**Exact factor list.** Define the aligned length-\(m\) blocks \(Q_j=p_{(j-1)m}\cdots p_{jm-1}\) for \(j\ge1\). The arithmetic formula yields
\[
Q_j=p_0\cdots p_{m-2}\,c_j,\qquad c_j=1-\bigl((k+\nu_2(j))\bmod2\bigr).
\]
Every two consecutive positive integers include an odd one. Therefore any constant run of two or more exceptional letters \(c_j\) must have the value \(b_k\); every aligned block in such a run equals \(W_k\). Every four consecutive positive integers include an integer congruent to \(2\) modulo \(4\), whose exceptional letter is opposite to \(b_k\). Hence no constant run has length four. On the other hand, \(j=3,4,5\) has valuation parities \(0,0,0\), proving that a run of length three occurs. Each constant run of length \(e=2,3\) supports every rotation of \(W_k^e\): starting at offset \(r\) within the first aligned block, the factor uses the same \(e\) exceptional letters and otherwise the common prefix. Conversely, every starting index has a unique residue \(r\) modulo \(m\), and equality of its \(e\) blocks forces exactly that constant exceptional-letter run. This proves the stated set equality and absence for \(e\ge4\).

**Distinct rotations.** If \(k\ge1\), the letters of \(W_k\) at positions \(m/2-1\) and \(m-1\) differ, since their valuation parities are those of \(k-1\) and \(k\). If \(W_k\) had a proper period whose length divided \(m\), that length would divide \(m/2\) and these letters would agree. Thus \(W_k\) is primitive. The \(m\) rotations are distinct. For \(k=0\), \(m=1\) and the claim is immediate.

**Occurrence frequencies.** At a start \(qm+r\), \(0\le r<m\), an \(e\)-power occurs precisely when \(\nu_2(q+1),\ldots,\nu_2(q+e)\) are all even. For \(e=2\), one of the two integers is odd, and the even one must have a positive even valuation. The set of positive integers of valuation \(2h\) has natural density \(2^{-(2h+1)}\). Summing \(h\ge1\) gives \(1/6\), with the even integer occupying either of two positions, hence density \(1/3\) of eligible \(q\). For \(e=3\), the middle integer must be even with positive even valuation and its neighbors are odd, giving density \(1/6\). Every residue \(r\) produces its uniquely assigned rotation, so division by \(m\) gives individual-factor frequencies \(1/(3m)\) and \(1/(6m)\). The densities exist since sets with fixed 2-adic valuations are unions of residue classes and the omitted high-valuation tail has arbitrarily small density. This completes the proof.

## Verification

The standalone standard-library programs `check_factors.py` and `check_arithmetic.py` use different constructions: substitution iteration versus direct 2-adic valuation. The first exhaustively compares the actual and predicted distinct Abelian-power factor sets for every \(k\) from \(0\) to \(8\) and exponents \(2,3,4,5\), using a length-\(32768\) prefix. The second verifies one-coordinate Hamming rigidity and Parikh-to-literal equivalence for all periods \(2^k\) with \(0\le k\le10\), first 301 starts, and four adjacent pairs at each start. All assertions passed. The proof above establishes the infinite scope independently of these finite experiments.

A non-dyadic qualification is essential: the length-12 factor `101110101011` occurs at index zero and is an Abelian fourth power with period three, since its blocks `101`, `110`, `101`, `011` each contain two ones. It is not an ordinary fourth power.

## Relationship to prior work

Cassaigne, Richomme, Saari and Zamboni (2010) establish general occurrence of arbitrary Abelian powers under bounded Abelian complexity, without prescribing this dyadic period in the period-doubling word. Cassaigne, Fici, Sciortino and Zamboni (2014) show that its cyclic factor complexity at dyadic lengths equals two, but their conjugacy-class count neither identifies which factors repeat at dyadic periods nor yields Abelian-power rigidity and the exact occurrence densities. Parreau, Rigo, Rowland and Vandomme (2014) study 2-abelian complexity of the same automatic word, which is a different equivalence invariant of single factors. The present statement fixes exact repetition length and exponent and counts both distinct factors and their occurrence frequencies. Comparison is based on inspected primary sources; no universal historical-priority guarantee is implied.

## Limitations

Only the one-sided binary period-doubling fixed point specified above, exact integer exponents, and prescribed periods \(2^k\) are classified. Abelian powers at other periods may have different behavior. No claim about general automatic words, approximate repetition, or maximal code sizes is made. Historical-priority checking is limited to accessible indexed sources; external independent validation has not been performed.

## References

- J. Cassaigne, G. Richomme, K. Saari, L. Q. Zamboni, *Avoiding Abelian Powers in Binary Words with Bounded Abelian Complexity* (public preprint 2010-05-14), https://arxiv.org/abs/1005.2514 .
- J. Cassaigne, G. Fici, M. Sciortino, L. Q. Zamboni, *Cyclic Complexity of Words* (public preprint 2014-02-24), https://arxiv.org/abs/1402.5843 .
- A. Parreau, M. Rigo, E. Rowland, E. Vandomme, *A new approach to the 2-regularity of the ℓ-abelian complexity of 2-automatic sequences* (public preprint 2014-05-14), https://arxiv.org/abs/1405.3532 .
