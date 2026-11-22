# Primitive fixed-density Boolean words: arithmetic facet deletion and a sphere-wedge law

## Finding

For integers \(n\ge 2\) and \(1\le k<n\), let \([n]=\{0,1,\ldots,n-1\}\), with indices taken modulo \(n\). Let \(\mathcal P_{n,k}\) consist of the \(k\)-subsets \(X\subseteq[n]\) whose cyclic indicator word has **no nonidentity rotational symmetry**. These are all *labeled rotations* of primitive binary necklaces of length \(n\) and weight \(k\), not just one canonical representative per necklace. Each concept answers membership queries at the individual indexed positions.

Set \(r=\min\{k,n-k\}\) and
\[
A(n,k)=\sum_{d\mid\gcd(n,k)}\mu(d)\binom{n/d}{k/d},
\]
where \(\mu\) is the number-theoretic Möbius function. For every support \(S\subseteq[n]\), **all** Boolean traces on \(S\) occur in \(\mathcal P_{n,k}\) if and only if
\[
|S|<r\quad\text{or}\quad \bigl(|S|=r\text{ and }S\text{ is cyclically aperiodic}\bigr).
\]
For \(|S|>r\) the support is not shattered. Consequently the complete shattered-support polynomial and the VC dimension are
\[
\Phi_{n,k}(z)=\sum_{j=0}^{r-1}\binom{n}{j}z^j+A(n,k)z^r,
\qquad \operatorname{VCdim}(\mathcal P_{n,k})=r.
\]
The simplicial complex \(\Delta_{n,k}\) of shattered supports is pure of dimension \(r-1\), and has ordinary homotopy type
\[
\boxed{\Delta_{n,k}\simeq\bigvee^{\,A(n,k)-\binom{n-1}{r-1}} S^{r-1}.}
\]
When \(r=1\), the formula denotes a discrete complex of \(n\) vertices, or a wedge of \(n-1\) zero-spheres. No equivariant homotopy classification is asserted.

For example, at \((n,k)=(8,4)\), the six periodic four-subsets are exactly the six missing maximal faces; all lower-dimensional faces remain. The complex has \(64\) tetrahedral faces and is homotopy equivalent to a wedge of \(29\) three-spheres. At \((n,k)=(6,3)\) there are \(18\) top faces and \(8\) two-spheres.

## Assumptions and scope

A cyclic indicator word is periodic if it is a repetition of a shorter binary block, equivalently if it is fixed by a nonzero rotation modulo \(n\). Shattering is by *individually indexed position-membership queries*, not by rotation-invariant queries on necklace equivalence classes. A subset \(S\) is shattered when, for every \(T\subseteq S\), there is a primitive \(k\)-subset \(X\) with \(X\cap S=T\). The empty trace is included. All binomial coefficients are ordinary integer coefficients and \(S^0\) denotes the two-point zero-sphere.

The statement applies to the entire integer domain \(n\ge2\), \(1\le k<n\), including both unbalanced weights and \(n=2k\); there are no asymptotic or genericity hypotheses.

## Proof

**1. A spectral separation lemma for periodic sets.** Put \(\zeta=\exp(2\pi i/n)\) and \(M(X)=\sum_{a\in X}\zeta^a\). If a subset \(X\) is fixed by a nonidentity rotation, let \(H\) be its nontrivial rotational stabilizer in the cyclic group. Then \(X\) is a union of cosets of \(H\). For any such coset \(a+H\), the sum of the corresponding roots of unity vanishes, since \(H\) is a nontrivial subgroup of the cyclic group. Thus every periodic \(X\) has \(M(X)=0\). If \(Y=(X\setminus\{a\})\cup\{b\}\), where \(a\in X\), \(b\notin X\), then \(M(Y)-M(X)=\zeta^b-\zeta^a\ne0\). **Hence two distinct periodic \(k\)-subsets cannot be adjacent in the Johnson graph**, i.e. they cannot differ by one deletion and one addition. This conclusion is independent of the value of \(k\).

**2. Fibers with at least two possible free-coordinate weights.** Fix a support \(S\) of size \(s\), and a prescribed positive trace \(T\subseteq S\) of size \(t\). The unrestricted \(k\)-subsets inducing this trace have the form \(T\cup U\), where \(U\subseteq[n]\setminus S\) and \(|U|=k-t\). Whenever
\[
1\le k-t\le n-s-1,
\]
this fiber contains two neighboring \(k\)-subsets, obtained by swapping one selected and one unselected free position. By Step 1 these cannot both be periodic. Thus the trace is realized by a primitive word.

**3. Sharp support criterion.** Let \(r=\min(k,n-k)\). If \(s<r\), then for every \(0\le t\le s\) one has \(1\le k-t\le n-s-1\), so Step 2 realizes every trace. If \(s=r\) and \(k<n/2\), the positive trace \(T=S\) has the unique unrestricted extension \(X=S\). All other traces have fibers satisfying Step 2. Hence \(S\) is shattered precisely when \(S\) is aperiodic. If \(k>n/2\), the empty trace has unique unrestricted extension \(X=[n]\setminus S\), and all remaining fibers satisfy Step 2. Complementation preserves rotational stabilizers, so again the criterion is precisely the aperiodicity of \(S\). If \(n=2k\), both the positive and empty traces have unique extensions \(S\) and its complement; they are simultaneously primitive or periodic, and all intermediate fibers satisfy Step 2. This proves the same criterion. Finally, no support of size larger than \(r\) is shattered even by all \(k\)-subsets: either the all-positive or all-negative trace would require more than the available number of selected or unselected positions.

