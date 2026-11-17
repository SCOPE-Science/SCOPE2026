# Exact fourth-order Gauss–Legendre positivity on the weighted three-leaf star

## Finding
Let \(G\) be the four-vertex star with hub \(0\), leaves \(1,2,3\), and arbitrary edge conductances \(a,b,c>0\) on \(01,02,03\), respectively. Let \(L\) be its symmetric combinatorial weighted Laplacian and let
\[
T(h)=F(hL),\qquad F(z)=\frac{z^2-6z+12}{z^2+6z+12},\qquad h\geq0.
\]
This is the completed end-step transition of the two-stage, order-four Gauss–Legendre Runge–Kutta method for \(\dot u=-Lu\). Then
\[
\boxed{\ T(h)\geq0\text{ entrywise for every }h\geq0
\quad\Longleftrightarrow\quad
\begin{cases}
3bc\geq a(b+c),\\
3ac\geq b(a+c),\\
3ab\geq c(a+b).
\end{cases}\ }
\]
Equivalently, if \(r_1=1/a\), \(r_2=1/b\), \(r_3=1/c\), and \(S=r_1+r_2+r_3\), the condition is \(4r_i\geq S\) for each leaf. Every entry of \(T(h)\) is strictly positive for every \(h>0\) when the condition holds. When one inequality fails, the corresponding hub-to-leaf entry is negative at every sufficiently large timestep. In all cases \(T(h)\mathbf1=\mathbf1\), so the failure is positivity, not mass conservation.

## Assumptions and scope
The graph has exactly the four labeled vertices and the three undirected positive-conductance edges described above, with no other edges, killing, boundary loss, or normalization by vertex degree. The Laplacian is
\[
L=\begin{pmatrix}
a+b+c&-a&-b&-c\\
-a&a&0&0\\
-b&0&b&0\\
-c&0&0&c
\end{pmatrix}.
\]
All quantifiers range over real \(a,b,c>0\) and \(h\in[0,\infty)\). Nonnegativity concerns the completed matrix \(T(h)\), not the internal Runge–Kutta stages. The limiting case \(h=0\) gives the identity matrix, while the strict-positivity statement is for finite \(h>0\).

## Proof
Write \(M(h)=h^2L^2+6hL+12I\), \(N(h)=h^2L^2-6hL+12I\), and \(D(h)=\det M(h)/48\). Every eigenvalue \(\lambda\) of \(L\) is nonnegative; hence the eigenvalues \((h\lambda)^2+6h\lambda+12\) of \(M(h)\) are strictly positive. Thus \(D(h)>0\) for every \(h\geq0\), and \(T(h)=M(h)^{-1}N(h)\).

Define \(C_a=3bc-a(b+c)\) and similarly \(C_b=3ac-b(a+c)\), \(C_c=3ab-c(a+b)\). Direct adjugate multiplication gives the following **exact** rational formulas, valid for all positive conductances and all \(h\geq0\):
\[
[T(h)]_{01}=\frac{3ah}{D(h)}A_a(h),
\]
where
\[
\begin{aligned}
A_a(h)={}&bcC_a h^4+12bc(b+c-a)h^3\\
&+12\bigl(2b^2+3bc+2c^2-a(b+c)\bigr)h^2\\
&+72(b+c)h+144.
\end{aligned}
\]
The corresponding formulas for the other hub-to-leaf entries follow by simultaneous permutation of \(a,b,c\) and labels \(1,2,3\). For two distinct leaves, the corresponding formula is
\[
[T(h)]_{12}=\frac{3ab h^2}{D(h)}B_{ab}(h),
\]
with
\[
\begin{aligned}
B_{ab}(h)={}&c\bigl(3c(a+b)-ab\bigr)h^3\\
&+12c(a+b+c)h^2+24(a+b+2c)h+72.
\end{aligned}
\]
Again, the other leaf-to-leaf entries follow by permutation. These identities can be checked exactly by expansion in the integer polynomial ring \(\mathbb Z[h,a,b,c]\); the accompanying standard-library checker verifies all six identities without floating point.

Suppose \(C_a,C_b,C_c\geq0\). From \(C_a\geq0\) and \(4bc\leq(b+c)^2\),
\[
a\leq\frac{3bc}{b+c}\leq\frac34(b+c)<b+c,
\]
and
\[
2b^2+3bc+2c^2-a(b+c)\geq2b^2+2c^2>0.
\]
Therefore every coefficient of \(A_a\) is nonnegative, and its constant term is positive. This holds for all hub-to-leaf entries by permutation. For leaf pair \(1,2\), \(C_a\geq0\) implies \(3bc\geq a(b+c)>ab\), hence \(3c>a\), so \(3c(a+b)>ab\). Every coefficient of \(B_{ab}\) is consequently strictly positive. The other leaf-pair cases follow by permutation. All off-diagonal entries of \(T(h)\) are therefore strictly positive for every \(h>0\).

