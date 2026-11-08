# Parity transition in optimally conditioned composite cyclic Gabor tomography

## Finding
Fix a **composite integer** \(N\ge6\). Let \(\mathbf1\in\mathbb C^{\mathbb Z_N}\) be the all-ones vector and \(e_0\) the coordinate vector at zero. For every \(z\in\mathbb C\), form the unit window
\[
g_z=\frac{\mathbf1+ze_0}{\sqrt{N+|z|^2+2\operatorname{Re}z}}.
\]
Let \(\mathcal A_z\) be the full \(N^2\)-outcome cyclic Gabor *operator* lifting defined in the next section, with the Hilbert--Schmidt norm on matrices and Euclidean norm on data. Define its spectral condition number as \(+\infty\) if singular.

Writing \(h=\pi/(2N)\), the **sharp optimum across all complex impulses**, including every singular parameter, is
\[
\boxed{\min_{z\in\mathbb C}\kappa(\mathcal A_z)=
\begin{cases}
(\sqrt N-1)/\sin h,&N\text{ odd composite},\\
(\sqrt N-\cos h)/\sin h,&N\text{ even composite}.
\end{cases}}
\]
The complete optimizer classification is
\[
\boxed{z=-\sqrt N\quad\text{if }N\text{ is odd};\qquad
z=-\sqrt N e^{\pm ih}\quad\text{if }N\text{ is even}.}
\]
The two even-order choices are conjugates. Every optimizer yields an informationally complete operator frame. In both parity classes the optimal condition number grows as \(2N^{3/2}/\pi\), but its exact value and optimizing phase depend on parity.

## Assumptions and scope
Write \(\omega=e^{2\pi i/N}\). For \(a,b,x\in\mathbb Z_N\), define
\[
(T_af)(x)=f(x-a),\qquad (M_bf)(x)=\omega^{bx}f(x).
\]
Set \(v_{a,b}=M_bT_ag_z\) and \(P_{a,b}=v_{a,b}v_{a,b}^*\). The complex-linear operator measurement map is
\[
\mathcal A_z:M_N(\mathbb C)\longrightarrow\mathbb C^{N^2},\qquad
\mathcal A_z(X)=\bigl(\operatorname{tr}(XP_{a,b})\bigr)_{a,b\in\mathbb Z_N}.
\]
This is the full, labelled minimal-outcome Weyl--Heisenberg operator measurement, not a nonlinear stability bound for rank-one recovery. The denominator in \(g_z\) equals \(N-1+|1+z|^2>0\). The stipulated composite hypothesis is essential: the corresponding prime problem has a different optimum and was already settled separately. No assertion is made for a restricted subset of measurements or for arbitrary windows.

## Proof
**1. Fourier diagonalization and complete ambiguity amplitudes.** The normalized Weyl operators \(N^{-1/2}M_bT_a\) are an orthonormal Hilbert--Schmidt matrix basis, and conjugation by time--frequency shifts multiplies each by a character. The characters are mutually orthogonal when summed over all \(N^2\) measurements. Therefore the singular values of \(\mathcal A_z\) are exactly \(\sqrt N\) times the magnitudes of all ambiguity coefficients \(\langle g_z,M_bT_ag_z\rangle\). This standard Weyl-covariant frame diagonalization does not depend on primality.

Put \(z=re^{i\phi}\), with \(r\ge0\), and \(B=N+r^2+2r\cos\phi\). Directly separating the two exceptional coordinates in the correlation gives the following complete multiset of *unnormalized* ambiguity magnitudes:
\[
\begin{array}{c|c}
\text{Weyl labels}&B|\langle g_z,M_bT_ag_z\rangle|\\ \hline
(a,b)=(0,0)&B\\
a=0,\ b\ne0&|r^2+2r\cos\phi|\\
a\ne0,\ b=0&|N+2r\cos\phi|\\
a\ne0,\ b\ne0&|\overline z+z\omega^{ab}|=2r|\cos(\phi+\pi ab/N)|.
\end{array}
\]
The second and third rows each have multiplicity \(N-1\); the fourth contains one value per ordered pair \((a,b)\) with both entries nonzero. In particular, the largest singular value is always \(\sqrt N\), since the identity ambiguity coefficient has modulus one and every others has modulus at most one by Cauchy--Schwarz.

**2. The composite-modulus phase obstruction.** Because \(N\) is composite, some nonzero residue pair has zero product modulo \(N\), whereas choosing \(a=1\) realizes all nonzero products. Hence the mixed-label products \(ab\), with \(a,b\ne0\), realize **every** residue \(k\in\mathbb Z_N\). Define
\[
\delta_N(\phi)=\min_{0\le k<N}|\cos(\phi+\pi k/N)|.
\]
The least normalized ambiguity magnitude \(m_z=s_{\min}(\mathcal A_z)/\sqrt N\) obeys
\[
m_z\le\frac{2r\delta_N(\phi)}{N+r^2+2r\cos\phi}
\le\frac{\delta_N(\phi)}{\sqrt N+\cos\phi},
\]
where the latter inequality uses \(r^2+N\ge2\sqrt N r\) and is strict for \(r\ne\sqrt N\), provided \(\delta_N(\phi)>0\). If \(r=0\) or \(\delta_N(\phi)=0\), the measurement map is singular, and no optimum of positive margin occurs there.

