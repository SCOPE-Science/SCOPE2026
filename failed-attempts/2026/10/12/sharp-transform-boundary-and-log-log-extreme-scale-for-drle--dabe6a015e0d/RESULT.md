# Sharp transform boundary and log-log extreme scale for DRLE
## Finding
Let \(X\) have the discrete Ramos–Louzada exponential (DRLE) distribution obtained by survival discretization of the continuous Ramos–Louzada exponential model with
\[
\alpha>0,\qquad \beta\ge2.
\]
Write
\[
\lambda=\frac{\alpha}{\beta},
\qquad
q=e^{-\lambda},
\qquad
c=\frac{\alpha}{\beta(\beta-1)}
=\frac{\lambda}{\beta-1}.
\]
The continuous parent survival is
\[
S(x)=(1+cx)e^{-\lambda x}.
\]
Therefore survival discretization gives the exact lattice survival
\[
\boxed{
S_n=\Pr(X\ge n)=(1+cn)q^n,
\qquad n=0,1,2,\ldots .
}
\]

The probability mass function is consequently
\[
\boxed{
p_n=q^n(A+Bn),
}
\]
where
\[
A=1-q(1+c)>0,
\qquad
B=c(1-q)>0.
\]
The positivity of \(A\) follows from
\[
1+\frac{\lambda}{\beta-1}
\le1+\lambda<e^\lambda.
\]

The probability generating function is
\[
\boxed{
G(z)
=
\frac{A}{1-qz}
+
\frac{Bqz}{(1-qz)^2},
\qquad |z|<q^{-1}.
}
\]
Its radius of convergence is exactly
\[
\boxed{
R_G=q^{-1}=e^{\alpha/\beta}.
}
\]
Accordingly, the ordinary probabilistic moment-generating function satisfies the sharp domain statement
\[
\boxed{
M(t)=\mathbb E[e^{tX}]<\infty
\quad\Longleftrightarrow\quad
t<\frac{\alpha}{\beta}.
}
\]
For \(t<\alpha/\beta\),
\[
M(t)
=
\frac{A}{1-qe^t}
+
\frac{Bqe^t}{(1-qe^t)^2}.
\]
At \(t=\alpha/\beta\), the summands satisfy
\[
e^{tn}p_n\sim Bn,
\]
and therefore the defining expectation diverges. For \(t>\alpha/\beta\), the summands grow exponentially. Thus values of the rational expression outside its convergence domain are not values of a probabilistic MGF.

The discrete hazard has the exact closed form
\[
\boxed{
h_n
=
1-q-\frac{qc}{1+cn}.
}
\]
Hence it is strictly increasing and
\[
\boxed{
h_n\longrightarrow1-q=1-e^{-\alpha/\beta},
\qquad
(1-q)-h_n\sim\frac{q}{n}.
}
\]

The upper quantile also has a sharp second-order scale. If \(Q(1-u)\) denotes the smallest integer \(n\) with
\[
\Pr(X\le n)\ge1-u,
\]
then
\[
\boxed{
Q(1-u)
=
\frac{\beta}{\alpha}
\left[
\log\!\left(\frac1u\right)
+
\log\log\!\left(\frac1u\right)
-
\log(\beta-1)
\right]
+O(1)
}
\]
as \(u\downarrow0\).

Thus the DRLE tail is geometric with a linear prefactor. That prefactor is asymptotically invisible at first logarithmic order but creates both the double-pole transform boundary and the explicit \(\log\log(1/u)\) correction in extreme quantiles.

## Assumptions and scope
The parameter domain is
\[
\alpha>0,\qquad\beta\ge2,
\]
matching the continuous Ramos–Louzada exponential parent used by the DRLE construction.

The survival discretization convention is
\[
\Pr(X\ge n)=S(n).
\]
The stated quantile expansion is lattice-accurate up to \(O(1)\); no claim is made that the bounded integer-rounding phase converges.

The MGF statement concerns the expectation
\[
\mathbb E[e^{tX}],
\]
not analytic continuation of its closed-form rational expression. A rational formula can be evaluated algebraically beyond the power-series radius without representing a finite expectation there.

All positive polynomial moments are finite, since the PMF has geometric decay. The finding focuses instead on the sharp positive-exponential boundary and the extreme-count correction.

## Proof
Survival discretization of
\[
S(x)=(1+cx)e^{-\lambda x}
\]
gives
\[
S_n=(1+cn)q^n.
\]
Therefore
\[
p_n=S_n-S_{n+1}
=
q^n\left[
1+cn-q(1+c(n+1))
\right]
=
q^n(A+Bn),
\]
with
\[
A=1-q(1+c),
\qquad
B=c(1-q).
\]

Since \(\beta\ge2\),
\[
c=\frac{\lambda}{\beta-1}\le\lambda,
\]
and
\[
q(1+c)
\le e^{-\lambda}(1+\lambda)<1,
\]
so \(A>0\).

For \(|qz|<1\),
\[
\sum_{n\ge0}q^n z^n=\frac1{1-qz}
\]
and
\[
\sum_{n\ge0}nq^n z^n=\frac{qz}{(1-qz)^2}.
\]
Thus
\[
G(z)
=
\frac{A}{1-qz}
+
\frac{Bqz}{(1-qz)^2}.
\]
Because
\[
p_n\sim Bnq^n,
\]
the root test gives the exact radius
\[
R_G=q^{-1}.
\]

