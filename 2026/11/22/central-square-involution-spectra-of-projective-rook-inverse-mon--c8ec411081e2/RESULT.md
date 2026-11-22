# Central-square involution spectra of projective rook inverse monoids

## Finding
Let \(G\) be an arbitrary finite group, let \(n\geq 1\), and let \(\mathcal R_n(G)\) denote the inverse monoid of partial \(G\)-labelled bijections of an \(n\)-element set (equivalently, the rook wreath product). Let \(\operatorname{Inn}_{\mathrm p}(\mathcal R_n(G))\) denote its inverse monoid of partial inner automorphisms, defined by conjugating the supported local corners.

Write \(Z=Z(G)\), and for \(z\in Z\) set \(\rho_G(z)=|\{g\in G:g^2=z\}|\). For each positive rank \(r\), the partial-inner homomorphism identifies exactly those labelled partial bijections that have the same domain, image and underlying bijection, with labels differing by a **single common multiplier from \(Z\)**. In particular, its rank-\(r\) stratum has cardinality
\[
B_{n,r}=\binom nr^2\frac{r!\,|G|^r}{|Z|},\quad 1\leq r\leq n,
\]
while \(B_{n,0}=1\). A maximal subgroup at a rank-\(r\) idempotent is
\[
H_r\cong (G^r\rtimes\mathfrak S_r)/\Delta Z,
\qquad \Delta Z=\{(z,\ldots,z;1):z\in Z\}.
\]

More finely, the number \(I_{n,r}(G)\) of **self-inverse** elements \(u=u^{-1}\) of rank \(r\) is \(I_{n,0}(G)=1\) and, for \(1\le r\le n\),
\[
\boxed{I_{n,r}(G)=\frac{\binom nr}{|Z|}
 \sum_{j=0}^{\lfloor r/2\rfloor}
 \frac{r!\,|G|^j}{2^j j!(r-2j)!}
 \sum_{z\in Z}\rho_G(z)^{r-2j}.}
\]
Exponent zero in the inner sum is interpreted as \(\rho_G(z)^0=1\), including when \(\rho_G(z)=0\).

When \(G=A\) is abelian and \(t=|A[2]|\), the inner central-square average simplifies to
\[
\frac1{|A|}\sum_{z\in A}\rho_A(z)^f=
\begin{cases}1,&f=0,\\t^{f-1},&f\ge1.\end{cases}
\]
Consequently, for \(n\ge2\), the rank-two maximal subgroup is the generalized dihedral group \(A\rtimes_{-1}C_2\), and the rank-two self-inverse stratum has exactly
\[
\binom n2\bigl(|A|+|A[2]|\bigr)
\]
elements. The complete rank counts for \(A=C_4\) and \(A=C_2^2\) agree for each \(n\), but their rank-two self-inverse counts differ: at \(n=2\), they are \(6\) and \(8\), respectively.

## Assumptions and scope
The group \(G\) is finite, not necessarily abelian; \(n\) is any positive integer. A labelled partial bijection \(u\) consists of a bijection \(\sigma:A\to B\) between subsets of \([n]\) and one label \(\gamma_a\in G\) on each arrow \(a\mapsto\sigma(a)\). Composition follows path concatenation with label multiplication. Its rank is \(|A|=|B|\). The zero has rank zero. At a subset \(B\subseteq[n]\), write \(\mathcal R_B(G)\) for the submonoid of partial labelled bijections supported entirely in \(B\).

The associated partial inner automorphism of \(u:A\to B\) acts from \(\mathcal R_B(G)\) to \(\mathcal R_A(G)\) as \(x\mapsto u^{-1}xu\). This is the standard inverse-semigroup specialization of partial inner automorphisms; the established general theorem identifies their monoid as the image of this map. No assertion is made about arbitrary partial automorphisms rather than partial **inner** automorphisms.

A self-inverse element means \(u=u^{-1}\) in the inverse monoid, not merely an element with square equal to the global identity. Its square is the idempotent of its local domain.

## Proof
**1. Determine the kernel.** Fix \(u:A\to B\) of positive rank. The domain and range of its partial conjugation are precisely \(\mathcal R_B(G)\) and \(\mathcal R_A(G)\), so equality of partial conjugations identifies \(A\) and \(B\). The rank-one idempotents supported at each \(b\in B\) recover the underlying bijection \(B\to A\). Therefore two representatives of the same partial conjugation have the same underlying partial bijection.

Represent a supported labelled matrix unit by \(e_{bc}(x)\), with one arrow \(b\to c\) carrying \(x\in G\). If the corresponding source labels for \(u\) are \(\gamma_b\) in coordinates indexed by \(B\), the conjugate of \(e_{bc}(x)\) has label \(\gamma_b^{-1}x\gamma_c\). For another representative with labels \(\eta_b\), equality on the diagonal units \(e_{bb}(x)\) for all \(x\in G\) forces \(\eta_b\gamma_b^{-1}=z_b\in Z\). Equality on \(e_{bc}(1)\) then forces \(z_b=z_c\) for all \(b,c\). For rank one this last condition is vacuous; the single \(z_b\) is still common. Thus the entire kernel fiber is exactly \(\{(z\gamma_b)_{b\in B}:z\in Z\}\), of size \(|Z|\). Conversely, central simultaneous multiplication leaves every conjugate matrix unit unchanged. Matrix units together with zero exhaust the local corner, proving the kernel assertion.

