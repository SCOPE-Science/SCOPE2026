# Sharp one-substitution dinucleotide-profile capacity and de Bruijn saturation

## Finding
Let \(\Sigma\) be a fixed labeled alphabet of \(q\ge3\) symbols. For any linear word \(w=w_1\cdots w_n\), \(n\ge3\), let \(P_2(w)=(c_{ab}(w))_{a,b\in\Sigma}\) be its *oriented dinucleotide profile*, counting every overlapping adjacent pair. Define the one-substitution profile ball
\[
\mathcal S_2(w)=\{P_2(v):v\in\Sigma^n,\ d_H(v,w)=1\},\qquad B_2(w)=|\mathcal S_2(w)|,
\]
where the changed letter must be different and coincident resulting profiles are counted only once.

For all such words,
\[
\boxed{B_2(w)\le M_q=(q-1)(q^3-q+2).}
\]
The bound is sharp for every length \(n\ge q^3+2\), and its **first possible attainment** is exactly
\[
\boxed{N_q=q^3+2.}
\]
A word of this first attaining length maximizes \(B_2\) **if and only if** its successive three-letter factors contain each of the \(q^3\) possible triples exactly once. Consequently the number of indexed, labeled length-\(N_q\) maximizers equals
\[
\boxed{(q!)^{q^2}.}
\]
The capacities for \(q=3,4,5,6\) are respectively \(52,186,488,1060\); their first attaining lengths are respectively \(29,66,127,218\).

## Assumptions and scope
Words are indexed, **linear**, and over a fixed labeled alphabet; the first and last symbols are not adjacent. Histograms keep multiplicity, orientation and all \(q^2\) coordinates. Exactly **one original symbol** is replaced by a **different** symbol. All choices of the changed position and replacement count as one profile if their resulting histogram vectors coincide. Length is unchanged by substitution. The sharp threshold and extremizer enumeration are asserted for integers \(q\ge3\) and \(n\ge3\). The same universal upper bound also holds for shorter words, but the first-attainment statement intentionally excludes the binary exceptional case.

Write \(E_{ab}\) for the matrix with a unit in ordered-pair coordinate \((a,b)\) and zeros elsewhere. A vector's row and column sums are with respect to these q-by-q coordinates. The permutation of the labeled symbols is not quotiented out when counting maximizers.

## Proof
**1. Local substitution-change formula.** An interior replacement \(b\to d\), \(d\ne b\), when the two neighbors are \(a,c\), changes the profile by
\[
\Delta(a,b,c;d)=E_{ad}+E_{dc}-E_{ab}-E_{bc}.
\]
This is an exact identity, including overlaps and possible equal neighboring letters. For a fixed ordered replacement \((b,d)\), put
\[
R_a=E_{ad}-E_{ab},\qquad C_c=E_{dc}-E_{bc};\qquad \Delta=R_a+C_c.
\]
The row-sum and column-sum vectors of \(\Delta\) are both \(e_d-e_b\), so interior changes from different ordered replacements cannot coincide.

**2. All interior collisions.** For fixed \(b\ne d\), the \(q^2\) pairs of neighboring symbols \((a,c)\) yield exactly \(q^2-1\) distinct changes: the only collision is
\[
\Delta(b,b,d;d)=\Delta(d,b,b;d)=E_{dd}-E_{bb}.
\]
To prove completeness, suppose \(R_a+C_c=R_{a'}+C_{c'}\). If \(a=a'\), distinct column supports of \(C_c\) force \(c=c'\); similarly \(c=c'\) forces \(a=a'\). For a nontrivial equality \(a\ne a'\), the difference \(R_a-R_{a'}\) has precisely the two nonzero rows \(a,a'\), while \(C_{c'}-C_c\) has nonzero rows only \(b,d\). Thus \(\{a,a'\}=\{b,d\}\). Comparing columns analogously forces \(\{c,c'\}=\{b,d\}\). Of the four choices, equality of signed entries occurs only between \((a,c)=(b,d)\) and \((a',c')=(d,b)\), as the displayed identity shows. There are therefore exactly \(q(q-1)(q^2-1)\) different *potential* interior-profile changes.

