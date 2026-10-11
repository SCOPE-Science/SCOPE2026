# Exact critical coupling for the Exner–Jex branching-star monotonicity transition

## Finding

Consider the mirror-symmetric three-edge star used by Exner and Jex to demonstrate that branching can reverse the dependence of the ground-state energy on an edge length. Two identical upper edges have length \(1\) and endpoint coupling \(-3/2\). The axial edge has arbitrary length \(L>0\) and endpoint coupling \(-2\). The central vertex has \(\delta\)-coupling \(\alpha\le0\). On each edge the Hamiltonian is \(-d^2/dx^2\), and coordinates point outward from the central vertex.

The transition value plotted numerically in the source is exactly
\[
\alpha_{\mathrm{crit}}
=
\frac{2(21-e^4)}{e^4+7}
=
-1.090881788335\ldots.
\]
At this coupling the ground-state energy is
\[
E_0=-4
\]
for every axial length \(L>0\). The axial ground-state component is proportional to
\[
e^{2x},
\]
so the source's exceptional edge index \(\sigma=0\) is realized exactly and globally in \(L\).

The full monotonicity diagram is also exact:
\[
\alpha_{\mathrm{crit}}<\alpha\le0
\quad\Longrightarrow\quad
\frac{\partial E_0}{\partial L}<0,
\]
while
\[
\alpha<\alpha_{\mathrm{crit}}
\quad\Longrightarrow\quad
\frac{\partial E_0}{\partial L}>0.
\]
Thus the critical value is independent of the axial length, and there is no additional transition curve hidden in the \((L,\alpha)\)-plane.

## Assumptions and scope

The graph and coupling constants are exactly those in the source figure: two mirror arms with length \(1\) and endpoint coupling \(-3/2\), one axial arm of length \(L>0\) and endpoint coupling \(-2\), and a non-repulsive central coupling \(\alpha\le0\). The statement concerns only the lowest eigenvalue of this compact star graph.

No claim is made for arbitrary branching graphs, unequal mirror arms, different endpoint couplings, positive central coupling, or higher eigenvalues. In particular, the source's broader open problem of a general regime characterization for arbitrary branching graphs remains open.

## Proof

