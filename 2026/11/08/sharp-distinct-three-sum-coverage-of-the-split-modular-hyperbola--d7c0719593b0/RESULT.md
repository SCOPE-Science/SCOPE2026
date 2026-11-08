# Sharp distinct three-sum coverage of the split modular hyperbola

## Finding

Let \(F=\mathbb F_q\) have characteristic at least five, and define the split modular hyperbola
\[
H_q=\{(u,u^{-1}):u\in F^\times\}\subset F^2.
\]
For \((s,t)\in F^2\), define \(R_q(s,t)\) as the number of **ordered** triples \((x,y,z)\in(F^\times)^3\) with pairwise distinct entries and
\[
x+y+z=s,\qquad x^{-1}+y^{-1}+z^{-1}=t.
\]
Write \(\chi\) for the quadratic character on \(F\), extended by \(\chi(0)=0\), and let \(c=st\). The exact formula for every field and target in the stated scope is
\[
R_q(s,t)=
\begin{cases}
2(q-1),&(s,t)=(0,0),\ 3\mid(q-1),\\
0,&(s,t)=(0,0),\ 3\nmid(q-1),\\
3(q-3),&c=1,\\
q-6-\chi(-3),&c=9\ \text{or}\ (c=0,\ (s,t)\ne(0,0)),\\
q+\sum_{u\in F}\chi(D_{s,t}(u))-4-3(1+\chi((c-1)(c-9))),&c\notin\{0,1,9\},
\end{cases}
\]
where
\[
D_{s,t}(X)=(tX-1)(s-X)\big((tX-1)(s-X)-4X\big).
\]
Thus for every \(q\ge23\), the **restricted threefold sumset**, using distinct summands, is exactly
\[
H_q\mathbin{\widehat+}H_q\mathbin{\widehat+}H_q=
\begin{cases}
F^2,&q\equiv1\pmod3,\\
F^2\setminus\{(0,0)\},&q\equiv2\pmod3.
\end{cases}
\]
The uniform lower bound \(q\ge23\) is sharp. For every smaller allowed field order a nonzero target is missed: \((s,t)=(1,0)\) for \(q=5,7\); \((1,2)\) for \(q=11\); \((1,3)\) for \(q=13\); \((1,4)\) for \(q=17\); and \((1,3)\) for \(q=19\). The exact missing-target counts for these six fields are respectively \(21,36,41,48,49,18\); the supplied verifier exhaustively checks them.

## Assumptions and scope

All field operations take place in \(\mathbb F_q\). The characteristic is at least five, so \(2\) and \(3\) are invertible and \(q\) is odd with \(3\nmid q\). All three parameters \(x,y,z\) are nonzero and pairwise distinct; this restriction is indispensable. The character formula, including exceptional cases, holds for every \(q\) in scope, not only \(q\ge23\). No statement is made for characteristics two or three. An ordinary sumset allowing repeated points is a different object.

## Proof

**1. Reduction to a quartic.** Fix \((s,t)\) with \(st\notin\{0,1,9\}\), so \(s,t\ne0\). Choosing \(x\), the remaining equations imply
\[
y+z=s-x,\qquad yz=\frac{x(s-x)}{tx-1},
\]
provided \(x\ne0,s,t^{-1}\). The discriminant of the quadratic with roots \(y,z\) is
\[
(y-z)^2=(s-x)^2-\frac{4x(s-x)}{tx-1}.
\]
Multiplying this discriminant by the square \((tx-1)^2\) produces \(D_{s,t}(x)\). Hence for admissible \(x\), the number of ordered pairs \((y,z)\) before excluding collisions is \(1+\chi(D_{s,t}(x))\).

The two factors \((tx-1)\) and \((s-x)\) give distinct simple roots \(x=t^{-1},s\). The third factor is the quadratic
\[
Q(x)=-tx^2+(st-3)x-s,
\]
with discriminant \(\Delta=(st-1)(st-9)\ne0\). It contributes \(r=1+\chi(\Delta)\in\{0,2\}\) rational simple roots; these are precisely the admissible cases \(y=z\). For the remaining collision \(x=y\) or \(x=z\), substitution gives
\[
G(x)=2t x^2-(st+3)x+2s=0,
\]
whose discriminant is also \(\Delta\), hence it has \(r\) roots. Each such root contributes two forbidden ordered pairs. The excluded places \(x=0,s,t^{-1}\) contribute respectively \(2,1,1\) to the unrestricted character count. The \(G\)-roots cannot coincide with the \(Q\)-roots: a coincidence would force \(x=y=z\) and hence \(st=9\), contrary to the hypothesis. They do not equal \(0,s,t^{-1}\) because \(st\ne1\). Therefore the exact number is
\[
R_q(s,t)=q+\sum_{x\in F}\chi(D_{s,t}(x))-4-3r.
\]
This proves the generic formula, including the collision corrections.

