# Sharp cyclic Poisson Lipschitz constants with a four-residue quantization law

## Finding
For every integer \(n\ge3\), let \(L=2I-T-T^{-1}\) be the unnormalized combinatorial Laplacian of the unit-edge cycle \(C_n=\mathbb Z/n\mathbb Z\), where \((Tf)(j)=f(j+1)\). Let \(L^+\) be its Moore–Penrose inverse, vanishing on constants. Equip real functions modulo constants with the Lipschitz seminorm
\[
\operatorname{Lip}(f)=\max_{0\le j<n}|f(j+1)-f(j)|.
\]
Then the exact sharp inverse estimate is
\[
\operatorname{Lip}(L^+f)\le K_n\operatorname{Lip}(f),
\qquad
K_n=\begin{cases}
\dfrac{n^2}{32},&n\equiv0\pmod4,\\[2mm]
\dfrac{n^2+1-2/n}{32},&n\equiv1\pmod4,\\[2mm]
\dfrac{n^2+4}{32},&n\equiv2\pmod4,\\[2mm]
\dfrac{n^2+1+2/n}{32},&n\equiv3\pmod4.
\end{cases}
\]
These constants are attained for every \(n\). In particular, \(K_n/n^2\to 1/32\), but the unscaled correction \(K_n-n^2/32\) has a residue-dependent form: the two odd classes both approach \(1/32\), with opposite \(1/n\) terms.

**Complete equality classification.** Define the cyclic Green row
\[
G_j=\frac{n^2-1}{12n}-\frac{j(n-j)}{2n},\qquad j=0,\ldots,n-1.
\]
For a nonconstant input write \(s_j=(f(j+1)-f(j))/\operatorname{Lip}(f)\). Equality holds if and only if there are an output-edge shift \(a\in C_n\), a sign \(\varepsilon\in\{-1,1\}\), and a median \(c\) of \(\{G_j:0\le j<n\}\), such that
\[
\varepsilon s_{a+j}=\begin{cases}
1,&G_j>c,\\
-1,&G_j<c,\\
\text{an arbitrary member of }[-1,1],&G_j=c,
\end{cases}
\qquad \sum_{j=0}^{n-1}s_j=0.
\]
Conversely every such zero-sum increment vector integrates to a periodic input and attains the sharp constant, up to addition of constants and nonzero rescaling.

## Assumptions and scope
The functions, operators, and seminorm are real. Graph edges have unit length, the Laplacian is \(2I-T-T^{-1}\) (not normalized by vertex degree), and vertices are indexed modulo \(n\), with \(n\ge3\). The pseudoinverse is taken in ordinary counting-measure Euclidean geometry. Constants form the kernel of the seminorm and of the Laplacian, so the claimed operator acts on functions modulo constants. The source \(f\) need not have zero mean; its constant component is eliminated by \(L^+\).

## Proof
**1. Exact reduction to the zero-sum increment cube.** Put \(D=T-I\), so \(L=D^*D=DD^*\). Since \(D\), \(L\), and \(L^+\) are simultaneously diagonalizable cyclic convolutions, \(DL^+=L^+D\). The image of \(D\) is precisely
\[
E_n=\{s\in\mathbb R^n:\sum_j s_j=0\}.
\]
Indeed every such sequence is the difference sequence of a periodic real function. Therefore
\[
K_n=\sup_{s\in E_n,\ \|s\|_\infty\le1}\|L^+s\|_\infty.
\]
Translation invariance reduces the last norm to one row of \(L^+\).

**2. Kernel and dual median identity.** Let \(G_j\) be as in the finding. Direct cyclic differencing and summation give
\[
\sum_jG_j=0,\qquad 2G_j-G_{j-1}-G_{j+1}=\mathbf1_{\{j=0\}}-\frac1n.
\]
Consequently convolution with \(G\) is precisely \(L^+\). For every real row vector \(g\), one has the elementary exact dual identity
\[
\max_{\|s\|_\infty\le1,\ \sum_js_j=0}g\cdot s
=\min_{c\in\mathbb R}\sum_j|g_j-c|.
\]
To prove the upper bound, subtract \(c\sum_j s_j=0\) and use the triangle inequality. To attain it, choose any median \(c\), set \(s_j=+1\) for \(g_j>c\) and \(s_j=-1\) for \(g_j<c\), then assign \(s_j\in[-1,1]\) on tied entries to make the total zero. The median inequalities guarantee that such an assignment exists. Equality in every term of the triangle inequality gives the entire displayed sign-face classification, including ties. Applying the identity to the Green row proves
\[
K_n=\min_c\sum_{j=0}^{n-1}|G_j-c|.
\]
The absolute value in the row norm is absorbed by negating \(s\).

