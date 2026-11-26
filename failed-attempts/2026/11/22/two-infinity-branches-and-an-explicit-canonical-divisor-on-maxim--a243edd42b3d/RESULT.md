# Two infinity branches and an explicit canonical divisor on maximal automorphism-free plane curves

## Finding
Let \(p\) be any odd prime, \(n\ge2\), and put
\[
d=\frac{p^{2n}-1}{2(p-1)},\qquad
m_i=\frac{p^{2i}-1}{2(p-1)}\quad(1\le i\le n),\qquad
\alpha=d-p-1,\quad \beta=d-1.
\]
Over \(\mathbb F_p\), let \(C_{p,n}\subset\mathbb P^2_{[U:V:W]}\) be the ordinary degree-\(d\) projective closure of
\[
uv^p+v=-1-2\sum_{i=1}^{n}u^{m_i}.
\]
This plane curve is geometrically integral and has precisely one geometric singular point, \(S=[0:1:0]\). Its normalization \(\nu:\widetilde C_{p,n}\to C_{p,n}\) has exactly two \(\mathbb F_p\)-rational points \(P,Q\) over \(S\). In the chart \(V\ne0\), with \(a=U/V\) and \(b=W/V\), the branch at \(P\) is a tame unibranch cusp with value semigroup \(\langle\alpha,\beta\rangle\), and tangent \(b=0\); the branch at \(Q\) is smooth with tangent \(a=0\). Their intersection multiplicity is \(\alpha\). The complete local numerical data are
\[
\delta_S=\frac{(\alpha-1)(\beta-1)}2+\alpha,
\quad \operatorname{cond}_{P}=(\alpha-1)(\beta-1)+\alpha,
\quad \operatorname{cond}_{Q}=\alpha.
\]
Here the conductor orders are those of the conductor ideal of the completed local ring in the two components of its normalized completion. The normalization genus and canonical class satisfy
\[
g=\frac{(p-1)d}{2}=\frac{p^{2n}-1}{4},
\qquad K_{\widetilde C_{p,n}}\sim\bigl((p-1)d-p\bigr)P+(p-2)Q.
\]
In particular the singular plane model loses **exactly one rational point** relative to its normalization over every finite extension of \(\mathbb F_p\). With \(q=p^{4n+2}\), for every \(r\ge1\) its point counts and zeta function over \(\mathbb F_q\) are
\[
\#C_{p,n}(\mathbb F_{q^r})=q^r-2g(-p^{2n+1})^r,
\qquad Z(C_{p,n}/\mathbb F_q,T)=\frac{(1+p^{2n+1}T)^{2g}}{1-qT}.
\]
All these assertions concern the ordinary *singular plane closure*, as distinct from the smooth projective model in the initiating paper.

## Assumptions and scope
The characteristic is odd, \(n\ge2\), and all singularity statements are geometric over an algebraic closure of \(\mathbb F_p\); rationality of the branches is over \(\mathbb F_p\). Write \(\operatorname{cond}_P,\operatorname{cond}_Q\) for valuations of the local conductor as an ideal in the product of the two normalization DVRs, not the conductor of the global Weierstrass numerical semigroup. The displayed global zeta function uses maximality of the **normalization** over \(\mathbb F_{p^{4n+2}}\), as proved by Bartoli, Borges, Timpanella and Zini. The new part is the complete embedded infinity singularity, its conductor and canonical adjunction data, and the singular-model arithmetic correction. No claim is made about the full resolution graph beyond the determined branch pairs, or about unproven older-literature priority.

## Proof
**1. Projective integrality and the unique possible singularity.** It is useful to prove a uniform local statement. Let \(k\) be a field of odd prime characteristic \(p\), and let \(f(u)\in k[u]\) have degree \(d>p+1\), nonzero leading coefficient \(c\), and \(p\nmid d-1\). Consider \(uv^p+v=f(u)\). At \(u=\infty\), set \(t=1/u\). After division by \(u\), all roots of the degree-\(p\) polynomial in \(v\) have \(t\)-valuation \(-(d-1)/p\), since the two leading Newton terms are \(v^p\) and the pole of \(f(u)/u\). Any proper monic factor of degree \(e\), \(0<e<p\), over \(k((t))\) would have constant-coefficient valuation \(-e(d-1)/p\), a noninteger. Thus the polynomial is irreducible over \(k((t))\) and hence over \(k(u)\). The affine curve is smooth because the partial derivative with respect to \(v\) is \(1\).

