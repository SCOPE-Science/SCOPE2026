# Fourier spectrum and zero-free congruence classes of six-cycle orbits in \(K_{3,n}\)

## Finding
For every integer \(n\ge3\), let \(\mathcal C_n\subseteq\mathbb F_2^{3n}\) consist of the edge-incidence vectors of **all unoriented simple six-cycles** in \(K_{3,n}\). The complete Walsh coefficient profile of \(\mathbf1_{\mathcal C_n}\) is specified below by a four-cell multinomial distribution. For every frequency, the unnormalized coefficient is \(XYZ-X^2-Y^2-Z^2+2n\), where \(X,Y,Z\) are explicit integer linear forms in the four cell counts.

In particular, if \(n\equiv3\pmod4\), **every** Walsh coefficient has two-adic valuation exactly \(1\). If \(n\equiv6\pmod8\), **every** coefficient has valuation exactly \(3\). Thus the convolution operator by \(\mathbf1_{\mathcal C_n}\) on the Boolean group is invertible in either of these infinite arithmetic progressions. Other dimensions need not be zero-free: at \(n=4\) precisely \(3/4\) of all coefficients vanish, and at \(n=5\) precisely \(15/64\) vanish.

Let \(P_n\) be Fourier projection onto the frequency set \(\mathcal C_n\) on the Boolean group. The exact sharp endpoint norm is a finite multinomial sum (given below), and satisfies
\[
\lim_{n\to\infty}\frac{\|P_n\|_{\ell^1\to\ell^1}}{n^{3/2}}=
\lim_{n\to\infty}\frac{\|P_n\|_{\ell^\infty\to\ell^\infty}}{n^{3/2}}
=\left(\frac2\pi\right)^{3/2}.
\]

## Assumptions and scope
Let the three vertices of the small bipartition have labels \(1,2,3\), and the other vertices labels \(1,\ldots,n\). For each sign assignment \(s\in\mathbb F_2^{3n}\), write \(a_i,b_i,c_i\in\{-1,1\}\) for the three edge signs in column \(i\). Set \(x_i=a_i b_i\), \(y_i=a_i c_i\), and \(z_i=b_i c_i\); necessarily \(x_i y_i z_i=1\). The four permitted triples \((x_i,y_i,z_i)\), in order, are \((1,1,1)\), \((1,-1,-1)\), \((-1,1,-1)\), and \((-1,-1,1)\). Let \(t_0,t_1,t_2,t_3\) be their multiplicities, so \(t_0+t_1+t_2+t_3=n\). Define
\[
X=t_0+t_1-t_2-t_3,\quad
Y=t_0-t_1+t_2-t_3,\quad
Z=t_0-t_1-t_2+t_3,
\]
and \(F(t)=XYZ-X^2-Y^2-Z^2+2n\).

Use the unnormalized Walsh transform \(W_n(s)=\sum_{C\in\mathcal C_n}(-1)^{\langle s,C\rangle}\). For **every** integer \(w\), its exact multiplicity is
\[
\#\{s:W_n(s)=w\}=2^n\!\!\sum_{\substack{t_0+\cdots+t_3=n\\t_j\ge0,\ F(t)=w}}\frac{n!}{t_0!t_1!t_2!t_3!}.
\]
This formula merges coincident values automatically. The number of cycles is \(n(n-1)(n-2)\). There are exactly \(2^n n!/(t_0!t_1!t_2!t_3!)\) edge signings with a given cell-count quadruple.

## Proof
**Cycle parameterization.** Each six-cycle includes all three vertices on the small side and exactly three distinct vertices on the large side. Its three large-side vertices are bijectively assigned to the row pairs \(12,13,23\). This assignment specifies the six edges of the cycle uniquely, and each cycle yields just one such assignment. Consequently,
\[
W_n(s)=\sum_{\substack{i,j,k\in\{1,\ldots,n\}\\i,j,k\ \mathrm{pairwise\ distinct}}}x_i y_j z_k.
\]
Writing \(X=\sum_i x_i\), \(Y=\sum_i y_i\), \(Z=\sum_i z_i\) and using \(x_i y_i=z_i\), \(x_i z_i=y_i\), \(y_i z_i=x_i\), the three diagonal coincidences in \(XYZ\) subtract \(X^2+Y^2+Z^2\), while inclusion-exclusion adds back \(2\sum_i x_i y_i z_i=2n\). This proves \(W_n=F(t)\), and uniform column-type counting proves the stated complete multiplicity law.

**The class \(n\equiv3\pmod4\).** Every edge of \(K_{3,n}\) appears in exactly \(4\binom{n-1}{2}=2(n-1)(n-2)\) six-cycles, an even number. For any edge signing, the parity of the number of negative six-cycles is therefore zero: modulo two the sum of their negativity indicators equals the sum, over negative edges, of their cycle-incidence counts. Thus
\[
W_n(s)=|\mathcal C_n|-2\#\{\text{negative six-cycles}\}\equiv n(n-1)(n-2)\pmod4.
\]
When \(n\equiv3\pmod4\), the right side is \(2\pmod4\), proving valuation exactly \(1\) at every frequency.