Write the ground-state energy as
\[
E_0=-\kappa^2,
\qquad \kappa>0.
\]
By mirror symmetry the two upper components agree. For an edge of length \(\ell\) with endpoint Robin coupling \(-a\), so that
\[
\psi'(\ell)-a\psi(\ell)=0,
\]
let
\[
q_{a,\ell}(\kappa)=\frac{\psi'(0)}{\psi(0)}
\]
be its outward logarithmic derivative at the center. Solving \(\psi''=\kappa^2\psi\) gives
\[
q_{a,\ell}(\kappa)
=
\kappa\,
\frac{a-\kappa\tanh(\kappa\ell)}
{\kappa-a\tanh(\kappa\ell)}.
\]
For the positive ground state the denominator does not vanish. The central \(\delta\)-condition is therefore
\[
\alpha
=
2q_{3/2,1}(\kappa)+q_{2,L}(\kappa).
\]

Now set \(\kappa=2\). On the axial edge,
\[
q_{2,L}(2)=2
\]
for every \(L>0\); equivalently the axial component is \(Ce^{2x}\), which satisfies the endpoint condition \(\psi'(L)-2\psi(L)=0\) for every \(L\). Hence the central coupling required for the eigenvalue \(-4\) is
\[
\alpha_{\mathrm{crit}}
=
2q_{3/2,1}(2)+2.
\]
Using
\[
q_{3/2,1}(2)
=
2\frac{3/2-2\tanh 2}{2-(3/2)\tanh 2}
\]
and
\[
\tanh 2=\frac{e^4-1}{e^4+1},
\]
one obtains
\[
\alpha_{\mathrm{crit}}
=
\frac{2(21-e^4)}{e^4+7}.
\]
The corresponding eigenfunction is strictly positive on all three edges, so by the ground-state positivity and simplicity theorem used in the source, this eigenvalue is the ground state. This proves the exact \(L\)-independent critical branch.

It remains to determine the two sides of the transition. For fixed \(L\), the quadratic form contains the term
\[
\alpha|\psi(0)|^2.
\]
The simple ground eigenvalue is analytic in \(\alpha\), and the Hellmann--Feynman formula gives, for a normalized ground state,
\[
\frac{\partial E_0}{\partial\alpha}=|\psi(0)|^2>0.
\]
Therefore \(\kappa\) decreases strictly with \(\alpha\). Since \(\kappa=2\) exactly at \(\alpha_{\mathrm{crit}}\),
\[
\alpha>\alpha_{\mathrm{crit}}\Longleftrightarrow \kappa<2,
\qquad
\alpha<\alpha_{\mathrm{crit}}\Longleftrightarrow \kappa>2.
\]

Differentiate the axial logarithmic derivative with respect to its length. Directly from the displayed formula,
\[
\frac{\partial q_{2,L}}{\partial L}
=
\frac{\kappa^2(4-\kappa^2)\operatorname{sech}^2(\kappa L)}
{\bigl(\kappa-2\tanh(\kappa L)\bigr)^2}.
\]
On the ground-state branch, the derivative of the secular right-hand side with respect to \(\kappa\) is negative: this is equivalent to the already established strict decrease of \(\kappa\) with \(\alpha\). Implicit differentiation at fixed \(\alpha\) therefore shows that
\[
\operatorname{sgn}\frac{\partial\kappa}{\partial L}
=
\operatorname{sgn}(4-\kappa^2).
\]
Since \(E_0=-\kappa^2\),
\[
\operatorname{sgn}\frac{\partial E_0}{\partial L}
=
-\operatorname{sgn}(4-\kappa^2).
\]
Combining this with the comparison of \(\kappa\) to \(2\) gives the two strict regimes stated above.

## Verification

`verify_exner_jex_threshold.py` checks the exact algebraic reduction of the critical coupling, verifies the source decimal value, tests that \(q_{2,L}(2)=2\) over a broad set of axial lengths, checks the derivative formula for the axial logarithmic derivative by finite differences, including its sign on both sides of the critical decay rate.

These computations are supplementary. The all-\(L\) threshold and monotonicity classification follow from the exact secular equation, positivity of the ground state, and the Hellmann--Feynman argument in the proof.

## Relationship to prior work

Exner and Jex established the general edge-index monotonicity mechanism for attractive \(\delta\)-coupled quantum graphs. For their mirror-symmetric star example they reported two regimes separated by
\[
\alpha_{\mathrm{crit}}\approx-1.09088,
\]
and stated that at the critical value the ground-state energy is independent of the axial length because the axial component is a pure exponential. They did not give an exact expression for the critical coupling or an analytic proof that the same threshold governs every \(L>0\).

Their Remark 4.2 singled out the zero-index case as nontrivial and said that a more subtle analysis is needed in general. The calculation above resolves precisely that exceptional case for their concrete branching example.

Berkolaiko and Kuchment developed general analytic dependence of quantum-graph spectra on edge lengths and vertex conditions, which supports the perturbative framework but does not state this exact threshold. Later work on ground-state positivity for more general vertex conditions likewise does not supply the formula or regime classification for the Exner--Jex example.

Targeted searches for the reported decimal \(-1.09088\), for the source title together with “critical coupling,” and for exact formulas involving this star graph did not locate the displayed closed form.

## Limitations

This is a complete resolution of one natural branching example, not a solution of the source's open problem for arbitrary branching topology. The exact formula depends on the special endpoint data \(-3/2\), \(-2\) and unit mirror-arm length. Changing those parameters changes the critical value, although the same logarithmic-derivative method can be applied.

The originality claim is deliberately narrow because the ingredients are classical one-dimensional matching and analytic perturbation theory. An equivalent closed form could exist in notes or calculations not indexed by the searches.

## References

1. P. Exner and M. Jex, “On the ground state of quantum graphs with attractive \(\delta\)-coupling,” *Physics Letters A* 376 (2012), 713–717, arXiv:1110.1800, DOI: 10.1016/j.physleta.2011.12.035.
2. G. Berkolaiko and P. Kuchment, “Dependence of the spectrum of a quantum graph on vertex conditions and edge lengths,” in *Spectral Geometry*, Proceedings of Symposia in Pure Mathematics 84 (2012), 117–137, arXiv:1008.0369, DOI: 10.1090/pspum/084/1352.
3. P. Kurasov, “On the ground state for quantum graphs,” *Letters in Mathematical Physics* 109 (2019), 2491–2512, DOI: 10.1007/s11005-019-01192-w.
