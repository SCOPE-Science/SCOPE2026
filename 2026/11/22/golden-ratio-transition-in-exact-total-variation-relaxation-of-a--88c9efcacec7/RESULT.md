# Golden-ratio transition in exact total-variation relaxation of an endpoint-skewed tent map

## Finding
For every real \(0<b<1\), let \(T_b\) be the endpoint-skewed tent map specified below, with peak at \(b\) and right endpoint value \(b^2\). If Lebesgue probability \(m\) on \([0,1]\) is the initial law and \(\nu_b\) is the unique absolutely continuous invariant probability of \(T_b\), then for every integer \(n\ge0\),
\[
\begin{split}
\|T_b^n{}_*m-\nu_b\|_{\mathrm{TV}}={}&b^{n+2} \\
&+\frac{b(1-b)b^n}{b+2}\left[\frac{1-b-b^2}{1-b}-\frac{(-1)^n}{(1+2b)(1+b)^n}\right]_+.
\end{split}
\]
Here \([u]_+=\max(u,0)\). Define \(\gamma=(\sqrt5-1)/2\). There is an exact, sharp asymptotic
\[
\|T_b^n{}_*m-\nu_b\|_{\mathrm{TV}}=C(b)b^n+O_b\left((b/(1+b))^n\right),\quad
C(b)=\begin{cases}\displaystyle \frac{b(1+b)}{b+2},&0<b\le\gamma,\\ b^2,&\gamma\le b<1.\end{cases}
\]
The leading mixing prefactor changes its algebraic formula, with a genuine first-derivative corner at the golden-ratio conjugate \(b=\gamma\), although the decay eigenvalue \(b\) is smooth. The probability of still lying in the transient interval \([0,b^2)\) after \(n\) iterates is *exactly* \(b^{n+2}\). Thus for \(b>\gamma\), this transient mass supplies the full leading total-variation error; for \(b<\gamma\), a second cell contributes an additional leading mass.

## Assumptions and scope
The map is the continuous piecewise-affine function on \([0,1]\)
\[
T_b(x)=\begin{cases} x/b,&0\le x\le b,\\ b^2+(1+b)(1-x),&b<x\le1.\end{cases}
\]
The initial law is **normalized Lebesgue probability on the entire interval**, not an arbitrary initial density. The total-variation convention is \(\|p-q\|_{\mathrm{TV}}=\tfrac12\int_0^1|p-q|\,dx\). The theorem is pointwise in \(b\); no parameter-uniform error estimate at endpoints is claimed. Endpoints of Markov cells have measure zero.

## Proof
Set \(J_0=[0,b^2)\), \(J_1=[b^2,b)\), \(J_2=[b,1]\), with lengths \(b^2,b-b^2,1-b\). The orbit of the critical point is \(b\mapsto1\mapsto b^2\mapsto b\); hence these form a Markov partition with \(T_b(J_0)=J_0\cup J_1\), \(T_b(J_1)=J_2\), \(T_b(J_2)=J_1\cup J_2\), interpreted modulo endpoints. The absolute slopes are \(1/b\) on the first two cells and \(1+b\) on the third, both strictly exceeding one. For densities constant on each cell, the Perron--Frobenius operator is the matrix
\[
L_b=\begin{pmatrix}b&0&0\\b&0&(1+b)^{-1}\\0&b&(1+b)^{-1}\end{pmatrix}.
\]
Its normalized fixed density, in cell-value coordinates, is
\[
h_b=\frac{1}{(1-b)(1+2b)}\begin{pmatrix}0\\1\\1+b\end{pmatrix}.
\]
Here \(L_bh_b=h_b\), the cell values weighted by cell lengths sum to one, and the invariant density gives zero mass to the transient cell \(J_0\). The full three-cell graph is not irreducible: only the closed class \(J_1,J_2\) is primitive.

