# Sharp one-frequency Walsh-basis substitution on central Boolean Hamming balls

## Finding
Let \(r\ge1\), \(n=2r+1\), and \(B_r=\{x\in\mathbb F_2^n:\operatorname{wt}(x)\le r\}\). Its cardinality is \(M=2^{2r}\). The \(M\) even-weight characters \(\chi_\lambda(x)=(-1)^{\lambda\cdot x}\), normalized by \(M^{-1/2}\) on \(B_r\), form an orthonormal basis; the odd-weight characters are the other, and only other, complete orthogonal character spectrum.

Choose any even-weight frequency \(\lambda\), remove it from this basis, and replace it with any odd-weight \(\mu\). Writing \(\operatorname{wt}(\mu+\lambda)=2s+1\), with \(0\le s\le r\), define
\[
\rho_s=\frac{\binom{2r}{r}\binom r s}{2^{2r}\binom{2r}{2s}}.
\]
The resulting normalized square Fourier sampling matrix is invertible, and the **complete squared singular-value spectrum**, including multiplicities, is
\[
\left\{1+\sqrt{1-\rho_s^2},\ 1-\sqrt{1-\rho_s^2},\ 1\ (M-2\text{ times})\right\}.
\]
Its sharp squared condition number is
\[
\mathcal K_s=\frac{1+\sqrt{1-\rho_s^2}}{1-\sqrt{1-\rho_s^2}}.
\]
The **best-conditioned substitutions** are exactly those at Hamming distance \(1\) or \(n\) from the removed frequency, with \(\rho_{\rm best}=2^{-2r}\binom{2r}{r}\), and \(\mathcal K_{\rm best}\sim4\pi r\). The **worst-conditioned substitutions** occur exactly at indices \(s=\lfloor r/2\rfloor\) and \(s=\lceil r/2\rceil\) (one index if equal), with
\[
\rho_{\rm worst}=\begin{cases}
2^{-2r}\binom{r}{r/2},&r\text{ even},\\
2^{-2r}\frac{r+1}{r}\binom r{(r-1)/2},&r\text{ odd},
\end{cases}
\quad \mathcal K_{\rm worst}\sim 2\pi r\,4^r.
\]
Thus one nonorthogonal frequency substitution has a sharp polynomial-versus-exponential worst/best stability dichotomy, despite always preserving a basis.

## Assumptions and scope
The ambient group is the binary vector space \(G=\mathbb F_2^n\). Frequencies are distinct elements of \(G\), and the signal space has counting-measure inner product on \(B_r\). Every character row is divided by \(\sqrt M\), so it has squared norm one. The phrase 'squared condition number' means the ratio of maximal to minimal eigenvalues of the normalized Gram matrix; the singular-value condition number is its square root. The one-frequency substitution replaces exactly one frequency and retains the other \(M-1\) frequencies, without changing sample locations or weights.

## Proof
**1. A complete parity spectrum.** Antipodal translation \(x\mapsto x+\mathbf1\), where \(\mathbf1\) is the all-ones vector, swaps \(B_r\) with its complement: since \(n=2r+1\), every antipodal pair contributes exactly one point of \(B_r\). Hence \(|B_r|=2^{n-1}=M\). For a nonzero even-weight \(\eta\), the character \(\chi_\eta\) takes the same value at paired points; the full-group Walsh sum is zero, so \(\sum_{x\in B_r}\chi_\eta(x)=0\). Thus any two distinct even frequencies are orthogonal on \(B_r\), giving an orthonormal basis after normalization. The same holds for every odd-frequency coset, because differences of two odd frequencies have even weight.

**2. The exact nonzero odd correlations.** Write \(W(w)=\sum_{x\in B_r}(-1)^{\eta\cdot x}\) for any \(\eta\) of weight \(w\). With binary Krawtchouk polynomials \(K_j(w;n)=[z^j](1-z)^w(1+z)^{n-w}\), the partial-sum identity gives, for \(w\ge1\),
\[
W(w)=\sum_{j=0}^r K_j(w;2r+1)=K_r(w-1;2r).
\]
For odd \(w=2s+1\), binomial duality \(\binom{2r}{2s}K_r(2s;2r)=\binom{2r}{r}K_{2s}(r;2r)\) and \(K_{2s}(r;2r)=[z^{2s}](1-z^2)^r=(-1)^s\binom r s\) yield
\[
W(2s+1)=(-1)^s\frac{\binom{2r}{r}\binom r s}{\binom{2r}{2s}}\ne0.
\]
Together with the even-weight vanishing from step 1, these are all the Walsh zeros of \(\mathbf1_{B_r}\), except that the zero-frequency coefficient equals \(M\). Every two distinct frequencies in an orthogonal full spectrum must therefore have even-weight difference, so they lie in the same parity coset. As there are only \(M\) frequencies in one parity coset, those two cosets are the only complete orthogonal character spectra.