**3. Boundary vectors and the universal upper bound.** Replacing the first letter \(b\) by \(d\), with second letter \(c\), contributes \(E_{dc}-E_{bc}\); its column sums vanish but row sums are \(e_d-e_b\). Replacing the last letter \(b\) by \(d\), with penultimate letter \(a\), contributes \(E_{ad}-E_{ab}\); its row sums vanish but column sums are \(e_d-e_b\). Each end has exactly \(q-1\) alternatives; neither end type can agree with an interior change or with the other end type, because \(d\ne b\) and these row/column-sum signatures differ. Combining the disjoint families proves
\[
B_2(w)\le q(q-1)(q^2-1)+2(q-1)=(q-1)(q^3-q+2).
\]

**4. Necessity of every three-letter window.** Fix any ordered triple \((a,b,c)\). Because \(q\ge3\), there is a replacement \(d\ne b\) for which \((a,c)\) is **not** either of the two colliding contexts \((b,d),(d,b)\): if \(a=b\) and \(c\ne b\), choose \(d\notin\{b,c\}\); if \(c=b\) and \(a\ne b\), choose \(d\notin\{b,a\}\); otherwise any \(d\ne b\) works. By Step 2, this change vector is realized by no other interior context with the same replacement and, by Step 1, by none with a different replacement. The boundary row/column signatures exclude boundary realization. Thus a word attaining the universal bound must contain the literal factor \(abc\). The triple was arbitrary, so every one of the \(q^3\) possible triples must occur. As a linear length-\(n\) word has only \(n-2\) three-letter windows, \(n\ge q^3+2\) is necessary.

**5. Construction and first-length rigidity.** Take any cyclic de Bruijn word of order three over \(\Sigma\), containing each length-three cyclic factor exactly once. Write its \(q^3\) cyclic letters and append the first two. The resulting linear word has length \(q^3+2\) and contains every triple. Consequently every possible interior change and all \(2(q-1)\) end changes occur, attaining the bound. Arbitrarily appending letters preserves the presence of every triple and therefore preserves maximality for each larger length. At the minimal length there are exactly \(q^3\) windows, so necessity and distinctness force each triple to occur exactly once. Conversely that condition suffices. This proves the threshold and characterizes all first-length maximizers.

**6. Counting the first-length maximizers.** The order-three de Bruijn digraph has the \(q^2\) ordered pairs \((a,b)\) as vertices and one arc \((a,b)\to(b,c)\) for every triple \((a,b,c)\). Every vertex has indegree and outdegree \(q\). Its adjacency matrix \(A\) satisfies \(A^2=J\), the all-ones matrix; hence the nonzero eigenvalue of \(A\) is \(q\) once, with all remaining eigenvalues zero. The graph is Eulerian and strongly connected, so the directed Matrix-Tree theorem, equality of its rooted cofactors, and the Laplacian \(qI-A\) give \(q^{q^2-3}\) in-arborescences rooted at any fixed vertex. The BEST Euler-tour formula therefore gives
\[
q^{q^2-3}((q-1)!)^{q^2}
\]
cyclic de Bruijn words modulo cyclic rotation. Every order-three de Bruijn cycle has exactly \(q^3\) distinct indexed starting positions: a nontrivial rotational period would repeat a triple. Linearizing at these starts yields
\[
q^3\,q^{q^2-3}((q-1)!)^{q^2}=(q!)^{q^2}
\]
different length-\(q^3+2\) words, as claimed.

## Verification
Three standalone Python programs accompany this note. `verify_local.py` separately enumerates all local mutation-change matrices for alphabet sizes two through eight; checks the ordered-replacement classes and their unique cross-context collision; then directly builds mutant profile balls for order-three de Bruijn witness words. The output includes \((q,M_q,N_q)=(3,52,29),(4,186,66),(5,488,127)\), and ends `LOCAL_CHECK_PASS`.

`verify_enumeration.py` directly enumerates *all input words* up to lengths eleven (binary), eight (ternary), and six (quaternary) and computes every resulting profile from literal one-letter substitutions, without importing the first checker. It also uses a separate Eulerian construction of de Bruijn witnesses through \(q=6\), and counts sixteen indexed order-three binary de Bruijn words as a cross-check. Its output ends `ENUMERATION_CHECK_PASS`.

