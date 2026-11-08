# Exact enumeration of cyclic binary trigram profiles

## Finding

For each integer \(n\geq1\), take all binary circular words of length \(n\), where cyclic rotation is identified but reversal and complementation are not. The *trigram profile* of a circular word is the eight-dimensional vector of counts of the consecutive circular triples \(000,001,010,011,100,101,110,111\), including triples crossing the chosen linearization boundary. Let \(S(n)\) be the number of *distinct profiles* realizable by at least one such word, **not** the number of words realizing a profile.

Put \(U_t(z)=z+z^2+\cdots+z^t\). Then the exact generating function, valid as a formal power series, is

\[
\sum_{n\geq1} S(n)z^n
=\frac{2z}{1-z}+\frac{z^2}{1-z^2}
+\sum_{t\geq1}z^{2t}\left(\frac{2U_t(z)}{1-z}+\frac{U_t(z)^2}{(1-z)^2}\right).
\]

Equivalently, the generating function is the following **rational function**:

\[
\boxed{\begin{aligned}
\sum_{n\geq1} S(n)z^n
={}&\frac{2z}{1-z}+\frac{z^2}{1-z^2}\\
&+\frac{2z}{(1-z)^2}\left(\frac{z^2}{1-z^2}-\frac{z^3}{1-z^3}\right)\\
&+\frac{z^2}{(1-z)^4}\left(\frac{z^2}{1-z^2}-\frac{2z^3}{1-z^3}+\frac{z^4}{1-z^4}\right).
\end{aligned}}
\]

Thus \(S(n)=n^4/288+O(n^3)\), and its first values (for lengths \(1\) through \(13\)) are \(2,3,4,6,8,13,18,27,38,53,72,98,128\). In the exact-read-multiset model, \(S(n)\) is also the maximum size of a collection of binary circular words of length \(n\) in which no two words have equal circular trigram multisets.

## Assumptions and scope

A length-\(n\) circular word is a cyclic equivalence class of \(w_0w_1\cdots w_{n-1}\in\{0,1\}^n\). Circular triples start at all \(n\) positions, with indices modulo \(n\), even when \(n=1\) or \(n=2\). Profiles distinguish the eight labeled triples. Equality of spectra does not require equality of circular words. The theorem counts all positive lengths and includes profiles containing zero entries.

## Proof

**Step 1: Characterize possible profiles by flows.** Let the profile coordinates, in the specified order, be \((A,B,C,D,E,F,G,H)\). Construct the directed binary de Bruijn graph with vertices \(00,01,10,11\); a triple \(ijk\) is an edge from \(ij\) to \(jk\). Reading a circular word gives an Eulerian closed walk using each edge with the indicated multiplicity. Thus the weighted graph must have equal indegree and outdegree at every vertex, and the support of its positive edges must be a single connected Eulerian component. Conversely, any nonempty balanced directed multigraph with one connected edge-bearing component has an Eulerian circuit; spelling its edge triples produces a circular word realizing the profile, including loops and repeated edges.

The balances at \(00\) and \(11\) force \(B=E=x\) and \(D=G=y\), for nonnegative integers \(x,y\). Balance at \(01\) is \(C+y=x+F\). Write \(t=x+F=y+C\), so \(F=t-x\), \(C=t-y\), and \(0\leq x,y\leq t\). The total word length is

\[
n=A+H+x+y+2t.
\]

**Step 2: Enforce one Eulerian component rather than merely balance.** If \(x>0\) and \(y>0\), the edges \(001,011,110,100\) join all four vertices in a directed cycle; both loop multiplicities \(A,H\geq0\) are unrestricted. If \(x>0,y=0\), the positive edges \(001,010,100\) join \(00,01,10\) and the isolated \(11\) loop must be absent: \(H=0\); \(A\geq0\) is free. The case \(x=0,y>0\) is symmetric, with \(A=0\) and \(H\geq0\). If \(x=y=0\), then \(C=F=t\). Connectivity permits only an all-zero loop, an all-one loop, or the pure alternating two-edge circuit (the last requires \(t\geq1\)); mixing these components is not realizable by one circular word. This exhausts all cases.

