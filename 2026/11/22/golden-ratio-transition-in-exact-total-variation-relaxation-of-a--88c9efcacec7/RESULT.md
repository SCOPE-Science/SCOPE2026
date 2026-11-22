# Golden-ratio transition in exact total-variation relaxation of an endpoint-skewed tent map

## Finding
For every real \(0<b<1\), specialize the endpoint-skewed tent map (3) of Moysis et al. to \(a=0\) and \(c=b^2\). Write \(\mathcal L\) for its Perron--Frobenius operator with respect to Lebesgue measure \(m\). If \(m\) is the initial law and \(\nu_b\) its unique absolutely continuous invariant probability, then for every integer \(n\ge0\),
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
Since the three-cell transition graph is primitive and the map is piecewise expanding, the standard finite Markov expanding-map argument gives uniqueness, mixing and absolute continuity of the physical invariant probability. More concretely, \(L_bh_b=h_b\) and the weighted cell lengths sum to one; the transient cell has no stationary absolutely continuous mass. We only need the explicit finite-dimensional action for the claimed convergence of the initial uniform density.

The eigenvalues of \(L_b\) are \(1\), \(b\), and \(-b/(1+b)\). Define
\[
 v_b=(b^2+b-2,b^2+b-1,b^2+b)^{\mathsf T},\qquad
 w_b=(0,-1,b)^{\mathsf T}.
\]
Direct multiplication shows \(L_bv_b=bv_b\), \(L_bw_b=-b(1+b)^{-1}w_b\), and the exact uniform-density decomposition is
\[
(1,1,1)^{\mathsf T}=h_b-\frac{v_b}{(1-b)(b+2)}+\frac{w_b}{(b+2)(1+2b)}.
\]
Consequently the density at time \(n\) is
\[
h_b-\frac{b^n v_b}{(1-b)(b+2)}+\frac{(-b/(1+b))^n w_b}{(b+2)(1+2b)}.
\]
Its deviation on \(J_0\) equals \(b^n>0\). Its deviation on \(J_2\) is strictly negative for every \(n\), because the magnitude of the second eigenmode there is smaller than the first one by a factor at most \((1-b)/[(1+2b)(1+b)]<1\). Since signed density deviations integrate to zero, total variation equals the positive mass on \(J_0\) plus the positive part of the deviation on \(J_1\). Substituting cell lengths gives the stated exact formula for every \(n\ge0\).

The subdominant mode has modulus \(b/(1+b)<b\). The leading deviation on \(J_1\) has sign determined by \(1-b-b^2\). Hence its positive contribution persists in the leading coefficient precisely when \(b<\gamma\). Taking the positive part and simplifying gives the displayed piecewise \(C(b)\). The two branches agree at \(\gamma\); their derivatives differ there (the right derivative is \(2\gamma\), while the left derivative is the derivative of \(b(1+b)/(b+2)\)).

## Verification
The standalone `checks/verify.py` uses symbolic identities for the matrix, normalization, both eigenvectors, and exact decomposition, followed by exact rational comparisons of transfer iteration and total variation through time 16 for \(b=1/4,1/2,2/3,7/8\). These finite tests corroborate algebra; the proof above establishes all \(n\) and all real \(0<b<1\).

## Relationship to prior work
Moysis et al. introduced the three-endpoint-parameter generalized skewed tent map and studied statistical behavior numerically, primarily at \(c=0\). Their published article does not derive the present postcritical \(c=b^2\) three-cell density evolution or exact total-variation law. Previously reported analyses of other Markov or full-branch skew-tent subfamilies address stationary correlations, band exchange, or densities rather than the present entire-initial-Lebesgue transient and golden-ratio prefactor. The elementary matrix method is classical; the parameter-specific sharp formula and prefactor transition are the asserted addition.

## Limitations
Only the exact postcritical curve \(a=0,c=b^2\) and initial uniform Lebesgue law are treated. The result is not a new general spectral theorem for arbitrary densities, does not establish statistical security or pseudorandomness, and does not claim novelty of the underlying Perron--Frobenius technique. Broader literature on interval-map transfer spectra could contain equivalent formulas. No independent audit has been performed.

## References
1. L. Moysis, M. Lawnik, C. Volos, M. S. Baptista and S. K. Goudos, *Chaotic Maps with Tunable Mean Value—Application to a UAV Surveillance Mission*, Symmetry 15 (2023), 2138, https://doi.org/10.3390/sym15122138 (published 2023-12-01).
2. A. Boyarsky and P. Góra, *Laws of Chaos: Invariant Measures and Dynamical Systems in One Dimension*, Birkhäuser, 1997 (standard transfer-operator background; no claim of a literature-wide novelty certification).
