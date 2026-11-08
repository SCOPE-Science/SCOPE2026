# Exact operator-lifting spectrum and maximal information for cyclic quadratic-chirp masks

## Finding
For every integer \(n\ge 2\), put \(\omega=\exp(2\pi i/n)\). For every nonempty set \(S\subseteq\mathbb Z_n\) of \(r\) distinct slopes, consider the \(rn\) unit vectors
\[
 v_{s,k}(j)=n^{-1/2}\omega^{s j^2+k j},\qquad j,k\in\mathbb Z_n,\ s\in S,
\]
and the matrix-intensity lifting
\[
 \mathcal M_S(X)=\bigl(v_{s,k}^{*}Xv_{s,k}\bigr)_{s\in S,\ k\in\mathbb Z_n}.
\]
Equip matrices with the Hilbert--Schmidt norm and measurement arrays with the unweighted Euclidean norm. Let \(g=\gcd(n,2)\) and \(h=n/g\). For every divisor \(m\mid h\) and residue \(c\in\mathbb Z_m\), define the occupancy \(a_m(c)=|\{s\in S:s\equiv c\pmod m\}|\).

**Exact singular-spectrum theorem.** The strictly positive singular values of \(\mathcal M_S\), including multiplicities, are
\[
 \boxed{\sqrt{a_m(c)}\quad\text{with multiplicity }g\varphi(m)
 \quad(m\mid h,\ c\in\mathbb Z_m,\ a_m(c)>0).}
\]
Here the multiplicities are additive when values from different pairs \((m,c)\) coincide. In particular,
\[
 \boxed{\operatorname{rank}\mathcal M_S
 =g\sum_{m\mid h}\varphi(m)\,|S\bmod m|.}
\]
The same nonzero singular spectrum holds for the real-linear restriction from Hermitian matrices to real measurements, using the corresponding real Hilbert--Schmidt norm.

**Explicit kernel.** For each cyclic lag \(d\in\mathbb Z_n\), and each frequency \(\ell\in\mathbb Z_n\) outside \(\{-2ds\pmod n:s\in S\}\), let \(E_{d,\ell}\) have entries \(E_{d,\ell}(a,a+d)=n^{-1/2}\omega^{\ell a}\) and zero elsewhere. These matrices form an orthonormal complex basis of \(\ker\mathcal M_S\). Their Hermitian parts \((E_{d,\ell}+E_{d,\ell}^{*})/2\) and \(i(E_{d,\ell}-E_{d,\ell}^{*})/2\) span the corresponding real Hermitian nullspace. In particular, no unobserved matrix direction is concealed by the rank count.

**Sharp maximal identifiable dimension.** For every \(1\le r\le n\),
\[
 \boxed{\max_{|S|=r}\operatorname{rank}\mathcal M_S
 =g\sum_{m\mid h}\varphi(m)\min(r,m).}
\]
Every \(r\)-element consecutive cyclic block of slopes is optimal. An arbitrary slope set is optimal **if and only if**
\[
 |S\bmod m|=\min(r,m)\qquad\text{for every }m\mid h.
\]
Thus \(h\) masks are necessary and sufficient to attain the maximal rank obtainable by this entire deterministic quadratic-mask family. When \(n=2h\) is even and \(r=h+t\) with \(0\le t\le h\), exactly
\[
 \boxed{\binom ht2^{h-t}}
\]
sets of \(r\) distinct slopes attain this saturated maximum: they contain both representatives of exactly \(t\) of the pairs \(\{c,c+h\}\), and one representative from each other pair.

**Tomographic obstruction.** Even if every quadratic slope is used and all \(n\) coordinate-basis intensity measurements are added, the lifted measurement is injective on all Hermitian matrices **if and only if** \(n\) is an odd prime. Its exact rank is
\[
 \boxed{n-1+g\sum_{m\mid h}m\varphi(m)},
\]
and its Hermitian nullity is \(n^2-n+1-g\sum_{m\mid h}m\varphi(m)\). The injectivity criterion concerns *linear recovery of arbitrary Hermitian matrices*, not injectivity restricted to rank-one matrices or nonlinear phase retrieval.

## Assumptions and scope
The index set is the ring \(\mathbb Z_n\), not a finite field when \(n\) is a prime power. Slopes are distinct modulo \(n\), all \(n\) Fourier modulation indices are measured for each slope, and each vector has Euclidean norm one. Slopes are not weighted; the map uses raw, not probability-normalized, measurements. The symbol \(\varphi\) is Euler's totient, with \(\varphi(1)=1\). The source code `CHECK.py` uses this identical normalization. All claims hold for both odd and even \(n\), including \(n=2\) and \(r=n\).

