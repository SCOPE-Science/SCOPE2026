# Sharp directed three-cycle instability before isolated ideal-storage oscillation

## Finding

Consider the coupled ideal-storage recurrence below with a nonnegative row-stochastic interaction matrix. There is a sharp, explicitly algebraic parameter threshold below which a directed three-site cycle is linearly stable and above which it is linearly unstable, although each isolated site remains linearly stable. Precisely, on the parameter line \(c=2\delta/5\), \(C_r=2\delta\), \(0<\delta<1\), and for the directed cycle \(W_{12}=W_{23}=W_{31}=1\), the homogeneous equilibrium is linearly asymptotically stable if and only if \(0<\delta<\delta_*\), with a nonhomogeneous unit-modulus multiplier pair at \(\delta=\delta_*\), and linearly unstable when \(\delta_*<\delta<1\). Here \(\delta_*\) is the unique positive root of
\[
3\delta^4+14\delta^3+17\delta^2-10\delta-12=0,
\qquad 0.8141<\delta_*<0.8142.
\]
For every \(0<\delta<1\), all nonnegative symmetric row-stochastic interactions, of any size, are linearly stable at the same homogeneous equilibrium. The same holds for every nonnegative row-stochastic interaction matrix of size one or two, including nonsymmetric matrices. Thus three is the minimum number of sites for an instability created solely by directed interactions within this model family.

## Assumptions and scope

For a positive integer \(n\), define the synchronous update on \(S_i\ge0\), \(0<R_i<1\) by
\[
S_i^+=(1-R_i)S_i+c,\qquad
R_i^+=\left[1+\exp\!\left(C_r-5S_i\sum_{j=1}^nW_{ij}R_j\right)\right]^{-1}.
\]
Assume \(c>0\), \(C_r\ge0\), \(W_{ij}\ge0\), and \(\sum_jW_{ij}=1\) for each \(i\). A row-stochastic matrix need not be symmetric. Define \(r=[1+\exp(C_r-5c)]^{-1}\); the homogeneous fixed point is \(S_i=c/r\), \(R_i=r\). Let \(\delta=5c(1-r)\). The stability assertions concern the Jacobian eigenvalues of this discrete-time map, with strict linear stability meaning every eigenvalue has modulus below one. The explicit threshold is asserted only on the physical parameter line \(r=1/2\), or equivalently \(c=2\delta/5\) and \(C_r=2\delta\).

## Proof

Differentiating at the homogeneous fixed point yields three \(n\times n\) scalar blocks and, for each eigenvalue \(w\) of \(W\), the characteristic factor of the corresponding two-dimensional mode:
\[
A(w)=\begin{pmatrix}1-r&-c/r\\5r^2(1-r)&\delta w\end{pmatrix},\quad
p_w(z)=z^2-(1-r+\delta w)z+\delta\bigl[r+(1-r)w\bigr].
\]
This spectral factorization holds even when \(W\) is not diagonalizable: the characteristic determinant is the product of these factors, with algebraic multiplicities, as follows by triangularizing \(W\) over \(\mathbb C\).

When \(w\) is real and \(-1\le w\le1\), put \(T=1-r+\delta w\) and \(D=\delta[r+(1-r)w]\). The real quadratic Jury inequalities follow from
\[
1-T+D=r[1+\delta(1-w)]>0,
\]
\[
1+T+D=2-r+2\delta(r-1)+\delta(2-r)(w+1)>r>0,
\]
\[
1-D=1-\delta+\delta(1-r)(1-w)>0.
\]
For the middle inequality the first displayed lower bound is \(2-r-2\delta(1-r)>r\) because \(\delta<1\). Every eigenvalue of a nonnegative row-stochastic matrix has modulus at most one. If \(W\) is symmetric, all its eigenvalues are real, so every mode is strictly Schur-stable. If \(n=2\), writing \(W=\left(\begin{smallmatrix}a&1-a\\b&1-b\end{smallmatrix}\right)\) gives eigenvalues \(1\) and \(a-b\in[-1,1]\). The case \(n=1\) is immediate. These conclusions cover arbitrary (not necessarily symmetric) nonnegative row-stochastic matrices of size at most two.

