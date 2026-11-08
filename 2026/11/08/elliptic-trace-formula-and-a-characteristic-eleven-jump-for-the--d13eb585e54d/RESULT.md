# Elliptic-trace formula and a characteristic-eleven jump for the sextic finite-field graph

## Finding
Let \(F=\mathbb F_q\) be any finite field of characteristic \(p>5\), and let \(\chi\) denote its quadratic character, with \(\chi(0)=0\). For the sextic graph
\[
C_6=\{(t,t^6):t\in F\}\subset F^2,
\]
write \(E(C_6)\) for its ordered additive energy, the number of quadruples \((a,b,c,d)\in F^4\) satisfying \(a+b=c+d\) and \(a^6+b^6=c^6+d^6\). Define
\[
\begin{aligned}
T_1&=\sum_{u\in F}\chi\bigl(-3u(u^2+10u-55)\bigr),\\
T_2&=\sum_{z\in F}\chi\bigl(15z(11z^2+26z+11)\bigr),\\
I&=2\#\{r\in F:r^4+10r^2+5=0\},\\
g&=\gcd(6,q-1),\qquad d=\chi(-3).
\end{aligned}
\]
Then the **exact energy** is
\[
\boxed{E(C_6)=1+(q-1)g+(q-1)(3q-2-2d+2T_1+T_2-I).}\tag{1}
\]
When \(p\ne11\), both character sums are traces of smooth elliptic curves: if
\[
\mathcal A:\ y^2=-3u(u^2+10u-55),\qquad
\mathcal B:\ y^2=15z(11z^2+26z+11),
\]
then \(T_i=\#\mathcal E_i(F)-(q+1)\) for \(\mathcal E_1=\mathcal A\), \(\mathcal E_2=\mathcal B\). In particular \(|T_i|\le2\sqrt q\), \(0\le I\le8\), and \(E(C_6)=3q^2+O(q^{3/2})\), uniformly over prime powers of characteristic greater than five other than eleven.

In characteristic eleven the elliptic curves degenerate, and (1) simplifies **for every \(q=11^m\)** to
\[
\boxed{E(C_6)=1+(q-1)\bigl(4q-13-2(-1)^m+\gcd(6,q-1)\bigr).}\tag{2}
\]
Consequently, along field extensions of fixed characteristic eleven, \(E(C_6)/q^2\to4\), whereas in every other fixed characteristic \(p>5\) it tends to \(3\).

For any nontrivial additive character \(\psi\) of \(F\), the normalized constant-input finite-field Fourier extension
\[
\mathcal E1(X,Y)=q^{-1}\sum_{t\in F}\psi(Xt+Yt^6)
\]
satisfies the exact fourth-moment identity
\[
\boxed{\sum_{X,Y\in F}|\mathcal E1(X,Y)|^4=E(C_6)/q^2.}\tag{3}
\]
Thus the characteristic-eleven jump is also a sharp **constant-input** fourth-moment distinction; no unrestricted extension-operator norm is asserted.

## Assumptions and scope
The theorem applies to every prime-power \(q\) with characteristic strictly greater than five, including extensions and characteristic eleven. Addition and multiplication, quadratic characters, and polynomial roots are taken in \(F\), not merely in its prime subfield. Energies count *ordered* quadruples. The curves above have one rational point at infinity and are nonsingular for \(p>5\), \(p\ne11\). Characteristic eleven is explicitly treated as a singular special case rather than subjected to an incorrect elliptic Hasse estimate.

## Proof
Fix the common first-coordinate sum \(s=a+b=c+d\) and let \(E_s\) be the number of corresponding ordered collisions. For \(s=0\), putting \(b=-a\), \(d=-c\) gives \(2a^6=2c^6\). In the multiplicative group \(F^\times\), the sixth-power map has kernel of order \(g=\gcd(6,q-1)\). Its zero fiber has size one, so
\[
E_0=1+(q-1)g.\tag{4}
\]

For \(s\ne0\), put \(h=s/2\) and uniquely parameterize \(a=h(1+r)\), \(b=h(1-r)\), \(c=h(1+t)\), \(d=h(1-t)\). The sixth-power sum is
\[
a^6+b^6=2h^6(1+15r^2+15r^4+r^6).
\]
Since \(2h^6\ne0\), equality is equivalent to
\[
(r^2-t^2)\underbrace{\bigl(r^4+r^2t^2+t^4+15(r^2+t^2)+15\bigr)}_{P(r,t)}=0.\tag{5}
\]
The equation \(r^2=t^2\) has exactly \(2q-1\) ordered solutions. The intersection with \(P(r,t)=0\) has exactly \(I\) solutions: on either branch \(t=\pm r\), the remaining equation becomes \(3(r^4+10r^2+5)=0\); because \(5\ne0\), \(r=0\) cannot occur, so each root gives both signs. Denote by \(B\) the number of solutions to \(P(r,t)=0\). Inclusion–exclusion yields
\[
E_s=2q-1+B-I.\tag{6}
\]

We now compute \(B\) without a point-counting black box. Let \(u=r^2\) and \(v=t^2\). Their equation is the conic
\[
D(u,v)=u^2+uv+v^2+15(u+v)+15=0.
\]
For every \(u\), the equation \(r^2=u\) has \(1+\chi(u)\) solutions. Therefore
\[
B=\sum_{D(u,v)=0}(1+\chi(u))(1+\chi(v))
 =\#D+2\sum_D\chi(u)+\sum_D\chi(uv).\tag{7}
\]
For fixed \(u\), the quadratic equation in \(v\) has discriminant
\[
\Delta_u=-3(u^2+10u-55).
\]
Because the discriminant of \(u^2+10u-55\) is \(320\ne0\) for \(p>5\), the standard identity \(\sum_u\chi(u^2+10u-55)=-1\) gives
\[
\#D=q-\chi(-3)=q-d.\tag{8}
\]
Moreover, counting the \(v\)-roots for each \(u\), and using \(\sum_u\chi(u)=0\), gives
\[
\sum_D\chi(u)=\sum_u\chi(u)(1+\chi(\Delta_u))=T_1;\tag{9}
\]
symmetry gives the identical sum for \(v\).

To calculate the final term, any point with \(uv=0\) contributes zero. For \(v\ne0\) write \(u=zv\), so
\[
(z^2+z+1)v^2+15(z+1)v+15=0.\tag{10}
\]
Its discriminant is \(15(11z^2+26z+11)\). When \(z^2+z+1\ne0\), the number of solutions in \(v\) is \(1+\chi(15(11z^2+26z+11))\), and no solution can have \(v=0\). When \(z^2+z+1=0\), the equation becomes linear with one solution, while the same quadratic formula would count two (the discriminant is the nonzero square \(15^2(z+1)^2\)). Hence
\[
\sum_D\chi(uv)=T_2-\sum_{z:z^2+z+1=0}\chi(z).\tag{11}
\]
The two roots, if they exist, are primitive cube roots of unity. In an odd finite field their existence forces \(6\mid(q-1)\), hence both are squares, giving character sum \(2\); otherwise there are no roots. Thus the last sum is \(1+d\), where \(d=\chi(-3)\). Combining (7)–(11),
\[
B=q-1-2d+2T_1+T_2.\tag{12}
\]
Substitution into (6), followed by (4) and the \(q-1\) identical nonzero values of \(s\), proves (1).

For \(p\ne11\), the cubics in \(T_1,T_2\) are squarefree: the first has distinct nonzero roots unless \(11=0\), since \(320\ne0\), and the second has its factor \(z\) disjoint from the quadratic factor unless \(11=0\), while the latter has discriminant \(192\ne0\) in the stated characteristics. Their smooth projective completions are elliptic curves with one rational point at infinity. The elementary relation between character sums and affine points gives \(\#\mathcal E_i(F)=q+1+T_i\). Hasse's elliptic bound therefore gives \(|T_i|\le2\sqrt q\). As \(I\le8\), (1) gives the claimed \(3q^2+O(q^{3/2})\) estimate.

For \(p=11\), the two cubics reduce respectively to \(-3u^2(u-1)\) and \(5z^2\). Directly summing quadratic characters gives \(T_1=-1\), \(T_2=q-1\), and \(d=\chi(-3)=(-1)^m\). The quartic \(r^4+10r^2+5\) has four roots already in \(\mathbb F_{11}\): setting \(y=r^2\), the two solutions are \(y=3,9\), both nonzero squares. Thus \(I=8\), proving (2). Dividing (1), respectively (2), by \(q^2\) and passing to fixed-characteristic extensions gives the asymptotic dichotomy.

Finally expand the fourth power in (3). Summing additive characters over \(F^2\) leaves exactly the two additive-collision constraints. The ambient sum gives \(q^2\) and the four normalized extension factors give \(q^{-4}\), yielding (3).

## Verification
Run `python verify_sextic_energy.py` with Python 3 (standard library only). The independent checker constructs ordered pair-sum histograms directly, sums their squared multiplicities, and separately evaluates the quadratic-character traces, root intersection, and auxiliary quartic count. It tests prime fields of orders \(7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71\) and quadratic extensions of orders \(49,121,169\). Successful completion prints `SEXTIC_GRAPH_EXACT_ENERGY_CHECKS_PASS`. This finite enumeration is corroborative; the preceding argument proves every stated infinite-family claim.

## Relationship to prior work
Mockenhaupt and Tao initiated the finite-field restriction framework and give a general even-moment interpretation through additive representations. Their detailed moment-curve analysis concerns complete moment curves, not the sparse two-coordinate sextic graph here. Iosevich and Koh and Koh and Shen study finite-field extension bounds for quadratic surfaces and general algebraic curves, respectively; their stated bounds and structural criteria do not supply the exact ordered sextic energy or the characteristic-eleven singular jump.

The separately published quartic-graph energy formula follows a discriminant involution and yields a two-branch polynomial expression, whereas the fifth-power-graph two-sum spectrum reduces to conic point counts. Neither formula, nor the inclusion of these powers in a full moment curve, implies equation (1) for the sixth-power graph: the latter has two separate genus-one traces, and its characteristic-eleven specialization has a different quadratic-order leading term. This distinction is one of mathematical statements, not titles or mere exponents.

## Limitations
Characteristics \(2,3,5\) are excluded. No general sharp \(L^2\)-to-\(L^4\) Fourier-extension operator norm, weighted extremizer classification, or complete two-sum representation histogram is claimed. Elliptic Hasse bounds are used only in characteristics other than eleven; the characteristic-eleven formula is obtained directly. Published general algebraic-curve extension theory could contain an implicit comparison not identified here, and obscure earlier character-sum formulas may subsume (1); historical priority has not been independently verified.

## References
1. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234v1, first public 18 April 2002, especially finite-field extension and even-moment counting.
2. A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505v1, first public 28 April 2008.
3. D. Koh and C.-Y. Shen, *Sharp extension theorems and Falconer distance problems for algebraic curves in two dimensional vector spaces over finite fields*, arXiv:1003.4240v1, first public 22 March 2010; Rev. Mat. Iberoam. 28 (2012), 157–178.
4. *Exact additive energy of the finite-field quartic graph*, public mathematical record, 2026: https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-additive-energy-of-the-finite-field-quartic-graph--235f10989b3f.
5. *Complete two-sum spectrum of the finite-field fifth-power graph*, public mathematical record, 2026: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-two-sum-spectrum-of-the-finite-field-fifth-power-graph--f9410cde2e91.
