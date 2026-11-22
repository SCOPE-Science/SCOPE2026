# The affine cycle-index distinction between equicharacteristic and mixed-characteristic length-two chain rings

## Finding

**Theorem (unnormalized natural-action cycle index).** Let \(p\ge3\) be prime, let \(q=p^f\), and let \(R\) be a finite commutative chain ring of length two, with \(R/\mathfrak m\cong\mathbb F_q\), \(\mathfrak m^2=0\), and \(|R|=q^2\). Consider the faithful permutation group \(\operatorname{AGL}_1(R)=\{f_{u,a}:x\mapsto ux+a\mid u\in R^\times,\ a\in R\}\) on the underlying set of \(q^2\) ring elements. Write \(X_j\) for a formal variable that counts cycles of length \(j\) and \(\varphi\) for Euler's totient function. Its **unnormalized** cycle index \(\mathcal Z_R(\mathbf X)=\sum_{u\in R^\times,a\in R}\prod_{j\ge1}X_j^{c_j(f_{u,a})}\) is exactly

\[
\begin{aligned}
\mathcal Z_R(\mathbf X)={}&X_1^{q^2}
+A_R X_p^{q^2/p}+B_R X_{p^2}^{q^2/p^2}
+q(q-1)X_1^qX_p^{q(q-1)/p}\\
&+\sum_{\substack{d\mid q-1\\d>1}}\varphi(d)q^2
X_1X_d^{(q^2-1)/d}\\
&+\sum_{\substack{d\mid q-1\\d>1}}\varphi(d)(q-1)q^2
X_1X_d^{(q-1)/d}X_{dp}^{q(q-1)/(dp)}.
\end{aligned}
\]

If \(\operatorname{char}R=p\), then \((A_R,B_R)=((q-1)(q^2+1),0)\). If \(\operatorname{char}R=p^2\), then \((A_R,B_R)=(q-1,q^2(q-1))\). All the displayed cycle types are distinct, and their coefficients sum to \(|\operatorname{AGL}_1(R)|=q^3(q-1)\). The *normalized* cycle index is \(\mathcal Z_R/(q^3(q-1))\).

Despite the distinction, the **fixed-point distribution is identical** in both characteristics: exactly \((q-1)(q^2+1)\) group elements have zero fixed points, \(q^3(q-2)\) have one, \(q(q-1)\) have \(q\), and one has \(q^2\). More sharply, the full natural-action cycle index distinguishes the two isomorphism types of length-two commutative chain rings with any fixed odd-characteristic residue field. It does so by a positive \(p^2\)-cycle coefficient, which occurs exactly in characteristic \(p^2\).

## Assumptions and scope

A length-two commutative chain ring has exactly the ideals \(0\subsetneq\mathfrak m\subsetneq R\), with \(\mathfrak m^2=0\), \(|\mathfrak m|=q\), and \(|R|=q^2\). Its radical is a one-dimensional \(\mathbb F_q\)-vector space. The additive order of \(1_R\) is either \(p\) or \(p^2\). At fixed \(q=p^f\), the characteristic-\(p\) ring is \(\mathbb F_q[\varepsilon]/(\varepsilon^2)\), while the characteristic-\(p^2\) ring is the unique Galois ring \(\mathrm{GR}(p^2,f)\); these are standard length-two instances of chain-ring classification. The general proof below does not rely on a chosen model. Its assumption \(p\ge3\) matters in the power computation; characteristic two is not claimed. For \(f=1\), classical cycle-index formulas already give the mixed-characteristic \(\mathbb Z/p^2\mathbb Z\) specialization; the asserted uniform comparison and the nonprime-residue-field cases are the subject of the present theorem.

## Proof

**Structure of the units and residue action.** The kernel \(1+\mathfrak m\) of \(R^\times\to\mathbb F_q^\times\) has order \(q\). Since \(\mathfrak m^2=0\), multiplication \((1+w)(1+v)=1+(w+v)\) makes it an elementary abelian group of exponent \(p\). For every residue unit \(\bar u\) of order \(d\mid q-1\) (necessarily prime to \(p\)), its fiber in \(R^\times\) contains exactly one element of order \(d\) (the prime-to-\(p\) component) and the other \(q-1\) elements have order \(dp\). There are \(\varphi(d)\) residue units of order \(d\).

**Nonidentity residue multiplier.** Suppose \(\bar u\ne1\), so \(1-u\) is invertible. Translating by the unique fixed point conjugates \(x\mapsto ux+a\) to multiplication \(x\mapsto ux\). The zero element is its only fixed point. Every nonzero element of \(\mathfrak m\) has orbit length \(d\), since multiplication on \(\mathfrak m\) factors through the residue field; every unit has orbit length equal to the order of \(u\), either \(d\) or \(dp\). Thus the unique lift of order \(d\) contributes \(X_1X_d^{(q^2-1)/d}\); each of the \(q-1\) other lifts contributes \(X_1X_d^{(q-1)/d}X_{dp}^{q(q-1)/(dp)}\). Every lift is compatible with all \(q^2\) translations \(a\), yielding the two divisor sums in the theorem.

**Identity residue multiplier and radical translation.** Now \(u=1+w\), with \(w\in\mathfrak m\). If \(w=a=0\), the map is the identity. If \(w=0\) and \(a\in\mathfrak m\setminus0\), it is a nonzero translation of order \(p\), giving \(q-1\) copies of \(X_p^{q^2/p}\). If \(w\ne0\) and \(a\in\mathfrak m\), the map preserves each residue fiber in \(R/\mathfrak m\) and on the fiber of residue \(c\in\mathbb F_q\) it translates by \(a+wc\in\mathfrak m\). Multiplication by nonzero \(w\) identifies the residue field additively with \(\mathfrak m\), so exactly one of the \(q\) fibers is fixed pointwise; the other fibers decompose into \(p\)-cycles. There are \(q(q-1)\) such maps, of cycle type \(X_1^qX_p^{q(q-1)/p}\).

