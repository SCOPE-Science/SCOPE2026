# Exact Beatty coding of odd elliptic multiples giving rational \(\Delta\)-triples

## Finding
Fix coprime integers \(a>b\ge1\), write \(s=a+b\), and consider
\[E_{a,b}:Y^2=ab\,w(w+ab)(w+s^2),\qquad P=(-bs,ab^2s).\]
Define the explicit complete- and incomplete-period ratio, with \(u=a/b\),
\[\beta=\beta(u)=\frac{\displaystyle\int_u^{u+1}\frac{dt}{\sqrt{t(t-u)((u+1)^2-t)}}}{\displaystyle\int_u^{(u+1)^2}\frac{dt}{\sqrt{t(t-u)((u+1)^2-t)}}}.\]
For each integer \(k\ge0\), put \(Q_k=(2k+1)P\) in the ordinary elliptic-curve group law and set \(I_k=1\) precisely if the affine coordinate \(w(Q_k)\) satisfies \(-bs<w(Q_k)<-ab\), and \(I_k=0\) otherwise. Then \(\beta\) is irrational, \(0<\beta<1\), and
\[\boxed{I_k=\lfloor(k+1)\beta\rfloor-\lfloor k\beta\rfloor\quad(k\ge0).}\]
Consequently the exact number of successful positions \(0\le k<K\) is \(\lfloor K\beta\rfloor\) for every integer \(K\ge0\), with discrepancy strictly smaller than one. The successful odd indices are exactly
\[\boxed{\bigl\{2\lfloor m/\beta\rfloor+1:m\in\mathbb Z_{\ge1}\bigr\}.}\]
Their successive gaps, measured in the \(k\)-index, take only the two values \(\lfloor1/\beta\rfloor\) and \(\lceil1/\beta\rceil\). The first successful multiple is \((2\lfloor1/\beta\rfloor+1)P\).

## Assumptions and scope
The curve has standard identity \(O\) at infinity. The point \(P\) is rational and on the bounded real component. The rational \(\Delta\)-triple criterion is the one in Schvöllner: a rational point on \(E_{a,b}\) with \(-bs<w<-ab\) and positive ordinate gives a rational triple satisfying \(x<y\le z<1\), \(1/x-x=(1/y-y)+(1/z-z)\), and \(z/y=a/b\); clearing rational denominators gives integral \(\Delta\)-triples for some perfect square. If a point has negative ordinate, replace it by its elliptic inverse, which retains \(w\) and changes the sign of \(Y\). The theorem identifies the exact indices on this particular orbit; it does not assert all rational triples come from this orbit or determine the least possible perfect square.

## Proof
**1. Invariant arc-coordinate.** Set \(T=(-ab,0)\), one of the order-two points on the bounded oval, and let \(t=-w\), so \(ab\le t\le s^2\) along that oval. Put
\[J=\int_{ab}^{s^2}\frac{dt}{\sqrt{t(t-ab)(s^2-t)}},\qquad F(t)=\int_{ab}^{t}\frac{dv}{\sqrt{v(v-ab)(s^2-v)}}.\]
Define a normalized coordinate \(\theta\) on the oval by \(\theta(Q)=F(-w(Q))/(2J)\) for \(Y(Q)>0\) and \(\theta(Q)=1-F(-w(Q))/(2J)\) for \(Y(Q)<0\), with the continuous values \(0\) and \(1/2\) at \(T\) and \((-s^2,0)\). The differential \(dw/(2Y)\) is invariant under elliptic translation. Its oriented real integral is a real-group coordinate; therefore \(\theta\) is a group isomorphism from the oval endowed with the translated group operation \(Q\star R=Q+R-T\) to \(\mathbb R/\mathbb Z\), after choosing the positive orientation. This assertion also follows by integrating the translation-invariant differential around the oval: its total period is \(J/\sqrt{ab}\), and the preceding definition divides by that period. As \(T\) has order two, every odd ordinary multiple of \(P\) equals the corresponding odd multiple in the shifted group based at \(T\).

