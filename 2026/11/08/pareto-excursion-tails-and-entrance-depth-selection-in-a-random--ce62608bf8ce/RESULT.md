# Pareto excursion tails and entrance-depth selection in a random convex interval map

## Finding
Fix \(\kappa>0\). In the iid random interval-map family defined below, let \(R\) be the first return from \(Y=(1/2,1]\) to \(Y\), with the entrance point sampled from the probability \(\nu\) obtained by normalizing the distinguished conservative invariant measure on \(Y\). Put
\[
Z(y)=\log_2\frac{1}{y-1/2},\qquad C_\kappa=\int_Y Z(y)^\kappa\,\nu(dy).
\]
Then \(0<C_\kappa<\infty\), and for **every integer** \(n\ge1\),
\[
\boxed{\mathbb P(R>n)=n^{-\kappa}\int_Y\min\{Z(y),n\}^{\kappa}\,\nu(dy).}
\]
In particular, with a constant that may depend on \(\kappa\) and the stationary entrance law,
\[
\mathbb P(R>n)=C_\kappa n^{-\kappa}+O(2^{-n}/n),\quad
0\le C_\kappa-n^\kappa\mathbb P(R>n)
=\kappa\int_n^\infty z^{\kappa-1}\nu\{Z>z\}\,dz.
\]
There is also a **joint conditional rare-excursion law**: as integer \(n\to\infty\),
\[
\left(Z,R/n\right)\mid\{R>n\}\ \Rightarrow\ (\widehat Z,V),
\]
where \(\widehat Z\) has the \(Z^\kappa\)-size-biased entrance-depth distribution
\[
\mathbb P(\widehat Z\in dz)=\frac{z^\kappa}{C_\kappa}\,\nu_Z(dz),
\]
and \(V\) is independent of \(\widehat Z\), with \(\mathbb P(V>v)=v^{-\kappa}\) for \(v\ge1\). Consequently \(\mathbb E[R^s]<\infty\) exactly for \(0<s<\kappa\), and the full stationary invariant measure is finite exactly for \(\kappa>1\).

## Assumptions and scope
At every discrete time select an independent \(B\) with Pareto law \(\mathbb P(B>t)=t^{-\kappa}\) for \(t\ge1\), supported on \([1,\infty)\). The randomly selected map is
\[
T_B(x)=\begin{cases}
2x,&0\le x\le1/2,\\
(x-1/2)^B,&1/2<x\le1.
\end{cases}
\]
This is the \(\alpha=0\) specialization of the wide-entrance model (4.6) of Inoue--Toyokawa [1]; in their density parameterization it corresponds to \(\ell=\kappa+1\). Their Theorem 3.1 and Lemma 3.1 give a conservative, ergodic Lebesgue-equivalent \(\sigma\)-finite invariant measure \(\mu\), unique up to scale, and its induced stationary law on \(Y\). Condition (A) is satisfied because the left derivative is the constant \(2\). Therefore its density on \(Y\) is bounded above and below by positive constants. Normalize \(\nu(A)=\mu(A\cap Y)/\mu(Y)\); this is a probability because \(0<\mu(Y)<\infty\). The future parameter \(B\) at an entrance is independent of its entrance point. All statements concern annealed (random-composition) distributions and first returns to \(Y\), not quenched almost-sure laws or deterministic fixed-parameter iterates. Endpoint ambiguities have zero \(\nu\)-probability.

## Proof
**1. Exact return clock.** Starting at \(y\in Y\), the first map places the orbit at \(w=(y-1/2)^B=2^{-BZ(y)}\le1/2\). Subsequent left-branch iterates double \(w\) until they first lie strictly above \(1/2\). For \(w=2^{-s}\), \(s\ge1\), the minimal integer number of doublings is \(\lfloor s\rfloor\): at a noninteger \(s\) it gives \(2^{\lfloor s\rfloor-s}>1/2\), while at integer \(s\) it gives \(1\). Hence, including the first right-branch step,
\[
R(y,B)=1+\lfloor BZ(y)\rfloor.
\]
In particular, for any integer \(n\ge1\), \(\{R>n\}=\{BZ\ge n\}\). A fresh independent Pareto draw thus yields
\[
\mathbb P(R>n\mid Z=z)=\mathbb P(B\ge n/z)=\min\{1,(z/n)^\kappa\}.
\]
Integration over \(\nu\) proves the exact formula.

**2. Quantitative tail.** From the source theorem, \(d\nu/dy\le M\) on \(Y\), so for \(z\ge1\),
\[
\nu(Z>z)=\nu\big((1/2,1/2+2^{-z})\big)\le M2^{-z}.
\]
This implies all positive moments of \(Z\) are finite and \(C_\kappa>0\). Integrating the nonnegative part \(Z^\kappa-n^\kappa\) above \(Z>n\) by the layer-cake identity gives the exact deficit
\[
C_\kappa-n^\kappa\mathbb P(R>n)
=\kappa\int_n^\infty z^{\kappa-1}\nu(Z>z)\,dz.
\]
The exponential bound is \(O(n^{\kappa-1}2^{-n})\) for fixed \(\kappa>0\), hence the claimed \(O(2^{-n}/n)\) error in the probability. This estimate is uniform as \(n\to\infty\) for each fixed \(\kappa\), and no universal numerical value for \(C_\kappa\) is assumed.

