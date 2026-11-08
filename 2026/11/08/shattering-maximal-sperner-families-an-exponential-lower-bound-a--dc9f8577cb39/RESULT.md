# Shattering maximal Sperner families: an exponential lower bound and the exact five-atom profile

## Finding

For every integer \(n\ge1\), let \(B_n=2^{[n]}\) be the inclusion-ordered Boolean lattice, and let \(\mathcal M_n\) be the Boolean concept class of all inclusion-maximal antichains of \(B_n\). The instance domain is \(B_n\); a hypothesis \(A\in\mathcal M_n\) gives label \(1\) on \(x\in B_n\) exactly when \(x\in A\).

For all \(n\ge1\),
\[
\binom{n-1}{\lfloor(n-1)/2\rfloor}\le \operatorname{VCdim}(\mathcal M_n)\le\binom n{\lfloor n/2\rfloor}.
\]
In particular, \(\operatorname{VCdim}(\mathcal M_n)=\Theta(2^n/\sqrt n)\) as \(n\to\infty\).

For \(n=1,2,3,4,5\), the *exact* VC dimensions are respectively \(1,1,2,3,6\). At five atoms the complete shattered-support polynomial is
\[
\Phi_5(z)=1+32z+285z^2+1090z^3+1780z^4+1224z^5+310z^6,
\]
where \(\Phi_n(z)=\sum_{S\subseteq B_n:\,S\text{ shattered}}z^{|S|}\). The \(310\) shattered six-point supports form exactly \(11\) orbits under permutations of the five atoms, with orbit sizes
\[
5,5,10,15,15,20,30,30,60,60,60.
\]
Their canonical representatives and multiplicities appear in `ORBIT_CLASSES.json` with an explicit bitmask convention. Five atoms is the first ground-set size for which this VC dimension exceeds the number of atoms.

## Assumptions and scope

An antichain of a finite poset is a subset of pairwise incomparable points. It is *inclusion-maximal* if it cannot be enlarged while remaining an antichain; no equal-cardinality assumption is imposed. A support \(S\subseteq B_n\) is *shattered* when, for each \(T\subseteq S\), there exists an inclusion-maximal antichain \(A\subseteq B_n\) satisfying \(A\cap S=T\). The empty support is counted as shattered. These are ordinary VC dimensions, not Littlestone dimensions, and they are distinct from the maximum size of a single antichain (Sperner width).

The unrestricted claims cover all integer \(n\ge1\). The exact enumerations and orbit classification apply only through \(n=5\). No exact formula for \(n\ge6\) is asserted.

## Proof

**General lower bound.** Fix an atom \(a\in[n]\) and a rank \(r\in\{1,\ldots,n\}\). Take the support
\[
S_{n,r,a}=\{x\subseteq[n]:|x|=r,\ a\in x\}.
\]
It has \(\binom{n-1}{r-1}\) elements. For each prescribed positive sub-support \(T\subseteq S_{n,r,a}\), form
\[
D_T=T\cup\{x\setminus\{a\}:x\in S_{n,r,a}\setminus T\}.
\]
All members of \(T\) have size \(r\) and contain \(a\); all remaining members of \(D_T\) have size \(r-1\) and avoid \(a\). Such a lower member \(x\setminus\{a\}\) can be contained in an upper member \(t\in T\) only if \(t=x\), which is excluded by construction. Consequently \(D_T\) is an antichain. Extend it to an inclusion-maximal antichain \(A_T\) of the finite lattice. The omitted points \(x\in S_{n,r,a}\setminus T\) are each comparable to their own blocker \(x\setminus\{a\}\in D_T\), and therefore cannot enter \(A_T\). Every point of \(T\) remains. Thus \(A_T\cap S_{n,r,a}=T\), proving that \(S_{n,r,a}\) is shattered. Maximizing over \(r\) gives the displayed lower bound.

**General upper bound.** If \(S\) is shattered then its all-positive labeling is realized by some antichain \(A\), so \(S\subseteq A\) is itself an antichain of \(B_n\). Sperner's theorem gives \(|S|\le\binom n{\lfloor n/2\rfloor}\). The two central binomial coefficients have order \(2^n/\sqrt n\), yielding the asymptotic conclusion.

**Complete finite determination.** Build the incomparability graph of \(B_n\), whose vertices are the \(2^n\) subsets of \([n]\), with an edge joining two distinct incomparable subsets. The inclusion-maximal antichains are precisely the maximal cliques in this graph. The accompanying standalone checker uses a pivoted Bron–Kerbosch recursion to enumerate all maximal cliques; it additionally checks their antichain and maximality properties directly.

