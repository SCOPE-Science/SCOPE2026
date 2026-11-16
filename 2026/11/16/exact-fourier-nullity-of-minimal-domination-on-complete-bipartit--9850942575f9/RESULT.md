# Exact Fourier nullity of minimal domination on complete bipartite graphs

## Finding

Let \(m,n\ge 2\) be integers, and let \(D_{m,n}\subseteq\mathbb F_2^{m+n}\) consist of incidence vectors of inclusion-minimal dominating vertex sets of the graph \(K_{m,n}\). Define the unnormalized Walsh transform
\[
W_{m,n}(u,v)=\sum_{x\in D_{m,n}}(-1)^{\langle (u,v),x\rangle}.
\]
If \(i=|u|\) and \(j=|v|\), then **every** Fourier coefficient equals
\[
\boxed{W_{m,n}(u,v)=(m-2i)(n-2j)+(-1)^i+(-1)^j.}
\]
Write \(Z_{m,n}\) for the number of zero coefficients, counted with the actual frequency multiplicities. The following disjoint cases give its exact value:

* If \(m,n\) are both odd, then \(\boxed{Z_{m,n}=0}\).
* If \(m=2a\) and \(n=2b+1\), where \(a,b\ge1\), then
\[
\boxed{Z_{2a,2b+1}=\binom{2a}{a}2^{2b}+\binom{2a}{a-1}\binom{2b+1}{b}.}
\]
The corresponding formula with the coordinates interchanged applies when only \(n\) is even.
* If \(m=2a\) and \(n=2b\), where \(a,b\ge1\), then
\[
\boxed{Z_{2a,2b}=\binom{2a}{a}2^{2b-1}+\binom{2b}{b}2^{2a-1}-\mathbf1_{a+b\,\mathrm{odd}}\binom{2a}{a}\binom{2b}{b}.}
\]

Consequently, convolution by \(\mathbf1_{D_{m,n}}\) on \(\ell^2(\mathbb F_2^{m+n})\) has rank \(2^{m+n}-Z_{m,n}\) and is invertible **if and only if both part sizes are odd**. The least strictly positive absolute multiplier is \(1\) when both sizes are odd and \(2\) otherwise; therefore the exact Moore–Penrose inverse norm is respectively \(1\) or \(1/2\), and the positive-spectrum condition number is respectively \(mn+2\) or \((mn+2)/2\).

In particular, for balanced bicliques,
\[
\frac{\operatorname{rank}C_{N,N}}{2^{2N}}=
\begin{cases}
1,&N\text{ odd},\\
1-2^{-N}\binom{N}{N/2},&N\text{ even},
\end{cases}
\]
so along even \(N\) the lost Fourier proportion is asymptotic to \(\sqrt{2/(\pi N)}\), despite the operator being singular at each such \(N\).

## Assumptions and scope

Graphs are finite, simple, undirected and labelled. \(K_{m,n}\) has a fixed ordered left shore \(L\) of size \(m\) and right shore \(R\) of size \(n\). A vertex set is dominating if it meets the closed neighborhood of every vertex; inclusion-minimal means no proper subset is dominating. Frequency vectors \(u\in\mathbb F_2^m\), \(v\in\mathbb F_2^n\) have Hamming weights \(i,j\). Convolution is the **unnormalized** sum \((C_{m,n}f)(x)=\sum_y\mathbf1_{D_{m,n}}(y)f(x-y)\). All spectral assertions concern the complex Hilbert space with counting measure; the same singular values hold over the real space.

The hypothesis \(m,n\ge2\) is essential for the stated classification of inclusion-minimal dominating sets. No statement is made for a shore of size one.

## Proof

**1. Support.** A dominating set contained entirely in \(L\) must contain all of \(L\), because left-shore vertices have no left-shore neighbors. Analogously, a dominating set contained entirely in \(R\) must be all of \(R\). Any vertex set meeting both shores dominates the graph. Such a set is inclusion-minimal exactly when it contains one vertex from each shore: deleting one from a mixed pair leaves a singleton that does not dominate its own shore, since \(m,n\ge2\). It follows that the support is the disjoint union of the two entire shores and the \(mn\) cross-shore pairs.

**2. Fourier formula.** For weights \(i,j\), the signed contribution from all mixed pairs is
\[
\left(\sum_{\ell\in L}(-1)^{u_\ell}\right)\left(\sum_{r\in R}(-1)^{v_r}\right)=(m-2i)(n-2j).
\]
The two complete shores contribute \((-1)^i\) and \((-1)^j\). This proves the displayed multiplier formula for all frequencies, not merely a sample or an asymptotic family.

**3. Zeros: both odd.** When \(m,n\) are odd, the product of the two signed sums is odd and the other two signs sum to an even number. Every multiplier is odd, hence nonzero.