The eigenvalues of \(L_b\) are \(1\), \(b\), and \(-b/(1+b)\). Define
\[
 v_b=(b^2+b-2,b^2+b-1,b^2+b)^{\mathsf T},\qquad
 w_b=(0,-1,b)^{\mathsf T}.
\]
Direct multiplication shows \(L_bv_b=bv_b\), \(L_bw_b=-b(1+b)^{-1}w_b\), and the exact uniform-density decomposition is
\[
 (1,1,1)^{\mathsf T}=h_b-\frac{v_b}{(1-b)(b+2)}+\frac{w_b}{(b+2)(1+2b)}.
\]
To show uniqueness among all absolutely continuous probabilities, refine the cells by the itineraries through time \(k\). Each positive-length refined interval maps affinely onto a whole cell under \(T_b^k\), by the Markov property. If \(\rho=\max\{b,(1+b)^{-1}\}<1\), its length is at most \(\rho^k\). Averaging an \(L^1\) density on these refining intervals approximates it in \(L^1\) as \(k\to\infty\) (first approximate by a continuous function and use the shrinking mesh). For each fixed \(k\), the averaged probability density transfers after \(k\) steps to a cell-constant probability density, which then converges in \(L^1\) to \(h_b\) by the three eigenvalues above and conservation of mass. The transfer operator contracts \(L^1\), so the unaveraged density also converges in \(L^1\) to \(h_b\). An invariant absolutely continuous density must therefore equal \(h_b\).

For the uniform initial law the decomposition gives the density at time \(n\) explicitly:
\[
h_b-\frac{b^n v_b}{(1-b)(b+2)}+\frac{(-b/(1+b))^n w_b}{(b+2)(1+2b)}.
\]
Its deviation on \(J_0\) equals \(b^n>0\). Its deviation on \(J_2\) is strictly negative for every \(n\), because the magnitude of the second eigenmode there is smaller than the first one by a factor at most \((1-b)/[(1+2b)(1+b)]<1\). Since signed density deviations integrate to zero, total variation equals the positive mass on \(J_0\) plus the positive part of the deviation on \(J_1\). Substituting cell lengths gives the stated exact formula for every \(n\ge0\).

The subdominant mode has modulus \(b/(1+b)<b\). Since the positive-part function is 1-Lipschitz, dropping that mode from the exact formula costs at most \(O_b((b/(1+b))^n)\), even at \(b=\gamma\). The positive contribution of \(J_1\) to the leading coefficient occurs precisely when \(1-b-b^2>0\). The two expressions for \(C(b)\) agree at \(\gamma\); the left branch minus the right branch is \(b(1-b-b^2)/(b+2)\), with derivative \(-\gamma(1+2\gamma)/(\gamma+2)<0\) at \(\gamma\).

## Verification
The standalone `checks/verify.py` requires SymPy. It checks symbolic identities for the matrix, normalization, both eigenvectors, and exact decomposition, followed by exact rational comparisons of transfer iteration and total variation through time 16 for \(b=1/4,1/2,2/3,7/8\). These finite tests corroborate algebra; the proof above establishes uniqueness and the formula for all \(n\) and all real \(0<b<1\).

## Relationship to prior work
The endpoint-parameter tent-map family is attributed to Moysis et al. [1]; the map here is defined independently by the displayed branch formulas. For comparison, the golden-mean tent map on its invariant interval has an exact six-step total-variation contraction for piecewise-affine densities [3]. At \(b=\gamma\) its invariant-interval map is affinely conjugate to the restriction of \(T_b\) to \([b^2,1]\): both branches have absolute slope \(1/\gamma\) and the maps have the same normalized endpoint and peak values. This does not include the transient interval or describe its initial mass, and it does not address variation in \(b\). The matrix method is classical; the claim concerns the sharp whole-interval formula and prefactor transition for this family, not a new technique or exhaustive publication-priority determination.

## Limitations
Only the exact postcritical curve and initial uniform Lebesgue law are treated by the quantitative formula. The qualitative uniqueness argument does not give a comparable rate for arbitrary absolutely continuous initial laws. The result does not establish statistical security or pseudorandomness. Broader literature on interval-map transfer spectra could contain equivalent formulas.

## References
1. L. Moysis, M. Lawnik, C. Volos, M. S. Baptista and S. K. Goudos, *Chaotic Maps with Tunable Mean Value—Application to a UAV Surveillance Mission*, Symmetry 15 (2023), 2138, https://doi.org/10.3390/sym15122138 (published 2023-12-01).
2. A. Boyarsky and P. Góra, *Laws of Chaos: Invariant Measures and Dynamical Systems in One Dimension*, Birkhäuser, 1997 (standard transfer-operator background; no claim of a literature-wide novelty certification).
3. *Exact six-step density relaxation and alternating correlations of the golden-mean tent map*, https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-exact-six-step-density-relaxation-and-alternating-correlations-o--006ba8e20665.
