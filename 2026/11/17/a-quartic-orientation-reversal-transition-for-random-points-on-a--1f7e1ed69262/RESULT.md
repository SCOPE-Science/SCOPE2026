# A quartic orientation-reversal transition for random points on a circular helix

## Finding
Let \(T_1,T_2,T_3,T_4\) be independent uniform samples on \([0,L]\), with order statistics \(t_1<t_2<t_3<t_4\). Embed them on the unit-radius, unit-pitch circular helix \(\gamma(t)=(\cos t,\sin t,t)\). Write
\[
D(t_1,t_2,t_3,t_4)=\det\begin{pmatrix}1&t_1&\cos t_1&\sin t_1\\1&t_2&\cos t_2&\sin t_2\\1&t_3&\cos t_3&\sin t_3\\1&t_4&\cos t_4&\sin t_4\end{pmatrix}.
\]
This is six times the oriented tetrahedral volume, with a fixed coordinate convention. For \(0<L\le2\pi\) it is positive almost surely. For \(L=2\pi+\varepsilon\), \(\varepsilon\downarrow0\),
\[
\Pr(D<0)=\frac{\varepsilon^4}{4\pi^4}+o(\varepsilon^4).
\]
Furthermore, conditional on \(D<0\), the scaled ordered times
\[
X_\varepsilon=\left(t_1/\varepsilon,t_2/\varepsilon,(t_3-2\pi)/\varepsilon,(t_4-2\pi)/\varepsilon\right)
\]
converge in total variation to uniform Lebesgue measure on the four-dimensional region
\[
\mathcal R=\{(x_1,x_2,x_3,x_4):0<x_1<x_2,\ x_3<x_4<1,\ x_3+x_4>x_1+x_2\},
\qquad \operatorname{vol}_4(\mathcal R)=1/6.
\]
The limiting midpoint \((x_1+x_2)/2\) has density \(12a(1-a)^2\) for \(0<a<1\), a \(\operatorname{Beta}(2,3)\) law.

## Assumptions and scope
The four sample parameters are independent with uniform (parameter, not arclength-normalized) distribution on \([0,L]\). On the unit-radius, unit-pitch helix the speed is constant, so uniform parameter and uniform arclength coincide. The event uses the fixed increasing-parameter order; it does not assert an unsigned volume distribution. All asymptotics are for the length approaching one full turn from above with fixed helix radius and pitch.

## Proof
**1. Positivity through one turn.** A plane through four distinct points on the helix would yield four zeros of \(f(t)=A+Bt+C\cos t+E\sin t\). Unless the function is identically zero (impossible for independent functions), Rolle's theorem requires at least three zeros of \(f'(t)=B-C\sin t+E\cos t\). Three distinct zeros of a nonconstant shifted sine have a span at least \(2\pi\); the constant case has none, except an identically zero derivative, which cannot give four zeros of \(f\). Therefore a determinant for four strictly increasing parameters in a window of length at most \(2\pi\) never vanishes. Its sign is positive, as follows by confluent expansion around four close parameters (positive Vandermonde with positive leading Wronskian). This also proves the only possible transition is beyond a full turn.

**2. Exact paired determinant.** Set \(t_1=m-h,t_2=m+h,t_3=n-k,t_4=n+k\), with \(h,k>0\) and \(d=n-m\). Elementary row sums and differences give the exact identity
\[
D=4\sin h\sin k\,H(h,k,d),
\]
\[
H=(\cos k-\cos h)\left(\frac h{\sin h}-\frac k{\sin k}\right)
+(1-\cos d)\left(\frac{h\cos h}{\sin h}+\frac{k\cos k}{\sin k}\right)-d\sin d.
\]
Quotients at zero are interpreted by their analytic extensions. Around \(h=k=0,d=2\pi\), with \(\delta=d-2\pi\),
\[
H=-2\pi\delta+O\left(\delta^2+(h^2+k^2)|\delta|+(h^2+k^2)^2\right).
\]
At \(d=2\pi\), \(H=(\cos k-\cos h)(h/\sin h-k/\sin k)\ge0\) for small \(h,k\).

