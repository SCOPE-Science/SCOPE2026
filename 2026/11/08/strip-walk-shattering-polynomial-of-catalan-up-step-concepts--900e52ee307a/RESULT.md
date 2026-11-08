# Strip-walk shattering polynomial of Catalan up-step concepts

## Finding
For each integer \(n\ge1\), let \(\mathcal D_n\) be the family of length-\(2n\) Dyck words, represented by the set of positions carrying an up-step, and let queries ask whether a position is an up-step. The complete shattered-support polynomial is
\[
\Phi_n(z)=\sum_{k=0}^{n-1} (A_{n-1-k}^{\,n-1})_{0,n-1-k}z^k,
\]
where \(A_d\) is the \((d+1)\)-by-\((d+1)\) tridiagonal matrix indexed by \(0,\ldots,d\), with diagonal entries \(2\), entries \(1\) immediately above and below the diagonal, and all other entries zero. In particular,
\[
\operatorname{VCdim}(\mathcal D_n)=n-1,\qquad [z^{n-1}]\Phi_n(z)=2^{n-1},
\]
and, for \(n\ge2\),
\[
[z^{n-2}]\Phi_n(z)=\frac{3^{n-1}-1}{2}.
\]
The shattering complex is nonpure for every \(n\ge4\): it has inclusion-maximal faces of sizes \(n-2\) and \(n-1\).

A support \(S\subseteq[2n]\) is shattered if and only if it avoids the endpoints \(1,2n\) and the following strip condition holds. Put \(N=n-1\), \(k=|S|\), and \(d=N-k\). Partition the internal positions into consecutive pairs \(Q_i=\{2i,2i+1\}\), for \(1\le i\le N\). With \(h_0=0\) and
\[
h_i=h_{i-1}+1-|S\cap Q_i|,
\]
we require \(d\ge0\) and \(0\le h_i\le d\) at every \(0\le i\le N\). Necessarily \(h_N=d\). This is an exact structural test for every support, not only for maximum supports.

## Assumptions and scope
A Dyck word has exactly \(n\) up-steps and \(n\) down-steps and never has more down-steps than up-steps in an initial segment. Positions are ordered and labeled \(1,\ldots,2n\). A support is shattered when all \(2^{|S|}\) assignments of up/down answers on its positions extend to at least one Dyck word; different assignments may have different completions. This result is finite, valid for every \(n\ge1\), and does not concern the number of completions of a particular assignment or other lattice-path boundaries.

## Proof
**1. All-positive and all-negative tests suffice.** The up-step sets of Dyck words are the bases of the Catalan matroid, by Ardila's basis-exchange theorem. For any finite matroid, suppose a support \(S\) is contained in a basis \(B_+\) and disjoint from a basis \(B_-\). Given \(T\subseteq S\), start with \(B_+\) and eliminate the elements of \(S\setminus T\) one by one. For any unwanted \(e\in B\setminus B_-\), the basis-exchange axiom gives \(f\in B_-\setminus B\) for which \(B-e+f\) is a basis. Since \(B_-\cap S=\varnothing\), no exchange inserts a forbidden support element, and every desired element of \(T\) stays put. Thus all assignments are realized. The converse follows by taking the all-positive and all-negative labelings. This general criterion is standard matroid theory, not a new claim of the present work.

**2. Translate both tests into prefix inequalities.** Every Dyck up-step set contains position \(1\) and avoids position \(2n\), so shattered supports avoid both endpoints. For each \(0\le i\le N\), let \(F_i=|S\cap[1,2i+1]|\); equivalently, \(F_i\) counts support elements among the first \(i\) internal pairs. A Dyck word avoiding \(S\) exists if and only if \(F_i\le i\) for all \(i\). Necessity follows because its \((2i+1)\)-position prefix must contain at least \(i+1\) ups. For sufficiency, take the first \(n\) available positions outside \(S\) as up-steps. The inequality ensures that the \(j\)-th chosen up-step occurs no later than \(2j-1\) for every \(1\le j\le n\), which is exactly the Dyck condition.

Reflection followed by interchanging up- and down-steps preserves the Dyck family. It converts the existence of a Dyck up-step set containing \(S\) into the existence of a Dyck up-step set avoiding the reflected support \(\{2n+1-s:s\in S\}\). Applying the preceding prefix criterion to the reflection gives, for all \(i\),
\[
|S\cap[2i+2,2n]|\le N-i,
\]
or equivalently \(F_i\ge k-(N-i)\). Thus the simultaneous conditions are
\[
k-N+i\le F_i\le i\quad(0\le i\le N).
\]
Writing \(h_i=i-F_i\) yields \(0\le h_i\le N-k=d\), with \(h_0=0\) and \(h_N=d\), and gives the stated recurrence after processing each pair.

**3. Enumerate the support walks.** For one internal pair, selecting no positions increases height by one (one choice); selecting exactly one gives a horizontal step (two choices); and selecting both decreases height by one (one choice). Therefore the total number of size-\(k\) shattered supports is the number of length-\(N\) walks from \(0\) to \(d=N-k\) confined to \(\{0,\ldots,d\}\), with weights \(1,2,1\) on up, level, down steps. The transfer matrix is exactly \(A_d\), so this count is \((A_d^N)_{0,d}\). For \(k>N\) no support is shattered. This proves the full polynomial without extrapolating from finite data.