For a diagonal entry, \(F(x)>0\) for every \(x\geq0\), because its numerator is \((x-3)^2+3\) and its denominator is \((x+3)^2+3\). Since \(L\) is symmetric, \(T(h)\) is positive definite, so every diagonal entry is strictly positive. This proves sufficiency, including all boundary equality cases.

Conversely, suppose \(C_a<0\). The leading term of \(A_a(h)\) is \(bcC_a h^4\), which is negative. Hence \(A_a(h)<0\) for every sufficiently large \(h\), and the displayed formula gives \([T(h)]_{01}<0\). If \(C_b<0\) or \(C_c<0\), relabeling gives the analogous negative hub-to-leaf entry. This proves necessity and the exact classification.

For interpretation of the obstruction, direct inversion on the mean-zero subspace gives
\[
(L^+)_{01}=-\frac{C_a}{16abc},\qquad
[T(h)]_{01}=\frac{3C_a}{4abc\,h}+O(h^{-2})\quad(h\to\infty).
\]
The known weighted-star group-inverse \(M\)-matrix condition is exactly the three inequalities above. The additional assertion proved here is that on this four-vertex branching graph this *large-step necessary condition* is also sufficient for positivity of the fourth-order rational map at **every** intermediate timestep.

## Verification
Run `python3 verify.py` using Python 3.9 or newer. The script constructs \(L\), \(M\), \(N\), and all six rational off-diagonal numerators as sparse integer polynomials and compares them coefficient-for-coefficient with the identities in the proof. It then checks the exact negative witness
\[
a=4,\quad b=c=1,\quad h=8,\qquad [T(8)]_{01}=-\frac{6240}{106309}<0.
\]
Successful output ends with `EXACT_POLYNOMIAL_IDENTITIES_OK`. The sign argument in the proof, not a finite numerical sweep, establishes the all-weights and all-timesteps assertion.

## Relationship to prior work
Zappavigna, Colaneri, Kirkland and Shorten's work on Padé discretizations supplies the original high-order positivity problem, examples of failure in general positive systems, and step-restricted sufficient conditions. Lóczi and Ketcheson develop global absolute-monotonicity bounds for rational Runge–Kutta stability functions; those do not classify a fixed weighted star for every timestep. The 1998 weighted-tree group-inverse classification by Kirkland and Neumann, restated in Carmona, Encinas, Patra and Sivakumar's 2026 full-text Corollary 4.14, already determines exactly when \(L^+\) is an \(M\)-matrix. The conductance inequalities themselves are **not** proposed as previously unknown; their exact sufficiency for all-step fourth-order Gauss–Legendre positivity on \(K_{1,3}\) is the specific additional conclusion. A published eight-state Padé/Markov positivity result concerns unrestricted chains and a small-step minimal dimension rather than the present four-state weighted reversible graph.

## Limitations
No analogous iff claim is made for arbitrary larger weighted stars, other graph families, other Runge–Kutta methods, or internal stages. The argument assumes exact arithmetic and strictly positive edge conductances. The proof supplies an all-timestep sign classification, not an error or efficiency bound. The existing group-inverse literature makes the boundary itself known; only the rational-method equivalence and intermediate-step positivity are assessed here. Wider publication-priority uncertainty remains.

## References
1. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, *Essentially Negative News About Positive Systems*, publicly deposited 19 June 2012, https://mural.maynoothuniversity.ie/id/eprint/3761/ ; PDF https://mural.maynoothuniversity.ie/id/eprint/3761/1/SK_Essentially_Negative.pdf .
2. L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, arXiv:1303.6651v1, first submitted 26 March 2013, https://arxiv.org/html/1303.6651v1 .
3. S. J. Kirkland and M. Neumann, *The M-matrix group inverse problem for weighted trees*, SIAM J. Matrix Anal. Appl. **19** (1998), 226–234, https://doi.org/10.1137/S0895479896304927 .
4. Á. Carmona, A. M. Encinas, S. Patra and K. C. Sivakumar, *The M-matrix group inverse problem for star networks*, Comput. Appl. Math. **45** (2026), article 272, https://doi.org/10.1007/s40314-026-03651-2 .
5. *Eight-state barrier for Markov positivity of the [2/2] Padé map*, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab .
