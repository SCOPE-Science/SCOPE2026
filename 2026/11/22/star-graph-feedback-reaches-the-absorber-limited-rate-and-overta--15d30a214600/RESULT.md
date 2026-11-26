# Star-graph feedback reaches the absorber-limited rate and overtakes a ring at seven qubits

## Finding
For frustration-free singlet-measurement feedback on \(n\ge3\) qubits whose measured edges form the star \(K_{1,n-1}\), with one independent unit-rate Poisson measurement clock per edge and uniform feedback strength \(0<\lambda\le1\), the exact smallest *pair-sector* decay rate is
\[
\Lambda_\star(n,\lambda)=\frac12\left(\lambda+\frac n2-\sqrt{\left(\lambda+\frac n2\right)^2-4\lambda}\right).
\]
For fixed \(\lambda\), it is asymptotically \(2\lambda/n\). Thus the star asymptotically saturates the absorber-fraction bound for connected \(n\)-vertex trees with uniform unit-rate measurement and feedback on every edge, without additional transport operations. In general the uniform-strength bound is \(\lambda|\mathcal F|/\binom n2\), where \(\mathcal F\) is the set of feedback edges under unit edge clocks; \(2\lambda/n\) is its value at \(|\mathcal F|=n-1\), not a bound for arbitrary feedback graphs.

At maximal feedback \(\lambda=1\), compare with the periodic nearest-neighbor ring on the same \(n\) qubits, measured at rate one on each of its \(n\) edges, whose previously established pair-sector rate is \(\Lambda_\circ(n)=2[1-\cos(\pi/n)]\). The star is slower for \(3\le n\le5\), ties **exactly** at \(n=6\), and is faster for every \(n\ge7\), despite possessing one fewer measurement edge. For large \(n\), the ratio \(\Lambda_\star/\Lambda_\circ\) is asymptotic to \(2n/\pi^2\).

For completeness, the entire star pair-sector spectrum is also explicit. Let \(m=n-1\), \(a=\lambda+(m-1)/2\), and \(d_0=\sqrt{(a-1)^2+2(m-1)}\). For \(m\ge3\), there are two simple eigenvalues \((a+1\pm d_0)/2\), two eigenvalues \((a+1\pm d_1)/2\) each of multiplicity \(m-1\), where \(d_1=\sqrt{(a-1)^2+m-2}\), and eigenvalue \(1\) of multiplicity \(m(m-3)/2\). If \(m=2\), the eigenvalues are \((a+1\pm d_0)/2\) and \(a\). The case \(n=2\) has sole pair-sector eigenvalue \(\lambda\).

## Assumptions and scope
Let \(P_{ij}=(I-S_{ij})/2\), where \(S_{ij}\) exchanges two spin-one-half sites. Each monitored edge undergoes independent Poisson measurements at unit rate. Use the standard SWAP measurement-feedback protocol of [1]: the triplet outcome is left uncorrected and a detected singlet is followed by the single-site Pauli rotation (e.g., \(U=\exp(i\phi Z)\) on one endpoint) with removal strength \(\lambda=\sin^2\phi\). The monitored and corrected star edges are precisely \((0,j)\), \(1\le j\le n-1\). There are no extra scrambling operations, measurement-rate constraints per vertex, or physical errors. Time is measured in inverse edge measurement rates.

The *pair-sector* is the exact invariant operator space spanned by the \(P_{ij}\); its decay matrix \(K\) acts on \(\binom n2\) pairs. The proof determines that sector's spectrum and the rate controlling pair-witness relaxation. For the connected SWAP feedback model of [1] with an active feedback bond, the equality of its smallest pair decay rate and the full Liouvillian gap is an existing theorem ([1], v2, Sec. IV I, Eq. (78)); it applies to the star and ring in this protocol. This does not identify the remaining full Liouvillian spectrum or the state-dependent preparation times.