Putting \(z=e^t\), the defining MGF series converges exactly when
\[
qe^t<1,
\]
which is
\[
t<-\log q=\lambda=\frac{\alpha}{\beta}.
\]
At equality its terms are asymptotic to \(Bn\), and above equality the terms do not approach zero.

For the hazard,
\[
h_n
=
1-\frac{S_{n+1}}{S_n}
=
1-q\frac{1+c(n+1)}{1+cn}
=
1-q-\frac{qc}{1+cn}.
\]
The correction term is positive and strictly decreasing in \(n\), proving monotone increase. Moreover,
\[
\frac{qc}{1+cn}\sim\frac qn.
\]

For the quantile, define \(m_u\) as the positive real solution of
\[
(1+cm_u)e^{-\lambda m_u}=u.
\]
The lattice quantile differs from \(m_u\) by at most a bounded amount because the event
\[
\Pr(X>n)\le u
\]
is equivalent to
\[
S_{n+1}\le u.
\]
Let
\[
L=\log(1/u).
\]
Taking logarithms gives
\[
\lambda m_u
=
L+\log(1+cm_u).
\]
Since \(m_u\sim L/\lambda\),
\[
\log(1+cm_u)
=
\log L+\log(c/\lambda)+o(1).
\]
Because
\[
\frac c\lambda=\frac1{\beta-1},
\]
we obtain
\[
m_u
=
\frac1\lambda
\left[
L+\log L-\log(\beta-1)
\right]
+o(1).
\]
Restoring the lattice rounding gives the displayed \(O(1)\) quantile formula.

## Verification
The accompanying checker evaluates the exact survival and PMF for several parameter pairs, including the two simulation scenarios publicly described for the DRLE article.

It verifies normalization of the PMF, the exact hazard identity, monotonicity of the hazard, convergence of
\[
n\{(1-q)-h_n\}
\]
to \(q\), and the tail ratio
\[
\frac{p_n}{Bnq^n}\to1.
\]
It also evaluates MGF partial sums below, at, and above the predicted boundary and verifies that only the below-boundary sums stabilize.

Finally, it computes exact lattice upper quantiles by monotone search and checks that subtracting
\[
\frac{\beta}{\alpha}
\left[
\log(1/u)+\log\log(1/u)-\log(\beta-1)
\right]
\]
leaves a bounded lattice-scale residual over increasingly small tail probabilities.

These calculations are consistency checks. The convergence domain, hazard rate, and quantile expansion are proved analytically above.

## Relationship to prior work
Alazwari et al. introduce the DRLE distribution by discretizing the survival function of its continuous counterpart. Their public record states that the PMF, CDF, survival, hazard, and moment-generating function are derived analytically, and that the hazard is increasing. The accessible public record does not expose the full formula section, so whether it explicitly records the maximal MGF convergence domain cannot be resolved from that material alone.

Aljohani et al. define the continuous Ramos–Louzada exponential parent and give
\[
S(x)
=
\left(
1+\frac{\alpha x}{\beta(\beta-1)}
\right)e^{-\alpha x/\beta},
\]
which fixes the DRLE lattice survival under the stated survival discretization.

Eldeeb, Ahsan-ul-Haq, and Eliwa treat the earlier one-parameter discrete Ramos–Louzada model. Their full text gives a rational PGF and an MGF obtained by substituting \(e^t\) into it, but the displayed MGF formula is not accompanied there by the maximal power-series convergence domain. That one-parameter model is recovered from the same linear-geometric structural mechanism, but it does not state the two-parameter DRLE extreme-quantile correction above.

Focused searches using the target DOI, DRLE name, MGF convergence, PGF radius, hazard-limit, quantile, and Lambert-\(W\) aliases did not locate the sharp transform boundary plus extreme-scale theorem stated here.

## Limitations
The full formula section of the 2026 DRLE article was not exposed through the accessible public interface during this comparison. The article is therefore retained as a residual originality risk for any overlap with its undisplayed MGF derivation.

The quantile expansion is stated only through \(O(1)\), which is the natural resolution for a lattice distribution without specifying a subsequential rounding phase.

The theorem concerns mathematical tail and transform structure. It does not reassess the paper's estimation procedures, simulations, or empirical goodness-of-fit conclusions.

## References
1. A. A. Alazwari, A. M. Karakaş, F. Bulut, E. Hussam, M. Ahsan-ul-Haq, S. Alzubaidi, A. Alrumayh, and M. E. Sobh, “New discrete Ramos–Louzada exponential–type distribution with applications to biological and COVID-19 data,” AIMS Mathematics 11 (2026), 27018–27055. DOI: 10.3934/math.20261083.
2. H. M. Aljohani, F. M. Zaghdoun, M. A. Meraou, A. S. Alharthi, W. A. J. Almohri, Z. I. Kalantan, A. A. EL-Helbawy, E. Hussam, and A. H. Muse, “A novel extension of the exponential distribution with application in modeling complex lifetime and environmental data,” Scientific Reports 15 (2025), 33581. DOI: 10.1038/s41598-025-18711-6.
3. A. S. Eldeeb, M. Ahsan-ul-Haq, and M. S. Eliwa, “A discrete Ramos-Louzada distribution for asymmetric and over-dispersed data with leptokurtic-shaped: properties and various estimation techniques with inference,” AIMS Mathematics 7 (2022), 1726–1741. DOI: 10.3934/math.2022099.
