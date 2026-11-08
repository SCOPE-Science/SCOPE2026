# Sharp two-harmonic bifurcation of periodic-orbit Fréchet means and an alignment-algorithm trap

## Finding

For every real \(a>0\), the smooth polynomial vector field on \(\mathbb C^2\cong\mathbb R^4\)
\[
\dot z=(1-|z|^2+i)z,\qquad \dot w=(a^2-|w|^2+2i)w
\]
has two distinct embedded periodic trajectories of minimal period \(2\pi\),
\[
\gamma_+(t)=(e^{it},a e^{2it}),\qquad
\gamma_-(t)=(e^{it},-a e^{2it}).
\]
They have the same constant speed \(\sqrt{1+4a^2}\). Define the equal-weight, squared phase-aligned \(L^2\) Fréchet functional on the quotient by circular time shifts, as specified below. The *entire set* of its minimizers is as follows.

For \(0<a\leq 1/2\), there is exactly one mean class, represented by \((e^{it},0)\); the minimum Fréchet variance is \(a^2\).

For \(a>1/2\), there are exactly two inequivalent mean classes. With \(\phi_* =\arccos(1/(4a^2))\), they are represented by
\[
\left(\cos(\phi_*/2)e^{it},\, \pm i a\sin(\phi_*)e^{2it}\right),
\]
and their common minimum variance is \(1/2-1/(16a^2)\). This classification is unchanged if the trajectories are normalized by arc length instead of physical time.

Moreover, the alternating phase-alignment/arithmetic-averaging iteration initialized at the unaligned arithmetic mean \(m_0(t)=(e^{it},0)\) remains fixed at \(m_0\) for every \(a>0\). For \(a>1/2\), this fixed point is **not even a local Fréchet minimum**, and the exact objective gap is
\[
F([m_0])-\min F=\frac{(4a^2-1)^2}{16a^2}>0.
\]

## Assumptions and scope

Identify the sample period circle with \(\mathbb R/(2\pi\mathbb Z)\). Set \(H=L^2(\mathbb R/(2\pi\mathbb Z),\mathbb C^2)\), viewed as a *real* Hilbert space with
\[
\langle u,v\rangle_H=\frac1{2\pi}\int_0^{2\pi}\operatorname{Re}(u_1(t)\overline{v_1(t)}+u_2(t)\overline{v_2(t)})\,dt.
\]
For a phase \(\theta\) let \(T_\theta u(t)=u(t+\theta)\); write \([u]\) for its orbit under this isometric circle action. Define
\[
d([u],[v])=\min_{\theta\in[0,2\pi]}\|u-T_\theta v\|_H,\qquad
F([u])=\tfrac12 d([u],[\gamma_+])^2+\tfrac12 d([u],[\gamma_-])^2.
\]
The minimization runs over the **whole quotient Hilbert space** \(H/S^1\), not only a finite-dimensional ansatz or the set of actual trajectories. The two sample curves are genuine distinct solutions of the same autonomous flow: direct substitution gives \(\dot z=iz\) and \(\dot w=2iw\) on \(|z|=1\), \(|w|=a\). Their first-coordinate winding makes the least period exactly \(2\pi\), and their speed is constant and positive. Their parameter-normalized arc lengths therefore induce precisely the same circular parametrizations as time normalization (up to shifts).

The iteration in the statement is: at a current representative \(m\), choose for each sample a phase minimizing its squared \(H\)-distance to \(m\), then replace \(m\) by the arithmetic average of the two aligned samples. The claim concerns the indicated natural initialization and exact phase minimization, not arbitrary initializations or implementations.

## Proof

**1. Global reduction without finite-dimensional restriction.** For arbitrary \(u,v_1,v_2\in H\), the parallelogram identity yields
\[
\tfrac12\|u-v_1\|_H^2+\tfrac12\|u-v_2\|_H^2
=\left\|u-\frac{v_1+v_2}{2}\right\|_H^2+\tfrac14\|v_1-v_2\|_H^2.
\]
Both individual phase minima exist by compactness and strong continuity of the shift action. Minimize the right-hand side jointly over \(u\) and two independent sample shifts. Thus *every* Fréchet minimizer must equal, up to a common phase, the average of a pair of optimally shifted samples, and *every* such average is a minimizer. A common shift can be removed; writing \(\phi\) for the relative shift, the problem reduces exactly to minimizing
\[
\tfrac14\|\gamma_+-T_\phi\gamma_-\|_H^2
=\tfrac12\bigl(1+a^2-C_a(\phi)\bigr),
\qquad C_a(\phi)=\cos\phi-a^2\cos(2\phi).
\]
The real inner-product identity for \(C_a\) follows either from harmonic orthogonality or by pointwise multiplication of the two complex Fourier coordinates.

