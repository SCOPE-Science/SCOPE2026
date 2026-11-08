# Poisson quantum-return variance as an inverse-gap spectral sum

## Finding

**Theorem (unbiased-spectrum Poisson first-return law).** Let \(n\ge2\) be finite and let \(H\) be a Hermitian Hamiltonian with pairwise distinct real energies \(E_1,\ldots,E_n\), using units \(\hbar=1\). Prepare and attempt to detect the same normalized state \(|\psi\rangle\) satisfying \(|\langle E_j|\psi\rangle|^2=1/n\) for all \(j\). Between successive ideal rank-one projective detection attempts, evolve unitarily for independent waiting times having exponential density \(r e^{-rt}\), with \(r>0\). Stop at the first successful detection and let \(N\ge1\) count **attempts**, not elapsed time. Then detection occurs almost surely, both moments are finite, and

\[
\mathbb E N=n,\qquad
\operatorname{Var}N=n(n-1)+\frac{8r^2}{n}\sum_{1\le j<k\le n}\frac{1}{(E_j-E_k)^2}.
\]

Thus the excess over \(n(n-1)\) is exactly an inverse-square spectral-gap statistic for every finite simple spectrum and every positive Poisson measurement rate.

**Chiral triangle corollary.** Let \(J>0\) and \(H_\alpha=-J(e^{i\alpha}T+e^{-i\alpha}T^\dagger)\), where \(T=|0\rangle\langle1|+|1\rangle\langle2|+|2\rangle\langle0|\). Prepare and detect \(|0\rangle\). When \(\sin(3\alpha)\ne0\),

\[
\mathbb E N=3,\qquad \operatorname{Var}N=6+\frac{2r^2}{J^2\sin^2(3\alpha)}.
\]

At the exceptional fluxes \(\alpha\in(\pi/3)\mathbb Z\), the **exact** statistics instead obey

\[
\mathbb E N=2,\qquad \operatorname{Var}N=\frac52+\frac{r^2}{2J^2}.
\]

Consequently, away from exceptional fluxes the variance has global minima \(6+2(r/J)^2\) precisely at \(\alpha=\pi/6+k\pi/3\), and it diverges as \(2r^2/[9J^2(\alpha-k\pi/3)^2]\) when a nonexceptional flux approaches \(k\pi/3\), even though its value **at** the degeneracy is finite. All these statements concern the first-success **attempt number**.

## Assumptions and scope

The result assumes a closed finite-dimensional Hamiltonian between measurements, independent exponential waits of fixed rate, ideal instantaneous yes/no projection onto the prepared pure state, and nondegenerate energies in the general theorem. The unbiased-spectrum condition is exactly \(|\langle E_j|\psi\rangle|^2=1/n\). Phases of eigenvectors can be chosen so that \(|\psi\rangle=n^{-1/2}\sum_j|E_j\rangle\). The triangle has this spectral weight at each nondegenerate flux. At the exceptional triangle fluxes, two energies coincide and the effective bright subspace is two-dimensional, so the general theorem is not applied there; a separate two-level calculation gives the stated values.

## Proof

Write \(P=|\psi\rangle\langle\psi|\) and \(Q=I-P\). In the energy basis choose phases so that \(P=\mathbf1\mathbf1^\top/n\) and \(Q=I-\mathbf1\mathbf1^\top/n\). The averaged unitary channel is

\[
\Phi(X)_{jk}=m_{jk}X_{jk},\qquad m_{jk}=\frac{r}{r+i(E_j-E_k)}.
\]

On operators supported on the no-detection subspace define \(\mathcal T(X)=Q\Phi(X)Q\) and \(B=Q\Phi(P)Q\). Because \(\Phi\) is unital,

\[
(I-\mathcal T)Q=B.
\]

The map \(\mathcal T\) has spectral radius strictly below one: any nonzero state supported in \(Q\) has strictly positive averaged next-step detection probability. Indeed, for any nonzero vector \(|u\rangle\) in that subspace, \(\langle\psi|e^{-iHt}|u\rangle\) cannot vanish identically in \(t\), by distinctness of the energies and nonzero overlap of \(|\psi\rangle\) with each eigenvector. Analyticity and the strictly positive waiting density give a positive probability; compactness of the set of unit trace positive operators supported on \(Q\) gives a uniform strict contraction. Thus \(R=(I-\mathcal T)^{-1}\) exists and \(RB=Q\).

The survival probabilities are \(s_0=1\) and \(s_k=\operatorname{Tr}(\mathcal T^{k-1}B)\) for \(k\ge1\). Tail summation yields

\[
\mathbb EN=1+\operatorname{Tr}(RB)=n,\qquad
\mathbb EN^2=n+2\operatorname{Tr}(R^2B).
\]

We explicitly solve the Poisson equation \((I-\mathcal T)Y=Q\), so that \(Y=RQ=R^2B\). Put

\[
s_j=\sum_{k\ne j}\frac1{E_j-E_k},\qquad a_j=-\frac r n s_j,
\]

and for distinct indices define

\[
Y_{jk}=\big[-1+i(a_j-a_k)\big]\left(1-\frac{ir}{E_j-E_k}\right),\qquad
Y_{jj}=-\sum_{k\ne j}Y_{jk}.
\]

Since \(\sum_j s_j=0\) and \(na_j+rs_j=0\), the row sums of imaginary parts vanish; the displayed diagonal entries are real, \(Y\) is Hermitian, and \(Y\mathbf1=0\). Hence \(QYQ=Y\). Entrywise application of \(\Phi\) gives

