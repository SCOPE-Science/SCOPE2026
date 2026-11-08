# Sharp arithmetic determinant gap for three-coset Fourier bases on separated integer intervals

## Finding
For an integer \(m\ge 3\), put
\[
 E_m=[0,1)\cup[m,m+2),\qquad
 \Lambda_\tau=\mathbb Z\cup(\mathbb Z+\tau)\cup(\mathbb Z+2\tau),\quad 0<\tau<1.
\]
The constant Fourier-fiber matrix for the exponential synthesis system on \(L^2(E_m)\) is
\[
 V_m(\tau)=\big(e^{2\pi i a s\tau}\big)_{a\in\{0,m,m+1\},\;s\in\{0,1,2\}}.
\]
Define its squared-volume stability measure \(D_m(\tau)=\det(V_m(\tau)^*V_m(\tau))\), and the optimal restricted design value \(D_m^*=\max_{0\le\tau\le1}D_m(\tau)\). Then
\[
 D_m(\tau)=64\sin^2(\pi\tau)\sin^2(\pi m\tau)\sin^2(\pi(m+1)\tau).
\]
For all \(m\ge3\), \(D_m^*\le27\), with equality **exactly** for \(m\equiv1\pmod3\), in which case the only maximizing shifts modulo one are \(\tau=1/3,2/3\). For \(m\equiv0,2\pmod3\), the optimum is strictly below \(27\), but has the sharp arithmetic asymptotic
\[
 \boxed{\ D_m^*=27-\frac{6\pi^2}{m^2}+O(m^{-3})\ }\qquad(m\to\infty,\ m\not\equiv1\pmod3).
\]
Moreover, for all sufficiently large \(m\not\equiv1\pmod3\) there are exactly two maximizing shifts \(\tau_m,1-\tau_m\). Choosing \(\tau_m\to1/3\), their sharp location satisfies
\[
 \boxed{\ \tau_m=\frac13+\frac{\sigma_m}{3(m+1/2)}+O(m^{-3}),\qquad
 \sigma_m=\begin{cases}1,&m\equiv0\pmod3,\\-1,&m\equiv2\pmod3.\end{cases}\ }
\]
Each maximizing system is a Riesz basis. The optimization is exclusively over the three *equally spaced* frequency cosets above; it is not asserted to optimize the smallest Riesz bound, the condition number, or arbitrary spectra.

## Assumptions and scope
Lebesgue measure is unnormalized and the exponentials are \(e^{2\pi i\lambda x}\). The integer \(m\ge3\) fixes two separated intervals of lengths one and two, with total measure three; the three coset representatives are \(0,\tau,2\tau\). The determinant is that of the **squared** singular-value matrix, not the determinant of a normalized Gram matrix. Asymptotic constants are universal along the two residue classes \(m\equiv0,2\pmod3\), with uniform \(O(m^{-3})\) there. Frequencies with collisions give \(D_m(\tau)=0\) and do not yield bases.

## Proof
**Fiber reduction.** For almost every \(x\in[0,1)\), the three lifts of \(x\) into \(E_m\) are \(x,x+m,x+m+1\). Fourier series in the integer frequency index and unit-modulus row/column factors give a unitary decomposition of the exponential synthesis operator into copies of \(V_m(\tau)\). Thus its sharp squared Riesz bounds are the smallest and largest eigenvalues of \(V_m^*V_m\), and it is a Riesz basis exactly when \(\det V_m\ne0\). The Vandermonde identity with nodes \(1,e^{2\pi i m\tau},e^{2\pi i(m+1)\tau}\) proves the stated product formula.

**Exact arithmetic equality.** For any three points \(z_0,z_1,z_2\) on the unit circle,
\[
 \sum_{i<j}|z_i-z_j|^2=9-|z_0+z_1+z_2|^2\le9,
 \qquad\prod_{i<j}|z_i-z_j|^2\le 27.
\]
Equality holds precisely for an equilateral triple. Our two successive nodes have ratio \(e^{2\pi i\tau}\), so equality forces \(\tau=1/3\) or \(2/3\). The three nodes are then equilateral if and only if \(m\equiv1\pmod3\). For other residues, continuity on the compact circle makes the optimum strictly less than \(27\).

**Local determinant defect.** Write the phases of three nodes in counterclockwise order, near an equilateral triple, as
\[
 (0,\;1/3+u,\;2/3+v)\pmod1.
\]
Taylor's formula applied to the three squared chord lengths, uniformly as \((u,v)\to(0,0)\), gives
\[
 \log D=\log27-\frac{4\pi^2}{3}\bigl(u^2+v^2+(v-u)^2\bigr)
 +O\bigl((|u|+|v|)^3\bigr).
\tag{1}
\]
The positive quadratic form and the isolated equality configurations imply that \(D\ge27-O(m^{-2})\) forces the node phases to lie \(O(m^{-1})\) from an equilateral configuration.

