# Sharp universal phase-coherence windows for three separated Fourier bands

## Finding

Let \(T,w,d>0\), \(d>w\), and consider three disjoint equal-width Fourier bands
\[
F_{d,w}= [-d-w/2,-d+w/2]\cup[-w/2,w/2]\cup[d-w/2,d+w/2].
\]
For the centered observation interval \(I_T=[-T/2,T/2]\), a *universal phase template* is a measurable function \(\chi:F_{d,w}\to\mathbb C\) with \(|\chi|=1\) almost everywhere such that, **for every** nonnegative \(h\in L^2(F_{d,w})\), the inverse Fourier transform of \(h\chi\) maximizes energy on \(I_T\) among all functions with Fourier modulus \(h\). The template must be independent of \(h\).

Put \(\delta=Tw\) and \(x=Td\). Such a template exists **if and only if**
\[
0<\delta\le\frac13,\qquad
k+\delta\le x\le k+\frac{1-\delta}{2}
\quad\text{for some integer }k\ge0,
\]
together with the stipulated strict band separation \(x>\delta\). If it exists, it is unique up to a common constant complex phase: on the ordered left, central and right bands it takes the values
\[
\chi=(1,(-1)^k,1).
\]
For \(\delta<1/3\), the coherence windows form infinitely many disjoint intervals of length \((1-3\delta)/2\) in the dimensionless separation \(x\); for \(\delta=1/3\) they collapse to isolated values \(x=k+1/3\), necessarily with \(k\ge1\); for \(\delta>1/3\) there is no universal phase template at any separation.

For strict inequalities \(k+\delta<x<k+(1-\delta)/2\) the maximizing phase has the exact quantitative rigidity identity
\[
\mathcal E(h\chi)-\mathcal E(hz)=\frac12\iint_{F_{d,w}^2}h(u)h(v)|K_T(u-v)|\big|z(u)\overline{\chi(u)}-z(v)\overline{\chi(v)}\big|^2\,du\,dv,
\]
where \(\mathcal E(a)\) means the squared time-window energy of the inverse Fourier transform of \(a\), \(|z|=1\) where \(h>0\), and
\[
K_T(s)=\begin{cases}\sin(\pi Ts)/(\pi s)&s\ne0,\\ T&s=0.\end{cases}
\]
In particular, with
\[
c=\min_{s\in[0,w]\cup[d-w,d+w]\cup[2d-w,2d+w]}|K_T(s)|>0,
\]
we have
\[
\mathcal E(h\chi)-\mathcal E(hz)\ge c\left[\left(\int_{F_{d,w}}h\right)^2-\left|\int_{F_{d,w}}h z\overline\chi\right|^2\right].
\]
This constant is explicitly computable from the sinc kernel; **no claim of optimality for this coercivity coefficient** is made.

## Assumptions and scope

The Fourier convention is \(\widehat f(\xi)=\int_{\mathbb R} f(t)e^{-2\pi i\xi t}\,dt\). The inverse transform is \(f(t)=\int_{F_{d,w}}\widehat f(\xi)e^{2\pi i\xi t}\,d\xi\). Any prescribed \(h\in L^2(F_{d,w})\) is automatically integrable because the frequency set has finite measure. The competing phases \(z\) are arbitrary measurable functions into the unit circle on \(\{h>0\}\); their values on \(\{h=0\}\) do not matter. The quantifiers concern **every spectral amplitude** \(h\), not a maximizer chosen separately for each amplitude. Boundary values of bands are irrelevant up to null sets.

## Proof

**Step 1: Exact kernel and the pairwise necessity principle.** Fubini's theorem gives
\[
\mathcal E(hz)=\iint_{F_{d,w}^2} h(u)h(v)K_T(u-v)z(u)\overline{z(v)}\,du\,dv.
\]
The kernel is continuous, real and even. Suppose \(\chi\) universally maximizes the form. Choose any two distinct Lebesgue points \(u,v\) of \(\chi\) for which \(K_T(u-v)\ne0\). For \(h\) supported on two small disjoint intervals about these points, and with arbitrary positive relative masses, comparison with phases constant on each packet and then shrinking the packets shows
\[
\chi(u)\overline{\chi(v)}=\operatorname{sgn}K_T(u-v).
\]
Indeed, after dividing by the product of the two packet masses, the off-diagonal term converges to \(2K_T(u-v)\operatorname{Re}(\chi(u)\overline{\chi(v)})\), and its maximum over relative phase is \(2|K_T(u-v)|\). The diagonal packet contributions are identical in this limit for any candidate phases because \(K_T(0)>0\). Thus the equality is necessary for almost every pair away from sinc zeros. Conversely, if this equality holds for almost every pair, inserting \(z=\chi q\) into the kernel gives the nonnegative-phase difference identity displayed above. Therefore the pairwise condition is also sufficient.

**Step 2: Piecewise constant phase.** Since \(K_T(s)>0\) for all sufficiently small \(|s|\), the pairwise condition forces \(\chi\) to be constant almost everywhere on each connected band: it is equal on almost every pair separated by less than a sufficiently small radius, and chains of overlapping subintervals connect any two interior points. A necessary condition is that \(K_T\) be nonnegative throughout each within-band difference interval; otherwise a pair would require opposite phases on the same band. In particular \(\delta=Tw\le1\). Between any two bands the difference set is a full interval; because the phase ratio of the two bands is constant, the real sinc kernel must have constant sign on the interior of that difference interval. For \(s>0\), the sign of \(K_T(s)\) on \(j<Ts<j+1\) is \((-1)^j\). Sinc zeros at the finite interval endpoints do not affect an almost-everywhere conclusion.

