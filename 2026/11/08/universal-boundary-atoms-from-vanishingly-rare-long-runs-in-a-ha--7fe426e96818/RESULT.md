# Universal boundary atoms from vanishingly rare long runs in a harmonic active particle

## Finding

Let \(\kappa,v>0\), let \(G\) be a probability law on \((0,\infty)\) of finite mean \(\nu>0\), and fix \(\mu>\nu\). For \(L>\max\{\mu,\nu\}\), let the run durations be independent with law
\[
G_L=(1-p_L)G+p_L\delta_L,\qquad p_L=\frac{\mu-\nu}{L-\nu}.
\]
The propulsion sign \(\sigma_t\in\{-1,+1\}\) reverses at each renewal, and position satisfies \(\dot X_t=-\kappa X_t+v\sigma_t\). Write \(V=v/\kappa\), and let \(\pi_G,\pi_L\) be the stationary position laws at equilibrium renewal time for the two duration laws. Then
\[
\pi_L\Rightarrow \pi_\infty:=\frac{\nu}{\mu}\pi_G+\frac{\mu-\nu}{2\mu}(\delta_{-V}+\delta_V),\qquad
W_1(\pi_L,\pi_\infty)\le \frac{Vp_L}{\mu}\left(2\nu+\frac4\kappa\right),
\]
where the Wasserstein cost is \(|x-y|\). Although \(G_L\Rightarrow G\) and every \(G_L\) has the same mean \(\mu\), the stationary position laws do not converge to \(\pi_G\): the limit has an atom of mass \((\mu-\nu)/(2\mu)\) at each endpoint, whereas \(\pi_G\) has no endpoint mass.

**Fourth-cumulant sign reversal.** In units \(\kappa=v=1\), take \(G=\delta_{9/10}\) and \(\mu=1\). With \(a=\tanh(9/20)\), the limiting second and fourth moments and the limiting fourth cumulant are
\[
M_2=1-2a,\qquad M_4=1-2a-\tfrac23 a^3,\qquad
\mathcal K_4=-2+10a-12a^2-\tfrac23a^3>0.0329.
\]
For every \(L\ge300\), the finite-\(L\) stationary fourth cumulant is already positive. In contrast, exponential switching of the same mean \(1\) has fourth cumulant \(-2/15\).

## Assumptions and scope

There is no positional thermal noise. The base law can be discrete, continuous, or unbounded; only positivity and a finite first moment are required. Stationary position refers to observation at equilibrium time, not at a flip. Position lies in \([-V,V]\), so all stationary moments exist. For deterministic durations the equilibrium phase is uniform over the periodic orbit. This is a fixed-trap limit, not a simultaneous weak-trap or vanishing-mean limit.

## Proof

**Embedded chain.** At a run's start let \(Z=\sigma X/V\) with the new sign \(\sigma\). Within the run the position at age \(s\) is \(\sigma V[1+(Z-1)e^{-\kappa s}]\). At the next start the signed position is \(F_A(Z)=A-1-AZ\), where \(A=e^{-\kappa T}\). These maps preserve \([-1,1]\) and have Lipschitz factor \(A\). For any positive duration law, \(\mathbb EA<1\), so products of factors from the past tend to zero almost surely (the expectations decay geometrically). Iterating from the infinite past gives the unique stationary signed entry law on this interval. A fair sign, independent of the duration sequence, gives the symmetric alternating extension.

**Coupling at flips.** Write \(a_G=\mathbb E_G[e^{-\kappa T}]<1\). At each event use a common \(G\)-duration in both chains with probability \(1-p_L\); otherwise use \(L\) in the \(G_L\)-chain and an independent \(G\)-duration in the other. Use such pairs independently across events in the past. The factors satisfy \(\mathbb E|A_L-A_G|\le p_L\) and \(\mathbb EA_L\le(1-p_L)a_G+p_L\). Since \(|F_A(z)-F_B(w)|\le A|z-w|+2|A-B|\) on \([-1,1]\), independence of the upcoming duration pair from the entry pair gives, for \(d_0=\mathbb E|Z_L-Z_G|\),
\[
d_0\le\mathbb EA_L\,d_0+2p_L,\qquad
d_0\le\frac{2p_L}{(1-p_L)(1-a_G)}.
\]

**Equilibrium occupation and Wasserstein bound.** At stationary renewal time the interval law is length-biased and the age within the interval is uniform. Equivalently, for \(H=G,G_L\), with \(Z_H,\sigma,T\) taken at a typical run start,
\[
\pi_H(f)=\frac1{\mathbb E_HT}\mathbb E\int_0^T f\bigl(\sigma V[1+(Z_H-1)e^{-\kappa s}]\bigr)\,ds.
\]
At a run start \(T\) is independent of the entry law and the sign. Take \(f\) real 1-Lipschitz with \(f(0)=0\), so \(|f|\le V\) on the physical interval. On the ordinary runs, the integrand change caused by replacing \(Z_L\) with the coupled \(Z_G\) contributes at most
\[
\frac{(1-p_L)Vd_0}{\mu}\frac{1-a_G}{\kappa}\le\frac{2Vp_L}{\kappa\mu}.
\]
Replacing their weight \((1-p_L)\nu/\mu\) by \(\nu/\mu\) costs at most \(Vp_L\nu/\mu\). On the exceptional runs, approximation by \(f(\sigma V)\) costs at most \(2Vp_L/(\kappa\mu)\), because the distance to \(\sigma V\) at age \(s\) is at most \(2Ve^{-\kappa s}\). Their aggregate weight is \(p_LL/\mu\). Since \((1-p_L)\nu+p_LL=\mu\), replacing this weight by \((\mu-\nu)/\mu\) costs at most \(Vp_L\nu/\mu\). The fair sign splits the endpoint mass equally. Summing and using Kantorovich–Rubinstein duality proves the displayed rate.

