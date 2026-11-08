# Exact Calkin power law for periodically modulated Rhaly operators

## Finding

Let \(q\ge2\) and let \(c=(c_n)_{n\ge1}\) be a nonzero, complex, \(q\)-periodic sequence. Write
\[
 m=\frac1q\sum_{r=1}^q c_r,\qquad
 \mu=\frac1q\sum_{r=1}^q|c_r|^2>0.
\]
On complex \(\ell^2(\mathbb N)\), let the Cesàro and Rhaly operators be
\[
 (Cx)_n=\frac1n\sum_{k=1}^n x_k,\qquad
 (R_cx)_n=\frac{c_n}{n}\sum_{k=1}^n x_k.
\]
Then, for every integer \(p\ge1\),
\[
 \boxed{\ \|R_c^p\|_{\mathrm{ess}}=2^p\sqrt\mu\,|m|^{p-1}\ },
\]
where the factor \(|m|^0\) at \(p=1\) means \(1\), even if \(m=0\). In particular, the essential spectral radius is
\[
 \boxed{\ r_{\mathrm{ess}}(R_c)=2|m|\ }.
\]
If the periodic mean vanishes, \(m=0\), then \(R_c\) is noncompact while \(R_c^2\) is Hilbert–Schmidt. Thus its image in the Calkin algebra is a **nonzero square-zero element**, its Fredholm essential spectrum equals \(\{0\}\), and its Calkin numerical radius is exactly \(\sqrt\mu\).

The constructive ideal statement behind the power law is that, for every integer \(p\ge2\),
\[
 R_c^p-m^{p-1}D_c C^p\in\mathcal S_2,
 \qquad D_c=\operatorname{diag}(c_1,c_2,\ldots).
\]
Consequently the alternating coefficient choice \(c_n=(-1)^n\) has \(\|R_c\|_{\mathrm{ess}}=2\), \(R_c^2\in\mathcal S_2\), \(\sigma_{\mathrm{ess}}(R_c)=\{0\}\), and \(R_c^*R_c=C^*C\) **exactly**. This exhibits operators with identical positive Gram operators but sharply different essential spectral radii.

## Assumptions and scope

All operators are bounded operators on complex \(\ell^2(\mathbb N)\), with indices starting at \(1\). The coefficient sequence is bounded by periodicity. The symbol \(\mathcal S_2\) denotes the Hilbert–Schmidt ideal; \(\pi\) is the canonical quotient map onto the Calkin \(C^*\)-algebra \(\mathcal B(\ell^2)/\mathcal K(\ell^2)\). The essential norm is \(\|T\|_{\mathrm{ess}}=\|\pi(T)\|\); the Fredholm essential spectrum is \(\sigma(\pi(T))\); and the essential spectral radius is \(r(\pi(T))\). The Calkin numerical radius means the numerical radius defined using states of this quotient \(C^*\)-algebra.

The result includes complex, signed and zero-valued periodic coefficients; no positivity or invertibility of \(D_c\) is required. It does not assert a formula for the entire essential spectrum when \(m\ne0\).

## Proof

**Step 1: Periodic cancellation.** If \(d\) is a complex \(q\)-periodic sequence with mean zero, every consecutive partial sum of \(d\) has absolute value bounded by \(q\max_r|d_r|\). Summation by parts, applied to the decreasing sequences \(j^{-1}\) and \(j^{-2}\), gives constants \(B_d<\infty\) such that for integers \(n\ge k\ge1\) and \(M\ge1\),
\[
 \left|\sum_{j=k}^n\frac{d_j}{j}\right|\le\frac{B_d}{k},\qquad
 \left|\sum_{j=M}^{\infty}\frac{d_j}{j^2}\right|\le\frac{B_d}{M^2}.
\]
These estimates are valid for arbitrary complex coefficients.