**Step 3: Enumerate without counting words or embeddings.** For fixed \(t\geq1\), choose \(x\) and \(y\) among \(1,\ldots,t\) for the four-vertex case. Their contributions to length are \(2t+x+y\), while the two independent nonnegative loop weights contribute \((1-z)^{-2}\). The generating contribution is \(z^{2t}U_t(z)^2/(1-z)^2\). If exactly one of \(x,y\) is positive, there are two choices of side, a single free loop weight, and the contribution is \(2z^{2t}U_t(z)/(1-z)\). The pure alternating spectra contribute \(z^2/(1-z^2)\), and the two unary spectra contribute \(2z/(1-z)\). Each valid parameter tuple specifies exactly one ordered eight-vector, so no two tuples are counted as different profiles of the same vector. Summing gives the stated series.

Since \(U_t(z)=z(1-z^t)/(1-z)\), the two geometric summations are

\[
\sum_{t\geq1}z^{2t}U_t(z)=\frac{z}{1-z}\left(\frac{z^2}{1-z^2}-\frac{z^3}{1-z^3}\right),
\]
\[
\sum_{t\geq1}z^{2t}U_t(z)^2=\frac{z^2}{(1-z)^2}\left(\frac{z^2}{1-z^2}-\frac{2z^3}{1-z^3}+\frac{z^4}{1-z^4}\right).
\]

Substitution proves the rational formula. Its only pole of order five is at \(z=1\), with \(\lim_{z\to1}(1-z)^5\sum_{n\geq1}S(n)z^n=1/12\). Other roots of unity yield lower-order poles, hence \(S(n)=n^4/288+O(n^3)\). Finally, selecting one representative from each profile attains the claimed optimum reconstruction-code size, and two representatives of one profile cannot coexist in such a code.

## Verification

The standalone Python 3 standard-library program `verify.py` independently enumerates all \(2^n\) binary linear words and their cyclic triple-count vectors for every \(1\leq n\leq17\), then compares the resulting **sets** of vectors with an independent enumeration of the balanced-connected-flow parametrization and the coefficient formula. This covers \(262142\) input words in total and \(1460\) distinct vectors (summed across those lengths). For all lengths through \(80\), it also compares the parameter enumeration with coefficients obtained by an independent nested-sum formula. Run `python3 verify.py` in the same directory; it should print `PASS`. The finite checks supplement but do not substitute for the all-length proof.

The first noninjectivity at length \(6\) is illustrated by the nonconjugate circular words `001011` and `001101`, each with profile \((0,1,1,1,1,1,1,0)\). The counts \(S(1),\ldots,S(5)=(2,3,4,6,8)\) equal the numbers of binary necklaces at those lengths; at length \(6\), there are \(14\) necklaces but only \(13\) profiles.

## Relationship to prior work

The graph-theoretic correspondence between substring multisets and Eulerian walks is classical. Tesler's *Multi de Bruijn Sequences* (2017, Sections 2 and 9) counts cyclic sequences when every \(k\)-mer has a common prescribed multiplicity and counts multicyclic decompositions for a fixed arbitrary edge-multiplicity vector. Those results do not enumerate **which unequal multiplicity vectors can occur as a single cyclic string**, or their distinct counts over every length. Bernardini et al. (CPM 2022) study shortest words preserving **sets** of \(k\)-mers and state the distinction from multiset information; their results do not supply this all-profile enumeration. The present proof supplies the missing binary/trigram connectivity exclusion and its complete rational enumerator, not a new Euler-circuit theorem.

## Limitations

The theorem is limited to the binary alphabet, circular contiguous trigrams, and exact counts with multiplicity. It does not count how many different necklaces share each profile; no profile-specific reconstruction multiplicity is asserted. Earlier unindexed equivalent enumerations remain possible. Independent scientific validation has not been performed.

## References

- Glenn Tesler, *Multi de Bruijn Sequences*, arXiv:1708.03654, first posted 2017-08-11, https://arxiv.org/abs/1708.03654 . See especially Sections 2 and 9.
- Giulia Bernardini, Alessio Conte, Esteban Gabory, Roberto Grossi, Grigorios Loukides, Solon P. Pissis, Giulia Punzi and Michelle Sweering, *On Strings Having the Same Length-\(k\) Substrings*, CPM 2022, https://doi.org/10.4230/LIPIcs.CPM.2022.16 .
- Aranka Steyaert, Pieter Audenaert and Jan Fostier, *Accurate determination of node and arc multiplicities in de Bruijn graphs using conditional random fields*, BMC Bioinformatics 21:402 (2020), https://doi.org/10.1186/s12859-020-03740-x . Context for weighted de Bruijn graph observations, not an enumeration source.
