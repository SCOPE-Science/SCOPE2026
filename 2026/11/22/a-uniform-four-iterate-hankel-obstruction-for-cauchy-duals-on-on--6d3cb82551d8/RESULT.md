# A uniform four-iterate Hankel obstruction for Cauchy duals on one-circuit composition graphs

## Finding
Let \(C\) be any bounded \(2\)-isometric composition operator arising from the one-circuit, single-branching-vertex measure model described below. Write \(\kappa\ge2\) for the length of the circuit and \(x>0\) for the initial circuit mass divided by the positive mass increment. Let \(T=C(C^*C)^{-1}\) be its Cauchy dual, and let \(e_{\kappa-1}\) be the normalized point vector at the penultimate circuit vertex. Put \(\gamma_n=\|T^ne_{\kappa-1}\|^2\). Then
\[
\det(\gamma_{i+j})_{i,j=0}^{2}
=-\frac{(\kappa-2)(\kappa+x-2)^2(\kappa x+2\kappa+2x)}{(\kappa+x)^4(x+1)^2(x+2)(\kappa+x-1)^2}.
\]
For every \(\kappa\ge3\), this determinant is **strictly negative** for every admissible mass ratio, regardless of the number of attached rays or how positive ray mass is distributed. In particular, the Cauchy dual fails the degree-two Stieltjes moment positivity test using only the five norms \(\|T^ne_{\kappa-1}\|\), \(0\le n\le4\). When \(\kappa=2\) the determinant vanishes. The two lower-order consecutive Hankel determinants for this same vector, using only moments through order three, are both strictly positive; thus moment order four is the first Hankel-positive-semidefiniteness obstruction in this vector's initial-moment tests.

## Assumptions and scope
Fix an integer \(\kappa\ge2\) and a finite or countable nonempty family of positive ray masses \(c_i\), with \(0<c=\sum_i c_i<\infty\). Put \(s=c/\kappa\) and choose \(a_1>0\). The point set has cycle vertices \(v_1,\ldots,v_\kappa\), and ray vertices \(u_{i,j}\) for \(j\ge1\). The backward map \(\phi\) sends \(v_{r+1}\) to \(v_r\) for \(1\le r<\kappa\), sends \(v_1\) and all \(u_{i,1}\) to \(v_\kappa\), and sends \(u_{i,j+1}\) to \(u_{i,j}\). The discrete measure has \(\mu(v_r)=a_1+(r-1)s\) and \(\mu(u_{i,j})=c_i\). Define \(C f=f\circ\phi\) on \(L^2(\mu)\). These are precisely the positive-mass \(2\)-isometric measures on the specified graph, by the cited 2019/2021 classification, and direct computation independently gives boundedness and the \(2\)-isometry identity.

Set \(x=a_1/s>0\), and let \(e_z=\mathbf 1_{\{z\}}/\sqrt{\mu(z)}\). All displayed norms are Hilbert-space norms; the determinant is a finite real determinant, not an assertion about an arbitrary operator-valued moment matrix. The result concerns only this one-branching-vertex composition-graph family, not arbitrary \(2\)-isometries or arbitrary one-cycle weighted shifts.

## Proof
**Normalized Cauchy-dual edges.** The Radon–Nikodym diagonal of \(C^*C\) is \(h(v_r)=(a_r+s)/a_r\), including the final vertex with \(a_{\kappa+1}=a_1+c\), and \(h(u_{i,j})=1\). Consequently \(C\) is bounded below and \(T=C(C^*C)^{-1}\) exists. With \(a_r=s(x+r-1)\) and \(A=x+\kappa\), the squared coefficient of the edge \(e_{v_r}\mapsto e_{v_{r+1}}\) for \(r<\kappa\) is \((x+r-1)/(x+r)\). The final vertex has a squared edge coefficient to \(e_{v_1}\) of \(x(x+\kappa-1)/A^2\) and total squared coefficient to ray starts of \(\kappa(x+\kappa-1)/A^2\). Every later ray edge is isometric.

**First five moments.** Orthogonality of the distinct descendants at each fixed iterate lets us sum squared edge amplitudes. Write \(B=x+\kappa-2\), \(D=x+\kappa-1\), and \(A=x+\kappa\). For \(e=e_{v_{\kappa-1}}\), the resulting moments are exactly
\[
\begin{aligned}
\gamma_0&=1, &\gamma_1&=\frac{B}{D}, &\gamma_2&=\frac{B}{A},\\
\gamma_3&=\frac{B}{A^2}\!\left(\kappa+\frac{x^2}{x+1}\right), &
\gamma_4&=\frac{B}{A^2}\!\left(\kappa+\frac{x^2}{x+2}\right).
\end{aligned}
\]
The formulas hold for all \(\kappa\ge2\), including the two-cycle. They involve ray masses only through their sum \(c\), which disappears after normalization by \(s\).

