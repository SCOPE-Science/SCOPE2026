# Sharp singleton classification and periodic count of loop-free ternary cyclic digram profiles

## Finding
A cyclic adjacent-pair histogram can fail to identify the underlying circular word. For the three-symbol alphabet, when repeated adjacent symbols are forbidden, **all** uniquely identifying histograms admit an exact structural classification. This also implies that the number of uniquely reconstructing digram profiles is eventually periodic, rather than growing with word length.

Let \(s_n\) be the number of realizable directed-digram histograms of circular words of length \(n\) that determine a unique circular word up to rotation. Then
\[\sum_{n\ge2}s_nz^n=\frac{3z^2}{1-z^2}+\frac{3z^4(1+z^2)}{1-z^2}+\frac{2z^3}{1-z^3}+\frac{6z^5}{1-z^2}+\frac{6z^8}{1-z^3}.\]
For all \(n\ge6\), \((s_n,s_{n+1},\ldots,s_{n+5})=(11,6,15,8,9,12)\) whenever \(n\equiv0\pmod6\). There are three singleton profiles at length two, two at length three, and six at each of lengths four and five.

## Assumptions and scope
Fix the labeled alphabet \(\Sigma=\{0,1,2\}\). A *circular word* is a nonempty cyclic sequence of letters up to orientation-preserving rotation, not reversal or alphabet relabeling. Work only with words of length \(n\ge2\) having no cyclic adjacent equal letters, including across the final-to-first boundary. The directed digram profile \(E=(e_{ij})\) counts each adjacent ordered pair with multiplicity. Its diagonal entries vanish and every row sum equals the corresponding column sum.

