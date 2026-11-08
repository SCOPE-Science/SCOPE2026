# Uniform Hamming spectrum of the cubic-scroll toric code

## Finding
Let \(q\ge4\) be a prime power, \(t=q-1\), and \(P=\operatorname{conv}\{(0,0),(2,0),(1,1),(0,1)\}\subset\mathbb R^2\). This lattice trapezoid is the hyperplane polygon of the cubic rational normal scroll \(S(1,2)\), equivalently the degree-three embedding of the first Hirzebruch surface. Evaluate the five toric monomials \(1,x,x^2,y,xy\) on the dense torus \(T(\mathbb F_q)=(\mathbb F_q^\times)^2\). Let \(C_P(q)\) denote the resulting linear code and \(W_q(z)=\sum_w A_wz^w\) its Hamming weight enumerator.

Put \(U=t(t^2+t+6)/2\). **For every prime power \(q\ge4\)**, the exact weight enumerator is
\[
\begin{aligned}
W_q(z)={}&1+\frac{t^2(t-1)}2z^{t(t-2)}+3t^3z^{t(t-2)+1}
+t^3(t-1)z^{t(t-2)+2}\\
&+(4t^2+2tU)z^{t(t-1)}+(6t^3+t^2U)z^{t(t-1)+1}\\
&+4t^3(t-1)z^{t(t-1)+2}
+\frac{t^3(t-1)(t-2)}2z^{t(t-1)+3}
+(U+2t)z^{t^2}.
\end{aligned}
\]
If two exponents coincide, their coefficients are added; this occurs for the last two terms when \(q=4\). The length, dimension, minimum distance, next weight, and minimum-weight multiplicities are
\[
[n,k,d]_q=[t^2,5,t(t-2)]_q,\quad d_2=d+1,\quad
A_d=\frac{t^2(t-1)}2,\quad A_{d_2}=3t^3.
\]
For \(q\ge5\), there are exactly eight distinct nonzero weights; for \(q=4\), exactly seven. The dual code has minimum distance \(3\).

**Support geometry.** Every minimum-weight word, uniquely as a function, is a nonzero scalar multiple of \((x-r)(x-s)\), with distinct \(r,s\in\mathbb F_q^\times\); its zero set is the disjoint union of two vertical torus fibers. Every next-to-minimum word is \(\beta(x-r)(y+h(x))\), where \(r,\beta\in\mathbb F_q^\times\) and \(h\) is one of: a nonzero constant, a nonzero multiple of \(x\), or a nonzero multiple of \(x-r\) (after absorbing scalar factors into \(\beta\)). It has exactly \(2t-1\) torus zeros.

## Assumptions and scope
The ground field is exactly \(\mathbb F_q\), where \(q\) ranges over all prime powers at least four; there is no characteristic restriction. The polygon contains exactly the five lattice points shown above, and evaluation takes place on \(T(\mathbb F_q)\), not all rational points of the compact scroll. A codeword is indexed by the coefficient tuple of
\[
f(x,y)=A(x)+yB(x),\qquad \deg A\le2,\quad\deg B\le1.
\]
The variable \(z\) in \(W_q(z)\) marks Hamming weight, not an affine coordinate. The lower bound \(q\ge4\) is necessary for injectivity in the stated five-dimensional representation: \(t=q-1\ge3\).

## Proof
**(1) The toric code and injectivity.** The listed lattice points yield precisely the basis \(1,x,x^2,y,xy\). If \(A(x)+yB(x)\) vanishes for every \((x,y)\in T(\mathbb F_q)\), fixing \(x\in\mathbb F_q^\times\) and taking two distinct nonzero values of \(y\) gives \(A(x)=B(x)=0\). Since \(t\ge3\), the degree-at-most-two polynomial \(A\) and degree-at-most-one polynomial \(B\) are both identically zero. Thus each coefficient tuple yields a unique word, and the dimension is five.

**(2) Quadratic root census.** Among \(A\in\mathbb F_q[x]\) of degree at most two, exclude \(A=0\). The numbers of polynomials having respectively two, one, and zero distinct roots in \(\mathbb F_q^\times\) are
\[
U_2=t\binom t2=\frac{t^2(t-1)}2,\qquad
U_1=t(q^2-1)-2U_2=3t^2,\qquad U_0=q^3-1-U_1-U_2=U.
\]
Indeed, every pair of distinct nonzero roots determines a quadratic up to a nonzero scalar, and for each fixed root the subspace of polynomials vanishing there has dimension two. The zero polynomial is a separate fourth case.

**(3) Split by the linear coefficient of \(y\).** When \(B=0\), a nonzero \(A\) with \(r\) distinct torus roots gives exactly \(rt\) zeros, and \(A=0\) gives the zero word. When \(B\) has no torus root, it must be a nonzero constant or a nonzero scalar multiple of \(x\); there are \(2t\) such \(B\)'s. For each \(x\) with \(A(x)\ne0\), exactly one \(y\in\mathbb F_q^\times\) satisfies \(A(x)+yB(x)=0\), and for each \(x\) with \(A(x)=0\), none does. Thus \(A=0\) contributes zero zeros, and a nonzero \(A\) with \(r\) roots contributes \(t-r\) zeros.

There are \(t^2\) other nonzero \(B\)'s, each uniquely of the form \(\beta(x-r)\) for \(\beta,r\in\mathbb F_q^\times\). Fix \(r\). If \(A(r)=0\), write \(A=(x-r)Q\) with \(\deg Q\le1\). At \(x=r\), all \(t\) values of \(y\) are zeros. At each other nonzero \(x\), exactly one \(y\) is a zero unless \(Q(x)=0\). The possibilities for \(Q\) are: zero (one choice, total zero count \(t\)); nonzero with no root in \(\mathbb F_q^\times\setminus\{r\}\) (\(3t\) choices, total zero count \(2t-1\)); or one root in that set (\(t(t-1)\) choices, total zero count \(2t-2\)). The \(3t\) root-free possibilities are exactly nonzero constants, nonzero multiples of \(x\), and nonzero multiples of \(x-r\).

