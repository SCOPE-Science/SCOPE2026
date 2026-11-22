# Uniform sharp quantum transport blockade across Mycielskian layers

## Finding
Let \(G_n\) be any finite simple \(r\)-regular graph on \(n\) vertices, where \(r\ge2\) is fixed and \(n\to\infty\) through admissible values. Form its Mycielskian \(M(G_n)\) with original vertices \(v_i\), shadow vertices \(u_i\), and a hub \(w\). Consider the single-excitation adjacency Hamiltonian \(H=A(M(G_n))\), with all graph edges of hopping amplitude one and initial state \(|w\rangle\). Let \(P_n(t)\) be the total Born probability on the \(n\) original vertices at time \(t\ge0\). Then
\[
\lim_{n\to\infty}n\sup_{t\ge0}P_n(t)=4r^2,
\qquad
\lim_{n\to\infty}nP_n\!\left(\frac{\pi}{\sqrt n}\right)=4r^2.
\]
In particular, the quantum probability of reaching the entire original layer is uniformly \(O_r(n^{-1})\), irrespective of the base graph's internal geometry. For the continuous-time classical walk with rate one on each edge, also started at \(w\), the probability \(C_n(t)\) of occupying an original vertex satisfies
\[
\lim_{n\to\infty}C_n(t)=\frac{1-e^{-2rt}}2\quad\text{for each fixed }t>0.
\]
Hence the same networks exhibit a strictly positive classical outer-layer occupation at any fixed positive time, but vanishing quantum occupation at **all** times.

## Assumptions and scope
The Mycielski construction retains every edge \(v_iv_j\) of \(G_n\), inserts \(u_iv_j\) whenever \(v_iv_j\) is a base edge, and joins \(w\) to every shadow \(u_i\), without original-to-hub edges or shadow-to-shadow edges. The base is simple and undirected, possibly disconnected, and has degree exactly \(r\). The quantum time evolution is \(e^{-itA}\); the classical generator has off-diagonal transition rate one for each edge and diagonal equal to minus vertex degree. No decoherence, site potential, or loss is present. All limits hold with fixed \(r\) and growing \(n\).

