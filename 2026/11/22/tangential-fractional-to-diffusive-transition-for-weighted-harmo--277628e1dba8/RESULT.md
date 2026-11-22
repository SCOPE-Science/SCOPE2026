# Tangential fractional-to-diffusive transition for weighted harmonic Berezin kernels

## Finding

For each real \(\alpha>-1\), consider the complex Hilbert space of harmonic functions on the upper half-plane \(\mathbb H=\{x+iy:y>0\}\) that are square-integrable against \(y^\alpha\,dx\,dy\). Let \(R_\alpha(z,w)\) be its real-valued reproducing kernel, and define the harmonic Berezin transform of a bounded measurable symbol by
\[
 (\mathcal B_\alpha f)(z)=\frac{1}{R_\alpha(z,z)}\int_{\mathbb H}f(w)R_\alpha(z,w)^2(\Im w)^\alpha\,dA(w).
\]
Put \(\beta=\alpha+2>1\), and let \(p_\beta\) be the normalized horizontal marginal of the coherent-state measure at \(z=i\). Then \(p_\beta\) is an even probability density with the **exact sharp tail**
\[
 p_\beta(x)\sim A_\beta |x|^{-\beta-1}\quad(|x|\to\infty),
\]
where
\[
 A_\beta=\frac{2^{2\beta-1}(\beta-1)}{\pi}\,I_\beta>0,
 \qquad I_\beta=\frac14\mathrm B\!\left(\frac{\beta-1}{2},\frac{\beta+1}{2}\right)
 -\frac12\sin\!\left(\frac{\pi\beta}{2}\right)\mathrm B(\beta-1,\beta+1).
\]
Here \(\mathrm B\) denotes Euler's beta function. Let \(\Phi_\alpha(t)=\int_{\mathbb R}e^{itx}p_\beta(x)\,dx\). For every real \(\xi\) and \(z=x+iy\),
\[
 \mathcal B_\alpha[e^{i\xi\operatorname{Re}(\cdot)}](x+iy)
 =e^{i\xi x}\Phi_\alpha(|\xi|y).
\]
As \(t\downarrow0\), the **complete three-regime leading dispersion law** is
\[
 1-\Phi_\alpha(t)\sim
 \begin{cases}
 \displaystyle \frac{\pi A_{\alpha+2}}{\Gamma(\alpha+3)\sin(\pi(\alpha+2)/2)}\,t^{\alpha+2},&-1<\alpha<0,\\[5pt]
 t^2\log(1/t),&\alpha=0,\\[4pt]
 \displaystyle\frac{1}{\alpha}t^2,&\alpha>0.
 \end{cases}
\]
In particular, the horizontal second moment exists **if and only if** \(\alpha>0\), when its exact value is \(2/\alpha\). At the critical unweighted exponent, the *entire* multiplier is
\[
 \Phi_0(t)=e^{-t}\left(1+\frac23t^2\right)+t\,E_2(t),\qquad
 E_2(t)=\int_1^\infty e^{-tu}u^{-2}\,du,\quad t\ge0.
\]
All limits are for fixed \(\alpha\), not asserted uniform as \(\alpha\to0\).

## Assumptions and scope

The kernel is for the full **complex-valued harmonic** weighted Bergman Hilbert space, not the holomorphic subspace and not the hyperbolic invariant measure. The vertical weight is exactly \(y^\alpha\), \(\alpha>-1\), with no hidden probability-measure normalization. The Fourier convention is \(\widehat f(\xi)=\int_{\mathbb R}e^{-i\xi x}f(x)\,dx\); all characteristic functions are even and real. For negative weights \(-1<\alpha<0\), the Gaussian-tail conclusion is not claimed: this is precisely the fractional regime.

## Proof

