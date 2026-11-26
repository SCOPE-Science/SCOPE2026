# Even-harmonic interpolation on the 120 \(E_8\) root lines: an exact rank reversal and permanent recovery

## Finding

Let \(R\subset\mathbb R^8\) be the 240 normalized \(E_8\) roots, and let \(X\) contain one arbitrary representative from each antipodal pair \(\{x,-x\}\). Thus \(|X|=120\). For each **even integer** \(\ell\ge0\), evaluate all complex spherical harmonics of the *single homogeneous degree* \(\ell\) on \(X\):
\[
E_\ell:\mathcal H_\ell(S^7;\mathbb C)\longrightarrow\mathbb C^{120},\qquad (E_\ell f)_x=f(x).
\]
The rank has the following complete classification:
\[
\boxed{\operatorname{rank}E_\ell=\begin{cases}
1,&\ell=0,\\
35,&\ell=2,\\
84,&\ell=4,\\
119,&\ell\in\{6,10\},\\
120,&\ell=8\text{ or every even }\ell\ge12.
\end{cases}}
\]
Thus degree eight first interpolates *all* antipodally consistent samples, degree ten **loses exactly the mean** despite the degree-eight surjectivity, and every even degree from twelve onward is again surjective. At degrees six and ten the image is exactly the zero-sum subspace; at degree two it is a canonical 35-dimensional orthogonality-graph eigenspace, and at degree four a canonical 84-dimensional eigenspace.

The result also gives the **complete rational spectrum at every even degree**, all image projectors, the unique minimum-spherical-norm interpolant of each admissible data vector, and a uniform eventual stability bound. Specifically, let \(A\) be the adjacency matrix of the orthogonality graph on \(X\), let \(J\) be the all-ones matrix, and put
\[
P_0=J/120,\qquad P_3=(A+9I-72P_0)/12,\qquad P_{-9}=I-P_0-P_3.
\]
These are pairwise orthogonal projections of ranks \(1,84,35\). Define \(a_\ell=C_\ell^{(3)}(1)\), \(b_\ell=C_\ell^{(3)}(1/2)\), \(c_\ell=C_\ell^{(3)}(0)\), where \(C_\ell^{(3)}\) is the Gegenbauer polynomial. The diagonal-one Gram matrix of normalized degree-\(\ell\) zonal harmonics is
\[
K_\ell=\lambda_0P_0+\lambda_3P_3+\lambda_{-9}P_{-9},
\]
with **exact** eigenvalues
\[
\boxed{\lambda_0=\frac{a_\ell+63c_\ell+56b_\ell}{a_\ell},\quad
\lambda_3=\frac{a_\ell+3c_\ell-4b_\ell}{a_\ell},\quad
\lambda_{-9}=\frac{a_\ell-9c_\ell+8b_\ell}{a_\ell}.}
\]
Their respective multiplicities are \(1,84,35\). For \(\ell=2k\ge12\), put
\[
\rho_k=\frac{\frac{63}{2}(k+1)(k+2)+\frac{56}{6}(2k+6)(2k+3)}{\binom{2k+5}{5}}.
\]
Then \(0<\rho_k<1\) and \(1-\rho_k\le\lambda_s\le1+\rho_k\) for every spectral sector \(s\). In particular, the zonal sampling condition number is at most \((1+\rho_k)/(1-\rho_k)\) and tends to one at rate \(O(\ell^{-3})\).

## Assumptions and scope

The normalized roots are the vectors of Euclidean norm one obtained by dividing by \(\sqrt2\) the following 240 vectors:
\[
\{\pm e_i\pm e_j:1\le i<j\le8\}\cup
\left\{\frac12(\varepsilon_1,\ldots,\varepsilon_8):\varepsilon_i\in\{-1,1\},\ \prod_i\varepsilon_i=1\right\}.
\]
Every even harmonic has \(f(-x)=f(x)\), so the evaluation map and its spectrum are independent of which antipodal representatives are selected. The inner product on \(\mathcal H_\ell\) uses surface **probability** measure on \(S^7\); the sample space uses its unweighted Euclidean norm, with no averaging by 120. Only single even degrees are classified; statements about accumulated harmonic bands, odd degrees, and arbitrary perturbations of \(X\) are not asserted.

