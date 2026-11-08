# A sharp three-critical-point ceiling for four-periodic geometric shift tests

## Finding
For every real \(a,b,c>0\) and \(0<d<1\), consider the geometric-vector trial function
\[
F(z)=\frac{(1-z)\sqrt z\,(1+az+bz^2+cz^3)}{1-dz^4},\qquad 0<z<1.
\]
Its derivative has **at most three zeros in \((0,1)\), counted with multiplicity**, and it has either one or three zeros counted with multiplicity. All critical points lie in \((1/3,1)\); hence \(F\) has **at most two local maxima**, so evaluation at at most two candidates obtains its exact maximum. The ceiling of three is sharp: the choice
\[
(a,b,c,d)=(1/1000,1/1000,73/100,49/50)
\]
has exactly three distinct simple critical points in \((1/3,1)\), with two local maxima separated by a local minimum.

## Assumptions and scope
Let \(T\) be the unilateral weighted shift on \(\ell^2(\mathbb N_0)\) with weights
\[
(w_{4k},w_{4k+1},w_{4k+2},w_{4k+3})=d^k(1,a,b,c),\quad k\ge0.
\]
For the unit vector \(x(z)=(\sqrt{1-z}\,z^{n/2})_{n\ge0}\), the Rayleigh quotient is exactly \(\langle Tx(z),x(z)\rangle=F(z)\). Thus \(\max_{0\le z\le1}F(z)\) is a computable lower bound for the numerical radius of \(T\). The finding concerns this particular **geometric-vector lower bound** only: it does not identify the full operator numerical radius or its maximizing vectors.

Zeros and their multiplicities refer to the ordinary real-analytic derivative on \((0,1)\). The function extends continuously by zero to both endpoints, and is strictly positive in the interior.

## Proof
Put \(P(z)=1+az+bz^2+cz^3\). Direct differentiation shows that \(F'(z)\) has the sign of
\[
G(z)=(1-3z)P(z)(1-dz^4)+2z(1-z)P'(z)(1-dz^4)+8dz^4(1-z)P(z),
\]
more precisely \(F'(z)=G(z)/(2\sqrt z(1-dz^4)^2)\).

First, all critical points lie above \(1/3\). Indeed, \(F\) is a strictly positive linear combination of the four functions
\[
h_j(z)=\frac{(1-z)z^{j+1/2}}{1-dz^4},\quad j=0,1,2,3.
\]
For \(0<z\le1/3\), their logarithmic derivatives are
\[
\frac{h_j'(z)}{h_j(z)}=\frac{j+1/2}{z}-\frac1{1-z}+\frac{4dz^3}{1-dz^4}>0.
\]
Moreover \(G(0)=1>0\) and \(G(1)=-2(1-d)(1+a+b+c)<0\), so at least one critical point exists in \((1/3,1)\).

Now make the monotone substitution \(v=z/(1-z)\), mapping \((0,1)\) bijectively onto \((0,\infty)\). The polynomial
\[
Q(v)=(1+v)^8G\bigl(v/(1+v)\bigr)=\sum_{j=0}^{8}B_jv^j
\]
has coefficients
\[
\begin{aligned}
 B_0&=1,\\
 B_1&=5+3a,\\
 B_2&=7+16a+5b,\\
 B_3&=-7+33a+23b+7c,\\
 B_4&=-35+30a+40b+26c+7d,\\
 B_5&=-49+(5+5d)a+30b+34c+23d,\\
 B_6&=-35+(12d-12)a+(5+3d)b+16c+27d,\\
 B_7&=(d-1)(13+9a+5b+c),\\
 B_8&=2(d-1)(1+a+b+c).
\end{aligned}
\]
Here \(B_0,B_1,B_2>0\) and \(B_7,B_8<0\). The only potentially five-change sign sequence would require \(B_3<0\) and \(B_4>0\). That transition is impossible, as the exact identity
\[
B_4-\frac{26}{7}B_3=-9+7d-\frac{648}{7}a-\frac{318}{7}b<-2
\]
shows that \(B_3\le0\) forces \(B_4<0\). If \(B_3>0\), the remaining four slots \(B_4,B_5,B_6,B_7\) can contribute at most three sign changes; if \(B_3\le0\), \(B_4<0\) and the total is likewise at most three. Deleting any zero coefficients cannot increase these bounds. Descartes' rule of signs therefore gives at most three positive roots, counted with multiplicity, of \(Q\), hence of \(G\) on \((0,1)\). The opposite endpoint signs make the total positive-root multiplicity odd, hence equal to one or three.

For sharpness, take the rational parameters displayed above. Direct exact evaluation gives the signs
\[
G(1/2)>0,\quad G(3/5)<0,\quad G(3/4)>0,\quad G(9/10)<0.
\]
The intermediate value theorem yields three distinct zeros, and the just-proved global bound shows that these are the only zeros and are all simple. Their signs alternate from positive to negative to positive to negative, giving exactly two strict local maxima separated by one strict local minimum.

## Verification
The accompanying `verify.py` (requiring SymPy) expands all nine transformed polynomial coefficients, checks the critical coefficient inequality as a symbolic identity, and checks the six rational endpoint/witness evaluations with exact arithmetic. Running `python verify.py` prints `SHARP_THREE_CRITICAL_POINT_CEILING_VERIFIED`. These checks support the displayed algebra; the uniform bound comes from the Descartes argument, not from parameter sampling.

## Relationship to prior work
Ghosh, Birbonshi and Ojha (2026) introduce the geometric-vector bound for the narrower shift with \(a=sq\), \(b=q^2\), \(c=tq^3\), \(d=q^4\), prove uniqueness of its critical point in a restricted parameter regime, and pose unrestricted uniqueness. A subsequent public resolution supplies uniqueness for the whole narrower family. A related previously described sufficient condition \(b\ge\sqrt d\) in the broader four-weight family also covers that narrower case. **None of those uniqueness statements is claimed here.**

The contribution is the sharp *global cap of three* critical points **without** any restriction linking \(b\) and \(d\), or limiting \(a,c\). This is compatible with the known existence of three-critical-point examples, which alone does not establish that four or more can never occur. The maximal count constrains the geometry of the geometric-vector optimization problem uniformly over the enlarged family.

## Limitations
The result does not classify the parameter regions with one versus three critical points, give a closed radical formula for the critical positions, or determine the actual numerical radius of the weighted shift. The three-critical-point witness is not asserted to be new by itself. No general claim is made for period lengths other than four, complex/negative weights, or \(d\ge1\). The literature comparison is best-knowledge and is not independent publication-priority validation.

## References
1. A. Ghosh, R. Birbonshi, and S. Ojha, *On the numerical radius of a class of weighted shift operators*, arXiv:2608.17486v1 (first public 2026-08-18), Sections 1--3. https://arxiv.org/abs/2608.17486v1
2. *Ghosh, Birbonshi and Ojha: the unique polynomial root*, public mathematical result and scope assessment, https://www.trureturing.org/research/ghosh-birbonshi-ojha-2026-weighted-shift-root-uniqueness/ (read 2026-11-05).
