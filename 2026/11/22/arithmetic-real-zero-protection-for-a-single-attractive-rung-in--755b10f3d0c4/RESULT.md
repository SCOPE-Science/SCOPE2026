# Arithmetic real-zero protection for a single attractive rung in paired hard-core chains

## Finding

Consider two replicas of the length-\(n\) hard-core path, each with uniform occupied-site fugacity \(z\). On each rail, neighboring sites may not both be occupied. At one marked position \(v\), simultaneous occupation of the two replicas receives a relative weight \(a\ge 0\); all other inter-replica pairs are noninteracting. Write
\[
Z_{n,v}(z;a)=\sum_{S,T\in\mathcal I(P_n)}z^{|S|+|T|}a^{\mathbf 1_{\{v\in S\cap T\}}}.
\]
Here \(n\ge1\) and \(1\le v\le n\). Put
\[
m=\left\lceil\frac n2\right\rceil,\quad d_-=\gcd(n+2,v),\quad d_+=\gcd(n+2,v+1),\quad
k=\left\lfloor\frac{d_--1}{2}\right\rfloor+\left\lfloor\frac{d_+-1}{2}\right\rfloor.
\]
The complete real-zero census is:

- For \(0\le a<1\), every finite zero is negative and real. For \(0<a<1\), the polynomial has degree \(2m\), with exactly \(k\) distinct double zeros and \(2m-2k\) simple zeros.
- For \(a=1\), there are exactly \(m\) distinct double negative zeros.
- For every \(a>1\), there are **exactly \(k\) distinct real zeros**, each negative and double; the other \(2m-2k\) zeros are nonreal, forming \(m-k\) conjugate pairs. The real-root set does not depend on the magnitude of \(a>1\).

In the third case the surviving real zeros are precisely
\[
r_j=-\frac{1}{4\cos^2(\pi j/(n+2))},\qquad 1\le j\le m,
\]
for indices satisfying \((n+2)\mid jv\) or \((n+2)\mid j(v+1)\). In particular, **all real zeros disappear** for \(a>1\) if and only if both \(\gcd(n+2,v)\le2\) and \(\gcd(n+2,v+1)\le2\). When \(n+2\) is prime, every marked position has this property.

For every non-surviving root \(r_j\), its pair near \(a=1\) opens with an explicit square-root law:
\[
z_\pm(a)=r_j\pm c_j\sqrt{1-a}+O(1-a)\quad (a\uparrow1),
\qquad z_\pm(a)=r_j\pm i c_j\sqrt{a-1}+O(a-1)\quad (a\downarrow1),
\]
where \(c_j=|r_j B_{n,v}(r_j)/I_n'(r_j)|>0\) and \(B_{n,v}\) is defined below.

## Assumptions and scope

The substrate is exactly two open length-\(n\) paths with nearest-neighbor exclusion separately within each replica. The only inter-replica interaction is the single soft rung at the **same** site index \(v\), whose double occupancy has nonnegative relative weight \(a\). Fugacity is a single common complex variable, while \(a\) is a fixed nonnegative real parameter. The theorem concerns zeros of a finite grand-canonical polynomial, not a thermodynamic singularity. At \(a=0\), a leading coefficient can vanish, so no uniform degree or multiplicity statement is asserted there.

## Proof

**1. Exact local-defect identity.** Let \(I_j(z)=\sum_{S\in\mathcal I(P_j)}z^{|S|}\) for \(j\ge0\), with \(I_{-1}(z)=1\). Define
\[
A_n(z)=I_n(z),\qquad B_{n,v}(z)=I_{v-2}(z)I_{n-v-1}(z).
\]
We use the convention \(I_j=1\) for \(j\le0\). A single replica containing \(v\) must avoid its neighboring sites, so the occupied-\(v\) contribution is \(zB_{n,v}(z)\). Two independent replicas have partition polynomial \(A_n^2\); replacing weight one by \(a\) exactly on the configurations where both contain \(v\) yields
\[
\boxed{Z_{n,v}(z;a)=A_n(z)^2+(a-1)z^2B_{n,v}(z)^2.}\tag{1}
\]
This identity follows by a disjoint count of configurations, with no large-size limit.

**2. Real-rootedness for \(0\le a\le1\).** Put \(t=\sqrt{1-a}\in[0,1]\). Equation (1) factors as
\[
Z_{n,v}(z;a)=[A_n(z)+tzB_{n,v}(z)]\,[A_n(z)-tzB_{n,v}(z)].\tag{2}
\]
The single-path deletion identity is
\[
A_n(z)=I(P_n-v,z)+zB_{n,v}(z).
\]
Consequently each factor in (2) is the path independent-set polynomial with all vertex activities equal to \(z\), except the marked vertex activity is \((1+t)z\) or \((1-t)z\), respectively. Such a weighted independent-set polynomial on \(P_n\) is the weighted matching generating polynomial of \(P_{n+1}\) obtained by assigning edge \(i\) weight \(w_i\) equal to the corresponding vertex weight coefficient.

For nonnegative \(w_i\), let \(J\) be the real symmetric \((n+1)\)-by-\((n+1)\) tridiagonal matrix with off-diagonal entries \(\sqrt{w_i}\). Its determinant expansion by disjoint adjacent transpositions gives
\[
\det(x\mathbf1-J)=\sum_{M\text{ matching}}(-1)^{|M|}x^{n+1-2|M|}\prod_{i\in M}w_i.
\]
The spectrum of \(J\) is real and symmetric about zero. Pairing opposite eigenvalues proves that the matching generating polynomial is a product of factors \((1+\lambda^2 z)\) for positive eigenvalues \(\lambda\); hence all finite zeros are negative and real. When all \(w_i>0\), \(J\) is irreducible tridiagonal, so all its eigenvalues are simple, and the negative zeros are simple. Thus for \(0<a<1\) both factors in (2) have \(m\) distinct negative zeros; at \(a=0\) nonnegative weights still guarantee all remaining finite zeros are negative and real.

**3. Exact arithmetic count of shared zeros.** For \(0<a<1\), a shared zero of the two factors in (2) must satisfy \(A_n(z)=0\) and \(zB_{n,v}(z)=0\); since \(A_n(0)=1\), this means \(A_n=B_{n,v}=0\). Each shared zero is double, because both weighted factors have simple zeros.

The unweighted tridiagonal path spectrum gives the complete distinct roots
\[
r_j=-[4\cos^2(\pi j/(n+2))]^{-1},\quad 1\le j\le m.\tag{3}
\]
The roots of \(I_{v-2}\) have the same form with denominator \(v\), and those of \(I_{n-v-1}\) with denominator \(n-v+1\). All relevant angles lie strictly between zero and \(\pi/2\), where cosine is injective. Consequently \(r_j\) is a zero of \(B_{n,v}\) if and only if
\[
(n+2)\mid jv\quad\text{or}\quad(n+2)\mid j(n-v+1),
\]
which is the stated condition with \(v+1\), since \(n-v+1\equiv-(v+1)\pmod{n+2}\). For a divisor \(d\mid(n+2)\), precisely \(\lfloor(d-1)/2\rfloor\) indices \(1\le j\le m\) satisfy \((n+2)\mid jd'\) when \(d=\gcd(n+2,d')\). The two indexed collections are disjoint: their intersection would require \((n+2)\mid j(v+1)-jv=j\), impossible for \(1\le j\le m\). Hence the common-zero count is exactly \(k\).