**1. Exact harmonic kernel and probability law.** Set \(\beta=\alpha+2\) and \(C_\beta=2^{\beta-1}(\beta-1)/\pi\). Fourier decomposition in the horizontal direction (or the positive/negative-frequency harmonic subspaces) gives
\[
 R_\alpha(x+iy,u+iv)
 =C_\beta\operatorname{Re}\big[(y+v)-i(x-u)\big]^{-\beta}.
\]
Indeed the Fourier transform of this kernel in \(x-u\), at positive frequency \(\lambda\), is \(2^{\beta-1}\lambda^{\beta-1}e^{-(y+v)\lambda}/\Gamma(\beta-1)\), with its even reflection at negative frequency. This is the reciprocal weighted norm density of the decaying harmonic Fourier mode: \(\int_0^\infty v^{\beta-2}e^{-2\lambda v}dv=\Gamma(\beta-1)/(2\lambda)^{\beta-1}\). Hence the formula reproduces the full weighted harmonic space. Its diagonal is \(R_\alpha(x+iy,x+iy)=C_\beta(2y)^{-\beta}\). The reproducing identity implies \(\int R_\alpha(z,w)^2(\Im w)^\alpha\,dA(w)=R_\alpha(z,z)\); therefore the normalized squared kernel defines a probability measure. Horizontal translation and simultaneous dilation imply that its horizontal displacement at height \(y\) has density \(y^{-1}p_\beta((u-x)/y)\). At height one this density is
\[
 p_\beta(x)=\frac{2^{2\beta-1}(\beta-1)}\pi
 \int_0^\infty v^{\beta-2}
 \left[\operatorname{Re}(1+v-ix)^{-\beta}\right]^2dv.
\]
This proves the Fourier-plane-wave identity in the finding.

**2. Tail and exact constant.** For \(x>0\), replace \(v\) by \(xt\), obtaining
\[
 x^{\beta+1}p_\beta(x)
 =\frac{2^{2\beta-1}(\beta-1)}\pi
 \int_0^\infty t^{\beta-2}
 \left[\operatorname{Re}(t+x^{-1}-i)^{-\beta}\right]^2dt.
\]
The integrand is bounded by \(t^{\beta-2}(1+t^2)^{-\beta}\), integrable at both endpoints because \(\beta>1\). Dominated convergence yields the stated positive constant \(A_\beta\), with
\[
 I_\beta=\int_0^\infty t^{\beta-2}
 \left[\operatorname{Re}(t-i)^{-\beta}\right]^2dt.
\]
The identity \((\operatorname{Re}z)^2=(|z|^2+\operatorname{Re}z^2)/2\), the real beta integral after \(t^2\) substitution, and the complex beta integral
\[
 \int_0^\infty t^{\beta-2}(t-i)^{-2\beta}dt
 =e^{i\pi(\beta+1)/2}\mathrm B(\beta-1,\beta+1)
\]
(on the principal branch) give the formula in the finding. Positivity follows from the original nonzero squared integral. Evenness yields the two-sided tail.

**3. Fractional and logarithmic cases.** By symmetry,
\[
 1-\Phi_\alpha(t)=2\int_0^\infty(1-\cos(tx))p_\beta(x)\,dx.
\]
For \(1<\beta<2\), the tail and elementary dominated comparison after \(u=tx\) imply
\[
 1-\Phi_\alpha(t)\sim 2A_\beta t^\beta
 \int_0^\infty(1-\cos u)u^{-\beta-1}\,du.
\]
The integral equals \(\pi/[2\Gamma(\beta+1)\sin(\pi\beta/2)]\), yielding the fractional coefficient. For \(\beta=2\), the same formula split at \(x=1/t\), together with \(p_2(x)\sim A_2x^{-3}\), gives \(1-\Phi_0(t)\sim A_2t^2\log(1/t)\). The beta expression gives \(I_2=\pi/8\) and \(A_2=1\). These arguments use only an explicit integrable tail and not an unproved probabilistic limit theorem.

**4. Finite-variance case.** For \(\beta>2\), Parseval applied to the even horizontal Fourier transform
\[
 \widehat{R_\alpha(\cdot+i,u+iv)}(\lambda)
 =\frac{2^{\beta-1}}{\Gamma(\beta-1)}|\lambda|^{\beta-1}e^{-(1+v)|\lambda|}
\]
shows that, conditional on vertical coordinate \(v\), the second moment of the horizontal displacement is exactly \((1+v)^2/(2\beta-3)\). The normalized vertical density is
\[
 \frac{v^{\beta-2}(1+v)^{-(2\beta-1)}}{\mathrm B(\beta-1,\beta)},\qquad v>0.
\]
Its \((1+v)^2\) moment exists precisely for \(\beta>2\) and equals \(2(2\beta-3)/(\beta-2)\). Thus \(\int x^2p_\beta(x)dx=2/(\beta-2)=2/\alpha\), and dominated convergence in \((1-\cos(tx))/t^2\) gives \(1-\Phi_\alpha(t)\sim t^2/\alpha\). For \(\beta\le2\), the strictly positive tail constant makes the second moment infinite, proving the threshold.

