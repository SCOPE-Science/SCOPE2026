# Unique Poisson-reset resonance with gamma-distributed maturation latency

## Finding

Consider the phase-selected renewal-response model defined below. At every reset a two-state output is selected by the phase of a periodic forcing, but that output becomes visible only after an independent gamma-distributed maturation time. For all forcing frequencies \(\omega>0\), fixed mean maturation \(\tau>0\), and gamma shapes \(k>0\), the fundamental harmonic has a **unique** maximizing positive reset rate. If \(x=\tau r\) and \(w=\tau\omega\), its dimensionless optimum \(x_k(w)\) is the unique positive root of
\[
 kx^4+k^2x^3+(k-1)w^2x^2+k(k-2)w^2x-w^2(k^2+w^2)=0.
\]
For every \(w>0\), \(x_k(w)\) is **strictly decreasing** in the shape \(k\) at fixed mean, hence strictly increasing in the gamma latency coefficient of variation \(k^{-1/2}\). It has the sharp asymptotics
\[
 x_k(w)=w^{2/3}+\frac{k^{-1}-1}{3}w^{4/3}+O_k(w^2)
 \quad(w\downarrow0),\qquad
 x_k(w)\sim \frac{w}{\sqrt{k}}\quad(w\to\infty).
\]
Its optimal harmonic amplitude \(\mathcal A_*\) satisfies
\[
 \frac{\mathcal A_*(w,k)}{4q/\pi}\sim
 \frac{1}{\sqrt{1+k}}\left(\frac{k^3}{1+k}\right)^{k/2}w^{-k}
 \quad(w\to\infty).
\]
For deterministic latency \(T\equiv\tau\), in contrast, the unique optimum \(x_\infty(w)\) solves \(x(x^2+w^2)=w^2\), so \(x_\infty(w)\to1\) and the optimal harmonic amplitude is asymptotic to \((4q/\pi)e^{-1}w^{-1}\). The high-frequency rate law changes qualitatively at any nonzero gamma latency heterogeneity, even at fixed mean.

## Assumptions and scope

Let \(\{S_j\}\) be the events of a homogeneous Poisson process on the whole real line of rate \(r>0\). Independently at each \(S_j\), sample \(T_j\sim\operatorname{Gamma}(k,\tau/k)\), with **shape** \(k>0\), **scale** \(\tau/k\), and mean \(\tau\). For the most recent event \(S(t)\le t\), define the real-valued output
\[
 Y(t)=q\,\operatorname{sgn}\bigl(\cos(\omega S(t))\bigr)\,
 \mathbf1\{t-S(t)\ge T_{S(t)}\},
 \qquad q>0,\quad\omega>0.
\]
The output is zero while maturation remains incomplete. Once matured, the sign selected at the **reset phase**, not the current forcing phase, persists until the next reset. The sampled maturation clock is **aborted at the next reset** and redrawn independently. Thus this is a precisely defined ideal phase-selected two-branch response, not an exact assertion about the trajectories of a smooth double-well potential.

\(\mathcal A(r,\omega;k,\tau,q)\) is the amplitude of the fundamental harmonic in the periodic ensemble mean \(\mathbb E Y(t)\). For fixed \(\omega,k,\tau,q\), extend \(\mathcal A\) continuously to \(r=0\); this extension is not a claim of a stationary renewal process at zero rate. The theorem addresses \(r>0\), all real gamma shapes \(k>0\), and a fixed positive mean \(\tau\). When \(k\) is a positive integer, maturation is an Erlang chain of \(k\) exponential activation stages.

## Proof

