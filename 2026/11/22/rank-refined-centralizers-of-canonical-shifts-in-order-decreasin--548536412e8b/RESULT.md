# Rank-refined centralizers of canonical shifts in order-decreasing partial-isometry monoids

## Finding

Let \(n\ge2\) and \(1\le k<n\) be integers, and let \(\pi\) be the partial shift \(\pi(x)=x-1\) with domain \(\{2,\ldots,n\}\). Let \(\mathcal O_n\) consist of all order-preserving, order-decreasing partial isometries of \(\{1,\ldots,n\}\), and let \(\mathcal D_n\) be the corresponding monoid without the order-preserving restriction. Write \(C_{\mathcal M}(\pi^k)\) for the commuting centralizer in either monoid and \(\operatorname{rk}(\alpha)=|\operatorname{dom}\alpha|\).

For \(0\le d<n\), set \(m_d=\min\{k,n-d\}\), and for \(1\le j\le m_d\) put
\[
L_{d,j}=1+\left\lfloor\frac{n-d-j}{k}\right\rfloor.
\]
The complete centralizer rank polynomials are
\[
\begin{aligned}
T_{n,k}(z)&=1+\sum_{d=0}^{n-1}\left[\prod_{j=1}^{m_d}(1+z^{L_{d,j}})-1\right],\\
R_{n,k}(z)&=z^2\sum_{p=n-k+1}^{n-1}\sum_{q=p+1}^{n}
 \bigl(p+\min\{k,p\}-q\bigr)_+(1+z)^{q-p-1},\\
\sum_{\alpha\in C_{\mathcal O_n}(\pi^k)}z^{\operatorname{rk}(\alpha)}&=T_{n,k}(z),\\
\sum_{\alpha\in C_{\mathcal D_n}(\pi^k)}z^{\operatorname{rk}(\alpha)}&=T_{n,k}(z)+R_{n,k}(z),
\end{aligned}
\]
where \(t_+=\max\{t,0\}\). In particular,
\[
|C_{\mathcal O_n}(\pi^k)|=(n-k+2)2^k-n-1.
\]
When \(n\ge2k-1\), the reversing contribution stabilizes in \(n\):
\[
\begin{aligned}
R_{n,k}(z)&=z^2\sum_{w=1}^{k-1}(k-w)^2(1+z)^{w-1},\\
|C_{\mathcal D_n}(\pi^k)|&=(n-k+5)2^k-n-k^2-2k-4.
\end{aligned}
\]
At \(k=1\), both centralizers are exactly \(\{\pi^0,\pi^1,\ldots,\pi^n\}\) (so each has \(n+1\) elements). Thus the nilpotent generator \(\pi\) is self-centralizing in either monoid.

## Assumptions and scope

All maps are partial injections on the nonempty finite chain \(X_n=\{1,\ldots,n\}\), composed as partial functions, with the empty map \(0\) included. An isometry preserves absolute differences on its domain; order-decreasing means \(\alpha(x)\le x\) wherever defined. Rank means domain cardinality, not minimum generator size. For \(k\ge n\), \(\pi^k=0\) and its centralizer is the whole monoid, so the displayed claim is restricted to \(1\le k<n\). All formulas hold at small \(n\), including \(n=2\). The polynomial variable \(z\) is formal.

## Proof

**1. Exhaustive normal forms.** Every partial isometry of rank at least two is either increasing, hence of the form \(\tau_{d,D}(x)=x-d\), or decreasing, hence of the form \(\rho_{c,D}(x)=c-x\). An increasing order-decreasing form has \(0\le d<n\) and a nonempty domain \(D\subseteq\{d+1,\ldots,n\}\). A decreasing form with at least two points has \(p=\min D<q=\max D\), \(c>q\) (positive minimum image), and \(c-p\le p\) (order-decreasing at the smallest point); its image automatically lies in \(X_n\). The decreasing and increasing forms are disjoint for rank at least two. Every rank-one map is increasing for a unique offset \(d\); the empty map is counted once.

**2. Increasing commutants.** Fix \(d\). At any \(x\in\{d+k+1,\ldots,n\}\), both \(\pi^k\tau_{d,D}\) and \(\tau_{d,D}\pi^k\), when defined, have value \(x-d-k\). Their membership conditions are respectively \(x\in D\) and \(x-k\in D\) (possibly with composition-order labels reversed); neither composite has a domain point below \(d+k+1\). Consequently they are equal exactly when
\[
 x\in D\quad\Longleftrightarrow\quad x-k\in D
 \qquad(d+k+1\le x\le n).
\]
This holds precisely when \(D\) is a union of whole congruence chains modulo \(k\) inside \(\{d+1,\ldots,n\}\). The \(j\)-th chain starts at \(d+j\) and has length \(L_{d,j}\), with \(j\in\{1,\ldots,m_d\}\). Every chain may be present or absent independently, except that the globally empty map is counted only once. Hence the increasing polynomial is \(T_{n,k}(z)\). At \(z=1\), summing \(2^{\min(k,n-d)}-1\) over \(d\), then adding one, gives \((n-k+2)2^k-n-1\).

