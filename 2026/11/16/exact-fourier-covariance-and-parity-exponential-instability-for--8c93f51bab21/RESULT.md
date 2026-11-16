# Exact Fourier covariance and parity-exponential instability for perfect matchings of cyclic prisms

## Finding

Let \(P_n=C_n\square K_2\) be the simple cyclic prism for each integer \(n\ge3\). Sample uniformly from its perfect matchings. Index the \(3n\) edge indicators by the two rails and rungs, and let \(C_n\) be their covariance matrix. Define Fibonacci numbers by \(F_0=0,F_1=1\), Lucas numbers by \(L_0=2,L_1=1\), and
\[
 Z_n=L_n+2\mathbf1_{\{2\mid n\}},\qquad
 g(t)=\frac{4+2t}{3+2t}.
\]
Then the **complete list of positive eigenvalues of \(C_n\), with multiplicity indexed by Fourier frequency**, is
\[
\lambda_{n,k}=\frac{F_n}{Z_n}g\!\left(\cos\frac{2\pi k}{n}\right),\quad 1\le k\le n-1,
\]
with the additional zero-frequency eigenvalue
\[
\lambda_{n,0}=\begin{cases}
\dfrac65\left(\dfrac{F_n}{L_n}-\dfrac{n}{L_n^2}\right),&n\text{ odd},\\[5pt]
\dfrac{6F_n+3n}{5Z_n},&n\text{ even},
\end{cases}
\]
and, **only when \(n\) is even**, one rail-antisymmetric eigenvalue \(\lambda^-_n=n/Z_n\). All other eigenvalues vanish. Hence \(\operatorname{rank}C_n=n\) for odd \(n\), and \(n+1\) for even \(n\). The probability-normalized Gram matrix of centered edge Walsh characters is \(4C_n\), with the same positive spectral condition ratio.

For odd \(n\), the least positive mode is zero frequency and the greatest is the pair of Fourier frequencies \(k=(n\pm1)/2\). In this case the **exact sharp condition ratio** is
\[
\kappa_n=\frac56\frac{4-2\cos(\pi/n)}{3-2\cos(\pi/n)}\frac{F_nL_n}{F_nL_n-n}
\longrightarrow\frac53\qquad(n\to\infty\text{ through odd integers}).
\]
For every even \(n\ge4\), the greatest eigenvalue is the alternating symmetric mode \(2F_n/Z_n\), while the least positive eigenvalue is the antisymmetric mode \(n/Z_n\), so
\[
\boxed{\kappa_n=\frac{2F_n}{n}\sim\frac2{\sqrt5}\frac{\phi^n}{n}}
\qquad(n\to\infty\text{ through even integers}),\qquad \phi=\frac{1+\sqrt5}2.
\]
At \(n=4\), the greatest eigenvalue also occurs at zero frequency and the least positive eigenvalue additionally occurs at both quarter-turn Fourier frequencies. These are the only extra extrema ties. The parity contrast is exponential-versus-bounded conditioning.

## Assumptions and scope

The cycle vertices are numbered modulo \(n\). Let \(T_i\) and \(B_i\) denote the indicators for top and bottom edges between columns \(i\) and \(i+1\); let \(V_i\) be the rung indicator in column \(i\). Covariance means expectation under the uniform law on all perfect matchings, not on arbitrary matchings, and no external normalization beyond counting probability. Define centered Walsh coordinates \(W_e=(-1)^{X_e}-\mathbb E[(-1)^{X_e}]\). Since \(W_e=-2(X_e-\mathbb EX_e)\), their Gram matrix is exactly \(4C_n\). Singular directions are excluded from \(\kappa_n\); the theorem does not claim a Riesz family on all \(3n\) edge coordinates.

## Proof

