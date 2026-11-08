# Sharp trispectrum sampling for antiperiodic signals on even cycles

## Finding

Let \(N\ge4\) be even, put \(M=N/2\), \(m=\lfloor N/4\rfloor\), and write \(\mathbb Z_N=\mathbb Z/N\mathbb Z\). Let \(\mathcal C_N\) consist of **real** signals \(f:\mathbb Z_N\to\mathbb R\) satisfying
\[
 f(x+M)=-f(x),\qquad \widehat f(k)\ne0\quad\text{for every odd } k\in\mathbb Z_N.
\]
Here the Fourier transform is unnormalized and is zero at every even frequency by antiperiodicity. Suppose the *complete second autocorrelation* (equivalently, the full Fourier power spectrum) is supplied.

**Theorem.** The following \(m\) individually specified fourth-autocorrelation Fourier coefficients
\[
 T_j(f)=\widehat{\rho_4(f)}(2j-1,1,1),\qquad j=1,\ldots,m,
\]
uniquely determine every \(f\in\mathcal C_N\), together with the second autocorrelation, **up to cyclic translation**. This holds for every such signal, not merely generically. No fixed nonadaptive selection of fewer than \(m\) individual Fourier coefficients of \(\rho_4\), even with the full second autocorrelation, can determine all members of \(\mathcal C_N\) up to translation. Thus \(m=\lfloor N/4\rfloor\) is the exact optimal number of individual fourth-order spectral samples. Every odd-order autocorrelation vanishes identically on this class, so third-order data cannot substitute for these samples.

## Assumptions and scope

For \(r\ge1\), define the *unnormalized* autocorrelation by
\[
 \rho_r(f)(t_1,\ldots,t_{r-1})=\sum_{x\in\mathbb Z_N}f(x)\prod_{i=1}^{r-1}f(x+t_i),
\]
with \(\rho_1(f)=\sum_x f(x)\), and define \(\widehat f(k)=\sum_x f(x)e^{-2\pi ikx/N}\). Fourier transforms of autocorrelations are unnormalized transforms over all lag coordinates. The \(m\) measurements are individual **complex** coefficients of the complete fourth-order spectrum; their magnitudes are already implied by the second-order data. The lower bound concerns *fixed, nonadaptive choices of individual fourth-order Fourier coefficients*, not arbitrary linear combinations of them, adaptive queries, or time-domain autocorrelation values. No positivity, integrality, or rationality of the time-domain signal is assumed. The strict nonvanishing at **every** odd frequency is essential.

The class is nonempty: take Fourier coefficients equal to \(1\) at all odd frequencies and \(0\) at all even frequencies, which in time corresponds to \((\delta_0-\delta_M)/2\).

## Proof

**1. Fourier polyspectrum identity and parity obstruction.** Directly exchanging the finite sums over \(x\) and the lags gives, for any \(r\ge2\),
\[
 \widehat{\rho_r(f)}(a_1,\ldots,a_{r-1})
 =\widehat f(a_1)\cdots\widehat f(a_{r-1})\widehat f\!\left(-\sum_{i=1}^{r-1}a_i\right).
\]
In particular, \(\widehat{\rho_2(f)}(k)=|\widehat f(k)|^2\) because \(f\) is real. Since every factor changes sign under \(x\mapsto x+M\), \(\rho_r(f)=0\) whenever \(r\) is odd. The Fourier transform of \(f\) is supported on odd frequencies because \(f(x+M)=-f(x)\).

**2. Constructive uniqueness.** Suppose \(f,g\in\mathcal C_N\) have the same second autocorrelation and the same displayed \(m\) fourth-order coefficients. For every odd frequency define
\[
 h(k)=\frac{\widehat g(k)}{\widehat f(k)}.
\]
All ratios exist and have modulus \(1\); reality implies \(h(-k)=\overline{h(k)}=h(k)^{-1}\). Equality of the measured fourth-order coefficients and the polyspectrum identity yield
\[
 h(2j-1)h(1)^2h(-2j-1)=1
 \quad\Longleftrightarrow\quad h(2j+1)=h(2j-1)h(1)^2,
 \qquad 1\le j\le m.
\]
Putting \(z=h(1)\), induction gives \(h(2j+1)=z^{2j+1}\) for \(0\le j\le m\).

If \(N=4m\), the last recurrence says \(h(2m+1)=z^{2m+1}\). Since \(2m+1\equiv-(2m-1)\pmod N\), reality also gives \(h(2m+1)=z^{-(2m-1)}\); therefore \(z^N=1\). If \(N=4m+2\), the last recurrence says \(h(2m+1)=z^{2m+1}\). Now \(2m+1=M\) is its own negative frequency; reality forces \(h(M)\in\{-1,1\}\), so again \(z^N=1\). Conjugate symmetry then gives \(h(k)=z^k\) at *every* odd frequency modulo \(N\). Since \(z\) is an \(N\)-th root of unity, \(z=e^{-2\pi it/N}\) for some \(t\in\mathbb Z_N\). The Fourier shift identity implies \(g(x)=f(x-t)\) for every \(x\). Conversely all cyclic translations preserve all autocorrelations, proving exact uniqueness modulo translations. This proof also gives an explicit reconstruction algorithm: recover the magnitudes from \(\rho_2\), choose any phase of \(\widehat f(1)\), and use successive \(T_j\) to recover higher odd phases; the terminal relation leaves exactly the finite cyclic translation ambiguity.