For the directed three-cycle, the eigenvalues of \(W\) are \(1,\omega,\overline\omega\), where \(\omega=(-1+i\sqrt3)/2\). On the parameter line \(r=1/2\), the homogeneous mode \(w=1\) is strictly stable by the preceding argument. In a nonhomogeneous mode, write
\[
T=\tfrac12+\delta\omega,\qquad
D=\tfrac{\delta}{2}(1+\omega),\qquad
p_\omega(z)=z^2-Tz+D.
\]
For \(|D|<1\), the strict complex quadratic Schur–Cohn criterion is \(|T-\overline T D|<1-|D|^2\). Here \(|D|=\delta/2\), and exact simplification gives
\[
(1-|D|^2)^2-|T-\overline T D|^2
=-\frac{3\delta^4+14\delta^3+17\delta^2-10\delta-12}{16}.
\]
The quartic has exactly one positive root by Descartes' rule of signs. Its values at \(\delta=0\) and \(\delta=1\) are \(-12\) and \(12\), and its values at the exact rational endpoints \(8141/10000\) and \(8142/10000\) have opposite signs. Hence it has exactly one root \(\delta_*\) in the stated interval. The strict Schur criterion is satisfied precisely below the root. At equality, the Schur–Cohn boundary with \(|D|<1\) gives one simple unit-modulus root of the nonhomogeneous quadratic and a second root strictly inside the unit disk. Its complex-conjugate spatial mode provides the conjugate multiplier on the unit circle. Above the threshold the complex quadratic fails Schur stability strictly, and since its root moduli cannot cross through zero or remain both within the disk, at least one multiplier lies outside the unit disk; conjugacy supplies the second unstable multiplier.

For an entirely rational witness, at \(\delta=5/6\) take \(c=1/3\), \(C_r=5/3\) and \((S_*,R_*)=(2/3,1/2)\). The quartic equals \(49/48>0\), so the directed three-cycle is linearly unstable; its characteristic spectral radius is approximately \(1.020441989493\). Each individual oscillator is strictly stable, as is every symmetric row-stochastic coupling at the same parameter values.

## Verification

The accompanying standalone `verify.py` performs exact symbolic differentiation of the modal Jacobian, matches the characteristic polynomial against the direct real six-dimensional Jacobian, verifies the complex Schur–Cohn identity, checks the signs of the quartic at rational test parameters, and checks the real-eigenvalue Jury inequalities algebraically. It also computes numerical roots solely as a diagnostic and reports two unstable and four stable multipliers at \(\delta=5/6\). Execute `python verify.py` with SymPy available. Exact symbolic identities establish the infinite-parameter statement; numerical eigenvalues and bounded parameter samples alone do not.

## Relationship to prior work

Hordijk's 2026 ideal-storage cellular automaton study analyzes bifurcation and spiral behavior of a symmetric Moore-neighborhood averaging model, and its underlying scalar ideal-storage recurrence. The directed interaction matrix here is a mathematically explicit asymmetric extension of the same update equations. The 2010 coupled ideal-storage model work likewise uses spatial neighborhoods and reports spiral dynamics, without the present three-node directed-cycle stability boundary. The known general idea that directed topology can destabilize locally stable units is not new: Asllani and collaborators established topology-driven instabilities for continuous-time reaction–diffusion systems on directed networks. Their continuous-time Laplacian criterion does not determine the discrete-time ideal-storage cubic-mode polynomial, the sharp quartic threshold here, or minimality under nonnegative row-stochastic coupling. The contribution is confined to these model-specific exact results, not the broad phenomenon of topology-driven instability.

## Limitations

This is a local linear stability result, not a proof of a nonlinear attractor, travelling wave, invariant circle, or spiral, and no nonlinear claim is made at equality. The class permits directed weighted averaging and is therefore more general than the symmetric square-lattice diffusion architecture used in the motivating numerical study. The quartic classification applies to the specified physical one-parameter slice and directed three-cycle, not to every directed graph or parameter choice. Independent scientific validation and exhaustive historical-priority verification have not been performed.

## References

1. W. Hordijk, *Spontaneous Spirals in Spatial Systems* (2026), arXiv:2610.38710v1, first posted 2026-10-28, https://arxiv.org/html/2610.38710v1.
2. A. Dress, W. Hordijk, L. Wei and P. Serocka, *The Ideal Storage Cellular Automaton Model* (2010), Dagstuhl Seminar Proceedings 10231, https://drops.dagstuhl.de/entities/document/10.4230/DagSemProc.10231.8.
3. M. Asllani, J. D. Challenger, F. S. Pavone, L. Sacconi and D. Fanelli, *The theory of pattern formation on directed networks*, Nature Communications 5, 4517 (2014), https://doi.org/10.1038/ncomms5517, arXiv:1402.0760.