**1. Decompose all perfect matchings.** The perfect-matching relations at the two vertices in each column give
\[
V_i+T_{i-1}+T_i=1,\qquad V_i+B_{i-1}+B_i=1.
\]
Set \(S_i=(T_i+B_i)/2\) and \(D_i=(T_i-B_i)/2\). Then
\[
 V_i=1-S_{i-1}-S_i,\qquad D_i=-D_{i-1}.
\]
For odd \(n\), the latter equation forces \(D_i=0\) for all \(i\), so the two rail matchings coincide. Each such perfect matching is uniquely encoded by a matching of edges of the base cycle: put \(S_i=1\) precisely on selected pairwise nonadjacent edges; the remaining columns carry rungs. This correspondence also holds for even \(n\) if any rung occurs. When \(n\) is even, precisely two further matchings have no rung and alternating opposite rail edges: \(S_i=1/2\) and \(D_i=\pm(-1)^i/2\). Thus the total count is \(Z_n=L_n+2\mathbf1_{\{2\mid n\}}\), consistent with Lekshmi–West (2020). Exchanging the rails sends \(D\) to \(-D\) and fixes \(S\), so \(\operatorname{Cov}(S,D)=0\).

**2. Exact cyclic pair kernel.** In the ordinary base-cycle matching ensemble, write \(A_i\) for the indicator of selecting cycle edge \(i\) and \(K=\sum_i A_i\). The unnormalized singleton and pair counts are
\[
\sum_M A_0=F_{n-1},\qquad
B_d:=\sum_M A_0A_d=F_{d-1}F_{n-d-1}\quad(0\le d<n),
\]
where the boundary convention \(F_{-1}=1\) is used only for \(d=0\). The identity \(5F_rF_s=L_{r+s}-(-1)^sL_{r-s}\), combined with \(L_{j+2}+L_{j-2}=3L_j\), proves for the interior distances \(2\le d\le n-2\) the following cyclic kernel identity. At \(d=0\) it reduces to \(3F_{n-1}=L_{n-2}+F_n\), and at \(d=1,n-1\) it reduces to \(F_{n-1}+F_{n-3}=L_{n-2}\). Thus for every \(d\bmod n\)
\[
3B_d+B_{d-1}+B_{d+1}=L_{n-2}+F_n\mathbf1_{\{d=0\}}.
\tag{1}
\]
The exceptional even matchings have constant \(S_i=1/2\), so their contribution to the \(S\)-covariance is spatially constant and disappears at nonzero Fourier frequency; the rank-one mean subtraction also disappears there. Fourier-transforming (1), for every \(k\ne0\), yields
\[
\widehat{\operatorname{Cov}(S)}(k)=\frac{F_n}{Z_n(3+2\cos(2\pi k/n))}.
\]
The linear map from the \(S\)-sector to the full edge vector has frequencywise squared norm multiplier
\[
2+|1+e^{2\pi ik/n}|^2=4+2\cos(2\pi k/n).
\]
This proves the stated \(n-1\) nonzero-frequency eigenvalues.

