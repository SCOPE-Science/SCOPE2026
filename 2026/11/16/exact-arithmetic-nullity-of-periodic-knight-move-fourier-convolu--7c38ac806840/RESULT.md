# Exact arithmetic nullity of periodic knight-move Fourier convolution

## Finding
For integers \(m,n\geq5\), let \(G=\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z\). Define the eight-shift operator \(K\) on complex functions on \(G\) by
\[
(Kf)(x,y)=\sum_{\varepsilon,\delta\in\{-1,1\}}\bigl[f(x+\varepsilon,y+2\delta)+f(x+2\varepsilon,y+\delta)\bigr].
\]
Put \(g=\gcd(m,n)\), \(L=\operatorname{lcm}(m,n)\), and write \(\mathbf1_E\) for the indicator of condition \(E\). Then the **exact complex nullity** is
\[
\begin{aligned}
\dim_{\mathbb C}\ker K={}&2g\mathbf1_{2\mid L}-\mathbf1_{2\mid m}-\mathbf1_{2\mid n}\\
&+2\bigl(\mathbf1_{6\mid m}+\mathbf1_{6\mid n}+\mathbf1_{2\mid m,\,3\mid n}+\mathbf1_{3\mid m,\,2\mid n}\bigr)\\
&+8\mathbf1_{8\mid m,\,8\mid n}.
\end{aligned}
\]
In particular, \(K\) is invertible **if and only if both \(m\) and \(n\) are odd**. On a square torus of side \(N\geq5\), the formula reduces to
\[
\dim\ker K=(2N-2)\mathbf1_{2\mid N}+8\mathbf1_{6\mid N}+8\mathbf1_{8\mid N}.
\]
Every null vector is a linear combination of the explicitly identified Fourier characters described in the proof.

## Assumptions and scope
The group is finite and the functions are complex valued. All eight knight displacements \((\pm1,\pm2)\) and \((\pm2,\pm1)\), with independent sign choices, are distinct for \(m,n\geq5\), so \(K\) is also the ordinary (unweighted) adjacency operator of the simple toroidal knight graph. The theorem concerns the exact zero eigenspace and invertibility, not the size of nonzero eigenvalues, statistical recovery with noise, or bounded square boards without wraparound.

## Proof
For \(0\leq k<m\) and \(0\leq\ell<n\), the character
\[
\chi_{k,\ell}(x,y)=\exp\!\left(2\pi i\left(\frac{kx}{m}+\frac{\ell y}{n}\right)\right)
\]
forms part of the orthogonal Fourier basis. Put \(\theta=2\pi k/m\), \(\phi=2\pi\ell/n\), \(u=\cos\theta\), \(v=\cos\phi\). Directly summing the eight shifts gives
\[
K\chi_{k,\ell}=\lambda_{k,\ell}\chi_{k,\ell},\qquad
\lambda_{k,\ell}=4(\cos2\theta\cos\phi+\cos\theta\cos2\phi)
=4(u+v)(2uv-1).
\]
Consequently the kernel is exactly the span of those characters for which \(u+v=0\) or \(2uv=1\). These two cases are disjoint: if \(v=-u\), then \(uv=-u^2\leq0\).

**First factor.** The equation \(\cos\theta+\cos\phi=0\) holds exactly when \(\theta+\phi\equiv\pi\) or \(\theta-\phi\equiv\pi\pmod{2\pi}\). Each of the two homomorphisms
\[
(k,\ell)\longmapsto k/m\pm\ell/n\pmod1
\]
has image the subgroup of order \(L\) in \(\mathbb Q/\mathbb Z\) and kernel of size \(g\). Thus each equation has \(g\) solutions if \(L\) is even, otherwise none. The two solution sets intersect at precisely \((\theta,\phi)=(\pi,0)\) if \(m\) is even and \((0,\pi)\) if \(n\) is even. Inclusion-exclusion gives \(2g\mathbf1_{2\mid L}-\mathbf1_{2\mid m}-\mathbf1_{2\mid n}\).

