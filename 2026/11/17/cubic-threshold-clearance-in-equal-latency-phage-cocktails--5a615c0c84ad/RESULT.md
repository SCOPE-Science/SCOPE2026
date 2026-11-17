# Cubic threshold clearance in equal-latency phage cocktails

## Finding
For the multi-phage coinfection delay system below, suppose the bacterial invasion eigenvalue vanishes and the first nonlinear center coefficient vanishes. Set
\[
 r_i=\frac{d_i}{m_i},\quad E=e^{-\mu\tau},\quad B=\frac{\alpha(1-E)}{\mu},\quad
 A_i=k_i(1-b_i E)+h_iB,
\]
\[
 K=\sum_{i=1}^n\frac{k_i d_i A_i}{m_i^2},\qquad
 C=\sum_{i=1}^n\frac{k_i d_i A_i^2}{m_i^3}.
\]
Assume \(\alpha=\sum_i k_i d_i/m_i\) and \(K=0\). If at least one \(A_i\ne0\), then \(C>0\), the bacteria-free equilibrium is locally asymptotically stable, and every sufficiently nearby biologically compatible solution with \(S(0)>0\) satisfies
\[
 \lim_{t\to\infty}\sqrt t\,S(t)=\frac1{\sqrt{2C}},\qquad
 \lim_{t\to\infty}\frac{I(t)}{S(t)}=B,\qquad
 \lim_{t\to\infty}\frac{Q_i(t)-r_i}{S(t)}=-\frac{r_iA_i}{m_i}.
\]
If instead every \(A_i=0\), a nontrivial curve of exact positive bacterial equilibria meets the bacteria-free state, so that state is not asymptotically stable. The alternatives exhaust the second-order cancellation \(K=0\).

## Assumptions and scope
Fix an integer \(n\ge1\) and positive numbers \(\alpha,\mu,\tau,k_i,h_i,b_i,d_i,m_i\) for \(1\le i\le n\); all phage types have the same delay \(\tau\). For \(t\ge0\) solve
\[
 \begin{aligned}
 \dot S(t)&=S(t)\left(\alpha-\sum_i k_iQ_i(t)\right),\\
 \dot I(t)&=\sum_i k_i\left[Q_i(t)S(t)-E Q_i(t-\tau)S(t-\tau)\right]-\mu I(t),\\
 \dot Q_i(t)&=d_i-m_iQ_i(t)-k_iQ_i(t)S(t)-h_iQ_i(t)I(t)
                 +k_ib_i E Q_i(t-\tau)S(t-\tau).
 \end{aligned}
\]
The state comprises continuous histories for \(S,Q_i\) and the present value of \(I\). Physical compatibility requires nonnegative histories and
\[
 I(0)=\sum_i k_i\int_{-\tau}^0e^{\mu s}Q_i(s)S(s)\,ds.
\]
For local statements take histories sufficiently close in the supremum norm to the constant bacteria-free history \((S,I,Q_i)=(0,0,r_i)\). The word *locally* is essential: no global clearance is asserted. The equilibrium linearization has a simple zero eigenvalue and strictly negative remaining characteristic roots at \(\alpha=\sum_i k_i r_i\).

All conditions are achievable with strictly positive parameters. For \(n=2\), set \(\mu=1\), \(\tau=\log 2\), \(\alpha=2\), \(k_i=h_i=d_i=m_i=1\), \((b_1,b_2)=(2,6)\). Then \(B=1\), \((A_1,A_2)=(1,-1)\), \(K=0\), \(C=2\), and the exact clearance coefficient is \(1/2\).

## Proof
**1. Spectrum and center directions.** Write \(u=S\), \(v=I\), and \(q_i=Q_i-r_i\). At the critical dose the linear delay system is triangular in the order \((u,v,q_1,\ldots,q_n)\). Its characteristic equation is
\[
 \lambda(\lambda+\mu)\prod_{i=1}^n(\lambda+m_i)=0.
\]
Hence a one-dimensional smooth local center manifold exists, with exponential stable foliation. Parameterize it by the current bacterial coordinate \(u\). Solving the zero-eigenvector equations yields
\[
 I=Bu+O(u^2),\quad Q_i=r_i-\frac{r_iA_i}{m_i}u+O(u^2).
\]
Inserting this in the first equation gives the quadratic reduced coefficient
\[
 \dot u=Ku^2+O(u^3).
\]
Our assumption \(K=0\) implies \(\dot u=O(u^3)\). Consequently over the fixed delay interval, along this center manifold,
\[
 u(t-\tau)=u(t)+O(u(t)^3),\quad
 Q_i(t-\tau)=Q_i(t)+O(u(t)^3).
\]
Every estimate refers to the small center coordinate, and follows by integrating its smooth reduced vector field and the smooth center-graph derivatives over a fixed interval.

**2. The infected class has no quadratic correction.** The exact compatible-history identity is
\[
 I(t)=\sum_i k_i\int_0^\tau e^{-\mu s}Q_i(t-s)S(t-s)\,ds.
\]
Up to order \(u^2\), the retarded product equals its present value. Since
\[
 \sum_i k_iQ_i=\alpha-Ku+O(u^2)=\alpha+O(u^2),
\]
this integral gives \(I=Bu+O(u^3)\) on the center manifold. Equivalently, the difference between this convolution and \(I\) obeys the strictly stable scalar equation \(D'=-\mu D\), and therefore vanishes on the center manifold.

**3. Cubic coefficient.** Because \(\dot Q_i=O(u^3)\) along the center manifold, the phage equations through order \(u^2\) reduce to
\[
 0=d_i-(m_i+A_i u)Q_i+O(u^3).
\]
Thus
\[
 Q_i=r_i\left(1-\frac{A_i}{m_i}u+\frac{A_i^2}{m_i^2}u^2\right)+O(u^3).
\]
It follows that \(\sum_i k_iQ_i=\alpha-Ku+Cu^2+O(u^3)\). The center equation is therefore
\[
 \boxed{\dot u=-Cu^3+O(u^4)}.
\]
Strict positivity of all \(k_i,d_i,m_i\) proves \(C>0\) whenever some \(A_i\ne0\). The reduced origin is asymptotically stable from both sides. Exponential attraction of transverse directions and the reduction principle give local asymptotic stability in the full retarded phase space.

**4. Universal rate for positive bacteria.** For every positive center solution approaching zero, differentiation gives
\[
 \frac{d}{dt}\frac1{u(t)^2}=2C+O(u(t)),
\]
so \(u(t)\sqrt t\to(2C)^{-1/2}\). Standard stable-foliation tracking matches any nearby full trajectory to a center trajectory with exponentially small error in its present coordinates. The tracked center trajectory must be positive and nonzero if \(S(0)>0\): a negative nonzero center trajectory would contradict eventual positivity of \(S(t)\), whereas a zero center trajectory would force \(S(t)\) and \(Q_i(t)-r_i\) to be exponentially small. In the latter case \(\int_0^\infty|\alpha-\sum_i k_iQ_i(t)|dt<\infty\), and the exact logarithmic equation \((\log S)'=\alpha-\sum_i k_iQ_i\) would give a positive limit for \(S\), another contradiction. Thus the positive tracked center asymptotic applies. Division of the tracked center expansions by \(S(t)\) gives the stated ratios.

**5. Complete cancellation.** If every \(A_i=0\), then for every sufficiently small \(u\ge0\) the constant history
\[
 (S,I,Q_i)=(u,Bu,r_i)
\]
is an exact equilibrium: the bacterial equation vanishes by critical dosing, the infected equation by the definition of \(B\), and each phage equation by \(A_i=0\). Hence the bacteria-free state is nonisolated and not asymptotically stable. For \(n=1\), the condition \(K=0\) forces this exceptional case; the nontrivial cubic clearance needs at least two phage types.

## Verification
The algebraic witness with two phages gives \((A_1,A_2)=(1,-1)\) and \(C=2\) exactly. The accompanying `verify_phage.py` uses exact symbolic arithmetic to check the center coefficients and residual orders. A separate finite-step integration of the full delay equations, with physically compatible constant histories, gives \(\sqrt t S(t)\) values approximately \(0.46564\), \(0.47821\), and \(0.48613\) at \(t=300,600,1200\), respectively, compared with the analytical limit \(0.5\). These finite tests do not prove the limit. Run `python verify_phage.py` with Python 3 and SymPy.

## Relationship to prior work
Bardina, Cano, and Cuadrado derive the model, its compatible-history identity, the strictly hyperbolic bacterial-dose stability criteria (Proposition 5.1), and the equilibrium function for two common-latency phage types (Section 5.1). The equality case with the simultaneous cancellation of the first nonlinear coefficient is not resolved there. The equilibrium function's positive second derivative is consistent with, but is not itself a proof of, the full retarded center-manifold clearance rate. Earlier critical-dose work describes the generic nonzero quadratic coefficient and \(t^{-1}\) rate, explicitly excluding the present zero-coefficient case. General delay-equation center-manifold theory provides a method, not the particular squared-coefficient law \(C\) or its positive-parameter realization.

## Limitations
The result is deterministic and local, assumes positive parameters and common latency, and concerns the physically compatible history manifold. It gives neither a global basin description nor stochastic clearance times, and makes no claim for distinct latencies or a uniform crossover as \(K\) approaches zero. The finite DDE computation is corroborative, not independent mathematical validation.

## References
1. X. Bardina, M. Cano, S. Cuadrado, *Modelling and analysis of a cocktail phage therapy with coinfection*, arXiv:2611.08370v1 (first public 2026-11-05), https://arxiv.org/html/2611.08370v1, especially equations (2.1)–(2.3), Proposition 5.1 and Section 5.1.
2. J. K. Hale and S. M. Verduyn Lunel, *Introduction to Functional Differential Equations*, Springer, 1993 (standard retarded center-manifold and stable-foliation theory).
