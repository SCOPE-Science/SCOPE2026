# Sharp modal staircase and resolution barrier for the wrapped Poisson–Lindley law

## Finding

**Theorem (complete fixed-origin modal phase diagram).** Let \(m\ge2\) be an integer, \(\theta>0\), and let \(R\in\{0,1,\ldots,m-1\}\) be the residue modulo \(m\) of a Poisson–Lindley random variable with parameter \(\theta\). Write \(w_{m,\theta}(r)=\Pr(R=r)\) and define

\[
H_m(\theta)=\frac1\theta-\theta-2-\frac{m}{(1+\theta)^m-1},
\qquad J_m=\max\left\{0,\left\lfloor\frac{m-4}{2}\right\rfloor\right\}.
\]

The masses are strictly log-concave at every interior residue, and the global modal sector follows a complete staircase. If \(H_m(\theta)<0\), the sole mode is \(0\); if \(H_m(\theta)>0\) is not an integer, the sole mode is \(\lceil H_m(\theta)\rceil\); if \(H_m(\theta)=j\) for an integer \(j\ge0\), the only two modes are the adjacent residues \(j,j+1\). The latter case occurs exactly at one parameter value \(\theta_{m,j}>0\) for each \(j=0,\ldots,J_m-1\), and never otherwise. The transition values are strictly ordered

\[
0<\theta_{m,J_m-1}<\cdots<\theta_{m,1}<\theta_{m,0},
\]

when there are at least two transitions. Every sector \(0,1,\ldots,J_m\) occurs as the sole mode on a nonempty interval of positive parameter values; **no sector above \(J_m\) can ever be globally modal**. Hence for \(2\le m\le5\), sector \(0\) is always the unique mode, while \(m=6\) is the smallest resolution at which a nonzero global mode is possible.

At \(m=6\), the sole transition \(\theta_{6,0}\) is the unique positive zero of

\[
3-16\theta-40\theta^2-44\theta^3-26\theta^4-8\theta^5-\theta^6=0,
\]

with the rigorously checked rational enclosure

\[
0.13478761972309<\theta_{6,0}<0.13478761972311.
\]

Moreover, as the resolution grows, the first transition has the sharp limit and rate

\[
\theta_{m,0}\uparrow\sqrt2-1,\qquad
\lim_{m\to\infty}\frac{\sqrt2-1-\theta_{m,0}}{m2^{-m/2}}
=\frac1{4+2\sqrt2}.
\]

This is a statement about *the original labeled sectors with fixed angular origin*, not a rotation-invariant location model.

## Assumptions and scope

The Poisson–Lindley parent on nonnegative integers is defined for \(\theta>0\) by

\[
\Pr(X=k)=\frac{\theta^2(k+\theta+2)}{(1+\theta)^{k+3}},
\qquad k=0,1,2,\ldots.
\]

The circular variable is \(2\pi R/m\) with \(R=X\bmod m\). All probability modes refer to maximizers of the \(m\) atom probabilities, with the sector labels \(0,\ldots,m-1\) fixed. For \(m=1\), the distribution has one atom and is excluded only to avoid vacuous adjacent comparisons. No assumption is made about data, a sample size, fitted parameters, or an additional angular-location parameter.

## Proof

Put \(q=1+\theta>1\) and \(A=q^m-1>0\). The nonnegative parent masses sum to one because the two elementary series for \(\sum_{k\ge0}q^{-k}\) and \(\sum_{k\ge0}kq^{-k}\) give \(\sum_{k\ge0}\Pr(X=k)=1\). Partitioning these nonnegative integers by residues and summing the same two geometric series gives the exact wrapped law

\[
w_{m,\theta}(r)=\frac{\theta^2q^{m-3}}{A}q^{-r}(r+b),
\quad b=\theta+2+\frac mA,
\quad 0\le r<m.
\]

The normalizing factor is strictly positive, and the formula follows directly from the normalized parent, so no unproved normalization is required. For \(0\le r\le m-2\),

\[
\frac{w_{m,\theta}(r+1)}{w_{m,\theta}(r)}
=\frac{r+b+1}{q(r+b)},
\qquad
w_{m,\theta}(r+1)>w_{m,\theta}(r)
\iff r<H_m(\theta).
\]

The ratio on the right is strictly decreasing in \(r\); equivalently \(w(r)^2>w(r-1)w(r+1)\) for every \(1\le r\le m-2\). A sequence with these strictly decreasing adjacent ratios has a unique mode at the first nonincreasing step, except when one ratio is exactly one, in which case precisely two adjacent atoms tie. This proves the modal formula from the sign of \(H_m(\theta)-r\), including all equality cases.

We next prove that the parameter traverses the thresholds once, in a fixed order. Differentiating,

\[
H_m'(\theta)=-\frac1{\theta^2}-1+
\frac{m^2q^{m-1}}{(q^m-1)^2}.
\]

Since \(q^m-1=\theta\sum_{k=0}^{m-1}q^k\), strict arithmetic–geometric mean for the nonconstant list \(1,q,\ldots,q^{m-1}\) gives

\[
\sum_{k=0}^{m-1}q^k>m q^{(m-1)/2},\qquad
\frac{m^2q^{m-1}}{(q^m-1)^2}<\frac1{\theta^2}.
\]

