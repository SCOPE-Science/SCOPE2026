# Sharp \(2k-3\) attack-size ranking reversals among equal-mean susceptibility mixtures

## Finding
Consider two populations with distinct fixed susceptibility laws, each supported on at most \(k\ge2\) types, and with identical mean susceptibility. Both obey a homogeneous-infectivity SIR fluid model with the same initial fractions \(s_0>0\), \(i_0>0\), \(r_0\ge0\), \(s_0+i_0+r_0=1\). As the transmission-to-recovery ratio \(\eta\) varies over all positive values, their total final *new-infection fractions* can agree at no more than \(2k-3\) distinct values. This upper bound is attained as strict sign-changing crossings for every \(k\). If the two laws are identical, the final fractions instead agree at every positive ratio.

For two types, take
\[
\mu_A=\tfrac23\delta_2+\tfrac13\delta_4,\qquad
\mu_B=\tfrac16\delta_1+\tfrac56\delta_3.
\]
Both have mean \(8/3\), hence the same initial reproduction number at each fixed contact strength. For \((s_0,i_0,r_0)=(9/10,1/10,0)\) the two final attack fractions agree only at
\[
\eta_*=\frac{160\log2}{133}.
\]
Below this value A has the smaller attack fraction, and above it B has the smaller attack fraction. The crossing is strict.

## Assumptions and scope
For each population let \(\mu\) be a probability law on \([0,\infty)\) supported on at most \(k\) points. Each initially susceptible individual's susceptibility is drawn from \(\mu\), held fixed throughout susceptible life, and does not alter infectiousness. In the deterministic infinite-population limit, recovery occurs at rate \(\gamma>0\) and mass-action transmission at rate \(\beta>0\), with \(\eta=\beta/\gamma\). Separate experiments begin from identical positive seed \(i_0\), initial susceptible \(s_0\) and removed \(r_0\), and vary only \(\eta\). Let \(z_\mu(\eta)\) be the eventual fraction of the total population newly infected among the initial susceptibles. This is not the initially infected share.

The bound on the number of ties assumes \(\mu_A\ne\mu_B\). The same-mean condition is \(\int \lambda\,d\mu_A=\int\lambda\,d\mu_B\). It does not require equal variance or equal class masses. Equality of initial reproduction numbers follows because susceptibility enters only acquisition and infectiousness is homogeneous.

## Proof
**1. Final-size comparison as a Laplace-transform comparison.** Write \(G_\mu(a)=\int e^{-a\lambda}\,d\mu(\lambda)\). The cumulative infection pressure \(a(t)=\beta\int_0^t i(u)du\) gives \(s(t)=s_0G_\mu(a(t))\) and \(r(t)=r_0+a(t)/\eta\). At the terminal state, \(i(\infty)=0\), so \(a=a_\mu(\eta)>0\) uniquely solves
\[
\frac a\eta=1-r_0-s_0G_\mu(a)=:H_\mu(a),
\qquad z_\mu(\eta)=\frac a\eta-i_0=s_0[1-G_\mu(a)].
\]
Indeed \(H(0)=i_0>0\), \(H\) is increasing and concave, and \(H(a)\le1-r_0\). Consequently \(a/H(a)\) is strictly increasing from zero to infinity: its derivative has the sign of
\[
H(a)-aH'(a)=i_0+s_0\int[1-(1+a\lambda)e^{-a\lambda}]\,d\mu(\lambda)>0.
\]
Thus every positive pressure \(a\) corresponds to a unique ratio \(\eta=a/H_\mu(a)\).

The two attack curves agree at a ratio \(\eta\) if and only if the two terminal pressures agree, because \(z=a/\eta-i_0\). At that common positive pressure \(a\), the two Laplace transforms agree. Conversely, if \(G_A(a)=G_B(a)\) for \(a>0\), then the ratio \(\eta=a/[1-r_0-s_0G_A(a)]\) is common and unique, and the attack fractions agree. This correspondence preserves increasing order of crossings because \(a/H_\mu(a)\) increases strictly. At simple zeros the attack-size ranking reverses: at fixed positive \(a\), higher \(G\) means smaller newly infected fraction and a larger ratio needed to reach that pressure.

**2. Universal sharp upper bound.** The signed difference \(D(a)=G_A(a)-G_B(a)\) is a nontrivial exponential polynomial with at most \(2k\) distinct real exponents. A nonzero real exponential sum with \(m\) distinct real exponents has at most \(m-1\) real zeros counted with multiplicity. For completeness, divide by the lowest exponential; its derivative has \(m-1\) terms, and induction plus Rolle's theorem yields this zero bound, including multiplicity. Normalization implies \(D(0)=0\), and equal mean gives \(D'(0)=0\), so zero has multiplicity at least two. Hence at most \((2k-1)-2=2k-3\) strictly positive zeros, hence at most that many positive ratios where final attack fractions tie. If \(D\equiv0\), uniqueness of finite exponential sums gives identical laws; they are excluded.