## Proof
**1. Pair transport and absorption.** The singlet-projector closure of [1] gives \(K=-\Delta_{\mathrm{pair}}/2+\lambda\operatorname{diag}(1_{\mathcal F})\): each endpoint of an unordered pair moves along a monitored edge at rate \(1/2\) unless that move would make the endpoints coincide; a pair coinciding with a feedback edge is absorbed at rate \(\lambda\). In the adjoint channel the two projective outcomes without feedback give \((O+S_{ij}OS_{ij})/2\). The single-site rotation on the singlet outcome changes the same-edge projector contribution by \(-\lambda P_{ij}\). It gives no change to a pair projector sharing only one measured endpoint, since the compression of any traceless single-site Pauli operator to the singlet is zero; disjoint pair projectors commute with the channel on the measured edge. The finite-site Kraus computation is also checked in `check.py`.

On the star, denote \(A_i=\{0,i\}\) and \(B_{ij}=\{i,j\}\) for distinct leaves \(1\le i<j\le m\). The only pair-graph edges are \(A_i\leftrightarrow B_{ij}\) and \(A_j\leftrightarrow B_{ij}\), each with rate \(1/2\). Each \(A_i\) has \(m-1\) neighbors and killing rate \(\lambda\); each \(B_{ij}\) has two neighbors and no killing. With \(C\) the unsigned vertex-edge incidence matrix of the complete graph on \(m\) leaves, the exact symmetric pair decay matrix is
\[
 K=\begin{pmatrix}
 a I_m & -C/2\\
 -C^{\mathsf T}/2 & I_{\binom m2}
 \end{pmatrix},\qquad a=\lambda+\frac{m-1}{2}.
\]

**2. Spectrum and lowest mode.** For \(m\ge3\), \(CC^{\mathsf T}=(m-2)I_m+\mathbf1\mathbf1^{\mathsf T}\); its singular values squared are \(2(m-1)\) on constants and \(m-2\) on the \((m-1)\)-dimensional mean-zero leaf subspace. The singular-value decomposition turns \(K\) into one two-by-two block for the constant sector, \(m-1\) two-by-two blocks for the mean-zero sector, and an identity on \(\ker C\), of dimension \(\binom m2-m=m(m-3)/2\). These blocks give the asserted complete spectrum. For \(m=2\), the mean-zero leaf vector decouples with eigenvalue \(a\). All off-diagonal entries of \(K\) are nonpositive and the pair graph is connected, so Perron–Frobenius for a shifted matrix makes the smallest eigenvector unique and strictly positive. Leaf permutations fix it, so it must lie in the constant sector.

That constant block has trace \(\lambda+(m+1)/2=\lambda+n/2\) and determinant \(\lambda\), giving the displayed \(\Lambda_\star\). Rationalizing the small root yields \(\Lambda_\star=2\lambda/[S+\sqrt{S^2-4\lambda}]\), with \(S=\lambda+n/2\). Thus \(n\Lambda_\star\to2\lambda\). The Rayleigh quotient on the all-ones vector gives \(\Lambda_\star\le\lambda m/\binom n2=2\lambda/n\) and the ratio tends to one. At finite \(n\ge3\) the inequality is strict because \(K\mathbf1\) vanishes on leaf pairs but not on hub–leaf pairs: \(\mathbf1\) is not a lowest eigenvector. This proves that the star is asymptotically absorber-limited under the stated clock normalization.

**3. Exact star-versus-ring crossover.** At \(\lambda=1\) the ring rate from [1, Eq. (39)] is \(z_n=2(1-\cos(\pi/n))\). In the same clock convention, the positive ring pair mode is \(f(s)=\sin(\pi s/n)\) on oriented separations \(1\le s\le n-1\); it is symmetric under \(s\mapsto n-s\), so it defines a function on unordered pairs. Here \(Kf=2f(s)-f(s-1)-f(s+1)\), with \(f(0)=f(n)=0\): at a boundary separation the allowed moves total rate one and feedback adds rate one. This verifies the benchmark normalization independently of the star formula.

