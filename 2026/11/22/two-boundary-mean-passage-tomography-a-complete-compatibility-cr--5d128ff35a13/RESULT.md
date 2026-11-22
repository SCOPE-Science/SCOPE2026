# Two-boundary mean-passage tomography: a complete compatibility criterion and sharp instability

## Finding
Consider two experiments that retain the same interior one-dimensional diffusion dynamics but exchange which endpoint absorbs and which reflects. The complete functions of starting point giving the two mean passage times determine both the spatial diffusivity and the drift, even when neither is known beforehand. There is an exact necessary-and-sufficient compatibility condition on the observed pair, an explicit recovery of the equilibrium density, and a sharp obstruction to robust recovery from only one spatial derivative.

More precisely, for a compact interval \([0,L]\), let \(F(x)\) be the mean time to hit \(0\) while \(L\) reflects, and let \(G(x)\) be the mean time to hit \(L\) while \(0\) reflects. Define the oriented slopes and their sum and ratio by
\[
a(x)=F'(x),\qquad b(x)=-G'(x),\qquad S(x)=a(x)+b(x),\qquad q(x)=\frac{a(x)}{S(x)}.
\]
The pair is realized by a unique drift \(\mu\in C^1([0,L])\) and a unique strictly positive diffusivity \(D\in C^1([0,L])\) precisely under the compatibility assumptions below. Then
\[
\boxed{D(x)=-\frac1{S(x)q'(x)},\qquad
\mu(x)=-D(x)\frac{S'(x)}{S(x)},\qquad
\pi(x)=-q'(x).}
\]
Here \(\pi\) is the normalized zero-current stationary probability density of the diffusion when both endpoints reflect. In particular, \(q\) is the upper-tail probability of that stationary distribution.

This identification is **ill-conditioned at order one derivative**. There are strictly elliptic zero-drift diffusion coefficients \(D_n\) bounded above and below uniformly in \(n\), whose two MFPT curves converge to the standard Brownian pair in \(C^1\), but \(D_n\) remain a fixed positive distance from the constant Brownian diffusivity in uniform norm. A single left-absorbing MFPT curve has infinitely many smooth drift/diffusivity realizations.

## Assumptions and scope
Fix \(L>0\). The process is a regular reflected Itô diffusion in the closed interval, with interior stochastic equation
\[
 dX_t=\mu(X_t)\,dt+\sqrt{2D(X_t)}\,dW_t,
\]
with the usual instantaneous normal reflection at the reflecting endpoint; the coefficient \(D\) is strictly positive. The backward generator is \(\mathcal Lf=Df''+\mu f'\), not the Fick-form generator \((Df')'+\mu f'\). Thus the chosen stochastic convention is essential. Both experiments use the same interior coefficients. All passage times are measured from deterministic starting positions, and each absorbing endpoint is hit in finite mean time.

Let prescribed \(F,G\in C^3([0,L])\). The complete compatibility criterion is:

1. Endpoint data: \(F(0)=0\), \(F'(L)=0\), \(G(L)=0\), \(G'(0)=0\).
2. Oriented slopes: \(F'(x)>0\) for \(0\le x<L\), \(-G'(x)>0\) for \(0<x\le L\), and hence \(S(x)>0\) throughout \([0,L]\).
3. Strict slope-ratio decrease: \(q'(x)<0\) for every \(x\in[0,L]\) (one-sided endpoint derivatives).

No supplementary normalization constraint is required: automatically \(q(0)=1\) and \(q(L)=0\). This is an exact characterization for the stated smooth class, not a statistical inference guarantee from sparse or noisy profiles. The regularity assumptions can be weakened, but that is not claimed here.

## Proof
**Backward equations and necessity.** Denote \(a=F'\), \(b=-G'\). The two reflecting-to-absorbing backward boundary-value problems have the same right-hand side \(-1\):
\[
 D F''+\mu F'=-1,\quad F(0)=0,\ F'(L)=0,
\]
\[
 D G''+\mu G'=-1,\quad G(L)=0,\ G'(0)=0.
\]
Consequently
\[
 Da'+\mu a=-1,\qquad Db'+\mu b=+1.
\]
Adding gives \(DS'+\mu S=0\). Writing \(a=qS\) in the first identity and using the sum gives \(DSq'=-1\). This proves the recovery formulas and \(q'<0\). Standard integrating-factor solutions of the scalar backward equations with one absorbing and one reflecting endpoint give \(a>0\) away from the absorbing-side derivative zero and \(b>0\) away from its opposite endpoint, including their stated one-sided positivity.

**Sufficiency and uniqueness.** Conversely, assume the compatibility conditions. The displayed formulas define a positive \(C^1\) diffusivity and a \(C^1\) drift. Compactness and strict positivity yield uniform ellipticity. They satisfy \(DS'+\mu S=0\) and \(DSq'=-1\); therefore \(Da'+\mu a=-1\), \(Db'+\mu b=+1\), and \(DG''+\mu G'=-1\). The prescribed boundary conditions are exactly those of the respective passage-time problems, and uniqueness of the regular second-order mixed Dirichlet–Neumann boundary-value problems identifies \(F,G\) with their MFPT solutions. The same equations show every realizing coefficient pair must equal the displayed reconstruction pointwise.

**Stationary density.** With both ends reflecting, zero stationary probability flux means \((D\pi)'=\mu\pi\). Setting \(\pi=-q'=1/(DS)\) yields \(D\pi=1/S\), so both sides equal \(-S'/S^2\). Its integral is \(-\int_0^Lq'(x)\,dx=q(0)-q(L)=1\). Thus \(\pi\) is the unique normalized reflecting-stationary density and \(q(x)=\int_x^L\pi(y)\,dy\).

**One-profile ambiguity.** On \([0,1]\), the standard Brownian left-absorbing MFPT is \(F(x)=x-x^2/2\). Given *any* smooth \(h\) and nonzero sufficiently small real \(\varepsilon\), set
\[
 D_\varepsilon(x)=1+\varepsilon(1-x)h(x),\qquad \mu_\varepsilon(x)=\varepsilon h(x).
\]
Then \(D_\varepsilon F''+\mu_\varepsilon F'=-1\), with \(F(0)=F'(1)=0\). Infinitely many distinct admissible coefficient pairs therefore share this entire single directional MFPT profile. Choosing \(h(0)=h(1)=0\) even preserves the endpoint diffusivities.

**Quantified inverse instability.** Fix any \(0<c<1\), work on \([0,1]\), and define
\[
 S_n(x)=1,\quad q_n(x)=1-x+\frac{c}{n\pi}\sin(n\pi x),\quad
 D_n(x)=\frac1{1-c\cos(n\pi x)},\quad \mu_n(x)=0
\]
for integers \(n\ge1\). Because \(q_n'=-1+c\cos(n\pi x)<0\), all compatibility conditions hold with
\[
 F_n(x)=\int_0^xq_n(y)\,dy,\qquad
 G_n(x)=\int_x^1[1-q_n(y)]\,dy.
\]
Their limiting Brownian counterparts are \(F_0(x)=x-x^2/2\), \(G_0(x)=(1-x^2)/2\). Direct integration gives \(\|F_n-F_0\|_{C^1}+\|G_n-G_0\|_{C^1}=O(n^{-1})\). Yet \(D_n(0)=1/(1-c)\), so
\[
 \|D_n-1\|_\infty\ge\frac{c}{1-c}>0.
\]
All \(D_n\) obey the common ellipticity bounds \(1/(1+c)\le D_n\le1/(1-c)\). Thus no continuous inverse from the \(C^1\) pair of passage profiles to \(L^\infty\) diffusivity exists on this uniformly elliptic class. This does not assert instability under stronger \(C^2\) data norms.

## Verification
The accompanying `checker.py` verifies the defining reconstruction equations symbolically for abstract differentiable \(S,q\), checks the exact nonconstant-diffusivity example \(D(x)=1+x\) with zero drift, checks the continuum of single-profile aliases symbolically, evaluates six high-frequency instability witnesses, and compares reconstructed MFPTs with four independently solved numerical mixed-boundary-value problems for nonconstant diffusivity and drift. Execute with Python, NumPy, SymPy, and SciPy by running `python checker.py`. Numerical agreement illustrates rather than substitutes for the analytic proof.

An explicit exact example is \(D(x)=1+x\), \(\mu(x)=0\) on \([0,1]\), for which
\[
 a(x)=\log\frac2{1+x},\quad b(x)=\log(1+x),\quad S=\log2,
 \quad\pi(x)=\frac1{(1+x)\log2}.
\]
The formulas recover these coefficients without presupposing their form.

## Relationship to prior work
Keidar, Reuveni, and Sokolov (arXiv:2611.03831v1, first submitted 2026-11-02) establish inverse realization for **one mean-time profile on a half-line with constant diffusivity**, with a distinct integrability restriction at infinity. Their force reconstruction and its underlying backward equation are foundational, not claimed as new here. Bal and Chou (2004) investigate reconstructing drift or diffusion from **the entire first-exit-time distribution at a fixed starting point** subject to partial prior knowledge and discuss the classical scale/speed inverse framework. Established diffusion theory also identifies scale and speed densities from exit probabilities and mean exit-time data. The contribution here is the different **pair of opposite reflecting-to-absorbing mean profiles**: its complete realizability conditions, explicit simultaneous recovery of two spatial coefficient functions, stationary-density identity, and explicit \(C^1\)-ill-posedness. No assertion is made that the scale/speed method or backward equations themselves are new.

## Limitations
The two experimental profiles must correspond to identical interior Itô dynamics despite opposite boundary conditions. Data must be complete smooth functions; noisy discrete samples generally require differentiation/regularization, and the instability construction demonstrates a genuine obstruction in the \(C^1\) topology. The result does not apply without alteration to multidimensional diffusions, non-Markovian motion, partially transmitting boundaries, or a different stochastic calculus convention. The formulas are algebraically compatible with classical scale/speed theory; an equivalent paired-profile formulation outside the inspected literature cannot be ruled out and should be checked before publication claims.

## References
1. T. D. Keidar, S. Reuveni, and I. M. Sokolov, *The Inverse Mean First-Passage Time Problem*, arXiv:2611.03831v1 (2026-11-02), https://arxiv.org/abs/2611.03831.
2. G. Bal and T. Chou, *On the reconstruction of diffusions from first-exit time distributions*, *Inverse Problems* **20** (2004), 1053–1065, https://doi.org/10.1088/0266-5611/20/4/004.
3. M. Abundo, *One-dimensional reflected diffusions with two boundaries and an inverse first-hitting problem*, arXiv:1405.5333 (2014), https://arxiv.org/abs/1405.5333. This reference concerns inversion of the **starting-position distribution**, not joint drift and diffusivity from the two mean curves.
