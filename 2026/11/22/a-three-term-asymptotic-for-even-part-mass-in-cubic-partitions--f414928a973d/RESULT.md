# A three-term asymptotic for even-part mass in cubic partitions

## Finding

Let \(a(n)\) count cubic partitions of \(n\): odd parts have one color and positive even parts have two distinguishable colors. Let \(CES(n)\) be the sum, over all such partitions, of the sizes of all even parts, counted with multiplicity. Then, as \(n\to\infty\),

\[
\frac{CES(n)}{a(n)}
=\frac{2n}{3}-\frac{2\sqrt n}{3\pi}
 +\frac1{12}-\frac1{\pi^2}+O(n^{-1/2}).
\]

Consequently, the mean odd-part mass is \(n/3+2\sqrt n/(3\pi)-1/12+1/\pi^2+O(n^{-1/2})\). In particular, for all sufficiently large \(n\), the even-part mass is strictly less than \(2n/3\) on average, despite two even-part colors and one odd-part color. The explicit negative square-root correction and constant term refine the color-density leading prediction.

## Assumptions and scope

All partitions have positive integer parts and total size \(n\). The two colors of every even part are distinct independent part types. The empty partition is included in \(a(0)=1\), and \(CES(0)=0\). The claim is an asymptotic for integers \(n\to\infty\); the error constant is absolute, not stated effectively. No pointwise claim is made about individual partitions.

Write \(f_r(q)=\prod_{m\ge1}(1-q^{rm})\), \(A(q)=1/(f_1(q)f_2(q))=\sum_{n\ge0}a(n)q^n\), and \(L(q)=\sum_{m\ge1}\sigma(m)q^m\), with \(\sigma(m)=\sum_{d\mid m}d\). Define \(C=\pi^2/4\) and, for \(n\ge1\), \(N=n-1/8\), \(z=2\sqrt{CN}=\pi\sqrt N\). The symbol \(I_\nu\) denotes the modified Bessel function of the first kind.

## Proof

**1. Marking the even mass.** In each of the two even-part colors, marking the sum of part sizes with a variable and differentiating at one gives

\[
\mathcal C(q):=\sum_{n\ge0}CES(n)q^n
=4L(q^2)A(q).
\]

Equivalently, \(CES(n)=4\sum_{j=1}^{\lfloor n/2\rfloor}\sigma(j)a(n-2j)\). Both identities are exact over formal integer power series. They also appear as Theorems 3.1–3.2 of Bardhan and Saikia, whose emphasis is on congruences.

**2. Exact local modular transformations.** For complex \(w\) with \(\operatorname{Re}w>0\), Dedekind eta transformation gives

\[
A(e^{-w})=\frac{w}{\sqrt2\pi}
 \exp\!\left(\frac Cw-\frac w8\right)
 \frac1{f_1(e^{-4\pi^2/w})f_1(e^{-2\pi^2/w})}.
\]

The quasimodular transformation of \(E_2(q)=1-24L(q)\) gives

\[
4L(e^{-2w})=\frac{\pi^2}{6w^2}-\frac1w+\frac16
 +\frac{\pi^2}{6w^2}\bigl(E_2(e^{-2\pi^2/w})-1\bigr).
\]

(The last term is written with its exact sign.) Thus, uniformly when \(\operatorname{Re}(1/w)\) grows like \(1/|w|\), the factors involving \(e^{-2\pi^2/w}\) are exponentially small. Multiplying the displayed identities yields the local model

\[
\mathcal C(e^{-w})=\frac1{\sqrt2\pi}
 \left(\frac{\pi^2}{6w}-1+\frac w6\right)
 \exp\!\left(\frac Cw-\frac w8\right)
 \bigl(1+\text{exponentially small correction}\bigr).
\]

The exact sign of the exponentially small correction is immaterial, but no algebraic-order terms have been omitted.

**3. Quantitative coefficient extraction.** Fix any \(0<\delta<1/4\), and choose \(t=\sqrt{C/N}\). On \(q=e^{-t+i\theta}\), use \(w=t-i\theta\). The positivity of the coefficients of \(\log A\) gives, for \(-\pi\le\theta\le\pi\) and \(M=\lfloor1/t\rfloor\),

\[
\log A(e^{-t})-\log|A(e^{-t+i\theta})|
\ge e^{-1}\sum_{m=1}^M(1-\cos(m\theta))
\ge c\min(M^3\theta^2,M),
\]