\[
Y-\Phi(Y)=I-\mathbf1\mathbf1^\top+i(a\mathbf1^\top-\mathbf1a^\top).
\]

Multiplication by \(Q\) on both sides kills the terms containing \(\mathbf1\), giving \(Q(Y-\Phi(Y))Q=Q\), as needed.

The diagonal values sum to

\[
\operatorname{Tr}Y=n(n-1)+\frac{r^2}{n}\sum_{j\ne k}\frac{s_j-s_k}{E_j-E_k}
=n(n-1)+\frac{2r^2}{n}\sum_j s_j^2.
\]

Expanding the squares, cross terms from each unordered triple cancel by the partial-fraction identity

\[
\frac1{(x-y)(x-z)}+\frac1{(y-x)(y-z)}+\frac1{(z-x)(z-y)}=0.
\]

Therefore \(\sum_j s_j^2=2\sum_{j<k}(E_j-E_k)^{-2}\), giving

\[
\operatorname{Tr}Y=n(n-1)+\frac{4r^2}{n}\sum_{j<k}(E_j-E_k)^{-2}.
\]

Finally \(\operatorname{Var}N=2\operatorname{Tr}Y-n(n-1)\), proving the theorem.

For the triangle, its Fourier eigenvectors have constant site weight \(1/3\) and energies \(E_k=-2J\cos(\alpha+2\pi k/3)\), for \(k=0,1,2\). If \(\sin3\alpha\ne0\), the trigonometric identity

\[
\sum_{j<k}(E_j-E_k)^{-2}=\frac3{4J^2\sin^2(3\alpha)}
\]

follows from \(\sum_{k=0}^2\csc^2(\alpha+k\pi/3)=9\csc^2(3\alpha)\). Substitution proves the regular-flux formula, minima and inverse-square singularity.

At \(\alpha\in(\pi/3)\mathbb Z\), there are two distinct energies separated by \(3J\) with target spectral weights \(1/3\) and \(2/3\). The averaged first-failure probability in the accessible two-level space is \(q=2p(1-p)(3J)^2/[r^2+(3J)^2]\) with \(p=1/3\). After a failure the orthogonal state is fixed, and its next success probability is also \(q\). Therefore \(\Pr(N=1)=1-q\), \(\Pr(N=m)=q^2(1-q)^{m-2}\) for \(m\ge2\), yielding \(\mathbb EN=2\) and \(\operatorname{Var}N=2/q-2=5/2+r^2/(2J^2)\).

## Verification

Run `python VERIFY.py` with Python 3, NumPy, SciPy, and SymPy. The script verifies the constructed operator solution exactly for rational spectra of dimensions two through five; independently computes the projected density-matrix survival superoperator and its two resolvent moments for dimensions two through six; compares the triangle at representative nondegenerate fluxes; and tests the independent reduced two-level degenerate-flux calculation. It reports 158 passed checks. These finite tests corroborate but do not replace the all-dimensional analytic proof above.

## Relationship to prior work

Kessler, Barkai and Ziegler (arXiv:2012.01763, first posted 2020-12-03) establish the general random-probing survival-superoperator framework, integer mean return attempt count, and general matrix formula for second moments. Varbanov, Krovi and Brun (arXiv:0803.3446) give an earlier Poisson measurement treatment of continuous quantum-walk hitting times. Yin, Ziegler, Thiel and Barkai (arXiv:1903.03394) classify divergent return fluctuations for **periodic** projective measurements. Wang et al. (arXiv:2402.15843, first posted 2024-02-24) study the same magnetic triangle, but their measurements are **periodic**, including finite-resolution and flux-dependent dark-state phenomena. The present result concerns an exact uniform-in-dimension spectral-gap identity for **independent exponential probe intervals** and its complete magnetic triangle specialization. The established general moment matrices logically permit such specializations, so this finding does not claim a new detection formalism or novelty of integer mean return times. The value lies in the explicit spectral statistic, proof by a closed-form Poisson equation, and singular flux law; undiscovered equivalent formulas remain a priority risk.

## Limitations

The formula is not asserted for non-uniform spectral weights, degenerate general Hamiltonians, non-exponential inter-measurement intervals, imperfect measurements, or elapsed-time variance. The exact degenerate-triangle result comes from a separate reduced-space calculation. At a fixed positive probe rate, the divergence describes approach to—not occupation of—the degeneracy. Mathematical correctness is independently testable using the included code, but no independent scientific audit or priority determination has been performed.

## References

- M. Varbanov, H. Krovi and T. A. Brun, *Hitting time for the continuous quantum walk*, arXiv:0803.3446 (2008), https://arxiv.org/abs/0803.3446.
- R. Yin, K. Ziegler, F. Thiel and E. Barkai, *Large fluctuations of the first detected quantum return time*, arXiv:1903.03394 (2019), https://arxiv.org/abs/1903.03394.
- D. A. Kessler, E. Barkai and K. Ziegler, *The first detection time of a quantum state under random probing*, arXiv:2012.01763 (2020), https://arxiv.org/abs/2012.01763.
- Q. Wang, S. Ren, R. Yin, K. Ziegler, E. Barkai and S. Tornow, *First Hitting Times on a Quantum Computer: Tracking vs. Local Monitoring, Topological Effects, and Dark States*, arXiv:2402.15843 (2024), https://arxiv.org/abs/2402.15843.
