# Frobenius degrees of all bitangent-contact points in Ciani's symmetric quartic pencil

## Finding
Let \(k=\mathbb F_q\) have characteristic at least five, and let
\[
 C_\lambda:\ X^4+Y^4+Z^4+\lambda(X^2Y^2+X^2Z^2+Y^2Z^2)=0,
 \qquad \lambda\in k\setminus\{-2,-1,2\}.
\]
For every geometric bitangent, retain the *reduced support* of its degree-two contact divisor. The union \(D_\lambda\) of these distinct contact points is a finite reduced \(k\)-scheme. Every closed point has degree \(1\), \(2\), or \(4\). Its precise Frobenius cycle decomposition is determined by the following rules, which give the contributions of three disjoint groups of bitangents to the numbers of cycles of each degree. Here \(\chi\) is the quadratic character of \(k\), \(d=-1-\lambda\), \(e=2+\lambda\), and the notation \(1^a2^b4^c\) means \(a\) cycles of degree one, \(b\) of degree two, and \(c\) of degree four.

**Four sign bitangents:** contribute \(1^8\) if \(\chi(-3)=1\), and \(2^4\) otherwise.

**Twelve mixed-coefficient bitangents:** if \(\chi(d)=1\), contribute \(1^{12}\) at \(\lambda=3\), otherwise \(1^{24}\) if \(\chi(3-\lambda)=1\) and \(2^{12}\) if \(\chi(3-\lambda)=-1\). If \(\chi(d)=-1\), contribute \(2^6\) at \(\lambda=3\), and \(2^{12}\) otherwise.

**Twelve coordinate-zero bitangents:** if \(\lambda=0\), contribute \(1^{12}\) when \(\chi(d)=\chi(e)=1\), and \(2^6\) otherwise. If \(\lambda\ne0\) and \(\chi(d)=\chi(e)=1\), choose either \(w\in k\) with \(w^2=d\); they contribute \(1^{24}\) if \(\chi(-4\lambda/(1-w))=1\), and \(2^{12}\) otherwise. This character test does not depend on the chosen root. If \(\lambda\ne0\) and both \(\chi(d)\) and \(\chi(e)\) equal \(-1\), they contribute \(4^6\). In the other remaining cases they contribute \(2^{12}\).

Add the three contributions to obtain \(D_\lambda\)'s exact zeta function:
\[
 Z(D_\lambda/k,T)=\frac1{(1-T)^{n_1}(1-T^2)^{n_2}(1-T^4)^{n_4}}.
\]
There are \(56\) geometric contact supports except at \(\lambda=0\) or \(\lambda=3\), when there are \(44\). The only hyperflex parameters are these two (provided the parameter is smooth); each has twelve hyperflex lines.

In particular, precisely
\[
 \frac{q-\chi(-1)}4-\mathbf 1_{q\equiv3\ (\mathrm{mod}\ 8)}
\]
smooth marked parameters have six degree-four closed contact points. For these parameters some contacts genuinely require \(\mathbb F_{q^4}\), **even though every geometric bitangent line itself is defined over \(\mathbb F_{q^2}\)**. For example, over \(\mathbb F_{11}\), the parameter \(\lambda=4\) gives \(Z(D_4,T)=(1-T^2)^{-16}(1-T^4)^{-6}\), whereas \(\lambda=1\) has all \(28\) bitangent lines rational but no rational contact point, with \(Z(D_1,T)=(1-T^2)^{-28}\).

## Assumptions and scope
The characteristic restriction excludes exceptional behavior at three and inseparability at two. A geometric bitangent meets the smooth quartic in twice a degree-two effective divisor, possibly a repeated point (hyperflex). Distinct lines cannot share a smooth contact point because the tangent line at that point is unique. Consequently, removing repeated contacts at hyperflexes gives a reduced finite scheme, and the above cycle counts have their usual finite-set interpretation. All counts concern literal coefficient parameters \(\lambda\), not geometric isomorphism classes or twists. If \(\lambda=3\) is excluded by smoothness (characteristic five), its hyperflex rule is vacuous.

## Proof
**1. Smoothness and all geometric bitangents.** For characteristic at least five, the partial derivatives yield smoothness exactly for \(\lambda\notin\{-2,-1,2\}\). Choose \(w^2=d=-1-\lambda\) and \(s^2=e=2+\lambda\) over an algebraic closure. The \(28\) bitangents are the four sign lines \(X\pm Y\pm Z=0\); the twelve permutations of \(wX\pm Y\pm Z=0\); and the twelve coordinate-zero lines whose two nonzero coefficients have ratio \(\kappa\in\{\pm(1+w)/s,\pm(1-w)/s\}\). Their restrictions are explicit squares. The exclusions make all \(28\) lines distinct. The classical count of \(28\) geometric bitangents to a smooth plane quartic in odd characteristic proves completeness. These formulas and their quadratic-field descent are also established in the prior bitangent-line classification cited below; the present result concerns the contact points instead.

**2. Quadratic contact equations.** For a sign line, the restricted quartic equals \((\lambda+2)(U^2+UV+V^2)^2\); the contact quadratic discriminant is \(-3\). For a mixed line, after using \(w^2=d\), the contact quadratic can be normalized to \(U^2+wUV-V^2\), whose discriminant is \(w^2+4=3-\lambda\). For a coordinate-zero line \(Z=\kappa X\), its restriction is
\[
 \left(Y^2+\tfrac{\lambda(1+\kappa^2)}2X^2\right)^2,
\]
with discriminant \(\delta_\kappa=-2\lambda(1+\kappa^2)\). The mixed group is hyperflex exactly at \(\lambda=3\); the coordinate-zero group is hyperflex exactly at \(\lambda=0\). No sign bitangent is a hyperflex in characteristic at least five. All contact points are geometrically distinct between distinct lines, giving \(56\) or \(44\) supports.