**3. Decreasing commutants.** Fix a rank-at-least-two decreasing form \(\rho(x)=c-x\). On any common input on which the compositions exist, the two expressions \(\rho\pi^k\) and \(\pi^k\rho\) differ by \(2k>0\). Thus equality of these *partial functions* is possible if and only if both compositions have empty domain. Since the domain and image of \(\pi^k\) are \(\{k+1,\ldots,n\}\) and \(\{1,\ldots,n-k\}\), this happens exactly when
\[
 D\subseteq\{n-k+1,\ldots,n\},\qquad
 \rho(D)\subseteq\{1,\ldots,k\}.
\]
For prescribed endpoints \(p<q\) within the upper interval, order decrease and the image bound are equivalent to
\[
 q+1\le c\le p+\min\{p,k\}.
\]
There are \((p+\min\{p,k\}-q)_+\) such integer centers. The \(q-p-1\) interior points can be chosen independently, so their rank generating factor is \(z^2(1+z)^{q-p-1}\). Summing yields \(R_{n,k}(z)\). This counts no increasing forms because it requires rank at least two.

**4. Stable range and self-centralization.** If \(n\ge2k-1\), each permissible \(p\) is at least \(k\), so \(\min\{p,k\}=k\). For a gap \(w=q-p\in\{1,\ldots,k-1\}\), exactly \(k-w\) endpoints \(p\) occur, and each admits \(k-w\) centers. This gives the stable-range polynomial. The identity
\[
\sum_{w=1}^{k-1}(k-w)^2 2^{w-1}
 =3\cdot 2^k-k^2-2k-3
\]
follows from the usual finite geometric sums (or induction on \(k\)), including \(k=1\). Adding the increasing count proves the cardinality formula. At \(k=1\), each nonzero increasing commutant consists of the single full chain for its offset \(d\), giving \(\pi^d\), and there are no reversing commutants. The list of powers is therefore exact.

## Verification

The accompanying standalone \(\texttt{VERIFY.py}\) (Python standard library only) independently enumerates finite order-decreasing partial isometries and compares the rank-by-rank counts of both orientation types with the two formulas for every \(n\in\{2,\ldots,9\}\) and \(1\le k<n\), totaling 36 parameter pairs. For \(n\le6\), it also checks its complete normal-form enumerator against a separate brute-force enumeration of all partial injections. Running \(\texttt{python3 VERIFY.py}\) prints \(\texttt{CENTRALIZER_RANK_CENSUS_OK 36}\) and fails on any discrepancy. Finite computation is a check, not a proof of the formulas for unbounded \(n\) or \(k\).

## Relationship to prior work

Ayık, Ayık and Fernandes (2026, arXiv:2611.12150v1) introduce the same monoids and explicitly identify the distinguished nilpotent partial shift and its powers; their results concern generating sets, ranks of ideals, and presentations, not rank-refined centralizers. Kehinde, Makanjuola and Umar (2011, arXiv:1101.2558) establish structural Green-relation and cardinality results for the same monoids; Al-Kharousi, Kehinde and Umar (2017, arXiv:1702.04485) give rank, idempotent, and Green-class counts, again without centralizer rank spectra. Earlier work on centralizers of nilpotent elements in the *full symmetric inverse monoid* counts a different ambient centralizer and does not filter by both order decrease and metric preservation. A separate calculation of commuting partners restricted only to a rank-prescribed family of shift-one generators does not determine the centralizers inside the full monoids or for arbitrary powers. The special case \(k=1\) is also compatible with the classical unrestricted single-chain centralizer; the substantive new enumeration is the all-power, rank-refined submonoid formula including the reversal correction. These comparisons distinguish the present complete filtered centralizer theorem from the cited prior statements; they do not establish absolute historical uniqueness.

## Limitations

Only centralizers of powers of the canonical full shift are classified; arbitrary elements' centralizers, other chain actions, and nonlinear partial maps are outside scope. The stable-range closed formula requires \(n\ge2k-1\); outside it the exact endpoint sum must be used. Historical priority remains conditional on literature indexing and accessible full texts. The result has not received an independent mathematical audit.

## References

1. G. Ayık, H. Ayık, V. H. Fernandes, *On semigroups of order-decreasing partial isometries: presentations and ranks of certain ideals*, arXiv:2611.12150v1 (first posted 2026-11-09), https://arxiv.org/html/2611.12150v1 .
2. R. Kehinde, S. O. Makanjuola, A. Umar, *On the semigroup of order-decreasing partial isometries of a finite chain*, arXiv:1101.2558 (2011), https://arxiv.org/abs/1101.2558 .
3. F. Al-Kharousi, R. Kehinde, A. Umar, *Combinatorial results for certain semigroups of order-decreasing partial isometries of a finite chain*, arXiv:1702.04485 (2017), https://arxiv.org/abs/1702.04485 .
4. *A cycle-cancellation sieve for nilpotent centralizers in symmetric inverse monoids*, public published-finding corpus record (2026-10-25), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-cycle-cancellation-sieve-for-nilpotent-centralizers-in-symmetr--1d8c7c099b3b .
5. *Nilpotent partial-permutation conjugacy is determined by its centralizer rank spectrum*, public published-finding corpus record (2026-10-26), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-nilpotent-partial-permutation-conjugacy-is-determined-by-its-cen--8be29dd91c24 .
