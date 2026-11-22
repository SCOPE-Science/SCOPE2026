# Two resetting-rate fluctuation crossings in mortal Brownian search: a sharp noise phase diagram

## Finding

Let a one-dimensional Brownian searcher start at distance \(x>0\) from an absorbing point target, diffuse with generator \(D\partial_{xx}\) for \(D>0\), and independently reset to its initial location at Poisson rate \(r\geq 0\). The particle dies independently at exponentially distributed rate \(\mu>0\); let \(T\) denote its target-hitting time **conditioned on hitting before death**. Define

\[
 m=\frac{\mu x^2}{D},\qquad \rho=\frac{r x^2}{D},\qquad
 C_V(m,\rho)=\frac{\sqrt{\operatorname{Var}(T)}}{\mathbb E T}.
\]

There is a unique universal constant

\[
 m_c=1.10642822093643738483298618\ldots
\]

with the following **complete classification of positive resetting rates where \(C_V=1\)**:

| Dimensionless mortality \(m\) | Positive solutions of \(C_V(m,\rho)=1\) | Sign of \(C_V-1\) as \(\rho\) increases |
| --- | --- | --- |
| \(0<m<1\) | Exactly one, \(\rho_+\) | Positive, then negative |
| \(m=1\) | Exactly one, \(\rho_+\); additionally \(C_V(m,0)=1\) | Positive for \(0<\rho<\rho_+\), then negative |
| \(1<m<m_c\) | Exactly two, \(0<\rho_-<\rho_+\) | Negative, positive, negative |
| \(m=m_c\) | Exactly one double/tangential solution, \(\rho_c\) | Negative except at equality |
| \(m>m_c\) | None | Strictly negative |

In particular, **a narrow, nonempty mortality interval exhibits reentrance from below-unit to above-unit and back to below-unit relative first-passage fluctuations**, although the mortal searcher and its resetting rule remain unchanged. The tangency occurs at

\[
 \rho_c=0.28424024613180761598645935\ldots.
\]

For \(m=1.05\), the two positive crossing rates are

\[
 \rho_-=0.05874513323198482763\ldots,\qquad
 \rho_+=0.61152196303662872034\ldots.
\]

The exact characterization is as follows. Define

\[
 H(z)=(z^2-5z+8)e^z-8,\qquad
 B(z)=\frac{4z^2\bigl((2-z)e^z-2\bigr)}{H(z)},\quad z>0,
\]

and

\[
 G(z)=(z^3-10z^2+34z-32)e^{2z}
 +(-2z^3+2z^2-34z+64)e^z-32.
\]

The function \(G\) has exactly one positive zero \(z_c=1.17926607136313601347\ldots\); the above threshold is \(m_c=B(z_c)\), and \(\rho_c=z_c^2-m_c\). For every \(m>0\), all admissible crossings are obtained without spurious roots by solving

\[
 B(z)=m,\qquad z>\sqrt m,\qquad \rho=z^2-m.
\]

## Assumptions and scope

The underlying Brownian paths are continuous, the target is the point zero on the line, reset returns are instantaneous to the same positive initial location \(x\), and the independent death time has constant hazard \(\mu\). Search and resetting continue until whichever occurs first: target capture or death. Conditioning is solely on successful target capture; unsuccessful trajectories are excluded from the law of \(T\). The theorem holds for every \(D,x,\mu>0\) and all \(r\geq0\); it makes no claim about non-exponential mortality, position-dependent resets, or unconditional termination time.

The standard Brownian convention here is \(\operatorname{Var}(X_t-X_0)=2Dt\). The physical mortality threshold is \(\mu_c=m_c D/x^2\) and the physical tangent rate is \(r_c=\rho_c D/x^2\). The boundary \(r=0\) is explicitly distinguished from strictly positive rates. The limiting immortal case \(\mu=0\) is not included in the assertion.

## Proof

**1. Transform and conditional cumulants.** Without resetting, the Laplace transform of the target first-passage time is \(e^{-x\sqrt{s/D}}\). The standard renewal decomposition at the first Poisson reset gives for the corresponding immortal resetting first passage

\[
 \phi_r(s)=\frac{(r+s)e^{-x\sqrt{(r+s)/D}}}
 {s+r e^{-x\sqrt{(r+s)/D}}}.
\]

Let \(\mathcal A(s)=(e^{\sqrt{s}}-1)/s\) for \(s>0\). In dimensionless variables this becomes

\[
 \phi_\rho(q)=\frac1{1+q\mathcal A(q+\rho)}.
\]

The probability of capture before an independent exponential death clock is \(p=\phi_\rho(m)\), and the conditional Laplace transform of the successful hitting time (in units \(x^2/D\)) is exactly \(\phi_\rho(m+u)/\phi_\rho(m)\). Differentiating its logarithm at \(u=0\), with \(s=m+\rho\), yields dimensionless mean \(M\) and variance \(V\):

\[
 M=\frac{\mathcal A(s)+m\mathcal A'(s)}{1+m\mathcal A(s)},\quad
 V=M^2-\frac{2\mathcal A'(s)+m\mathcal A''(s)}{1+m\mathcal A(s)}.
\]

As the conditional hitting-time distribution is nondegenerate, \(M,V>0\). Therefore the sign of \(C_V^2-1=(V-M^2)/M^2\) is the *opposite* of the sign of \(2\mathcal A'(s)+m\mathcal A''(s)\).

**2. Exact crossing curve.** Write \(z=\sqrt{s}\). Direct differentiation gives

\[
 \mathcal A'(z^2)=\frac{(z-2)e^z+2}{2z^4},\qquad
 \mathcal A''(z^2)=\frac{(z^2-5z+8)e^z-8}{4z^6}=\frac{H(z)}{4z^6}.
\]

Since \(H(0)=0\) and \(H'(z)=e^z(z^2-3z+3)>0\) for every \(z>0\), the second derivative is strictly positive. Hence

\[
 \operatorname{sgn}(C_V^2-1)=\operatorname{sgn}(B(z)-m),
 \qquad B(z)=-\frac{2\mathcal A'(z^2)}{\mathcal A''(z^2)}.
\]

A cancellation special to the Brownian first-passage transform gives

\[
 B(z)-z^2=\frac{z^3e^z(1-z)}{H(z)}.
\]

Thus \(B(1)=1\); on \(0<z<1\), \(B(z)>z^2\), whereas on \(z>1\), \(B(z)<z^2\).

**3. Unimodality, with a global coefficient certificate.** Differentiation, with the above \(G\), yields

\[
 B'(z)=-\frac{4z G(z)}{H(z)^2}.
\]

Set \(G(z)=\sum_{n\ge0}g_n z^n/n!\). Exact expansion shows \(g_0=g_1=g_3=0\), \(g_2=-12\), and for \(n\ge4\)

\[
 g_n=\frac{2^n(n^3-23n^2+158n-256)
 -16n^3+64n^2-320n+512}{8}.
\]

For \(n=4,5,6,7,8,9,10\), these coefficients are respectively \(48,150,320,546,768,942,1536\), all positive. For every integer \(n\ge11\), let \(P(n)=n^3-23n^2+158n-256\). We have \(P(11)=30\), and \(P'(n)=3n^2-46n+158>0\) for \(n\ge11\), so \(P(n)\ge30\). Moreover \(30\cdot2^{11}>16\cdot11^3+320\cdot11\), and

\[
 2(16n^3+320n)-(16(n+1)^3+320(n+1))
 =16(n^3-3n^2+17n-21)>0
\]

for every integer \(n\ge11\). Induction gives \(30\cdot2^n>16n^3+320n\) for all such \(n\), implying \(g_n>0\). This proves positivity of **all** remaining coefficients rather than checking only finitely many of them.

Consequently

\[
 \frac{G(z)}{z^2}=-6+\sum_{n\ge4}\frac{g_n}{n!}z^{n-2}
\]

is strictly increasing from \(-6\) to \(+\infty\) on positive \(z\). Thus \(G\) has exactly one positive zero \(z_c\); \(B\) increases strictly before \(z_c\) and decreases strictly after it. Further,

\[
 G(1)=-7e^2+30e-32=-(7e-16)(e-2)<0,
\]

so \(z_c>1\). The function \((z-2)e^z+2\) has exactly one positive zero \(z_*\in(1,2)\), besides the zero at \(z=0\), because its derivative is \((z-1)e^z\). At \(z_*\), \(B(z_*)=0\) and \(B'(z_*)<0\), so \(z_c<z_*\). Also \(B(z)>0\) precisely for \(0<z<z_*\).

**4. Number of admissible intersections.** For each fixed mortality \(m>0\), the physical domain is \(z\ge\sqrt m\), and positive reset rates require \(z>\sqrt m\). If \(m<1\), then \(B(\sqrt m)>m\) and unimodality yields one strictly positive intersection on the decreasing branch. If \(m=1\), the solution \(z=1\) occurs at the excluded positive-rate boundary \(\rho=0\), with exactly one further solution. Because \(z_c>1\), the maximum \(m_c=B(z_c)\) satisfies \(m_c>1\); the identity in Step 2 also gives \(m_c<z_c^2\). For \(1<m<m_c\), \(z=\sqrt m<z_c\) and \(B(\sqrt m)<m\), while \(B(z_c)>m\) and \(B(z_*)=0<m\); there are therefore exactly two positive-rate intersections. At \(m=m_c\), the maximum is tangent, and at \(m>m_c\) no intersection exists. Since \(B\) is strictly monotone on either side of \(z_c\), every crossing has the asserted sign and multiplicity. This completes the proof.

## Verification

The accompanying `check.py` uses only Python's standard library. It verifies polynomial/exponential identities by exact integer-polynomial arithmetic, independently compares the moment expressions against the original explicit formulas, checks coefficient bounds and interval brackets, and computes the positive root and crossing values using 72-digit decimal arithmetic. Run:

```bash
python3 check.py
```

Its output records the threshold, tangency location, and the two crossings at \(m=1.05\). These numerical checks do not prove uniqueness; the infinite coefficient sign argument in Step 3 does.

## Relationship to prior work

Radice's *Effects of mortality on stochastic search processes with resetting* (first publicly posted November 29, 2022; Physical Review E 107, 024136 (2023)) derives the exact conditional mean and variance, Eqs. (71)-(72), and numerically discusses a single rate denoted \(r_c\) where conditional standard deviation equals conditional mean. Its Fig. 4 places disappearance of such a rate near dimensionless mortality \(1.1\). The present classification uses that model and its transform, but supplies a new exact threshold, rigorous global zero count, and a narrow **two-positive-crossing regime** for \(1<m<m_c\), which is not identified by the cited numerical single-rate treatment.

Reuveni's 2016 universal unit-coefficient-of-variation result concerns nonzero rates that *minimize an unconditional restarted mean*, not the conditionally successful hitting time of a mortal particle at every reset rate. Belan's 2018 splitting-probability optimization concerns successful outcomes, but does not determine the zero count of the conditional variance-minus-square-mean curve. Later general selective-outcome reset criteria likewise do not state this explicit mortal Brownian global crossing phase diagram.

A related published classification of reentrant first-passage fluctuations changes the ratio between *initial and reset positions* in an immortal search; this theorem instead holds those positions equal and creates reentrance by changing independent mortality. Neither statement directly implies the other.

## Limitations

The argument uses an exponential mortality clock, a single perfectly absorbing target, constant diffusivity, instantaneous resetting to the initial point and a Poisson reset clock. It classifies equality of the conditional coefficient of variation with unity; it does **not** assert that \(C_V\) is monotone, that either crossing optimizes mean successful search time, or that the sign pattern is a stochastic ordering of entire first-passage distributions. The mathematical classification is an explicit refinement of known first-passage formulas, not an independent derivation of a new stochastic-process model. Literature priority remains subject to specialist assessment, notably for implied but unpublished consequences of the existing formulas.

## References

1. M. Radice, *Effects of mortality on stochastic search processes with resetting*, arXiv:2211.16173 (first posted 2022-11-29); Phys. Rev. E **107**, 024136 (2023). https://arxiv.org/abs/2211.16173 ; https://doi.org/10.1103/PhysRevE.107.024136
2. S. Reuveni, *Optimal Stochastic Restart Renders Fluctuations in First Passage Times Universal*, Phys. Rev. Lett. **116**, 170601 (2016). https://arxiv.org/abs/1512.01600 ; https://doi.org/10.1103/PhysRevLett.116.170601
3. S. Belan, *Restart Could Optimize the Probability of Success in a Bernoulli Trial*, Phys. Rev. Lett. **120**, 080601 (2018). https://arxiv.org/abs/1703.01486 ; https://doi.org/10.1103/PhysRevLett.120.080601
4. S. Pal, L. Dagdug, D. Ghosh, D. Boyer, A. Pal, *Universal criterion for selective outcomes under stochastic resetting*, arXiv:2502.09127 (2025). https://arxiv.org/abs/2502.09127
