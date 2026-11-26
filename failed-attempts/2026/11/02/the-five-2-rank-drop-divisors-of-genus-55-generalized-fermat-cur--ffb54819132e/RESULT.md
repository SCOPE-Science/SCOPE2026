# The five \(2\)-rank-drop divisors of genus-\(55\) generalized Fermat curves

## Finding
Let \(K\) be an algebraically closed field of characteristic \(2\). For \(\lambda,\mu\in K\setminus\{0,1\}\) with \(\lambda\ne\mu\), let \(C_{\lambda,\mu}\subset\mathbb P^4_K\) be the smooth curve given by
\[
X_0^3+X_1^3+X_2^3=\lambda X_0^3+X_1^3+X_3^3=\mu X_0^3+X_1^3+X_4^3=0.
\]
It has genus \(55\). Define the following five polynomials, considered on the smooth marked parameter surface \(U\):
\[
P_\infty=1+\lambda+\mu,\qquad P_0=\lambda\mu+\lambda+\mu,\qquad P_1=1+\lambda\mu,
\]
\[
P_\lambda=\lambda^2+\mu,\qquad P_\mu=\lambda+\mu^2.
\]
Let \(m\) be the number of these polynomials that vanish at \((\lambda,\mu)\). The Jacobian has constant \(a\)-number \(15\), and its \(2\)-rank is
\[
\gamma\bigl(\operatorname{Jac}(C_{\lambda,\mu})\bigr)=40-2m.
\]
The five smooth curves \(P_i=0\) meet pairwise **only** at the two marked parameters \((\alpha,\alpha^2)\) and \((\alpha^2,\alpha)\), where \(\alpha^2+\alpha+1=0\). All five meet there, with five distinct tangent directions, forming \(\mathbb P^1(\mathbb F_4)\). Consequently the complete \(2\)-rank stratification on \(U\) consists of rank \(40\) off the five curves, rank \(38\) at their other points, and rank \(30\) at these two intersections. No other ranks occur.

## Assumptions and scope
The result is geometric, over an algebraically closed field of characteristic \(2\), for an **ordered marked** five-point branch configuration. Parameters \(0,1,\lambda,\mu,\infty\) are required to be pairwise distinct; no assertion is made about degenerations on the excluded boundary. The words 'two points' refer to marked parameters, not geometric isomorphism classes of curves. Here \(a(J)=\dim_K\operatorname{Hom}(\alpha_2,J[2])\) and \(\gamma(J)=\dim_{\mathbb F_2}J[2](K)\). The result does not assert a full Ekedahl–Oort type or Newton polygon classification.

## Proof
**1. Geometry and tame character factors.** The diagonal group \(H\cong(\mathbb Z/3\mathbb Z)^4\) acts by the five homogeneous coordinates modulo simultaneous scalars. The invariant coordinate \(x=-X_1^3/X_0^3\) makes \(C/H\cong\mathbb P^1\), with five simple tame branch points \(B=\{\infty,0,1,\lambda,\mu\}\), inertia order three at each. The fiber product is smooth and geometrically connected for distinct branch values; Riemann–Hurwitz yields
\[
2g-2=81\left(-2+5\left(1-\frac13\right)\right)=108,
\]
so \(g=55\). Because \(3\) is invertible in characteristic \(2\), the group-algebra character projectors split the \(2\)-divisible Jacobian (and its Cartier/Hasse–Witt invariants) into the factors associated to nontrivial characters up to inversion. Equivalently, the norm/pullback quotient construction supplies an isogeny with degree prime to \(2\); all projector denominators are powers of \(3\). A character is represented by a vector of five exponents in \(\{0,1,2\}\), with sum zero modulo three, modulo negation. If it is supported at \(r\) branch points, the corresponding cyclic degree-three cover is ramified at exactly these \(r\) points, of genus \(r-2\). Direct counting gives the numbers of character pairs for \(r=2,3,4,5\) as
\[
10,\quad10,\quad15,\quad5,
\]
respectively, and \(10\cdot0+10\cdot1+15\cdot2+5\cdot3=55\). Tame isogenies preserve the \(2\)-rank and \(a\)-number: they identify the associated \(2\)-divisible groups.

**2. The genus-one and genus-two factors.** Each of the ten three-branch cyclic cubics is an elliptic curve with an order-three automorphism fixing a point, hence has \(j=0\) and is supersingular in characteristic two. It contributes \((a,\gamma)=(1,0)\). Each of the fifteen four-branch cyclic cubics is an ordinary genus-two curve. To see this without a genericity assumption, take any four-point subset of \(B\); its generalized Fermat \((3,3)\)-cover of genus \(10\) has \(2\)-rank exactly \(6\) for every nondegenerate parameter, as computed by the Cartier operator in Hidalgo, Section 5.1.3 of arXiv:1710.01349. Its seven positive-genus character factors are four supersingular elliptics and the three genus-two quotients from that four-point set. Since their total \(2\)-rank is six and each genus-two contribution is at most two, **all three** are ordinary. This reasoning applies to every four-point subset. Thus the genus-one factors contribute \((10,0)\), and the genus-two factors contribute \((0,30)\) to \((a,\gamma)\).

