# A universal quantum-integer denominator for fixed-degree descendant series

## Finding
Fix the data of Theorem A in Kennedy-Hunt--Shafi--Urundolil Kumaran and an admissible degree vector \(p=(p_1,\ldots,p_n)\). Define
\[
F_p(u)=\sum_{g\ge 0}N_{g,\vartheta}^{\beta_p}u^{2g},
\qquad
[\ell]_q=\frac{q^{\ell/2}-q^{-\ell/2}}{q^{1/2}-q^{-1/2}}.
\]
Put \(P=\max_j p_j\),
\[
e_\ell(p)=\sum_j\left\lfloor\frac{p_j}{\ell}\right\rfloor,
\qquad
D_p(q)=\prod_{\ell=2}^P[\ell]_q^{e_\ell(p)}.
\]
Then there is a Laurent polynomial \(A_p(t)\in\mathbf Q[t^{\pm1}]\) such that
\[
F_p(u)=\frac{A_p(e^{iu/2})}{D_p(e^{iu})}
\]
as a formal Taylor series at \(u=0\).

Consequently, if \(\zeta\ne1\) is a primitive \(d\)-th root of unity, any pole of the corresponding rational function at \(q=\zeta\) has order at most
\[
E_d(p)=\sum_{\substack{2\le\ell\le P\\ d\mid\ell}}e_\ell(p).
\]
For each fixed \(\ell\), the exponent \(e_\ell(p)\) is exactly the largest possible exponent \(\sum_j k_{\ell j}\) among the partition data \(k\vdash p\) in Corollary 3.9. This last statement is about the raw partition envelope; cancellations may lower the reduced denominator.

## Assumptions and scope
The target is a Looijenga pair presented in the form used in the initiating paper: a toric surface is blown up at boundary points indexed by \(m=(m_1,\ldots,m_n)\), and \(\vartheta=(r_1,\ldots,r_s)\) is the prescribed tangency tuple. The vector \(p\in\mathbf N^n\) is admissible in the sense that \(\sum_i p_im_i=\sum_j r_j\). The invariant \(N_{g,\vartheta}^{\beta_p}\) includes the \((-1)^g\lambda_g\), point, and descendant insertions of the source.

The statement controls a universal denominator depending only on \(p\). It does not claim that this denominator is reduced, that every allowed root-of-unity pole actually occurs, or that the pole-order bound is sharp after summing tropical contributions.

## Proof
Corollary 3.9 of the initiating paper writes the coefficient of \(t_1^{p_1}\cdots t_n^{p_n}\) in the cyclically symmetrized quantum-mirror structure constant as a finite sum over partition data \(k=(k_{\ell j})\) satisfying
\[
\sum_{\ell\ge1}\ell k_{\ell j}=p_j
\quad\text{for every }j.
\]
Each summand is a refined tropical count multiplied by
\[
\prod_{j,\ell}
\frac{1}{k_{\ell j}!}
\left(
\frac{(-1)^{\ell-1}}{\ell}
\frac{q^{1/2}-q^{-1/2}}{q^{\ell/2}-q^{-\ell/2}}
\right)^{k_{\ell j}}
=
\prod_{j,\ell}
\frac{1}{k_{\ell j}!}
\left(
\frac{(-1)^{\ell-1}}{\ell[\ell]_q}
\right)^{k_{\ell j}}.
\]

The refined tropical count is a Laurent polynomial in \(q^{1/2}\) with rational coefficients. Indeed, pointed-vertex multiplicities are finite averages of Laurent monomials, unpointed trivalent multiplicities are quantum integers, bivalent multiplicities are \(1\), and only finitely many rigid tropical curves occur for fixed degree.

For every partition datum,
\[
k_{\ell j}\le\left\lfloor\frac{p_j}{\ell}\right\rfloor
\]
because \(\ell k_{\ell j}\le p_j\). Therefore
\[
\sum_j k_{\ell j}\le e_\ell(p),
\]
so multiplication by \(D_p(q)\) clears every quantum-integer denominator in every summand. The resulting coefficient is therefore some \(A_p(q^{1/2})\in\mathbf Q[q^{\pm1/2}]\).

Theorem A identifies this fixed-\(p\) coefficient after \(q=e^{iu}\) with \(F_p(u)\), proving the displayed rational form. Since \([\ell]_q\) vanishes at a nontrivial primitive \(d\)-th root of unity precisely when \(d\mid\ell\), and the zero is simple, the pole order is bounded by \(E_d(p)\).

Finally, for fixed \(\ell\) and \(p_j\), the maximum possible value of \(k_{\ell j}\) over integer partitions of \(p_j\) is \(\lfloor p_j/\ell\rfloor\), attained by using that many parts of size \(\ell\) and filling the remainder with parts of size \(1\). Summing over \(j\) gives the componentwise sharp exponent envelope \(e_\ell(p)\).

## Verification
The proof is symbolic and does not depend on finite experimentation. The bundled checker enumerates ordinary integer partitions for \(p_j\le12\) and verifies that the maximum number of parts of size \(\ell\) is \(\lfloor p_j/\ell\rfloor\), including several multi-index degree vectors. It returned `VERIFY_OK`.

The source formula was checked directly in Corollary 3.9, together with the vertex multiplicities in Definition 2.5, finiteness in Proposition 2.6 and Remark 2.7, and the coefficientwise identification in Theorem A.

## Relationship to prior work
The initiating paper proves the quantum-mirror/logarithmic-Gromov--Witten correspondence and remarks that the answer has rationality properties. Its Corollary 3.9 displays the partition factors from which the present denominator follows, but the inspected text does not state a degree-local universal quantum-integer denominator, a root-of-unity pole envelope, or the componentwise exponent bound above.

The earlier toric correspondence of Kennedy-Hunt--Shafi--Urundolil Kumaran identifies toric descendant series directly with refined tropical counts; those counts are Laurent polynomials and do not contain the non-toric partition denominators isolated here. Bousseau's quantum-mirror construction supplies the broader scattering-diagram context but predates the fixed-degree formula used here.

## Limitations
The displayed \(D_p(q)\) is a universal clearing denominator, not necessarily the reduced denominator of \(F_p\). Different quantum integers share cyclotomic factors, and cancellations among partition and tropical terms can lower or remove poles. The pole statement is therefore an upper bound only. No asymptotic claim for \(N_{g,\vartheta}^{\beta_p}\) is made.

## References
1. P. Kennedy-Hunt, Q. Shafi, A. Urundolil Kumaran, *Refined curve counting with descendants and quantum mirrors*, arXiv:2502.17236; Épijournal de Géométrie Algébrique 10 (2026), DOI 10.46298/epiga.2026.15425.
2. P. Kennedy-Hunt, Q. Shafi, A. Urundolil Kumaran, *Tropical Refined Curve Counting with Descendants*, Communications in Mathematical Physics 405 (2024), 240, DOI 10.1007/s00220-024-05114-3.
3. P. Bousseau, *Quantum mirrors of log Calabi--Yau surfaces and higher-genus curve counting*, Compositio Mathematica 156 (2020), 360--411, arXiv:1808.07336.