The general inverse-semigroup partial-inner theorem implies that this image contains all partial inner automorphisms, and composition agrees with labelled partial-bijection multiplication. Hence the quotient is an inverse monoid. For a chosen rank \(r\), the two supports contribute \(\binom nr^2\) choices, their bijection \(r!\) choices, and the labels \(|G|^r/|Z|\) equivalence classes. The rank-zero element is unique. At an idempotent support of size \(r\), the source and target coincide and the local permutation-label group is \((G^r\rtimes\mathfrak S_r)/\Delta Z\). The diagonal subgroup is central since every element of \(Z\) commutes with all labels and is fixed by every coordinate permutation.

**2. Count self-inverse elements.** A partial bijection whose class is self-inverse must have identical domain and image, and its underlying permutation \(\sigma\) must be an involution. If \(\sigma\) has \(j\) two-cycles and \(f=r-2j\) fixed points, there are \(r!/(2^j j!f!)\) choices of \(\sigma\). Its labelled square represents the identity at that support exactly when **all** squared labels are the same central element \(z\in Z\).

For a fixed \(z\), each two-cycle allows an arbitrary first label \(a\in G\), with the opposite label forced to be \(a^{-1}z\); centrality ensures that the reversed product also equals \(z\). This gives \(|G|^j\) label assignments. Each fixed point label must satisfy \(a^2=z\), giving \(\rho_G(z)^f\) assignments. Summing over \(z\in Z\) and quotienting by the free common central multiplier action divides by \(|Z|\). Multiplication by a common central element sends a square value \(z\) to another central square value, so this division does not assume that individual terms are separately divisible by \(|Z|\). Multiplying by the \(\binom nr\) support choices yields the displayed formula. The empty support supplies the unique rank-zero self-inverse element.

**3. Abelian simplification and separation example.** If \(A\) is abelian, its squaring map has kernel \(A[2]\) of size \(t\). Therefore exactly \(|A|/t\) elements of \(A\) have \(t\) square roots and all others have none. This yields the stated central-square averages. At rank two, \((A^2/\Delta A)\rtimes\mathfrak S_2\cong A\rtimes_{-1}C_2\): the quotient coordinate is \((a,b)\mapsto ab^{-1}\), and transposition induces inversion. The rank-two involutions are the \(t\) elements of the index-two abelian subgroup with square one, together with the \(|A|\) reflections. The groups \(C_4\) and \(C_2^2\) have equal order and center size, hence equal rank polynomials \(B_{n,r}\), but \(|C_4[2]|=2\) and \(|(C_2^2)[2]|=4\), which separates their involution spectra.

## Verification
The accompanying standalone Python checker implements finite groups through multiplication tables and independently enumerates every labelled partial bijection on \(n\le3\) points for six representative groups: \(C_2,C_3,C_4,C_2^2,S_3,Q_8\). It forms the projective classes, tests self-inversion directly, computes the formula independently from central square roots, and compares the rank-by-rank counts. For \(n\le2\), and additionally \(n=3\) for \(C_2,S_3\), it also identifies the actual conjugation functions on every supported labelled matrix unit, rather than relying solely on projective labels. All comparisons passed.

For example, with \(n=3\), the rank strata for \(S_3\) are \((1,54,648,1296)\) and the self-inverse strata are \((1,12,66,136)\). For \(Q_8\), they are \((1,36,576,1536)\) and \((1,12,84,208)\). These checks test finite examples, not the all-groups proof, which is the argument above. Reproduction: run \(\texttt{python3 check\_projective\_rook.py}\) using an ordinary Python 3 interpreter; no third-party packages are needed.

## Relationship to prior work
Araújo, Bentz, Kinyon, Konieczny, Malheiro and Mercier (2026) introduce the partial-inner construction for arbitrary semigroups and, in Remark 3.11, state that for inverse semigroups the partial-inner homomorphism has the central congruence as kernel; they explicitly identify the unlabelled symmetric inverse monoid with its partial-inner monoid. This general mechanism is **prior work**, not a new claim here. Kinyon and Stanovský (original preprint 2022) establish the general conjugation/central-congruence connection, likewise credited.

The new assertion isolates the **specific congruence fibers** for a labelled rook wreath monoid and derives its all-rank **central-square self-inverse enumerator** and the rank-two torsion-sensitivity example. The published sources inspected do not state this joint formula. Existing work on ordinary wreath-product powers and rank enumerators of other partial-automorphism monoids is not equivalent: it counts different objects and does not quotient by a common central label. Historical priority for differently formulated projective-wreath involution counts remains open to further library review.

## Limitations
The results concern finite label groups, and **self-inverse** elements of the partial-inner quotient, not involutions in arbitrary semigroup presentations or general partial automorphism monoids. The argument does not classify all element orders or all conjugacy classes of the quotient. The numerical verification covers only the listed small groups and \(n\le3\); the infinite families are established by the algebraic proof, not by finite testing. No independent external mathematical audit has been carried out.

## References
1. J. Araújo, W. Bentz, M. Kinyon, J. Konieczny, A. Malheiro and V. Mercier, *The Inverse Monoid of Partial Inner Automorphisms of a Semigroup*, arXiv:2605.00041, initial public posting 2026-04-28. https://arxiv.org/abs/2605.00041
2. M. Kinyon and D. Stanovský, *Abelianness and centrality in inverse semigroups*, arXiv:2209.13805, initial posting 2022-09-28; later published in Proceedings of the Edinburgh Mathematical Society. https://arxiv.org/abs/2209.13805
3. C. H. Houghton, *Embedding inverse semigroups in wreath products*, Glasgow Mathematical Journal 17 (1976), 77–82, DOI:10.1017/S0017089500002767. https://doi.org/10.1017/S0017089500002767
4. R. Kundu and S. Mondal, *Powers in the wreath product of \(G\) with \(S_n\)*, arXiv:2010.04954 (2020). https://arxiv.org/abs/2010.04954
