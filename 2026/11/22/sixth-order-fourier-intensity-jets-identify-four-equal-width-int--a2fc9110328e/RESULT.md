# Sixth-order Fourier-intensity jets identify four equal-width intervals

## Finding
Let \(\Omega\subset\mathbb R\) be the union of exactly four closed intervals with a common, initially unknown length \(a>0\) and strictly positive gaps:
\[
\Omega=\bigcup_{j=1}^4[x_j,x_j+a],\qquad
x_1<x_2<x_3<x_4,\quad x_{j+1}-x_j>a.
\]
With the angular Fourier convention \(\widehat f(t)=\int_{\mathbb R}f(x)e^{-itx}\,dx\), define its squared Fourier intensity \(I(t)=|\widehat{\mathbf 1_\Omega}(t)|^2\). Then the four real numbers
\[
\boxed{\quad I(0),\ I''(0),\ I^{(4)}(0),\ I^{(6)}(0)\quad}
\]
**uniquely determine all four interval positions up to translation and reflection**, among all unions of exactly four equally long strictly separated intervals. Sixth order is sharp: the complete intensity jet of order at most five fails to be injective on this class, even when the common width is known.

An explicit inverse uses one physically admissible root of a cubic. Recover \(a=\sqrt{I(0)}/4\) and put
\[
J(t)=\frac{I(t)}{a^2\operatorname{sinc}^2(at/2)},\qquad \operatorname{sinc}(z)=\frac{\sin z}{z},\quad \operatorname{sinc}(0)=1.
\]
For \(k=1,2,3\), compute
\[
M_{2k}=\frac{(-1)^k}{2}J^{(2k)}(0),\qquad
E=\frac{M_2}{4},\quad F=\frac{M_4}{4},\quad G=\frac{M_6}{4}.
\]
There is exactly one *physically admissible* real root \(P\) of
\[
\boxed{\quad 156P^3-156EP^2+39FP+16E^3-15EF-G=0.\quad}
\]
Set
\[
W=E-2P,\quad Q=\frac{E^2+2EP-3P^2-F}{4},
\]
\[
U=\frac{P+\sqrt{P^2-4Q}}2,\qquad
V=\frac{P-\sqrt{P^2-4Q}}2.
\]
The four starts, after translation, are
\[
\boxed{\{-\sqrt U,\ \sqrt W-\sqrt V,\ \sqrt W+\sqrt V,\ \sqrt U\}.}
\]
Replacing \(\sqrt W\) by \(-\sqrt W\) yields the reflected set. Physical admissibility means \(U>V>0\), \(W\ge0\), and the three consecutive start gaps \(\sqrt U-\sqrt V\pm\sqrt W\) and \(2\sqrt V\) all exceed \(a\). If \(W=0\), the reflection alternatives coincide.

## Assumptions and scope
All widths and gaps are strictly positive. Only four-interval equal-width *competitors* are considered; the data are noiseless derivatives at frequency zero, not discrete Fourier samples. The inverse provides no condition number or uniform noisy stability assertion. Intensity is even and real, so all odd derivatives vanish.

## Proof
**Reduction to six distances.** The common rectangle Fourier transform factors exactly:
\[
I(t)=a^2\operatorname{sinc}^2(at/2)
\left|\sum_{j=1}^4e^{-itx_j}\right|^2.
\]
Hence \(I(0)=16a^2\) and, near zero, \(J(t)=4+2\sum_{i<j}\cos(t(x_j-x_i))\). Differentiating proves the stated formulas for \(M_2,M_4,M_6\). In particular no arbitrary phase choice enters the reconstruction.

**Ordered geometric coordinates.** Translate by the midpoint of the outermost starts and write the ordered start coordinates uniquely as
\[
-S,\quad m-T,\quad m+T,\quad S,
\]
with \(S>T>0\) and \(|m|<S-T-a\); moreover \(2T>a\). Let \(U=S^2\), \(V=T^2\), \(W=m^2\), \(P=U+V\), \(Q=UV\). The six positive pairwise distances are
\[
2S,\quad2T,\quad S+m+T,\quad S+m-T,\quad S-m+T,\quad S-m-T.
\]
Expanding their even powers gives the three exact polynomial identities
\[
E=2P+W,
\]
\[
F=5P^2-4Q+W^2+6PW,
\]
\[
G=17P^3-36PQ+W^3+15WP^2+15W^2P+60WQ.
\]
The expressions for \(W\) and \(Q\) follow by solving the first two identities. Eliminating them from the third gives
\[
G=16E^3-15EF+39FP-156EP^2+156P^3,
\]
which is precisely the proposed cubic.