**5. Exact critical multiplier.** When \(\beta=2\), the kernel is \(R_0(x+iy,u+iv)=(2/\pi)\operatorname{Re}(y+v-i(x-u))^{-2}\). Set \(F_b(x)=(2/\pi)\operatorname{Re}(b-ix)^{-2}\). Squaring and taking the horizontal Fourier transform yields, for \(s\ge0\) and \(b>0\),
\[
 \int_{\mathbb R}e^{isx}F_b(x)^2dx
 =\frac{e^{-bs}}\pi\left(\frac{s^3}{3}+\frac{s}{b^2}+\frac1{b^3}\right).
\]
Setting \(b=1+v\), dividing by \(R_0(i,i)=1/(2\pi)\) and integrating \(v\ge0\) gives
\[
 \Phi_0(s)=2\int_1^\infty e^{-bs}
 \left(\frac{s^3}{3}+\frac{s}{b^2}+\frac1{b^3}\right)db
 =e^{-s}\left(1+\frac23s^2\right)+sE_2(s).
\]
The value at zero follows by continuity. The expansion \(E_2(s)=1+s(\log s+\gamma-1)+o(s)\) also independently checks the unit coefficient of the critical \(s^2\log(1/s)\) term.

## Verification

The accompanying `check.py` numerically compares the beta-function expression for \(I_\beta\) with direct quadrature for nine exponents, checks scaled horizontal tails, verifies the critical Fourier transform at six positive frequencies, verifies the logarithmic cusp, and checks conditional and integrated second moments. It reports 58 passing finite diagnostics with SciPy. The checks support normalization and constants; the exact all-parameter proof is the sequence of computations above.

## Relationship to prior work

Bradík (arXiv:2310.17562, first publicly submitted 26 October 2023) studies harmonic Bergman kernels on upper half-spaces with vertical weights and expansions of harmonic Berezin transforms for **symbols depending only on height**. The present result instead characterizes horizontal coherent-state displacement and the sharp small-horizontal-frequency multiplier for **symbols depending on the horizontal variable**. The common kernel formula is an input, not the claimed new conclusion. Engliš (arXiv:1601.03716) studies high-power weight asymptotics; its accessible summary does not establish the present fixed-weight transition. The classic upper-half-space Toeplitz and Schatten theory provides general operator context but not the formulas claimed here. No claim of independent mathematical certification or proof of absolute historical priority is made.

## Limitations

The assertion concerns only planar \(\mathbb H\), the exact power weights \(y^\alpha\), the horizontal-frequency response and its low-frequency asymptotics. It does not claim arbitrary vertical weights, higher-dimensional analogues, full two-dimensional Fourier diagonalization, uniform crossover as \(\alpha\to0\), or an independent external audit. Existing general kernel formulas imply the starting integral but do not by themselves state these sharp horizontal dispersion constants. Historical coverage by less easily indexed literature remains possible.

## References

1. Jaroslav Bradík, *Harmonic Berezin transform on half-space with vertical weights*, arXiv:2310.17562v1 (26 October 2023), https://arxiv.org/abs/2310.17562 . In the HTML full text of v4 see Section 2, Lemma 2 and equations (10), (16); Section 3, Theorem 2 and equations (19)–(21).
2. Miroslav Engliš, *High-power asymptotics of some weighted harmonic Bergman kernels*, arXiv:1601.03716v1 (14 January 2016), https://arxiv.org/abs/1601.03716 . Contextual source; only its abstract was accessible for comparison.
3. Boo Rim Choe, Hyungwoon Koo and Young Joo Lee, *Positive Schatten(-Herz) class Toeplitz operators on the half-space*, Potential Analysis 27 (2007), 73–100, https://doi.org/10.1007/s11118-007-9044-6 . General operator context; complete text not inspected.
