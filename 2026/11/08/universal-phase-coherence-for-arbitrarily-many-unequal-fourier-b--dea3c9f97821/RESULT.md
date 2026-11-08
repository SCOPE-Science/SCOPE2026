# Universal phase coherence for arbitrarily many unequal Fourier bands

## Finding

Consider \(m\ge2\) disjoint Fourier passbands centered at equally spaced frequencies but with **arbitrary positive widths**. A single phase template maximizes concentration on a centered time interval for **every prescribed nonnegative Fourier magnitude** precisely on explicit intervals determined by the widths. This is an exact classification for every band count, not an assertion about the unrestricted concentration-operator norm.

Write the passbands, their union, and the observation interval as
\[
B_j=\left[(j-\tfrac{m-1}{2})d-\tfrac{w_j}{2},\;(j-\tfrac{m-1}{2})d+\tfrac{w_j}{2}\right],\qquad F=\bigcup_{j=0}^{m-1}B_j,\qquad I_T=[-T/2,T/2],
\]
where \(T,d,w_0,\ldots,w_{m-1}>0\), and assume \(d>(w_j+w_{j+1})/2\) for every adjacent pair. Set
\[
 x=Td,\quad \delta_j=Tw_j,\quad
 \Delta_r=\max_{0\le j<m-r}\frac{\delta_j+\delta_{j+r}}2\qquad(1\le r<m).
\]
For every measurable \(\chi:F\to\mathbb T\), call \(\chi\) *universal* if, for every nonnegative \(h\in L^2(F)\), the Fourier transform \(h\chi\) maximizes \(\int_{I_T}|f(t)|^2\,dt\) over all Fourier transforms with modulus \(h\). Its value where \(h=0\) is irrelevant.

**Theorem.** Such a universal template exists **if and only if** all of the following conditions hold:
\[
\delta_j\le1\quad(0\le j<m),\qquad
L\le u\le U,\qquad
u=x-\lfloor x\rfloor,
\]
where
\[
 L=\max_{1\le r<m}\frac{\Delta_r}{r},
 \qquad U=\min_{1\le r<m}\frac{1-\Delta_r}{r}.
\]
(Thus the intervals are empty when \(L>U\); the original strict passband disjointness assumption still applies.) Whenever the criterion holds, **every** universal phase is, up to one common unimodular factor, the bandwise constant template
\[
\chi(\omega)=(-1)^{j\lfloor x\rfloor},\qquad \omega\in B_j\quad(0\le j<m).
\]
Endpoints \(u=L\) and \(u=U\) are included whenever the bands remain disjoint: the zeros of the sinc kernel then occur only on measure-zero boundary pairs.

For the equal-width specialization \(w_j=w\), putting \(\delta=Tw\), the criterion simplifies to
\[
0<\delta\le \frac1m,\qquad
x\in\left[k+\delta,\;k+\frac{1-\delta}{m-1}\right],\quad k\in\mathbb Z_{\ge0},\quad x>\delta.
\]
Thus the largest feasible number of equal-width bands is governed sharply by \(m\delta\le1\). In particular, if \(\delta=1/m\), the nonempty windows collapse to isolated points at each positive integer translate; if \(\delta<1/m\), they are genuine recurring intervals, including at arbitrarily large separations.

## Assumptions and scope

Fourier inversion and Plancherel use \(f(t)=\int_F\widehat f(\omega)e^{2\pi i\omega t}\,d\omega\). The closed passbands have positive lengths and disjoint interiors; the strict adjacent-gap assumption ensures all pair differences between distinct bands have a fixed positive sign when ordered by band index. The integer \(m\) is arbitrary but finite; the number, widths, and center separation are deterministic. The theorem optimizes spectral phases *for each fixed magnitude*, uniformly across every choice of that magnitude; it does **not** optimize the magnitude itself.

## Proof

**1. The exact kernel and the pairwise necessity lemma.** Since \(F\) has finite measure, each \(\widehat f\in L^2(F)\) is integrable. Fourier inversion and Fubini yield
\[
\int_{I_T}|f(t)|^2\,dt=\iint_{F^2}\widehat f(\omega)\overline{\widehat f(\eta)}K_T(\omega-\eta)\,d\omega\,d\eta,
\quad
K_T(s)=\begin{cases}\sin(\pi Ts)/(\pi s),&s\ne0,\\T,&s=0.\end{cases}
\]
We claim that a universal \(\chi\) must satisfy \(K_T(\omega-\eta)\chi(\omega)\overline{\chi(\eta)}=|K_T(\omega-\eta)|\) for almost every pair where \(K_T\ne0\). Indeed, choose nonnegative magnitudes supported on two arbitrarily short disjoint intervals around any two Lebesgue points of \(\chi\), and compare to independently rotating the phase on the second interval. The rotation-dependent cross term, after dividing by the product of the interval masses and shrinking the intervals, converges to \(K_T(\omega-\eta)\chi(\omega)\overline{\chi(\eta)}\). Universality forces this limit to be nonnegative real; rotation by its negative argument gives strict improvement otherwise. This holds at almost every pair by differentiation. Conversely, that pairwise identity immediately maximizes the quadratic form for all nonnegative magnitudes, since every real cross term is bounded above by its absolute value.

**2. Constant phase on each band and the local width obstruction.** The sinc kernel is strictly positive for \(0<|Ts|<1\). Therefore the pairwise identity forces \(\chi\) to be almost everywhere locally constant on each connected band, hence constant there. If \(Tw_j>1\), two positive-measure subintervals of that band have differences strictly between \(1/T\) and \(\min(2/T,w_j)\), on which \(K_T<0\); this contradicts constancy. Consequently every \(\delta_j\le1\). With these inequalities, every within-band pair has nonnegative sinc kernel.