**4. Attractive side and root multiplicity.** For \(a>1\) and any real \(z\), equation (1) is a sum of nonnegative squares. It vanishes exactly when \(A_n(z)=B_{n,v}(z)=0\). Each root \(r_j\) of \(A_n\) is simple, so at such a common root the leading Taylor coefficient is
\[
[A_n'(r_j)]^2+(a-1)r_j^2[B_{n,v}'(r_j)]^2>0,
\]
proving exact multiplicity two. No other real zeros exist. At \(a=1\), equation (1) is simply \(A_n^2\), so each of its \(m\) distinct real zeros is double. For \(a>0\), the leading coefficient of \(Z_{n,v}\) is positive because a maximal independent set can occupy both replicas, giving degree \(2m\); the remaining complex zeros therefore occur as the stated conjugate pairs.

**5. Local square-root motion.** Let \(A_n(r_j)=0\) and \(B_{n,v}(r_j)\ne0\). In (1), expand at \((z,a)=(r_j,1)\). The leading balance is
\[
[A_n'(r_j)]^2(z-r_j)^2+(a-1)r_j^2[B_{n,v}(r_j)]^2=0.
\]
Analytic implicit-function expansion in \(\sqrt{|a-1|}\) gives the two displayed square-root laws and their positive coefficient \(c_j\). The arithmetic common zeros from step 3 persist exactly, rather than merely to leading order.

## Verification

The standalone program `verify_replica_rung.py` independently enumerates all allowed two-rail configurations for \(n\le7\), every rung location, and four exact rational rung weights, comparing the result with (1). It then uses exact Sturm root counts for all \(n\le12\), all positions \(v\), and four positive rational weights on either side of the transition. It reports `IDENTITY_CHECKS_PASSED 112` and `ROOT_COUNT_CHECKS_PASSED 312`. The finite checks are not substituted for the all-length spectral and arithmetic proof above. Run with Python and SymPy: `python verify_replica_rung.py`.

## Relationship to prior work

The real-root property of nonnegative weighted matching polynomials is classical, from Heilmann–Lieb and its extensions such as Wagner's multivariate treatment. It supplies the underlying spectral principle in step 2; no claim of discovery is made for that theorem. Scott–Sokal treat general repulsive lattice-gas zero questions, including soft repulsion, but their stated interaction range is repulsive rather than the attractive rung \(a>1\). The new statement is the complete site-dependent arithmetic count of zero pairs that survive a strictly attractive interlayer defect, its all-parameter multiplicities, and the corresponding sharp local opening. The endpoint-rung case agrees exactly with the previously known centered softened bond of a single longer path; the protected arithmetic interior-rung cases are not covered by that endpoint identity. An earlier equivalent unindexed solution is not excluded.

## Limitations

The two rails must be equal open paths with aligned marked sites, common fugacity and exactly one soft rung. The result does not classify unequal rails, multiple interactions, nonuniform rail fugacities, nor higher-dimensional substrates. The coexistence of double real roots for special arithmetic sites is a finite-polynomial effect, not a physical thermodynamic transition. The comparison with earlier literature cannot establish absolute historical priority.

## References

1. O. J. Heilmann and E. H. Lieb, *Theory of monomer-dimer systems*, Communications in Mathematical Physics **25** (1972), 190–232. https://doi.org/10.1007/BF01877590
2. A. D. Scott and A. D. Sokal, *The repulsive lattice gas, the independent-set polynomial, and the Lovász local lemma*, arXiv:cond-mat/0309352, first public version 2003-09-15. https://arxiv.org/abs/cond-mat/0309352
3. D. G. Wagner, *Weighted enumeration of spanning subgraphs with degree constraints*, arXiv:0803.1659, first public version 2008-03-11. https://arxiv.org/abs/0803.1659
