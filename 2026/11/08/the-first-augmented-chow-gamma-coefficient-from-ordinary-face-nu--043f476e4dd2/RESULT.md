# The first augmented-Chow gamma coefficient from ordinary face numbers, and simplex minimality through dimension four

## Finding
Let \(P\) be any convex polytope of dimension \(n\geq1\), and let \(f_j(P)\) count its \(j\)-dimensional nonempty proper faces, \(0\leq j\leq n-1\). Write \(F_P^R(z)\) and \(F_P^L(z)\) for the right and left augmented Chow polynomials of the bounded face poset, with gamma expansions
\[
F_P^{\varepsilon}(z)=(1+z)^{n+1}\sum_{q=0}^{\lfloor(n+1)/2\rfloor}\gamma_q^{\varepsilon}(P)\left(\frac{z}{(1+z)^2}\right)^q,\qquad\varepsilon\in\{R,L\}.
\]
The first coefficients are determined by the ordinary face vector in *every* dimension:
\[
\boxed{\begin{aligned}
\gamma_1^R(P)&=\sum_{j=0}^{n-1}f_j(P)+f_{n-1}(P)-2n-1,\\
\gamma_1^L(P)&=\sum_{j=0}^{n-1}f_j(P)+f_0(P)-2n-1.
\end{aligned}}
\]
In particular, their difference records exactly the vertex–facet imbalance:
\[
\gamma_1^R(P)-\gamma_1^L(P)=f_{n-1}(P)-f_0(P).
\]
For either side and any \(n\geq1\),
\[
\boxed{\gamma_1^{\varepsilon}(P)\geq2^{n+1}-n-2,}
\]
with equality if and only if \(P\) is a simplex.

Moreover, **for every convex polytope of dimensions \(1\leq n\leq4\)** the entire right and left gamma vectors are coefficientwise at least the corresponding simplex gamma vector. These simplex gamma vectors, in ascending dimension, are
\[
(1,1),\quad(1,4),\quad(1,11,5),\quad(1,26,43).
\]
For \(n=2,3,4\), every non-simplex has *strictly larger* coefficients in every positive gamma degree. No full gamma-minimality assertion is made for dimensions \(n\geq5\).

## Assumptions and scope
Use the standard noncommutative \(\mathbf{cd}\)-index of the face lattice of an \(n\)-polytope, normalized by \(\mathbf c=\mathbf a+\mathbf b\), \(\mathbf d=\mathbf{ab}+\mathbf{ba}\). Its top word has coefficient one and its total \(\mathbf{cd}\)-degree is \(n\). Augmented Chow polynomials and the gamma-word functional are normalized exactly as in Faustini–Ferroni–Piazza, Proposition 6.3 (2026). The duality \(F_P^L=F_{P^*}^R\) is the same paper's convention. The case \(n=1\) is included; it is the single combinatorial type of segment.

## Proof
**Step 1: isolate the linear gamma coefficient.** For \(n\geq2\), decompose the \(\mathbf{cd}\)-index into terms with zero, one, and at least two letters \(\mathbf d\):
\[
\Phi_P=\mathbf c^n+\sum_{j=0}^{n-2}b_j\mathbf c^j\mathbf d\mathbf c^{n-j-2}+\Psi_{\geq2\mathbf d}.
\]
Proposition 6.3 of Faustini–Ferroni–Piazza gives a gamma polynomial \(\Gamma(w,t)\) for each \(\mathbf{cd}\)-word. Expanding its explicit Catalan formula at \(t=0\) yields
\[
[t]\Gamma(\mathbf c^n,t)=1,\qquad
[t]\Gamma(\mathbf c^j\mathbf d\mathbf c^{n-j-2},t)=2+\mathbf1_{\{j=n-2\}},
\]
while every word with two or more \(\mathbf d\)'s has no term of degree one. Linearity therefore gives
\[
\gamma_1^R(P)=1+2\sum_{j=0}^{n-2}b_j+b_{n-2}.
\]

**Step 2: eliminate the flag coefficients.** In the \(\mathbf{ab}\)-index, the coefficient of the length-\(n\) word with its sole \(\mathbf b\) in position \(k\) is \(f_{k-1}(P)-1\), because the corresponding flag-\(h\) number equals \(f_{k-1}-1\). In the expansion of \(\Phi_P\), that word receives coefficient one from \(\mathbf c^n\) and coefficient \(b_{k-2}+b_{k-1}\) from the one-\(\mathbf d\) terms, using boundary conventions \(b_{-1}=b_{n-1}=0\). Hence
\[
f_{k-1}(P)-2=b_{k-2}+b_{k-1}\quad(1\leq k\leq n).
\]
Summation gives \(\sum_{k=0}^{n-1}(f_k-2)=2\sum_jb_j\), and setting \(k=n\) gives \(b_{n-2}=f_{n-1}-2\). Substitution proves the right-hand face-vector identity. The unique segment has \(\Phi=\mathbf c\) and \(\Gamma(\mathbf c,t)=1+t\), establishing the same identity for \(n=1\). The left-hand identity follows by replacing \(P\) with its combinatorial polar dual and observing \(f_j(P^*)=f_{n-j-1}(P)\).

**Step 3: sharp first-coefficient lower bound.** Billera–Ehrenborg, Theorem 5.3, states that \(\Phi_P-\Phi_{\Delta_n}\) has nonnegative coefficients in every \(\mathbf{cd}\)-word. All one-\(\mathbf d\) weights in Step 1 are strictly positive, so \(\gamma_1^R(P)\geq\gamma_1^R(\Delta_n)\). The simplex face vector gives \(\gamma_1^R(\Delta_n)=2^{n+1}-n-2\). If equality holds, the coefficient \(b_0=f_0-2\) (for \(n\geq2\)) must equal its simplex value, so \(f_0=n+1\). Every \(n\)-polytope on exactly \(n+1\) vertices is a simplex. Conversely, simplices attain equality. Applying duality proves the left-sided assertion and its equality case.