Under either duration law the stationary past contains intervals of both signs of strictly positive lengths, so the stationary filter \(v\int_0^\infty e^{-\kappa s}\sigma_{-s}\,ds\) lies strictly between \(-V\) and \(V\) almost surely. This argument also applies at run starts. Conditional on the entry and the duration, the position as a function of the uniform age is thus strictly monotone with nonzero derivative on the run; changing variables in the age integral shows that the ordinary stationary position law is absolutely continuous. In particular \(\pi_G\) and every finite-\(L\) law have zero endpoint mass. As \(p_L\to0\), the bound proves the claimed weak convergence. The limit has an absolutely continuous component of mass \(\nu/\mu\) and a singular atomic component of total mass \((\mu-\nu)/\mu\). Hence convergence is not in total variation: the endpoint set alone has that mass in the limit and zero mass at every finite \(L\).

**Fourth-cumulant witness.** For deterministic duration \(t>0\) in units \(\kappa=v=1\), the orbit reaches \(\pm a_t\), where \(a_t=\tanh(t/2)\). A full period has length \(2t\). The two crossings of an interior point have speeds \(1-x\) and \(1+x\), so its equilibrium position density is
\[
q_t(x)=\frac{\mathbf1_{\{|x|<a_t\}}}{t(1-x^2)}.
\]
Integrating \(x^2\) and \(x^4\) gives \(1-2a_t/t\) and \(1-(2/t)(a_t+a_t^3/3)\). At \(t=9/10\), the limiting law gives mass \(9/10\) to this density and \(1/20\) to each endpoint. Substitution yields the stated moments and, by symmetry, \(\mathcal K_4=M_4-3M_2^2\).

For the strict numerical inequality, take \(u=9/10\), \(S=\sum_{j=0}^{14}u^j/j!\), and \(U=S+u^{15}/(15!(1-u/16))\). Then \(S<e^u<U\), and \((S-1)/(S+1)<a<(U-1)/(U+1)\). Substituting the lower bound in the positive linear term and the upper bound in the two negative powers gives \(\mathcal K_4>329/10000\) by rational arithmetic. The Wasserstein bound is \(\varepsilon_L=(29/5)(1/10)/(L-9/10)\). The observables \(x^2,x^4\) have Lipschitz constants \(2,4\) on \([-1,1]\), and the second moments are in \([0,1]\). Consequently
\[
|\mathcal K_{4,L}-\mathcal K_4|\le 16\varepsilon_L
=\frac{232}{25(L-9/10)}\le\frac{464}{14955}<\frac{329}{10000}\qquad(L\ge300).
\]
For exponential switching of mean \(1\), stationarity of \(x^k\) and \(\sigma x^{k-1}\) for the rate-one flipping dynamics gives \(\mathbb EX^k=\mathbb E[\sigma X^{k-1}]=(k-1)\mathbb EX^{k-2}/(k+1)\) for \(k\ge2\). Thus the exponential comparison has \(\mathbb EX^2=1/3\), \(\mathbb EX^4=1/5\), and fourth cumulant \(-2/15\).

## Verification

The companion `verify.py` checks the rational exponential enclosure, the finite-\(L\) sign inequality, deterministic-cycle moments, and a recursion for invariant affine moments at several finite choices of \(L\). It uses Python and the standard library. These calculations check the worked example; the general theorem and bound follow from the coupling and occupation proof above.

## Relationship to prior work and limitations

Farago and Smith formulate confined non-Markovian tumbling for general run-time distributions and develop a numerical stationary-distribution method. Their studied clocks include exponential, semi-Gaussian, and half-\(t\) laws. Sun, Ye and Podgornik give exact moments for a Markov model with finite-duration zero-propulsion tumble phases. Equilibrium length bias and the exponential telegraph stationary law are classical. The result here concerns the fixed-mean, rare-long-run stationary limit for a specific alternating-sign model, with a rate for the full position law and an explicit finite-duration cumulant witness. It does not address other reorientation rules or added thermal noise, and is not a claim of exhaustive priority.

## References

1. O. Farago and N. R. Smith, *Confined run and tumble particles with non-Markovian tumbling statistics*, https://arxiv.org/abs/2401.01576.
2. A. Sun, F. Ye and R. Podgornik, *Exact moments for a run and tumble particle with a finite tumble time in a harmonic trap*, https://arxiv.org/abs/2409.00578.
3. R. Garcia-Millan and G. Pruessner, *Run-and-tumble motion in a harmonic potential: field theory and entropy production*, J. Stat. Mech. 063203 (2021), DOI 10.1088/1742-5468/ac014d.
4. W. Whitt, *The renewal-process stationary-excess operator*, Journal of Applied Probability.