**Unit translation; the characteristic dichotomy.** It remains to take \(u=1+w\) and \(a\in R^\times\), accounting for \(q^2(q-1)\) affine maps. Modulo \(\mathfrak m\), the map is the nonzero additive translation \(c\mapsto c+\bar a\), of exact order \(p\). As \(w^2=0\), the \(p\)-th power in characteristic \(p\) or \(p^2\) satisfies

\[
f_{u,a}^p(x)=(1+w)^p x+a\sum_{j=0}^{p-1}(1+w)^j=x+pa+\binom p2 wa=x+pa.
\]

Indeed \(p\mathfrak m=0\) and \(p\mid\binom p2\) for odd \(p\). If \(\operatorname{char}R=p\), then \(pa=0\) and every orbit has exact length \(p\) because the residue action already has order \(p\). If \(\operatorname{char}R=p^2\), then \(pR=\mathfrak m\) and \(pa\ne0\) for unit \(a\). Consequently \(f^p\) is a nonzero translation of exact order \(p\), and every \(f\)-orbit has exact length \(p^2\). This yields the displayed \(A_R,B_R\) after including the \(q-1\) nonzero radical translations.

**Exhaustion, fixed points, and reconstruction.** The cases exhaust the \(q(q-1)\) units \(u\) and the \(q^2\) translations \(a\). The only elements with one fixed point are precisely the \(q^3(q-2)\) elements with \(\bar u\ne1\); the \(q(q-1)\) maps with one whole fixed residue fiber have \(q\) fixed points; the identity has \(q^2\); the rest have none. The exponent of \(X_{p^2}\) in the pure \(p^2\)-cycle monomial is positive precisely in characteristic \(p^2\). Since the degree \(q^2\) fixes \(q\) and the two characteristic classes each comprise exactly one ring isomorphism type, the unnormalized cycle-index multiset recovers the ring isomorphism type within the stated family. Every inference is exact for all \(p\ge3\) and \(f\ge1\).

## Verification

Run the standalone dependency-free script `verify_chain_affine.py` with `python3 verify_chain_affine.py`. It constructs both characteristic types directly for \(q=3,5,9\), including the nonsplit ring \(\mathrm{GR}(9,2)\), enumerates every unit coefficient and additive coefficient, constructs each induced permutation on the ring's underlying points, and computes its actual disjoint cycles without invoking the theorem. It independently recomputes the above closed-form coefficients and fixed-point counts. For \(q=3\), the group order is \(54\); for \(q=5\), \(500\); for \(q=9\), \(5832\). All six enumerations match. No finite list proves the arbitrary-\(q\) theorem; the proof is the preceding argument.

## Relationship to prior work

Cella's 2011 thesis *On Symbolic Representations of Music*, Section 3.3, gives a classical explicit cycle-index formula for \(\operatorname{AGL}_1(\mathbb Z/p^a\mathbb Z)\), quoting earlier work. **The specialization to \(\mathbb Z/p^2\mathbb Z\) is already known and is not claimed as new**. The present comparison extends to residue fields of all odd prime-power orders and includes the characteristic-\(p\) dual-number ring, plus an exact cycle-index separation of two rings whose fixed-point statistics agree. The published study *Conjugacy and ordinary character spectra of affine groups over finite chain rings* classifies conjugacy and ordinary complex character data of \(\operatorname{AGL}_1(R)\) and proves other numerical spectra ring-independent; it does not give the natural-action permutation cycle index or the characteristic-sensitive distinction. The published *Centralizer spectra of finite affine monoids distinguish local-ring geometry* counts commuting affine maps, not their natural-action permutation cycles. Alabiad and Alkhamees supply the finite-chain-ring classification context, while Alabiad, Alkhamees and Alhomaidhi study ring automorphisms, distinct from affine permutations of the underlying set.

## Limitations

The statements require an odd prime and length exactly two; no claim is made for characteristic two, higher Loewy length, nonchain or noncommutative local rings, or arbitrary affine monoids with nonunit multipliers. Fixed-point distributions alone do not separate the two ring classes. Prime-field mixed-characteristic cycle indices are covered by classical results; the contribution is the uniform residual-extension comparison, complete parallel census, and characteristic reconstruction. The checker tests only six finite instances. Earlier equivalent all-residue-field cycle-index formulas in specialized permutation-group or finite-ring literature may exist and remain a bibliographic priority risk; no independent audit has been performed.

## References

- S. Alabiad and Y. Alkhamees, *On classification of finite commutative chain rings*, AIMS Mathematics 7 (2022), 1742–1757; first published 2 November 2021, DOI:10.3934/math.2022100. https://www.aimspress.com/article/doi/10.3934/math.2022100
- S. Alabiad, Y. Alkhamees, and A. A. Alhomaidhi, *On Automorphisms of Chain Rings*, Symmetry 15 (2023), 1482; DOI:10.3390/sym15081482. https://www.mdpi.com/2073-8994/15/8/1482
- C. E. Cella, *On Symbolic Representations of Music*, doctoral thesis, Università di Bologna (2011), Section 3.3, p. 49 (printed pagination); https://amsdottorato.unibo.it/id/eprint/4180/1/cella_phd.pdf
- *Conjugacy and ordinary character spectra of affine groups over finite chain rings*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-conjugacy-and-ordinary-character-spectra-of-affine-groups-over-f--0a4181d7ad6d
- *Centralizer spectra of finite affine monoids distinguish local-ring geometry*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-centralizer-spectra-of-finite-affine-monoids-distinguish-local-r--5531b23a5b4d
