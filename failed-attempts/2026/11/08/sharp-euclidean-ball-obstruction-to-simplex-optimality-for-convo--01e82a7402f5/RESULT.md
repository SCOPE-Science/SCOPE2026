# Sharp Euclidean-ball obstruction to simplex optimality for convolution bodies

## Finding

For every integer \(n\ge2\), define the normalized volume of the symmetric Euclidean lens
\[
g_n(r)=\frac{|B_2^n(r e_1,1)\cap B_2^n(-r e_1,1)|}{|B_2^n|}
=I_{1-r^2}\!\left(\frac{n+1}{2},\frac12\right),\quad 0\le r\le1,
\]
where \(I_x(a,b)\) is the regularized incomplete beta function. Put
\[
c_n=\frac12\binom{2n}{n}^{1/n},\qquad s_n(r)=g_n(r)^{1/n}.
\]
There exists exactly one \(r_n\in(0,1)\) such that
\[
r_n=c_n\bigl(1-s_n(r_n)\bigr).
\]
Let \(s_n^*=s_n(r_n)=1-r_n/c_n\) and \(\theta_n^*=(s_n^*)^n\). For each \(0<\theta<\theta_n^*\), the Euclidean ball pair \((B_2^n,-B_2^n)\) gives a *strictly smaller* normalized \(\theta\)-convolution-body volume ratio than any opposite simplex pair. For \(\theta_n^*<\theta<1\), the inequality between these two specified classes reverses; they tie at \(\theta_n^*\). This makes \(\theta_n^*\) the exact ball-versus-simplex comparison threshold, not necessarily the true universal threshold for simplex optimality.

The exact crossing has the sharp high-dimensional laws
\[
\boxed{r_n=\frac45-\frac{3}{25n}\log\!\left(\frac{512\pi n}{729}\right)+o(n^{-1})},
\]
\[
\boxed{s_n^*=\frac35-\frac{7\log n}{50n}+\frac{1}{50n}\log\!\left(\frac{2^{27}}{3^{18}\pi^7}\right)+o(n^{-1})},
\]
and consequently
\[
\boxed{\theta_n^*\sim\left(\frac35\right)^n n^{-7/30}\left(\frac{2^{27}}{3^{18}\pi^7}\right)^{1/30}}.
\]
The previously published elementary ball obstruction \(s\le(c_n^2-1)/(c_n^2+1)\), where \(s=\theta^{1/n}\), is strictly improved in every dimension: 
\[
\boxed{s_n^*>\frac{c_n^2-1}{c_n^2+1}.}
\]
For \(n=2\), the exact comparison threshold is numerically \(s_2^*\approx0.4107874899\), or \(\theta_2^*\approx0.1687463619\), versus the previously explicit obstruction \(s\le1/5\).

## Assumptions and scope

A convex body is compact, convex, and full-dimensional. For \(K,L\subset\mathbb R^n\) and \(0\le\theta\le1\), the \(\theta\)-convolution body is \(K+_\theta L=\{z\in K+L:|K\cap(z-L)|\ge\theta M(K,L)\}\), with \(M(K,L)=\max_z|K\cap(z-L)|\). Define its normalized ratio \(R_n(K,L;\theta)=|K+_\theta L|^{1/n}/(|K|^{1/n}+|L|^{1/n})\). All comparisons concern the specific full-dimensional Euclidean ball pair and opposite nondegenerate simplex pair, in the same dimension. The statement does not identify a global minimizer among all convex body pairs in the interval where the ball wins this two-family comparison.

## Proof

**1. Exact lens profile and the two ratios.** Write \(\kappa_j=|B_2^j|\). Slicing the intersection of unit balls whose centers are separated by \(2r\) gives
\[
g_n(r)=\frac{2\kappa_{n-1}}{\kappa_n}\int_r^1(1-t^2)^{(n-1)/2}\,dt,
\qquad g_n'(r)=-\frac{2\kappa_{n-1}}{\kappa_n}(1-r^2)^{(n-1)/2}.
\]
Substitution \(u=1-t^2\) and normalization at \(r=0\) yield the stated beta-function representation. Since \((B_2^n)+_\theta(-B_2^n)\) is the centered ball of radius \(2r\) determined by \(g_n(r)=\theta\), its ratio is \(r\). An opposite simplex pair has ratio exactly \(c_n(1-\theta^{1/n})\), by the known equality formula for simplex convolution bodies. Thus the comparison function at lens separation \(r\) is \(h_n(r)=c_n(1-s_n(r))-r\): a ball strictly beats the simplex when \(h_n(r)>0\).

