# Exact conditional phase law and two-scale discrepancy for expanding circle maps

## Finding

Let \(T_b(x)=bx\pmod 1\) on the circle \(\mathbb T=\mathbb R/\mathbb Z\), with integer \(b\ge2\) and Haar-distributed initial state \(X\). For integers \(1\le n<m\), define its self-displacement phases \(U=(T_b^n(X)-X)\pmod1\) and \(Y=(T_b^m(X)-X)\pmod1\). Fix any half-open circular arc \(I=[a,a+L)\pmod1\) of length \(0<L<1\). The following gives the **complete conditional probability law** of the later displacement \(Y\) given the earlier phase constraint \(U\in I\), together with two sharp, distinct mixing metrics.

Set
\[
M=b^n-1,\quad N=b^m-1,\quad g=\gcd(M,N)=b^{\gcd(n,m)}-1,\quad u=M/g,\quad v=N/g.
\]
Then \(\gcd(u,v)=1\) and \(1\le u<v\). Define \(q=\lfloor vL\rfloor\), \(\theta=vL-q\), and the circular residual arc \(J=[va,va+\theta)\pmod1\); \(J\) is empty when \(\theta=0\). **The conditional density with respect to Haar measure** is
\[
\boxed{\quad f_{Y\mid U\in I}(y)=\frac{q+\mathbf1_J(uy\pmod1)}{vL}\quad}\qquad\text{for Haar-almost every }y\in\mathbb T.
\]

Write \(\nu\) for this conditional law and \(h\) for Haar probability. Its total-variation distance (supremum over all Borel sets) and its *single-circular-arc discrepancy* are respectively
\[
\boxed{d_{\mathrm{TV}}(\nu,h)=\frac{\theta(1-\theta)}{vL},\qquad
D_{\mathrm{arc}}(\nu,h):=\sup_{B\ \mathrm{circular\ arc}}|\nu(B)-h(B)|=\frac{\theta(1-\theta)}{uvL}.}
\]
Thus \(d_{\mathrm{TV}}=uD_{\mathrm{arc}}\), and both suprema are attained: the total-variation extremizer is the union of the \(u\) short arcs where \(f\) is largest, whereas one arc spanning an increasing portion of one period attains \(D_{\mathrm{arc}}\). Both expressions hold for arbitrary circular-arc starting point \(a\), including wrapping arcs.

An exact independence criterion follows:
\[
\boxed{\ U\in I\text{ is independent of the complete later phase }Y\ \Longleftrightarrow\ vL\in\mathbb Z.\ }
\]
For \(0<L<1\), this means precisely \(L=j/v\) for some \(1\le j\le v-1\). If \(0<L<1/v\), the conditional law occupies \(u\) disjoint arcs and has \(d_{\mathrm{TV}}=1-vL\) but \(D_{\mathrm{arc}}=(1-vL)/u\). In general, the sharp unconditional covariance bounds against a later-phase Borel target \(B\) and against any later-phase arc \(B\), respectively, are
\[
\sup_{B\ \mathrm{Borel}}|\mathbb P(U\in I,Y\in B)-Lh(B)|
=\frac{\theta(1-\theta)}{v},
\quad
\sup_{B\ \mathrm{arc}}|\mathbb P(U\in I,Y\in B)-Lh(B)|
=\frac{\theta(1-\theta)}{uv}.
\]
These equalities reveal the strict difference between unrestricted and connected-target correlations in the same dynamical system.

## Assumptions and scope

The circle is equipped with normalized Haar (Lebesgue) probability. The parameters are *all* integers \(b\ge2\), \(1\le n<m\), *all* half-open arcs \(I\) of length \(0<L<1\), and no restrictions on their starting points. The integer \(g\) is the greatest common divisor; \(u,v\) are coprime positive integers. All arc endpoints are irrelevant to probability and discrepancy because the laws have densities. The theorem concerns the two displacement phases of a **single** uniform initial point, not two independent points. 'Total variation' means \(\sup_B|\nu(B)-h(B)|\), without an additional factor of two.

## Proof

**1. Reduction to coprime circle multipliers.** We have \(U=MX\pmod1\) and \(Y=NX\pmod1\). The classical gcd identity \(\gcd(b^n-1,b^m-1)=b^{\gcd(n,m)}-1\) gives the stated \(g\). Let \(Z=gX\pmod1\); since multiplication by an integer preserves Haar probability, \(Z\) is uniform and \((U,Y)=(uZ,vZ)\pmod1\). The coprimality of \(u,v\) is automatic.

**2. Exact conditional density.** For almost every \(y\), the map \(z\mapsto vz\pmod1\) has exactly \(v\) inverse branches \(z_j=(y+j)/v\), each carrying equal conditional weight \(1/v\). Therefore
\[
\mathbb P(U\in I\mid Y=y)=\frac1v\sum_{j=0}^{v-1}\mathbf1_I\left(\frac{uy+uj}{v}\pmod1\right).
\]
Because \(u\) is coprime to \(v\), the residues \(uj\pmod v\) permute \(0,\ldots,v-1\). Counting the equally spaced \(v\)-grid points in the circular arc \(I\) gives exactly \(q\) complete turns and one additional membership precisely when \(uy\pmod1\in J\), with \(q=\lfloor vL\rfloor\) and \(J=[va,va+\theta)\pmod1\). Hence
\[
\mathbb P(U\in I\mid Y=y)=\frac{q+\mathbf1_J(uy\pmod1)}v.
\]
The marginal law of \(Y\) is Haar and \(\mathbb P(U\in I)=L\); Bayes' formula gives the stated conditional density. As a consistency check, the indicator has Haar mean \(\theta\), so the density integrates to \((q+\theta)/(vL)=1\).