## Proof
**1. Fourier separation of matrix diagonals.** Write \(X_{a,b}\) for the matrix entries with indices in \(\mathbb Z_n\). Expanding a measurement gives
\[
 v_{s,k}^*Xv_{s,k}
 =\frac1n\sum_{d\in\mathbb Z_n}\omega^{s d^2+kd}
 \sum_{a\in\mathbb Z_n}X_{a,a+d}\omega^{2sda}.
\]
Apply the unitary inverse Fourier transform across the \(k\)-index within each slope. The Fourier coefficient indexed by \(d\) is
\[
 \widetilde{\mathcal M_S(X)}_{s,d}
 =n^{-1/2}\omega^{s d^2}
 \sum_{a\in\mathbb Z_n}X_{a,a+d}\omega^{2sda}.
\]
Distinct values of \(d\) act on orthogonal cyclic diagonals of \(X\), and their outputs are orthogonal Fourier coordinates. This is an exact unitary block decomposition, so the singular spectrum is the union of the singular spectra of these \(d\)-blocks.

**2. Orthogonal rows and collisions.** Every row in the \(d\)-block has Euclidean norm one. The rows for slopes \(s,t\) are orthogonal precisely when \(2d(s-t)\not\equiv0\pmod n\), by the geometric-sum identity. Otherwise the two rows coincide up to a scalar of modulus one. Writing \(m_d=n/\gcd(n,2d)\), the collision criterion is exactly \(s\equiv t\pmod{m_d}\). Consequently, for each residue \(c\) occupied modulo \(m_d\), the block has one nonzero singular value \(\sqrt{a_{m_d}(c)}\), with all other singular values zero. This establishes the complete spectrum for each individual lag, including its kernel multiplicity. Specifically, the row pairing with \(n^{-1/2}\omega^{\ell a}\) vanishes for all slopes precisely when \(\ell\not\equiv -2ds\pmod n\) for every \(s\in S\). Since these Fourier characters form a basis on each lag, the explicit kernel vectors in the finding are complete.

**3. Grouping cyclic lags by arithmetic order.** Multiplication by two maps \(\mathbb Z_n\) onto its even-multiple subgroup, of order \(h=n/\gcd(n,2)\); every element has exactly \(g=\gcd(n,2)\) preimages. The integer \(m_d\) is the additive order of \(2d\) in \(\mathbb Z_n\). This subgroup has \(\varphi(m)\) elements of each exact order \(m\mid h\). Therefore \(m_d=m\) occurs precisely \(g\varphi(m)\) times. Summing the lag spectra proves the singular-value and rank formulas.

**4. Real Hermitian normalization.** Every measurement matrix \(v_{s,k}v_{s,k}^*\) is Hermitian. In a real orthonormal basis of Hermitian matrices, its lifted coefficient matrix is real. Complexifying that real linear map identifies the domain with all complex matrices and gives exactly the complex-linear map above. Thus the real and complex maps have identical nonzero singular values and the rank equals the real dimension of the identifiable Hermitian subspace.

**5. Maximum rank and optimizer classification.** For each \(m\mid h\), a set of \(r\) slopes occupies at most \(\min(r,m)\) residue classes modulo \(m\). A consecutive block of \(r\) slopes occupies exactly \(\min(r,m)\) classes for every modulus simultaneously. As every coefficient \(g\varphi(m)\) is strictly positive, equality in the sum holds exactly when every modular occupancy bound is saturated. Since \(h\mid h\) and \(\varphi(h)>0\), saturation of all information requires at least \(r=h\), and consecutive blocks show sufficiency. When \(n=2h\), saturation for \(r\ge h\) is equivalent to meeting each antipodal slope pair, and the stated counting formula follows by choosing the \(t=r-h\) doubled pairs and one of two representatives from each remaining pair.

**6. Adding coordinate intensities.** The coordinate-basis projectors span all diagonal matrices, a space of dimension \(n\). The original chirp projectors intersect that space in precisely the scalar identity direction, since their \(d=0\) Fourier block has rank one. The coordinate measurements therefore contribute \(n-1\) new dimensions. With all available distinct slopes, each residue modulo every divisor \(m\mid h\) occurs, so the chirp rank is \(g\sum_{m\mid h}m\varphi(m)\). Every matrix lag \(d\ne0\) is completely determined exactly when \(m_d=n\), because all distinct rows in that block can then span its \(n\)-dimensional diagonal. This holds for all nonzero \(d\) exactly when \(\gcd(n,2d)=1\) for all \(d\ne0\), namely when \(n\) is an odd prime. For any other \(n\), a nonzero lag with \(\gcd(n,2d)>1\) leaves an explicit unmeasured subspace. The nullity formula follows by subtraction from \(n^2\).

