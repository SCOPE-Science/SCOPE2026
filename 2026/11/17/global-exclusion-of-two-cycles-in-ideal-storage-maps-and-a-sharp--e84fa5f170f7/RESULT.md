# Global exclusion of two-cycles in ideal-storage maps and a sharp feedback boundary

## Finding

Let \(c>0\) and let \(h:[0,\infty)\to(0,1)\) be *nondecreasing*, with no continuity or differentiability assumption. On the physical state space \(X=[0,\infty)\times[0,1]\), define the ideal-storage map

\[
F_{c,h}(s,r)=\big(s(1-r)+c,\ h(sr)\big).
\]

**Theorem.** Every point of period dividing two is a fixed point:

\[
F_{c,h}^{\,2}(z)=z\quad\Longrightarrow\quad F_{c,h}(z)=z,\qquad z\in X.
\]

In particular, there is no primitive two-cycle at any replenishment level or feedback gain. The sole fixed point is \(z_*=(c/h(c),h(c))\); the fixed-point formula is recalled from earlier literature and is not claimed as new.

The monotonicity condition has a sharp dynamical boundary. At \(c=1/2\), consider the smooth strictly decreasing logistic response

\[
\alpha=\frac52\log\frac{35}{9},\qquad
\beta=\frac3{10}\alpha+\log\frac73,\qquad
h_-(u)=\frac{1}{1+\exp(\alpha u-\beta)}.
\]

Then \(h_-(3/10)=7/10\) and \(h_-(7/10)=3/8\); the map has the exact primitive cycle

\[
\left(\frac45,\frac38\right)
\longmapsto\left(1,\frac7{10}\right)
\longmapsto\left(\frac45,\frac38\right).
\]

This counterexample shows that the no-two-cycle theorem cannot be extended to arbitrary smooth positive feedback of range \((0,1)\) after dropping monotonic increase.

## Assumptions and scope

The theorem applies to all \(c>0\) and all nondecreasing responses \(h:[0,\infty)\to(0,1)\), including constant and discontinuous responses. Every initial \((s,r)\in X\) remains in \(X\), because \(s(1-r)+c\ge c>0\) and \(0<h(sr)<1\). The conclusion concerns **primitive temporal period two of the isolated local map**. It does not rule out invariant curves, higher-period orbits, oscillations, or spatial patterns produced by coupling several such maps. The smooth decreasing response is offered solely to establish a boundary for the monotonicity hypothesis.

## Proof

Suppose \((s_0,r_0)\mapsto(s_1,r_1)\mapsto(s_0,r_0)\). All rates and stocks along a period-two orbit are strictly positive. Put \(a=s_0r_0\) and \(b=s_1r_1\), the successive released quantities. The stock equation gives

\[
s_1-s_0=c-a,\qquad s_0-s_1=c-b.
\]

Adding yields \(a+b=2c\), and hence

\[
s_1-s_0=\frac{b-a}{2}.\tag{1}
\]

The rate equation gives \(r_1=h(a)\) and \(r_0=h(b)\), so that

\[
s_1-s_0=\frac{b}{h(a)}-\frac{a}{h(b)}.\tag{2}
\]

If \(b>a\), monotonicity and the strict bound \(h(b)<1\) imply

\[
\frac{b}{h(a)}-\frac{a}{h(b)}
\ge\frac{b-a}{h(b)}
>b-a>\frac{b-a}{2}.
\]

This contradicts (1)–(2). If \(a>b\), exchange the two cyclically indexed points and reach the same contradiction. Thus \(a=b=c\), and (1) gives \(s_1=s_0\). Also \(r_1=h(a)=h(b)=r_0\), so the two points coincide. Conversely each fixed point is of period dividing two. At a fixed point the stock equation forces \(sr=c\), so the rate equation forces \(r=h(c)\) and then \(s=c/h(c)\). This proves the main theorem without smoothness assumptions.

For sharpness, \(\alpha>0\) makes \(h_-\) smooth and strictly decreasing with values in \((0,1)\). By the selected \(\beta\), the logistic log-odds at \(u=3/10\) equal \(\log(7/3)\), hence \(h_-(3/10)=7/10\). At \(u=7/10\), they equal \(\log(3/5)\), hence \(h_-(7/10)=3/8\). Direct exact substitution gives

\[
\begin{aligned}
F_{1/2,h_-}(4/5,3/8)&=(4/5\cdot5/8+1/2,\ h_-(3/10))=(1,7/10),\\
F_{1/2,h_-}(1,7/10)&=(3/10+1/2,\ h_-(7/10))=(4/5,3/8).
\end{aligned}
\]

The two displayed states are distinct, completing the proof.

## Verification

The argument above is exact and does not rely on finite numerical experiments. The accompanying standalone `verify.py` checks the rational stock identities, both specified logistic values, the explicit two-step orbit, the fixed point, and samples of the strict flux-order contradiction using several monotone response functions. Execute `python3 verify.py` using Python 3. No external mathematical package is required. The finite tests are supplementary and do not establish universal nonexistence.

## Relationship to prior work

Hordijk (2026) studies the identical logistic ideal-storage oscillator as part of a spatial spiral model and reports a Neimark–Sacker oscillatory regime. Dress and Lin (2011) study the same general family with positive monotone feedback, establishing boundedness, uniqueness of the fixed point, local multipliers and Neimark–Sacker behavior. The global absence of primitive two-cycles is a distinct all-state conclusion, not a reformulation of their local fixed-point classification. The present theorem treats the entire monotone response class, not just the logistic example, and supplies a concrete smooth decreasing-response counterexample demonstrating the hypothesis boundary.

A 1982 foundational source by Dress, Jaeger and Plath was identified bibliographically, but its full text was not available to compare; historical priority must be qualified accordingly. Other published work on continuous-time monotone feedback and on discrete predator–prey maps with different update equations does not directly imply the precise claim here. This is a statement-level comparison, not proof of uniqueness in the literature.

## Limitations

Only primitive period two is excluded. Neither periods at least three nor invariant circles, chaos, global convergence, spatial coupling, and quantitative rates are settled. The decreasing logistic example does not characterize the full nonmonotone response class. The 1982 precursor remains an unresolved historical-priority risk; independent review and broader literature comparison have not been performed.

## References

1. W. Hordijk, *Spontaneous Spirals in Spatial Systems*, arXiv:2610.38710v1 (first posted 28 October 2026), https://arxiv.org/html/2610.38710v1.
2. A. W. M. Dress and W. Lin, *Dynamics of a Discrete-Time Model of an “Ideal-Storage” System Describing Hetero-Catalytic Processes on Metal Surfaces*, *International Journal of Bifurcation and Chaos* **21** (2011), 1331–1339, https://doi.org/10.1142/S0218127411029197; author-supplied full text at https://www.researchgate.net/publication/220272976_DYNAMICS_OF_A_DISCRETE-TIME_MODEL_OF_AN_IDEAL-STORAGE_SYSTEM_DESCRIBING_HETERO-CATALYTIC_PROCESSES_ON_METAL_SURFACES.
3. A. Dress, N. I. Jaeger and P. J. Plath, *Zur Dynamik idealer Speicher. Ein einfaches mathematisches Modell*, *Theoretica Chimica Acta* **61** (1982), 437–460 (bibliographic evidence only; full text not inspected).
