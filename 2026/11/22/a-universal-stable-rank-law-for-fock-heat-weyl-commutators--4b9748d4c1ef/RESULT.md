# A universal stable-rank law for Fock heat–Weyl commutators

## Finding

For integer dimension \(d\ge1\), the commutator of Gaussian Fock dilation with a fixed nontrivial Weyl displacement has an exact Hilbert–Schmidt norm and a sharp operator-norm limit. The ratio of their squares, the **stable rank**, diverges at a universal dimension-dependent rate despite operator-norm convergence of the commutator to zero:

\[
\begin{aligned}
\|[D_r,W_a]\|_{\mathcal S_2}^2&=\frac{2}{(1-r^2)^d}\left(1-\exp\left[-\frac{1-r}{1+r}|a|^2\right]\right),\
\lim_{r\uparrow1}\frac{\|[D_r,W_a]\|}{\sqrt{1-r}}&=|a|\sqrt{\frac2e},\
\lim_{r\uparrow1}(1-r)^d\frac{\|[D_r,W_a]\|_{\mathcal S_2}^2}{\|[D_r,W_a]\|^2}&=\frac{e}{2^{d+1}}.
\end{aligned}
\]

The final coefficient is independent of the nonzero displacement amplitude.

## Assumptions and scope

Use the Hilbert space \(\mathcal F_d\) of entire holomorphic functions on \(\mathbb C^d\) with squared norm \(\pi^{-d}\int_{\mathbb C^d}|f(z)|^2e^{-|z|^2}\,dV(z)\). The orthonormal monomials are \(e_\nu(z)=z^\nu/\sqrt{\nu!}\), indexed by multi-indices \(\nu\in\mathbb N_0^d\). Assume \(d\in\mathbb N\), \(d\ge1\), \(0<r<1\), and \(a\in\mathbb C^d\setminus\{0\}\). Let

\[
(D_r f)(z)=f(rz),\qquad (W_af)(z)=e^{z\cdot\overline a-|a|^2/2}f(z-a).
\]

The dot product means \(z\cdot\overline a=\sum_{j=1}^{d}z_j\overline{a_j}\). The Weyl operator is unitary; \(D_r\) has diagonal eigenvalues \(r^{|\nu|}\), and is trace class for every \(r<1\). Hence \(C_{r,a}=D_rW_a-W_aD_r\) is trace class. All asymptotic limits keep \(d\) and nonzero \(a\) fixed while \(r\uparrow1\).

## Proof

**1. Reduction to one displaced coordinate.** Unitary coordinate rotation sends \(a\) to \((|a|,0,\ldots,0)\). As \(D_r\) is invariant under this rotation, the commutator is unitarily equivalent to

\[
C^{(1)}_{r,|a|}\otimes D_r^{\otimes(d-1)}.
\]

Thus the operator norm is its one-dimensional value, and the squared Hilbert–Schmidt norm is the one-dimensional squared value multiplied by \((1-r^2)^{-(d-1)}\), since \(\sum_{n\ge0}r^{2n}=(1-r^2)^{-1}\).

**2. Exact Gaussian trace.** In one variable, the two operators \(D_rW_a\) and \(W_aD_r\) have reproducing-kernel integrands

\[
\begin{aligned}
K_1(z,w)&=e^{-|a|^2/2}\exp(rz\overline w+r z\overline a-a\overline w),\
K_2(z,w)&=e^{-|a|^2/2}\exp(rz\overline w+z\overline a-r a\overline w).
\end{aligned}
\]

The Hilbert–Schmidt norm of such an integral-kernel operator is obtained by integrating the squared kernel against normalized Gaussian measure in both variables. The elementary complex Gaussian identity

\[
\frac1\pi\int_{\mathbb C}e^{-c|z|^2+uz+v\overline z}\,dA(z)=c^{-1}e^{uv/c}\quad(c>0)
\]

(after completing the square, or first checking polynomials and continuing analytically) gives

\[
\|D_rW_a\|_2^2=\|W_aD_r\|_2^2=(1-r^2)^{-1},\qquad
\langle D_rW_a,W_aD_r\rangle_{\mathcal S_2}=\frac{e^{-|a|^2(1-r)/(1+r)}}{1-r^2}.
\]

The cross term is real and positive. Expanding the square and using the tensor factorization proves the asserted exact \(d\)-dimensional formula.

**3. Sharp operator-norm upper bound.** In one dimension, let \(B_a=aM_z-\overline a\,\partial_z\), the skew-adjoint generator of \(W_{sa}=e^{sB_a}\), and put \(t=1-r\). On the monomial basis, the bounded self-adjoint commutator \([B_a,D_r]\) has upper and lower first diagonals of respective magnitudes

\[
|a|t\sqrt{n+1}\,r^n\quad(n\ge0).
\]