**4. Enumerating top supports and computing dimension.** The classical fixed-density necklace count gives \(A(n,k)=nL(n,k)\), where \(L(n,k)\) is the number of primitive necklace orbits, and Möbius inversion yields the displayed divisor sum. Complementing each labeled word gives \(A(n,k)=A(n,n-k)=A(n,r)\). Every contiguous cyclic block of \(k\) consecutive positions is primitive (its cyclic indicator has exactly two transitions, impossible for a nontrivial repeated block). Therefore at least one top support exists and the VC dimension is \(r\). Counting the full lower skeleton and the primitive rank-\(r\) faces establishes the polynomial.

**5. Purity and homotopy.** Regard \(\Delta_{n,k}\) as the full \((r-2)\)-skeleton of a simplex on \(n\) vertices, together with all but the periodic \(r\)-element faces. By Step 1 the omitted \(r\)-faces have no common codimension-one face. Every \((r-1)\)-element subset has \(n-r+1\ge2\) possible rank-\(r\) extensions, at most one of which is periodic, proving purity for \(r\ge2\); \(r=1\) is immediate.

For \(r\ge2\), let \(K=\Delta_{n,k}\) and let \(L\) denote the full \((r-1)\)-skeleton of the \((n-1)\)-simplex. If \(F\) is any deleted periodic rank-\(r\) face, choose \(v\notin F\). The \(r\) other rank-\(r\) faces of the boundary of the abstract \(r\)-simplex on \(F\cup\{v\}\) are all present in \(K\), since each differs from \(F\) by one swap. Their union is a closed \((r-1)\)-ball spanning \(\partial F\) within \(K\). Thus the attaching map of each omitted \((r-1)\)-simplex is nullhomotopic already in \(K\). For \(r=2\), \(K\) is a connected graph (the complete graph minus a matching), and adding any missing edge creates a wedge-circle. For \(r\ge3\), adjoining all omitted top cells similarly gives
\[
L\simeq K\vee\bigvee^{P(n,r)}S^{r-1},
\quad P(n,r)=\binom nr-A(n,r).
\]
The full simplex skeleton \(L\) is \((r-2)\)-connected and is a wedge of exactly \(\binom{n-1}{r}\) spheres of dimension \(r-1\). Since the cells are attached trivially, \(K\) is also \((r-2)\)-connected. A finite \((r-1)\)-dimensional, \((r-2)\)-connected CW complex is a wedge of top-dimensional spheres (with the connected graph case treated separately). Its reduced top homology rank is obtained by subtracting the number of null-attached cells:
\[
\binom{n-1}{r}-P(n,r)=A(n,r)-\binom{n-1}{r-1}.
\]
For \(r=1\), \(K\) is \(n\) isolated vertices and the same rank formula is \(n-1\). This completes all claims.

## Verification

The attached `checker.py` uses separate exhaustive enumeration of primitive words, trace tests for every support and every \((n,k)\) with \(2\le n\le12\), an independent implementation of the Möbius count, and Gaussian elimination over \(\mathbb F_2\) on the top boundary matrices for every \(2\le n\le10\). It passed \(81{,}924\) support decisions, \(680\) tests of periodic Johnson adjacency pairs, and \(45\) boundary-rank computations. Finite checking corroborates but does not certify the all-parameter theorem, which rests on the root-of-unity, trace-fiber, and simplex-attachment arguments above. Run from the directory containing the file with `python checker.py` using Python 3.9 or later; no nonstandard dependencies are needed.

## Relationship to prior work

Heckenberger and Sawada (2018) study fixed-density necklace/Lyndon counts and a Pascal-like inequality; Hartman and Sawada (2019) establish ranking/unranking and prefix-counting algorithms for fixed-density necklaces and Lyndon words; Adamson, Deligkas, Gusev and Potapov (2021) treat multidimensional necklaces with fixed-content enumeration and algorithms. The count \(A(n,k)\), the definition of primitive cyclic words, and all standard properties of complete simplex skeleta are prior mathematics. None of the inspected statements gives the exact indexed-coordinate shattering criterion or the topology of its shattered-support complex. An algorithm for counting prefixes does not itself imply the all-support closed classification, although it can assist finite testing. Related public findings on Fourier spectra of primitive binary words concern different transforms (Walsh rather than the first complex cyclic moment used as an obstruction here) and do not state this trace/topology theorem in the retrieved summaries.

## Limitations

The theorem is for the class of **all labeled primitive binary words of one fixed weight**. It is not a result about one necklace representative per orbit, mixed weights, aperiodicity for more general group actions, or robustness under noise. The homotopy type is ordinary nonequivariant homotopy; the rotational representation on homology is not determined. The Möbius enumerator and the complete skeleton homotopy theorem are classical ingredients, not separate new discoveries. The priority comparison uses accessible primary texts, public record summaries and bounded historical search; equivalent unindexed results or inaccessible full texts remain possible. No independent review has been performed.

## References

1. I. Heckenberger and J. Sawada, *A Pascal-like Bound for the Number of Necklaces with Fixed Density*, first posted January 29, 2018, arXiv:1801.09516, https://arxiv.org/abs/1801.09516.
2. P. Hartman and J. Sawada, *Ranking and Unranking Fixed-Density Necklaces and Lyndon Words*, Theoretical Computer Science 791 (2019), 36–47, DOI:10.1016/j.tcs.2019.04.007, lawful author manuscript https://www.socs.uoguelph.ca/~sawada/papers/fixDenRank.pdf.
3. D. Adamson, A. Deligkas, V. V. Gusev and I. Potapov, *Combinatorial Algorithms for Multidimensional Necklaces*, first posted August 4, 2021, arXiv:2108.01990, https://arxiv.org/abs/2108.01990.