**Second factor.** The identity \(2\cos\theta\cos\phi=\cos(\theta+\phi)+\cos(\theta-\phi)\) reduces the equation \(2uv=1\) to the rational-angle equation \(\cos A+\cos B=1\). By the two-term case of the Conway–Jones rational-cosine classification [2, Theorem 7], its possibilities are \(\{\cos A,\cos B\}=\{1,0\}\) or \(\{\tfrac12,\tfrac12\}\). To see that the classification applies, when neither summand is an endpoint, both cosines must be strictly positive. The only nontrivial two-angle rational relation listed in [2] has **opposite** cosine coefficients, hence cannot give a positive-coefficient sum equal to one; rational individual cosines are confined to \(0,\pm\tfrac12,\pm1\).

Solving the angle equations gives precisely the following possibilities, with each \(\pm\) independently chosen:
\[
\begin{gathered}
(\theta,\phi)=(0,\pm\pi/3),\quad(\pm\pi/3,0),\\
(\pi,\pm2\pi/3),\quad(\pm2\pi/3,\pi),\\
(\theta,\phi)\in\{\pm\pi/4\}^2\cup\{\pm3\pi/4\}^2.
\end{gathered}
\]
The first four forms contribute, respectively, \(2\mathbf1_{6\mid n}\), \(2\mathbf1_{6\mid m}\), \(2\mathbf1_{2\mid m,3\mid n}\), and \(2\mathbf1_{3\mid m,2\mid n}\) frequencies. The last form contributes \(8\mathbf1_{8\mid m,8\mid n}\). The forms are disjoint and exhaust the second factor.

Adding the two disjoint contributions proves the stated nullity. If both dimensions are odd, every term is zero. If either dimension is even, \(L\) is even and \(2g-\mathbf1_{2\mid m}-\mathbf1_{2\mid n}\geq1\), so a zero mode exists. The square formula follows by substitution.

## Verification
A standalone Python 3 script, `verify_knight.py`, constructs two independent roots of unity inside suitable finite prime fields and evaluates the unfactored eight-shift multiplier at every frequency for all \(400\) pairs \(5\leq m,n\leq24\). It counts zero values and compares against the formula without using complex floating point. It also checks seven boundary examples, including \((m,n)=(6,9)\). Command: `python3 verify_knight.py`. The observed output is `PASS: 400 exact finite-field spectral-nullity checks (5<=m,n<=24)` and `PASS: seven boundary and resonance examples`. These finite-field tests provide a reproducible consistency check, not an independent proof over \(\mathbb C\); the unlimited-size conclusion is the preceding Fourier and rational-angle argument.

## Relationship to prior work
The publicly available full text of Cibu and collaborators [1] defines and studies the same toroidal knight graphs but seeks graph gonality using chip-firing and cut arguments, not the fixed adjacency-convolution zero spectrum. Conway and Jones [2] classify the relevant rational-angle relations but do not count Fourier zeros for the knight stencil. The broad toroidal graph spectral method of John and Sachs [3] explains factorization principles for periodic graphs, particularly hexagonal tessellations; the published text of its general spectral factorization and hexagonal applications does not state this rectangular knight nullity formula. The fixed-operator kernel and the arithmetic \(6\)- and \(8\)-resonance counts are the claimed contribution, not Fourier diagonalization itself.

## Limitations
The assertion relies on the classical two-angle classification [2]. It is not an elementary standalone reproof of that theorem. It gives only kernel dimension and a Fourier basis, not a quantitative condition number. It does not extend as stated to boards of side fewer than five, where knight displacements can coincide modulo a side. A complete historical-priority search of older graph-spectrum tables remains a limitation; no assertion of independent external verification is made.

## References
1. N. Cibu, K. Ding, S. DiSilvio, S. Kononova, C. Lee, R. Morrison, K. Singal, *The Gonality of Chess Graphs*, arXiv:2403.03907, initial public version March 6, 2024. https://arxiv.org/abs/2403.03907
2. J. H. Conway and A. J. Jones, *Trigonometric Diophantine Equations (On Vanishing Sums of Roots of Unity)*, Acta Arithmetica 30 (1976), 229–240, Theorem 7. https://mathweb.ucsd.edu/~tgrubb/trig_dio.pdf
3. P. E. John and H. Sachs, *Spectra of Toroidal Graphs*, Discrete Mathematics 309 (2009), 2663–2681, DOI:10.1016/j.disc.2008.06.034. https://doi.org/10.1016/j.disc.2008.06.034