**Step 2: Two Hilbert–Schmidt sandwich identities.** Write \(d_n=c_n-m\). Matrix multiplication yields
\[
 (CD_dC)_{nk}=\mathbf1_{\{k\le n\}}\frac1n\sum_{j=k}^n\frac{d_j}{j}.
\]
The first bound from Step 1 implies
\[
 \|CD_dC\|_{\mathcal S_2}^{2}
 \le B_d^2\sum_{n=1}^{\infty}\sum_{k=1}^n\frac1{n^2k^2}<\infty.
\]
Therefore
\[
 CD_cC-mC^2\in\mathcal S_2.\tag{1}
\]
Similarly \(e_n=|c_n|^2-\mu\) is periodic and mean zero, and
\[
 (C^*D_eC)_{jk}=\sum_{n\ge\max(j,k)}\frac{e_n}{n^2}.
\]
Since at most \(2M-1\) pairs of positive indices have \(\max(j,k)=M\), the second bound implies
\[
 \|C^*D_eC\|_{\mathcal S_2}^{2}
 \le B_e^2\sum_{M=1}^{\infty}\frac{2M-1}{M^4}<\infty.
\]
Thus
\[
 C^*D_c^*D_cC-\mu C^*C\in\mathcal S_2.\tag{2}
\]
The Hilbert–Schmidt statement (2) suffices here. No priority is claimed for the periodic Gram relation itself; the new assertion is the joint first-moment/squared-modulus law for every essential power.

**Step 3: The Cesàro Calkin norm and normality.** The classical \(\ell^2\) Hardy inequality gives \(\|C\|\le2\). For each \(N\), define the unit vector
\[
 x^{(N)}_k=\frac{\mathbf1_{\{k\le N\}}}{\sqrt{kH_N}},\qquad
 H_N=\sum_{k=1}^N\frac1k.
\]
The vectors converge weakly to zero. For \(n\le N\), the elementary estimate \(\sum_{k=1}^n k^{-1/2}=2\sqrt n+O(1)\) shows
\[
 \liminf_{N\to\infty}\|Cx^{(N)}\|^2
 \ge \lim_{N\to\infty}\frac1{H_N}\sum_{n=1}^N
 \frac{(2\sqrt n+O(1))^2}{n^2}=4.
\]
Every compact operator sends a weakly null bounded sequence to a norm-null sequence; hence \(\|\pi(C)\|=2\). Furthermore, with \(M=\max(j,k)\),
\[
 (C^*C-CC^*)_{jk}=\sum_{n=M}^{\infty}\frac1{n^2}-\frac1M=O(M^{-2}).
\]
The same count as in Step 2 shows \(C^*C-CC^*\in\mathcal S_2\). Thus \(a=\pi(C)\) is normal and \(\|a^p\|=2^p\) for all positive integers \(p\).

**Step 4: Exact quotient identities and power law.** Set \(b=\pi(D_c)\). Equations (1) and (2) become
\[
 aba=ma^2,\qquad a^*b^*ba=\mu a^*a.
\]
By induction, \((ba)^p=m^{p-1}ba^p\) for every integer \(p\ge1\). Moreover,
\[
 \|ba^p\|^2
 =\|(a^{p-1})^*a^*b^*ba\,a^{p-1}\|
 =\mu\|(a^p)^*a^p\|=\mu\,4^p.
\]
Because \(\pi(R_c)=ba\), the asserted essential norm identity follows. The standard spectral-radius formula in a unital Banach algebra gives
\[
 r_{\mathrm{ess}}(R_c)=\lim_{p\to\infty}
 \|\pi(R_c)^p\|^{1/p}=2|m|,
\]
including \(m=0\). Equation (1), multiplied by bounded factors and iterated, also yields \(R_c^p-m^{p-1}D_cC^p\in\mathcal S_2\) for all \(p\ge2\).

**Step 5: Square-zero regime and numerical radius.** If \(m=0\), (1) yields \(R_c^2=D_cCD_cC\in\mathcal S_2\). Yet the first-power formula gives \(\|\pi(R_c)\|=2\sqrt\mu>0\). Therefore \(\pi(R_c)\) is nonzero and square-zero, so its spectrum equals \(\{0\}\). Every square-zero element \(y\) of a \(C^*\)-algebra has numerical radius \(\|y\|/2\): the positive elements \(y^*y\) and \(yy^*\) are orthogonal, and for any real \(\theta\),
\[
 \|e^{i\theta}y+e^{-i\theta}y^*\|^2
 =\|y^*y+yy^*\|=\|y\|^2.
\]
The state-space numerical-radius formula therefore gives \(w(\pi(R_c))=\sqrt\mu\). If \(c_n=(-1)^n\), \(D_c^*D_c=I\), hence \(R_c^*R_c=C^*C\), completing the example.