**3. Total variation.** Since \(q-vL=-\theta\),
\[
f(y)-1=\frac{\mathbf1_J(uy\pmod1)-\theta}{vL}.
\]
Multiplication by \(u\) preserves Haar measure; the positive set has measure \(\theta\), where \(f-1=(1-\theta)/(vL)\), and the negative set has measure \(1-\theta\), where \(f-1=-\theta/(vL)\). Integrating its positive part gives \(d_{\mathrm{TV}}=\theta(1-\theta)/(vL)\), with the union of the positive arcs as an extremizer.

**4. Sharp single-arc discrepancy.** The signed density \(f-1\) has spatial period \(1/u\), and its integral over each period is zero. On each period the signed primitive rises with constant positive slope for a subinterval of length \(\theta/u\), then falls at constant negative slope back to its starting value. Its full oscillation is exactly
\[
\frac{1-\theta}{vL}\frac{\theta}{u}=\frac{\theta(1-\theta)}{uvL}.
\]
The integral over any (possibly wrapping) circular arc equals the difference of the primitive at its two endpoints, so its absolute value cannot exceed this oscillation. Choosing those endpoints at a positive-segment start and end attains it. Consequently \(D_{\mathrm{arc}}=d_{\mathrm{TV}}/u\). Multiplying these conditional discrepancies by \(\mathbb P(U\in I)=L\) gives both stated sharp covariance equalities.

**5. Resonance and limits.** A measure with density \(f\) equals Haar precisely if its total-variation distance is zero, which for \(0<L<1\) occurs exactly when \(\theta=0\), i.e. \(vL\) is an integer. If \(vL<1\), then \(q=0\) and \(\theta=vL\), giving the stated support and discrepancy formulas. No limit in \(n\) or \(m\) is needed for any equality.

## Verification

The accompanying standalone file `checker.py` computes the two-dimensional preimage geometry of \((MX,NX)\pmod1\) using rational endpoints, pushes the conditioned intervals forward to the later phase, reconstructs the exact piecewise-constant density, and directly integrates its positive part and signed primitive. This is an algorithmically different route from the coprime-grid argument. On direct execution the checker reported `PASS 914 exact rational direct-pushforward, TV and arc-discrepancy checks`. It includes examples of exact independence and nearly singular conditional support. This finite rational verification is corroborative; the proof above covers arbitrary permitted parameters.

## Relationship to prior work

Kirsebom, Kunde and Persson (arXiv:2003.01361, §6.1, Lemma 6.2 and equations (6.3)–(6.4)) use the same self-displacement integer multipliers, their gcd identity and a Fourier-resonance expansion to **bound** two-time correlations for shrinking symmetric self-return events. Those ingredients are acknowledged. The present conclusion differs in both object and strength: it gives the **full phase-conditional density for an arbitrary arc**, sharp total-variation distance, sharp *connected arc* discrepancy, an exact factor separating these metrics, and complete conditional independence resonances. In the inspected primary text these exact distributional statements are neither asserted nor proved. They could also be derived by further analysis of the published Fourier identity, so the novelty assertion is explicitly limited to the results actually inspected rather than claiming that prior methods are inapplicable.

He and Liao (arXiv:2302.05149) treat quantitative recurrence in a broad class of piecewise expanding maps, establishing recurrence criteria and estimates rather than the present exact conditional distribution for circle multipliers. A published exact covariance formula for **equal-radius symmetric** circle-return intervals and a sharp critical-window pair-correlation variance theorem were also inspected in full. The symmetric Bernoulli-polynomial covariance kernel is prior work, not newly claimed here: it is a restriction of a two-time joint law, whereas the present theorem computes the *entire later-phase law conditional on any circular arc* and both sharp discrepancy metrics. Other indexed results concern random compositions of distinct expanding maps and conditional moments for different systems.

## Limitations

The assumption that the initial state is Haar uniform is essential. The conclusion does not extend as stated to general smooth expanding noninteger maps, nonuniform invariant densities, or three or more conditioning times. This is not an independent publication-priority certification: a Fourier analysis of the earlier resonance identity, or differently indexed work, might contain an equivalent statement. Exact arithmetic checks are finite and cannot substitute for the proof. No independent mathematical audit has been performed.

## References

1. Maxim Kirsebom, Philipp Kunde and Tomas Persson, *On shrinking targets and self-returning points*, arXiv:2003.01361 (first public 2020-03-03), especially §6.1, Lemma 6.2 and equations (6.3)–(6.4). https://arxiv.org/abs/2003.01361
2. *Sharp second-moment inflation for expanding circle-map pair correlations*, publicly available mathematical finding (2026), full `RESULT.md`, especially the Bernoulli-polynomial symmetric two-frequency covariance calculation. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-second-moment-inflation-for-expanding-circle-map-pair-corr--d5c688b954c6
3. Yubin He and Lingmin Liao, *Quantitative recurrence properties for piecewise expanding maps on [0,1]^d*, arXiv:2302.05149 (first public 2023-02-10), especially recurrence results and intersection estimates. https://arxiv.org/abs/2302.05149
