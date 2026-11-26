# Independent mathematical audit

## correctness

PASS

In the normalized Weyl matrix basis, analysis of each basis matrix on the projector orbit is a character of the two orbit indices times its value at the unshifted projector. Character orthogonality gives singular values sqrt(N) times ambiguity moduli on the full complex matrix space, including the maximum sqrt(N) at the identity. Expanding the constant and impulse terms gives the two axis branches and the mixed branch (up to phase and conjugation conventions). All residues occur as mixed products, including zero from 2 times N/2. Writing z=rho exp(i theta), AM–GM optimizes the mixed ratio at rho=sqrt(N); even N gives the zero grid pi Z/N, hence numerator sin(d) with d the distance to that grid and denominator at least sqrt(N)-cos(d). The ratio is strictly increasing for d between 0 and eta=pi/(2N). At equality theta must be at distance eta from pi, giving precisely the two claimed impulses. Both axis numerators at these points are N-2sqrt(N)cos(eta), at least 2sqrt(N)sin(eta) by equality at N=6 and monotonicity in N thereafter. Thus axes do not spoil attainment, the lifting is invertible, and applying it to xx* yields phase retrieval. A separate full-lifting check of Weyl column norms and orthogonality at N=6,8,12 for both optimizers passed (`python3 /workspace/audit_evidence/reproduce.py 2`).

## originality

PASS

The Weyl frame spectrum, rank characterization and chirp shear are prior ingredients. The exact sharp even-order condition number, equality set and attainment are distinct from the strongest inspected statements. In prime order the mixed phase grid lacks the residue zero, so even-order optimization is not a substitution into the prime formula. Nearby exact same-date results concern different windows or orders.

## value

PASS

This natural two-real-parameter perturbation gives a usable exact conditioning ceiling rather than just an invertible window. The result gives the only window parameters attaining it, explains the parity-sensitive obstruction and threshold where the axis branches become harmless, and quantifies the deterioration of the best attainable stability with dimension. The linear-lifting objective makes this useful for choosing and benchmarking a simple window even though it makes no unrestricted window claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
