# Exact ternary two-gram profile counts and a six-period reconstruction law

## Finding
For each linear word \(x=x_1\cdots x_n\) on \(\{0,1,2\}\), let \(k_{ij}(x)\) be the number of indices \(1\le t<n\) with \(x_t=i\) and \(x_{t+1}=j\). A read-length-two multispectrum consists of the nine entries of the matrix \(k(x)\), including multiplicities. Write \(P_3(n,2)\) for the number of distinct matrices attained by words of length \(n\).

**Theorem.** For every integer \(n\ge2\), with \(m=n-1\),
\[
\sum_{m\ge1}P_3(m+1,2)z^m=
\frac{z(9-12z+5z^2+19z^3-4z^4-10z^5-14z^6+14z^7+6z^8-9z^9+3z^{10})}{(1-z)^7(1+z)^2(1+z+z^2)}.
\]
Its coefficients for \(n=2,\ldots,13\) are
\[
9,24,65,156,342,683,1272,2226,3708,5919,9120,13625.
\]
The coefficient sequence is an exact degree-six quasipolynomial of \(m=n-1\) with **least** period six, and
\[
P_3(n,2)=\frac7{8640}(n-1)^6+O(n^5).
\]
A ternary code is exactly distinguishable from these noiseless read-length-two multispectra if and only if it contains at most one word per attained matrix, so its maximum cardinality is exactly \(P_3(n,2)\).

## Assumptions and scope
The alphabet has three **labeled** symbols, and all \(n-1\) adjacent pairs in the **non-cyclic** word are recorded with multiplicities. The spectrum records ordered pairs \(ij\), rather than unordered pair compositions, mere supports, length-two subsequences or cyclic read counts. The code-size interpretation concerns exact noiseless distinguishability, with no error correction claim. The endpoint symbols are not separately observed. All dimensions and quantifiers are over integers \(n\ge2\).

For an integer \(3\times3\) matrix \(k=(k_{ij})\) with nonnegative entries and total \(m\), set \(d_i=\sum_j k_{ij}-\sum_j k_{ji}\). Call a vertex active if it touches a positive-multiplicity arc (including a loop). Connectivity always means weak connectivity of the underlying undirected graph on active vertices. The empty matrix is excluded from the length-positive enumeration.

## Proof
**1. Exact characterization of feasible profiles.** The sequence of adjacent pairs of any word is a directed trail which uses the arc \(i\to j\) with multiplicity \(k_{ij}\). Hence its directed graph is weakly connected on its active vertices, and the divergence vector \((d_0,d_1,d_2)\) is either \((0,0,0)\), or has one \(+1\), one \(-1\), and one zero. Conversely, the Euler-trail theorem for directed multigraphs shows that these two conditions are sufficient to order every arc into a single directed trail; listing the successive vertices recovers a word. This is the only realization criterion used below.

**2. Balanced matrices before connectivity correction.** Let \(z\) mark one adjacent-pair occurrence, and put
\[
L=\frac{z}{1-z},\qquad C_2=\frac{z^2}{(1-z)^2(1-z^2)}.
\]
Here \(L\) counts a single active vertex with one or more loops. The function \(C_2\) counts a balanced *connected* graph on a specified pair of vertices: its two opposite crossing-arc multiplicities are equal and positive, its two loop multiplicities are arbitrary. For a balanced \(3\times3\) matrix, three loop counts give \((1-z)^{-3}\). The opposing off-diagonal arcs on each of three vertex pairs have a common nonnegative part, contributing \((1-z^2)^{-3}\). The remaining net directed flow must circulate around one triangle. If this circulation equals an integer \(h\), its minimum contribution to the number of arcs is \(3|h|\). Thus the generating function of *all* balanced matrices, connected or not, including the zero matrix, is
\[
B=\frac{1}{(1-z)^3(1-z^2)^3}\sum_{h\in\mathbb Z}z^{3|h|}
=\frac{1+z^3}{(1-z)^3(1-z^2)^3(1-z^3)}.
\]
A nonzero disconnected balanced matrix on three labeled vertices has precisely one of three forms: two loop-only components (\(3L^2\)), three loop-only components (\(L^3\)), or a two-vertex connected balanced component and a disjoint loop-only vertex (\(3LC_2\)). Hence the connected nonzero balanced contribution is
\[
B_{\rm con}=B-1-3L^2-L^3-3LC_2.
\]
The singleton-loop matrices remain in this expression, correctly, because they are connected on their active support.

**3. Open trails and the disconnected obstruction.** Fix **ordered** distinct endpoints, say start vertex \(0\) and end vertex \(1\). The divergence conditions imply
\[
k_{01}-k_{10}=h+1,\quad k_{12}-k_{21}=h,\quad k_{20}-k_{02}=h
\]
for exactly one integer \(h\). For each pair, after its signed difference has been fixed, its two crossing-arc counts have one common nonnegative part. Thus the generating function of all matrices with these specified endpoint divergences is
\[
H=\frac{1}{(1-z)^3(1-z^2)^3}\sum_{h\in\mathbb Z}z^{|h+1|+2|h|}
=\frac{z+z^2}{(1-z)^3(1-z^2)^3(1-z^3)}.
\]
A graph with these divergences that is not weakly connected must have a component containing the endpoints and a separate loop-only component at the third vertex. Indeed, every component's divergences sum to zero, so the \(+1\) and \(-1\) vertices necessarily lie in the same component, and the remaining vertex has no crossing arcs. Such disconnected matrices contribute exactly
\[
J=\frac{z^2}{(1-z)^3(1-z^2)}:
\]
one mandatory \(0\to1\) arc, any number of opposing pairs of \(0\leftrightarrow1\) arcs, arbitrary loops at the two endpoints and a **positive** loop count at the third vertex. Therefore the connected contribution for this ordered endpoint pair is \(H-J\).