**3. Cartier operator on each genus-three quotient.** Fix a distinguished branch point \(b\in B\). After a Möbius transformation sending \(b\) to infinity, its genus-three cyclic cubic quotient has equation
\[
y^3=f(t)=\prod_{j=1}^{4}(t-r_j)=t^4+s_1t^3+s_2t^2+s_3t+s_4
\]
with four distinct finite roots. The holomorphic forms are \(\omega_1=dt/y\), \(\omega_2=dt/y^2\), \(\omega_3=t\,dt/y^2\). Regularity follows from local parameters at the four simple zeros of \(f\) and the valuations \(v_\infty(t)=-3\), \(v_\infty(y)=-4\), \(v_\infty(dt)=-4\). Their number is the genus, so they form a basis. Write \(f=f_e^2+t f_o^2\), where \(f_o=\sqrt{s_3}+\sqrt{s_1}\,t\). Since \(y^3=f\), the characteristic-two Cartier identities \(\mathcal C(g^2dt)=0\), \(\mathcal C(tg^2dt)=gdt\) give
\[
\mathcal C(\omega_1)=\sqrt{s_3}\,\omega_2+\sqrt{s_1}\,\omega_3,\quad \mathcal C(\omega_2)=0,\quad \mathcal C(\omega_3)=\omega_1.
\]
In particular \(s_1,s_3\) cannot both vanish: otherwise \(f=t^4+s_2t^2+s_4\) is a square in characteristic two, contradicting the distinct roots. Therefore Cartier has rank two and the quotient has \(a=1\) for all parameters. Since \(\mathcal C^2(\omega_1)=s_1^{1/4}\,\omega_1\) and \(\mathcal C(\omega_3)=\omega_1\), its stable rank is two when \(s_1\ne0\), and zero when \(s_1=0\) (in the latter case it is nilpotent). The quotient has \(2\)-rank two or zero accordingly.

**4. Exactly five rank-drop equations.** With the distinguished point at infinity, the four roots are \(0,1,\lambda,\mu\), so \(s_1=P_\infty\). For a finite distinguished point \(v\in\{0,1,\lambda,\mu\}\), put \(t=1/(x-v)\). Its four roots are \(0\) and \(1/(w-v)\) for the other three finite points \(w\). Their sum is \(\sum_{w\ne v}1/(w-v)\). Direct common-denominator simplification on \(U\) yields numerators \(P_0,P_1,P_\lambda,P_\mu\), respectively. Each genus-three factor contributes \((a,\gamma)=(1,2)\) off its divisor and \((1,0)\) on it. Summing the ten elliptic, fifteen genus-two, and five genus-three factors proves \(a=10+5=15\) and \(\gamma=30+2(5-m)=40-2m\).

**5. Geometry of the rank-drop loci.** All five \(P_i=0\) are smooth on \(U\); this follows from their partial derivatives (for \(P_\lambda\) the \(\mu\)-derivative is one and for \(P_\mu\) the \(\lambda\)-derivative is one). Pairwise elimination of \(\mu\) from any two equations, after removing factors \(\lambda\) and \(\lambda+1\) that cannot vanish on \(U\), gives the same remaining factor \(\lambda^2+\lambda+1\). Substitution into all five equations shows that the only solutions in \(U\) are \((\alpha,\alpha^2)\), \((\alpha^2,\alpha)\), where \(\alpha^2+\alpha+1=0\); conversely all five vanish there. The five tangent slopes at \((\lambda,\mu)=(\alpha,\alpha^2)\), using \(d\mu/d\lambda\) and recording vertical slope for \(P_\mu\), are
\[
1,\quad (\mu+1)/(\lambda+1),\quad\mu/\lambda,\quad0,\quad\infty,
\]
which are the five distinct elements of \(\mathbb P^1(\mathbb F_4)\). The other point is the conjugate configuration and has the same distinct-direction property. This establishes the complete stratification.

## Verification
Run `python3 verify.py` with Python 3 (standard library only). The script checks all ten pairwise eliminations over \(\mathbb F_2[\lambda]\), the \(10,10,15,5\) character-orbit count, the five rank-drop equations and Cartier semilinear iterates over \(\mathbb F_8\) and \(\mathbb F_{16}\), and the full tangent-direction statement over \(\mathbb F_4\). It reports `VERIFY_OK`. The finite-field enumeration is **not** the proof of the infinite-field theorem; the symbolic eliminations, character arguments and explicit Cartier computation above establish the theorem for every algebraically closed characteristic-two field.

## Relationship to prior work
The generalized Fermat models and their automorphisms are treated in *Automorphisms of the Generalized Fermat Curves*, arXiv:1409.3063; the quotient/Jacobian factor approach is described in *Isogenous Decomposition of the Jacobian of Generalized Fermat Curves*, arXiv:1507.02903. In *Holomorphic Differentials of Generalized Fermat Curves*, arXiv:1710.01349, Hidalgo gives the complete characteristic-two Cartier computation for type \((3,3)\) in Section 5.1.3 and a general Cartier table for type \((k,4)\) in Section 5.1.4. The new conclusion isolated here is the **complete type \((3,4)\) \(2\)-rank stratification**, constancy of the \(a\)-number, and five-divisor collision geometry. These are compatible with, and can be developed from, the earlier general Cartier machinery; they are not presented there as a classification of all marked parameter values.

## Limitations
This treats only the type \((3,4)\) family in characteristic two, and only the indicated two invariants, not full \(2\)-torsion group schemes, Newton polygons, or compactified boundary curves. The marked parameter locus is not the moduli quotient by permutations. Literature priority for an equivalent classification under other terminology is not independently settled; the nearby general Cartier formula is strong prior coverage and must be acknowledged when citing this specialized result. The claim of completeness concerns parameter strata, not all genus-\(55\) curves.

## References
- R. Hidalgo et al., *Automorphisms of the Generalized Fermat Curves*, arXiv:1409.3063v1 (2014-09-10).
- G. Carvacho, R. Hidalgo and S. Quispe, *Isogenous Decomposition of the Jacobian of Generalized Fermat Curves*, arXiv:1507.02903v1 (2015-07-10).
- R. Hidalgo, *Holomorphic Differentials of Generalized Fermat Curves*, arXiv:1710.01349v1 (2017-10-03), especially Sections 5.1.3–5.1.4.