**3. Attainment for every \(k\).** Choose arbitrary distinct numbers \(0<q_1<\cdots<q_{2k-3}<1\), and define
\[
P(x)=(1-x)^2\prod_{j=1}^{2k-3}(x-q_j)=\sum_{n=0}^{2k-1}c_nx^n.
\]
All roots of this degree-\(2k-1\) polynomial are positive. Therefore every coefficient is nonzero, and the signs strictly alternate, with exactly \(k\) positive and \(k\) negative coefficients. Since \(P(1)=P'(1)=0\), the positive coefficients and the absolute values of the negative coefficients have the same total mass \(C>0\) and the same first moment when attached to susceptibility rates \(n+1\). Normalize the positive and negative collections by \(C\) to obtain two distinct probability laws \(\mu_A\), \(\mu_B\), each with exactly \(k\) positive atoms and the same mean. Their transform difference is
\[
G_A(a)-G_B(a)=\frac{e^{-a}}C P(e^{-a}).
\]
Its strictly positive zeros are exactly \(a_j=-\log q_j\), all simple, with alternating signs. By step 1 they yield exactly \(2k-3\) strict attack-size ranking reversals at the corresponding distinct positive transmission-to-recovery ratios. This completes sharpness.

**4. Two-type exact calculation.** For \(k=2\) and \(q_1=1/2\), the polynomial is \(P(x)=x^3-\tfrac52x^2+2x-\tfrac12\), giving the two laws displayed above. At \(a=\log2\), both transforms equal \(3/16\); hence \(H(a)=1-(9/10)(3/16)=133/160\), proving the exact \(\eta_*\). The sign of \((1-e^{-a})^2(e^{-a}-1/2)\) gives the claimed orientation of the unique crossing.

## Verification
The standalone file `verify_crossings.py` constructs the signed-polynomial witnesses using exact rational arithmetic for \(k=2,3,4,5\); checks normalization and equal means exactly; computes the predicted crossing ratios; solves the SIR final-size equation by bisection; and checks the reversal behavior numerically. It passed 68 numerical and exact-arithmetic assertions in the supplied environment. These finite tests do not prove the all-\(k\) result; that follows from the exponential-sum zero bound and constructive factorization above.

## Relationship to prior work
Izyumtseva, KhudaBukhsh, Gomes and Rempala establish the heterogeneous Sellke/SIR fluid limit, its Laplace-transform final-size relation, and the finite-discrete susceptibility closure. Those are inputs, not new claims. Novozhilov's earlier heterogeneous epidemic theory likewise obtains final-size transforms and shows that moments alone do not determine an epidemic's final size. Classical exponential-polynomial Chebyshev theory supplies the zero-count principle; the present result couples it to the parameter-dependent SIR terminal-pressure map and gives a sharp **equal-mean, all-class-number** epidemic risk-ranking reversal construction. Work on heterogeneous network SIR epidemics with mixed acquisition and infectivity concerns a different comparison and is not an implication of the present susceptible-only result. Historical priority should be checked independently, particularly for applications of total positivity to epidemic outcome rankings.

## Limitations
The theorem concerns exact deterministic fluid-limit final sizes and noiseless variation of a *known* transmission/recovery ratio; it is not an inference stability bound. Repeated epidemics in one population may alter the starting susceptibility distribution, violating the assumptions. It does not cover susceptibility–infectiousness correlation, changing mixing structure, finite stochastic outbreak probabilities, or arbitrary within-population susceptibility variation with infinitely many atoms. The number \(2k-3\) counts isolated *positive* crossing ratios, not monotonicity changes within one population's (itself increasing) attack curve.

## References
1. O. Izyumtseva, W. R. KhudaBukhsh, M. G. M. Gomes and G. A. Rempala, *From Individual-Based Stochastic Epidemics to Heterogeneous SIR Equations*, arXiv:2608.22122v1, first public August 22, 2026. https://arxiv.org/abs/2608.22122
2. A. S. Novozhilov, *Epidemiological Models With Parametric Heterogeneity: Deterministic Theory for Closed Populations*, Mathematical Modelling of Natural Phenomena 7 (2012), 147–167, DOI 10.1051/mmnp/20127310. https://doi.org/10.1051/mmnp/20127310
3. A. Leibenzon and M. Assaf, *Heterogeneity can markedly increase final outbreak size in the SIR model of epidemics*, arXiv:2306.09024 (2023); Physical Review Research 6, L012010 (2024). https://arxiv.org/abs/2306.09024