**1. Renewal and harmonic transfer.** At any time \(t\), the backward age \(a=t-S(t)\) is exponential with density \(r e^{-ra}\), independently of the maturation mark. Thus
\[
 \mathbb E Y(t)=q\int_0^\infty re^{-ra}F_T(a)
 \operatorname{sgn}(\cos(\omega(t-a)))\,da.
\]
The first-harmonic amplitude of the sign-of-cosine wave is \(4/\pi\). With \(\operatorname{Re}z>0\), absolute integrability permits Fubini's theorem, which gives
\[
 \int_0^\infty e^{-za}F_T(a)\,da
 =\mathbb E\int_T^\infty e^{-za}\,da=\frac{\mathbb E e^{-zT}}{z}.
\]
Since the gamma Laplace transform is \(\mathbb E e^{-zT}=(1+\tau z/k)^{-k}\),
\[
 \boxed{\displaystyle
 \mathcal A=\frac{4q}{\pi}\frac{x}{\sqrt{x^2+w^2}}
 \left[(1+x/k)^2+(w/k)^2\right]^{-k/2}.}
\]
No expansion in forcing amplitude is used in this exact response-level calculation.

**2. Exact uniqueness.** Differentiating the logarithm of the positive normalized amplitude with respect to \(x\) yields
\[
 \frac{d\log\mathcal A}{dx}
 =\frac{w^2}{x(x^2+w^2)}-
 \frac{k(k+x)}{(k+x)^2+w^2}.
\]
After multiplication by the positive denominator \(x(x^2+w^2)((k+x)^2+w^2)\), the derivative has the opposite sign from
\[
 P_{k,w}(x)=kx^4+k^2x^3+(k-1)w^2x^2+k(k-2)w^2x-w^2(k^2+w^2).
\]
Its coefficient signs, in descending powers and omitting zeros, have **exactly one** change for each \(k>0\): \(+, +,\operatorname{sgn}(k-1),\operatorname{sgn}(k-2),-\). By Descartes' rule there is at most one positive root, counted with multiplicity. Since \(P_{k,w}(0)<0\) and \(P_{k,w}(x)\to\infty\), one root exists, crosses from negative to positive, and is the unique global maximizer. The amplitude approaches zero as \(x\downarrow0\) (because \(w>0\)) and as \(x\to\infty\) (because \(k>0\)).

**3. Ordering by latency heterogeneity.** Put
\[
 g_k(x)=\frac{k(k+x)}{(k+x)^2+w^2}.
\]
For each \(x,w>0\),
\[
 \frac{\partial g_k(x)}{\partial k}
 =\frac{x(k+x)^2+(2k+x)w^2}{((k+x)^2+w^2)^2}>0.
\]
The other term in the stationary equation is independent of \(k\), and the derivative of \(\log\mathcal A\) is strictly positive before its one zero and strictly negative after. Thus increasing \(k\) shifts the zero strictly **left**. Moreover \(g_k(x)<1\) for finite \(k\), while \(g_k(x)\to1\) as \(k\to\infty\). Hence \(x_k(w)>x_\infty(w)\), and \(x_k(w)\downarrow x_\infty(w)\) as \(k\to\infty\).

**4. Low- and high-frequency laws.** For fixed \(k\), set \(\varepsilon=w^{2/3}\) and \(x=t\varepsilon\) in \(P_{k,w}(x)=0\). Division by \(\varepsilon^3\) gives a polynomial tending on compact \(t\)-sets to \(k^2(t^3-1)\), which has a unique positive zero. Bracketing around this zero and uniqueness of the original positive root show \(t\to1\). Expanding further in \(x=\varepsilon+a\varepsilon^2+O(\varepsilon^3)\) gives \(3a+1=k^{-1}\), proving the low-frequency expansion. For \(w\to\infty\), write \(x=tw\) in the polynomial and divide by \(w^4\). The dominant polynomial is
\[
 kt^4+(k-1)t^2-1=(t^2+1)(kt^2-1).
\]
Its unique positive zero \(t=1/\sqrt{k}\), with the one-root sign structure, implies \(x_k(w)/w\to1/\sqrt{k}\). Substituting into the exact amplitude gives the stated sharp \(w^{-k}\) law, including its coefficient.

