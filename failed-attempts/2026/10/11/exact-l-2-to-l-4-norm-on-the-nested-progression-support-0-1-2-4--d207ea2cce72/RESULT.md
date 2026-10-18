# Exact \(L^2\)-to-\(L^4\) norm on the nested-progression support \(\{0,1,2,4\}\)
## Finding
For every \(a,b,c,d\in\mathbb C\), let \(P(t)=a+b e^{2\pi i t}+c e^{4\pi i t}+d e^{8\pi i t}\) on \(\mathbb T=\mathbb R/\mathbb Z\). Then the sharp inequality \[\|P\|_{L^4(\mathbb T)}\le C_{0124}\bigl(|a|^2+|b|^2+|c|^2+|d|^2\bigr)^{1/2}\] has \(C_{0124}^4=2+\delta_*\), where \(\delta_*\) is the unique positive root of \[7405408\delta^9+29910288\delta^8+50188768\delta^7+43830564\delta^6+19545666\delta^5+2647793\delta^4-1203370\delta^3-539404\delta^2-84328\delta-6889=0.\] Numerically, \(\delta_*=0.299413862840328\ldots\) and \(C_{0124}=1.231414565773106\ldots\).

The support \(\{0,1,2,4\}\) contains the two nested three-term arithmetic-progression relations \(2\cdot1=0+2\) and \(2\cdot2=0+4\). The sharp constant therefore records the interaction of two overlapping pair-sum collisions, rather than a single-collision correction.

## Assumptions and scope
The circle \(\mathbb T\) has normalized Haar measure. The norm \(\|P\|_4\) is the usual normalized \(L^4(\mathbb T)\) norm. Coefficients are arbitrary complex numbers, with no equal-modulus or phase restriction. The statement is specific to the four-frequency set \(\{0,1,2,4\}\).

## Proof
Put \(x=|a|\), \(y=|b|\), \(z=|c|\), and \(w=|d|\). Parseval applied to \(P^2\) gives
\[
\begin{aligned}
\|P\|_4^4={}&|a|^4+4|ab|^2+|b^2+2ac|^2+4|bc|^2\\
&+|c^2+2ad|^2+4|bd|^2+4|cd|^2+|d|^4.
\end{aligned}
\]
For fixed moduli, the two interference terms are bounded above by replacing their real parts with their absolute values, and equality in both bounds is attained simultaneously by taking \(a,b,c,d\) with a common phase. Hence, after the normalization
\[
x^2+y^2+z^2+w^2=1,
\]
the sharp fourth power is the maximum of
\[
H(x,y,z,w)=2-(x^4+y^4+z^4+w^4)+4xzy^2+4xwz^2
\]
over the nonnegative orthant of the unit sphere.

Every boundary point has \(H\le15/7\). Indeed, if \(x=0\) or \(z=0\), the collision terms vanish and \(H\le2-1/3=5/3\). If \(y=0\), set \(q=z^2\) and \(p=x^2+w^2=1-q\). The inequalities \(xw\le p/2\) and \(x^4+w^4\ge p^2/2\) give
\[
H\le2-\frac{p^2}2-q^2+2pq
=\frac{15}{7}-\frac72\left(q-\frac37\right)^2.
\]
The case \(w=0\) is identical after setting \(q=y^2\) and \(p=x^2+z^2\). On the other hand, \(x=y=z=w=1/2\) gives \(H=9/4>15/7\), so every global maximizer is interior.

Write \(G=H-2\). At an interior maximizer, Euler's identity and Lagrange multipliers give \(\nabla G=4\delta v\), where \(v=(x,y,z,w)\) and \(\delta=G(v)>0\). Scaling by \(x>0\), put \(r=y/x\), \(s=z/x\), \(t=w/x\), and \(k=\delta/x^2\). The stationary equations become
\[
-1+sr^2+ts^2=k,
\qquad -r^2+2s=k,
\]
\[
-s^3+r^2+2ts=ks,
\qquad -t^3+s^2=kt.
\]
Exact Gröbner elimination of \(r,s,t,k\), together with \(\delta=k/(1+r^2+s^2+t^2)\), yields the necessary equation
\[
7405408\delta^9+29910288\delta^8+50188768\delta^7+43830564\delta^6+19545666\delta^5+2647793\delta^4-1203370\delta^3-539404\delta^2-84328\delta-6889=0.
\]
The coefficients of this polynomial have exactly one sign change, so Descartes' rule gives at most one positive root. Its value at \(0\) is negative and its value at \(1\) is positive, so there is exactly one positive root \(\delta_*\). Since a global maximizer exists, is interior, and has \(\delta>0\), its value must be that root. This proves the sharp constant.

## Verification
The accompanying exact-arithmetic checker reconstructs the boundary estimate, the four stationary equations, the lexicographic Gröbner basis, and the resultant eliminating the scaled stationary variables. It verifies that the resultant is a nonzero integer multiple of the displayed degree-nine polynomial, verifies its single sign change and an exact rational sign bracket \(1497/5000<\delta_*<599/2000\), and then evaluates the numerical constant only for convenience.

A replay produces:

`VERIFY_OK delta=0.299413862840328 C4=1.231414565773106 groebner_degree=9 positive_roots=1 boundary=2.142857142857143`

The decimal evaluation is not the proof; the exact polynomial, the boundary argument, and the elimination certificate are.

## Relationship to prior work
Neuwirth's 1997 preprint develops the even-moment Parseval mechanism in terms of arithmetic relations among frequencies and explicitly analyzes the basic \(p=4\) relation types. In particular, the full text identifies three-term progression relations \(2q_1=q_2+q_3\) and four-distinct-point relations \(q_1+q_2=q_3+q_4\). It does not state the sharp \(L^2\)-to-\(L^4\) norm for the four-frequency support \(\{0,1,2,4\}\), where two progression relations overlap.

The closest indexed finite-support result located in the comparison search concerns phase-only fourth moments of four-point supports: it fixes all coefficient moduli and minimizes the fourth moment. That problem neither contains nor implies the unrestricted-amplitude maximization above. A separate one-collision sharp-norm classification likewise does not apply because \(\{0,1,2,4\}\) has two pair-sum collisions.

## Limitations
The theorem determines one exact finite-support Nikolskii invariant. It does not classify all four-point supports, and it does not give a general formula in terms of an arbitrary collision hypergraph. The literature search did not locate a covering statement for this exact support and norm, but an older sparse-\(\Lambda(4)\) or Nikolskii table under different terminology remains a residual originality risk.

## References
1. S. Neuwirth, *Metric unconditionality and Fourier analysis*, arXiv:math/9707211v1 (first public version 28 July 1997); Studia Mathematica 131 (1998), 19--62.