for an absolute \(c>0\) and sufficiently large \(M\). To verify the last elementary inequality, use \(1-\cos u\ge c_0u^2\) when \(|u|\le1\), then the geometric-sum bound for \(\sum_{m=1}^M e^{im\theta}\) when \(|\theta|\gg1/M\); the compact intermediate range is handled by a Riemann-sum estimate for \(1-\cos u\). Also \(|4L(q^2)|\le4L(e^{-2t})=O(t^{-2})\). The entire arc \(|\theta|\ge t^{3/2-\delta}\) therefore contributes \(O(e^{z-c't^{-2\delta}})\) up to powers of \(t^{-1}\), negligible to every algebraic order compared with the main saddle contribution.

On the remaining short arc, \(\operatorname{Re}(1/w)=(1+o(1))/t\), so the two modular formulas have exponentially small errors, uniformly. Standard local saddle-contour deformation (the connecting tails have phase smaller by \(c't^{-2\delta}\)) therefore reduces the coefficient integrals, with error negligible to every algebraic order, to

\[
J_s(N)=\frac1{2\pi i}\oint_{|w|=\sqrt{C/N}}
 w^s e^{C/w+Nw}\,dw
=\left(\frac CN\right)^{(s+1)/2} I_{s+1}(z),
\qquad s\in\{-1,0,1\}.
\]

The last equality follows directly from the power-series definition of \(I_\nu\) or its generating-function contour. In particular, writing \(K=1/(\sqrt2\pi)\),

\[
a(n)=K\frac CN I_2(z)\bigl(1+O(n^{-B})\bigr)
\]

and

\[
CES(n)=K\left(\frac{\pi^2}6 I_0(z)
 -\sqrt{\frac CN}I_1(z)+\frac C{6N}I_2(z)\right)
 +O\!\left(e^z n^{-B}\right)
\]

for every fixed \(B>0\), after taking a suitable fixed short-arc exponent. These are asymptotic Bessel representations, not claimed as exact identities of the original coefficients. Polynomial factors in the remainder can be absorbed by reducing the exponent \(B\). Since \(I_2(z)\sim e^z/\sqrt{2\pi z}\), their ratio satisfies, to arbitrary algebraic order,

\[
\frac{CES(n)}{a(n)}
=\frac{2N}{3}\frac{I_0(z)}{I_2(z)}
 -\sqrt{\frac NC}\frac{I_1(z)}{I_2(z)}+\frac16
 +O(n^{-B}).
\]

**4. Expansion and constants.** The fixed-order Bessel expansion is

\[
I_\nu(z)=\frac{e^z}{\sqrt{2\pi z}}
\left(1-\frac{4\nu^2-1}{8z}
 +\frac{(4\nu^2-1)(4\nu^2-9)}{128z^2}
 +O(z^{-3})\right).
\]

Direct division gives \(I_0(z)/I_2(z)=1+2/z+3/z^2+O(z^{-3})\) and \(I_1(z)/I_2(z)=1+3/(2z)+O(z^{-2})\). Since \(z=2\sqrt{CN}\), substitution yields

\[
\frac{CES(n)}{a(n)}
=\frac{2N}{3}-\frac{\sqrt N}{3\sqrt C}
 +\frac16-\frac1{4C}+O(N^{-1/2}).
\]

Finally \(C=\pi^2/4\) and \(N=n-1/8\), giving exactly \(2n/3-2\sqrt n/(3\pi)+1/12-1/\pi^2+O(n^{-1/2})\). The corresponding odd-part expectation follows from the exact identity \(COS(n)+CES(n)=na(n)\). The negative square-root term establishes the eventual strict bias.

## Verification

Run `python3 check_cubic_even_mass.py` (Python 3 standard library only). Two independent exact-integer methods agree on all 126 coefficients through index 125: one uses the divisor-sum convolution and the other inserts each colored part independently with a marked even-size statistic. At indices \(100,200,400,800,1200\), the checker compares exact ratios with the Bessel expression and the three-term expression. It prints `CUBIC_EVEN_MASS_ASYMPTOTIC_DIAGNOSTICS_OK`. These finite calculations are diagnostics, not the proof of the coefficient-extraction lemma or the infinite asymptotic.

## Relationship to prior work

Bardhan–Saikia (2026) introduce the exact weighted sums \(COS\) and \(CES\), their Lambert-series formulas, and congruences modulo small primes. The present claim concerns the coefficientwise size-asymptotic average and its explicit square-root and constant corrections, not their congruences. Mauth (2024; corrected 2025) gives a Rademacher-type exact formula and asymptotics for the unweighted cubic count \(a(n)\), but not the weighted-even-mass numerator. Schlosser–Zhou (2025) study residue-class **part counts** and their bias in ordinary/distinct/overpartitions; their statistics and partition ensembles do not entail the displayed cubic size-weighted mass expansion. Standard eta, Eisenstein, and Bessel identities are used as established tools. No claim of priority beyond the literature checked is made.

## Limitations

No explicit effective lower bound for the eventual strict inequality is supplied. The proof applies specifically to cubic partitions with precisely two even colors. Its \(O(n^{-1/2})\) error is not evaluated with an explicit numerical constant. An unindexed or later-discovered general weighted-colored-partition asymptotic could contain this specialization; the overlap assessment is based on the cited and indexed literature rather than a proof of global uniqueness.

## References

1. G. Bardhan and N. Saikia, *Divisibility Properties of Odd Part and Even Part Sums in Cubic Partitions* (2026), arXiv:2611.05196v1, 2026-11-03. https://arxiv.org/html/2611.05196
2. L. Mauth, *Exact formula for cubic partitions*, Ramanujan Journal 64 (2024), 1323–1334, and its 2025 correction. https://doi.org/10.1007/s11139-024-00871-0
3. M. J. Schlosser and N. H. Zhou, *Residue class biases in unrestricted partitions, partitions into distinct parts, and overpartitions*, Research in the Mathematical Sciences 12 (2025), article 17. https://doi.org/10.1007/s40687-025-00502-0
4. NIST Digital Library of Mathematical Functions, §10.40, *Asymptotic Expansions for Large Argument: Modified Bessel Functions*. https://dlmf.nist.gov/10.40