## Verification

An independently executable, standard-library-only script `check_periodic_cesaro.py` verifies the exact finite-matrix sandwich formulas over multiple real periodic patterns (including zero-mean and nonzero-mean cases) and computes finite weakly-null norm-test diagnostics. Run it with `python3 check_periodic_cesaro.py` after extracting it alongside this document. The script reports 2,884 successful entrywise identities and elementary numerical tests. It neither proves compactness nor replaces the infinite Hilbert–Schmidt estimates and quotient-algebra argument above. The unbounded-index statements are proved in Steps 1–5.

## Relationship to prior work

Sang's 2026 study establishes the Cesàro operator's membership in the Hardy Toeplitz algebra and characterizes Rhaly membership under a coefficient criterion. The 2025 study by Bellavita, Dellepiane and Stylogiannis treats boundedness, compactness and Schatten ideals for Rhaly matrices. Gallardo-Gutiérrez and Partington's 2024 preprint/2025 publication investigates spectral questions and invariant subspaces, focusing its explicit spectral theorems on moment-generated classes. Bellavita and Stylogiannis's 2026 discrete Mellin calculus proves Hilbert–Schmidt multiplicativity for sampled-ratio matrices; Sang explicitly observes that sampled-ratio matrices and Rhaly matrices intersect only in scalar multiples of Cesàro, so that broader calculus does not contain the present nonconstant periodic Rhaly family. Gül establishes essential normality of the ordinary Cesàro operator; this property is also verified directly in Step 3. None of those inspected results states the exact power-essential-norm law for arbitrary complex periodic modulation, or the noncompact square-zero example in the Calkin algebra. Periodic Gram information alone gives essential singular-value information, not the first-moment-dependent essential spectral radius; the additional sandwich identity (1) supplies the missing spectral information.

## Limitations

The coefficient mean controls the **essential spectral radius**, not a claimed full essential-spectrum shape for nonzero mean. The theorem requires exact periodicity; arbitrary bounded, almost-periodic or ergodic modulation is not included. The ideal remainder is proved to be Hilbert–Schmidt, with no sharp singular-value asymptotics asserted. Literature-priority uncertainty remains for broader averaging theorems expressed in other operator-algebra language; published mathematical novelty is not guaranteed by the reported searches. No independent mathematical validation has occurred.

## References

1. Yuanqi Sang, *The Cesàro Operator, Rhaly operators, and the Toeplitz Algebra* (initial arXiv submission 2026-08-26), arXiv:2608.25740, https://arxiv.org/abs/2608.25740.
2. Carlo Bellavita, Eugenio Dellepiane and Georgios Stylogiannis, *Boundedness, compactness and Schatten class for Rhaly matrices*, arXiv:2503.21930, https://arxiv.org/html/2503.21930v3.
3. Eva A. Gallardo-Gutiérrez and Jonathan R. Partington, *Rhaly operators: more on generalized Cesàro operators*, arXiv:2408.03182; *Annali di Matematica Pura ed Applicata* 204 (2025), https://doi.org/10.1007/s10231-025-01560-5.
4. Carlo Bellavita and Georgios Stylogiannis, *A discrete Mellin calculus in the Toeplitz algebra*, arXiv:2609.09453, https://arxiv.org/abs/2609.09453.
5. Uğur Gül, *The Cesaro Operator in \(\ell^2\) is Essentially Normal*, arXiv:2311.15245, https://arxiv.org/abs/2311.15245.
6. A. Brown, P. R. Halmos and A. L. Shields, *Cesàro operators*, *Acta Sci. Math.* 26 (1965), 125–137; cited for classical Cesàro operator theory.
