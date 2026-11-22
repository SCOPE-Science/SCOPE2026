# Sharp two-input quadratic edge variation of centered maximal averaging on a four-vertex path

## Finding

For the unweighted path with consecutive vertices \(0,1,2,3\), let \(M\) be the centered Hardy–Littlewood maximal averaging operator with counting measure and with absolute values inside its averages. For every pair of nonnegative real vertex functions \(f,g\),
\[
\boxed{V_2(Mf-Mg)\le\sqrt{\frac32}\,V_2(f-g),}
\qquad
V_2(h)=\left(\sum_{i=0}^2|h_i-h_{i+1}|^2\right)^{1/2}.
\]
The constant \(\sqrt{3/2}\) is sharp, including among strictly positive rational pairs. For example, equality holds with
\[
g=(8,1,1,8),\qquad
f=g+\frac1{100}(3,2,1,0).
\]
Consequently centered maximal averaging can **amplify differences in quadratic edge variation**, even though a single-input graph-variation bound is a separate, often contractive, problem.

## Assumptions and scope

The graph is exactly the four-vertex unweighted path \(P_4\), with edges \(\{0,1\},\{1,2\},\{2,3\}\). Its centered balls are \(B(i,r)=\{j:|i-j|\le r\}\) for integer \(r\ge0\), and
\[
(Mf)_i=\max_{r\ge0}\frac1{|B(i,r)|}\sum_{j\in B(i,r)}|f_j|.
\]
Functions \(f,g\) are **nonnegative and real**; no complex-valued, signed-input, or other-graph two-input theorem is asserted. The edge seminorm counts each undirected edge once and takes the square root of the sum of squared differences. It vanishes on constant functions; on nonnegative functions the maximal operator commutes with addition of a nonnegative constant.

## Proof

Let \(B\) be the oriented edge-difference matrix and \(T\) its convenient right inverse:
\[
B=\begin{pmatrix}1&-1&0&0\\0&1&-1&0\\0&0&1&-1\end{pmatrix},
\quad
T=\begin{pmatrix}1&1&1\\0&1&1\\0&0&1\\0&0&0\end{pmatrix},
\quad BT=I_3.
\]
Every vector \(h\in\mathbb R^4\) satisfies \(h=T(Bh)+c\mathbf1\) for a real constant \(c\). On the nonnegative cone the maximal operator is the componentwise maximum of finitely many *linear ball-average* functions. On any cell where a selected ball at each vertex is active, it equals \(A f\), where \(A\) is a row-stochastic four-by-four matrix with each row equal to a centered-ball average. Since \(A\mathbf1=\mathbf1\),
\[
B A h=B A T(Bh).
\]
The four vertices admit respectively \(4,3,3,4\) distinct centered balls, so there are \(4\cdot3\cdot3\cdot4=144\) possible row selections, including selections that never occur as strict activation cells. Write \(A_{12}=12A\), with integer entries, and put \(H_{12}=B A_{12}T\). The exact finite certificate verifies for **each of the 144 selections** the seven principal minors of the integer symmetric matrix
\[
D_A=216I_3-H_{12}^{\mathsf T}H_{12}
\]
are nonnegative. A real symmetric matrix is positive semidefinite if and only if every principal minor is nonnegative. Therefore \(H_{12}^{\mathsf T}H_{12}\preceq216I_3\), or equivalently
\[
\|BA T\|_{2\to2}^2\le\frac{216}{12^2}=\frac32
\]
for every possible active cell. The certificate is independently reproducible from `check_P4_variation.py`: it constructs the balls afresh, enumerates every mask, and uses integer determinants, with no numerical tolerance or external dependencies.

For any nonnegative \(f,g\), their connecting segment remains in the nonnegative cone and splits at finitely many ball-selection changes into linear subsegments. On each such subsegment the derivative of \(B M\) has the form \(BA\). Since its action on differences has operator norm at most \(\sqrt{3/2}\) measured by \(\|Bh\|_2\), summing/integrating along the segment proves the stated global two-input inequality. Ties cause no problem by continuity; every derivative segment is one of the certified choices.

Sharpness is attained on the strictly active branch where endpoints select singleton balls and the two inner vertices select the radius-two balls (the whole graph), yielding
\[
A h=(h_0,\overline h,\overline h,h_3),
\qquad \overline h=\frac{h_0+h_1+h_2+h_3}{4}.
\]
For this branch the edge-space matrix is
\[
H=BA T=\begin{pmatrix}3/4&1/2&1/4\\0&0&0\\1/4&1/2&3/4\end{pmatrix}.
\]
Its Gram eigenvalues are \(0,1/4,3/2\), and the edge vector \((1,1,1)\) is a top norming direction. At \(g=(8,1,1,8)\), the indicated four ball choices are strict. They remain strict after adding \(T(1,1,1)/100=(3,2,1,0)/100\), so the explicit pair has squared edge-variation quotient exactly \(3/2\).

## Verification

Run `python3 check_P4_variation.py` using only the Python standard library. It checks \(144\) integer positive-semidefinite certificates (all seven principal minors per mask), identifies the two masks whose determinant is zero, verifies strict activity of the exhibited branch for both rational inputs, and checks the sharp ratio by exact `fractions.Fraction` arithmetic. A successful execution prints:

```text
PASS: 144 exact branch positive-semidefinite certificates
Equality branch masks: [(0, 2, 2, 0), (3, 0, 0, 3)]
PASS: positive rational maximizing pair, exact squared ratio 3/2
```

The exact finite certificate is exhaustive for the \(144\) derivative matrices because each row must select one of the explicitly enumerated balls. Its result, together with the segment proof, establishes the inequality for all nonnegative real inputs, rather than only for tested signals.

## Relationship to prior work

González-Riquelme, Kovač and Madrid (arXiv:2603.12462v1) analyze **one-input** graph \(p\)-variation and list a sharp first-variation result for \(P_4\); a one-input inequality does not control the difference \(Mf-Mg\) in terms of \(f-g\). Liu, Lian and Wang (arXiv:2611.15377v1) treat one-input variation and norm inequalities for centered and fractional graph maximal operators, focusing sharp formulas on complete graphs and stars. Lu and Zhao (arXiv:2611.24180v1) likewise study one-input edge variation, including exact star constants and general oscillation estimates. These results motivate, but do not state, the two-input sharp quadratic edge-variation calculation here. Related published two-input results on stars, complete graphs and uncentered cycles concern different graphs and/or first variation. No blanket priority claim is made beyond the inspected sources.

## Limitations

The exact constant concerns only nonnegative real functions on \(P_4\). It is a finite-graph stability theorem, not a general estimate for all paths or arbitrary graphs. The certificate is finite but exhaustive for this graph; it is not an infinite-graph computation. No full equality-case classification is asserted. Bibliographic coverage may be incomplete; independent verification and priority review have not been performed.

## References

1. C. González-Riquelme, V. Kovač, and J. Madrid, *Sharp variational inequalities for the Hardy–Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462v1 (first public 2026-03-12), https://arxiv.org/abs/2603.12462.
2. F. Liu, Y. Lian, and Y. Wang, *Sharp \(L^p\) and variation inequalities for maximal operators on finite connected graphs*, arXiv:2611.15377v1 (first public 2026-11-11), https://arxiv.org/abs/2611.15377.
3. S. Lu and F. Zhao, *Variational Estimates for the Hardy–Littlewood Maximal Operator on Finite Graphs*, arXiv:2611.24180v1 (first public 2026-11-18), https://arxiv.org/abs/2611.24180.
4. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs*, arXiv:2005.03146 (2020), https://arxiv.org/abs/2005.03146.