**3. Concentration at the double-endpoint configuration.** In the compact closure of ordered quadruples from \([0,2\pi]\), the confluent divided determinant is nonnegative. Its zero set among configurations permitting a sign change with the window expanded past \(2\pi\) is the endpoint double-pair configuration \((0,0,2\pi,2\pi)\). One proof uses the equality case of the preceding Rolle zero-spacing argument with multiplicities: the three derivative zeros must occupy a full period, and the only four-contact plane section at the critical span is, up to scale, \(1-\cos t\), with double zeros at the two ends. Compactness therefore localizes all negative determinants for \(L\downarrow2\pi\) there. In that neighborhood, \(H<0\) and the displayed expansion imply \(\delta\ge-C(h+k)^4\) whenever \(\delta\le0\), and in fact \(\delta>0\) throughout the negative region sufficiently near the boundary. As the total span satisfies \(d+h+k\le2\pi+\varepsilon\), it follows that \(h+k=O(\varepsilon)\), \(\delta=O(\varepsilon)\), and the endpoint constraints imply \(m=O(\varepsilon)\). Hence all four coordinates in the following rescaling stay in a fixed bounded box.

**4. Limiting sign domain and probability.** Put \(t_1=\varepsilon x_1,t_2=\varepsilon x_2,t_3=2\pi+\varepsilon x_3,t_4=2\pi+\varepsilon x_4\). Uniformly on fixed bounded rescaled boxes,
\[
D=\pi\varepsilon^3(x_1-x_2)(x_3-x_4)(x_1+x_2-x_3-x_4)+O(\varepsilon^4).
\]
Consequently the asymptotic negative-sign domain is precisely \(\mathcal R\), up to a null boundary. To compute its volume, set \(a=(x_1+x_2)/2\), \(h=(x_2-x_1)/2\), \(b=(x_3+x_4)/2\), \(k=(x_4-x_3)/2\). The domain becomes \(0<h<a<b<1\), \(0<k<1-b\); the Jacobian is \(4\). Thus
\[
\operatorname{vol}_4(\mathcal R)=4\int_0^1 a\int_a^1(1-b)\,db\,da=\frac16.
\]
The joint density of ordered points is \(24/L^4\). With Jacobian \(\varepsilon^4\) for the rescaling, the limit is
\[
\Pr(D<0)\sim\frac{24\varepsilon^4}{(2\pi)^4}\cdot\frac16=\frac{\varepsilon^4}{4\pi^4}.
\]
The rescaled, sign-restricted densities converge pointwise almost everywhere and their integrals converge to the positive finite volume above. Scheffé's lemma gives convergence in total variation after conditioning. Integrating the variables \(h,b,k\) at fixed \(a\) gives \(2a(1-a)^2\) before dividing by \(1/6\); the normalized midpoint density is \(12a(1-a)^2\).

## Verification
The standalone `CHECKER.py` checks the paired determinant against a separate direct matrix determinant, verifies the leading homogeneous expansion, checks the exact polytope volume via rational arithmetic, and numerically samples the limiting sign region. It is reproducible with Python 3 and NumPy; its finite tests corroborate but do not replace the preceding proof.

## Relationship to prior work
Musin's 2009 public preprint studies Chebyshev zero-count constraints for convex curves, an appropriate deterministic context for the one-turn sign argument, without a four-point stochastic orientation transition. Starostin and van der Heijden study the geometry of cylindrical curves and the circular helix as a model; this does not imply the precise sharp probability or the conditional four-dimensional law. The new finding concerns an orientation sign under independent arclength sampling, not the existence or classification of cylindrical helices.

## Limitations
No formula for the orientation probability at general \(L>2\pi\) is claimed. The limiting law uses fixed unit radius and unit pitch; arbitrary varying-radius helices or nonuniform sampling are outside the theorem. The original literature search is not a historical uniqueness guarantee, and no external mathematical audit has been performed.

## References
- O. Musin, *Chebyshev systems and zeros of a function on a convex curve*, arXiv:0903.1908, initial public version 2009-03-11, https://arxiv.org/abs/0903.1908.
- E. Starostin and G. van der Heijden, *Characterisation of cylindrical curves*, published online 2014-12-05, https://doi.org/10.1007/s00605-014-0705-4, lawful manuscript https://discovery.ucl.ac.uk/id/eprint/1465538/1/art_10.1007_s00605-014-0705-4.pdf.