**3. Rank-two Gram eigenvalues.** Let \(e_\nu\) denote the normalized character on \(B_r\). Relative to the complete orthonormal even-frequency basis, the replacement vector \(e_\mu\) has coordinate \(c=\langle e_\mu,e_\lambda\rangle=W(2s+1)/M\) along the removed vector, with \(|c|=\rho_s>0\). Its projection onto the \(M-1\) retained vectors has norm \(\sqrt{1-\rho_s^2}\), by Parseval. In an adapted orthonormal coordinate system, the Gram matrix of the retained vectors together with \(e_\mu\) is the identity off one two-dimensional space; its two eigenvalues are \(1\pm\sqrt{1-\rho_s^2}\). This proves invertibility, the complete spectrum, and the sharp frame condition number, including the case \(r=1\).

**4. Exact optimizer and asymptotics.** A cancellation of binomial factors gives
\[
\frac{\rho_{s+1}}{\rho_s}=\frac{2s+1}{2r-2s-1},\qquad 0\le s<r.
\]
This ratio is less than, equal to, or greater than one according as \(s<(r-1)/2\), \(s=(r-1)/2\), or \(s>(r-1)/2\). Consequently the maximum of \(\rho_s\) occurs exactly at \(s=0,r\), and its minimum exactly at the central one or two indices stated above. Direct binomial simplification gives the two formulas for \(\rho_{\rm worst}\). Because \(\mathcal K_s\) decreases strictly as \(\rho_s\) increases, these are exactly the best and worst replacements. Stirling's formula yields
\[
\rho_{\rm best}\sim(\pi r)^{-1/2},\qquad
\rho_{\rm worst}\sim\sqrt{\frac2{\pi r}}\,2^{-r}.
\]
Since \(\frac{1+\sqrt{1-u^2}}{1-\sqrt{1-u^2}}\sim4/u^2\) as \(u\downarrow0\), the stated sharp squared-conditioning asymptotics follow.

## Verification
The accompanying standard-library program `verify.py` verifies the all-index Krawtchouk binomial identity in exact integer arithmetic through \(r=20\), independently enumerates actual Boolean-ball Walsh coefficients for \(1\le r\le5\), tests complete parity-coset orthogonality and the Parseval replacement coefficient, and checks the exact finite-dimension optimizer indexes. Execute `python3 verify.py`; passing output is `VERIFY_OK exact_krawtchouk=230 direct_boolean_balls=5 parity_and_parseval=5 optimal_index=20`. These finite tests corroborate, but do not replace, the all-dimensional proof.

## Relationship to prior work
Ferguson and Iosevich [1,2] develop finite-Boolean-group spectral/tiling theory and Fourier-support obstructions, not one-frequency conditioning on the central Hamming ball. Hogan and Lakey [3,4] treat Walsh Slepian concentration on Hamming balls, not replacement of one character in a complete halfcube Fourier basis. A related published exact quadratic-band majority-halfcube concentration theorem [5] studies the smaller degree-at-most-two Walsh space; its sharp bounds do not imply the complete-basis substitution spectrum. The elementary rank-two row-replacement identity and Krawtchouk polynomial duality are classical inputs, not claimed as new in isolation. The subject-specific contribution here is their exact all-dimensional synthesis for the canonical central Hamming ball, including the complete optimality classification and the polynomial-versus-exponential robustness gap.

## Limitations
The result concerns odd-dimensional central Boolean Hamming balls, exactly one even-to-odd frequency substitution, and uniform samples. It does not solve arbitrary multi-frequency replacement, arbitrary half-density tiling transversals, noisy or weighted sampling, or all Fourier-minor conditioning problems. General Hadamard perturbation bounds and established majority-function Fourier coefficient identities may allow an earlier equivalent derivation; bibliographic priority beyond the inspected evidence remains provisional. The conditioning asymptotics concern \(r\to\infty\) through integer radii; they do not imply every nonorthogonal basis is badly conditioned at a fixed dimension.

## References
[1] Samuel J. Ferguson and Joshua Iosevich, *Fuglede's conjecture holds in eight dimensions over the field with two elements*, arXiv:2610.36417v1, first public 26 October 2026, https://arxiv.org/abs/2610.36417 .

[2] Samuel J. Ferguson and Joshua Iosevich, *Fuglede's conjecture holds in finite prime fields for the eight-dimensional binary and three-dimensional eleven-element cases*, preliminary preprint arXiv:2610.30712v1, first public 22 October 2026, https://arxiv.org/abs/2610.30712 .

[3] J. A. Hogan and J. D. Lakey, *An Analogue of Slepian Vectors on Boolean Hypercubes*, Journal of Fourier Analysis and Applications 25 (2019), 2004–2020, https://doi.org/10.1007/s00041-018-09654-w .

[4] J. A. Hogan and J. D. Lakey, *Spatio-spectral limiting on hypercubes: eigenspaces*, arXiv:1812.08905v1 (2018), https://arxiv.org/abs/1812.08905 .

[5] *Complete two-channel Slepian spectrum for quadratic Walsh signals on majority halfcubes*, publicly indexed mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-complete-two-channel-slepian-spectrum-for-quadratic-walsh-signal--676bf9df5fe8 .