**3. Four residue classes.** The sequence \(j(n-j)\) strictly increases with the cyclic distance \(k=\min\{j,n-j\}\) until the midpoint. Its multiplicities are one at \(k=0\), two at internal shells, and one at the opposite vertex when \(n\) is even. A median Green value comes from shell
\[
k=\begin{cases}q,&n=4q,4q+1,4q+2,\\q+1,&n=4q+3.\end{cases}
\]
For \(n=4q+2\), any real number between the adjacent shell values is also a median. The finite summation is elementary: use
\[
\sum_{j=1}^qj(n-j)=\frac{nq(q+1)}2-\frac{q(q+1)(2q+1)}6,
\qquad
\sum_{j=0}^{n-1}j(n-j)=\frac{n(n^2-1)}6.
\]
Subtracting the median, grouping the two sides of the shell, and evaluating the resulting sums gives
\[
\begin{array}{c|c|c}
 n&\text{median shell}&\displaystyle\sum_j|G_j-c|\\\hline
4q&q&\dfrac{q^2}2\\[2mm]
4q+1&q&\dfrac{q(4q^2+3q+1)}{2(4q+1)}\\[2mm]
4q+2&q&\dfrac{2q^2+2q+1}4\\[2mm]
4q+3&q+1&\dfrac{(q+1)(4q^2+5q+2)}{2(4q+3)}
\end{array}
\]
The four rational expressions simplify to the asserted formulas. The stated asymptotics are immediate. For \(n=3\), the last row applies with \(q=0\); the remaining cases have \(q\ge1\). This completes the proof, including equality conditions.

## Verification
The accompanying `check_cycle_inverse.py` uses only the Python standard library and exact rational arithmetic. Executing it tests all four rational expressions for cycle lengths \(3\le n<200\), verifies the Green-function residual equation at each position for \(3\le n<23\), and independently exhausts the vertices of the zero-sum unit cube for \(3\le n<13\). Its final outputs include `ALL_FOUR_RESIDUE_FORMULAS_PASSED 197`, `INDEPENDENT_DISCRETE_GREEN_RESIDUALS_PASSED 250`, `EXHAUSTIVE_ZERO_SUM_CUBE_VERTEX_EVALUATIONS_PASSED 4850`, and `ALL_CYCLE_LIPSCHITZ_POISSON_CHECKS_PASSED`. The infinite family and all extremizers follow from the analytical argument; finite checks are corroboration only.

## Relationship to prior work
Ellis (2003), Section 3, Theorem 1, derives the cycle Green kernel for the **normalized** graph Laplacian \(L/2\). Hence that published normalized Green row is twice the unnormalized \(G\) used here. The kernel formula and its recurrence are prior results; the new claim is the sharp cyclic Lipschitz inverse norm, its median-centered optimization, complete equality faces, and explicit four-residue law. No novelty is claimed for the kernel itself or general median duality.

Ilyin, Laptev, and Zelik (2014), especially Introduction and equation (1.2), establish sharp \(\ell^2\)-based discrete Sobolev interpolation inequalities on lattices, not the exact \(\ell^\infty\) first-difference-to-first-difference norm of the **periodic pseudoinverse**. A separate published finite-cycle Riesz-transform calculation derives a cotangent kernel for \(D L^{-1/2}\), a distinct Fourier multiplier from \(D L^+\); its sharp endpoint estimate does not state or imply the inverse-Poisson four-class formula. A published exact Lipschitz norm for an individual Fourier harmonic projection on finite cycles likewise does not cover sharp norms for the full inverse-Laplacian sum, since extremizing sign profiles across frequencies need not coincide.

## Limitations
All norms and equality classifications concern real sequences, unweighted cycles, and the unnormalized Laplacian. They do not claim analogous sharp constants for weighted cycles, complex-valued sequences, the normalized Laplacian without adjustment, or multivariate discrete tori. The relationship between the four-residue values and classical periodic best-constant/Favard inequalities may have implicit older formulations not discovered in the indexed sources; no claim of bibliographic exhaustiveness or independent validation is made.

## References
1. R. B. Ellis, *Discrete Green's functions for products of regular graphs*, arXiv:math/0309080v1, first posted 4 September 2003; revised version arXiv:math/0309080v2, Section 3, Theorem 1 (8 September 2003). https://arxiv.org/abs/math/0309080
2. A. Ilyin, A. Laptev, S. Zelik, *Sharp interpolation inequalities for discrete operators and applications*, arXiv:1407.0675v1, 2 July 2014, especially Introduction and equation (1.2). https://arxiv.org/abs/1407.0675
3. *Cycle Riesz transforms as parity blocks of doubled cyclic Hilbert transforms*, publicly accessible mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-cycle-riesz-transforms-as-parity-blocks-of-doubled-cyclic-hilber--241f167596e5