**2. The phase and the window.** Since \(P=(-bs,ab^2s)\) has positive ordinate, \(\theta(P)=F(bs)/(2J)=\beta/2\); the ratio becomes the displayed expression for \(\beta(u)\) after the change of variables \(t=b^2v\). Consequently
\[\theta(Q_k)\equiv(2k+1)\beta/2\equiv k\beta+\beta/2\pmod1.\]
The strict window \(ab<t<bs\) consists of the two arcs
\[(0,\beta/2)\cup(1-\beta/2,1)\quad\text{in }\mathbb R/\mathbb Z.\]
Schvöllner's Lemma 7.1(3) proves that \(P\) has infinite order whenever \(a>b\); because \(T\) has order two, the group coordinate \(\beta/2\) is irrational, so \(\beta\) is irrational. In particular, none of the orbit's later phases is a boundary point: for \(k\ge1\), neither \(\{k\beta\}=0\) nor \(\{k\beta\}=1-\beta\) can occur. At \(k=0\), \(Q_0=P\) is at the window endpoint and fails. For every \(k\ge0\) the phase therefore lies in the window exactly when \(\{k\beta\}>1-\beta\), which is equivalent to
\[\lfloor(k+1)\beta\rfloor-\lfloor k\beta\rfloor=1.\]
This establishes the claim with exact endpoint conventions.

**3. Exact counting and indices.** Summing the successive floor differences telescopes to \(\lfloor K\beta\rfloor\). Because \(\beta\) is irrational, the \(m\)-th unit jump occurs at \(k=\lfloor m/\beta\rfloor\) for \(m\ge1\). Its ordinary elliptic multiplier is \(2k+1\). The two-gap statement follows by differencing consecutive floor terms of \(m/\beta\). No asymptotic averaging or unproved equidistribution rate is used.

## Verification
A stand-alone standard-library Python file, `artifacts/verify.py`, recomputes exact rational additions on the Weierstrass model \(V^2=u(u+a^2b^2)(u+ab(a+b)^2)\), where \(u=ab w\) and \(V=abY\), and compares the strict-window test with the Beatty floor expression. For eight coprime parameter pairs and seventeen successive odd multiples each, all 136 comparisons passed. The elliptic integrals in the finite test are evaluated by a desingularizing sine substitution and composite Simpson quadrature; this numerical sampling does **not** prove the theorem, whose infinite statement follows from the differential/group argument above.

## Relationship to prior work
Schvöllner [1, Sections 4, 6, 7] supplies the elliptic model, the exact open window, the canonical point \(P\), its infinite order for \(a>b\), and the fact that infinitely many odd multiples enter that window. The present result identifies the actual successful odd indices and all finite-prefix counts, not merely their infinitude. General circle rotations and Beatty/mechanical words are classical: the specific integral rotation number, phase alignment with the canonical degenerate point, and resulting zero-intercept floor formula make this an explicit arithmetic coding for the \(\Delta\)-triple construction. Golfieri–Schvöllner [2] concerns \(\Delta\)-primitive squares via Pell equations, without coding odd elliptic multiples.

## Limitations
The result does not give the heights or minimal denominators of the triples, their distinct primitive integral representatives, or the smallest square carrying a fixed quotient. Numerical tests cover only the listed parameter cases. The closest literature was compared on statements and implication; an equivalent observation outside the inspected/indexed material cannot be excluded without independent expert literature review.

## References
[1] V. N. Schvöllner, *Encoding rational \(\Delta\)-triples on elliptic curves*, arXiv:2611.14803v1 (first public version 2026-11-10), Sections 4, 6–7. https://arxiv.org/abs/2611.14803

[2] F. Golfieri and V. N. Schvöllner, *On the \(\Delta\)-primitive squares conjecture*, arXiv:2611.11574v1 (2026-11-08). https://arxiv.org/abs/2611.11574
