# Sharp resonant trapping and two algebraic relaxation laws in a dissipative Labyrinthic map

## Finding

Consider the dissipative Labyrinthic map on \(\mathbb T\times\mathbb R\), with \(\mathbb T=\mathbb R/\mathbb Z\),
\[
I_{n+1}=(1-\gamma)I_n-b[\sin(2\pi\theta_n)+\sin(2\pi\eta\theta_n)],\qquad
\theta_{n+1}=\theta_n-a(I_{n+1}-r_1)(I_{n+1}-r_2)\pmod1.
\]
Fix the natural full-reset and unit-rotation resonance \(\gamma=1\), \(a=1\), \(r_1=1\), \(r_2=-1\), and \(\eta=3\). Let \(t_*\in(0,\pi/2)\) be the unique root of
\[
2t\cot t-4t\tan t=1,
\]
and set
\[
 b_* = \left(\frac{32\pi\sin^2t_*\cos^4t_*}{t_*}\right)^{-1/2}
      =0.18970685602526177149\ldots,\qquad u_* =\frac{t_*}{2\pi}.
\]

**Sharp sector-trapping frontier.** For every \(0<b<b_*\) and every initial \((\theta_0,I_0)\in\mathbb T\times\mathbb R\), the phase interval \((k/4,(k+1)/4)\) containing \(\theta_0\) is forward invariant and its orbit converges to its **left** endpoint \(k/4\) (indices understood modulo four). Exactly four fixed states \((k/4,0)\) exist, and these are the only periodic states. Every invariant Borel probability is exactly a convex combination of the four corresponding point masses; in particular the phase map has zero topological entropy.

The no-crossing property of **all four canonical lifted sectors** holds also at \(b=b_*\), where one interior point in each even-index sector maps to its left endpoint. It fails for every \(b>b_*\). Here a no-crossing sector means that the canonical real lift sends every point of the closed sector into that same sector; the failure assertion does not claim global chaos beyond threshold.

**Two universal rates.** For \(0<b<b_*\), \(\theta_0\in(k/4,(k+1)/4)\), and \(d_n=\theta_n-k/4>0\) in the canonical lift,
\[
\lim_{n\to\infty}n d_n=\frac1{64\pi^2b^2}\quad(k=0,2),\qquad
\lim_{n\to\infty}n d_n^3=\frac1{768\pi^4b^2}\quad(k=1,3).
\]
Thus ordinary and quadratic zeros of the harmonic forcing cause different algebraic critical exponents in alternating, equal-length phase basins. If \(\theta_0\) is uniform on \(\mathbb T\), the distribution of \(n^{1/3}d_n\) converges weakly to
\[
\frac12\delta_0+\frac12\delta_{(768\pi^4 b^2)^{-1/3}}.
\]
The result extends immediately to arbitrary absolutely continuous initial phase laws by replacing the weights by the masses of the even and odd quarter-circle basins.

