# Parity-sensitive enumeration of minimum facet transversals of even-dimensional cyclic polytopes

## Finding
Let \(k\ge1\) and \(n\ge2k+1\) be integers. Let \(C(n,2k)\) be the cyclic polytope whose \(n\) moment-curve vertices are labeled in increasing order. A *facet transversal* is a subset of vertex labels meeting every facet. Put \(h=\lfloor n/2\rfloor\), \(r=k-1\), and \(\tau=\lceil n/2\rceil-k+1\).

**Theorem.** A set \(T\subseteq[n]\) is a minimum facet transversal if and only if its complement is of the form \(I\cup R\), where \(I\) is a maximum independent set of the cycle on \([n]\) (with the cyclic edge \(\{n,1\}\)), \(R\subseteq[n]\setminus I\), and \(|R|=r\). All these transversals have size \(\tau\), and their number is
\[
 M_{n,k}=\begin{cases}
 2\binom{h}{r},& n=2h,\\
 n\binom{h}{r},& n=2h+1.
 \end{cases}
\]

For fixed \(k\), the two parity subsequences have distinct polynomial growth orders:
\[
 M_{n,k}\sim\begin{cases}
 \dfrac{n^{k-1}}{2^{k-2}(k-1)!},&n\text{ even},\\
 \dfrac{n^k}{2^{k-1}(k-1)!},&n\text{ odd}.
 \end{cases}
\]
The already-known value of \(\tau\) is included only to identify the minimum sets; the contribution is their complete description and exact count, including the parity jump.

## Assumptions and scope
All parameters are integers with \(k\ge1\) and \(n\ge2k+1\). Cyclic polytopes are defined by any distinct real moment-curve parameters \(t_1<\cdots<t_n\); the result is combinatorial and independent of their values. A transversal must intersect each *facet vertex set* (not all faces), and all subsets are counted with the original vertex labels, not modulo dihedral symmetry. The case \(k=1\) reduces to vertex covers of a cycle. The boundary \(n=2k+1\) includes the simplex case.

## Proof
**Facet-to-matching equivalence.** Gale's evenness criterion says that the facets of \(C(n,2k)\) are exactly the \(2k\)-sets that are unions of \(k\) pairwise vertex-disjoint edges of the cycle \(C_n\) (with the wraparound edge). Consequently \(T\) hits every facet if and only if the induced graph on \(Y=[n]\setminus T\) contains no matching of size \(k\). This equivalence also holds at \(n=2k+1\).

**Maximum complement and rigidity.** Write \(\nu(Y)\) for the matching number of the induced cycle graph on \(Y\). If \(T\) is a transversal then \(\nu(Y)\le r\). Since \(r<\lfloor n/2\rfloor\), \(Y\ne[n]\), so its induced graph is a disjoint union of paths. Each path has an independent set with size equal to its number of vertices minus its matching number; hence there exists \(I\subseteq Y\) independent in the full cycle with \(|I|=|Y|-\nu(Y)\). The independence number of \(C_n\) is \(h\), so
\[
 |Y|\le h+\nu(Y)\le h+r.
\]
Conversely, any maximum independent set \(I\) of \(C_n\) together with any \(r\)-subset \(R\) of its complement forms \(Y=I\cup R\) with \(\nu(Y)\le r\), because every edge of the induced graph touches \(R\). Thus \(|Y|=h+r\) is achievable. If equality holds, the preceding independent-set argument forces \(|I|=h\) and \(|R|=r\). This proves both the classification and \(|T|=n-h-r=\tau\).

**Even \(n=2h\).** The only maximum independent sets of \(C_{2h}\) are the two alternating sets. Each permits \(\binom h r\) choices for \(R\). No \(Y\) of size \(h+r<2h\) contains both alternating sets, so the two collections are disjoint. The count is \(2\binom h r\).

