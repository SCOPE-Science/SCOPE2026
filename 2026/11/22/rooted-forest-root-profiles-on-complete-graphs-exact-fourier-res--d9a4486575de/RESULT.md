# Rooted-forest root profiles on complete graphs: exact Fourier resonances and sharp gaps

## Finding
For each integer \(n\ge2\) and real activity \(t>0\), consider all spanning forests of the labelled complete graph \(K_n\), with one distinguished root in each component. Give each such rooted forest the weight \(t^{|R|}\), where \(R\subseteq[n]\) is its root set, and collect weights by \(R\). The resulting function \(f_{n,t}\) on the Boolean group \(\mathbb F_2^n\) determines the unnormalized XOR-convolution operator \(T_{n,t}\).

**Exact Fourier spectrum.** The multiplier at any character supported on \(S\subseteq[n]\) depends only on \(s=|S|\) and is
\[
\Lambda_{n,t}(s)=\begin{cases}
t(n+t)^{n-1},&s=0,\\
t(n-t-2s)(n+t)^{n-s-1}(n-t)^{s-1},&1\le s\le n-1,\\
-t(n-t)^{n-1},&s=n.
\end{cases}
\]
At \(t=n\), the middle expression has the usual integer-power interpretation; in particular the multiplier at \(s=1\) is nonzero and all multipliers at \(s\ge2\) vanish.

**Full singular-activity phase diagram.** For positive real \(t\), convolution is singular precisely at
\[
t=n\quad\text{or}\quad t=n-2j,\qquad 1\le j\le\left\lfloor\frac{n-1}{2}\right\rfloor.
\]
At \(t=n\), the nullity is \(2^n-n-1\) and rank is \(n+1\). At each other listed activity \(t=n-2j\), the nullity is exactly \(\binom nj\). Outside these activities the convolution is invertible. Frequency multiplicity at weight \(s\) is \(\binom ns\).

**Sharp integer-weight recovery threshold.** At \(t=1\), the convolution is invertible exactly when \(n\) is even. If \(n=2m+1\) is odd, its kernel has dimension \(\binom{n}{m}\). The smallest **nonzero** absolute multiplier is
\[
g_n=\begin{cases}
(n^2-1)^{m-1},&n=2m,\ m\ge1,\\
2(n+1)^{m-1}(n-1)^m,&n=2m+1,\ m\ge1.
\end{cases}
\]
The largest multiplier magnitude is \((n+1)^{n-1}\). Thus the sharp Hilbert-space Moore--Penrose norm is \(\|T_{n,1}^{\dagger}\|_{2\to2}=1/g_n\), and the sharp condition number on the nonzero spectral subspace is
\[
\kappa_2=\begin{cases}
\dfrac{(n+1)^m}{(n-1)^{m-1}},&n=2m,\\[4pt]
\dfrac{(n+1)^{m+1}}{2(n-1)^m},&n=2m+1.
\end{cases}
\]
These are statements about counting-weight convolution; normalization by total forest mass rescales multipliers and the pseudoinverse norm but does not alter zeros or the condition number.

## Assumptions and scope
A rooted forest is an undirected, labelled, spanning acyclic graph together with exactly one chosen vertex in every component. Edge weights are all one. Two rooted forests with the same root set are counted with their full combinatorial multiplicity. For \(R\ne\varnothing\) with \(|R|=k\), the classical fixed-root forest enumerator is \(k n^{n-k-1}\), interpreted as one when \(k=n\). Consequently
\[
f_{n,t}(R)=t^k k n^{n-k-1},\qquad f_{n,t}(\varnothing)=0.
\]
Characters are \(\chi_S(R)=(-1)^{|S\cap R|}\). The operator acts by \((T_{n,t}h)(X)=\sum_R f_{n,t}(R)h(X\mathbin{\triangle}R)\). All statements apply to every integer \(n\ge2\), each specified real \(t>0\) (not merely integer activities), and real or complex \(\ell^2(\mathbb F_2^n)\) with the usual counting or uniformly normalized Hilbert norm.

## Proof
The fixed-root enumerator is classical; alternatively, the all-minors matrix-tree theorem gives it because a reduced Laplacian of \(K_n\) on the \(n-k\) nonroots has matrix \(nI-J\), with determinant \(k n^{n-k-1}\). For \(k=n\), the empty determinant is one. The multiaffine root-set generating polynomial is therefore
\[
F_{n,t}(z_1,\dots,z_n)=\sum_{R\ne\varnothing}t^{|R|}|R|n^{n-|R|-1}\prod_{i\in R}z_i
=\frac{t}{n}\sum_{i=1}^{n}z_i\prod_{j\ne i}(n+t z_j).
\]
The second equality follows by selecting which \(i\in R\) supplies the factor \(|R|\). Setting all variables to one gives total mass \(F_{n,t}(1,\dots,1)=t(n+t)^{n-1}\).

At \(z_i=-1\) for \(i\in S\), and \(z_i=1\) otherwise, let \(a=n-t\), \(b=n+t\). For \(1\le s\le n-1\), the terms with \(i\notin S\) and \(i\in S\) yield
\[
\Lambda_{n,t}(s)=\frac{t}{n}\bigl[(n-s)a^s b^{n-s-1}-s a^{s-1}b^{n-s}\bigr]
=t(n-t-2s)b^{n-s-1}a^{s-1}.
\]
The evaluations \(s=0\) and \(s=n\) directly give the two boundary cases. This proves the stated spectrum without division by zero, including \(t=n\).

For \(0<t<n\), \(a\ne0\), so the only zeros can occur in middle shells where \(n-t-2s=0\), namely \(t=n-2s>0\) for \(1\le s\le\lfloor(n-1)/2\rfloor\). For \(t>n\), all displayed factors are nonzero. For \(t=n\), the middle formula is \(-2t\,s\,b^{n-2}\) at \(s=1\) and zero for \(2\le s\le n-1\), and the boundary \(s=n\) is zero; \(s=0\) is positive. Multiplicities \(\binom ns\) give the stated nullities. At \(t=1\), \(n-1-2s=0\) holds only when \(n\) is odd, on \(s=(n-1)/2\).

For the sharp unit-activity nonzero gap, let \(a=n-1\) and \(b=n+1\). For \(1\le s\le n-1\),
\[
|\Lambda_{n,1}(s)|=|n-1-2s|\,b^{n-s-1}a^{s-1}.
\]
Along the strictly positive factor branch (until its last positive shell), each consecutive ratio equals
\[
\frac{n-3-2s}{n-1-2s}\frac{a}{b}<1.
\]
Along the negative branch, the consecutive ratio equals
\[
\frac{2s+3-n}{2s+1-n}\frac{a}{b}\ge1,
\]
with equality only at the terminal step \(s=n-1\) to \(s=n\) (the terminal equality follows also directly from the boundary formula). The comparison between the two shells nearest the sign change always favors the first strictly negative shell: the negative-to-positive absolute ratio is \(a/b\) when \(n\) is even and \((a/b)^2\) when \(n\) is odd, whenever both neighbors exist. The exceptional small orders \(n=2,3\) can be checked directly from the spectrum. Therefore the minimum nonzero absolute value occurs at \(s=m\) for \(n=2m\) and at \(s=m+1\) for \(n=2m+1\), which yields the two formulas for \(g_n\). The positive shell at \(s=0\) has magnitude \(b^{n-1}\); all other absolute values are strictly lower, by the same ratios and the terminal bound \(a^{n-1}<b^{n-1}\). Walsh characters orthogonally diagonalize XOR convolution; hence the spectral minimum and maximum imply the asserted Moore--Penrose norm and condition number.

An additional interpretation follows from the normalized root distribution: first choose a uniformly distributed vertex \(U\in[n]\), include \(U\) as a root, then include each other vertex independently with probability \(t/(n+t)\). The probability of any fixed nonempty root set \(R\) of size \(k\) is exactly \(\frac{k}{n}\bigl(\frac{t}{n+t}\bigr)^{k-1}\bigl(\frac{n}{n+t}\bigr)^{n-k}\), identical to \(f_{n,t}(R)/[t(n+t)^{n-1}]\). This is consistent with, and derives immediately from, the classical determinantal root-set law; it is not claimed as a new stand-alone probability law.

## Verification
The included standalone `check_root_spectrum.py` uses the Python 3 standard library only. Running `python3 check_root_spectrum.py` produced `PASS 759494 exact assertions; independent root-forest enumeration up to n=6; all-symmetry arithmetic through n=159`. It reconstructs every rooted-forest profile independently from forest edge subsets and component-root choices for \(2\le n\le6\), computes direct Walsh transforms at six activities per size (fewer if duplicates), checks all resonance and sign branches through \(n=129\), and checks exact unit-activity gaps through \(n=159\). These computations independently test finite cases but are not substituted for the all-\(n\), all-real-\(t\) algebraic proof above.

## Relationship to prior work
Pitman's 1997 tree/forest enumeration explicitly records the classical \(k n^{n-k-1}\) fixed-root formula; Chebotarev--Shamis's matrix-forest theorem supplies the determinant formulation. Avena--Gaudillière (2013) proves a determinantal point process for root sets at arbitrary activity. Their results already imply the complete root-set distribution and can be specialized to recover the first displayed Fourier formula by standard determinant identities; no originality is claimed for the distribution, the probability coupling, or the basic generating polynomial. D'Achille--Enriquez--Melotti (2026) examines complete-graph massive-forest local distributions, and Moumeni (2026) examines root identities including an explicit complete-graph example. The contribution assessed here is the **complete positive-activity cancellation locus with exact shell multiplicities**, including a high-codimension resonance, together with the **sharp all-order nonzero Walsh gap and conditioning at unit activity**. The inspected sources do not state those latter spectral optimization and recovery results.

## Limitations
The result is for complete graphs with unit edge weights and one common positive root activity; it does not classify weighted noncomplete graphs or complex activities. The general root-set measure and exact enumerator are already established in the literature. The spectral classification follows by a tractable specialization of that measure, so an earlier unindexed equivalent signed-root calculation or a corollary in a different formalism remains a specific novelty risk. No independent audit has been performed. Exact-arithmetic checks sample finite dimensions and activities and do not certify the infinite proof by exhaustion.

## References
1. Jim Pitman, *Enumerations of trees and forests related to branching processes and random walks*, Berkeley Statistics Technical Report 482, archived May 1, 1997: https://statistics.berkeley.edu/tech-reports/482 ; full text: https://statistics.berkeley.edu/sites/default/files/tech-reports/482.pdf .
2. Pavel Chebotarev and Elena Shamis, *Matrix-Forest Theorems*, arXiv:math/0602575 (2006), https://arxiv.org/abs/math/0602575 .
3. Luca Avena and Alexandre Gaudillière, *On some random forests with determinantal roots*, arXiv:1310.1723 (first posted October 7, 2013), https://arxiv.org/abs/1310.1723 .
4. Matteo D'Achille, Nathanaël Enriquez and Paul Melotti, *Massive Spanning Forests on the Complete Graph: Exact Distribution and Local Limit*, *Random Structures & Algorithms* (2026), https://doi.org/10.1002/rsa.70048 .
5. Nordine Anis Moumeni, *Punctured Wilson--Evolving Sets and Root Identities for Massive Kirchhoff Forests*, arXiv:2607.13210 (2026), https://arxiv.org/abs/2607.13210 .