**The class \(n\equiv6\pmod8\).** Now \(X,Y,Z\) are even. Write \(U=X/2\), \(V=Y/2\), \(T=Z/2\). The identity \(X+Y+Z=4t_0-n\) shows that \(U+V+T=2t_0-n/2\) is odd. Moreover,
\[
W_n(s)=4\left(2UVT-U^2-V^2-T^2+\frac n2\right).
\]
Exactly one or all three of \(U,V,T\) are odd. In the first case, \(2UVT\equiv0\pmod4\) and \(U^2+V^2+T^2\equiv1\pmod4\); in the second, these residues are \(2\) and \(3\), respectively. Since \(n/2\equiv3\pmod4\), the parenthesized term is \(2\pmod4\) in either case. Hence \(W_n(s)\equiv8\pmod{16}\) universally, proving valuation exactly \(3\).

**Exceptional dimensions.** For \(n=4\), the cell counts \((t_0,t_1,t_2,t_3)=(0,0,1,3)\) give \((X,Y,Z)=(-4,-2,2)\) and \(F(t)=0\). For \(n=5\), counts \((0,1,1,3)\) give \((-3,-3,1)\) and \(F(t)=0\). Evaluating the complete multinomial profile gives the precise zero fractions \(3/4\) and \(15/64\), respectively. Nonzero Walsh coefficients at all frequencies are equivalent, by Fourier diagonalization, to invertibility of convolution by the cycle indicator.

**Exact sharp norm and Gaussian limit.** For every \(n\ge3\), the convolution kernel of \(P_n\) is \(2^{-3n}W_n\). Its \(\ell^1\) and \(\ell^\infty\) operator norms equal the kernel's absolute sum, attained by a delta function or the signs of the reversed kernel. Therefore
\[
L_n:=\|P_n\|_{1\to1}=\|P_n\|_{\infty\to\infty}
=4^{-n}\sum_{t_0+\cdots+t_3=n}\frac{n!}{t_0!t_1!t_2!t_3!}\,|F(t)|.
\]
For independent uniform column types, the vectors \((x_i,y_i,z_i)\) have mean zero and covariance the identity matrix; their coordinates are bounded. By the multivariate central limit theorem, \((X,Y,Z)/\sqrt n\) converges in distribution to three independent standard Gaussians \((G_1,G_2,G_3)\). Since \(\mathbb E(X^2+Y^2+Z^2)=3n\), the noncubic term contributes at most \(5n\) to \(\mathbb E|W_n-XYZ|\). Uniform sixth-moment bounds for the normalized sums (by bounded independent increments) ensure uniform integrability of the cubic products. Thus
\[
L_n/n^{3/2}\longrightarrow\mathbb E|G_1G_2G_3|
=(\mathbb E|G_1|)^3=(2/\pi)^{3/2}.
\]

## Verification
The standalone file `check_sixcycle.py` constructs the orbit indicator from all ordered assignments of three distinct columns to the row pairs, computes its **complete** integer Walsh-Hadamard transform, and compares **every** coefficient against \(F(t)\) for \(3\le n\le6\). It also checks exact norms, zero fractions, Parseval's second moment, and both residue laws using the multinomial profile for \(3\le n\le70\). It is an independent computational corroboration of the displayed symbolic proof, not an infinite certificate. Run it with Python 3 (standard library only) using `python check_sixcycle.py`.

## Relationship to prior work
Goodall (2008) presents finite abelian Fourier orthogonality and graph-polynomial methods but does not evaluate this specific six-cycle Walsh orbit, its sharp endpoint norm, or its valuation laws. Schaefer (2015) studies negative-cycle vectors on signed **complete graphs**, rather than the full coefficient profile on \(K_{3,n}\). Schaefer and Zaslavsky (2017), particularly Section 4.2, study negative-cycle-vector dimensions on complete bipartite graphs and provide general signed-cycle inclusion-exclusion. Their universal inclusion-exclusion could in principle compute each coefficient, so that general algorithm is **not** new. The specific joint valuation congruences and sharp Gaussian norm asymptotic are the contributions assessed here. The specialized four-cell expression supports them and gives an explicit full multiplicity formula.

## Limitations
There is no claimed classification of all dimensions outside the two zero-free congruence classes, no closed polynomial-free simplification of the finite exact norm sum, no effective asymptotic error bound, and no proof of global historical uniqueness. The result covers six-cycles only for the labeled complete bipartite family with exactly three vertices on one side. The mathematical review described separately is not an independent audit.

## References
- Andrew Goodall, *Graph polynomials and Tutte-Grothendieck invariants: an application of elementary finite Fourier analysis*, arXiv:0806.4848v1, publicly submitted 2008-06-30, Sections 4–5. https://arxiv.org/abs/0806.4848
- Alex Schaefer, *The Negative Cycle Vectors of Signed Complete Graphs*, arXiv:1512.09087, publicly submitted 2015-12-30. https://arxiv.org/abs/1512.09087
- Alex Schaefer and Thomas Zaslavsky, *The Dimension of the Negative Cycle Vectors of Signed Graphs*, arXiv:1706.09041v1, publicly submitted 2017-06-27, Sections 3.1, 3.4, 4.2. https://arxiv.org/abs/1706.09041