**3. Zero frequency and exceptional Fourier sector.** The base-cycle matching-size partition polynomial is
\[
T_n(t)=\alpha(t)^n+\beta(t)^n,\qquad
\alpha(t),\beta(t)=\frac{1\pm\sqrt{1+4t}}2.
\]
Direct differentiation at \(t=1\) gives \(T_n(1)=L_n\), \(T_n'(1)=nF_{n-1}\), and
\[
T_n''(1)=\frac{n(n-1)}5L_{n-2}-\frac{2n}5F_{n-1}.
\]
Consequently the variance of \(K\), divided by \(n\), is exactly
\[
\frac{\operatorname{Var}(K)}n=\frac{F_n}{5L_n}+\frac{(-1)^n n}{5L_n^2},
\]
using \(L_n^2-5F_n^2=4(-1)^n\). For odd \(n\), this is the Fourier-zero variance of \(S\). For even \(n\), include the two additional configurations, both having \(\sum_iS_i=n/2\); their mixture with the base-cycle configurations gives
\[
\widehat{\operatorname{Cov}(S)}(0)=\frac{F_n+n/2}{5Z_n}.
\]
The zero-frequency map has squared norm multiplier \(6\), producing the stated \(\lambda_{n,0}\). For even \(n\), the two additional configurations have \(D_i=\pm(-1)^i/2\), and all others have \(D=0\). Their only nonzero covariance Fourier sector has \(D\)-eigenvalue \(n/(2Z_n)\). Since this mode has two rail coordinates and no rung component, its full-edge eigenvalue is \(n/Z_n\). This proves completeness, including all nullities.

**4. Locate sharp extrema.** The function \(g(t)=(4+2t)/(3+2t)\) decreases strictly in \(-1\le t\le1\), with derivative \(-2/(3+2t)^2\). The odd zero mode satisfies \(\lambda_{n,0}<6F_n/(5L_n)\), strictly smaller than each nonzero-frequency eigenvalue; the largest is at the available frequency nearest \(\pi\). This proves the odd formula. For even \(n\), \(F_n\ge n\) for \(n\ge6\), implying the isolated antisymmetric eigenvalue is below all symmetric modes. The alternating symmetric eigenvalue \(2F_n/Z_n\) dominates the other symmetric modes and the zero mode, since \(4F_n\ge3n\); \(n=4\) is checked directly and exhibits precisely the stated ties. Divide the extreme eigenvalues for the even condition ratio. Finally Binet's formula yields \(F_n\sim\phi^n/\sqrt5\). Positivity of the displayed eigenvalues establishes the asserted ranks.

## Verification

The accompanying self-contained program `check_prism.py` enumerates every perfect matching for lengths \(3\le n\le16\); it compares the exact matching count and all predicted Fourier eigenvalues against directly computed Fourier variances of the independent combinatorial ensemble, to numerical tolerance \(10^{-9}\). It also checks identity (1) using exact integers for \(3\le n\le69\) and both sharp condition-ratio formulas in the enumerated range. Run `python3 check_prism.py` with the standard library. These computations support, but do not replace, the unrestricted analytic proof.

## Relationship to prior work

Lekshmi and West (2020, arXiv:2003.09602) already supply the exact perfect-matching count \(L_n+2\mathbf1_{\{2\mid n\}}\); this is used as background, not claimed as new. Classical cycle-matching enumeration, and Fourier spectra of the cycle independent-set ensemble, cover the base-cycle part of the argument; the proposed contribution is the **full prism-edge covariance spectral decomposition**, in particular the parity-dependent additional antisymmetric sector, the sharp all-size extremal modes, and the exponential-versus-bounded sharp conditioning law. Wilkins and Powell (2021, arXiv:2103.03260) derive topological-sector and dimer-correlation results for a different square-lattice torus model. Such general dimer correlation tools are relevant but do not, from the material inspected, directly provide the stated finite-width cyclic prism eigenvalue theorem. Historical exact thin-cylinder static-structure-factor treatments remain a priority risk.

## Limitations

The theorem concerns simple prisms \(n\ge3\), uniform perfect-matchings only, and centered first-degree EDGE Fourier/Walsh sampling. It does not cover weighted dimers, general ladder widths, unmatched configurations, higher-order Walsh characters, or noncentered full-frame invertibility. The covariance has a large deterministic nullspace because vertex matching constraints hold identically. Priority is provisional: the 2020 enumeration paper's complete text and some older exact narrow-cylinder correlation sources could not be exhaustively compared; neither a search miss nor a finite checker run establishes originality.

## References

1. R. S. Lekshmi and Douglas B. West, “The Number of Perfect Matchings in Möbius Ladders and Prisms,” arXiv:2003.09602 (first public 2020-03-21), https://arxiv.org/abs/2003.09602.
2. Neil Wilkins and Stephen Powell, “Topological sectors, dimer correlations and monomers from the transfer-matrix solution of the dimer model,” arXiv:2103.03260 (first public 2021-03-04), https://arxiv.org/abs/2103.03260.
3. Classical Fibonacci/Lucas matching counts of a cycle and the transfer-matrix identity for cycle matchings (used in their elementary forms and proved here as needed).