**Sharp leakage onset.** Let \(\varepsilon=b-b_*>0\). For all sufficiently small \(\varepsilon\), the phases in each even-index quarter-circle that cross their left endpoint in one lifted step form one interval of width
\[
\mathcal L(b)=C_*\sqrt\varepsilon+O(\varepsilon),\qquad
C_* =\frac2\pi\sqrt{\frac{t_*}{-b_*H'(t_*)}}=0.449167782989702775\ldots,
\quad H(t)=2t\cot t-4t\tan t-1.
\]
Both odd-index sectors still have no such one-step leakage immediately above \(b_*\). In particular the total one-step leakage length is \(2C_*\sqrt\varepsilon+O(\varepsilon)\) over the unit phase circle.

## Assumptions and scope

The full-reset parameter \(\gamma=1\) annihilates memory of the incoming action coordinate after one iteration, and \(a=1\) is an exact integer unperturbed rotation. The odd harmonic \(\eta=3\) creates both simple and double forcing zeros. The specified sharp frontier concerns the canonical four phase sectors and the lifted one-step map; it is **not** a complete bifurcation description for arbitrary \(a\), \(\gamma\), \(\eta\), or for forcing above the frontier. For \(0<b<b_*\), no exceptional positive-measure set is excluded; phases initially at a sector endpoint are fixed immediately after the first reset and do not obey the nonzero-distance asymptotic laws.

## Proof

**1. Reduction and zeros.** Set \(f(\theta)=\sin(2\pi\theta)+\sin(6\pi\theta)=4\sin(2\pi\theta)\cos^2(2\pi\theta)\). With the indicated parameters, direct substitution yields
\[
I_{n+1}=-bf(\theta_n),\qquad
F_b(\theta_n)=\theta_{n+1}=\theta_n-b^2f(\theta_n)^2\pmod1.
\]
The forcing vanishes exactly at \(\theta=k/4\), \(k=0,1,2,3\). For a left endpoint \(\ell=k/4\) and displacement \(u\in[0,1/4]\), the phase lift is \(\ell+u\mapsto\ell+u-b^2f(\ell+u)^2\). Its displacement is nonincreasing, and it stays in its closed sector exactly when \(b^2f(\ell+u)^2\le u\) at every \(u\) in that sector.

**2. Exact extremal ratio.** Put \(t=2\pi u\in[0,\pi/2]\). In even and odd sectors, respectively,
\[
f(\ell+u)^2=16\sin^2t\cos^4t\quad\text{and}\quad
f(\ell+u)^2=16\cos^2t\sin^4t.
\]
The associated displacement ratios are
\[
R_e(t)=\frac{32\pi\sin^2t\cos^4t}{t},\qquad
R_o(t)=\frac{32\pi\cos^2t\sin^4t}{t},
\]
extended by continuity at zero. For \(0\le t\le\pi/4\), \(R_o(t)\le R_e(t)\). For \(\pi/4\le t\le\pi/2\), the universal harmonic bound \(|f|\le8/(3\sqrt3)\) and \(u\ge1/8\) give \(R_o\le512/27<27\), while \(R_e(\pi/6)=27\). Thus the global maximum of all four sector ratios occurs in an even sector.

The logarithmic derivative of \(R_e\) is \(H(t)/t\), where \(H(t)=2t\cot t-4t\tan t-1\). It satisfies \(H(0+)=1\), \(H(\pi/2-)=-\infty\), and
\[
H'(t)=2\left(\cot t-t\csc^2t\right)-4\left(\tan t+t\sec^2t\right)<0,
\]
since \(\sin t\cos t<t\) on \((0,\pi/2)\). Therefore \(t_*\) exists uniquely and is the unique nondegenerate maximizer. The inequality \(b^2\max\{R_e,R_o\}\le1\) is equivalent to \(b\le b_*\), establishing sharpness. At equality the two even sectors have a single additional critical preimage \(u_*\) of the left endpoint, where the lift is tangent to that endpoint.

**3. Global convergence and invariant measures.** For \(0<b<b_*\), in each open sector \(0<u_{n+1}<u_n\) because \(f\) has no interior zero. Thus \(u_n\downarrow u_\infty\ge0\). Continuity would force \(f(\ell+u_\infty)=0\), and the only zero in the closed interval below \(u_0<1/4\) is \(u_\infty=0\). The action component tends to zero by its reset formula. Endpoints are fixed after one step. No nonconstant periodic orbit can exist because the lifted displacement is strictly decreasing in every open sector. If \(\mu\) is an invariant Borel probability, the pointwise convergence and dominated convergence applied to continuous test functions imply that \(\mu\) is supported on the four fixed states. Conversely, any mixture of their point masses is invariant. The phase map is continuous on the compact circle; the variational principle and absence of positive-entropy invariant measures imply zero topological entropy.

**4. Rates and limiting phase law.** At even endpoints, \(f'(0)=8\pi\), \(f'(1/2)=-8\pi\); at odd endpoints, \(f'(\ell)=0\) and \(\tfrac12f''(1/4)=16\pi^2\), \(\tfrac12f''(3/4)=-16\pi^2\). Taylor expansion therefore yields
\[
u_{n+1}=u_n-64\pi^2b^2u_n^2+O(u_n^3)\quad(k\text{ even}),
\]
\[
u_{n+1}=u_n-256\pi^4b^2u_n^4+O(u_n^5)\quad(k\text{ odd}).
\]
For any positive decreasing sequence satisfying \(u_{n+1}=u_n-cu_n^p+O(u_n^{p+1})\) and \(u_n\to0\), \(p>1\), its reciprocal-power increments obey \(u_{n+1}^{-(p-1)}-u_n^{-(p-1)}\to(p-1)c\); Cesàro summation proves \(n u_n^{p-1}\to1/((p-1)c)\). This gives both stated constants. Under any phase law charging no endpoints, the pointwise limits of \(n^{1/3}d_n\) are zero on even sectors and \((768\pi^4b^2)^{-1/3}\) on odd sectors. Almost-sure convergence implies the stated weak mixture; no unjustified exchange of unbounded moments is used.

**5. Square-root onset.** Write \(G_b(u)=u-b^2f(u)^2=u[1-b^2R_e(2\pi u)]\) on an even sector. At \((b_*,u_*)\), \(G=G_u=0\). Its second derivative is positive because \(R_e\) has a strict nondegenerate maximum, and \(\partial_bG=-2u_*/b_*<0\). A Taylor expansion with the implicit-function theorem gives two simple zero branches \(u_\pm(b)=u_*\pm \tfrac12 C_*\sqrt{b-b_*}+O(b-b_*)\). The set where \(G_b<0\) is precisely \((u_-,u_+)\); the displayed formula for \(C_*\) follows from \(R_e''(t_*)=R_e(t_*)H'(t_*)/t_*\) and \(t=2\pi u\). The odd-sector ratio has a strictly smaller maximum, so the odd sectors remain nonleaking for all sufficiently small positive \(b-b_*\). The same even-sector geometry repeats after translation by \(1/2\).

## Verification

Run `python verify.py` with Python 3, `sympy` and `mpmath`. The checker independently tests the trigonometric factorization and fixed-phase jets, computes \(t_*\), \(b_*\), and the leakage coefficient at high precision, checks leakage openings at three small positive offsets, samples all four sector inequalities, and compares four long trajectories with the two exact asymptotic coefficients. The printed success marker is `VERIFY_OK`. The finite trajectory and mesh checks are **not** substitutes for the interval extremum proof or for the asymptotic argument.

## Relationship to prior work

Souza, Egydio de Carvalho, Viana, and Caldas (2024) introduce and study this dissipative Labyrinthic map and numerically investigate shearless attractors, coexistence of attractors, basin entropy, and parameter-space periodic structures. Their published treatment does not give the fully reset resonant sector invariant-measure classification, the exact sharp no-crossing threshold, the square-root leakage coefficient, or the alternating parabolic rates. Mugnaine et al. (2021) study dissipative standard nontwist dynamics, with numerical transitions and basin entropy, but do not establish the present four-sector exact theorem. Standard one-dimensional parabolic iteration explains the **general power-law method** once an explicit local map is known; it does not establish the global four-basin decomposition, this harmonic extremal equation, or the leakage-width constant. Literature-priority claims concern these specific evaluated combinations rather than a new general theory of parabolic maps.

## Limitations

The global classification is for maximal action reset, unit integer resonance, and harmonic index three. The no-crossing threshold is sharp **for the stated canonical sector property only**, not a claimed chaos or basin-merging threshold. The two asymptotic formulas apply to non-fixed initial phases for \(0<b<b_*\), not to phases that hit a fixed endpoint finitely at the boundary. The leakage expansion describes only the first lifted iterate just above the threshold; long-term fate of leaking orbits is not classified. The numerical checker is supplementary and independent historical priority has not been certified.

## References

1. L. F. B. Souza, R. Egydio de Carvalho, R. L. Viana, and I. L. Caldas, *Shearless and periodic attractors in the dissipative Labyrinthic map*, Chaos **34**, 123132 (public online December 5, 2024), DOI: https://doi.org/10.1063/5.0225577; freely available accepted manuscript: https://fisica.ufpr.br/viana/artigos/2024/luis.pdf.
2. M. Mugnaine et al., *Curry–Yorke route to shearless attractors and coexistence of attractors in dissipative nontwist systems*, Chaos **31**, 023125 (2021), DOI: https://doi.org/10.1063/5.0035303; freely available manuscript: https://web.if.usp.br/controle/sites/portal.if.usp.br.ifusp/files/Mugnaine%20Chaos%202021.pdf.
