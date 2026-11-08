# A unique spectral underdamping transition on a one-defect four-site stochastic ring

## Finding

For a biased four-state nearest-neighbor Markov ring with three unit conductances and one conductance \(k>0\), increasing the magnitude of the uniform bond bias induces **exactly one** change from entirely real relaxation eigenvalues to a complex-conjugate relaxation pair. The change occurs for every finite \(k>0\), including arbitrarily weak or strong defect bonds.

Set \(s=4\sinh^2(f/2)\), and define
\[
\begin{aligned}
P_k(s)={}&16(k-1)^2(k^2-2k+2)\\
&-4k(11k^3-18k^2+11k+12)s\\
&-8k^2(3k^2-10k+15)s^2\\
&-k^2(3k^2-14k+27)s^3.
\end{aligned}
\]
For \(k\ne1\), \(P_k\) has exactly one positive root \(s_*(k)\), and the sharp critical bias is
\[
f_c(k)=2\operatorname{arsinh}\bigl(\sqrt{s_*(k)}/2\bigr).
\]
For \(k=1\), define \(f_c(1)=0\). The nonzero eigenvalues are real for \(|f|\le f_c(k)\) and include exactly one nonreal conjugate pair for \(|f|>f_c(k)\). At equality the discriminant is zero and the eigenvalues remain real, with a repeated root.

The defect limits are sharp:
\[
\begin{aligned}
f_c(k)&=\tfrac23\log(1/k)+\tfrac13\log(32/27)+o(1),&&k\downarrow0,\\
f_c(k)&\longrightarrow\tfrac12\log3,&&k\to\infty.
\end{aligned}
\]
In particular, an arbitrarily large but finite fast bond does not suppress oscillatory relaxation at every bias; the limiting threshold remains positive and finite.

## Assumptions and scope

Sites are indexed by \(i\in\mathbb Z/4\mathbb Z\), with bond conductances \((s_0,s_1,s_2,s_3)=(1,1,1,k)\). For all \(i\), the directed rate \(i\to i+1\) is \(s_i e^{f/2}\), and \(i+1\to i\) is \(s_i e^{-f/2}\), where \(f\in\mathbb R\) and \(k>0\). The column-conservative generator \(W\) has these off-diagonal entries and diagonals equal to minus the outgoing rates. This is the classical (incoherent, \(c=0\)) sector of the bond-jump model in Avnit and Cohen (2023); no quantum-coherent spectral conclusion is asserted.

The chain is irreducible for every finite \(k>0\), so its stationary eigenvalue is simple and equals zero. All other eigenvalues have negative real part. A nonreal conjugate pair yields damped oscillatory components for generic initial distributions; the theorem does not claim that every observable must display oscillations.

## Proof

**1. Exact characteristic polynomial.** Put \(u=e^{f/2}\) and \(t=u+u^{-1}=2\cosh(f/2)\). Direct expansion of \(\det(zI-W)\), using the four directed bonds and column-sum conservation, gives
\[
\det(zI-W)=z\,Q_{k,t}(z),
\]
where
\[
Q_{k,t}(z)=z^3+(k+3)t z^2+(k+1)(3t^2-2)z+(3k+1)t(t^2-2).
\]
This identity may also be verified entry by entry by the standalone exact symbolic checker. It has no approximations in \(f\) or \(k\).

**2. Characteristic discriminant.** Let \(\Delta\) be the cubic discriminant of \(Q_{k,t}\). For a real cubic, \(\Delta>0\) means three distinct real roots, \(\Delta=0\) means all roots real with a repetition, and \(\Delta<0\) means one real and two nonreal conjugate roots. Substituting \(t^2=4+s\), where \(s=4\sinh^2(f/2)\ge0\), and expanding the standard cubic discriminant yields exactly \(\Delta=P_k(s)\).

**3. Strict one-crossing.** The coefficients of the positive powers of \(s\) in \(-P_k(s)\) are strictly positive for every \(k>0\). Indeed \(11k^2-18k+11>0\), \(3k^2-10k+15>0\), and \(3k^2-14k+27>0\) for every real \(k\), because their leading coefficients are positive and their discriminants are \(-160\), \(-80\), and \(-128\), respectively. The first coefficient also has the strictly positive additional term \(12\). Therefore \(P_k\) is strictly decreasing on \([0,\infty)\). Furthermore,
\[
P_k(0)=16(k-1)^2((k-1)^2+1),\qquad \lim_{s\to\infty}P_k(s)=-\infty.
\]
For \(k\ne1\), there is exactly one positive zero. When \(k=1\), the zero is at \(s=0\), and all larger \(s\) yield a negative discriminant. As \(|f|\mapsto s\) is continuous and strictly increasing for \(|f|>0\), the asserted classification follows on the entire parameter domain.

**4. Weak-defect limit.** Write \(s=k^{-2/3}q\). The discriminant converges, at fixed \(q>0\), to \(32-27q^3\) as \(k\downarrow0\). Strict monotonicity brackets the unique zero, hence \(k^{2/3}s_*(k)\to(32/27)^{1/3}\). Because \(2\operatorname{arsinh}(\sqrt{s}/2)=\log s+o(1)\) as \(s\to\infty\), the claimed logarithmic asymptotic follows.

**5. Fast-defect limit.** Dividing by \(k^4\) gives
\[
\lim_{k\to\infty}\frac{P_k(s)}{k^4}
=16-44s-24s^2-3s^3=-(s+4)(3s^2+12s-4).
\]
The unique positive zero is \(s_\infty=-2+4\sqrt3/3\). Strict monotonicity and sign bracketing imply \(s_*(k)\to s_\infty\), so
\[
\lim_{k\to\infty}f_c(k)
=\operatorname{arcosh}(1+s_\infty/2)
=\operatorname{arcosh}(2/\sqrt3)
=\tfrac12\log3.
\]
This completes the proof.

## Verification

Run \(\texttt{python verify.py}\) with Python, SymPy and NumPy. Exact symbolic checks independently construct the full \(4\times4\) generator, expand its characteristic polynomial, reconstruct its cubic discriminant, verify the positivity witnesses and both limiting polynomials. A separate matrix-eigenvalue comparison tests 52 nonsingular parameter points and six threshold substitutions. These finite tests are consistency checks, not the proof of uniqueness or the asymptotics.

## Relationship to prior work

Avnit and Cohen, arXiv:2308.08419v1 (16 August 2023), define the relevant stochastic bond-jump sector of a quantum walk in a random environment, discuss numerical relaxation spectra, and analyze coherent hopping perturbations. Their paper does not give the exact one-defect four-cycle discriminant or single-crossing law. Hurowitz and Cohen, arXiv:1512.00258, develop the older conservative random-walk ring theory and a weak-link approximation in a continuum/large-ring regime; the present claim concerns an exact *four-site* finite generator at arbitrary positive defect strength. The exact general characteristic equation in those references is acknowledged as prior machinery.

Uhl and Seifert, arXiv:1907.04260, and Kolchinsky, Ohga and Ito, arXiv:2605.15884, study general affinity-dependent spectral bounds. Such bounds constrain possible complex eigenvalues but do not, as stated, give necessary and sufficient existence or uniqueness of the crossing in this finite one-defect model. No absolute literature-exhaustiveness claim is made.

## Limitations

The conclusion concerns exactly four sites, three equal bond conductances, uniform antisymmetric bond bias, and no coherent hopping. It does not classify arbitrary four-bond disorder, all larger rings, or quantum-Lindblad spectra. The numerical tests are finite. Publication priority remains subject to a broader independent literature review, particularly for special-case discriminant classifications of unicyclic Markov generators.

## References

1. B. Avnit and D. Cohen, *Quantum walk in stochastic environment*, arXiv:2308.08419v1 (16 August 2023), https://arxiv.org/abs/2308.08419.
2. D. Hurowitz and D. Cohen, *Percolation, sliding, localization and relaxation in topologically closed circuits*, arXiv:1512.00258 (1 December 2015), https://arxiv.org/abs/1512.00258.
3. M. Uhl and U. Seifert, *Affinity-dependent bound on the spectrum of stochastic matrices*, arXiv:1907.04260 (9 July 2019), https://arxiv.org/abs/1907.04260.
4. A. Kolchinsky, N. Ohga and S. Ito, *Cycle affinity and winding localize eigenvalues of Markov generators*, arXiv:2605.15884 (15 May 2026), https://arxiv.org/abs/2605.15884.