Write
\[p=(e_{01},e_{12},e_{20}),\qquad m=(e_{10},e_{21},e_{02}).\]
Balance at vertices forces a common \(t\in\mathbb Z\) with \(p_i-m_i=t\) for all three indices. Define \(u_i=\min(p_i,m_i)\), and let \(h=\#\{i:u_i>0\}\). A realizable profile is singleton when its fiber under the cyclic digram map consists of exactly one circular word. For \(t=0\), singleton holds precisely when \(h=1\), or when \(h=2\) and the smaller of the two positive \(u_i\) equals one. For \(t\ne0\), singleton holds precisely when \(h=0\), or when \(h=1\) and \(\min(|t|,u_i)=1\) for its unique positive \(u_i\).

## Proof
**Balance and connectedness.** The difference equations follow by subtracting incoming from outgoing counts at each vertex. Every nonzero balanced profile with connected non-isolated support admits an Euler circuit; its edge-label sequence is a circular word with that profile. When \(t=0\), nonzero support is a connected one-, two- or three-edge undirected subgraph of the triangle, with symmetric arcs on each present pair. When \(t\ne0\), the three oriented arcs in the sign of \(t\) all occur, making the support connected. Thus the classification covers every realizable loop-free profile.

**Zero circulation.** If only one unordered pair is present, its unique circular output is alternating on two letters. If two pairs are present, their graph is a path with central vertex \(v\). Every Euler circuit splits uniquely at \(v\) into short two-edge return excursions to the two leaves; their counts are the two positive values \(u_i\). Circular words are exactly binary necklaces of these two excursion types. They are unique if and only if one multiplicity equals one. If both multiplicities exceed one, the necklace containing all excursions of each type in a block differs from a necklace with the types interlaced.

If all three pairs are present, relabel the vertices so the symmetric pair multiplicities are \(u\ge1\) on \(0\leftrightarrow1\), \(v\ge1\) on \(1\leftrightarrow2\), and \(w\ge1\) on \(0\leftrightarrow2\). At vertex one use the closed walks \(A:1\to0\to1\) and \(B:1\to2\to1\). One Euler tour is \(A^{u-1}B^vC\), where \(C:1\to0\to(2\to0)^w\to1\), with each walk concatenated at vertex one. A second is \(A^{u-1}B^{v-1}D\), where \(D:1\to0\to(2\to0)^{w-1}\to2\to1\to2\to0\to1\). Each uses precisely the same arcs and counts. The first has no cyclic triple \(120\), while the second has such a triple (the segment \(1\to2\to0\) in \(D\)); hence their circular word labels differ. Therefore no three-pair profile is singleton.

**Nonzero circulation.** Reverse directions if necessary, so \(t=s>0\). If all \(u_i=0\), the profile is exactly \(s\) copies of the oriented triangle and determines the circle \((012)^s\). If exactly one \(u_i>0\), rotate alphabet labels so it is the pair \(0\leftrightarrow1\) with reverse multiplicity \(u\). At vertex zero, each Euler circuit splits into short excursions \(0\to1\to0\) (\(u\) copies) and long excursions \(0\to1\to2\to0\) (\(s\) copies). The fiber is therefore the set of binary necklaces with these two multiplicities, singleton exactly when \(\min(s,u)=1\).

If at least two \(u_i\) are positive, cyclically relabel so they are the pairs \(0\leftrightarrow1\) and \(1\leftrightarrow2\). Put \(u=u_{01}\ge1\), \(v=u_{12}\ge1\), and \(w=u_{02}\ge0\). At vertex one take \(u\) copies of the closed excursion \(A:1\to0\to1\), \(v\) of \(B:1\to2\to1\), \(s-1\) of \(C:1\to2\to0\to1\), and one of \(C_w:1\to2\to(0\to2)^w\to0\to1\). These consume exactly every directed arc of the profile and have no internal occurrence of vertex one. In one cyclic tour order, put all \(A\) excursions then all \(B\) excursions then all \(C\)-type excursions; in another, put the \(C\)-type excursions between the \(A\) and \(B\) blocks. Their excursion-type cyclic orders are distinct, because three different excursion types occur, so the circular words differ. The cases \(t<0\) follow on reversal of all arrows. This proves the classification.

**Enumeration.** Zero-circulation singleton profiles contribute \(3z^2/(1-z^2)\) (one present pair) and \(3z^4(1+z^2)/(1-z^2)\) (two present pairs, minimum multiplicity one). Nonzero-circulation singleton profiles contribute \(2z^3/(1-z^3)\) (pure oriented triangles), plus \(6z^5/(1-z^2)+6z^8/(1-z^3)\) (one reverse pair, with the smaller excursion multiplicity one, splitting off the overlap). Summing proves the stated generating function and six-periodic tail.

## Verification
Run `python3 verify.py`. It independently exhausts all loop-free ternary circular words at lengths two through ten, grouping by cyclic digram profiles, and then checks every nonzero balanced loop-free profile of lengths two through twenty-nine using an exact directed matrix-tree / Euler-circuit count combined with Burnside's formula for rotation. It checks each profile against the theorem, not merely the total counts. Computations confirm finite instances; the unbounded assertion follows from the preceding proof.

## Relationship to prior work
The classical correspondence of balanced pair-count matrices and Eulerian directed multigraphs underlies Markov-type enumeration (Jacquet, Knessl and Szpankowski). That work enumerates *realizable profiles*, not the present question of which profiles have exactly one **cyclic realization**. Bernardini et al. study making de Bruijn graphs Eulerian, an algorithmic problem likewise not implying singleton-fiber classifications. Here the structural switch from paths and isolated directed cycles to non-unique Euler circuits is decisive. Earlier work on linear binary two-read multispectra counts different objects and cannot imply the three-symbol loop-free cyclic theorem.

## Limitations
The result requires a fixed three-letter **labeled** alphabet and forbids cyclic equal-letter neighbors. It classifies only singleton cyclic fibers, not the sizes of all nonsingleton fibers. No assertion about arbitrary alphabets, reversal equivalence or length-one circles is made. Literature searches cannot rule out all unindexed equivalent graph-theoretic formulations; independent scientific verification is not claimed.

## References
- P. Jacquet, C. Knessl, W. Szpankowski, *Counting Markov Types, Balanced Matrices, and Eulerian Graphs*, IEEE Trans. Inform. Theory 58 (2012), https://doi.org/10.1109/TIT.2012.2191476.
- P. Jacquet, C. Knessl, W. Szpankowski, *Counting Markov Types* (preprint), https://dmtcs.episciences.org/en/articles/2768/download.
- G. Bernardini, H. Chen, G. Loukides, S. P. Pissis, L. Stougie, M. Sweering, *Making de Bruijn Graphs Eulerian*, CPM 2022, https://doi.org/10.4230/LIPIcs.CPM.2022.12.
