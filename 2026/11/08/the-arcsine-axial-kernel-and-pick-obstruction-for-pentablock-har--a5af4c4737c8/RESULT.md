# Quantitative axial nonvanishing and failure of complete-Pick interpolation in the canonical pentablock Hardy space

## Finding

Let \(\mathcal P\) be the pentablock, let \(H^2(\mathcal P)\) denote the unweighted canonical Hardy space obtained from the pushforward of normalized Haar measure on \(\mathbb T^3\), and let \(L=\{(a,0,0):|a|<1\}\). The **previously published exact restricted kernel** is
\[
K((a,0,0),(b,0,0))=S(t)=\sum_{n\ge0}\frac{4^n}{\binom{2n}{n}}t^n
=\frac1{1-t}+\frac{\sqrt t\arcsin\sqrt t}{(1-t)^{3/2}},\quad t=a\overline b.
\]
Its derivation and the leading fractional boundary singularity were established in *Exact central-fibre Szegő kernel and fractional evaluation blowup for the pentablock* (2026-11-02), and also appear in *Axial reducing shifts and the half-Schatten threshold in three pentablock Hardy spaces* (2026-11-08). Neither the exact kernel nor its central-binomial coefficient norm is claimed as new here.

**The additional conclusions** are a global quantitative zero-free inequality on the axis,
\[
\boxed{|S(t)|\ge (2-\pi/2)|1-t|^{-3/2}>0\qquad(|t|<1),}
\]
and a definitive complete Nevanlinna–Pick obstruction: the restriction \(K|_{L\times L}\) is **not** a complete Pick kernel, and therefore neither is the canonical Hardy kernel on all of \(\mathcal P\). These conclusions distinguish kernel nonvanishing from complete Pick interpolation for a geometrically intrinsic fibre of this several-variable Hardy space.

## Assumptions and scope

The canonical measure is \(\mu=\Psi_*m_3\), with \(m_3\) normalized Haar measure on \(\mathbb T^3\) and
\[
\Psi(\xi,\lambda,\eta)=\bigl(\xi(\lambda-\eta)/2,\lambda+\eta,\lambda\eta\bigr).
\]
The ambient \(H^2(\mathcal P)\) is the closure of coordinate polynomials in \(L^2(\mu)\) with its holomorphic realization. Only this measure and the distinguished axis \(L\) are addressed. The closed formula above is analytic at \(t=0\), with its power-series branch throughout the disk. The zero-free estimate is for axis pairs, not arbitrary points of \(\mathcal P\). The complete Pick conclusion is global because that property is inherited by restricted kernels.

## Proof of the surviving result

**1. Use the established axial kernel and form an auxiliary function.** The exact formula for \(S\) is a previously published input. Define
\[
H(t)=(1-t)^{3/2}S(t)=\sqrt{1-t}+\sqrt t\arcsin\sqrt t.
\]
The analytically chosen power-series branches yield
\[
H'(t)=\frac{\arcsin\sqrt t}{2\sqrt t},\qquad
H(t)=1+\sum_{n=1}^\infty d_nt^n,
\quad d_n=\frac{1}{2n(2n-1)}\frac{\binom{2n-2}{n-1}}{4^{n-1}}>0.
\]
The coefficients are summable and \(H(1)=\pi/2\), so \(\sum_{n\ge1}d_n=\pi/2-1<1\). For every \(|t|<1\),
\[
\operatorname{Re}H(t)\ge1-\sum_{n\ge1}d_n|t|^n\ge 2-\pi/2>0.
\]
Consequently \(|H(t)|\ge2-\pi/2\). Since \(1-t\neq0\) in the disk, division by \(|1-t|^{3/2}\) proves the stated global lower bound and zero-freeness.

**2. A negative normalized Pick coefficient.** The known kernel coefficients begin
\[
S(t)=1+2t+\frac83t^2+O(t^3),\qquad
1-\frac1{S(t)}=2t-\frac43t^2+O(t^3).
\]
The axis kernel is normalized at \(a=0\), irreducible, and nonvanishing by Step 1. A necessary condition for such a kernel to be complete Nevanlinna–Pick is positivity of
\(1-1/S(a\bar b)\) as a kernel on the disk (the normalized complete-Pick criterion). For an analytic radial kernel \(\sum_j h_j(a\bar b)^j\), positivity forces every \(h_j\ge0\): average finite Gram forms over equally spaced angles or integrate the corresponding Fourier quadratic form to isolate each \(h_j\). The coefficient \(-4/3\) contradicts this necessity. Hence \(S\) fails the complete Pick property. As restriction preserves that property, the full canonical pentablock Hardy kernel cannot be complete Pick.

## Mathematical significance and relationship to earlier results

The natural question is whether canonical pentablock Hardy interpolation admits a complete Pick model. A positive answer would imply strong matrix-valued interpolation features; the explicit obstruction rules that out for this specific canonical space. The global quantitative zero-free bound also shows that absence of zeros, even with a uniform half-plane certificate after a known scalar normalization, is not enough for the complete Pick property. This is not merely a negative value of an arbitrary numeric test: the chosen axis is the canonical first-coordinate fibre, and its kernel is the actual restricted ambient kernel.

The 2026-11-02 *Exact central-fibre Szegő kernel and fractional evaluation blowup for the pentablock* already proves the **identical** two-point axial kernel and its boundary singularity. The 2026-11-08 *Axial reducing shifts and the half-Schatten threshold in three pentablock Hardy spaces* also explicitly obtains the identical closed function and its asymptotics. The original pentablock construction of Su and Tomar, arXiv:2610.17729, supplies the canonical Hilbert space and boundary measure; the earlier papers provide the exact kernel used here. The reciprocal-binomial series and general complete-Pick criterion are classical inputs and not claimed as original. The remaining potential novelty is only the quantitative zero-free inequality and its use with the negative quadratic coefficient to rule out complete Pick interpolation. A related earlier source using another kernel normalization might contain these deductions implicitly; full literature priority is therefore qualified.

## Verification and limitations

The accompanying unmodified `CHECK.py` verifies the first moments, the closed analytic kernel, the first negative normalized Pick coefficient, the coefficient sign in \(H\), and sample complex points with high precision. Independently, the exact coefficients \(1,2,8/3\) give the negative Pick coefficient \(-4/3\), and \(2-\pi/2>0\). Finite calculations are checks, not proofs of the global inequality or interpolation obstruction; these are the analytic arguments above. No off-axis zero-free result, full Pick interpolation classification for other measures, or assertion about all pointwise kernels is made.

## References

1. *Exact central-fibre Szegő kernel and fractional evaluation blowup for the pentablock* (2026-11-02), https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-exact-central-fibre-szeg-kernel-and-fractional-evaluation-blowup--cd47829e8f95 .
2. *Axial reducing shifts and the half-Schatten threshold in three pentablock Hardy spaces* (2026-11-08), https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-axial-reducing-shifts-and-the-half-schatten-threshold-in-three-p--1ffd80d63bf1 .
3. G. Su and N. Tomar, *Hardy Spaces and Toeplitz operators on the Pentablock*, arXiv:2610.17729, https://arxiv.org/abs/2610.17729 .
4. S. Pal and N. Tomar, *A Toeplitz corona theorem for the pentablock and applications*, arXiv:2606.00850, https://arxiv.org/abs/2606.00850 .