**Competitor and global lower defect.** Suppose \(m\equiv0\) or \(2\pmod3\), and set respectively \(c=1/3\) or \(c=-1/3\). The trial shift
\[
 \widetilde\tau=\frac13+\frac{c}{m}-\frac{c}{2m^2}
\]
places the last two node phases at \(1/3-c/(2m)+O(m^{-2})\) and \(2/3+c/(2m)+O(m^{-2})\), respectively. Equation (1) gives
\[
 D_m^*\ge D_m(\widetilde\tau)
 =27-\frac{6\pi^2}{m^2}+O(m^{-3}).\tag{2}
\]
Take any maximizing shift. The preceding stability statement and the fact that the difference of the last two node phases is \(\tau\) show that it lies \(O(m^{-1})\) from \(1/3\) or \(2/3\). Reflection \(\tau\mapsto1-\tau\) allows the first case. Write
\[
 \tau=\frac13+\frac{c}{m}+\frac{b}{m^2},
 \qquad c\in \mathbb Z+\eta_m,
 \quad \eta_m=\begin{cases}1/3,&m\equiv0\pmod3,\\-1/3,&m\equiv2\pmod3,\end{cases}
\]
where the bounded parameter \(b\) absorbs the \(O(m^{-1})\) phase error and \(c\) is bounded. The last two phase errors are
\(u=b/m\) and \(v=(b+c)/m+O(m^{-2})\). Hence, uniformly for bounded \(b,c\), equation (1) yields
\[
 D_m(\tau)=27-\frac{36\pi^2}{m^2}
 \bigl(b^2+(b+c)^2+c^2\bigr)+O(m^{-3}).\tag{3}
\]
For each \(c\), the quadratic bracket has minimum \(3c^2/2\), attained uniquely at \(b=-c/2\). Every admissible \(c\) has \(|c|\ge1/3\). Thus (3) and (2) match and force the coefficient \(6\pi^2\). They also exclude, for all sufficiently large \(m\), every alias except the unique smallest-modulus one: \(c=1/3\) in residue zero and \(c=-1/3\) in residue two.

**Location and uniqueness.** Each maximizing shift is an interior critical point of \(D_m\). The exact critical equation is
\[\cot(\pi\tau)+m\cot(\pi m\tau)+(m+1)\cot(\pi(m+1)\tau)=0.\]
Its uniform expansion at the surviving alias gives \(b=-c/2+O(m^{-1})\), hence
\[\tau_m=1/3+c/m-c/(2m^2)+O(m^{-3})
=1/3+c/(m+1/2)+O(m^{-3}).\]
On any interval where \(D_m>0\),
\[
 \frac{d^2}{d\tau^2}\log D_m(\tau)
 =-2\pi^2\bigl[\csc^2(\pi\tau)+m^2\csc^2(\pi m\tau)
 +(m+1)^2\csc^2(\pi(m+1)\tau)\bigr]<0.
\]
This strict concavity and the unique surviving alias give one maximizer near \(1/3\); its reflected partner is the sole other maximizer. These estimates hold eventually along either nonorthogonal residue class. \(\square\)

## Verification
A standalone standard-library checker, `CHECK.py`, evaluates the explicit Fourier fiber determinant against its chord product using direct complex arithmetic, confirms exact equilateral cases, and numerically stress-tests the sharp residue-class asymptotic and predicted shift locations for representative large orders. It tests finite cases only. The analytic argument above, especially the global compactness-and-alias step, proves the infinite family and sharp coefficient.

## Relationship to prior work
The multi-tile fiber/Vandermonde reduction is classical; Frederick and Okoudjou explicitly develop it and identify optimizing the choice of lattice shifts as outside the general construction developed there. Frederick and Yacoubou Djima work through two-interval and multi-rectangle sampling examples, without a three-coset sharp determinant limit for the integer-gap family above. The 2026 convolution-spectrality results of Zhou motivate quantifying nonorthogonal spectra when orthogonality is arithmetically constrained. The present specific restricted-design theorem isolates an arithmetic defect and determines its sharp decay and shift location as the interval gap grows. The equal-length three-interval determinant design studied elsewhere has different fibers, except for a small special geometry equivalent to the \(m=2\) case, which is excluded here. General unconstrained equilateral Fekete designs do not impose the coupled phases \((m\tau,(m+1)\tau)\).

## Limitations
The statement does not optimize over arbitrary triplets of non-equally-spaced coset representatives or over all exponential Riesz bases; it optimizes the Gram determinant rather than individual Riesz bounds. The \(O(m^{-3})\) expansions are asymptotic and give no universal explicit finite threshold for uniqueness. Earlier literature on restricted Vandermonde determinants under alternative terminology may contain related results. No independent mathematical audit has been performed.

## References
- Ting Zhou, *Spectrality of convolution and product measures: a block decomposition approach*, arXiv:2610.33987, first public 2026-10-25.
- Christina Frederick and Kasso A. Okoudjou, *Finding duality for Riesz bases of exponentials on multi-tiles*, Applied and Computational Harmonic Analysis 51 (2021), 104–117, DOI:10.1016/j.acha.2020.10.006.
- Ruxi Shi, *Fuglede's conjecture holds for three intervals*, arXiv:2607.24005, first public 2026-07-27 (context for spectrality, not a quantitative determinant formula).
- Christina Frederick and Karamatou Yacoubou Djima, *Examples of Riesz Bases of Exponentials for Multi-tiling Domains and Their Duals*, La Matematica 3 (2024), DOI:10.1007/s44007-023-00078-7.