**2. Degenerate target products.** When \(st=1\), the monic cubic whose roots are \(x,y,z\) has \(s\) as a root: writing \(P=xyz\), it factors as \((X-s)(X^2+P/s)\). Thus one entry equals \(s\), and the other two are nonzero opposites. There are \(q-3\) choices for their ordered values and three choices for the position of \(s\), proving \(R_q=3(q-3)\).

If \(s=0,t\ne0\), the quartic factors as \(D_{0,t}(X)=X^2(tX-1)(tX+3)\). The standard quadratic-character identity for a quadratic with distinct roots gives
\[
\sum_{x\in F}\chi(D_{0,t}(x))=-1-\chi(-3).
\]
From the \(q+\sum\chi(D)\) candidate pairs, remove one at each of \(x=0,t^{-1},-3t^{-1}\), plus two at \(x=3/(2t)\) (a repeated parameter). The total subtraction is five, yielding \(q-6-\chi(-3)\). Inverting the three parameters exchanges \(s\) and \(t\), so the same result holds when \(t=0,s\ne0\).

If \(st=9\), the quadratic \(Q\) has a double root \(x=s/3=3/t\). Here
\[
D_{s,t}(x)=t^2(x-t^{-1})(x-s)(x-s/3)^2,
\]
so the character sum is again \(-1-\chi(-3)\). Subtract contributions \(2,1,1\) at \(x=0,s,t^{-1}\), and one at \(x=s/3\), where all parameters coincide. This again yields \(q-6-\chi(-3)\).

Finally, \(s=t=0\) forces the roots \(x,y,z\) of their cubic to satisfy \(X^3=xyz\). Distinct nonzero roots exist exactly when \(F\) contains the nontrivial cube roots of unity, i.e. \(3\mid q-1\). In that case each nonzero \(x\) has two orderings of the other entries, proving \(2(q-1)\); otherwise the count is zero.

**3. Elliptic bound and sharpness.** In the generic case \(D_{s,t}\) is squarefree of degree four and has leading coefficient \(t^2\), a square. The smooth projective completion of \(Y^2=D_{s,t}(X)\) is a genus-one curve \(E_{s,t}\) with exactly two rational points at infinity. Setting \(a_{s,t}=q+1-\#E_{s,t}(F)\), Hasse's bound yields \(|a_{s,t}|\le2\sqrt q\) and
\[
q+\sum_{x\in F}\chi(D_{s,t}(x))=q-1-a_{s,t}.
\]
Consequently
\[
R_q(s,t)=q-8-3\chi(\Delta)-a_{s,t}\ge q-11-2\sqrt q>0\quad(q\ge23).
\]
All exceptional nonzero target counts are also positive for \(q\ge23\), while the origin condition was proved above. This proves the exact restricted sumset statement. For each \(q<23\) of characteristic at least five, the explicit missed nonzero target listed in the finding is confirmed by finite exhaustive enumeration in the verifier; since such fields are prime fields, this completes the sharp threshold proof.

## Verification

Run `python3 verify_hyperbola.py` with Python 3. The program constructs all unordered triples of distinct nonzero field elements, converts them to ordered multiplicities, and compares every target with the separately computed character formula, including all exceptional branches. It tests the seventeen prime fields \(q=5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67\) and quadratic extensions \(q=25,49,121\), totaling \(42,620\) target fibers. All tests passed. The program separately checks the predicted missing-target count for each tested \(q\ge23\). This finite verification does not replace Hasse's bound or the symbolic collision count, which prove the universal statement.

## Relationship to prior work

The original 2012 study by Bower, Evans, Luo and Miller defines **coordinate** sumsets of modular hyperbolas, and its Theorem 4.1 treats sums of coordinates subject to a fixed multiplicative product; it does not study three distinct points of the inverse graph with both coordinate sums prescribed. Zhao's 2014 restricted-sumset theorem bounds scalar sums of distinct elements from field subsets, not two simultaneous coordinates of a nonlinear graph. An earlier unrestricted threefold hyperbola coverage result admits repeated points and gives a different, lower field-size threshold; it does not imply the sharp distinct-summand threshold or the exact fiber formula here. These distinctions are by mathematical implication, not by title alone.

## Limitations

Characteristics two and three are excluded. The exact generic count involves an elliptic-curve trace and is not an elementary closed expression solely in \(q\) and \(st\). The cited comparisons do not establish exhaustive historical priority: an unknown specialized restricted-hyperbola theorem might cover some or all claims. The finite enumerations prove only the stated tested cases, while the general theorem relies on the displayed algebra and Hasse's theorem.

## References

1. A. Bower, R. Evans, V. Luo and S. J. Miller, *Coordinate sum and difference sets of d-dimensional modular hyperbolas*, arXiv:1212.2930v1 (first public version 2012-12-12), especially definitions and Theorem 4.1. https://arxiv.org/abs/1212.2930
2. L. Zhao, *On restricted sumsets over a field*, arXiv:1402.3383v1 (first public version 2014-02-14), especially Theorems 1.2–1.4. https://arxiv.org/abs/1402.3383
3. H. Hasse, the classical bound \(|\#E(\mathbb F_q)-(q+1)|\le2\sqrt q\) for elliptic curves over finite fields.
