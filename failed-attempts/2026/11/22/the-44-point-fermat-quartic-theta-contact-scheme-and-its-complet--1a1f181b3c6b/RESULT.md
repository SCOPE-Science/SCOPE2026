# The 44-point Fermat-quartic theta-contact scheme and its complete Frobenius spectrum

## Finding
Let \(k=\mathbb F_q\) be any finite field of characteristic \(p\ge5\), and let \(C/k\) be the smooth plane quartic \(F=X^4+Y^4+Z^4=0\). Let \(W\) be the *reduced geometric contact locus*: the reduced union of all scheme-theoretic points of intersection having contact multiplicity at least two with any of the 28 geometric bitangent lines of \(C\). Then \(W\) is finite étale of degree 44, with canonical disjoint decomposition
\[
W=W_h\sqcup W_o,\quad W_h=V(F,XYZ),\qquad W_o=V(F,X^4Y^4+Y^4Z^4+Z^4X^4).
\]
The first scheme has degree 12 and consists of hyperflex contacts; the second has degree 32 and consists of contact points on the 16 ordinary bitangents.

For every \(q\) in the indicated residue classes, the exact counts of rational hyperflex contacts, rational ordinary contacts, and total rational bitangent lines are:

| \(q\bmod24\) | \(\#W_h(k)\) | \(\#W_o(k)\) | Rational bitangent lines |
|:--:|--:|--:|--:|
| 1 | 12 | 32 | 28 |
| 5 | 0 | 0 | 16 |
| 7 | 0 | 8 | 4 |
| 11 | 0 | 0 | 4 |
| 13 | 0 | 32 | 16 |
| 17 | 12 | 0 | 28 |
| 19 | 0 | 8 | 4 |
| 23 | 0 | 0 | 4 |

Let \(f_q=\#W(k)\). All geometric points are rational over \(\mathbb F_{q^2}\), so
\[
Z(W/k,T)=(1-T)^{-f_q}(1-T^2)^{-(44-f_q)/2}.
\]
Every finite-extension count is \(\#W(\mathbb F_{q^n})=f_q\) for odd positive \(n\) and \(44\) for even positive \(n\). The least extension splitting all contact points has degree one exactly for \(q\equiv1\pmod{24}\), and otherwise has degree two.

## Assumptions and scope
The characteristic is at least five, so the quartic is smooth and the integers two and three are units. A *bitangent* means a geometric line whose intersection divisor on the smooth quartic is twice an effective divisor of degree two; a hyperflex has divisor \(4P\). We count *distinct geometric contact points*, not contacts with multiplicity, and distinguish rationality of a line from rationality of the points at which it is tangent. The statements hold for all prime powers \(q\) in this characteristic range, not only prime fields.

## Proof
**1. Every bitangent and its contacts.** In the algebraic closure, the twelve coordinate-pair lines are \(X=rY\), \(Y=rZ\), or \(Z=rX\) with \(r^4=-1\). The omitted fourth-power terms then force a single point with multiplicity four on the quartic. These twelve points have a zero coordinate, are distinct, and exhaust \(V(F,XYZ)\). The Hessian determinant of \(F\) is a nonzero scalar multiple of \(X^2Y^2Z^2\); hence exactly these points are flexes, and they have contact order four.

The sixteen further lines are \(X+aY+bZ=0\) for \(a^4=b^4=1\). Substituting \(X=-aY-bZ\) into \(F\) gives the identity
\[
F(-aY-bZ,Y,Z)=2(a^2Y^2+abYZ+b^2Z^2)^2.
\]
The quadratic has distinct roots because its discriminant is \(-3a^2b^2\ne0\). Write \(\mu_3^*=\{\omega\in\overline k: \omega^2+\omega+1=0\}\). Its two contact points are
\[
P(a,b,\omega)=[ab\omega^2:b\omega:a],\qquad a,b\in\mu_4,\quad \omega\in\mu_3^*.
\]
There are 32 distinct such points: each has nonzero coordinates, and its two fourth-power ratios determine \(\omega\), while its linear tangent determines \(a,b\). Thus the 12+16=28 exhibited lines are distinct. A smooth plane quartic in characteristic different from two has exactly 28 geometric bitangents counted as lines; since the list consists of 28 distinct genuine bitangents, it is complete. (This classical count is used only for completeness of the list.)

**2. Exact complete intersection.** Put \(H=X^4Y^4+Y^4Z^4+Z^4X^4\). There is no point on \(V(F,H)\) with a zero coordinate: for instance, \(Z=0\) would force \(X^4+Y^4=0\) and \(X^4Y^4=0\), impossible on the projective plane. In the chart \(Z=1\), set \(u=X^4\), \(v=Y^4\). The equations are \(u+v+1=0\), \(uv+u+v=0\), hence \(uv=1\) and \(u,v\) are the two distinct roots of \(t^2+t+1=0\). For each ordering there are four fourth roots for each coordinate, giving exactly \(2\cdot4\cdot4=32\) distinct geometric points. Since a degree-four curve and a degree-eight curve have total projective intersection number 32 and no common component, these points account for the entire intersection, all with multiplicity one; the intersection is reduced. Their coordinates are precisely the \(P(a,b,\omega)\) above. Consequently \(W_h\) and \(W_o\) are disjoint reduced finite étale schemes of degrees 12 and 32.

**3. Frobenius.** The twelve hyperflex points are determined by three choices of missing coordinate and four solutions to \(r^4=-1\); those solutions are precisely \(\mu_8\setminus\mu_4\), so all twelve are rational over \(k\) iff \(q\equiv1\pmod8\), and otherwise split into six transpositions under Frobenius.

The 32 other points have unique parameters \((a,b,\omega)\in\mu_4^2\times\mu_3^*\). The \(q\)-Frobenius raises all three parameters to the \(q\)-th power. The number of fixed choices of each \(a\) and \(b\) is four when \(q\equiv1\pmod4\) and two when \(q\equiv3\pmod4\); the number of fixed choices of \(\omega\) is two when \(q\equiv1\pmod3\), and zero when \(q\equiv2\pmod3\). Hence the ordinary count is \(32,8,0\) in those cases respectively. Combining this with the hyperflex count by the Chinese remainder theorem gives the eight rows of the table. Since every \(q\) prime to six satisfies \(q^2\equiv1\pmod{24}\), every contact becomes rational over \(\mathbb F_{q^2}\), which also proves the stated cycle types, zeta identity, and finite-extension counts. The bitangent-line column similarly follows because the 16 ordinary lines have parameters in \(\mu_4^2\) and the 12 hyperflex lines have parameters in \(\mu_8\setminus\mu_4\).

## Verification
Run the accompanying standalone program with `python3 fermat_contact_verifier.py`. It constructs exact quadratic finite fields for 23 primes from 5 through 97, explicitly enumerates all 44 geometric contact points and Frobenius orbits, checks the quartic equation and tangent incidence, and independently enumerates rational solutions of the two displayed complete intersections in the projective plane over each prime field. It reports `FERMAT_CONTACT_SPLITTING_VERIFIED_OK`. These finite checks corroborate, but do not replace, the proof valid for all prime powers.

## Relationship to prior work
The classical 12 hyperflex and 16 ordinary bitangent lines of the Fermat quartic, and the fact that the latter produce 32 geometric contacts, are described in Crane's 2003 thesis, chapter 3, section 3.4.4. They are explicitly **not** new here. Oyono–Ritzenthaler (2010) and Plaumann–Sturmfels–Vinzant (2010) provide geometric and arithmetic frameworks for bitangents and rational contacts. Related calculations classify finite-field bitangent **lines** of diagonal quartics and the intersections **among those lines**; neither type of statement gives the 44-point *on-curve contact locus*, its degree-32 complete-intersection equation, or the entire \(q\bmod24\) rational-contact and zeta classification as stated here. Historical priority relative to unavailable or unindexed full texts is not asserted exhaustively.

## Limitations
Characteristics two and three are excluded. The contact scheme is reduced by definition: no claim is made about its nonreduced theta-contact multiplicity scheme in excluded characteristics. This does not compute the zeta function of the genus-three curve itself. The result is a self-contained specific arithmetic classification of a fixed classical quartic, not a classification of all plane quartics. Some very closely related indexed computational texts were available only by summary, leaving a residual historical-priority risk. No independent mathematical audit has been performed.

## References
- E. T. Crane, *Topics in Conformal Geometry and Dynamics*, PhD thesis, University of Cambridge (2003), §3.4.4, https://people.maths.bris.ac.uk/~maetc/thesis.pdf.
- J.-C. Oyono and C. Ritzenthaler, *On rationality of the intersection points of a line with a plane quartic*, publicly available 2010-06-04, arXiv:1006.0873, https://arxiv.org/abs/1006.0873.
- D. Plaumann, B. Sturmfels, C. Vinzant, *Quartic Curves and Their Bitangents*, publicly available 2010-08-24, arXiv:1008.4104, https://arxiv.org/abs/1008.4104.
- M. Merta and D. Zieliński, *On quartics with maximal number of maximal tangency lines* (2025), https://doi.org/10.1007/s10998-025-00648-y (comparison of hyperflex geometry only).
