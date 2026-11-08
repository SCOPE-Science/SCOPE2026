# The first antipodal trapping resonance of two-range quantum rings

## Finding
Let \(n\ge6\) be even. A one-excitation quantum walk moves on the cyclic sites \(\mathbb Z/n\mathbb Z\) with positive nearest-neighbor hopping \(J_1\), positive next-nearest-neighbor hopping \(J_2\), and one irreversible absorber at site \(0\) with any positive capture rate \(\gamma\). Its excitation initially occupies the antipodal site \(n/2\).

Write \(\rho=J_2/J_1\). There is a finite, explicitly computable set \(\mathcal R_n\subset(0,\infty)\) of isolated resonant ratios such that eventual survival is positive exactly when \(\rho\in\mathcal R_n\). The first positive resonance is uniquely
\[
\rho_n^*=\frac{1}{4\cos^2(\pi/n)}.
\]
For all \(0<\rho<\rho_n^*\), capture is complete; at the endpoint the exact surviving probability jumps to
\[
\boxed{p_n(\rho_n^*)=\frac{8}{3n}.}
\]
In particular, \(\rho\le1/4\) guarantees complete antipodal capture on **every** even ring, and this family-uniform robust interval is sharp: the first resonances tend down to \(1/4\). More strongly, the union of all exceptional ratios over even \(n\ge6\) is countable and dense in \((1/4,\infty)\), whereas every fixed ring has only finitely many such ratios. The results are independent of the positive capture rate.

The complete finite-ring formula is as follows. Put \(c_k=\cos(2\pi k/n)\) and partition \(\{0,\dots,n-1\}\) into equal-energy classes for
\[
\varepsilon_k=2J_1c_k+2J_2(2c_k^2-1).
\]
If a class has \(e\) even indices and \(o\) odd indices, its contribution to eventual survival is \(4eo/[n(e+o)]\). Therefore
\[
p_n(\rho)=\frac4n\sum_{\text{equal-energy classes }C}\frac{e_Co_C}{e_C+o_C}.
\]
Equivalently the finite exceptional set is
\[
\mathcal R_n=\left\{-\frac{1}{2(c_k+c_l)}:\ 0\le k<l<n,\ k-l\text{ odd},\ c_k\ne c_l,\ c_k+c_l<0\right\}.
\]

## Assumptions and scope
The cyclic shift \(T\lvert x\rangle=\lvert x+1\rangle\) gives the Hermitian hopping operator
\[
H=J_1(T+T^*)+J_2(T^2+(T^*)^2).
\]
For \(J_1,J_2,\gamma>0\), use the effective no-capture Hamiltonian
\[
H_{\mathrm{eff}}=H-\frac{i\gamma}{2}\lvert0\rangle\langle0\rvert.
\]
The unconditional no-capture probability at time \(t\ge0\) is \(\|e^{-itH_{\mathrm{eff}}}\lvert n/2\rangle\|^2\), and \(p_n(\rho)\) is its limit as \(t\to\infty\). This is a single-particle, time-independent, zero-flux, homogeneous two-range model, not a repeatedly measured or dephased walk. All statements quantify over every even integer \(n\ge6\), every \(J_1>0\), every positive \(J_2\), and every \(\gamma>0\).

## Proof
**Loss-free spectral decomposition.** Let \(P_\lambda\) be the orthogonal spectral projection of \(H\) onto energy \(\lambda\). The vectors in \(\operatorname{Ran}P_\lambda\) that vanish at the absorbing site are exactly
\[
\operatorname{Ran}P_\lambda\cap\lvert0\rangle^\perp.
\]
Their direct sum \(\mathcal D\) is invariant under both \(H\) and \(H_{\mathrm{eff}}\); its orthogonal complement is invariant as well. Indeed, the derivative of the norm squared of any effective evolution is \(-\gamma|\langle0\mid\psi(t)\rangle|^2\). An eigenvector having no exponential decay must therefore vanish at the trap and be an \(H\)-eigenvector. No nondecaying Jordan block is possible in a contractive finite-dimensional semigroup. Thus the orthogonal complement of \(\mathcal D\) decays to zero and eventual survival is the squared norm of the projection of the initial state onto \(\mathcal D\), independent of \(\gamma>0\).

**Parity-resolved class formula.** The normalized Fourier modes
\[
\lvert k\rangle=n^{-1/2}\sum_{x=0}^{n-1}e^{2\pi ikx/n}\lvert x\rangle
\]
diagonalize \(H\), with energies \(\varepsilon_k\) stated above. Within a class \(C\) of \(m=e_C+o_C\) equal-energy Fourier modes, the trap has coefficient vector \((1,\ldots,1)/\sqrt n\), while the antipodal source has coefficients \(((-1)^k)_{k\in C}/\sqrt n\). Removing the normalized trap-bright direction leaves squared source norm
\[
\frac1n\left[m-\frac{(e_C-o_C)^2}{m}\right]=\frac{4e_Co_C}{nm}.
\]
Summing over orthogonal classes gives the formula and shows that a class contributes exactly when it contains Fourier indices of opposite parity.

**Exceptional coupling ratios.** For \(k,l\),
\[
\varepsilon_k-\varepsilon_l=2J_1(c_k-c_l)\left[1+2\rho(c_k+c_l)\right].
\]
On an even ring, \(c_k=c_l\) implies \(l\equiv\pm k\pmod n\), so those indices have the same parity. All mixed-parity coincidences therefore occur precisely at the displayed elements of \(\mathcal R_n\); the condition \(c_k+c_l<0\) is equivalent to positive \(\rho\). This also proves finiteness for each \(n\).

