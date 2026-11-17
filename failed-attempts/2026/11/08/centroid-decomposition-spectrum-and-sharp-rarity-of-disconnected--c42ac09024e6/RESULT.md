# Centroid decomposition spectrum and sharp rarity of disconnected perfect evolution algebras over finite fields

## Finding
Fix a finite field \(k=\mathbb F_q\), with \(q\) any prime power, and a positive integer \(n\). Perfect (also called idempotent) evolution-algebra multiplications on \(k^n\), expressed in a **fixed, ordered natural basis**, are parametrized by the invertible structure matrices \(M\in\mathrm{GL}_n(k)\). Define \(g_0=1\) and \(g_n=|\mathrm{GL}_n(k)|=\prod_{j=0}^{n-1}(q^n-q^j)\). Recursively define
\[
 c_0=0,\qquad c_n=g_n-\sum_{s=1}^{n-1}\binom{n-1}{s-1}c_s g_{n-s}\quad(n\ge1).
\]
For the number \(h_{n,k}\) of such matrices whose evolution algebras have centroid of dimension \(k\), set \(h_{0,0}=1\), \(h_{a,0}=0\) for \(a>0\), and
\[
 h_{n,k}=\sum_{s=1}^n\binom{n-1}{s-1}c_s h_{n-s,k-1}\quad(1\le k\le n).
\]
Then \(c_n=h_{n,1}\) is the exact count with one-dimensional centroid, and \(\sum_{k=1}^n h_{n,k}=g_n\). For every integer partition \(\lambda\vdash n\), with \(m_s\) components of size \(s\), the exact count with this unordered *list of indecomposable-ideal dimensions* is
\[
 N_\lambda=\frac{n!}{\prod_{s\ge1}(s!)^{m_s}m_s!}\prod_{s\ge1}c_s^{m_s}.
\]
Equivalently, the labeled formal exponential generating identity is
\[
 \sum_{n\ge0}\sum_{k\ge0}h_{n,k}u^k\frac{z^n}{n!}
 =\exp\left(u\sum_{s\ge1}c_s\frac{z^s}{s!}\right).
\]
This is a formal-power-series identity, with no analytic convergence claim.

There is also a sharp quantitative concentration result: for a uniform structure matrix \(M\in\mathrm{GL}_n(k)\), put \(p_{n,q}=\Pr(\dim_k\operatorname{Cent}(E_M)>1)\) and \(a_{n,q}=n(q-1)g_{n-1}/g_n=n(q-1)/(q^{n-1}(q^n-1))\). For \(n\ge2\),
\[
 a_{n,q}-\binom n2(q-1)^2\frac{g_{n-2}}{g_n}
 \ \le p_{n,q}\le\ a_{n,q}+\sum_{s=2}^{\lfloor n/2\rfloor}\binom ns\frac{g_sg_{n-s}}{g_n}.
\]
In particular, for each fixed prime power \(q\),
\[
 p_{n,q}\sim\frac{n(q-1)}{q^{n-1}(q^n-1)}\qquad(n\to\infty).
\]
Thus, in the labeled finite-field ensemble, the leading obstruction to a one-dimensional centroid is precisely the occurrence of an isolated one-dimensional ideal.

## Assumptions and scope
The algebra \(E_M\) is defined on the labeled vector space with the ordered natural basis \(e_1,\dots,e_n\) by \(e_ie_j=0\) for distinct indices and \(e_i^2=\sum_jM_{ij}e_j\). Invertibility of \(M\) is equivalent to \(E_M^2=E_M\). **Counts are for ordered-basis structure matrices**, not algebra isomorphism classes and not orbits of the monomial-basis-change group; each distinct matrix counts once. The centroid consists of linear maps \(T\) such that \(T(xy)=T(x)y=xT(y)\) for all \(x,y\). The centroid dimension and multiset of indecomposable-factor dimensions are isomorphism-invariant, even though the weighting by matrices is not uniform on isomorphism classes. A component is a weak connected component of the graph on \(\{1,\ldots,n\}\) with undirected edge between distinct \(i,j\) if \(M_{ij}\ne0\) or \(M_{ji}\ne0\). Diagonal entries cause no edges.

## Proof
**Centroid identification.** Let \(T(e_i)=\sum_j t_{ji}e_j\) lie in the centroid. For distinct \(i,j\), the identity \(T(e_i)e_j=e_iT(e_j)\), together with the linear independence of the squares \(\{e_i^2\}\), forces \(t_{ji}=t_{ij}=0\). Hence \(T(e_i)=t_ie_i\). The identity \(T(e_i^2)=T(e_i)e_i\) now states \(M_{ij}(t_j-t_i)=0\) for every ordered pair. Thus \(t_i\) is constant precisely along each weak connected component. Every such assignment is a centroid map; the centroid is a product of \(c\) copies of \(k\), where \(c\) is the number of weak components. Each component spans an ideal, and its matrix block is invertible; as its centroid has no nontrivial idempotents, it is indecomposable. The component sizes therefore give the dimensions of the indecomposable summands. The underlying centroid/decomposition characterization is already established in [1, Theorems 4.5 and 4.7]; the proof here checks it directly under the stated perfectness condition.