If \(A(r)\ne0\), let \(s\in\{0,1,2\}\) be the number of roots of \(A\) in \(\mathbb F_q^\times\setminus\{r\}\). The number of zeros of \(f\) is \(t-1-s\). The counts of \(A\)'s for \(s=2,1,0\) respectively are
\[
V_2=t\binom{t-1}2=\frac{t(t-1)(t-2)}2,
\quad V_1=(t-1)tq-2V_2=3t(t-1),
\quad V_0=tq^2-V_1-V_2=U.
\]
For each prescribed subset of at most two roots away from \(r\), the condition \(A(r)\ne0\) cuts out \(q-1\) times a power of \(q\), giving the displayed counts by the first two binomial moments. The equality \(V_0=U\) follows by direct expansion.

**(4) Collect the contributions.** Convert each zero count \(Z\) to weight \(t^2-Z\), multiply by the corresponding counts of \(B\), and sum. In particular, the counts by the three classes of \(B\) are
\[
\begin{array}{c|c|c}
B\text{ class}&\#B&\text{zero counts and coefficient multiplicities}\\\hline
B=0&1&t^2:(1),\ 0:U,\ t:3t^2,\ 2t:U_2\\
B\ne0,\ B|_T\ne0&2t&0:(1),\ t:U,\ t-1:3t^2,\ t-2:U_2\\
B=\beta(x-r)&t^2&t:(1),\ 2t-1:3t,\ 2t-2:t(t-1),\\
&&t-1:U,\ t-2:3t(t-1),\ t-3:V_2.
\end{array}
\]
In the first row, the entry \(t^2:(1)\) denotes the unique zero polynomial \(A=0\). Replacing the zero counts by weights and simplifying produces the claimed \(W_q(z)\). The sum of all coefficients equals \(q^5\), as required by injectivity.

**(5) Leading weights and dual.** For \(t\ge3\), the two smallest possible nonzero exponents are \(t(t-2)\) and \(t(t-2)+1\), with the claimed counts and factorization patterns, as the case split shows. The projective generator columns are the distinct points \([1:x:x^2:y:xy]\in\mathbb P^4(\mathbb F_q)\). Any two are independent, while three points with fixed \(x\) and distinct \(y\)'s lie on a projective line. Hence the dual has minimum distance exactly three.

## Verification
The standalone file `verify.py` implements finite fields \(\mathbb F_4,\mathbb F_5,\mathbb F_7,\mathbb F_8,\mathbb F_9\) directly using modular polynomial arithmetic. It enumerates all \(q^5\) coefficient tuples, independently evaluates each at all \((q-1)^2\) torus points, and compares the complete weight spectrum with a separate formula implementation. The supplied exact output `verification_output.txt` shows equality for all five fields, including the \(q=4\) coincident-exponent boundary, and terminates with `ALL_CHECKS_PASSED`. Run `python3 verify.py` in a standard Python 3 environment. The all-\(q\) result is proved above, not inferred from these five finite experiments.

## Relationship to prior work
The toric evaluation-code construction and its connection to Hirzebruch polygons are due to Hansen; Joyner, Little–Schenck, and subsequent authors established basic parameters and distance bounds. Yau–Zuo classify dimension-five toric surface codes, and Luo–Yau–Zhang–Zuo identify the polygon as the third five-point class in their Figure 1.3; their enumerator tables concern dimension-six codes at specified field sizes, not a uniform all-field spectrum for the present five-point class. Brown–Kasprzyk compute minimum-distance information for small polygons and small fields. These results establish the objects and several weaker invariants but do not, in the inspected material, supply the complete \(q\)-parametric enumerator or the next-weight classification proved here. The Yau–Zuo 2009 full text could not be inspected; this is a material historical-priority risk, not a mathematical deduction of novelty.

## Limitations
The statement concerns the *torus-point* code of the fixed cubic-scroll polytope, not the code obtained from all rational points on the scroll or an arbitrary toric surface. It requires \(q\ge4\); no claim is made for smaller fields. The finite-field verifier checks five field sizes only. No independent peer review or historical-priority certification has been performed, and the inaccessible 2009 primary work remains a source-comparison limitation.

## References
1. J. P. Hansen, *Hirzebruch surfaces and error-correcting codes*, Aarhus University Preprint Series 6 (August 2000). https://data.math.au.dk/publications/pp/2000/imf-pp-2000-6.pdf.
2. D. Joyner, *Toric codes over finite fields*, arXiv:math/0208155, first version publicly posted 2002-08-21. https://arxiv.org/abs/math/0208155.
3. J. Little and H. Schenck, *Toric surface codes and Minkowski sums*, arXiv:math/0507598, first posted 2005-07-28. https://arxiv.org/abs/math/0507598.
4. S. S.-T. Yau and H. Zuo, *Notes on classification of toric surface codes of dimension 5*, Applicable Algebra in Engineering, Communication and Computing 20 (2009), 175–185. DOI:10.1007/s00200-009-0096-2.
5. X. Luo, S. S.-T. Yau, M. Zhang and H. Zuo, *On classification of toric surface codes of low dimension*, arXiv:1402.0060, first posted 2014-02-01. https://arxiv.org/abs/1402.0060.
6. G. Brown and A. M. Kasprzyk, *Small polygons and toric codes*. https://kasprzyk.work/research/pdf/toric_codes.pdf.