**5. Deterministic-latency comparison.** The gamma Laplace transfer converges pointwise as \(k\to\infty\) to \(e^{-\tau z}\). Its normalized amplitude is \(x e^{-x}/\sqrt{x^2+w^2}\), whose derivative vanishes exactly at \(x(x^2+w^2)=w^2\); the left side is strictly increasing. Its root tends to \(1\) as \(w\to\infty\), and substitution proves the asymptotic \(e^{-1}/w\). The finite-\(k\) high-frequency and deterministic-latency high-frequency limits therefore cannot be interchanged at the level of the unscaled optimum: for every fixed finite \(k\), the optimum diverges, whereas the deterministic optimum remains bounded.

## Verification

The included standalone `verification.py` checks the exact derivative-polynomial identity and positive shape derivative symbolically, tests 81 positive parameter pairs for the unique stationary maximum, verifies monotone ordering over representative shape grids, checks the small- and large-frequency asymptotics, and independently integrates the gamma cumulative distribution against the exponential age kernel to reproduce the complex transfer factor. It completed with 428 deterministic assertions using the listed Python dependencies. These finite checks support reproducibility and do not replace the infinite-parameter proof.

Run with `python verification.py` after installing `sympy`, `numpy`, `scipy`, and `mpmath`.

## Relationship to prior work

Wang, Li, Zhu, Cherstvy, Metzler and Xu (arXiv:2611.01991v1, first public 2026-11-01) established a general Poisson-reset renewal formula for harmonic response and a deterministic phase-dependent post-reset transit-time approximation, obtaining a low-frequency \(\omega^{2/3}\) optimum. Their main-text equations (8)–(11), End Matter equations (A1)–(A5), and Supplemental Material sections S1.3–S2.1 are the direct precursor. The age-filter/Laplace-transform identity and the deterministic-time limit are not claimed as new here. The separately sampled **gamma maturation time**, exact unique optimizer for every frequency and shape, strict fixed-mean shape ordering, and **finite-shape high-frequency exponent and linear rate law** are the statements tested for noncoverage.

Radice (arXiv:2201.01829) studied gamma-distributed *reset intervals* and noninstantaneous return motion in diffusion, not gamma maturation after independent **Poisson** phase-selection resets. Plesser and Geisel (Phys. Rev. E 59, 7008, 1999) studied periodic forcing and stochastic resonance of an integrate-and-fire neuron with a phase Markov description, not this exact gamma-latency transfer and optimizer. The literature search uncovered no exact implication of this theorem in those inspected sources. This is a best-knowledge comparison, not a proof of priority.

## Limitations

This is a coarse-grained phase-selected observable; it does not assert that a smooth double-well Langevin system has independent gamma maturation, that its phase-selection sign is exact, or that all harmonics behave similarly. The dynamics assumes Poisson resets, independence of the maturation marks, abort-and-redraw at resets, perfect two-state selection and output persistence after maturation. Inference from the exponent \(k\) requires this model class. A more general, possibly unindexed renewal or refractory-response theorem might imply this explicit optimization classification. Independent validation has not been performed.

## References

1. W. Wang, K. Li, J. Zhu, A. G. Cherstvy, R. Metzler, and Y. Xu, *Weak-Signal Amplification through Stochastic Resetting*, arXiv:2611.01991v1 (2026-11-01), https://arxiv.org/html/2611.01991 ; https://arxiv.org/abs/2611.01991 .
2. M. Radice, *Diffusion processes with Gamma-distributed resetting and non-instantaneous returns*, arXiv:2201.01829 (2022), https://arxiv.org/abs/2201.01829 .
3. H. E. Plesser and T. Geisel, *Markov analysis of stochastic resonance in a periodically driven integrate-and-fire neuron*, Phys. Rev. E **59**, 7008–7017 (1999), https://doi.org/10.1103/PhysRevE.59.7008 .
