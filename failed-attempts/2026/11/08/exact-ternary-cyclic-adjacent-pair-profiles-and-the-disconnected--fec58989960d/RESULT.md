# Exact ternary cyclic adjacent-pair profiles and the disconnected correction

## Finding

For every integer \(n\ge 1\), let \(P_n\) be the number of distinct nine-entry cyclic adjacent-pair count matrices of length-\(n\) words over the labeled alphabet \(\{0,1,2\}\). Then the exact ordinary generating function is

\[
\begin{aligned}
G(z)=\sum_{n\ge1}P_nz^n={}&\frac{3z}{1-z}
+\frac{3z^2}{(1-z^2)(1-z)^2}\\
&+\frac{3z^4}{(1-z^2)^2(1-z)^3}
+\frac{z^6}{(1-z^2)^3(1-z)^3}\\
&+\frac{2z^3}{(1-z^3)(1-z^2)^3(1-z)^3}.
\end{aligned}
\]

The first twelve values, at lengths \(1,\ldots,12\), are
\[
(3,6,11,24,48,95,174,306,510,819,1266,1901).
\]

Let \(B_n\) count **all** nonnegative, balanced \(3\times3\) integer matrices of total entry sum \(n\), without a connectivity requirement, including \(B_0=1\). The exact disconnected-matrix correction is
\[
\sum_{n\ge1}(B_n-P_n)z^n
=\frac{3z^2}{(1-z)^2}+\frac{z^3}{(1-z)^3}
+\frac{3z^3}{(1-z^2)(1-z)^3},
\]
while
\[
\sum_{n\ge0}B_nz^n
=\frac{1+z^3}{(1-z^3)(1-z^2)^3(1-z)^3}.
\]

Consequently, \(P_n\) is the exact maximum size of a zero-error length-\(n\) ternary code whose only observation is the multiset of all cyclic adjacent ordered pairs. The leading asymptotic, which is already known from earlier Markov-type work, is \(P_n\sim n^6/8640\); the newly explicit disconnected correction satisfies \(B_n-P_n\sim n^3/4\).

## Assumptions and scope

Words have indexed positions \(0,\ldots,n-1\), with cyclic wraparound. For \(w\in\{0,1,2\}^n\), define
\[
m_{ij}(w)=\#\{r\in\{0,\ldots,n-1\}:w_r=i,\ w_{(r+1)\bmod n}=j\}.
\]
Two words have the same observed profile exactly when all nine entries of \(m(w)\) coincide. Word rotation does not change the profile, but alphabets are labeled and no quotient by global alphabet permutations is taken. Words using just one or two of the available symbols are included. Only nonempty words are counted in \(G(z)\).

A nonnegative integer matrix is *balanced* if its row sums equal its column sums at every vertex. Its *nonisolated support graph* has vertex set consisting of symbols incident to at least one positive entry, and an undirected edge between distinct vertices whenever either corresponding directed matrix entry is positive. Loops make their vertices active but do not connect distinct vertices.

## Proof

**Eulerian criterion.** The directed multigraph with \(m_{ij}\) edges from \(i\) to \(j\) is realized as the cyclic adjacency counts of one word if and only if it is balanced, has positive total size, and its nonisolated undirected support is connected. Necessity follows from walking around the cyclic word. Conversely, the Eulerian-circuit criterion for a finite balanced connected directed multigraph yields a closed edge walk; reading its consecutive vertex labels produces a realizing cyclic word. Loops and parallel edges pose no exception.

**Three-state flow parameterization.** Balance forces the three signed flows to agree:
\[
m_{01}-m_{10}=m_{12}-m_{21}=m_{20}-m_{02}=d\in\mathbb Z.
\]
Write \(a_i=m_{ii}\ge0\). If \(d=0\), the three unordered off-diagonal pairs have common multiplicities \(b_{01},b_{12},b_{20}\ge0\), with total weight \(2(b_{01}+b_{12}+b_{20})\), and the three loops contribute \(a_0+a_1+a_2\).

For \(d=0\), classify by the number of strictly positive \(b\)-variables. If none is positive, connectedness requires exactly one strictly positive loop and two zero loops, yielding \(3z/(1-z)\). If exactly one is positive, select the edge in three ways; its two endpoints may have any loops, while the isolated third vertex must have zero loop. The contribution is \(3z^2/((1-z^2)(1-z)^2)\). If exactly two are positive, the graph on all three vertices is a path, and all loops are unrestricted; its contribution is \(3z^4/((1-z^2)^2(1-z)^3)\). If all three are positive, the graph is connected and the contribution is \(z^6/((1-z^2)^3(1-z)^3)\). These four cases are disjoint and exhaustive.

