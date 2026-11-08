# Sharp six-state positivity barrier and recovery for two-stage Radau IIA on directed cycles

## Finding
Let \(n\ge2\) be an integer, let \(P\) cyclically advance the standard basis of \(\mathbb R^n\), and let \(Q=P-I\). For a dimensionless step \(h\ge0\), let \(T_n(h)\) be the one-step matrix of the two-stage Radau IIA method applied to \(y'=Qy\):
\[
 T_n(h)=R(hQ),\qquad R(z)=\frac{1+z/3}{1-2z/3+z^2/6}.
\]
All these matrices preserve total mass: \(\mathbf1^\mathsf{T}T_n(h)=\mathbf1^\mathsf{T}\). Their entrywise-positivity behavior has the following sharp dimension barrier and recovery law.

1. For every \(2\le n\le5\), \(T_n(h)\) is entrywise nonnegative for **every** \(h\ge0\), and strictly positive for every \(h>0\).
2. For **every** \(n\ge6\), the entry from state \(0\) to state \(5\) satisfies
\[
  (T_n(h))_{5,0}=-\frac{h^5}{108}+O(h^6)\quad(h\downarrow0).
\]
   Thus all these cycle sizes have negative entries at every sufficiently small positive step. Nonetheless, \(T_n(h)\to\mathbf1\mathbf1^\mathsf T/n\) as \(h\to\infty\), so all entries become strictly positive for all sufficiently large steps.
3. On the **first failing cycle**, \(n=6\), the complete nonnegative-step set is
\[
 \{0\}\cup[\rho,\infty),
\]
   where \(\rho\) is the **unique** positive root of
\[
 p(h)=h^5+15h^4+60h^3+90h^2+36h-12.
\]
   In particular, \(0.2086088<\rho<0.2086089\). The sole negative entry type for \(0<h<\rho\) is a displacement of five directed edges.
4. On the **eight-cycle** the positivity set is disconnected beyond the isolated zero step: the transition matrix is strictly positive at \(h=2\), negative on the diagonal at \(h=4\), and strictly positive again at \(h=20\). These statements hold by exact rational arithmetic, not simulation.

## Assumptions and scope
Here \(P e_j=e_{j+1\bmod n}\), so \(Q\) is a unit-rate, irreducible, nonreversible continuous-time Markov generator in the **column-vector convention**. Time steps are dimensionless; a common edge rate \(c>0\) replaces \(h\) by \(ch\). Entrywise nonnegative means all entries are nonnegative, including diagonal entries, not merely stability in a matrix norm. We analyze the one-step endpoint, not internal Runge–Kutta stages or the accuracy of iterated physical trajectories. The theorem does not assert the positivity set is a single interval for every \(n\).

## Proof
**Stability function and pole exclusion.** The two-stage Radau IIA tableau is
\[
 A=\begin{pmatrix}5/12&-1/12\\3/4&1/4\end{pmatrix},\qquad
 b=(3/4,1/4)^\mathsf T.
\]
Direct substitution into \(R(z)=1+zb^\mathsf T(I-zA)^{-1}\mathbf1\) gives the stated \(R\). The denominator zeros are \(2\pm i\sqrt2\), whereas every eigenvalue of \(Q\) is \(\zeta-1\) for an \(n\)th root of unity \(\zeta\), and hence has nonpositive real part. Thus \(T_n(h)\) exists for every \(h\ge0\). Since \(R(0)=1\) and \(\mathbf1^\mathsf TQ=0\), mass is conserved.

**Sharp small-step barrier.** Expand \(R\) about zero by multiplying the formal series by its quadratic denominator. The first six coefficients are
\[
 R(z)=1+z+\frac{z^2}{2}+\frac{z^3}{6}+\frac{z^4}{36}-\frac{z^5}{108}+O(z^6).
\]
When \(n\ge6\), a term of degree below five in \(P-I\) cannot transport from \(e_0\) to \(e_5\), and the coefficient of \(P^5\) in \((P-I)^5\) is one. No smaller power aliases to \(P^5\) modulo \(P^n-I\). Hence the indicated negative coefficient is exact for **all** \(n\ge6\). This is a sign statement about an analytic germ, not a finite-grid inference.

**Universal large-step recovery.** The permutation \(P\) is diagonalized by the discrete Fourier transform. The zero eigenvalue of \(Q\) is simple and corresponds to constants; all other eigenvalues satisfy \(\operatorname{Re}\lambda<0\). For each nonzero eigenvalue, \(R(h\lambda)=O(h^{-1})\) as \(h\to\infty\), because the numerator degree is one and the denominator degree is two. The Fourier decomposition therefore gives
\[
 T_n(h)=\frac1n\mathbf1\mathbf1^\mathsf T+O_n(h^{-1}).
\]
For fixed \(n\), every entry is consequently strictly positive at all sufficiently large \(h\).

**Exact low-dimensional sign certificates.** Write
\[
 D_n(h)=I-\frac{2h}{3}(P-I)+\frac{h^2}{6}(P-I)^2,
 \qquad U_n(h)=I+\frac h3(P-I).
\]
In the ring \(\mathbb Q[h,P]/(P^n-I)\), the certificate file `certificate.json` supplies integer polynomials \(d_n(h)>0\) and \(N_{n,j}(h)\) such that
\[
 D_n(h)\sum_{j=0}^{n-1}N_{n,j}(h)P^j=d_n(h)U_n(h).
\]
Thus \(T_n(h)=\sum_j(N_{n,j}(h)/d_n(h))P^j\). The coefficient lists are ascending in \(h\), so their signs are directly inspectable. All coefficients of \(d_n\) are nonnegative, with positive constant term. For each \(n=2,3,4,5\), all coefficients of each \(N_{n,j}\) are nonnegative and every such polynomial is positive for \(h>0\); this proves unconditional strict positivity. The standalone, standard-library-only `verify.py` checks **each** polynomial identity exactly, rather than merely evaluating at sampled steps.

For \(n=6\), the same exact certificate shows the four intermediate displacements \(j=1,2,3,4\) have strictly positive numerator polynomials at \(h>0\). The exceptional fifth displacement has numerator \(h^5p(h)\), with \(p\) as above. Its derivative is
\[
 p'(h)=5h^4+60h^3+180h^2+180h+36>0\qquad(h\ge0).
\]
Since \(p(0)=-12\), it has exactly one positive root. To exclude a hidden diagonal obstruction, its numerator is exactly
\[
 N_{6,0}(h)=h^{10}+5h^9-5h^8-50h^7+26h^6+664h^5
 +2280h^4+4440h^3+5400h^2+3888h+1296.
\]
For \(0<h\le3\), the negative terms have magnitude at most
\(5h^8+50h^7\le585h^5<664h^5\). For \(h\ge3\), the four leading terms equal \(h^7(h^3+5h^2-5h-50)>0\), because the cubic is increasing on \([3,\infty)\) and equals \(7\) at \(3\). Every remaining term is positive. Thus the diagonal numerator is positive for all \(h>0\). The asserted exact six-cycle set follows.

**An eight-cycle with separated windows.** Solving the \(8\times8\) rational circulant system exactly gives
\[
\begin{aligned}
 \min_{i,j}(T_8(2))_{ij}&=\frac{11824}{2058973}>0,\\
 \min_{i,j}(T_8(4))_{ij}&=-\frac{5703833}{339145563}<0,\\
 \min_{i,j}(T_8(20))_{ij}&=\frac{127548251905668327}{1666416340218976267}>0.
\end{aligned}
\]
The negative entry at \(h=4\) is diagonal. A circulant has all its entry types in one column, and the checker verifies its exact linear systems and column sums. Rational dependence on \(h\) ensures continuity: positivity near \(h=2\) and near \(h=20\), separated by negativity at \(h=4\), gives two distinct positive-step components. As established above, \(h=0\) is an additional isolated nonnegative step in dimension eight.

## Verification
Run `python3 verify.py` with `certificate.json` in the same directory. The checker uses only Python's standard library; it verifies polynomial identities for \(n=2,3,4,5,6\), numerator/denominator positivity certificates, the sixth-cycle root isolating interval, the scalar Taylor coefficients, and exact rational eight-cycle matrices at \(h=2,4,20\). The recorded `verification_output.txt` contains the result of executing the packaged checker. These finite polynomial identities are complete algebraic certificates for the finite small-cycle classifications; the arbitrary-dimension claims rely on the independent formal-series and Fourier arguments above.

## Relationship to prior work
Blanes, Iserles and Macnamara (first posted 16 February 2021) motivate positivity for graph-Laplacian ODEs and discuss barriers to positivity in classical high-order integrators. Their results concern general positivity-preserving constructions rather than the complete directed-cycle endpoint sign law of the two-stage Radau IIA rational function. Banjai and Ferrari (2022) analyze Gauss-based Runge–Kutta convolution quadrature and Padé stability functions, not these nonreversible Markov transition entries. A published eight-state positivity-barrier study examines the different fourth-order \([2/2]\) Padé / two-stage **Gauss–Legendre** method, whereas here the third-order \([1/2]\) Padé / two-stage **Radau IIA** map fails already at six cyclic states and ultimately recovers positivity through \(L\)-stability. The former method's positivity criterion does not imply this result, and neither does a generic absolute-monotonicity step bound.

## Limitations
The result concerns one-way unit-rate directed cycles and endpoint matrices only; it does not classify general Markov generators, unequal edge rates, higher-stage Radau methods, or the full positivity set at every \(n\ge7\). The six-cycle recovery root is algebraic but has no claimed elementary radical expression. The eight-cycle rational witnesses establish disconnectedness without enumerating every boundary point. The comparison with specialist publications is best-knowledge rather than a mathematical proof of global novelty; an inaccessible or unindexed prior theorem could supersede it.

## References
- S. Blanes, A. Iserles and S. Macnamara, *Positivity-preserving methods for ordinary differential equations* (first posted as arXiv:2102.08242 on 16 February 2021), https://arxiv.org/html/2102.08242v2 .
- L. Banjai and M. Ferrari, *Runge–Kutta convolution quadrature based on Gauss methods* (arXiv:2212.07170, first posted 14 December 2022), https://arxiv.org/html/2212.07170v1 .
- P. Munch, I. Dravins, M. Kronbichler and M. Neytcheva, *Stage-parallel fully implicit Runge–Kutta implementations with optimal multilevel preconditioners at the scaling limit* (arXiv:2209.06700, 14 September 2022), https://arxiv.org/abs/2209.06700 .
- *Eight-state barrier for Markov positivity of the [2/2] Padé map*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab .
