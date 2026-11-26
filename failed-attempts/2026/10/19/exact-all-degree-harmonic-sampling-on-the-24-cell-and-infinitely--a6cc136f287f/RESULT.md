# Exact all-degree harmonic sampling on the 24-cell and infinitely many tight interpolation degrees

## Finding

Let \(X\subset S^3\) be the 24 vertices of the regular 24-cell, normalized as
\[
X=\{(\pm e_i\pm e_j)/\sqrt2:1\le i<j\le4\}.
\]
For every integer \(\ell\ge0\), let \(\mathcal H_\ell\) be the complex spherical harmonics of **exactly** degree \(\ell\) on \(S^3\), with probability-normalized surface measure, and let \(E_\ell:\mathcal H_\ell\to\mathbb C^X\) be point evaluation. The parity constraint \(f(-x)=(-1)^\ell f(x)\) confines its range to a 12-dimensional subspace \(\mathcal Y_\ell\).

**Theorem.** Choose the 12 unit representatives \(R=\{r_{ij}^{\pm}=(e_i\pm e_j)/\sqrt2:1\le i<j\le4\}\). Let \(U_\ell\) be the Chebyshev polynomial of the second kind, normalized by \(U_\ell(1)=\ell+1\), and set
\[
\alpha_\ell=U_\ell(1/2)=\frac{2}{\sqrt3}\sin\frac{(\ell+1)\pi}{3},
\qquad B_\ell=\bigl(U_\ell(\langle r,s\rangle)\bigr)_{r,s\in R}.
\]
For even \(\ell\), set \(\beta_\ell=(-1)^{\ell/2}\). The complete spectrum of \(B_\ell\), including zero eigenvalues, is
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
\ell+1+8\alpha_\ell+3\beta_\ell&1\\
\ell+1-4\alpha_\ell+3\beta_\ell&2\\
\ell+1-\beta_\ell&9.
\end{array}
\]
For odd \(\ell\), its complete spectrum is
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
\ell+1+4\alpha_\ell&4\\
\ell+1-2\alpha_\ell&8.
\end{array}
\]
The 24-by-24 Gram matrix \(E_\ell E_\ell^*\) has these eigenvalues multiplied by \(2(\ell+1)\), together with an additional 12 parity-forced zero eigenvalues (and retaining any zeros already displayed).

In particular, its rank is
\[
\begin{array}{c|rrrrrrrrrrr|c}
\ell&0&1&2&3&4&5&6&7&8&9&10&\ell\ge11\\\hline
\operatorname{rank}E_\ell&1&4&9&8&11&12&10&12&12&12&11&12.
\end{array}
\]
Thus \(E_\ell\) first maps onto all parity-compatible data at degree \(5\), subsequently loses rank at degrees \(6\) and \(10\), and is onto \(\mathcal Y_\ell\) at **every** degree \(\ell\ge11\); the last threshold is sharp. Moreover, among all degrees with rank 12, the positive sampling singular values are identical **if and only if**
\[
\ell\equiv5\pmod6.
\]
At precisely those degrees the 12 representative-node reproducing kernels are mutually orthogonal, and every parity-compatible data vector \(y\) has a minimum-norm interpolant of squared \(L^2\) norm \(\frac{1}{2(\ell+1)^2}\sum_{x\in X}|y(x)|^2\).

## Assumptions and scope

The theorem concerns complex-valued spherical harmonics of a **single homogeneous degree**, not sums of degrees, and the explicit 24-cell \(X\) above. The domain is \(\ell\in\mathbb Z_{\ge0}\), with no hidden large-degree hypothesis. The normalized probability measure on \(S^3\) fixes the reproducing-kernel normalization. Since antipodes impose a necessary relation on every sample vector, full interpolation means surjectivity to \(\mathcal Y_\ell\), **not** to all \(\mathbb C^{24}\). The twelve representatives may be reordered without changing the spectrum; replacing a representative by its antipode conjugates the odd-degree matrices by a diagonal sign matrix.

## Proof