## Proof

**1. Exact geometry and graph decomposition.** Among the 120 root lines, distinct representatives have absolute inner product \(0\) or \(1/2\). The graph joining orthogonal lines is strongly regular with parameters \((120,63,30,36)\). It follows (or is checked exhaustively from the displayed 240-root construction in `checker.py`) that
\[
A\mathbf1=63\mathbf1,\qquad A^2=27I-6A+36J.
\]
On the orthogonal complement of constants, \(A\) therefore has eigenvalues \(3\) and \(-9\). Their multiplicities are fixed by trace zero and dimension 119: \(84\) and \(35\). Direct substitution verifies that \(P_0,P_3,P_{-9}\) above are their spectral projectors.

**2. Gram spectrum and reconstruction.** The addition formula for spherical harmonics on \(S^7\) states that the probability-normalized degree-\(\ell\) evaluation Gram matrix equals \(h_\ell K_\ell\), where
\[
h_\ell=\dim\mathcal H_\ell=\binom{\ell+7}{7}-\binom{\ell+5}{7}
\]
(the second binomial is zero when its upper argument is smaller than seven). As \(\ell\) is even, the kernel has entry \(1\) on the diagonal, \(c_\ell/a_\ell\) on edges of the orthogonality graph, and \(b_\ell/a_\ell\) on other distinct pairs. Hence
\[
K_\ell=(1-b_\ell/a_\ell)I+(c_\ell-b_\ell)A/a_\ell+(b_\ell/a_\ell)J.
\]
Substitution of the three graph eigenvalues gives exactly the three claimed \(\lambda\)'s.

For any vector \(y\) in the image, its unique minimum-norm harmonic interpolant is the finite, explicit sum
\[
f_y(z)=\sum_{x\in X}(K_\ell^+y)_x\,\frac{C_\ell^{(3)}(\langle z,x\rangle)}{C_\ell^{(3)}(1)},\qquad
K_\ell^+=\sum_{s\in\{0,3,-9\}:\lambda_s>0}\lambda_s^{-1}P_s.
\]
The equality \(E_\ell f_y=y\) follows from \(K_\ell K_\ell^+y=y\), and the Hilbert-space Moore--Penrose identity proves minimality, with exact norm
\[
\|f_y\|_{L^2(S^7)}^2=\frac1{h_\ell}\sum_{s:\lambda_s>0}\frac{\|P_sy\|_2^2}{\lambda_s}.
\]
When a \(\lambda_s\) vanishes, the corresponding projector gives the complete, necessary and sufficient sample constraint \(P_sy=0\).

**3. Explicit rational Gegenbauer contacts.** The generating function
\[
\sum_{\ell\ge0}C_\ell^{(3)}(t)z^\ell=(1-2tz+z^2)^{-3}
\]
gives for \(\ell=2k\):
\[
a_{2k}=\binom{2k+5}{5},\qquad
c_{2k}=(-1)^k\binom{k+2}{2}.
\]
Using \(1-z+z^2=(1+z^3)/(1+z)\) and writing \(2k=3q+r\), \(0\le r\le2\), also gives
\[
b_{2k}=\begin{cases}(-1)^q(q+1),&r=0,\\3(-1)^q\binom{q+2}{2},&r=1,2.\end{cases}
\]
These are integer formulas with no numerical fitting. Direct substitution gives the following exhaustive exceptional table (column labels identify the graph eigenspaces):

| \(\ell\) | \(\lambda_0\) | \(\lambda_3\) | \(\lambda_{-9}\) | rank |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 120 | 0 | 0 | 1 |
| 2 | 0 | 0 | \(24/7\) | 35 |
| 4 | 0 | \(10/7\) | 0 | 84 |
| 6 | 0 | \(10/11\) | \(96/77\) | 119 |
| 8 | \(360/143\) | \(140/143\) | \(144/143\) | 120 |
| 10 | 0 | \(1020/1001\) | \(984/1001\) | 119 |

