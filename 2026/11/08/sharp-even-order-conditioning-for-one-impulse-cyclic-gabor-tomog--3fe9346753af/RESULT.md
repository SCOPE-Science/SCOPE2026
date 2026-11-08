# Sharp even-order conditioning for one-impulse cyclic Gabor tomography

## Finding
For every **even** integer \(N\ge6\), let \(G=\mathbb Z_N\), \(\omega=\exp(2\pi i/N)\), and consider the normalized one-impulse window
\[
 h_z(j)=\frac{1+z\mathbf1_{\{j=0\}}}{\sqrt{N+|z|^2+2\operatorname{Re}z}},\qquad z\in\mathbb C.
\]
Let \(\mathcal L_z\) be the full cyclic Gabor intensity lifting of the \(N^2\) rank-one projectors onto \(M_vT_uh_z\). With Hilbert--Schmidt and Euclidean norms and condition number \(+\infty\) for a singular lifting, the **sharp constrained condition number** is
\[
\boxed{\min_{z\in\mathbb C}\kappa(\mathcal L_z)=
 \frac{\sqrt N-\cos(\pi/(2N))}{\sin(\pi/(2N))}.}
\]
The **only optimizers** are
\[
\boxed{z=-\sqrt N\exp\left(\pm\frac{\pi i}{2N}\right).}
\]
At either optimizer the normalized smallest self-ambiguity modulus is
\[
\frac{\sin(\pi/(2N))}{\sqrt N-\cos(\pi/(2N))}
\sim\frac{\pi}{2N^{3/2}}.
\]
The lifted map is invertible at both optimizers, so the full set of Gabor intensity samples determines every complex signal up to one global scalar phase. The result concerns one-impulse windows, not the best window of arbitrary form.

## Assumptions and scope
Take \(N\) through even integers \(N\ge6\). The unnormalized Euclidean norm on \(\mathbb C^N\) and the associated Hilbert--Schmidt norm on \(M_N(\mathbb C)\) are used. Put \(T_uf(j)=f(j-u)\) and \(M_vf(j)=\omega^{vj}f(j)\). For each \((u,v)\in G^2\), define \(P_{u,v}=|M_vT_uh_z\rangle\langle M_vT_uh_z|\) and \(\mathcal L_z(X)=(\operatorname{tr}(XP_{u,v}))_{u,v}\). The map is complex-linear on **all complex matrices**; the output has its unnormalized Euclidean norm. Its singular values equal \(\sqrt N\) times the moduli of the normalized self-ambiguity values, including multiplicities. Consequently its largest singular value is always \(\sqrt N\). We use \(\kappa=\sigma_{\max}/\sigma_{\min}\).

## Proof
**1. Complete ambiguity branches.** Write \(B=N+|z|^2+2\operatorname{Re}z>0\). Evaluating finite geometric sums gives the unnormalized self-ambiguity coefficients (up to harmless unit phases and frequency reflection)
\[
 B A_z(u,v)=
 \begin{cases}
 B,&u=v=0,\\
 |z|^2+2\operatorname{Re}z,&u=0,\ v\ne0,\\
 N+2\operatorname{Re}z,&u\ne0,\ v=0,\\
 z+\overline z\,\omega^{uv},&u\ne0,\ v\ne0.
 \end{cases}
\]
The general Weyl-basis diagonalization of the full Gabor lifting gives singular values \(\sqrt N|A_z(u,v)|\). Its largest is \(\sqrt N\), since \(|A_z(u,v)|\le1\) and \(A_z(0,0)=1\).

**2. The even-order product obstruction.** Every nonzero residue \(t\in G\) occurs as \(uv=t\) with \(u,v\ne0\) by taking \(u=1\). Since \(N\ge6\) is even, the missing residue \(t=0\) also occurs, for example \(u=2\) and \(v=N/2\). Thus **every** residue occurs among mixed labels. With \(z=\rho e^{i\theta}\), \(\rho>0\), set
\[
 d_N(\theta)=\min_{t\in G}
 \left|\cos\left(\theta-\frac{\pi t}{N}\right)\right|.
\]
The mixed branch ensures
\[
 \min_{u,v}|A_z(u,v)|\le
 \frac{2\rho d_N(\theta)}{N+\rho^2+2\rho\cos\theta}
 \le \frac{d_N(\theta)}{\sqrt N+\cos\theta}.
\]
The last inequality is the exact arithmetic--geometric mean inequality \(\rho+N/\rho\ge2\sqrt N\), with equality **only** at \(\rho=\sqrt N\). A zero impulse makes the lifting singular and cannot be optimal.