**3. Exact angular maximization.** The zeros of the function \(\delta_N\) form an equally spaced grid with spacing \(\pi/N\) on the phase circle modulo \(\pi\). On each interval between consecutive zeros, \(\delta_N(\phi)\) increases from zero to \(\sin h\) at the midpoint and then decreases to zero. On the increasing half, with \(t\in(0,h)\) the distance from the left zero, differentiation of \(\sin t/(\sqrt N+\cos\phi)\) has numerator
\[
\sqrt N\cos t+\cos(\phi-t)\;>\;\sqrt N\cos h-1>0.
\]
On the decreasing half, differentiation has numerator
\[
-\sqrt N\cos t-\cos(\phi+t)\;<\;-\sqrt N\cos h+1<0.
\]
The strict inequality \(\sqrt N\cos h>1\) holds for all \(N\ge6\). Thus the maximum of the phase--radius upper bound on each grid interval occurs **only at its midpoint**, and its value is \(\sin h/(\sqrt N+\cos\phi)\). Among midpoints it is greatest exactly when \(\cos\phi\) is smallest. For odd \(N\), the unique such midpoint modulo \(2\pi\) is \(\phi=\pi\). For even \(N\), they are \(\phi=\pi\pm h\). Consequently,
\[
\sup_z m_z\le
\begin{cases}
\sin h/(\sqrt N-1),&N\text{ odd composite},\\
\sin h/(\sqrt N-\cos h),&N\text{ even composite}.
\end{cases}
\]
The global maximum in this comparison has no further phases because the cosine strictly separates other grid midpoints.

**4. Sharp attainment, including the two axis branches.** At each candidate phase from Step 3 and at \(r=\sqrt N\), put \(C=1\) in the odd case and \(C=\cos h\) in the even case. The normalized mixed-label minimum is exactly
\[
\frac{\sin h}{\sqrt N-C}.
\]
The two nonidentity axis amplitudes are equal and are both
\[
\frac{\sqrt N-2C}{2(\sqrt N-C)}.
\]
They do not lie below the mixed minimum: the required condition \(\sqrt N-2C\ge2\sin h\) holds for every odd composite \(N\ge9\), since \(\sqrt N\ge3>2(1+\sin(\pi/18))\); and for every even composite \(N\ge6\), since \(\sqrt6=2(\cos(\pi/12)+\sin(\pi/12))\) and, as even \(N\) increases, \(\sqrt N\) increases while \(2(\cos h+\sin h)\) decreases. Thus the upper bounds are attained, all ambiguity coefficients are nonzero, and the corresponding operator liftings are invertible. Equality in the radial bound forces \(r=\sqrt N\); equality in the angular bound forces exactly the phases already displayed. Hence the optimizer classification is complete. Taking reciprocals proves the sharp condition numbers. Finally \(\sin(\pi/(2N))\sim\pi/(2N)\) and \(\sqrt N-C\sim\sqrt N\), giving \(\kappa_{\min}(N)\sim2N^{3/2}/\pi\).

## Verification
The standalone `verify.py` constructs, without inserting the formula into its matrices, each \(N^2\times N^2\) complex lifting matrix from normalized projectors and computes its complete singular spectrum with NumPy. It compares that spectrum with the direct ambiguity formula, verifies the claimed sharp margin, and tests nearby nonoptimal parameters for the composite dimensions \(N=6,8,9,10,12,14,15,16\). The executed run reported `DIRECT_SPECTRA_PASS 1134`. The tested condition numbers, in increasing dimension order, were approximately \(5.732050808\), \(9.470699650\), \(11.517540966\), \(13.900960501\), \(18.943759193\), \(24.543009288\), \(27.485177304\), and \(30.656018562\). These finite computations are corroboration, not an all-order proof; Steps 1--4 establish the all-composite theorem.

## Relationship to prior work
Goldberger--Kang--Okoudjou's general Gabor-POVM analysis already supplies the Weyl ambiguity diagonalization and rank criterion used in Step 1; those tools are **not new**. Bojarovska--Flinth establish general nonvanishing-ambiguity and phase-retrieval principles. A published sharp complex-impulse minimax settles **prime** lengths, where the mixed-label products omit the zero residue and the optimizers have quadrature phase. The present theorem deliberately excludes primes and identifies the different composite-modulus optimum: a negative real phase at odd composite lengths, and two near-negative phases at even composite lengths. A separate exact all-parameter rank classification of one-coordinate windows detects singular parameters at every modulus, but gives no optimum of the strictly positive minimum singular value, nor the associated parity-dependent equality classification. The distinction is therefore a sharp *stability* theorem, rather than a restatement of a known rank theorem.

## Limitations
Only a constant background plus **one complex impulse**, full cyclic Gabor measurements, and composite dimensions \(N\ge6\) are covered. The prime case was settled previously and is not included. The result is an exact operator-lifting stability statement; it gives neither minimax optimality across general windows nor a nonlinear or noisy phase-retrieval error theorem. The proof does not optimize partial-measurement schemes. Historical priority is provisional; broader or unindexed published results could potentially imply a constrained minimax. Independent mathematical validation has not been performed.

## References
1. A. Goldberger, S. Kang, and K. A. Okoudjou, *Towards a classification of incomplete Gabor POVMs in* \(\mathbb C^d\), first public 2021-06-02, arXiv:2106.01509. https://arxiv.org/abs/2106.01509
2. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, first public 2015-03-19, arXiv:1503.05800. https://arxiv.org/abs/1503.05800
3. *Optimal complex impulse in prime-cyclic Gabor tomography: a sharp conditioning barrier*, publicly indexed research result. Its prime-modulus minimax is distinguished in the relationship section.
4. *Exact rank discriminant for one-coordinate cyclic Gabor measurements*, publicly indexed research result. Its all-modulus rank classification is distinguished from the stability optimization.