## Verification
Running `python CHECK.py` with the `numpy` dependency from `requirements.txt` directly builds all the \(rn\) projector rows and compares their singular values with the arithmetic formula for both parities, dimensions \(2\) through \(16\), and a range of slope subsets. Additional exhaustive exact-integer checks cover all nonempty slope subsets through dimension \(10\), coordinate-basis augmentation through dimension \(13\), parity-saturation optimizer counts through even dimension \(12\), and modular occupancy identities through dimension \(30\). A separate independently constructed real orthonormal Hermitian basis is checked through dimension \(9\). The expected output is `QUADRATIC_CHIRP_PROJECTOR_SPECTRUM_CHECKS_PASSED 11651`. The numerical singular-value tolerance is \(2\cdot10^{-10}\); the infinite theorem is proved by the character-orthogonality argument, not by finite enumeration.

For illustration, with \(n=9\), using all slopes gives chirp rank \(61\); adding coordinate data gives rank \(69\) of the \(81\) real Hermitian degrees of freedom. For \(n=6\), only \(h=3\) distinct quadratic-mask bases are available up to modulation relabeling: the chirp rank saturates at \(14\) from three masks, and adding coordinate intensities gives rank \(19\) of \(36\).

## Relationship to prior work
Casazza and Fickus (2006) analyze finite quadratic-chirp Fourier transforms and their pairwise frame overlaps, including composite cyclic groups. Their Gauss sums are consistent with the row-orthogonality mechanism, but their stated results do not give an all-subset *projector-lifting singular-value distribution*, maximal linear recovery rank, or parity-dependent saturation/counting theorem. A directly relevant published research record, *Optimal fourth-overlap energy for arbitrary unions of finite quadratic-chirp bases* (2026), analyzes exactly the same vectors for odd cycle lengths, deriving a sharp **fourth-overlap potential** and its modular balancing condition. That previously established potential result is **not claimed as new here**: it measures a different spectral moment, and does not supply the entire singular spectrum, rank of the lifted measurement for arbitrary subsets, or the even-dimension rank and saturation laws. The present result also contrasts with Huang and Li's 2026 randomized coded-diffraction recovery guarantees, which address rank-one phase retrieval and random masks rather than the full deterministic Hermitian lifting spectrum. McNulty and Weigert (first submitted in 2024) review MUB tomography and the prime-dimension complete-basis phenomenon but not the stated all-subset arithmetic spectral law. The known odd-prime completion criterion is recovered as a consistency check, not asserted as a new isolated theorem.

## Limitations
The deterministic family \(\omega^{s j^2}\) is much smaller than all possible complex masks; rank deficiency here does not imply a lower bound on the number of masks required by other methods. Noninjectivity on arbitrary Hermitian matrices does **not** automatically imply failure of nonlinear phase retrieval for rank-one matrices. Spectral nonzero singular values quantify linear inversion on the identifiable operator subspace; they do not by themselves give sharp noise bounds for rank-one recovery algorithms. Related earlier projector-span calculations in quantum tomography may exist under different terminology; independent priority verification remains outstanding.

## References
1. G. Huang and S. Li, *PhaseLift for Coded Diffraction Patterns: Optimal Sampling Rate*, arXiv:2608.02450, first submitted 2026-08-03. https://arxiv.org/abs/2608.02450
2. P. G. Casazza and M. Fickus, *Fourier Transforms of Finite Chirps*, EURASIP Journal on Applied Signal Processing (2006), article 70204, DOI 10.1155/ASP/2006/70204. https://doi.org/10.1155/ASP/2006/70204
3. *Optimal fourth-overlap energy for arbitrary unions of finite quadratic-chirp bases* (2026), published mathematical record. https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-optimal-fourth-overlap-energy-for-arbitrary-unions-of-finite-qua--76e32f8a77b8/RESULT.md
4. D. McNulty and S. Weigert, *Mutually Unbiased Bases in Composite Dimensions -- A Review*, arXiv:2410.23997, first submitted 2024-10-31. https://arxiv.org/abs/2410.23997