## Proof
Put
\[
|O\rangle=n^{-1/2}\sum_i|v_i\rangle,\qquad
|S\rangle=n^{-1/2}\sum_i|u_i\rangle,\qquad |W\rangle=|w\rangle.
\]
Regularity gives \(A|O\rangle=r|O\rangle+r|S\rangle\), \(A|S\rangle=r|O\rangle+\sqrt n|W\rangle\), and \(A|W\rangle=\sqrt n|S\rangle\). Thus these three orthonormal vectors span an invariant subspace containing the initial state, with compressed Hamiltonian
\[
Q_n=\begin{pmatrix}r&r&0\\r&0&\sqrt n\\0&\sqrt n&0\end{pmatrix},
\quad
\chi_n(z)=\det(zI-Q_n)=z^3-rz^2-(n+r^2)z+rn.
\]
Consequently the full-layer probability is the squared modulus of the scalar matrix element \(\alpha_n(t)=(e^{-itQ_n})_{1,3}\). Because \(Q_n\) is a symmetric irreducible tridiagonal matrix its three eigenvalues \(\lambda_-<\lambda_0<\lambda_+\) are real and simple. The corner resolvent entry is \([(zI-Q_n)^{-1}]_{1,3}=r\sqrt n/\chi_n(z)\); spectral residues yield the **exact finite-size formula**
\[
\alpha_n(t)=r\sqrt n\sum_{\sigma\in\{-,0,+\}}\frac{e^{-it\lambda_\sigma}}{\chi_n'(\lambda_\sigma)},\qquad P_n(t)=|\alpha_n(t)|^2.
\]
Set \(c_\sigma=r\sqrt n/\chi_n'(\lambda_\sigma)\). Ordered roots give \(c_-,c_+>0>c_0\). The off-diagonal resolvent is \(O(z^{-3})\), so \(c_-+c_0+c_+=0\). The triangle inequality therefore establishes the all-time finite-size bound
\[
P_n(t)\le4c_0^2=\frac{4r^2n}{[\chi_n'(\lambda_0)]^2}.
\]
At fixed \(r\) and growing \(n\), the characteristic equation or eigenvalue perturbation gives \(\lambda_0=r+O_r(n^{-1})\) and \(\lambda_\pm=\pm\sqrt n+O_r(n^{-1/2})\), so \(c_0=-r/\sqrt n+O_r(n^{-3/2})\) and \(c_\pm=r/(2\sqrt n)+O_r(n^{-1})\). The upper bound therefore yields \(\limsup n\sup_tP_n(t)\le4r^2\). At \(t_n=\pi/\sqrt n\), the two outer eigenphases approach \(-1\), while the central eigenphase approaches \(+1\). Hence \(\sqrt n\alpha_n(t_n)\to-2r\), proving the matching lower bound and the theorem.

For the classical walk, aggregate the probabilities at hub, shadows and originals as \(h_n(t),s_n(t),o_n(t)\). Each shadow has one hub neighbor and \(r\) original neighbors; each original has \(r\) shadow neighbors, while original-to-original hops stay within the original class. Thus
\[
h_n'=-nh_n+s_n,\qquad o_n'=r(s_n-o_n),\qquad s_n=1-h_n-o_n
\]
with \((h_n,s_n,o_n)(0)=(1,0,0)\). The integrating-factor formula implies \(0\le h_n(t)\le e^{-nt}+1/n\). Solving the final scalar equation gives
\[
o_n(t)=\frac{1-e^{-2rt}}2-r\int_0^t e^{-2r(t-s)}h_n(s)\,ds.
\]
Its error from the displayed limiting value is at most \(r(1+t)/n\) for every fixed \(t\ge0\); this proves the classical statement without unproved mixing assumptions.

## Verification
The accompanying `verify.py` reconstructs full Mycielski adjacency matrices from seven explicit regular circulant bases and compares their exact-time numerical matrix exponentials against the three-dimensional quotient at three times each. It also checks the characteristic cubic and the residue signs, all-time spectral bound, and asymptotic coefficient on additional parameter sizes. All 33 recorded cases passed, with maximum full-versus-quotient probability discrepancy below \(4.5\times10^{-16}\). The proof above, not these finite calculations, establishes the infinitely many graph cases and the supremum over all times.

## Relationship to prior work
Farhi and Gutmann introduced root-initiated continuous-time quantum walks and classical comparisons on decision trees; their graph family and Hamiltonian normalization differ. Exact equitable-subspace reductions are established tools, not claimed as new. Scholes examines excitation localization and adjacency spectral structure on densely connected networks rather than this finite-time Mycielskian layer law. Vieira and Amorim prove occupation suppression for strongly weighted roots on lines and trees; their weighted-root destination problem has a related interference mechanism but does not give the present fixed-degree regular-base family, all-time sharp \(4r^2\) coefficient, or classical comparison. Published related graph-transfer results on hubs likewise do not directly imply these statements. Novelty is claimed only for the combined sharp, uniform-in-time Mycielskian transport law and its separation from a specified classical process, subject to the limitations below.

## Limitations
The result relies on exact base regularity, uniform edge amplitudes, a hub-localized initial excitation and adjacency rather than graph-Laplacian quantum dynamics. It does not hold as stated when \(r\) grows with \(n\), in the presence of disorder, for arbitrary initial states or after environmental dephasing. The analysis supplies an exact asymptotic probability maximum but not a unique maximizing time at finite size. Independent validation and definitive historical priority remain open.

## References
1. E. Farhi and S. Gutmann, *Quantum Computation and Decision Trees*, first publicly submitted 1997-06-27, arXiv:quant-ph/9706062, https://arxiv.org/abs/quant-ph/9706062.
2. G. D. Scholes, *Graphs that predict exciton delocalization*, first publicly submitted 2025-01-16, arXiv:2501.09843, https://arxiv.org/abs/2501.09843.
3. R. Vieira and E. P. M. Amorim, *Control of vertex probability via edge-weight modulation in continuous-time quantum walks*, *Quantum Information Processing* **25**, 92 (2026), https://doi.org/10.1007/s11128-026-05111-6.
4. L. Razzoli, P. Bordone and M. G. A. Paris, *Universality of the fully connected vertex in Laplacian continuous-time quantum walk problems*, arXiv:2202.13824, https://arxiv.org/abs/2202.13824.