**4. Zeros: both even.** Write \(m=2a,n=2b\). Then \((m-2i)(n-2j)\) is divisible by four, whereas \((-1)^i+(-1)^j\) belongs to \(\{-2,0,2\}\). Thus a zero occurs **exactly** when
\[
(i=a\ \text{or}\ j=b)\quad\text{and}\quad i+j\text{ is odd}.
\]
For \(i=a\), precisely half the \(2^{2b}\) right-shore frequencies have the required parity; the weighted count is \(\binom{2a}{a}2^{2b-1}\). Similarly, the \(j=b\) part has \(\binom{2b}{b}2^{2a-1}\) frequencies. Their intersection consists of \(\binom{2a}{a}\binom{2b}{b}\) frequencies if \(a+b\) is odd, and none otherwise. Inclusion–exclusion gives the even-even formula.

**5. Zeros: one even, one odd.** Write \(m=2a,n=2b+1\). Put \(p=(-1)^i,q=(-1)^j\). If \(p=-q\), the multiplier vanishes exactly when \(m-2i=0\); these are \(\binom{2a}{a}2^{2b}\) frequencies, since exactly half of the right-shore vectors have parity opposite to \(a\). If \(p=q\), a zero requires \((m-2i)(n-2j)=-2p\). Necessarily \(i=a\pm1\), \(j=b\) or \(j=b+1\). Of those four candidate weight pairs, **exactly one** satisfies the sign equation: for each parity choice of \(a,b\), there is one appropriate pair (the four possibilities follow by substituting \((-1)^{a-1}\) and \((-1)^b\)). Its multiplicity is \(\binom{2a}{a-1}\binom{2b+1}{b}\), by binomial symmetry. The two mechanisms are disjoint and exhaust all zeros. Swapping shores gives the remaining case.

**6. Sharp nonzero gap.** If one shore is even, every multiplier is even, and setting the even-shore Hamming weight to half the shore size and choosing the opposite shore parity appropriately yields multiplier \(\pm2\). If both shores are odd, all multipliers are odd. Taking the two Hamming weights immediately below or above their respective midpoints yields four values, three of absolute value \(1\) and one of absolute value \(3\); hence the least nonzero magnitude is \(1\). Their maximum absolute magnitude is \(mn+2\), achieved at the trivial frequency, and the triangle inequality proves that no coefficient exceeds this count of minimal dominating sets. Unnormalized group characters diagonalize convolution, so the rank, Moore–Penrose norm and positive-spectrum condition number follow.

**7. Balanced limit.** For \(m=n=N\) even, the two middle-layer contributions add and their intersection is empty, giving exactly \(Z_{N,N}=2^N\binom N{N/2}\). Stirling's formula gives \(2^{-N}\binom N{N/2}\sim\sqrt{2/(\pi N)}\). For odd \(N\), part 3 gives invertibility.

## Verification

Run `python3 check.py` with Python 3 and the standard library. The checker enumerates all vertex subsets and tests their domination minimality for \(2\le m,n\le6\), independently recomputes all 15,376 Walsh coefficients from these supports, and checks the stated formulas, ranks, spectral extrema and zero counts. It also performs exact weighted-frequency checks of the zero-count and least-positive-multiplier formulas for every \(2\le m,n\le40\). These computations are finite corroboration, not substitutes for the all-order proof above.

## Relationship to prior work

The basic minimal-domination condition and the general enumeration problem predate this result. Anthony and Picollelli (2013) study ordinary, univariate domination polynomials for complete multipartite graphs; their polynomial records unsigned cardinality counts rather than per-frequency signed Walsh sums. Kanté, Limouzy, Mary and Nourine (2014) study equivalences and enumeration of minimal dominating sets; Golovach and collaborators (2016) give an incremental-polynomial enumeration algorithm for chordal bipartite graphs, a class containing every \(K_{m,n}\). These results do not state the exact signed Fourier-nullity formula, the invertibility parity criterion or the sharp convolution gap derived here. The support classification is elementary and is not asserted to be a new graph-theoretic enumeration result. The mathematical claim is the **exact all-parameter Fourier nullity and spectral classification**, not the fact that minimal dominating sets can be enumerated.

## Limitations

The theorem concerns complete bipartite graphs with both shores of size at least two. It does not classify endpoint \(\ell^1\) or \(\ell^\infty\) projection constants, nor does it cover deleted-matching bicliques or other graph classes. The literature comparison was bounded; an unlocated multivariate minimal-domination polynomial or a known character-sum identity could affect historical priority. A closely related 2016 source was available through indexed text but its complete publisher manuscript could not be accessed for a page-by-page comparison. No independent mathematical audit has been performed.

## References

1. B. M. Anthony and M. E. Picollelli, *Complete r-partite graphs determined by their domination polynomial*, arXiv:1303.5999, first submitted 2013-03-24. https://arxiv.org/abs/1303.5999
2. M. M. Kanté, V. Limouzy, A. Mary and L. Nourine, *On the Enumeration of Minimal Dominating Sets and Related Notions*, arXiv:1407.2053, first submitted 2014-07-08. https://arxiv.org/abs/1407.2053
3. P. A. Golovach, P. Heggernes, M. M. Kanté, D. Kratsch and Y. Villanger, *Enumerating minimal dominating sets in chordal bipartite graphs*, Discrete Applied Mathematics **199** (2016), 30–36. DOI:10.1016/j.dam.2014.12.010. https://doi.org/10.1016/j.dam.2014.12.010