**Counting by the component containing the first label.** A graph component cannot have matrix entries to or from its complement, so after simultaneously reordering rows and columns the matrix is block diagonal. Invertibility is equivalent to invertibility of every block. Let \(c_s\) count connected-support invertible \(s\)-by-\(s\) blocks. In any invertible \(n\)-by-\(n\) matrix, the component containing label \(1\) has size \(s\); the other \(s-1\) labels can be chosen in \(\binom{n-1}{s-1}\) ways, its block in \(c_s\) ways, and the remaining arbitrary invertible block in \(g_{n-s}\) ways. Distinct choices cannot yield the same matrix. Therefore \(g_n=\sum_{s=1}^{n}\binom{n-1}{s-1}c_sg_{n-s}\), which rearranges to the stated recursion. Counting the remaining \(k-1\) components instead gives the \(h_{n,k}\) recurrence. If the component-size partition is \(\lambda\), first partition the labels into unordered blocks of those sizes (\(n!/\prod_s(s!)^{m_s}m_s!\) choices), then select a connected invertible block independently for each part; this proves \(N_\lambda\). Expanding the ordinary exponential of a formal exponential generating series gives the equivalent identity.

**Sharp probability estimate.** For a fixed label \(i\), let \(A_i\) be the event that \(\{i\}\) is its entire weak component. Exactly \((q-1)g_{n-1}\) invertible structure matrices have \(A_i\); the intersection of two distinct \(A_i\) has \((q-1)^2g_{n-2}\) matrices. The first two Bonferroni inequalities give the left bound. For the right bound, a disconnected support graph has either a singleton component or a component \(S\) with \(2\le |S|\le\lfloor n/2\rfloor\). For fixed \(S\), requiring no entries across the \(S\)-complement boundary yields exactly \(g_{|S|}g_{n-|S|}\) invertible matrices. A union bound establishes the right estimate.

For a fixed \(q\), let \(F_j=\prod_{i=1}^j(1-q^{-i})\) and \(C_q=\prod_{i\ge1}(1-q^{-i})^{-1}<\infty\). Then \(g_sg_{n-s}/g_n=q^{-2s(n-s)}F_sF_{n-s}/F_n\le C_q q^{-2s(n-s)}\); also \(g_{n-2}/g_n=O_q(q^{-4n})\). Since \(s(n-s)\ge2(n-2)\) for \(2\le s\le n/2\), the right-hand excess is bounded by \(C_q 2^nq^{-4(n-2)}\). Dividing both error bounds by \(a_{n,q}\asymp_q nq^{-2n}\) sends them to zero, because \(2/q^2<1\). This proves the sharp equivalence.

## Verification
The included standalone `verify.py` uses only Python's standard library and independently enumerates all \(q^{n^2}\) matrices in cases \((n,q)=(1,2),(2,2),(3,2),(4,2),(2,3),(3,3),(2,5)\). It checks invertibility by elimination and components by graph connectivity, then compares distributions against the recurrences. It also separately solves the full centroid linear identities on selected invertible matrices and checks the probability inequalities for several field sizes and dimensions. Execute `python3 verify.py`; success ends in `VERIFY_OK_CENTROID`.

For \(q=2\), the centroid-dimension multiplicities for \(n=4\), dimensions \(1,2,3,4\), are \((19446,683,30,1)\), summing to \(|\mathrm{GL}_4(\mathbb F_2)|=20160\). For \(q=3,n=3\), they are \((10960,264,8)\), summing to \(11232\). These finite checks are not proofs for all \(n,q\); the preceding argument is.

## Relationship to prior work
Cabrera Casado, Gonçalves and collaborators [1] prove the graph-component description of the centroid and uniqueness of the indecomposable decomposition. Those are **inputs acknowledged as prior**, not new results here. Wei and Zou [2] count isomorphism classes of perfect/idempotent evolution algebras using a permutation-and-torus group action on invertible structure matrices. Their published orbit formulas do not directly give the present **labeled centroid-dimension and component-size distribution** or the sharp finite-field asymptotic. The exponential formula for labeled connected components is a standard combinatorial principle; the asserted contribution is its application to the complete natural centroid/decomposition spectrum of this finite-field matrix ensemble, together with the explicit leading disconnectedness probability. Priority remains provisional: an unlocated enumeration of block-indecomposable invertible matrices could imply some or all of these consequences.

## Limitations
No count of isomorphism classes within each centroid stratum is claimed; those require orbit weighting. No result is asserted for nonperfect evolution algebras or coefficient rings that are not finite fields. The probability limit fixes \(q\) while \(n\) grows; no simultaneous-parameter asymptotic is claimed. Standard combinatorial connected-object enumeration is not claimed as independently new. This package has undergone self-review, not independent mathematical audit or priority certification.

## References
[1] Y. Cabrera Casado, M. I. Cardoso Gonçalves, D. Gonçalves, D. Martín Barquero, C. Martín González, I. Ruiz Campos, *Centroid and algebraic properties of evolution algebras through graphs*, arXiv:2404.08752v1 (first posted 2024-04-12), especially Theorems 4.5 and 4.7. https://arxiv.org/abs/2404.08752

[2] Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368v1 (first posted 2023-10-18), introduction and Sections 2–6. https://arxiv.org/abs/2310.12368