**2. Unique crossing.** Let \(C_r=B_2^n(r e_1,1)\cap B_2^n(-r e_1,1)\). For \(0\le\lambda\le1\), convexity of Euclidean balls gives
\[
(1-\lambda)C_{r_0}+\lambda C_{r_1}\subseteq C_{(1-\lambda)r_0+\lambda r_1}.
\]
Brunn--Minkowski implies concavity of \(s_n(r)=|C_r|^{1/n}/\kappa_n^{1/n}\). For distinct \(0\le r_0<r_1<1\), this concavity is strict: Brunn--Minkowski equality would require homothetic lenses, whereas their axial-to-transverse halfwidth ratio \((1-r)/\sqrt{1-r^2}=\sqrt{(1-r)/(1+r)}\) is strictly decreasing. Accordingly \(q_n(r)=c_n(1-s_n(r))/r\) is strictly increasing on \((0,1)\).

At \(r=0\), the derivative formula yields
\[
q_n(0+)=\frac{c_n}{n}\frac{2\kappa_{n-1}}{\kappa_n}=\frac{\binom{2n}{n}^{1/n}}{n}\frac{\kappa_{n-1}}{\kappa_n}<1.
\]
For \(n=2\), this is \(\sqrt6/\pi<1\); for \(n=3\), it is \(20^{1/3}/4<1\). For \(n\ge4\), log-convexity of the gamma function gives \(\kappa_{n-1}/\kappa_n\le\sqrt{(n+1)/(2\pi)}\), whence the displayed number is smaller than \(4\sqrt{(n+1)/(2\pi)}/n\le\sqrt{5/(2\pi)}<1\). On the other hand \(q_n(1-)=c_n>1\). Continuity and strict increase give a unique \(r_n\in(0,1)\). Since \(s_n\) decreases strictly, the two-family comparison has the direction and uniqueness asserted in the finding.

**3. Strict improvement over the published ball bound.** Adding the squared inequalities defining \(C_r\) gives \(\|x\|^2+r^2\le1\); this inclusion in \(\sqrt{1-r^2}B_2^n\) is strict in volume for \(0<r<1\). Therefore \(s_n(r)<\sqrt{1-r^2}\). Put \(s_0=(c_n^2-1)/(c_n^2+1)\). Then \(r_0=c_n(1-s_0)=\sqrt{1-s_0^2}\). Because \(s_n(r_0)<s_0\), the unique \(r\) with \(s_n(r)=s_0\) is strictly smaller than \(r_0\), so the ball beats the simplex at \(s_0\). By the unique-crossing result its actual crossing satisfies \(s_n^*>s_0\).

**4. Endpoint Laplace asymptotics.** Write \(F(t)=(1-t^2)^{(n+1)/2}\) and \(I_n(r)=\int_r^1(1-t^2)^{(n-1)/2}dt\). Integration by parts gives the exact identity
\[
I_n(r)=\frac{F(r)}{(n+1)r}-\frac1{n+1}\int_r^1\frac{F(t)}{t^2}dt.
\]
On any interval \(a\le r\le b\) with \(0<a<b<1\), the last integral is between zero and \(a^{-2}I_n(r)\). Rearrangement bounds \(I_n(r)\) above by \(F(r)/((n+1)r)\) and below by this quantity divided by \(1+a^{-2}/(n+1)\). This proves a uniform relative \(O(n^{-1})\) error. The gamma ratio and this bound give
\[
\frac{2\kappa_{n-1}}{\kappa_n}=\sqrt{\frac{2n}{\pi}}\bigl(1+O(n^{-1})\bigr),\quad
\int_r^1(1-t^2)^{(n-1)/2}dt=\frac{(1-r^2)^{(n+1)/2}}{nr}\bigl(1+O(n^{-1})\bigr).
\]
Consequently, with \(S(r)=\sqrt{1-r^2}\) and \(A(r)=\sqrt{2/\pi}\,S(r)/r\),
\[
g_n(r)=A(r)n^{-1/2}S(r)^n(1+O(n^{-1})),\qquad
s_n(r)=S(r)\left(1+\frac{\log A(r)-\tfrac12\log n}{n}+O\!\left(\frac{(\log n)^2}{n^2}\right)\right).
\]
Stirling's formula yields \(c_n=2-\log(\pi n)/n+O((\log n)^2/n^2)\). Thus \(h_n(r)\) converges uniformly on compact subsets to \(h_\infty(r)=2(1-\sqrt{1-r^2})-r\), whose unique interior root is \(r_0=4/5\) with derivative \(h_\infty'(r_0)=5/3\). Uniqueness of the finite-dimensional root and opposite signs at two fixed points on either side of \(4/5\) imply \(r_n\to4/5\).