**3. Sharp nonadaptive lower bound.** Fix any strictly positive Fourier magnitudes at odd frequencies. When \(N=4m\), the remaining choices for real signals are exactly \(m\) independent unit-circle phases, one for each conjugate pair of odd frequencies. When \(N=4m+2\), fix in addition one of the two signs of the self-conjugate Nyquist coefficient; the remaining connected component is again a torus \((S^1)^m\). All these signals are in \(\mathcal C_N\) and have exactly the same entire second autocorrelation.

At these fixed magnitudes, each individual fourth-order Fourier coefficient is either identically zero or a fixed nonzero complex constant times a **character** of this \(m\)-torus (an integer-exponent phase monomial). Any fixed family of \(s<m\) such coefficients therefore defines a torus homomorphism into \((S^1)^s\) after removing its fixed magnitudes and ignoring zero coefficients. The integer exponent matrix has rank at most \(s<m\), so its kernel contains a positive-dimensional subtorus. Translation acts through at most \(N\) points on this phase torus. Hence distinct nontranslation-equivalent signals produce the same \(s\) measured coefficients and the same second autocorrelation. This holds for every fixed selection of fewer than \(m\) fourth-order spectral entries, proving optimality.

## Verification

A standalone standard-Python script, `CHECK.py`, separately checks the integer phase-exponent matrices for every even \(4\le N\le200\), finding determinant absolute value \(N\) when \(4\mid N\) and \(N/2\) when \(N\equiv2\pmod4\). It exhaustively checks discrete \(N\)-th-root phase configurations for \(N\in\{4,6,8,10,12\}\) and finds exactly the \(N\) cyclic translation solutions in each case. An independent direct time-domain construction computes the full fourth autocorrelation and its Fourier transform for the same five orders to check the polyspectrum identity, complex signs, and Fourier normalization. Run with `python3 CHECK.py`; expected output is `CHECK_OK exact_and_direct_assertions=1011107`. These are supporting finite checks, not a proof for arbitrary \(N\); the universal proof is given above.

## Relationship to prior work

Agulnick and Busick-Warner (2026) study higher autocorrelations of real functions on finite abelian groups, including signals with Fourier zeros. Their index-two subgroup theorem gives general sufficient autocorrelation orders, not the exact optimal count of individually chosen trispectrum Fourier entries for the full odd-frequency coset here. Grünbaum and Moore (1995) work with rational cyclic sequences having a **nonzero constant Fourier coefficient** and give whole-order invariance results and counterexamples; their theorem cannot be specialized to the antiperiodic real class, whose constant Fourier coefficient is zero. They do not establish the exact count or choice of fourth-order individual entries. Casper and Orozco (2025) establish more general reconstruction results for rational-valued gridded data and exhibit even-cycle examples with very sparse Fourier support where fourth order is insufficient; those examples do not satisfy the present full odd-frequency nonvanishing hypothesis. Bendory, Edidin, and Kreymer (2021) study recovery from a few generic *linear measurements* of higher spectra; their setting neither specifies these individual entries nor proves this fixed-sample optimality for a Fourier-zero class. The finite-group phase-ratio method and the polyspectrum product identity are established tools, not claimed as new. The contribution claimed here is the sharp, explicit, nonadaptive \(\lfloor N/4\rfloor\)-entry reconstruction theorem in this structured zero-bispectrum regime.

## Limitations

The theorem requires even cyclic order, real antiperiodic signals, nonvanishing of *every* odd Fourier coefficient, the complete second autocorrelation, and complex fourth-order spectral samples. The lower bound is for fixed nonadaptive *individual entries*, not arbitrary measurement functionals or interactive sampling. It does not address perturbation stability, approximate zeros, partially missing odd frequencies, complex time-domain signals, or rationality constraints. No external independent mathematical audit has been performed. Earlier unindexed descriptions in the literature on separating invariants, higher-order spectra, or phase monomials remain possible.

## References

- F. A. Grünbaum and C. C. Moore, *The Use of Higher-Order Invariants in the Determination of Generalized Patterson Cyclotomic Sets*, Acta Crystallographica A51 (1995), 310–323, DOI:10.1107/S0108767394009827.
- A. Agulnick and T. Busick-Warner, *Higher-Order Autocorrelations on Finite Abelian Groups*, arXiv:2604.13310v1, posted 2026-04-14. https://arxiv.org/abs/2604.13310
- W. R. Casper and B. Orozco, *Reconstructing Gridded Data from Higher Autocorrelations*, arXiv:2503.21022v1, posted 2025-03-26. https://arxiv.org/abs/2503.21022
- T. Bendory, D. Edidin and S. Kreymer, *Signal recovery from a few linear measurements of its high-order spectra*, arXiv:2103.01551, first posted 2021-03-02. https://arxiv.org/abs/2103.01551