`verify_tree_count.py` evaluates directed Laplacian cofactors by exact integer elimination for alphabet sizes two through five and independently checks the BEST/count identity. Its output ends `TREE_COUNT_PASS`. These bounded calculations corroborate, but do not replace, the all-parameter arguments in Steps 1–6. The named scripts and recorded outputs are included with this result and require only a standard Python interpreter.

## Relationship to prior work
In Kiah, Puleo and Milenkovic's *Codes for DNA Sequence Profiles* (2015), oriented \(k\)-gram count vectors and substitutions in synthesis/sequencing channels are foundational. The paper studies codes and global profile constraints, not the *number of distinct length-two profile outputs under one source-letter substitution for each fixed word*, the exact q-ary maximum, or the first saturating length.

Simmonds and coauthors (2013) directly model context-dependent effects of a base mutation on dinucleotide counts. The local plus/minus formula in Step 1 is therefore an application of established local mutation bookkeeping; it is not claimed as independently novel. That paper concerns mutation/selection pressures, not output-profile collisions and exact saturation.

En Gad's preprint *Polynomially larger deletion codes by linear hashing of substring counts*, first publicly posted September 16, 2026 (and inspected in its October 18 revised public version), establishes a substring-count hashing method to build robust coding schemes, including discussion of replacement errors. Its inspected statements, proofs and examples do not supply the local one-substitution oriented-dinucleotide-profile sphere capacity or its rigidity theorem. He, Kari and Millan Arias (2025) discuss the connection between \(k\)-mer frequencies and Eulerian/de Bruijn graph constructions but do not give the mutant-ball extremal formula.

Published exact results on *binary one-deletion* and *binary one-insertion* dinucleotide-profile balls concern different edit operations and alphabets. Published exact *ternary ordered-bigram multispectrum* enumeration concerns the **global number of different profiles as the source word ranges**, not the local mutation-image capacity of one fixed source. Their statements do not imply the displayed sharp bound, first-length theorem, or maximizer count.

## Limitations
The exact sharp first-attainment result is for \(q\ge3\). The binary model has additional context collisions and first saturates earlier; no binary threshold is asserted here. The result concerns full oriented length-two multiplicity profiles from one source-symbol substitution, not higher-order reads, insertion/deletion errors, more than one substitution, cyclic source words, or the size of an error-correcting code. Shorter-length capacities below the first saturating length are not classified. An unindexed equivalent computation in the study of Markov types or mutation histograms remains a genuine historical-priority risk; no independent validation has been performed.

## References
1. E. En Gad, *Polynomially larger deletion codes by linear hashing of substring counts*, arXiv:2609.19493v1, first public September 16, 2026; inspected revised public full text at https://arxiv.org/html/2609.19493v2.
2. H. M. Kiah, G. J. Puleo, O. Milenkovic, *Codes for DNA Sequence Profiles*, arXiv:1502.00517v1, first public February 2, 2015, https://arxiv.org/html/1502.00517v1.
3. Simmonds et al., *Modelling mutational and selection pressures on dinucleotides in eukaryotic phyla—selection against CpG and UpA in cytoplasmically expressed RNA and in RNA viruses*, BMC Genomics 14 (2013), article 610, https://link.springer.com/article/10.1186/1471-2164-14-610.
4. He, Kari and Millan Arias, *Bridging Chaos Game Representations and k-mer Frequencies of DNA Sequences*, arXiv:2506.22172, first public June 27, 2025, https://arxiv.org/abs/2506.22172.
5. *Exact single-insertion dinucleotide-profile ambiguity in binary words* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-single-insertion-dinucleotide-profile-ambiguity-in-binary--7545727346c0.
6. *The complete one-deletion dinucleotide-profile ball distribution for binary words* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-complete-one-deletion-dinucleotide-profile-ball-distribution--294c530e44d7.
7. *Exact ternary ordered-bigram multispectrum counts and the degree-six law* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-ternary-ordered-bigram-multispectrum-counts-and-the-degree--f0497779133f.