**Uniqueness on the physical domain.** Write \(H(P)=16E^3-15EF+39FP-156EP^2+156P^3\). An exact differentiation gives
\[
H'(P)=39D(P),\qquad D(P)=F-8EP+12P^2.
\]
For every physically realizable solution, \(|m|<S-T\), so \(W<(\sqrt U-\sqrt V)^2=P-2\sqrt Q\). Consequently
\[
P>\frac E3,\qquad
D(P)=(P-W)^2-4Q>0.
\]
Two further polynomial identities imply
\[
4E^2-3F=(P-W)^2+12Q>0,
\qquad D(E/3)=F-\frac43E^2<0.
\]
The derivative \(D'(P)=24P-8E\) is strictly positive for all \(P>E/3\). It follows that \(D\) has a single zero \(r>E/3\) and \(H\) is strictly increasing for every \(P>r\). Every physically realizable \(P\) belongs to that increasing branch, and therefore no two physically realizable solutions can produce the same \((E,F,G)\). The recovered \(U,V\) are ordered uniquely; the sign of \(m\) is the unavoidable reflection ambiguity. This proves global injectivity.

**Sharpness of derivative order.** Fix \(a=1/4\) and the ordered start points \(\{-5,0,2,5\}\). Their coordinates have \((P,Q,W)=(26,25,1)\), and hence \((E,F)=(53,3437)\). For a second geometry prescribe
\[
P'=\frac{2599}{100},\quad
W'=\frac{51}{50},\quad
Q'=\frac{1004997}{40000}.
\]
Then \(E'=2P'+W'=53\) and \(F'=5(P')^2-4Q'+(W')^2+6P'W'=3437\). The second geometry has the starts
\[
-\sqrt{U'},\quad \sqrt{W'}-\sqrt{V'},\quad
\sqrt{W'}+\sqrt{V'},\quad \sqrt{U'},
\]
where \(U'=(P'+\sqrt{(P')^2-4Q'})/2\) and \(V'=(P'-\sqrt{(P')^2-4Q'})/2\). All three start gaps strictly exceed \(1/4\) (indeed, each exceeds \(1\)). For an exact margin certificate, direct squaring gives \(U'>2401/100\), \(1/4<V'<121/100\), and \(0<W'<121/100\). Thus the two outer start gaps are greater than \(49/10-11/10-11/10=27/10\), while the middle gap is greater than \(1\). The two geometries are not translates or reflections because \(P'\ne P\). Their \(a,E,F\) are identical, so their jets through order four are identical; every odd derivative vanishes. Thus no derivative order below six is universally sufficient.

## Verification
Execute `python CHECK.py` in the same directory using Python 3 and SymPy. The checker reproduces all three six-distance power identities, the cubic elimination, the derivative-sign identity, the positivity identity and the explicit two-geometry fourth-order collision. It additionally independently expands the analytic Fourier intensity through sixth order and checks 500 rational parameter configurations. The observed output was `FOUR_INTERVAL_SIXTH_JET_CHECKS_PASSED`. The finite tests corroborate the identities; global uniqueness and sharpness follow from the preceding exact inequalities and explicit configurations, not from random sampling.

## Relationship to prior work
Xia and Xu (2026) study one-dimensional phase retrieval of finite interval unions and show generic unrestricted higher-component ambiguities, providing the recent motivation. Their publicly accessible abstract does not state a finite-jet theorem for four equal-width intervals; full text could not be inspected for this comparison and remains a bibliographic risk. The full-data homometry theorem in *Equal-width interval diffraction reduces exactly to finite point-set homometry* (published-finding corpus, 2026-10-18) reduces complete intensity equality to finite point sets, but does not imply injectivity of the **three specific distance moments** \(M_2,M_4,M_6\). *Sixth-order Fourier-intensity recovery for three equal-width intervals* (published-finding corpus, 2026-11-08) treats only three intervals, with two spacing parameters; its polynomial identities and inference do not cover four intervals, with three spacing parameters and a distinct cubic monotonicity mechanism. Related three-moment identification results for two-dimensional parallelograms concern area-uniform Euclidean distance distributions rather than collinear four-point data, and no implication was found.

## Limitations
Competitors must consist of exactly four equal-width disjoint intervals. The theorem makes no claim about arbitrary unequal-width unions, additive noise, finite-frequency sampling, or general turnpike sets with more points. It does not provide a uniform stability constant near gaps that vanish or near repeated roots of the inverse polynomial. Although the cited accessible literature does not show the exact four-interval sixth-jet statement, older unindexed moment and inverse-problem identities and the unavailable full 2026 motivating preprint remain a residual originality risk. Independent audit has not been performed.

## References
1. Yu Xia and Zhiqiang Xu, *Fourier Phase Retrieval for Finite Unions of Intervals*, arXiv:2606.19855, first public submission 2026-06-18. https://arxiv.org/abs/2606.19855
2. *Sixth-order Fourier-intensity recovery for three equal-width intervals*, published-finding corpus public record 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sixth-order-fourier-intensity-recovery-for-three-equal-width-int--df0589a6cbc2
3. *Equal-width interval diffraction reduces exactly to finite point-set homometry*, published-finding corpus public record 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-equal-width-interval-diffraction-reduces-exactly-to-finite-point--417f34275d33
