# Uniform two-state approximation and global reset-rate selection for the Ising dimer

## Finding

Let \(H=-J\sigma_z\otimes\sigma_z+(\Omega/2)(\sigma_x\otimes I+I\otimes\sigma_x)\), with \(J,\Omega>0\). The entire dimer is reinitialized to \(D=|\downarrow\downarrow\rangle\) at independent Poisson times of rate \(r>0\). Write \(j=J/\Omega\), \(q=r/\Omega\), \(h_j=H/\Omega\), \(\omega_j=\sqrt{j^2+1}\), and \(\delta_j=\omega_j-j\). Measure time in units of \(1/\Omega\). Let \(\mathcal B\) be the maximum absolute CHSH expectation for nondegenerate two-outcome projective qubit observables (both eigenvalues \(\pm1\)).

The effective two-state evolution \(\phi_j(t)\) defined below approximates the exact density projector uniformly in time, and hence its ensemble average in trace norm against **any** probability law on the dimensionless age \(t\ge0\), with error at most \(2\sqrt{1-j/\omega_j}\). In particular, for the Poisson stationary state \(\rho_{j,q}\), the following bound holds simultaneously for every \(q>0\):
\[
\left|\mathcal B(\rho_{j,q})-2\sqrt{1+\left(\frac{\kappa}{1+\kappa^2}\right)^2}\right|
\le 4\sqrt2\sqrt{1-j/\omega_j},\qquad \kappa=q/\delta_j.
\]
It follows that the supremum over **all** reset rates is \(\sqrt5+O(j^{-1})\), is attained at a positive rate for all sufficiently large \(j\), and every choice of maximizing rate satisfies \(q_*/\delta_j\to1\) as \(j\to\infty\). Equivalently \(r_*\sim\Omega^2/(2J)\); the physical rate tends to zero when \(\Omega\) is held fixed. The dimensionless rate tends to zero regardless of the choice of time unit. This is an asymptotic statement, not an upper bound of \(\sqrt5\) at finite \(j\).

## Proof

Put \(B=(|\uparrow\uparrow\rangle+|\downarrow\downarrow\rangle)/\sqrt2\), \(A=(|\uparrow\uparrow\rangle-|\downarrow\downarrow\rangle)/\sqrt2\), and \(S=(|\uparrow\downarrow\rangle+|\downarrow\uparrow\rangle)/\sqrt2\). The reset vector is \((B-A)/\sqrt2\), the state orthogonal to these three is unoccupied, and \(h_j A=-j A\). On \((B,S)\) the matrix is \(\begin{pmatrix}-j&1\\1&j\end{pmatrix}\), with eigenvalues \(\pm\omega_j\). The upper eigenvector \(U=\sin\theta_j B+\cos\theta_j S\) has \(\sin^2\theta_j=(1-j/\omega_j)/2\); the lower one is \(\cos\theta_j B-\sin\theta_j S\).

Define \(\phi_j(t)=(e^{i\omega_j t}B-e^{ijt} A)/\sqrt2\). Subtracting it from the exact evolution gives exactly
\[
e^{-ih_jt}D-\phi_j(t)=\frac{\sin\theta_j}{\sqrt2}(e^{-i\omega_j t}-e^{i\omega_j t})U.
\]
Its norm is at most \(\sqrt2\sin\theta_j\) uniformly in \(t\). For two unit vectors the trace-norm difference of projectors is at most twice the norm of their difference. Convexity of trace norm gives the announced uniform estimate after averaging over any age law. No stationarity of a general non-Poisson clock is asserted by this estimate.

At positive \(q\), the stationary age law is \(q e^{-qt}dt\), so the exact state is the average of the exact projector against that law. Uniqueness also follows since the weight with no reset since time zero is \(e^{-qt}\). The effective state has only \(\uparrow\uparrow,\downarrow\downarrow\) support and its two diagonal entries in that order are \(1/[2(1+\kappa^2)]\) and \((1+2\kappa^2)/[2(1+\kappa^2)]\), with upper off-diagonal entry \(i\kappa/[2(1+\kappa^2)]\). These follow by integrating the sine and cosine at frequency \(\delta_j\). Its Pauli tensor has \(T_{zz}=1\) and \(T_{xy}=T_{yx}=-\kappa/(1+\kappa^2)\), all others zero. The Horodecki criterion (2 times the square root of the sum of the top two squared singular values of the Pauli tensor) gives the displayed comparison profile. The CHSH operator norm is at most \(2\sqrt2\), so the maximal value is \(2\sqrt2\)-Lipschitz in trace norm. This converts the uniform state bound into the uniform Bell bound.

The profile tends to 2 at both ends \(\kappa\downarrow0,\kappa\to\infty\), and has a unique maximum \(\sqrt5\) at \(\kappa=1\), with a positive gap outside every neighborhood of 1. The error bound is \(O(1/j)\). For sufficiently large \(j\), uniformity forces all points outside a fixed compact neighborhood interval to have value strictly below the value at 1. Continuity in \(q>0\) follows by integration of the bounded projector against the exponential age density, locally dominated in \(q\). Maximizing on that compact interval proves attainment and global optimality; applying the same separation to arbitrarily small neighborhoods proves selection for every maximizing rate. Finally \(\delta_j=1/(\omega_j+j)\sim1/(2j)\).

## Relation to established results

The exact resetting dimer, its stationary state and related strong-coupling scaling for entanglement observables are established by Kulkarni and Majumdar (arXiv:2307.07485; PRA 108, 062210). The two-qubit CHSH criterion is due to Horodecki et al. (Phys. Lett. A 200, 340–344). The earlier [strong-coupling quantum-reset window](https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-bell-nonlocality-in-a-strong-coupling-quantum-reset-window--1c9d1d25a201/RESULT.md) and [singular Bell-nonlocality window](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-a-singular-bell-nonlocality-window-for-two-interacting-spins-und--b5037141c959/RESULT.md) give the same fixed-scaling profile and its \(\sqrt5\) peak, and give the fixed-\(j\) weak-reset behavior. The latter record also gives the exact finite-rate Pauli tensor. These are not new claims here. A pointwise scaling limit alone does not bound CHSH values on reset sequences leaving the scaling window. The contribution here is the explicit uniform comparison obtained at the evolution level and its use to control the global reset-rate optimization and all maximizing rates.

## Verification and limits

The supplied NumPy `check.py` checks sample stationary density matrices by spectral averaging and a Liouville linear solve, and compares the trace-norm and CHSH bounds on a finite grid. Its checks of the known scaling profile and fixed-interaction weak-reset limit are baseline comparisons. The uniformity and optimizer conclusions are analytic. No claim is made about uniqueness of the finite-coupling maximizing rate, trajectory-conditioned Bell tests, other reset states, or more spins.
