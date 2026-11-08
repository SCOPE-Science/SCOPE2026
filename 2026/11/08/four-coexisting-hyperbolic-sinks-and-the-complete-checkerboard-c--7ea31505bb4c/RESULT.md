# Four coexisting hyperbolic sinks and the complete checkerboard census in a Gumowski–Mira ring

## Finding

For every **even integer** \(N\ge 2\), at the explicit parameter corner
\[
(a,b,\mu,\varepsilon)=\left(\frac{33}{100},\frac1{10},-\frac35,\frac3{10}\right),
\]
the nearest-neighbor Gumowski–Mira ring has **at least four distinct hyperbolically attracting equilibria**: the two homogeneous states \((x_i,y_i)=(1,0)\) and \((-1,0)\), and the two translations of one nonzero, antisymmetric checkerboard state. More precisely, **all** nonzero checkerboard equilibria of the form \((x_i,y_i)=(-1)^i(u,v)\) are exactly the four states given by two positive roots of
\[
Q(z)=3696z^4-136463z^3-161162z^2+27929z+78500.
\]
There is one root \(z_-\in(5/8,63/100)\), generating two attracting checkerboards, and one root \(z_+\in(38,39)\), generating two unstable checkerboards. The attracting checkerboard multipliers have modulus \(\sqrt{D(z_-)}<1\) on *every* spatial Fourier mode, independent of \(N\). The four sinks persist for all sufficiently small perturbations of the four common model parameters, with a common parameter neighborhood for every even \(N\).

## Assumptions and scope

The map acts on real states \((x_i,y_i)\), indexed modulo the even ring length \(N\). Define
\[
f(x)=\mu x+\frac{2(1-\mu)x}{1+x^2},\qquad
p(y)=(1+a)y-ab y^3.
\]
Its simultaneous update is
\[
X_i=(1-\varepsilon)\bigl[p(y_i)+f(x_i)\bigr]+\frac{\varepsilon}{2}(x_{i-1}+x_{i+1}),
\qquad
Y_i=-x_i+f(X_i).
\]
For \(N=2\), both neighbors coincide; the formula remains valid. A *nonzero antisymmetric checkerboard equilibrium* means a fixed point with \((x_i,y_i)=(-1)^i(u,v)\) and \(u\ne0\). Here \(y_i\) is allowed to have either sign; no state-space truncation is imposed. An *attracting equilibrium* is strictly linearly asymptotically stable in the full \(2N\)-dimensional system; hyperbolicity and local open basins follow from its spectral radius being less than one.

## Proof

**1. Exact scalar reduction and exhaustive checkerboard count.** Put \(z=u^2\) and
\[
g(z)=\mu+\frac{2(1-\mu)}{1+z}=\frac{13-3z}{5(1+z)}.
\]
The \(Y\)-fixed-point equation gives \(v=f(u)-u=u[g(z)-1]\). The two neighbors of an alternating site both have first coordinate \(-u\), so the \(X\)-fixed-point equation becomes
\[
(1+\varepsilon)u=(1-\varepsilon)[p(v)+f(u)].
\]
Dividing by the nonzero \(u\) and substituting the displayed parameters, this is exactly \(H(z)=0\), where
\[
H(z)=(1-\varepsilon)\bigl[(1+a)(g(z)-1)-abz(g(z)-1)^3+g(z)\bigr]-(1+\varepsilon).
\]
Direct rational expansion gives the polynomial identity
\[
(1+z)^3H(z)=\frac{2}{78125}Q(z).
\]
Thus positive checkerboard amplitudes correspond bijectively to positive roots of \(Q\), each giving the two signs \((u,v)\) and \((-u,-v)\). The exact sign tests
\[
Q(5/8)>0>Q(63/100),\qquad Q(38)<0<Q(39)
\]
give at least two distinct positive roots. The coefficient signs of \(Q\), in descending order, are \((+,-,-,+,+)\), with precisely two changes, so Descartes' rule of signs gives **at most two** positive roots counted with multiplicity. Both roots are therefore simple and lie in the stated disjoint intervals. This exhausts the claimed checkerboard class.

**2. The full ring Jacobian, not only the two-site restriction.** Because \(f\) and \(p\) are odd, their derivatives are even and identical on both checkerboard sublattices. Set
\[
F(z)=f'(\sqrt z)=-\frac35+\frac{16}{5}\frac{1-z}{(1+z)^2},
\quad
V(z)=z[g(z)-1]^2=\frac{64z(1-z)^2}{25(1+z)^2},
\]
\[
D(z)=(1-\varepsilon)p'(v)=\frac7{10}\left(\frac{133}{100}-\frac{99}{1000}V(z)\right).
\]
For a spatial Fourier frequency \(q=\cos(2\pi k/N)\in[-1,1]\), linearization of the \(X,Y\)-update gives the exact block
\[
J_q(z)=\begin{pmatrix}
(1-\varepsilon)F(z)+\varepsilon q&D(z)\\
-1+F(z)[(1-\varepsilon)F(z)+\varepsilon q]&F(z)D(z)
\end{pmatrix}.
\]
Therefore
\[
\det J_q(z)=D(z),\qquad
\operatorname{tr}J_q(z)=F(z)[1-\varepsilon+D(z)]+\varepsilon q.
\]
The real Fourier cosine values include every mode, and complex modes combine into real invariant spaces. Hence stability of every \(J_q\) is necessary and sufficient for full-ring linear stability.