**First resonance and its exact mass.** Among the distinct cosine levels the two smallest are \(-1\) (the unique index \(n/2\)) and \(-\cos(2\pi/n)\) (the two indices \(n/2\pm1\)). Their sum is strictly smaller than the sum of any other pair of distinct cosine levels. Consequently the smallest possible positive resonant \(\rho\) is
\[
\frac{1}{2[1+\cos(2\pi/n)]}=\frac{1}{4\cos^2(\pi/n)}.
\]
At that coupling this is the sole cross-cosine coincidence: one Fourier index has the parity opposite to the other two, yielding \(e_Co_C=2\) and \(e_C+o_C=3\). All other classes are parity-pure. Hence survival is exactly \(8/(3n)\). Since \(\rho_n^*\downarrow1/4\) as \(n\to\infty\), the size-uniform positive-coupling interval \(0<\rho\le1/4\) contains no resonance and cannot be extended to a larger entire interval.

**Density beyond the sharp boundary.** Fix any \(\rho_0>1/4\). There is \(\theta\in(0,\pi)\) such that \(\cos\theta=1-1/(2\rho_0)\). For a sequence of increasing even \(n\), choose \(l\in\{1,\dots,n/2-1\}\) of parity opposite to \(n/2\) and with \(2\pi l/n\to\theta\). Then the pair of Fourier levels indexed by \(n/2\) and \(l\) has distinct cosines and opposite parities, and its positive resonance
\[
\rho_n=\frac{1}{2[1-\cos(2\pi l/n)]}\to\rho_0.
\]
Each \(\rho_n\in\mathcal R_n\), establishing density. Since each \(\mathcal R_n\) is finite, their union is countable, hence Lebesgue-null.

## Verification
The accompanying `check_resonances.py` independently constructs the real-space cyclic hopping matrix, diagonalizes it, and removes the detector-bright direction in each eigenspace. It compares those results to direct Fourier class enumeration for even \(n\) from \(6\) through \(50\) and several detuned couplings: 115 checks passed. At each first resonance it confirms \(8/(3n)\), including \(4/9\) at \(n=6\), \(1/3\) at \(n=8\), and \(2/9\) at \(n=12\).

The separate `check_decay.py` directly exponentiates the non-Hermitian time evolution, testing four sizes, three different capture rates, and off-resonance detunings: 20 checks passed. Both scripts require only Python, NumPy, and (for direct evolution) SciPy. Neither finite calculation substitutes for the all-size proof above.

## Relationship to prior work
Xu and Liu (2008, arXiv:0801.4180) analyze untrapped rings with additional neighbor connections and Bloch spectra. More closely, Xu (2008, arXiv:0812.3452) studies irreversible trapping on long-range interacting cycles, including range-two edges, but fixes all edge hopping strengths equal and studies numerical survival averaged over initial sites and several randomly placed absorbers; that work does not determine the tunable first two-range single-sink resonance or the exact antipodal survival jump. Agliari, Mülken, and Blumen (2009, arXiv:0903.3288) study quantum ring trapping and trap arrangements, but work with nearest-neighbor ring motion. Krapivsky, Luck, and Mallick (2013, arXiv:1311.6298) establish complete absorption from the antipode of a single nearest-neighbor ring trap; their Section 4.2 is the closest published baseline for the localized-source conclusion. Bhandari and Durganandini (2021, arXiv:2101.11240) analyze two-range coherent hopping and identify a \(1/4\) coupling threshold in *untrapped infinite-chain wavefront dynamics*. That known threshold is not claimed to be discovered anew; neither their wavefront result nor the cited nearest-neighbor trapping result establishes the discrete finite-ring resonant capture formula or its exact jump \(8/(3n)\). Varbanov, Krovi, and Brun (2008, arXiv:0803.3446) study a general Poisson-measurement hitting model, but do not derive this continuous-loss, two-range ring classification.

## Limitations
The conclusions concern **infinite-time** capture. They do not imply robust finite-time protection: arbitrarily small detuning from a resonance restores eventual complete capture, and the associated absorption time may grow large near a resonance. Site disorder, nonuniform bonds, magnetic flux, dephasing, interacting particles, extra absorbers, and finite capture time scales are outside the claim. The novelty assessment is conditional on the literature and record comparisons undertaken; it is not an independent priority certification. The result uses standard Fourier spectral analysis and the established general loss-free subspace principle.

## References
- X. Xu and F. Liu, *Continuous-time quantum walks on one-dimension regular networks*, first public 2008-01-28, https://arxiv.org/abs/0801.4180.
- X.-P. Xu, *Coherent exciton transport and trapping on long-range interacting cycles*, first public 2008-12-18, https://arxiv.org/abs/0812.3452.
- M. Varbanov, H. Krovi, and T. A. Brun, *Hitting time for the continuous quantum walk*, first public 2008-03-24, https://arxiv.org/abs/0803.3446.
- E. Agliari, O. Mülken, and A. Blumen, *Continuous-Time Quantum Walks and Trapping*, first public 2009-03-19, https://arxiv.org/abs/0903.3288.
- P. L. Krapivsky, J. M. Luck, and K. Mallick, *Survival of classical and quantum particles in the presence of traps*, first public 2013-11-25, https://arxiv.org/abs/1311.6298.
- H. Bhandari and P. Durganandini, *Long time dynamics of a single particle extended quantum walk on a one dimensional lattice with complex hoppings: a generalized hydrodynamic description*, first public 2021-01-27, https://arxiv.org/abs/2101.11240.