There are six ordered distinct endpoint pairs, related by relabeling the alphabet. Their divergence classes are disjoint from each other and from the balanced class. The desired generating function is consequently
\[
F=B-1-3L^2-L^3-3LC_2+6(H-J).
\]
Substituting the explicitly displayed rational functions and multiplying denominators gives the claimed single rational function. No matrix is double-counted because its divergence determines its endpoint class, and connectivity ensures each counted matrix is realizable.

**4. Coefficient structure.** Its denominator factors as \((1-z)^7(1+z)^2(1+z+z^2)\). The numerator is nonzero at \(z=-1\) and has nonzero remainder modulo \(1+z+z^2\), so both a nontrivial period-two term and a nontrivial period-three term are present in the exact coefficients. The pole at \(z=1\) has order seven and limit
\[
\lim_{z\to1}(1-z)^7F(z)=\frac7{12}.
\]
Partial fractions therefore give a degree-six quasipolynomial in \(m\) with period dividing six for every \(m\ge1\); poles at primitive second and third roots force the least period to be divisible by both two and three, hence exactly six. Finally, \([z^m](1-z)^{-7}\sim m^6/6!\), so the leading coefficient is \(\frac7{12\cdot6!}=\frac7{8640}\). The code-size assertion follows by choosing exactly one representative word for each realizable spectrum.

## Verification
Run `python3 verify.py` using the Python standard library. It reconstructs the rational generating functions \(B,H,J,L,C_2\) independently as integer-coefficient numerator/denominator pairs and checks the displayed algebraic identity by cross-multiplication. It expands the rational series into exact integer coefficients. Independently, for every \(1\le m\le9\), it enumerates **all** \(3^{m+1}\) ternary words and every nonnegative \(3\times3\) integer matrix with sum \(m\); it checks equality between direct observed spectrum sets and the graph-criterion feasible sets, and compares the cardinalities with the generating-function coefficients. Finally, it compares the first twelve coefficients from both rational expressions. These checks support but do not substitute for the all-length proof.

## Relationship to prior work
Jacquet, Knessl and Szpankowski (2010), *Counting Markov Types*, explicitly restrict to cyclic strings to impose balanced flows and give the all-matrix balanced generating function for the ternary case. Their rational function counts matrices without excluding disconnected ones and does not include the six open-trail endpoint classes; it is not the formula for linear realizable read-length-two profiles here. Indeed, the new leading coefficient is seven times the cyclic **unrestricted balanced-matrix** leading coefficient. This is a statement about counted objects, not a new computation of their known balanced rational function.

Kiah, Puleo and Milenkovic (2015) define the noiseless profile-code model and analyze profile enumeration via restricted de Bruijn graphs and Ehrhart theory, without specifying the linear ternary length-two all-length rational enumerator in the inspected results. Chang, Chrisnata, Ezerman and Kiah (2016) give exact general-alphabet counts in the short regime \(2\le n<4\) for two-gram reads, and general bounds; those initial cases agree with the formula but do not imply its subsequent coefficients. Gabrys and Milenkovic (2018/2019) study substring multispectrum reconstruction codes with different read-length regimes. The recent Eulerian-trail algorithm paper of Bals, Pissis and Tinca (first public version March 13, 2026) gives the graph-theoretic mechanism motivating the exact realization distinction, not a count of feasible nine-entry spectra.

The published binary two-multispectrum count and the published ternary **circular strict-ranking** realization invariant concern different alphabets or observation objects; neither implies the current ternary linear frequency-matrix count. An expanded 2012 Markov-types article was available only at abstract level in this review, leaving a residual risk of an unobserved exact enumerator; its abstract describes asymptotics. No claim of global historical priority is made.

## Limitations
Only the ternary alphabet, linear strings, and complete ordered adjacent-pair multiplicities are treated. This does not count singleton reconstruction classes, give an efficient optimal codebook encoder, handle losses or sequencing errors, determine longer-read profiles or generalize to four symbols. The exact enumerator is mathematical; finite verification is not an infinite proof. The 2012 extended Markov-types source could not be inspected in full, and unindexed prior formulas may exist. Independent validation has not been performed.

## References
1. B. Bals, S. P. Pissis and M. Tinca, *Optimal Enumeration of Eulerian Trails in Directed Graphs*, arXiv:2603.12894v1, first public March 13, 2026, https://arxiv.org/html/2603.12894v1.
2. P. Jacquet, C. Knessl and W. Szpankowski, *Counting Markov Types*, DMTCS Proceedings AM (2010), DOI:10.46298/dmtcs.2768; https://dmtcs.episciences.org/en/articles/2768/download.
3. P. Jacquet, C. Knessl and W. Szpankowski, *Counting Markov Types, Balanced Matrices, and Eulerian Graphs*, IEEE Transactions on Information Theory 58(7), 4261–4272 (2012), DOI:10.1109/TIT.2012.2191476 (full text not inspected).
4. H. M. Kiah, G. J. Puleo and O. Milenkovic, *Codes for DNA Sequence Profiles*, arXiv:1502.00517v1 (2015), https://arxiv.org/html/1502.00517v1.
5. M. Chang, G. Chrisnata, M. Ezerman and H. M. Kiah, *Rates of DNA Sequence Profiles for Practical Values of Read Lengths*, arXiv:1607.02279v1 (2016), https://arxiv.org/abs/1607.02279.
6. R. Gabrys and O. Milenkovic, *Unique Reconstruction of Coded Strings from Multiset Substring Spectra*, arXiv:1804.04548v1 (2018), https://arxiv.org/html/1804.04548v2.