**1. Addition theorem and parity compression.** An orthonormal basis of \(\mathcal H_\ell\) for probability measure yields the reproducing kernel
\[
K_\ell(x,z)=(\ell+1)U_\ell(\langle x,z\rangle),
\qquad K_\ell(x,x)=(\ell+1)^2.
\]
This is the dimension-four addition theorem, since \(\dim\mathcal H_\ell=(\ell+1)^2\). Restricting to \(R\), the Gram matrix is \((\ell+1)B_\ell\). Extending to \(R\cup(-R)\), the full Gram matrix is unitarily equivalent to twice this 12-by-12 block and a 12-by-12 zero block. Hence its nonzero spectral data are exactly those claimed.

**2. The even-degree adjacency algebra.** Let \(A\) be the graph adjacency matrix on the twelve root lines, where two lines are adjacent iff their absolute inner product is \(1/2\). Every line is adjacent to eight others and orthogonal to the remaining three. Associate the two sign choices \(r_{ij}^+\) and \(r_{ij}^-\) with each of the six edges of the complete graph on four vertices. Then
\[
A=A_{L(K_4)}\otimes J_2.
\]
The unsigned four-vertex/edge incidence matrix \(C\), of dimensions \(6\times4\), satisfies \(C^*C=2I_4+J_4\) and \(CC^*=2I_6+A_{L(K_4)}\). Thus the eigenvalues of the line-graph adjacency are \(4\) (once), \(0\) (three times), and \(-2\) (twice); those of \(A\) are \(8\) (once), \(0\) (nine times), and \(-4\) (twice). For even \(\ell\), \(U_\ell\) is even and \(U_\ell(0)=\beta_\ell\). Therefore, with \(J=J_{12}\),
\[
B_\ell=(\ell+1-\beta_\ell)I+(\alpha_\ell-\beta_\ell)A+\beta_\ell J.
\]
The all-ones vector belongs to the eigenvalue-eight space of \(A\); the other two eigenspaces are perpendicular to it. This gives the three stated eigenvalues and multiplicities. Their orthogonal projectors are respectively
\[
P_1=J/12,\quad P_{-4}=A(A-8I)/48,\quad P_0=I-P_1-P_{-4}.
\]
These formulas also identify exact missing-data constraints in deficient degrees.

**3. The odd-degree signed algebra.** Assemble the twelve **unnormalized** representatives \(e_i\pm e_j\) as columns of a matrix \(M\in\mathbb R^{4\times12}\). Each of the six coordinate pairs contributes the sum of outer products \(2e_ie_i^*+2e_je_j^*\), so
\[
MM^*=6I_4.
\]
Set \(S=M^*M-2I_{12}\). Its diagonal is zero, and its off-diagonal entries are \(2\langle r,s\rangle\), equal to \(\pm1\) on adjacent lines and zero on orthogonal lines. Hence for odd \(\ell\), because \(U_\ell(0)=0\),
\[
B_\ell=(\ell+1)I+\alpha_\ell S.
\]
The eigenvalues of \(S\) are \(4\) with multiplicity \(4\) and \(-2\) with multiplicity \(8\). Indeed, \(M^*M\) has eigenvalue \(6\) four times and \(0\) eight times. The two orthogonal spectral projectors are
\[
P_4=(S+2I)/6,\qquad P_{-2}=(4I-S)/6.
\]
This proves the odd-degree spectral law, including the multiplicities.

**4. All-degree rank and the last defect.** The values of \(\alpha_\ell\) are the repeating six-term sequence \(1,1,0,-1,-1,0\), while for even degrees \(\beta_\ell\) alternates between \(1\) and \(-1\). Direct substitution for \(0\le\ell\le10\) gives the finite rank row in the theorem, with the last defect \(\ell=10\). For all even \(\ell\ge12\), the three displayed eigenvalues are bounded below respectively by \(\ell-10\), \(\ell-6\), and \(\ell\), hence are strictly positive. For all odd \(\ell\ge5\), the two displayed eigenvalues are at least \(\ell-3\) and \(\ell-1\), also strictly positive. This proves the assertion for **every** larger degree without extrapolation from finite computations.