For each candidate support \(S\), partition the set of maximal antichains by their binary membership pattern on \(S\). An extension to \(S\cup\{x\}\) is shattered **if and only if** each existing pattern class contains both a hypothesis including \(x\) and a hypothesis excluding \(x\). This is tested as a pair of nonempty bit intersections for every class. Since every shattered support is an antichain, the enumeration may exclude comparable new points. Supports are added in increasing numerical order, so each candidate is generated once. Induction on support cardinality proves that this recursion enumerates *all* shattered supports, not merely witnesses.

The exact number of inclusion-maximal antichains for \(n=1,2,3,4,5\) is respectively \(2,3,7,29,376\). The complete shattered-support counts by increasing support cardinality are

| Number of atoms | Counts by support size, starting at zero | VC dimension |
| --- | --- | --- |
| 1 | 1, 2 | 1 |
| 2 | 1, 4 | 1 |
| 3 | 1, 8, 9 | 2 |
| 4 | 1, 16, 55, 52 | 3 |
| 5 | 1, 32, 285, 1090, 1780, 1224, 310 | 6 |

The program explicitly tests the next support size and finds none in each case. In particular no seven-point support is shattered in \(B_5\); by downward heredity, no larger one is shattered. The general lower-bound construction already supplies six-point supports in \(B_5\), establishing equality. All \(120\) atom permutations are applied to each six-point support to obtain its lexicographically least image and thus its exact orbit, yielding the \(11\) classes reported above.

## Verification

Run `python3 verify.py` from the directory containing the bundled files. The implementation requires only the Python standard library, independently enumerates maximal antichains without importing graph libraries, verifies the complete support-count vectors, computes all atom-permutation orbits, and checks `ORBIT_CLASSES.json`. Its terminating line is `BOOLEAN_MAXIMAL_ANTICHAIN_SHATTERING_PASS`.

The finite statements are exhaustive because the algorithm visits every maximal clique and every eligible increasing support extension; the recursive split criterion is equivalent to shattering. The general bounds are mathematical proofs, not extrapolations from the finite data.

## Relationship to prior work

The February 14, 2023 preprint by Griggs, Kalinowski, Leck, Roberts and Schmitz determines possible *sizes* of inclusion-maximal antichains and develops flat two-level constructions, but does not give the VC dimension of the family of all maximal antichains as binary hypotheses. Ignatov's 2023 paper and OEIS A326358 enumerate maximal antichains themselves, not supports shattered *by the entire family*. In particular, the known total \(376\) does not imply the new six-point support count \(310\), its eleven symmetry orbits, or the exponential dimension lower bound without additional argument or computation.

Duffus, Sands and Winkler (1990) prove existence and avoidance properties for maximal chains and antichains; their results do not supply the quantified membership patterns here. Balogh, Mészáros and Wagner (2017) investigate induced matchings between adjacent hypercube layers and families having bounded VC dimension; their hypothesis families and shattering domain differ from this maximal-antichain membership family. The universal lower-bound construction is related to an induced matching between consecutive Boolean ranks, but the exact five-atom shattered-support polynomial and its orbit classification are not given by the inspected statements.

## Limitations

The upper and lower bounds are not generally equal; the exact VC dimension for \(n\ge6\) and a general description of all shattered supports remain open here. Published source search and accessible full-text comparison do not prove global historical uniqueness. Full text of Ignatov's 2023 article was not accessible in the reviewed channels; its public abstract, metadata and linked enumeration records were examined, but a hidden shattering result in its unavailable body cannot be excluded. The calculations are finite and do not constitute any external certification or independent mathematical audit.

## References

1. J. R. Griggs, T. Kalinowski, U. Leck, I. T. Roberts and M. Schmitz, *Sizes of flat maximal antichains of subsets*, first posted 2023-02-14, arXiv:2302.07062, https://arxiv.org/abs/2302.07062.
2. D. I. Ignatov, *On the Number of Maximal Antichains in Boolean Lattices for n up to 7*, Lobachevskii Journal of Mathematics 44 (2023), 137–146, DOI 10.1134/S1995080223010158, https://link.springer.com/article/10.1134/S1995080223010158.
3. OEIS A326358, *Number of maximal antichains of subsets of a finite set*, https://oeis.org/A326358.
4. D. Duffus, B. Sands and P. Winkler, *Maximal Chains and Antichains in Boolean Lattices*, SIAM Journal on Discrete Mathematics 3 (1990), 197–205, https://www.math.emory.edu/~dwight/papers/1-DSW-Boolean.pdf.
5. J. Balogh, T. Mészáros and A. Z. Wagner, *Two results about the hypercube*, first posted 2017-10-23, arXiv:1710.08509, https://arxiv.org/html/1710.08509v1.