If \(d>0\), put \(m_{01}=d+b_{01}\), \(m_{10}=b_{01}\), and cyclically the analogous formulas for the \((1,2)\) and \((2,0)\) pairs. The \(d\) baseline copies of the three oriented cycle arcs force connectivity; all three \(b\)-variables and all loops are unrestricted. The sign \(d<0\) contributes the same amount in the reversed orientation. Summing over \(|d|\ge1\) gives
\[
2\left(\sum_{d\ge1}z^{3d}\right)
\frac{1}{(1-z^2)^3(1-z)^3}
=\frac{2z^3}{(1-z^3)(1-z^2)^3(1-z)^3}.
\]
Adding the five disjoint contributions proves the displayed formula for \(G(z)\).

If connectivity is ignored, the \(d=0\) choices contribute \(((1-z^2)^3(1-z)^3)^{-1}\), including the empty matrix, and the two nonzero signs contribute the last term above. This simplifies to the displayed \(B(z)\). A disconnected balanced matrix necessarily has \(d=0\), because \(d\ne0\) contains an oriented triangle. Either no off-diagonal pair is positive and two or three isolated vertices have positive loops, contributing \(3(z/(1-z))^2+(z/(1-z))^3\); or exactly one pair is positive and the third vertex has a positive loop, contributing \(3z^3/((1-z^2)(1-z)^3)\). These are all disconnected cases, proving the exact correction.

For the coding interpretation, distinct profiles can be distinguished with zero error. Every code contains at most one representative from any given profile, and selecting one representative from each of the \(P_n\) profiles attains that bound. Finally, at \(z=1\), the known balanced generating function has leading singularity \((1/12)(1-z)^{-7}\), whereas the disconnected correction has leading singularity \((3/2)(1-z)^{-4}\). Standard polynomial coefficient formulas give the stated asymptotics.

## Verification

Two standalone Python 3 programs are provided. Run `python3 verify_words.py` to enumerate all ternary cyclic words for \(1\le n\le10\) and compare their distinct profiles with independently expanded case formulas. Run `python3 verify_matrices.py` to enumerate all nonnegative \(3\times3\) matrices of weight \(1\le n\le12\), filter by row-column balance, and test support connectivity by graph traversal; it independently checks the total balanced GF and the disconnected correction. Expected output is respectively `WORDS_VERIFY_OK n=1..10` and `MATRICES_VERIFY_OK n=1..12`. The infinite statements are established by the preceding exhaustive symbolic case classification, not by those bounded computations.

## Relationship to prior work

Jacquet, Knessl and Szpankowski developed the counting of Markov types and balanced frequency matrices and gave an asymptotic coefficient for the ternary case, alongside a general generating-function method for balanced matrices. Their conference manuscript was read for its setup, generating-function equations and asymptotic conclusions; it does not display the exact connectivity-corrected ternary rational GF above. Their expanded 2012 IEEE article has a closely related abstract but its full text was inaccessible in this review; this leaves an explicit historical-priority risk.

Kiah, Puleo and Milenkovic study length-two profile reconstruction and its coding application; they connect profile counts to de Bruijn graphs and give asymptotic polytope estimates. Their cited asymptotic constant is not claimed as new here. Related earlier records treat binary exact spectra or the number of ternary spectra admitting a **unique realizing necklace**; neither count is the total number \(P_n\) of attainable ternary cyclic profiles. Counting balanced matrices without support connectivity is not equivalent to the exact cyclic-word counting problem at finite lengths.

## Limitations

This result is specific to three labeled symbols, cyclic adjacency observations, and exact noise-free multisets of ordered length-two factors. It does not count reconstruction-list sizes, give an explicit optimal encoder, or classify all individual realizing words. General alphabet sizes and linear noncyclic read profiles require separate arguments. The main novelty claim concerns the full exact all-length generating function and finite disconnected correction; neither the leading growth constant nor Eulerian theory itself is new. Historical priority for the inaccessible expanded 2012 article and unindexed tables requires independent scrutiny.

## References

1. P. Jacquet, C. Knessl, W. Szpankowski, *Counting Markov Types*, DMTCS Proceedings AM (2010), DOI: 10.46298/dmtcs.2768. Public conference portal: https://dmtcs.episciences.org/en/articles/2768 (listing gives December 31, 2009 publication date).
2. P. Jacquet, C. Knessl, W. Szpankowski, *Counting Markov Types, Balanced Matrices, and Eulerian Graphs*, IEEE Transactions on Information Theory 58 (2012), 4261–4272, DOI: 10.1109/TIT.2012.2191476.
3. H. M. Kiah, G. J. Puleo, O. Milenkovic, *Codes for DNA Storage Channels*, arXiv:1410.8837, first submitted October 31, 2014; https://arxiv.org/abs/1410.8837.