**3. Sign of the cross-band interactions.** The differences between points in bands \(B_j\) and \(B_{j+r}\) have positive absolute size in
\[
\left[rd-\tfrac{w_j+w_{j+r}}2,\;rd+\tfrac{w_j+w_{j+r}}2\right].
\]
For the sinc sign to be constant on every such interval, none can contain a zero \(\ell/T\) in its interior. Because its center is \(rd\), this holds if and only if \([rx-\Delta_r,rx+\Delta_r]\) lies in one closed unit interval \([a_r,a_r+1]\), where \(a_r\) is an integer. Its common sign is \((-1)^{a_r}\). The maximum \(\Delta_r\) is valid because the intervals for fixed \(r\) are nested around the same center.

In particular, the adjacent-band sign is the same for every adjacent pair; writing \(k=\lfloor x\rfloor\), it equals \((-1)^k\). Thus adjacent phase matching forces the successive band phases to be \(\chi_j=\chi_0(-1)^{jk}\). A pair of bands at distance \(r\) requires \(a_r\equiv rk\pmod2\).

**4. The parity staircase cannot advance.** Put \(u=x-k\), so \(0\le u<1\). Because every \(\Delta_r>0\), the existence of the same-signed interval implies \(rx\notin\mathbb Z\) and \(a_r=\lfloor rx\rfloor=rk+\lfloor ru\rfloor\). The parity constraint says \(\lfloor ru\rfloor\) is even for each \(r=1,\ldots,m-1\). But \(\lfloor u\rfloor=0\) and successive differences \(\lfloor(r+1)u\rfloor-\lfloor ru\rfloor\) belong to \(\{0,1\}\). Since every member must be even, the entire staircase must remain zero: \(\lfloor ru\rfloor=0\) for all these \(r\). Hence each cross-band interval must lie in \([rk,rk+1]\), equivalently
\[
\Delta_r\le ru\le1-\Delta_r\qquad(1\le r<m).
\]
Taking the maximum lower and minimum upper bounds gives exactly \(L\le u\le U\).

**5. Sufficiency and uniqueness.** Assume these inequalities and \(\delta_j\le1\). Every within-band pair has nonnegative kernel. For bands \(j\) and \(j+r\), the entire difference range lies between \(rk\) and \(rk+1\), where the sinc kernel sign is \((-1)^{rk}\). The displayed template contributes the same sign and turns every cross term into the nonnegative absolute kernel. Step 1 proves optimality for *every* magnitude. Conversely, Step 2 fixes one phase per band, and adjacent matching fixes all of them from one common phase. This proves uniqueness almost everywhere. Equality endpoints have no effect on the almost-everywhere argument.

**6. Equal-width reduction.** If all \(\delta_j=\delta\), then \(\Delta_r=\delta\) for all \(r\). Consequently \(L=\delta\) and \(U=(1-\delta)/(m-1)\) whenever a nonempty interval is possible; it is possible exactly when \(m\delta\le1\). The case \(k=0,u=\delta\) violates the strict gap \(x>\delta\) and is excluded by hypothesis. All other asserted endpoint and recurrence statements follow directly.

## Verification

The argument above proves the result for every finite \(m\) and every positive allowed width vector, without numerical assumptions. The standalone program `check_unequal_multiband.py` exhausts the real sign comparisons on a deterministic collection of randomly generated nonboundary parameters for \(2\le m\le10\), and checks additional feasible constructions. Its verified output is `UNEQUAL_MULTIBAND_SIGN_CHECKS_PASS 6276`. These finite tests are a consistency check, **not** a proof of the infinite-parameter or measurable-phase assertions. No numerical certificate is required for the proof.

## Relationship to prior work

Baeza-Guasch, arXiv:2307.04558, develops fixed-modulus phase alignment on a *single connected* Fourier interval in a no-aliasing regime. In particular, its Section 2 gives the sinc quadratic-form mechanism used here. The revised text explicitly distinguishes that fixed-modulus result from unrestricted operator concentration. The present statement instead classifies an **arbitrary finite number of disconnected, unequal-width** Fourier bands, including arbitrarily large gaps, where the sinc kernel need not be globally positive. Its band-index parity argument and precise interval bounds are not asserted in the inspected source.

A previously established equal-width three-band phase-window classification is a special case of the present theorem and is **not claimed as an independent new result**. The new content is the complete arbitrary-band-count and unequal-width width-vector criterion, including its exact integer-window geometry. The 2026 work of Abreu and Speckbacher on unrestricted Paley–Wiener concentration concerns a different optimization: it does not prescribe a single phase for every Fourier magnitude.

## Limitations

The centers are equally spaced, the widths may differ, and the time observation set is a centered interval. The theorem does not classify irregularly spaced centers, several observation time intervals, nonmeasurable phases, or unrestricted optimization of Fourier magnitudes. Its originality comparison remains provisional against any earlier general signed-kernel or multiband phase theorem not located in the searches. Independent validation is not performed.

## References

1. O. Baeza-Guasch, *Phase symmetrization and a no-aliasing concentration principle in Paley-Wiener spaces*, arXiv:2307.04558, first submitted July 10, 2023; revised August 21, 2026. https://arxiv.org/html/2307.04558v2
2. D. L. Donoho and P. B. Stark, *Uncertainty principles and signal recovery*, SIAM Journal on Applied Mathematics 49 (1989), 906–931.
3. L. D. Abreu and M. Speckbacher, *Optimal concentration in the Paley-Wiener space*, arXiv:2607.19192 (2026); distinct operator-level setting. https://arxiv.org/abs/2607.19192