The star's small eigenvalue is the smaller root of \(p_n(z)=z^2-(n+2)z/2+1\). Because \(z_n\le1\) for \(n\ge3\) and the larger root of \(p_n\) is at least \(2\), the sign of \(p_n(z_n)\) determines whether \(z_n\) falls below or above the star rate. With \(d_n=1-\cos(\pi/n)\),
\[
 p_n(z_n)=1-(n+2)d_n+4d_n^2.
\]
For \(n=3,4,5,6\), this equals, respectively, \(-1/2\), \(1-\sqrt2\), \((\sqrt5-3)/4\), and \(0\). For every \(n\ge7\), \(d_n\le\pi^2/(2n^2)\) and \((n+2)\pi^2/(2n^2)<1\), so \(p_n(z_n)>0\). Consequently the star rate is below the ring rate for \(n=3,4,5\), equal for \(n=6\), and above for all \(n\ge7\). Their large-\(n\) expansions are \(\Lambda_\star\sim2/n\) and \(\Lambda_\circ\sim\pi^2/n^2\), completing the claim.

## Verification
Install `requirements.txt` and run `python check.py`. The checker constructs the star pair generator directly from its edge moves, diagonalizes it for \(2\le n\le16\) at three distinct feedback strengths, compares every eigenvalue with the closed forms, checks the ring crossover for \(3\le n\le100\), and checks the asymptotic normalization. It also constructs the quantum Kraus adjoint channel and singlet-projector operators for \(n=3,4,5\), verifying operator closure numerically against the pair generator. The supplied computation reports 146 passing finite spectrum/comparison checks and passing direct Kraus checks. The all-size claims follow from the analytic argument, not the finite numerical checks.

## Relationship to prior work
Dörstel, Lang, Iadecola, Wilson and Buchhold [1] establish the exact pair-projector closure for connected monitoring graphs, the absorber-fraction bound, the exact rate on a periodic nearest-neighbor chain, and in v2 the equality with the full Liouvillian gap in their model. Dörstel, Iadecola, Wilson and Buchhold [2] introduced the underlying transport and feedback mapping. The contribution here is the explicit star incidence-block spectrum, its asymptotic saturation of the tree bound at fixed unit edge clocks, and the exact six-to-seven-qubit crossover with the ring, not the general closure, Liouvillian-gap identity, or known ring rate.

## Limitations
The star's hub has \(n-1\) independent incident clocks and hence an aggregate incident measurement rate that grows linearly with \(n\); it is not a bounded-degree or constant-per-site-hardware protocol. If instead every site's total incident rate is constrained by the same ceiling, scaling all star edge clocks by \(1/(n-1)\) makes its pair rate asymptotic to \(2\lambda/n^2\); scaling each ring clock by \(1/2\) gives the ring rate asymptotic to \(\pi^2/(2n^2)\) at maximal feedback. Thus at equal bounded maximal incident rates, the ring is faster asymptotically; the star advantage is specific to equal per-edge clocks. No claims are made about quantum-device noise, parallel circuit depth, full many-body preparation time, or general tree optimality at each finite size. Other derivations of the star-specific spectrum might exist outside the inspected literature.

## References
1. T. Dörstel, T. C. Lang, T. Iadecola, J. H. Wilson, and M. Buchhold, *Frustration-free control for quantum-state preparation: an exact first-passage theory*, [arXiv:2611.13094v2](https://arxiv.org/abs/2611.13094v2).
2. T. Dörstel, T. Iadecola, J. H. Wilson, and M. Buchhold, *Frustration-Free Control and Absorbing-State Transport in Entangled State Preparation*, arXiv:2510.24845 (first publicly submitted 2025-10-28); *Physical Review Letters* **136**, 120603 (2026), https://arxiv.org/abs/2510.24845.
