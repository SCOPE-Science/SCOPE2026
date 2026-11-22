# A sharp bifurcation of worst BV errors for periodic implicit-Euler heat smoothing

## Finding
For real bounded-variation data on the unit circle, the implicit-Euler heat step \(R_t=(I-t\partial_x^2)^{-1}\) has a sharp, exactly computable \(BV\)-variation-to-\(L^2\) approximation-error constant at every \(t>0\). The unique shorter worst arc has an interior length less than one half at small times, but becomes exactly a semicircle after an explicit critical time:
\[
 a_c\coth a_c=3,\qquad t_c=\frac1{4a_c^2}=0.028063207218264555\ldots.
\]
This is a genuine optimizer bifurcation, not merely a change of an error estimate.

Write \(\lambda=\sqrt t\), \(a=1/(2\lambda)\), and define \(z_t\) as follows. For \(t\ge t_c\) take \(z_t=0\) and \(s_t=1/2\). For \(0<t<t_c\), let \(z_t\in(0,a)\) be the unique root
\[
 z_t\coth z_t=a\coth a-2,\qquad s_t=\frac12-\lambda z_t.
\]
Then the **exact sharp squared constant** is
\[
 \boxed{C(t)^2=\frac{\lambda}{8\sinh a}
 \left[a\sinh a-z_t\sinh z_t+
 (a\coth a-1)(\cosh z_t-\cosh a)\right].}
\]
All nonconstant equality functions are \(b+c\mathbf1_I\) with \(b\in\mathbb R\), \(c\ne0\), and \(I\) any rotated arc of length \(s_t\) or \(1-s_t\); there are no other equality functions modulo almost-everywhere equality.

The sharp limiting laws are
\[
 \frac{s_t}{\sqrt t}\longrightarrow2,\qquad
 \frac{C(t)^2}{\sqrt t}\longrightarrow\frac{1+e^{-2}}8
 =0.14191691040457659\ldots\quad(t\downarrow0),
\]
\[
 \frac{1/2-s_t}{\sqrt{t_c-t}}
 \longrightarrow\sqrt{\frac32(a_c^2-6)}
 =2.0887058655503873\ldots\quad(t\uparrow t_c).
\]

## Assumptions and scope
Here \(\mathbb T=\mathbb R/\mathbb Z\) has normalized Lebesgue measure. The domain is the real space \(BV(\mathbb T)\) of equivalence classes with finite distributional derivative measure, and \(V(f)=|Df|(\mathbb T)\) is full *circular* Jordan variation, including any jump across the choice of origin. We restrict \(V(f)>0\), since constants are annihilated by \(I-R_t\). The Laplacian \(\partial_x^2\) is periodic. No assumptions of absolute continuity, smoothness or finitely many jumps are made. The parameter \(t\) is any fixed positive real number.