**Step 3: Adjacent-band lobe.** The differences between either adjacent pair range from \(d-w\) to \(d+w\). Hence there is an integer \(k\ge0\) such that
\[
k\le x-\delta,\qquad x+\delta\le k+1,
\]
or equivalently \(x=k+u\) with \(\delta\le u\le1-\delta\). Both adjacent interactions have sign \((-1)^k\). Their product is positive, so the outer-band phase ratio must be positive.

**Step 4: Outer-band compatibility.** Outer-band differences lie between \(2d-w\) and \(2d+w\), so \(T\) times these differences ranges over \([2k+2u-\delta,2k+2u+\delta]\). Because \(u\in[\delta,1-\delta]\), this interval is contained in \([2k,2k+2]\) and cannot extend through the next even-positive sinc lobe. For the outer interaction to be nonnegative almost everywhere, it must lie inside the even-indexed positive lobe \([2k,2k+1]\). Its upper endpoint condition is
\[
2u+\delta\le1.
\]
The lower endpoint condition \(2u-\delta\ge0\) already follows from \(u\ge\delta\). We obtain \(\delta\le u\le(1-\delta)/2\), feasible exactly for \(\delta\le1/3\). Conversely these inequalities make all bandwise signed kernels nonnegative after assigning the three signs \((1,(-1)^k,1)\); the necessity-and-sufficiency principle in Step 1 proves universality. All interactions are nonzero away from finitely many difference lines, so the template is unique modulo one constant phase, including at closed-window endpoints. At \(\delta=1/3\), \(k=0\) would give \(d=w\), which is excluded, leaving \(k\ge1\).

**Step 5: Rigidity.** With \(q=z\overline\chi\), the preceding sign analysis gives \(\chi(u)\overline{\chi(v)}K_T(u-v)=|K_T(u-v)|\) almost everywhere. Subtracting the two quadratic forms and using \(1-\operatorname{Re}(q(u)\overline{q(v)})=|q(u)-q(v)|^2/2\) proves the exact identity. In a strict coherence window no sinc zero belongs to the compact set of absolute difference magnitudes (including within-band and both cross-band ranges), so the displayed \(c\) is strictly positive. Finally,
\[
\frac12\iint h(u)h(v)|q(u)-q(v)|^2\,du\,dv
=\left(\int h\right)^2-\left|\int hq\right|^2.
\]
This finishes the proof.

## Verification

The standalone script `checks/three_band_phase.py` tests the closed-form lobe classification against explicit sinc-sign intervals on 20,000 randomized parameter triples. It also computes discrete quadratic forms on three sampled bands with positive amplitudes and random competing phases, including coherence windows with positive and negative middle-band signs. Its output is `THREE_BAND_PHASE_DIAGRAM_PASS 20000` and `THREE_BAND_NUMERICS_PASS`. These finite tests do **not** prove the classification; Steps 1–5 above prove it. Run with Python 3 and NumPy by invoking `python checks/three_band_phase.py` from this document's directory.

## Relationship to prior work

Baeza-Guasch's phase-symmetrization theorem gives the real sinc quadratic form and phase alignment for a **single connected spectral interval** under the nonnegative-kernel condition. Those identities are used, not claimed as new. Its theorem does not classify universal phase templates for disconnected spectral bands and does not give the three-band sharp threshold, recurrent coherence windows, or bandwise phase rigidity. Donoho–Stark's classical concentration theory compares time/frequency projections at the operator level and does not assert a universal fixed-Fourier-modulus phase choice for this three-band geometry. Standard signed-graph cycle balance explains the algebraic sign obstruction abstractly; the new mathematical question is the exact interaction of the **continuous sinc sign lobes** with three equal positive-width spectral intervals. The present result concerns a distinct fixed-modulus problem and neither proves nor disproves the unrestricted concentration conjecture.

## Limitations

The theorem treats exactly three equally spaced, equal-width Fourier bands and the centered time interval. It asserts existence of a phase template **uniform over all prescribed Fourier magnitudes**; outside the permitted windows each individual magnitude may still have an optimizing phase, but no template works for all of them. The rigidity coefficient is a valid explicit positive bound, not asserted sharp. General unequal bands, noncentral time sets, and operator-level best concentration constants are not classified. Historical priority is provisional: an earlier general phase-gauge or signed-kernel theorem may imply the classification even if no precisely matching statement was located.

## References

1. O. Baeza-Guasch, *Phase symmetrization and a no-aliasing concentration principle in Paley–Wiener spaces*, arXiv:2307.04558; first public version July 10, 2023, revised August 21, 2026. In particular, §2, Lemma 2.1 and Theorem 2.2 give the real sinc quadratic form and connected-band phase comparison. https://arxiv.org/abs/2307.04558 ; https://arxiv.org/html/2307.04558v2
2. D. L. Donoho and P. B. Stark, *Uncertainty Principles and Signal Recovery*, SIAM Journal on Applied Mathematics 49 (1989), 906–931. DOI: 10.1137/0149053.