Its norm therefore satisfies

\[
\|[B_a,D_r]\|\le2|a|t\sup_{n\ge0}\sqrt{n+1}\,r^n
=|a|\sqrt{2t/e}\,(1+o(1)),
\]

because \(\sup_{n\ge0}\sqrt{n+1}\,r^n\sim(2et)^{-1/2}\). Along the strongly continuous Weyl one-parameter group, the conjugation difference is the integral of its commutator derivative. The derivative is bounded and its unitary conjugates have constant norm, so

\[
\|D_r-W_aD_rW_a^*\|\le\|[B_a,D_r]\|.
\]

This yields the sharp limsup. The integral identity may equivalently be justified first for finite-rank diagonal truncations and then by norm convergence, since both \(D_r\) and \([B_a,D_r]\) are compact for \(r<1\).

**4. Matching coherent-state lower bound.** For a normalized coherent vector \(k_z(w)=e^{w\overline z-|z|^2/2}\),

\[
\langle k_z,D_rk_z\rangle=e^{-t|z|^2},\qquad
\langle k_z,W_aD_rW_a^*k_z\rangle=e^{-t|z-a|^2}.
\]

Choose \(z=a/(|a|\sqrt{2t})\), for which \(|z|=(2t)^{-1/2}\). The difference of these two expectations is \(|a|\sqrt{2t/e}\,(1+o(1))\), giving the matching operator-norm liminf.

**5. Effective rank and boundary behavior.** The exact squared Hilbert–Schmidt norm has asymptotic \(|a|^2/[2^d t^{d-1}]\). Dividing by the squared operator norm, \(2|a|^2t/e\), proves

\[
t^d\operatorname{sr}(C_{r,a})\to e/2^{d+1}.
\]

Moreover \(D_r\to I\) strongly, so \([D_r,W_a]\to0\) strongly, and the sharper operator-norm limit is already proved. At \(d=1\) the Hilbert–Schmidt mass tends to \(|a|^2/2\); at \(d>1\) it diverges with the displayed power of \(t\).

## Verification

The standalone `CHECK.py` uses only the Python standard library. It compares the exact Hilbert–Schmidt formula with finite monomial matrices for three nontrivial parameter choices, tests tensor and positivity identities, and checks numerical coherent-state lower and Jacobi upper norm bounds near \(r=1\). Running `python CHECK.py` prints `PASS: 3 finite matrix comparisons, 9 dimension/positivity identities, 3 norm sandwiches.` Finite checks are corroboration only; the infinite-dimensional proof is the Gaussian identity, weighted-shift estimate, and coherent-state argument above.

## Relationship to prior work

Chalendar and Partington analyze iteration and semigroups of Fock weighted composition operators, including radial contractions. Kisil develops the Heisenberg/Weyl representation framework for Fock operators. Alpay and collaborators analyze commutator calculi for generalized Fock weighted shifts, not the present displacement-versus-heat spectral pairing. Classical quantum-optical studies of displaced thermal states give related Gaussian overlaps; Gaussian overlap by itself is not asserted to be new here. The claim under assessment is the *joint* exact Hilbert–Schmidt law, sharp small-time operator-norm coefficient, and displacement-independent dimension-dependent stable-rank limit. A literature search did not identify this complete assertion, but cannot exclude equivalent formulations in coherent-state or harmonic-oscillator semiclassics.

## Limitations

The norm asymptotic and stable-rank limit require fixed finite dimension and fixed nonzero displacement. No uniformity as \(|a|\to0\), \(|a|\to\infty\), or \(d\to\infty\) is proved. There is no claim of an exact finite-\(r\) operator norm, complete singular spectrum, or sharp trace-norm asymptotic. Independent validation and exhaustive historical-priority verification have not been performed.

## References

1. I. Chalendar and J. R. Partington, *Weighted composition operators on the Fock space: iteration and semigroups*, first public preprint 2021-06-01, arXiv:2106.00427, https://arxiv.org/abs/2106.00427.
2. V. V. Kisil, *Cross-Toeplitz Operators on the Fock–Segal–Bargmann Spaces and Two-Sided Convolutions on the Heisenberg Group*, first public preprint 2021-08-31, arXiv:2108.13710, https://arxiv.org/abs/2108.13710.
3. D. Alpay, P. Cerejeiras, U. Kaehler and T. Kling, *Commutators on Fock spaces*, first public preprint 2022-08-05, arXiv:2208.03394, https://arxiv.org/abs/2208.03394.
4. *Superoscillations and Fock spaces*, *Journal of Mathematical Physics* 64 (2023), Article 093505, https://doi.org/10.1063/5.0155981. The inspected accessible extract defines the standard unitary Weyl displacement; full publisher text was inaccessible.