An explicit eigenvalue version follows from the standard sine eigenvectors of a path matrix:
\[
[z^k]\Phi_n(z)=\frac{2}{d+2}\sum_{j=1}^{d+1}
\sin\left(\frac{j\pi}{d+2}\right)
\sin\left(\frac{(d+1)j\pi}{d+2}\right)
\left(2+2\cos\left(\frac{j\pi}{d+2}\right)\right)^N,
\quad d=N-k.
\]
Here the trigonometric expression represents an integer, and the transfer-matrix formula is the preferred exact form.

**4. Extremal layers and nonpurity.** At \(k=N\), the strip has height zero: each pair must contribute a horizontal step, with two support choices, giving exactly \(2^N\) maximal-size shattered supports. At \(k=N-1\), the strip has states \(0,1\) and transfer matrix \(\begin{pmatrix}2&1\\1&2\end{pmatrix}\); its off-diagonal \(N\)-th power is \((3^N-1)/2\). Every shattered support has size at most \(N\), so the VC dimension is \(N\).

For \(n\ge4\), consider \(S\) with \(S\cap Q_1=\varnothing\), \(S\cap Q_2=Q_2\), exactly one selected element in each \(Q_3,\ldots,Q_{N-1}\), and \(S\cap Q_N=\varnothing\). Its walk has heights \(0,1,0,\ldots,0,1\), lies in the strip \(\{0,1\}\), and ends at height one, so it is shattered with \(|S|=N-1\). It cannot extend to a size-\(N\) shattered support, because every such support contains exactly one element of each pair, whereas this \(S\) contains both members of \(Q_2\). Hence this face is inclusion-maximal of size \(N-1=n-2\), while size-\(N=n-1\) faces also exist. The complex is nonpure.

## Verification
Run `python3 verify_catalan_shattering.py` using Python 3 and only its standard library. The checker independently enumerates all \(\frac{1}{n+1}\binom{2n}{n}\) Dyck bases for \(1\le n\le7\), constructs every support, directly tests its complete trace set, and compares that test to the strip criterion and transfer-matrix coefficients. For \(8\le n\le24\), it also checks the matrix endpoint and top-two-layer identities. The successful terminal marker is `CATALAN_SHATTERING_CORRIDOR_PASS`. The exhaustive scope ends at seven pairs of semilength, and the proof above, not the finite checks, establishes the unbounded statement.

For reference, the coefficient rows are: \(n=1\): \((1)\); \(n=2\): \((1,2)\); \(n=3\): \((1,4,4)\); \(n=4\): \((1,6,13,8)\); \(n=5\): \((1,8,26,40,16)\); \(n=6\): \((1,10,43,100,121,32)\); \(n=7\): \((1,12,64,196,364,364,64)\).

## Relationship to prior work
Ardila established that Dyck up-step sets are the bases of the Catalan matroid and described its rank, independence, duality and Tutte polynomial. The general equivalence between shattering a matroid's basis indicators and simultaneous independence/coindependence is also known; the present result does not claim priority for this equivalence or for the resulting maximum dimension. Engström, Sanyal and Stump studied a different duality-invariant *lexicographic standard complex* of lattice-path matroids. The standard complex has exactly as many faces as matroid bases, whereas the ordinary shattering complex counted here has, for example, \(28\) faces when \(n=4\), compared with \(14\) Catalan bases. Neither of these comparisons supplies the all-degree matrix enumerator for ordinary shattered supports or this nonpurity witness. Chase and Freitag developed the model-theoretic and combinatorial perspective on banned label sequences, motivating coefficientwise analysis of coordinate traces.

## Limitations
This is not a claim of newness for Catalan matroids, the basis-exchange characterization, path-matrix diagonalization, or the known counting of Catalan bases. The coefficientwise shattering enumeration is a finite-family theorem; its priority under different terminology (for example, common-independent-set enumerators or lattice-path strip walks) has not been independently established. The result does not classify every inclusion-maximal face, determine trace multiplicities, or analyze arbitrary lattice-path matroids. Independent external verification is not yet performed.

## References
1. H. Chase and J. Freitag, *Model theory and combinatorics of banned sequences*, first public version 2018-01-23, arXiv:1801.07640; Journal of Symbolic Logic, DOI 10.1017/jsl.2019.35.
2. A. Engström, R. Sanyal and C. Stump, *Standard complexes of matroids and lattice paths*, first public version 2019-11-27, arXiv:1911.12290; Vietnam Journal of Mathematics 50 (2022), 763–779.
3. F. Ardila, *The Catalan matroid*, first public version 2002-09-25, arXiv:math/0209354; Journal of Combinatorial Theory A 104 (2003), 49–62.
4. V. Guingona, A. Kolesnikov, J. Nierwinski and R. Soucy, *Littlestone and VC-dimension of families of zero sets*, first public version 2021-09-10, arXiv:2109.04805.
5. R. P. Anstee, L. Rónyai and A. Sali, *Shattering News*, Graphs and Combinatorics 18 (2002), 59–73, DOI 10.1007/s003730200003 (related order-shattering literature, which differs from ordinary shattering).