Its homogeneous equation is
\[
F(U,V,W)=UV^pW^{d-p-1}+VW^{d-1}-\sum_{j=0}^{d}c_jU^jW^{d-j}=0,
\qquad f(u)=\sum_{j=0}^{d}c_ju^j.
\]
At \(W=0\), the equation becomes \(-cU^d=0\), so the sole point at infinity is \([0:1:0]\). Since \(d>p+1\), every local monomial there has total degree at least two; it is singular. There are no other singular points because the affine chart is smooth.

**2. Exact two-branch local calculation.** On \(V\ne0\), use \(a=U/V,b=W/V\) and put \(\alpha=d-p-1\), \(\beta=d-1=\alpha+p\). The completed local equation is
\[
G(a,b)=ab^\alpha+b^\beta-\sum_{j=0}^{d}c_j a^j b^{d-j}.
\]
All \((j,d-j)\) terms with \(j<d\) lie *strictly above* both edges of the lower Newton polygon, because their weights for \((\operatorname{wt}a,\operatorname{wt}b)=(\alpha,\beta)\) and \((p,1)\) are respectively \(\beta d-pj>\alpha d\) and \(d+(p-1)j>\beta\). Also \(b^\beta\) lies above the first edge, and \(a^d\) lies above the second. Thus the two lower edges have initial polynomials
\[
a(b^\alpha-ca^\beta),\qquad b^\alpha(a+b^p).
\]
Since \(\gcd(\alpha,\beta)=\gcd(p,d-1)=1\), and \(p\nmid\alpha\beta\), the first binomial gives exactly one tame plane branch with valuations \(\operatorname{ord}_P(a)=\alpha\), \(\operatorname{ord}_P(b)=\beta\), and semigroup \(\langle\alpha,\beta\rangle\). Indeed the primitive edge has one root after the toric substitution \(a=t^\alpha A,b=t^\beta B\), and its unit derivative is nonzero; the formal implicit-function argument gives one branch with no further characteristic exponent, since the two valuations are coprime. The second edge has one smooth branch, \(a=-b^p+\text{higher terms}\), with \(\operatorname{ord}_Q(a)=p\), \(\operatorname{ord}_Q(b)=1\). No other lower edges or branches exist. Their tangent lines are respectively \(b=0\) and \(a=0\). Substituting the smooth-branch equation into the cusp, or intersecting with its transverse tangent, shows \(I(P,Q)=\alpha\). Both branches are individually preserved by the \(k\)-Galois action (they have different tangent lines), so when \(k=\mathbb F_p\) both normalized points are rational.

**3. Delta, conductor, genus and adjunction.** For a tame one-Puiseux-pair branch with coprime pair \((\alpha,\beta)\), the semigroup is \(\langle\alpha,\beta\rangle\) and its delta invariant is \((\alpha-1)(\beta-1)/2\). The second branch has delta zero. The additive formula for the union gives
\[
\delta_S=\delta_P+\delta_Q+I(P,Q)=\frac{(\alpha-1)(\beta-1)}2+\alpha.
\]
For a reduced plane-curve singularity, the conductor order on a normalization branch equals twice its own delta plus the sum of its pairwise intersections with other branches. This gives the claimed two conductor orders and their sum \(2\delta_S\).

Because this is the only singularity, the genus formula is
\[
g=\frac{(d-1)(d-2)}2-\delta_S=\frac{(p-1)d}{2}.
\]
The line at infinity has normalized pullback \(\nu^*[W=0]=\beta P+Q\), since the local section \(b\) has valuations \(\beta,1\). The adjunction/conductor formula for a plane curve yields
\[
K_{\widetilde C}\sim(d-3)\nu^*[W=0]-\operatorname{cond}_P P-\operatorname{cond}_Q Q.
\]
Substituting \(\alpha=d-p-1\), \(\beta=d-1\) and simplifying gives
\[
K_{\widetilde C}\sim((p-1)d-p)P+(p-2)Q,
\]
whose degree is \((p-1)d-2=2g-2\), an independent adjunction consistency check.