**Step 4: the full conjectured comparison through dimension four.** The source formula produces the following *complete* gamma-word table (the parameter is \(t\)):

| Degree | Word | Gamma polynomial |
| --- | --- | --- |
| 1 | \(\mathbf c\) | \(1+t\) |
| 2 | \(\mathbf c^2\), \(\mathbf d\) | \(1+t\), \(3t\) |
| 3 | \(\mathbf c^3\), \(\mathbf{cd}\), \(\mathbf{dc}\) | \(1+t-t^2\), \(3t+t^2\), \(2t+2t^2\) |
| 4 | \(\mathbf c^4\), \(\mathbf c^2\mathbf d\), \(\mathbf{cdc}\), \(\mathbf d\mathbf c^2\), \(\mathbf d^2\) | \(1+t-t^2\), \(3t+t^2\), \(2t+2t^2\), \(2t+t^2\), \(7t^2\) |

Every listed word *other than the leading \(\mathbf c^n\)* has a coefficientwise nonnegative gamma polynomial. The leading coefficient is identically one in every polytope's \(\mathbf{cd}\)-index. Consequently the Billera–Ehrenborg theorem, applied to the difference \(\Phi_P-\Phi_{\Delta_n}\), proves coefficientwise gamma minimality on the right for \(n\leq4\). Duality proves it on the left. For \(n=2,3,4\), each one-\(\mathbf d\) word has strictly positive gamma coefficient in *each* positive degree that exists, while a non-simplex has positive surplus in at least the coefficient of the word starting with \(\mathbf d\) (because \(f_0>n+1\)); hence strictness in every positive degree. Finally, enumerating chains in the simplex Boolean face lattice and converting its flag-\(h\) vector to its \(\mathbf{cd}\)-index gives
\[
\begin{aligned}
\Phi_{\Delta_1}&=\mathbf c,\\
\Phi_{\Delta_2}&=\mathbf c^2+\mathbf d,\\
\Phi_{\Delta_3}&=\mathbf c^3+2\mathbf{cd}+2\mathbf{dc},\\
\Phi_{\Delta_4}&=\mathbf c^4+3\mathbf c^2\mathbf d+5\mathbf{cdc}+3\mathbf d\mathbf c^2+4\mathbf d^2.
\end{aligned}
\]
Applying the table gives exactly the four claimed simplex gamma vectors.

## Verification
Run `python3 verify_gamma.py` using Python 3.9 or newer and no optional dependencies. The program reconstructs flag-chain numbers of simplices from multinomial counts, computes flag-\(h\) coefficients by subset inversion, solves for \(\mathbf{cd}\)-coefficients by rational linear algebra, and independently applies Proposition 6.3's Catalan polynomial formula. It checks every word of degrees one through four, all one-\(\mathbf d\) linear coefficients through degree 29, polygon cases with 3 through 30 vertices, and one cube/polar-dual example. Its recorded output was `PASS 523 exact checks`.

The unbounded portions of this theorem are established by the symbolic proof in Steps 1–3, not by finite computation. The low-dimensional exhaustiveness follows because there are exactly the listed \(\mathbf{cd}\)-monomials in degrees at most four.

## Relationship to prior work
Faustini, Ferroni and Piazza (2026, arXiv:2609.22078, first public September 18, 2026), Proposition 6.3 and Theorem 6.9, give the gamma-word formula and gamma-positivity for face posets, and expressly conjecture coefficientwise simplex minimality. The proof here uses their formula to recover an ordinary-face-vector identity and to establish the entire conjectured comparison in dimensions at most four. Billera and Ehrenborg (2000, Theorem 5.3) provide coefficientwise simplex minimality of the underlying \(\mathbf{cd}\)-index. Their theorem does **not**, by itself, prove the gamma conjecture in every dimension, because the gamma transformation does not preserve coefficientwise nonnegativity on arbitrary \(\mathbf{cd}\)-monomials in degree five and above. This result explicitly combines those published ingredients; it does not claim a new general \(\mathbf{cd}\)-index inequality.

## Limitations
The dimensional cutoff concerns what is established here, not a counterexample to the higher-dimensional conjecture. For example, the degree-five word \(\mathbf c^3\mathbf d\) has a *negative* coefficient of \(t^3\) in its gamma polynomial. This only obstructs the simple termwise nonnegativity argument; it does **not** imply that any polytope violates simplex minimality. The result concerns convex polytopes and the source-normalized augmented Chow polynomials of their bounded face posets, not arbitrary Eulerian posets. The proof depends on the cited published gamma-word identity and classical \(\mathbf{cd}\)-monotonicity theorem. Historical priority requires separate confirmation; no independent audit has been performed.

## References
1. T. Faustini, L. Ferroni, L. Piazza, *Stellahedral geometry of partially ordered sets*, arXiv:2609.22078 (first version September 18, 2026), Proposition 6.3 and Theorem 6.9. https://arxiv.org/html/2609.22078v2
2. L. J. Billera and R. Ehrenborg, *Monotonicity of the cd-index for polytopes*, Mathematische Zeitschrift 233 (2000), 421–441, Theorem 5.3. Author-hosted copy: https://www.ms.uky.edu/~jrge/Papers/Monotone.pdf