**5. Precisely the tight degrees and reconstruction.** In full-rank odd degrees the two eigenvalues coincide iff \(6\alpha_\ell=0\), which among odd integers is equivalent to \(\ell\equiv5\pmod6\). In even degrees, equality of the first two eigenvalues would force \(\alpha_\ell=0\), whereas equality of the last two would then force \(\beta_\ell=0\), impossible. Therefore no full-rank even degree is tight. At the odd tight degrees, \(B_\ell=(\ell+1)I\), so the representative-node Gram matrix is \((\ell+1)^2I\). For prescribed parity-compatible data \(z=(y(r))_{r\in R}\), the minimum-norm solution is
\[
f_y(x)=\sum_{r\in R}c_rK_\ell(x,r),\qquad c=((\ell+1)B_\ell)^+z,
\]
provided \(z\) lies in the range of \(B_\ell\); here \({}^+\) is the Moore–Penrose pseudoinverse. This condition is necessary and sufficient, and the squared norm is \(z^*((\ell+1)B_\ell)^+z\). In the full-rank tight case \(c=z/(\ell+1)^2\), giving the asserted exact norm identity. The spectral projectors above express all obstructed data spaces without numerical inversion.

## Verification

Run `python3 CHECK.py` from the directory containing this document. The checker uses only the Python standard library, builds all twelve root-line representatives with rational coordinates before common normalization, verifies the signed and unsigned adjacency identities and all five spectral projectors exactly, and compares predicted spectra and exact Gram ranks for every degree from \(0\) through \(120\). It additionally checks the 24-node antipodal compression for degrees through \(15\). The run completed with `PASS: 399 degree/spectral/rank assertions plus exact geometry/projector identities`. These finite checks are independent corroboration of the all-degree algebraic argument; the inequalities in Proof step 4 establish the infinite claim.

## Relationship to prior work

Cohn, Conway, Elkies and Kumar introduced a 24-cell spherical-code deformation problem and calculated its inner-product distribution; the present result uses the fixed standard root configuration rather than their optimization problem. Hirao, Nozaki and Tasaka proved the 24-cell root system is a tight harmonic-index design at degrees \(2,4,10\), and their later group-theoretic paper determines the **mean-zero harmonic strength** of the binary tetrahedral group. Those results account for specific constant-vector obstructions here, but a vanishing sum of sample values is weaker than the complete sampling-rank classification, exact sector eigenvalues, and infinitely many mutually orthogonal representative-node kernel families. Earlier calculations also give the degree-three defect for type-\(D_n\) roots, the cumulative harmonic-band behavior of a rotated 24-cell, and full odd-degree recovery at sufficiently high degree for a larger \(F_4\) root configuration containing the 24-cell; those covered consequences are not asserted as new. None of these implications gives the even-degree three-sector spectrum, the first full-rank degree \(5\), the sharp degree-\(11\) permanent threshold, or the exact family \(\ell\equiv5\pmod6\) of tight single-degree 24-cell sampling. No claim is made that the classical 24-cell geometry, addition theorem, or harmonic-strength vanishing is new.

## Limitations

This theorem gives exactly the single-degree harmonic evaluation spectrum on the specified fixed node set. It does not classify arbitrary 24-point spherical designs, perturbation stability, partial-node erasure robustness, or full interpolation without antipodal compatibility. The computational tests cover finitely many degrees and do not independently certify the analytic bound. A logically equivalent decomposition may already occur under association-scheme, binary-tetrahedral representation, or spherical-code terminology outside the inspected sources; the accessible literature checks do not independently certify publication priority.

## References

1. H. Cohn, J. H. Conway, N. D. Elkies, and A. Kumar, *The \(D_4\) Root System Is Not Universally Optimal*, arXiv:math/0607447, first public arXiv version 19 July 2006 (later published in *Experimental Mathematics* 16 (2007), 313–320), especially Sections 1–2 and its 24-cell inner-product distribution.
2. M. Hirao, H. Nozaki, and K. Tasaka, *Spherical Designs and Modular Forms of the \(D_4\) Lattice*, arXiv:2303.09000, initial preprint 16 March 2023, especially Sections 1 and 3 and the harmonic-index design theorem.
3. M. Hirao, H. Nozaki, and K. Tasaka, *Spherical Designs for Finite Quaternionic Unit Groups and Their Applications to Modular Forms*, arXiv:2507.01358, initial preprint 2 July 2025, especially Theorem 1.2(i) on binary tetrahedral harmonic strength.
4. P. Delsarte, J.-M. Goethals, and J. J. Seidel, *Spherical Codes and Designs*, *Geometriae Dedicata* 6 (1977), 363–388 (addition theorem and harmonic/design framework).