At \(r_0=4/5\), \(S(r_0)=3/5\) and \(A(r_0)=(3/4)\sqrt{2/\pi}\); substitution into the preceding expansions gives
\[
h_n(r_0)=\frac{\frac15\log n-\frac25\log\pi-\frac65\log\bigl((3/4)\sqrt{2/\pi}\bigr)}{n}+o(n^{-1}).
\]
The derivative expansion is uniform as well: the exact derivative of \(g_n\) in Step 1 and the preceding uniform integral bound imply \(g_n'(r)/(n g_n(r))=-r/(1-r^2)+O(n^{-1})\), uniformly near \(4/5\). Hence \(s_n'(r)=s_n(r)g_n'(r)/(n g_n(r))\to-r/\sqrt{1-r^2}\) uniformly, and therefore \(h_n'(r)\to h_\infty'(r)\). The mean value theorem now yields
\[
r_n-\frac45=-\frac35h_n(4/5)+o(n^{-1})
=-\frac{3}{25n}\log\!\left(\frac{512\pi n}{729}\right)+o(n^{-1}).
\]
Now \(s_n^*=1-r_n/c_n\). Substituting the expansions for \(r_n\) and \(c_n\) and simplifying gives
\[
s_n^*=\frac35+\frac1n\left[-\frac7{50}\log n+\frac1{50}\log\!\left(\frac{2^{27}}{3^{18}\pi^7}\right)\right]+o(n^{-1}).
\]
Taking \(n\log(s_n^*/(3/5))\) proves the asymptotic for \(\theta_n^*\). The entire error analysis is uniform near the interior root, not an extrapolation from fixed-dimensional numerics.

## Verification

The independent-variable formulas \(g_n(r)=I_{1-r^2}((n+1)/2,1/2)\) and the integral representation provide two numerical routes to the lens profile. The companion `verify.py` checks root uniqueness numerically on grids, agreement with exact planar overlap, the strict improvement over the published cutoff, and convergence of the rescaled large-dimensional asymptotics. Numerical checks are supplementary; all-dimensional statements follow from the proof above. Execute `python verify.py` with Python 3 and SciPy installed.

## Relationship to prior work

Martín Goñi (2026) defines the universal sharp coefficient for \(\theta\)-convolution bodies and proves exact simplex optimality on a nontrivial interval. Its Section 4.2 uses the strict containment of a ball lens inside an enclosing smaller ball to rule out the simplex coefficient for \(s\le(c_n^2-1)/(c_n^2+1)\), and observes only the limiting upper cutoff \(3/5\). The result here *does not change that global theorem*: it uses the exact overlap mass to identify the unique ball-versus-simplex crossover in each dimension, rigorously improves the explicit ball obstruction, and calculates its polynomial-in-dimension correction with an exact constant. The older convolution-body work of Alonso-Gutiérrez, Jiménez, and Villa (2011 preprint; 2013 journal) and Alonso-Gutiérrez and Martín Goñi (2023 online; 2024 journal) establishes foundational level-set inequalities and the earlier certified simplex interval; the checked statements do not give this ball-crossing calculation. Haddad (2025) studies the opposite, volume-*maximizing* planar same-body convolution question and does not supply the current minimization comparison. Classical formulae for Euclidean ball lens volumes are inputs rather than claimed discoveries.

## Limitations

No statement is made about which convex body pair actually minimizes the universal coefficient below the certified simplex-optimality interval. The two-family crossing is not shown to be the universal optimality transition; other bodies may outperform both. The strict ball obstruction applies for \(0<\theta<\theta_n^*\), not at equality, where the ball and simplex ratios coincide. The asymptotic is for dimensions \(n\to\infty\), while the exact implicit classification holds for every integer \(n\ge2\). Historical priority is provisional: older specialized lens-convolution calculations may contain a reparameterized equivalent crossover. In particular, full text of Schmuckenschläger (1992) could not be inspected using the available scholarly access; no assumption of its noncoverage is made.

## References

1. Javier Martín Goñi, *Improved Brunn--Minkowski inequality for \(\theta\)-convolution bodies*, arXiv:2610.37066, first submitted 2026-10-27, especially Theorem 1.1 and Section 4.2. https://arxiv.org/abs/2610.37066
2. David Alonso-Gutiérrez and Javier Martín Goñi, *Brunn--Minkowski Inequality for \(\theta\)-Convolution Bodies via Ball's Bodies*, Journal of Geometric Analysis 34:58 (2024), published online 2023-12-29, DOI:10.1007/s12220-023-01508-2. https://link.springer.com/article/10.1007/s12220-023-01508-2
3. David Alonso-Gutiérrez, C. Hugo Jiménez, and Rafael Villa, *Brunn--Minkowski and Zhang inequalities for Convolution Bodies*, arXiv:1112.4757 (2011), Advances in Mathematics 238 (2013), 50--69. https://arxiv.org/abs/1112.4757
4. C. A. Rogers and G. C. Shephard, *The difference body of a convex body*, Archiv der Mathematik 8 (1957), 220--233.
5. J. Haddad, *On the volume of convolution bodies in the plane*, Journal of Geometric Analysis 35:314 (2025), DOI:10.1007/s12220-025-02143-9. https://doi.org/10.1007/s12220-025-02143-9
6. M. Schmuckenschläger, *The distribution function of the convolution square of a convex symmetric body in \(\mathbb R^n\)*, Israel Journal of Mathematics 78 (1992), 309--334. DOI:10.1007/BF02808061 (full text not inspected).