## Proof
**1. From arbitrary BV data to a single arc.** Let \(\mu=Df\), a finite real signed measure with \(\mu(\mathbb T)=0\). Its positive and negative parts both have mass \(V(f)/2\). Let \(G_t\) be the periodic convolution kernel of \(R_t\), and set \(K_t=-tG_t'\). A Fourier differentiation or distributional calculation gives \((I-R_t)f=K_t*\mu\). For any coupling \(\pi\) of the positive and negative parts of \(\mu\),
\[
 K_t*\mu=\iint\bigl(K_t(\cdot-u)-K_t(\cdot-v)\bigr)\,d\pi(u,v).
\]
The Bochner triangle inequality implies
\[
 \frac{\|(I-R_t)f\|_2^2}{V(f)^2}
 \le\frac14\max_{u,v\in\mathbb T}
 \|K_t(\cdot-u)-K_t(\cdot-v)\|_2^2.
\]
Equality is attained by a signed derivative \(\mu=c(\delta_u-\delta_v)\), corresponding to an arc indicator. Thus the sharp problem reduces **exactly**, with no finite-support assumption, to optimizing the length of one circular arc. Every nonzero Fourier coefficient of \(K_t\) is nonzero. If two maximal chords of its translate curve are equal as vectors, their associated two-atom signed measures have identical nonzero Fourier coefficients; their difference is both atomic and a constant multiple of Lebesgue measure, hence zero. Strict equality in the Hilbert triangle inequality therefore forces one ordered pair. This proves the asserted rigidity of all equality cases, once the best lengths are classified.

**2. Exact periodic Green kernel and objective.** Put \(\lambda=\sqrt t\), \(a=1/(2\lambda)\). For \(0\le s\le1/2\),
\[
 G_t(s)=\frac{\cosh((1/2-s)/\lambda)}{2\lambda\sinh a}.
\]
Indeed this is the unique periodic distributional solution of \((I-t\partial_x^2)G_t=\delta_0\). Write \(H_t=G_t*G_t\). The Fourier multipliers give \(H_t=G_t+t\partial_tG_t\). Since \(G_t\) is even and \(H_t\in C^2(\mathbb T)\),
\[
 E_t(s):=\|(I-R_t)\mathbf1_{(0,s)}\|_2^2
 =2t^2\bigl(H_t''(s)-H_t''(0)\bigr).
\]
This follows by writing the residual as the difference of two translates of \(-tG_t'\) and integrating its square. Consequently \(C(t)^2=\max_{0\le s\le1/2}E_t(s)/4\). For \(0<s<1/2\), differentiation of the explicit Green function, or the identity \(H_t''=(\partial_\lambda G_t)/(2\lambda)\), gives, with \(z=(1/2-s)/\lambda\),
\[
 \frac{d}{ds}\frac{E_t(s)}4
 =\frac{z\cosh z+(2-a\coth a)\sinh z}{8\sinh a}.
\]
Integrating from \(s=0\), where \(E_t(0)=0\), gives the boxed closed form with \(z=(1/2-s)/\lambda\).

**3. Global optimizer, uniqueness and transition.** The function \(h(u)=u\coth u\) is strictly increasing on \((0,\infty)\), with \(h(0+)=1\), since \(h'(u)=(\sinh u\cosh u-u)/\sinh^2u>0\). For \(0<s<1/2\), the sign of the last derivative is exactly the sign of \(h(z)+2-h(a)\), because \(\sinh z>0\). If \(h(a)\le3\), this sign is positive throughout the open half-circle, and the unique maximizing shorter length is \(1/2\). If \(h(a)>3\), there is a unique \(z_t\in(0,a)\) solving \(h(z_t)=h(a)-2\). As \(s\) increases from zero to one half, \(z\) decreases from \(a\) to zero; the derivative changes from positive to negative exactly once. Therefore \(s_t=1/2-\lambda z_t\) is the unique global maximizer on \([0,1/2]\). Because \(h(a)\) increases from \(1\) to infinity and \(a\) decreases with \(t\), exactly one transition exists, at \(h(a_c)=3\).

**4. The small-time and critical laws.** As \(t\downarrow0\), \(a\to\infty\) and \(h(u)=u+O(ue^{-2u})\) at large \(u\). The unique root equation thus gives \(z_t=a-2+o(1)\) and \(s_t/\lambda\to2\). Substitution in the closed form, equivalently the real-line exponential Green-kernel limit, yields \(C(t)^2/\lambda\to(1+e^{-2})/8\). At the transition, \(z\coth z=1+z^2/3+O(z^4)\). Writing \(\delta=t_c-t\), one gets
\[
 h(a)-3=\frac{h'(a_c)a_c}{2t_c}\delta+O(\delta^2),
 \qquad z_t^2=3(h(a)-3)+O((h(a)-3)^2).
\]
At the root \(h'(a_c)=(a_c^2-6)/a_c\), which is positive. Since \(\lambda\to1/(2a_c)\), the claimed square-root coefficient follows. All limits are single-parameter limits with the circle length fixed at one.

## Verification
The accompanying \(verify.py\) uses the exact hyperbolic formula and an independent Fourier-series representation
\[
 C_t(s)^2=\sum_{k=1}^{\infty}
 \frac{1-\cos(2\pi ks)}{(2\pi k)^2}
 \left(\frac{4\pi^2tk^2}{1+4\pi^2tk^2}\right)^2.
\]
The omitted positive tail after \(N\) terms is at most \(1/(2\pi^2N)\). Executing the file checks the critical root, the unique optimizer equation, numerical agreement at 36 sample pairs, and both limiting coefficients. This finite checking is supplementary; the full-theorem proof is the measure-coupling and explicit derivative-sign argument above.

## Relationship to prior work
The 2005 public manuscript record of Miranda, Pallara, Paronetto and Preunkert (published 2007) develops heat-semigroup characterizations of BV via \(L^1\) gradients on manifolds and includes a resolvent regularity argument. Its statement neither uses the periodic \(L^2\) identity-resolvent error nor optimizes its jump geometry. Kovács, Larsson and Lindgren (2013) analyze backward-Euler convergence for a stochastic Allen–Cahn equation by Sobolev and strong-error estimates, not a sharp deterministic variation error for a single periodic resolvent step. General heat, fractional heat and Steklov smoothers have different spectral multipliers; their individually optimized constants do not determine this problem's mixed-frequency quadratic error. The exact threshold \(a\coth a=3\) and global semicircle bifurcation depend on the periodic second-order resolvent kernel.

## Limitations
The result covers one spatial circle, the constant-coefficient periodic Laplacian, real BV data, the *single-step* backward-Euler resolvent, and ordinary unweighted \(L^2\) error. It makes no assertion about Neumann or Dirichlet boundaries, multiple time steps, variable coefficients, higher dimensions, or other resolvent powers. Historical-priority claims are necessarily conditional on accessible primary literature; the proof does not establish that an unindexed equivalent result cannot exist.

## References
1. M. Miranda Jr., D. Pallara, F. Paronetto, M. Preunkert, *Heat semigroup and functions of bounded variation on Riemannian manifolds*. Public repository record created 18 November 2005; J. Reine Angew. Math. 613 (2007), 99–119. https://cvgmt.sns.it/paper/376/ ; DOI: 10.1515/CRELLE.2007.093.
2. M. Kovács, S. Larsson, F. Lindgren, *On the backward Euler approximation of the stochastic Allen–Cahn equation*, first posted 8 November 2013. https://arxiv.org/abs/1311.2067.