**3. Frobenius for sign and mixed lines.** The sign lines are rational, so their nonzero quadratic discriminant \(-3\) directly gives \(1^8\) or \(2^4\). Mixed lines are rational precisely when \(d\) is square. If rational, their quadratic discriminant \(3-\lambda\) yields two rational contacts, one rational hyperflex, or a quadratic pair on each line. If not rational, they come in six degree-two line pairs. Since \(3-\lambda\in k\), its square root exists in \(\mathbb F_{q^2}\). Their contacts therefore have degree two, with twelve cycles ordinarily or six cycles in the hyperflex case.

**4. Frobenius for coordinate-zero lines.** They are rational precisely when \(d\) and \(e\) are both squares. If so, with \(w\in k\) and \(\kappa=(1+w)/s\), one has \(\kappa^2=(1+w)/(1-w)\), hence \(\delta_\kappa=-4\lambda/(1-w)\). Replacing \(w\) by \(-w\) changes the denominator from \(1-w\) to \(1+w\); these have the same square class because their product is \(e\), a square. Thus the character criterion is well-defined. If the lines are nonrational, they are defined over \(k_2=\mathbb F_{q^2}\) in six Frobenius pairs. For \(\lambda\ne0\), the discriminant \(\delta_\kappa\) is nonzero. If \(d\) is square and \(e\) nonsquare, it already lies in \(k\) and is therefore square in \(k_2\). If \(d\) is nonsquare, its norm from \(k_2\) to \(k\) is \(16\lambda^2/e\): indeed the two Frobenius-conjugate values of \(1+\kappa^2\) multiply to \(4/e\). An element of \(k_2\) is square exactly when its norm to \(k\) is square. Hence the contacts have degree four exactly when \(d,e\) are both nonsquares, and otherwise degree two. At \(\lambda=0\), all twelve coordinate-zero bitangents are hyperflexes with one contact per line, yielding \(1^{12}\) or \(2^6\). These cases exhaust every line and prove the stated zeta function.

**5. Frequency of quartic contacts.** Put \(d=-1-\lambda\), so \(e=1-d\). Across \(d\in k\setminus\{0,1\}\), the number for which \(d\) and \(1-d\) are both nonsquares equals \((q-\chi(-1))/4\) by the quadratic Jacobi sum \(\sum_d\chi(d(1-d))=-\chi(-1)\). The additionally forbidden smoothness value \(d=-3\) does not lie in this set, because \(1-d=4\) is a square. The special parameter \(\lambda=0\), equivalently \(d=-1,e=2\), must be deleted from the quartic-contact count because it is hyperflex; this value lies in the two-nonsquare set exactly when \(q\equiv3\pmod8\). The exact frequency follows.

## Verification
Run the dependency-free `verify_contacts.py` with Python 3. Its first route enumerates *all* rational projective lines for each smooth parameter over the prime fields of orders \(5,7,11,13,17,19,23,29\), tests whether the restricted quartic is a square, and independently extracts rational versus quadratic contact divisors from the binary discriminant. Its second route constructs both quadratic radicals and all \(28\) distinct bitangents in \(\mathbb F_{p^2}\), tests the discriminant's square class there, and verifies the inferred cycle decomposition including the six degree-four cycles. It confirms both the complete \(n_1,n_2,n_4\) census and the closed formula for the number of parameters with degree-four contacts. The program prints `CIANI_CONTACT_SUPPORT_FROBENIUS_VERIFIED`. Enumerations support, but do not replace, the preceding uniform proof.

## Relationship to prior work
Janasz–Pokora–Zieliński (2023) study this exact symmetric pencil and complex bitangent incidence. Bethea–Brazelton (2024) give the geometric orbit structures. An already published published-finding corpus classification establishes all \(28\) geometric bitangent lines, their quadratic descent, and the complete \(4/16/28\) **line** counts, explicitly without classifying rational contact divisors. A separate published finite census classifies rational bitangent contact types for the entire six-coefficient Ciani family only over \(\mathbb F_5\). The result here is different: it determines every *geometric contact support* and its Frobenius orbit degree for every smooth symmetric-pencil parameter over every characteristic at least five, and proves when degree-four contacts occur. In particular, knowing that a bitangent line descends to \(\mathbb F_{q^2}\) does not imply its two contacts descend to that field.

## Limitations
The scheme is the reduced contact support, not the length-\(56\) scheme with repeated hyperflex contacts. This is not a statement about rational points of the entire quartic or abstract curve isomorphism classes. Characteristic three is not covered. An alternative unpublished or unindexed contact-descent calculation could affect historical priority. External independent mathematical audit has not been performed.

## References
- M. Janasz, P. Pokora, M. Zieliński, *On arrangements of smooth plane quartics and their bitangents*, arXiv:2308.16514, first posted 2023-08-31, Section 3, https://arxiv.org/abs/2308.16514 .
- C. Bethea, T. Brazelton, *Bitangents to symmetric quartics*, arXiv:2410.09242, first posted 2024-10-11, Section 4.4, https://arxiv.org/abs/2410.09242 .
- *Quadratic Frobenius splitting and an exact rational-bitangent census for Ciani's quartic pencil*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-quadratic-frobenius-splitting-and-an-exact-rational-bitangent-ce--94af6b732234 .
- *Rational bitangent-contact spectrum of smooth Ciani quartics over \(\mathbb F_5\)*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-rational-bitangent-contact-spectrum-of-smooth-ciani-quartics-ove--86374f95f5d5 .