Therefore **\(H_m'(\theta)<-1\)** for all \(m\ge2\) and \(\theta>0\). Expanding the finite geometric sum around \(\theta=0\) gives

\[
\lim_{\theta\downarrow0}H_m(\theta)=\frac{m-5}{2},
\qquad \lim_{\theta\to\infty}H_m(\theta)=-\infty.
\]

For each integer \(j\ge0\), a unique positive solution of \(H_m(\theta)=j\) consequently exists if and only if \(j<(m-5)/2\). Such indices are precisely \(0,\ldots,J_m-1\). Strict decrease yields their strict ordering and realizes all modes \(J_m,J_m-1,\ldots,0\) on open parameter intervals. The upper bound on modes, the minimal \(m=6\) transition, and the absence of further ties follow.

For \(m=6\), the equation \(H_6(\theta)=0\) is equivalent, after multiplying by the strictly positive factor \(\theta A\), to

\[
(1-2\theta-\theta^2)((1+\theta)^6-1)-6\theta=0.
\]

Removing the positive factor \(\theta^2\) leaves the displayed sextic. At the two rational endpoints of the enclosure its values have opposite signs, as checked using exact fractions in `verify_wpl_modes.py`; strict monotonicity of \(H_6\) proves the unique root lies between them.

Finally, let \(t_*=\sqrt2-1\) be the positive root of \(B(t)=t^{-1}-t-2\). For fixed \(t>0\), the average \(m^{-1}\sum_{k=0}^{m-1}(1+t)^k\) increases strictly with \(m\), so \(m/((1+t)^m-1)\) decreases strictly. Thus \(H_m(t)\) increases with \(m\). Its unique zero \(t_m=\theta_{m,0}\) for \(m\ge6\) increases with \(m\), lies below \(t_*\), and converges to \(t_*\) because \(H_m(t)\to B(t)\) at each fixed \(t>0\). The identity

\[
B(t_m)=\frac{m}{(1+t_m)^m-1}
\]

and the mean-value theorem yield, for some \(\xi_m\in(t_m,t_*)\),

\[
t_*-t_m=\frac{m}{[(1+t_m)^m-1](1+\xi_m^{-2})}.
\]

As \(t_m\ge t_6>0\), the right side is \(O(m(1+t_6)^{-m})\); hence \(m(t_*-t_m)\to0\), and \((1+t_m)^m/(\sqrt2)^m\to1\). Since \(1+t_*=\sqrt2\) and \(1+t_*^{-2}=4+2\sqrt2\), the stated sharp exponential convergence follows. No numerical experiment is used to establish an infinite-dimensional or all-parameter assertion.

## Verification

Run `python3 verify_wpl_modes.py` using only Python's standard library. The program checks the exact wrapped-probability normalization, neighboring ratios, strict log-concavity, modal decisions, derivative/AM–GM inequalities for hundreds of rational parameter pairs, and the sextic enclosure with exact fractions. It also compares the closed form with finite direct wrap sums, and numerically diagnoses the large-resolution asymptotic. On the supplied version it reports `CHECK_OK 3863`.

The finite diagnostic checks are not substitutes for the infinite-series summation, strict derivative proof, or asymptotic argument given above. The exact root enclosure, unlike the asymptotic diagnostics, is established by fraction comparisons and analytic uniqueness.

## Relationship to prior work

Chesneau, Bakouch and Hussain [1] introduced the WPL law, derived its closed mass and adjacent recurrence, and illustrated varying shapes graphically. These distributional formulas are inputs, not discoveries claimed here. Their paper does not state the complete mode threshold diagram, the sharp \(m=6\) resolution barrier, or the large-\(m\) transition asymptotic in the inspected sections. Bell and Nadarajah's review [2] reproduces its density and data applications without these modal classifications.

An independently published result about the *different* wrapped discrete linear-exponential (WDLE) law [3] has a complete mode staircase and a half-circle restriction. Both laws have affine-geometric residue weights, so the adjacent-ratio technique is shared. However, the WDLE parent, parameter dependence and threshold function differ: its sectors can leave zero already at \(m=3\), whereas the WPL model cannot do so until \(m=6\). The present conclusion is therefore not a restatement or corollary of that theorem; its WPL-specific strict parameter monotonicity and resolution asymptotic are proved above. No exclusivity or exhaustive priority is claimed.

## Limitations

The result identifies *global* modes on the canonical labeled sectors. It does not imply that circular mean direction equals a modal sector, nor that the same absolute-sector bound holds after introducing a free rotation parameter. The proof does not address sampling variability, confidence intervals, or parameter-estimation quality. Known general results for weighted-geometric sequences may provide alternative proofs of the elementary adjacent-ratio step; independent historical-priority review remains valuable.

## References

1. C. Chesneau, H. S. Bakouch, T. Hussain, “Modeling and Applications to Circular Data with a Wrapped Poisson-Lindley Model,” *Journal of Mathematical Study* **55** (2022), 139–157. First publicly posted online 2022-02-10. DOI: https://doi.org/10.4208/jms.v55n2.22.03 . Full-text source: https://doc.global-sci.org/uploads/online_news/JMS/402c5d4883850fa0810ce6dcf572aa0f.pdf .
2. W. Bell, S. Nadarajah, “A Review of Wrapped Distributions for Circular Data,” *Mathematics* **12** (2024), 2440. DOI: https://doi.org/10.3390/math12162440 .
3. “The exact WDLE modal staircase and fixed-origin half-circle barrier,” public mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-the-exact-wdle-modal-staircase-and-fixed-origin-half-circle-barr--3bdb074628bd .