**Odd \(n=2h+1\).** Every optimal complement \(Y\) has \(m=h+r\) vertices, \(z=h+1-r\) missing vertices, and independence number exactly \(h\). As \(Y\ne[n]\), write its cyclic indicator word as alternating nonempty runs of ones and zeros. If the one-runs have lengths \(\ell_1,\ldots,\ell_t\), then the independent-set size of the induced union of paths is \(\sum_j\lceil\ell_j/2\rceil\). Hence exactly
\[
 u=2h-m=h-r
\]
of the one-runs have odd length. Since \(u\le t\le z=u+1\), there are exactly two mutually exclusive cases.

If \(t=u\), every one-run is odd, say \(\ell_j=1+2a_j\), with \(\sum a_j=r\). The zero-gaps have lengths one except for exactly one gap of length two. Root at the first one after that unique double-zero gap: there are \(n\) choices for its labeled position and \(\binom{r+u-1}{u-1}=\binom{h-1}{r}\) ordered weak compositions of \(r\). This yields \(n\binom{h-1}{r}\) distinct words.

If \(t=u+1\), all zero-gaps have length one, exactly one one-run has even length \(2+2a\), and all other one-runs have odd lengths \(1+2a_j\), with the total of the \(a_j\) equal to \(r-1\). Root at the first one in the unique even run: there are \(n\) labeled positions and \(\binom{(r-1)+t-1}{t-1}=\binom{h-1}{r-1}\) weak compositions. When \(r=0\) this case is empty, using \(\binom{h-1}{-1}=0\). The combined number is
\[
 n\left(\binom{h-1}{r}+\binom{h-1}{r-1}\right)=n\binom h r.
\]
This finishes the exact enumeration. For fixed \(r\), the displayed asymptotics follow from \(\binom{h}{r}\sim h^r/r!\).

## Verification
The standalone Python 3 checker \(\texttt{verify.py}\) independently derives facets by the *literal* Gale evenness test on all candidate \(2k\)-subsets, enumerates every putative transversal by bit mask, and compares minimum size, count, and complete optimizer set with the formulas and the independent-set classification. It passes \(34\) parameter instances with \(3\le n\le13\), comprising \(1232\) directly generated facet sets; the \(n=13\) instances stop at \(k=4\). These finite checks test, but cannot replace, the all-parameter proof above.

## Relationship to prior work
Briggs--Dobbins--Lee (2021/2023), Proposition 3.6, already determines the exact *size* \(\tau(C(n,2k))\) of a minimum transversal; that theorem is not asserted as new. Dobbins--Lee (2026) studies transversal *ratios* and weak chromatic numbers and supplies the recent motivation for understanding their extremizers. Novik--Zheng (2024/2025) studies transversal bounds and cyclic-polytope-derived families. None of the inspected pertinent statements counts or classifies all minimum transversals as in the present theorem. The parity-dependent count is not implied merely by the known extremal size; it requires analyzing all equality cases.

## Limitations
The theorem concerns even-dimensional cyclic polytopes, not arbitrary neighborly polytopes, odd-dimensional cyclic polytopes, or arbitrary hypergraph hitting sets. It does not classify transversals larger than minimum or count optimizers modulo symmetries. Historical priority is provisional: a combinatorially equivalent enumeration could occur in literature outside the inspected searches. The finite checker is not an infinite proof; the main argument is elementary and self-contained conditional on Gale's classical facet criterion. No independent audit has been performed.

## References
- M. G. Dobbins and S. Lee, *Polytopes with large transversal ratio*, arXiv:2603.16298, first public 2026-03-17, https://arxiv.org/abs/2603.16298.
- J. Briggs, M. G. Dobbins and S. Lee, *Transversals and colorings of simplicial spheres*, arXiv:2111.06560, especially Proposition 3.6 and its proof, https://arxiv.org/abs/2111.06560.
- I. Novik and H. Zheng, *Transversal numbers of simplicial polytopes, spheres, and pure complexes*, arXiv:2407.19693, especially §2.2 and §4, https://arxiv.org/abs/2407.19693.
- D. Gale's evenness criterion, as stated in the preceding two mathematical references.