**Hankel obstruction and first order.** Expanding the determinant of \(H=(\gamma_{i+j})_{0\le i,j\le2}\) and cancelling positive factors gives exactly the negative rational expression stated in the Finding. Its numerator has sign \(-\operatorname{sgn}(\kappa-2)\) for \(\kappa\ge2\), \(x>0\). For completeness, the consecutive two-by-two Hankel determinants are
\[
\begin{aligned}
\gamma_0\gamma_2-\gamma_1^2
 &=\frac{B}{AD^2}>0,\\
\gamma_1\gamma_3-\gamma_2^2
 &=\frac{B^2}{A^2(x+1)D}>0,\\
\gamma_2\gamma_4-\gamma_3^2
 &=\frac{xB^2(2\kappa x+2\kappa+x^2)}{A^4(x+1)^2(x+2)}>0.
\end{aligned}
\]
In particular the leading and once-shifted two-by-two matrices available through \(\gamma_3\) are positive definite, whereas \(H\) is indefinite at \(\gamma_4\). If \(T\) were subnormal, the spectral measure of a normal extension applied to \(e\) would give a positive Borel measure \(\nu\) with \(\gamma_n=\int_0^{\infty}t^n\,d\nu(t)\). Then \(H\) would be the Gram matrix of \(1,t,t^2\) in \(L^2(\nu)\) and necessarily positive semidefinite, contradicting the strictly negative determinant. No finite numerical experiment is used to infer an infinite-dimensional assertion.

## Verification
The included `checker.py` verifies the full symbolic determinant identity, each displayed consecutive two-by-two determinant, and exact rational norm recurrences over \(1{,}372\) sample pairs \((\kappa,x)\), with \(2\le\kappa\le50\). To reproduce, install SymPy and run `python checker.py` in the extracted directory. The symbolic cancellation verifies rational identities; the operator edge reduction and the positive-measure Gram implication are analytic proof steps, not outcomes inferred from finite testing.

## Relationship to prior work
Jabłoński and Kośmider (arXiv:1907.09222, first public 22 July 2019; subsequently published 2021) classify the relevant \(2\)-isometric one-circuit composition operators and prove subnormality of the Cauchy dual for a one-vertex circuit. Anand, Chavan, Jabłoński and Stochel (arXiv:2003.04090, 2020) develop Cauchy-dual counterexamples and moment criteria. Buchała (2024, Theorem 6.2) gives a general necessary-and-sufficient subnormality test for discrete one-cycle graphs using candidate two-atomic measures and initial moments. That theorem covers the broad qualitative subnormality question and is **not** claimed as new here. The distinct contribution is a concrete, uniform \(3\times3\) **negative Hankel certificate appearing after just four iterations**, with an exact value and positivity of both lower-order tests, independent of circuit length and branch distribution. The inspected prior results do not state or directly supply this finite-order determinant identity. An unindexed equivalent moment calculation remains a historical-priority risk.

## Limitations
The conclusion concerns a single point vector's moment matrix and does not establish a general theorem for all cyclic \(2\)-isometries. The moment-order sharpness is only for the displayed probe and the consecutive Hankel PSD tests, not all possible vectors or all Hausdorff localizing tests. Qualitative nonsubnormality has prior broader treatments; it is not an independent novelty claim. Classification of the graph weights is attributed to prior work. The proof and checker have received no independent mathematical audit.

## References
1. Z. J. Jabłoński and J. Kośmider, *m-Isometric Composition Operators on Directed Graphs with One Circuit*, arXiv:1907.09222 (2019); Integral Equations and Operator Theory 93 (2021), 50. https://arxiv.org/abs/1907.09222
2. A. Anand, S. Chavan, Z. J. Jabłoński and J. Stochel, *The Cauchy Dual Subnormality Problem for Cyclic 2-Isometries*, arXiv:2003.04090 (2020). https://arxiv.org/abs/2003.04090
3. M. Buchała, *m-Isometric Composition Operators on Discrete Spaces*, Complex Analysis and Operator Theory 18 (2024), 158, especially Theorem 6.2 and Example 6.4. https://doi.org/10.1007/s11785-024-01603-4