**4. Application and point counts.** For the specified family, \(d=m_n\), the leading coefficient of \(f=-1-2\sum_i u^{m_i}\) is \(-2\ne0\), and \(2d=1+p+\cdots+p^{2n-1}\), so \(2d\equiv1\pmod p\), hence \(p\nmid d-1\). Also \(d>p+1\) for \(n\ge2\). The uniform calculation applies. Bartoli--Borges--Timpanella--Zini, Theorem 1.3(ii), identify its smooth normalization as a curve of genus \(g=(p^{2n}-1)/4\) maximal over \(\mathbb F_q\) for \(q=p^{4n+2}\). Because \(P,Q\) are rational and are identified into one rational point in \(C_{p,n}\), while normalization is an isomorphism everywhere else, \(\#C_{p,n}(\mathbb F_{q^r})=\#\widetilde C_{p,n}(\mathbb F_{q^r})-1\) for every \(r\ge1\). Maximality forces every \(\mathbb F_q\)-Frobenius eigenvalue on \(H^1\) to equal \(-p^{2n+1}\), so
\[
\#\widetilde C_{p,n}(\mathbb F_{q^r})=q^r+1-2g(-p^{2n+1})^r.
\]
Subtracting one yields the point-count and zeta formulas. This is a singular-curve zeta identity, not a claim of a different smooth normalization.

## Verification
Run \(\texttt{python3 verify_infinity.py}\) with Python 3. It checks the precise Newton-support inequalities for \(p=3,5,7,11,13,17,19\) and \(2\le n\le6\), as well as exact integer identities for both branch conductors, the global genus and canonical degree. It prints \(\texttt{VERIFY_OK}\). These finite arithmetic calculations are cross-checks; the all-prime all-\(n\) proof is the symbolic Newton and adjunction argument above.

For \((p,n)=(3,2)\), one has \((d,\alpha,\beta)=(20,16,19)\), \(\delta_S=151\), conductor orders \((286,16)\), genus \(20\), and \(K\sim37P+Q\). For \((p,n)=(5,2)\), the corresponding values are \((78,72,77)\), \(\delta_S=2770\), conductor orders \((5468,72)\), genus \(156\), and \(K\sim307P+3Q\).

## Relationship to prior work
Bartoli--Borges--Timpanella--Zini, *Maximal curves with trivial automorphism group*, arXiv:2610.35788v1, Theorem 1.3(ii) and Section 6.1, supply the explicit prime-field affine equation, genus, geometric automorphism triviality and maximality. Their Proposition 2.1 describes fibers of the \(u\)-map, but does not calculate the singularity of the **ordinary projective plane closure**, its two branch semigroups and intersection, its conductor multidegree, or the singular-model zeta correction. These are additional embedded invariants.

The publicly posted *The Weierstrass semigroup of a non-Galois twisted Artin--Schreier cover* (November 2026, published-finding corpus record \(60088f5a2835\)) gives the global **one-point pole semigroup** at the point above \(u=\infty\) for the broader family \(uv^p-v=f(u)\), together with its genus. That is a different semigroup from the *local value semigroup of a branch at the plane model's singular point*. It does not state the two-branch plane singularity, local conductor, adjunction divisor, or the normalized-to-singular arithmetic point loss. Its global genus is consistent with, and independently checks, the present delta formula; the present claim is not a claim to rediscover that genus or global semigroup. A separate published *Exact pole semigroups on cyclic quotients of linearized Artin--Schreier curves* (published-finding corpus record \(f5b98af39465\)) concerns equations with \(u^2v^p\), not this local plane embedding.

General Newton--Puiseux/plane-branch theory and the plane-curve adjunction and conductor formula are standard tools. The contribution is their exact uniform embedded and arithmetic application to this new unbounded maximal family; there is no claim that the tools themselves are new.

## Limitations
The theorem is about the displayed ordinary plane embedding and its normalization, not a classification of every plane embedding of the abstract curve. It assumes odd characteristic and \(n\ge2\), and says nothing about the characteristic-two model or the low-degree \(n=1\) boundary. The branch semigroup and conductor are local; they must not be confused with the global Weierstrass semigroup or the conductor of a numerical semigroup of pole orders. Priority is assessed against accessible primary literature and mathematical records; an unindexed treatment of the same plane compactification remains possible. No independent mathematical validation has been performed.

## References
1. D. Bartoli, H. Borges, M. Timpanella, G. Zini, *Maximal curves with trivial automorphism group*, arXiv:2610.35788v1 (first public October 26, 2026), Theorem 1.3(ii), Proposition 2.1 and Section 6.1. https://arxiv.org/abs/2610.35788
2. *The Weierstrass semigroup of a non-Galois twisted Artin--Schreier cover*, publicly posted mathematical record (November 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-weierstrass-semigroup-of-a-non-galois-twisted-artin-schreier--60088f5a2835
3. *Exact pole semigroups on cyclic quotients of linearized Artin--Schreier curves*, publicly posted mathematical record (November 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-pole-semigroups-on-cyclic-quotients-of-linearized-artin-sc--f5b98af39465
4. Standard tame Newton-polygon theory for plane branches, the plane-branch conductor formula, and adjunction on reduced plane curves (used with detailed local calculations above).