**3. Joint conditional law.** For any bounded continuous \(f\) on \([1,\infty)\) and any fixed \(v\ge1\), conditioning on \(Z\), using the formula in Step 1 and the independent Pareto parameter gives
\[
\lim_{n\to\infty}n^\kappa\mathbb E\big[f(Z)\mathbf1_{\{R/n>v\}}\big]
=v^{-\kappa}\int f(z)z^\kappa\,\nu_Z(dz).
\]
For real \(v\), the integer event threshold is \(BZ\ge\lfloor nv\rfloor\) (with the usual harmless equality cases); pointwise convergence and the integrable bound proportional to \(Z^\kappa\) justify dominated convergence. Divide by \(n^\kappa\mathbb P(R>n)\to C_\kappa\). At every \(v\ge1\), the limiting mixed tail factors into the tilted \(Z\) law and a Pareto tail. Weak convergence of the first marginal, mixed tail convergence, and tightness from the marginal Pareto-tail bound establish joint weak convergence and independence. The limiting \(V\) has no atom at \(1\).

**4. Moments and total mass.** Since \(\mathbb P(R>n)\sim C_\kappa n^{-\kappa}\), the tail-sum or tail-integral formula shows \(\mathbb E[R^s]<\infty\) precisely for \(s<\kappa\) (for any \(s>0\)). In the induced-tower reconstruction of [1, Theorem 3.1, Lemma 3.1], normalized \(\nu\) is the base law and the total tower mass is proportional to \(\mathbb E_\nu R\). Therefore the invariant measure is finite if and only if \(\kappa>1\); at \(\kappa=1\) it diverges logarithmically.

## Verification
The included standalone Python program `checker.py` uses the standard library only. It separately enumerates exact-rational first-return orbits, checks the finite-threshold Pareto integration against independent quadrature for the **uniform entrance-point law** (a diagnostic, not a claim that \(\nu\) is uniform), and tests the convergence of the depth-tilt under that diagnostic law. It passes 834 finite checks. These calculations corroborate signs and normalization and are not substitutes for the infinite-parameter proof above. With uniformly sampled entrance points on \(Y\), for comparison only, \(Z\) has law \(1+\operatorname{Exp}(\log2)\), and
\[
\mathbb E[Z^\kappa]=\frac{2\,\Gamma(\kappa+1,\log2)}{(\log2)^\kappa}.
\]
This is **not** asserted as the stationary constant \(C_\kappa\).

## Relationship to prior work
Inoue and Toyokawa [1, §4.6, Proposition 4.6, Remark 4.5] introduce this right branch and bound the near-zero invariant mass, proving in particular that the Pareto family yields infinite stationary mass for \(\kappa\le1\). Their [1, Theorem 3.1, Lemma 3.1] supplies the induced stationary measure used here. The result above instead concerns the **exact return-time distribution** at an induced stationary entrance, a sharp asymptotic constant and exponentially small correction, the full conditional entrance-depth/Pareto overshoot law, and the converse finite-mass criterion at \(\kappa>1\). General inducing and heavy-tail product theory provide context [2,3], but cannot determine this map's particular return-time observable without Step 1. The distinct low-slope piecewise-linear example of [1, §4.1] has an additive return clock and does not give this multiplicative law.

## Limitations
The stationary density \(\nu\) is known to exist and to be bounded but is not given here in closed form; \(C_\kappa\) is an exact stationary expectation, not a claimed universal explicit number. This is an annealed result for \(\alpha=0\), iid Pareto parameters, and stationarity on the induced section. It does not treat \(\alpha>0\), general heavy-tailed laws, quenched limit distributions, or correlations between successive excursions. General renewal/regular-variation literature could contain an equivalent deduction; a later journal version of [1] and other relevant full texts were not all accessible for a complete publication-priority comparison. Independent mathematical review has not been performed.

## References
[1] T. Inoue and H. Toyokawa, *Invariant measures for random piecewise convex maps*, arXiv:2303.10873v1 (first public 20 March 2023), especially Theorem 3.1, Lemma 3.1, §4.6, Proposition 4.6 and Remark 4.5; https://arxiv.org/html/2303.10873v1. Journal version: *Nonlinearity* 37 (2024), 055016, DOI:10.1088/1361-6544/ad2ff9.

[2] T. Inoue, *First return maps of random maps and invariant measures*, *Nonlinearity*, DOI:10.1088/1361-6544/ab4c83 (general induced-measure background; full text not inspected).

[3] J. Aaronson, *An Introduction to Infinite Ergodic Theory*, AMS (1997), cited by [1] for uniqueness and tower foundations; no claim is made that its contents supply the specific law above.