**3. Sharp angular bound and equality.** Because \(N\) is even, the zeros of the cosine grid occur precisely at the points of \(\pi\mathbb Z/N\) modulo \(\pi\). Let \(s\in[0,\eta]\) denote the circular distance of \(\theta\) to this grid, with \(\eta=\pi/(2N)\). Then \(d_N(\theta)=\sin s\). The angle \(\pi\) belongs to the same grid; hence the angular distance from \(\theta\) to \(\pi\) is at least \(s\), giving \(\cos\theta\ge-\cos s\). Therefore
\[
 \frac{d_N(\theta)}{\sqrt N+\cos\theta}
 \le\frac{\sin s}{\sqrt N-\cos s}
 \le\frac{\sin\eta}{\sqrt N-\cos\eta}.
\]
The final function increases strictly: its derivative has numerator \(\sqrt N\cos s-1>0\) on \([0,\eta]\). Equality throughout occurs exactly at \(\theta=\pi\pm\eta\pmod {2\pi}\), and Step 2 additionally forces \(\rho=\sqrt N\). This proves the upper bound and **uniqueness of the two possible optimizers**.

**4. Attainment without unexamined branches.** At \(z=-\sqrt N e^{\pm i\eta}\), both the nontrivial axis branches of Step 1 have modulus \(N-2\sqrt N\cos\eta\); the smallest mixed modulus is exactly \(2\sqrt N\sin\eta\). For every even \(N\ge6\),
\[
 \sqrt N\ge2(\cos\eta+\sin\eta),
\]
with equality at \(N=6\). At \(N=6\) the equality follows from \(\cos(\pi/12)+\sin(\pi/12)=\sqrt6/2\); for larger \(N\) the left side increases while the right side strictly decreases. Hence the mixed minimum is no larger than either axis modulus, so the normalized smallest ambiguity **attains** the upper bound of Step 3. The corresponding condition number is its reciprocal, exactly as stated. All its singular values are nonzero. The standard injective-lifting implication proves phase retrieval.

## Verification
The standalone `CHECK.py` constructs each self-ambiguity coefficient directly from its defining complex finite sum, independently compares its minimum against the four-branch formula, and verifies the optimizer and closed norm formula in every even order \(N=6,8,10,12,14,16,18,20\). It additionally tests 1,280 independently selected nonoptimal complex-impulse parameters against the global upper bound. Running `python3 CHECK.py` returns `CHECK_OK even_orders=8 direct_cases=48 random_phase_radius_cases=1280`. Such finite calculations are corroboration; the proof establishes all even \(N\ge6\).

## Relationship to prior work
The previously established **prime-order** complex-impulse minimax gives \(\sqrt p/\sin(\pi/p)\) and optimizers \(\pm i\sqrt p\); that theorem assumes primality and its mixed-product set omits zero. The known **all-order** complex-impulse rank discriminant classifies which parameters are informationally complete, but does not optimize the smallest singular value for even dimensions. The prior exact positive-impulse quadratic-chirp calculation has a nontrivial lifted kernel in even dimensions; the optimized complex phase eliminates this obstruction. A quadratic chirp times a one-impulse constant window is unitarily related by a time-frequency shear, so that chirp is **not** a separate new construction. The current result is specifically the even-order sharp complex-parameter stability optimization, not the general Gabor lifting identity or the existence of phase-retrievable windows in all dimensions.

The more general 2026 algebraic-perturbation constructions supply quantitatively stable full-spark Gabor windows in all cyclic orders, but do not determine this sharp two-parameter one-impulse optimum. Full-spark and generic-window optimality are not claimed here.

## Limitations
No assertion is made for the smaller even dimensions \(N=2,4\) (where the axis branch need not permit the stated optimizer), for arbitrary windows, for incomplete measurement data, or for full spark. The result computes linear-lifting conditioning, not an optimal nonlinear inverse-Lipschitz constant. It may have an older equivalent formulation under Weyl-covariant POVM or polyphase-impulse terminology; priority is not independently certified.

## References
1. D. Li, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations*, arXiv:2609.09614, first public September 9, 2026; relevant finite-cyclic stabilization and ambiguity sections.
2. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800, especially Theorems 2.2--2.3.
3. *Optimal complex impulse in prime-cyclic Gabor tomography: a sharp conditioning barrier*, published-finding corpus public mathematical record, October 11, 2026, `https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-optimal-complex-impulse-in-prime-cyclic-gabor-tomography-a-sharp--c114096c73ba`.
4. *Exact rank discriminant for one-coordinate cyclic Gabor measurements*, published-finding corpus public mathematical record, October 11, 2026, `https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-rank-discriminant-for-one-coordinate-cyclic-gabor-measurem--4ad1eba7465a`.
5. *Single-impulse quadratic chirps: exact cyclic Gabor tomography spectrum and arithmetic rank obstruction*, published-finding corpus public mathematical record, October 11, 2026, `https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-single-impulse-quadratic-chirps-exact-cyclic-gabor-tomography-sp--03361b3cff9c`.