**4. All-degree positive cutoff and stability.** For every \(k\ge6\), the contact formulas imply
\[
|c_{2k}|=\frac{(k+1)(k+2)}2,\qquad
|b_{2k}|\le\frac{(2k+6)(2k+3)}6.
\]
Set \(B(k)=63(k+1)(k+2)/2+56(2k+6)(2k+3)/6\), the numerator used in \(\rho_k\). The following exact polynomial identity proves strict domination:
\[
15\left(\binom{2k+5}{5}-B(k)\right)=
(k-6)(4k^4+54k^3+409k^2+1534k+5335)+28560>0.
\]
For each of the three displayed eigenvalues, \(|\lambda_s-1|\le B(k)/a_{2k}=\rho_k<1\), proving **strict positivity for every even \(\ell\ge12\)**, the stable condition-number bound, and \(\rho_k=O(k^{-3})\). Together with the complete table through degree ten, this proves every rank and every range statement. In particular, since \(P_0y=\mathbf1(\sum_x y_x)/120\), the degree-six and degree-ten image is exactly the zero-sum subspace.

## Verification

`checker.py` generates all 240 roots as exact eight-tuples, retains precisely 120 antipodal classes, verifies every adjacency/common-neighbor count (hence the stated strongly regular identity), independently evaluates Gegenbauer polynomials by their three-term recurrence, compares the resulting direct Gram action against the three-projector formula in selected degrees through 100, checks all low-degree eigenvalues, and checks the all-degree positivity bound at sample degrees through 100. It ran successfully. The inequality and generating-function manipulations written above—not the finite degree checks—establish the claims for every even degree.

## Relationship to prior work

The spherical-harmonic addition formula and positive-definite Gegenbauer kernels are classical; Cohn and Kumar's *Universally optimal distribution of points on spheres* gives these ingredients and lists the 240 \(E_8\) roots as a spherical 7-design. Schmidt's *Quantum isomorphic strongly regular graphs from the \(E_8\) root system* records the 120-line orthogonality graph and its strongly regular parameters, while referring to earlier graph-theoretic treatments. The present statement specializes these known tools to single-degree **interpolation of arbitrary complex data**, giving an all-even-degree rank classification, the nonmonotone degree-ten obstruction after degree-eight surjectivity, explicit inverse reconstruction, and a global positivity cutoff. Neither inspected full manuscript explicitly supplies this combined degree-wise conclusion. The degree-ten mean obstruction is compatible with the known invariant-theoretic absence of a degree-ten basic \(E_8\) invariant and is not presented as an independent invariant-theory discovery.

## Limitations

The conclusion is not a claim of an independently audited theorem or a new general spherical-design formula. It relies on the known \(E_8\) line geometry and classical harmonic addition formula, whose combination makes the spectral expression relatively short; the all-degree nonvanishing and sampling interpretation are the specific further steps. The 1977 foundational article of Delsarte, Goethals and Seidel was identified but not fully inspected: an implicit equality or rank classification there or elsewhere remains an originality risk. No claim is made about odd degrees, arbitrary point sets, or robustness under point perturbations. Exact Gram calculations certify the 120-point geometry, while the unbounded-degree conclusion comes from the displayed polynomial inequality.

## References

1. H. Cohn and A. Kumar, *Universally optimal distribution of points on spheres*, arXiv:math/0607446, originally publicly posted 2006-07-19; J. Amer. Math. Soc. 20 (2007), 99–148. Sections 1 and 2.2–3 establish the relevant configuration and harmonic kernels.
2. S. Schmidt, *Quantum isomorphic strongly regular graphs from the \(E_8\) root system*, arXiv:2209.14906, originally publicly posted 2022-09-29. Section 3.1 identifies the 120-line orthogonality graph and its parameters.
3. Ph. Delsarte, J. M. Goethals and J. J. Seidel, *Spherical codes and designs*, Geom. Dedicata 6 (1977), 363–388, DOI:10.1007/BF03187604 (historical relevant source; full-text comparison not completed).