**3. Exact stability inequalities for the inner pair.** On \(5/8\le z\le63/100\), differentiation gives
\[
F'(z)=\frac{16}{5}\frac{z-3}{(1+z)^3}<0,
\qquad -\frac4{25}<F(z)<-\frac7{50}.
\]
Also \(V(z)\ge0\), and the monotone elementary envelope
\[
V(z)\le \frac{63}{100}\frac{64}{25}
 \left(\frac{1-5/8}{1+5/8}\right)^2<\frac9{100}
\]
implies \(9/10<D(z)<19/20\). For all \(-1\le q\le1\) this gives
\[
|\operatorname{tr}J_q|<\frac4{25}\left(\frac7{10}+\frac{19}{20}\right)+\frac3{10}
=\frac{141}{250},\qquad
\left(\frac{141}{250}\right)^2<4\cdot\frac9{10}<4D.
\]
Thus both eigenvalues of every \(J_q(z_-)\) form a complex conjugate pair of common modulus \(\sqrt{D(z_-)}<\sqrt{19/20}<1\). The same argument applies to either checkerboard translation.

**4. The outer checkerboards are unstable.** For \(z\ge38\),
\[
V(z)=\frac{64}{25}z\left(\frac{z-1}{z+1}\right)^2
\ge\frac{64}{25}\,38\left(\frac{37}{39}\right)^2>50,
\]
so \(D(z)<(7/10)[133/100-(99/1000)50]<-1\). Since \(\lvert\det J_q\rvert>1\), at least one of the two modal eigenvalues lies outside the closed unit disk. Every outer checkerboard is therefore unstable.

**5. Two further homogeneous sinks.** Because \(f(\pm1)=\pm1\) and \(p(0)=0\), the spatially homogeneous states \((x_i,y_i)=(\pm1,0)\) are exact fixed points. At either state \(f'(\pm1)=-3/5\) and
\[
D_0=(1-\varepsilon)p'(0)=\frac{931}{1000}.
\]
The Fourier blocks have determinant \(D_0\) and trace \(-\frac35(\frac7{10}+D_0)+\frac3{10}q\). The bound
\[
|\operatorname{tr}J_q|\le\frac35\left(\frac7{10}+D_0\right)+\frac3{10}
=\frac{6393}{5000},\qquad
\left(\frac{6393}{5000}\right)^2<4D_0
\]
shows conjugate multipliers of modulus \(\sqrt{931/1000}<1\) on every Fourier mode. These two states are distinct from the checkerboards, so the system has at least four disjoint nonempty open basins of attraction.

**6. Uniform local persistence.** The checkerboard root \(z_-\) is simple, hence the two opposite-sign checkerboard branches continue locally by the analytic implicit-function theorem when \((a,b,\mu,\varepsilon)\) varies. The homogeneous \(\pm1\) states continue as fixed points because \(f_\mu(\pm1)=\pm1\) at every \(\mu\) and \(p_{a,b}(0)=0\). All eigenvalue bounds above are strict, and the possible Fourier parameters remain in the fixed compact interval \([-1,1]\) for *every* even \(N\). Continuity on this compact set supplies a common open parameter neighborhood preserving strict stability of all four branches for all even ring lengths.

## Verification

Run `python verify.py` with Python 3, SymPy, and NumPy. It checks the displayed polynomial identity in exact rational arithmetic, exact rational root brackets and derivative/stability bounds, as well as the full original fixed-point equations and Fourier-block eigenvalues for five even ring sizes up to \(N=50\), totaling 20 distinct state configurations and 288 modal checks. The finite tests are corroboration; the all-ring result follows from the scalar-polynomial argument and uniform analytic inequalities.

## Relationship to prior work

Fatoyinbo and Ghosh introduced the precise ring model and surveyed synchronization and cluster regimes numerically at the two local parameter cases, including the Case-B parameters and the control ranges used here [1]. Their article, including its results, conclusion, and supplementary diagnostics, does not provide the present exact antisymmetric checkerboard equilibrium census or a four-way hyperbolic-sink coexistence theorem. An earlier analysis titled *Parity-selective equilibrium stabilization in a coupled Gumowski–Mira ring* addresses the **three homogeneous equilibria**, including the fact that the homogeneous \(\pm1\) states can both be attracting. That earlier homogeneous statement is not claimed here as an original discovery. The new content is the **two additional nonhomogeneous checkerboard sinks**, complete four-state checkerboard census, their full-mode linear stability, and hence the four-way coexistence within the exact published model. The earlier Ambika–Ambika analysis [3] uses a quadratic-numerator historical Gumowski–Mira variant and additive mutual two-site coupling, so its synchronization analysis does not imply the present antisymmetric fixed states of the odd-numerator ring. Periodic traveling waves of other lattice maps likewise do not imply the present stationary two-color fixed states or their spectra.

## Limitations

The exact checkerboard classification is restricted to *antisymmetric* spatial period-two configurations and the specified rational parameter corner; additional equilibria or attractors are not excluded. The four attracting equilibria are locally, not globally, attracting. The stability and four-way coexistence conclusions extend only to a sufficiently small common parameter neighborhood, not across the full published two-parameter region. Nothing is concluded about longer temporal cycles, stochastic perturbations, or basin volumes. Earlier literature may require further independent priority evaluation; independent scientific validation has not been performed.

## References

[1] H. O. Fatoyinbo and I. Ghosh, *Collective Phase Reorganization and Cluster Synchronization in Networks of Coupled Gumowski–Mira Maps*, arXiv:2607.03686v1, first posted 2026-07-04, https://arxiv.org/abs/2607.03686.

[2] *Parity-selective equilibrium stabilization in a coupled Gumowski–Mira ring*, mathematical research record, October 2026, publicly accessible in the published-finding corpus mathematical findings archive.

[3] G. Ambika and K. Ambika, *Intermittency and Synchronisation in Gumowski-Mira Maps*, arXiv:nlin/0606005v1, first posted 2006-06-01, https://arxiv.org/abs/nlin/0606005.