**2. Sharp phase transition.** Write \(x=\cos\phi\in[-1,1]\). Then
\[
C_a=a^2+x-2a^2x^2.
\]
This is a strictly concave quadratic in \(x\), maximized uniquely at \(x=1\) if \(a\leq1/2\), and uniquely at \(x=1/(4a^2)\) if \(a>1/2\). In the first case the only maximizing phase is \(\phi=0\) modulo \(2\pi\), the unique average is \((e^{it},0)\), and its variance is \(a^2\). In the second case the maximizing phases are exactly \(\phi=\pm\phi_*\), where \(0<\phi_*<\pi/2\), and
\[
\max_\phi C_a(\phi)=a^2+\frac1{8a^2},\qquad
\min F=\frac12-\frac1{16a^2}.
\]
After the common phase normalization \(t\mapsto t-\phi/2\), the averaged curve has first Fourier coefficient \(\cos(\phi/2)>0\) and second Fourier coefficient \(-ia\sin\phi\). Hence the two maximizing shifts give the two displayed representatives. They cannot be phase-shift equivalent: equality of their strictly positive real first Fourier coefficients forces the relative shift to be zero modulo \(2\pi\), but then their nonzero second Fourier coefficients have opposite signs. Step 1 excludes all other minimizers, including nonsmooth or higher-harmonic candidates in \(H\).

**3. Exact stationary trap and its strict descent.** The unaligned average is \(m_0=(\gamma_++\gamma_-)/2=(e^{it},0)\). For either sample \(\gamma_\pm\), its inner product with \(m_0\) after phase shift is exactly \(\cos\phi\). Therefore its unique best-alignment phase is zero. Averaging returns \(m_0\), and iteration stays there indefinitely, with \(F([m_0])=a^2\). The difference from the minimum in Step 2 simplifies to
\[
 a^2-\left(\frac12-\frac1{16a^2}\right)
=\frac{(4a^2-1)^2}{16a^2}.
\]
To show this fixed point is not even a local minimum for \(a>1/2\), define \(M_\phi=(\gamma_++T_\phi\gamma_-)/2\). It converges strongly to \(m_0\) as \(\phi\to0\). But \(C_a'(0)=0\) and \(C_a''(0)=4a^2-1>0\), so for every sufficiently small nonzero \(\phi\), \(C_a(\phi)>C_a(0)\). By selecting those two sample phases in the definition of \(F\),
\[
F([M_\phi])\leq\tfrac14\|\gamma_+-T_\phi\gamma_-\|_H^2
=\tfrac12(1+a^2-C_a(\phi))<a^2=F([m_0]).
\]
The classes \([M_\phi]\) converge to \([m_0]\) in quotient distance. This proves strict descent in every neighborhood without assuming that the displayed phases remain optimal at \(M_\phi\).

## Verification

The standalone standard-library script `verify_phase.py` tests exact rational variance and gap formulas for eight positive amplitude values, complex-harmonic inner products at 48 sample times, upper bounds on the cross-correlation at 2,888 sampled phases, and 12 strict-descent cases. Run with `python3 verify_phase.py`. Its expected final line is:

`VERIFY_OK exact_parameter_cases=8 harmonic_inner_products=48 scanned_phases=2888 suboptimal_descent_checks=12`

The script is supplementary: global optimality, orbit count, and the failure of local minimality are proved by the exact continuous-variable arguments above, not by finite phase sampling.

## Relationship to prior work

Hering and Kuehn (2026) formulate phase-aligned Fréchet means of normalized periodic curves in \(L^2\), establish existence, discuss nonuniqueness and parametrization effects, and study the iterative alignment/averaging procedure. The present result applies that framework to two explicitly realized, equally and constantly parametrized periodic trajectories, determines *all* global means and their sharp transition in a single explicit family, and exhibits the exact fixed-nonminimum behavior of the natural arithmetic initialization. The general existence theorem and the general warning that iterations need not find a global optimum do **not**, by themselves, imply these constants or the strict-nonminimum fixed point. This example also distinguishes the phenomenon from time-versus-arc-length bias: those parametrizations agree here.

Mixon, Needham and Willey (2026) study global structure of means in *finite-group* orbit spaces, including examples of nonuniqueness and obstructions to alternating minimization. Their finite-group results and examples do not directly cover the continuous circle-shift orbit space or the explicit one-to-two mean transition for genuine periodic flow trajectories. Bigot (2011) and Bigot–Gendre (2012) develop related Fourier-based curve registration and statistical shift-estimation settings; those problems use different estimation goals and do not provide the exact dynamical two-trajectory classification established here in the inspected portions. The result uses standard Hilbert-space completion and trigonometric optimization; these ingredients are not claimed to be new.

## Limitations

This is an explicit two-sample construction in a decoupled polynomial system, not a general uniqueness theorem or typical-case result for ensembles of periodic trajectories. It does not prove a general convergence or nonconvergence theorem for all phase-alignment algorithms or initial states. The mean need not itself be a trajectory. The algebraic phase-transition picture does not imply robustness to perturbations of the flow without further analysis. Independent verification and exhaustive historical-priority assessment remain outstanding.

## References

1. P. Hering and C. Kuehn, *Fréchet Means of Periodic Orbits in Dynamical Systems: Geometry, Dynamics, and Diagnostics*, arXiv:2606.10748v1 (first posted 2026-06-09), https://arxiv.org/abs/2606.10748 .
2. D. G. Mixon, T. Needham and N. Willey, *Certifiably Correct Fréchet Means in Orbit Spaces*, arXiv:2610.24191 (2026), https://arxiv.org/abs/2610.24191 .
3. J. Bigot, *Fréchet Means of Curves for Signal Averaging and Application to ECG Data Analysis*, arXiv:1111.1855 (2011), https://arxiv.org/abs/1111.1855 .
4. J. Bigot and X. Gendre, *Minimax Properties of Fréchet Means of Discretely Sampled Curves*, arXiv:1210.0771 (2012), https://arxiv.org/abs/1210.0771 .
