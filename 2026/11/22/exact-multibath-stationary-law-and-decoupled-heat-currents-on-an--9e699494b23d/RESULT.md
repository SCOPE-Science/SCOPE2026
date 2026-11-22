# Exact multibath stationary law and decoupled heat currents on an Ising star

## Finding

On an arbitrary finite Ising star with an independently infinite-temperature-driven hub, **all stationary spin correlations and the full joint distribution obey a triangular, subset-indexed formula**, even when every leaf has its own coupling, bath temperature and update rate. More sharply, each leaf-bath stationary heat current is exactly independent of the number and parameters of all other leaves, although different leaves have nonzero correlations induced by the same fluctuating hub.

For any integer \(n\ge1\), let the hub spin be \(C\in\{-1,+1\}\) and the leaves be \(\sigma_i\in\{-1,+1\}\), \(i\in[n]\), with energy
\[
\mathcal H(C,\sigma)=-\sum_{i=1}^n J_i C\sigma_i,
\qquad J_i>0.
\]
The hub is independently refreshed to a fair spin at rate \(c>0\); leaf \(i\) is heat-bath refreshed at rate \(\ell_i>0\) and inverse temperature \(\beta_i>0\). Write \(t_i=\tanh(\beta_i J_i)\in(0,1)\) and \(L_S=\sum_{i\in S}\ell_i\). For subsets \(S\subseteq[n]\), put
\[
A_S=\mathbb E_\pi\prod_{i\in S}\sigma_i,
\qquad B_S=\mathbb E_\pi C\prod_{i\in S}\sigma_i.
\]
The unique stationary probability law \(\pi\) has \(A_\varnothing=1\), \(B_\varnothing=0\), and, for every nonempty \(S\),
\[
\boxed{\displaystyle
A_S=\frac{\sum_{i\in S}\ell_i t_i B_{S\setminus\{i\}}}{L_S},
\qquad
B_S=\frac{\sum_{i\in S}\ell_i t_i A_{S\setminus\{i\}}}{c+L_S}.}
\]
Every one of the \(2^{n+1}\) state probabilities then follows from the exact Walsh inversion
\[
\boxed{\displaystyle
\pi(C=h,\sigma=s)=2^{-(n+1)}\sum_{S\subseteq[n]}
\bigl(A_S+hB_S\bigr)\prod_{i\in S}s_i,\qquad
h,s_i\in\{-1,+1\}.}
\]
In particular, for distinct leaves \(i,j\),
\[
\mathbb E_\pi(C\sigma_i)=\frac{\ell_i t_i}{c+\ell_i},\qquad
\mathbb E_\pi(\sigma_i\sigma_j)=
\frac{\ell_i\ell_j t_it_j}{\ell_i+\ell_j}
\left(\frac1{c+\ell_i}+\frac1{c+\ell_j}\right)>0.
\]
Writing \(u_i=\mathbb E_\pi(C\sigma_i)\), these exact formulas also give the **temperature-independent correlation amplification law**
\[
\boxed{\displaystyle
\frac{\mathbb E_\pi(\sigma_i\sigma_j)}{u_i u_j}
=1+\frac{2c}{\ell_i+\ell_j}>1,\qquad i\ne j.}
\]
The relative cross-leaf enhancement depends only on update rates, even when every leaf has a different physical temperature.

Let \(Q_a\) denote the stationary mean rate of energy transferred **from reservoir \(a\) to the spin system**. Then the exact current at leaf \(i\) and the compensating hub current are
\[
\boxed{\displaystyle
Q_i=-\frac{J_i c\ell_i t_i}{c+\ell_i}<0,
\qquad
Q_0=\sum_{i=1}^n\frac{J_i c\ell_i t_i}{c+\ell_i}=-\sum_iQ_i.}
\]
Thus one infinite-temperature reservoir supplies all the finite-temperature leaf reservoirs, with an additive, strictly positive entropy production rate
\[
\dot S_{\mathrm{tot}}=\sum_{i=1}^n\frac{\beta_i J_i c\ell_i\tanh(\beta_i J_i)}{c+\ell_i}>0.
\]
In this setting the energy-current decoupling is **exact despite the strictly positive cross-leaf correlations**.

When the leaf refresh rates coincide, \(\ell_i=\ell\), an additional closed positive-mixture expression describes every finite joint probability. Set \(\alpha=c/(2\ell)\). Define the classical symmetric beta density on \((-1,1)\)
\[
p_\alpha(z)=\frac{(1-z^2)^{\alpha-1}}{B(1/2,\alpha)},
\]
where \(B\) is the Euler beta function. Then
\[
\boxed{\displaystyle
\pi(C=h,\sigma=s)=\int_{-1}^1 p_\alpha(z)\,
\frac{1+hz}{2}\prod_{i=1}^n\frac{1+s_it_i z}{2}\,dz.}
\]
This exact finite-size mixture allows the leaf temperatures and couplings still to differ. As a familiar consequence of the telegraph-filter beta law, if also \(t_i=t>0\), the empirical mean \(n^{-1}\sum_i\sigma_i\) converges in distribution as \(n\to\infty\) to \(tZ\), \(Z\sim p_\alpha\), with nonzero limiting variance \(t^2\ell/(c+\ell)\). The limiting density changes from endpoint-peaked to uniform to center-peaked at \(c=2\ell\); this beta-law fact itself is **not** claimed to be new.

## Assumptions and scope

Each site's update clock is independent. When the hub clock rings at rate \(c\), it draws a fresh fair spin independent of all other variables: its effective flip rate is \(c/2\). When the clock at leaf \(i\) rings at rate \(\ell_i\), it draws \(+1\) with probability \((1+t_i C)/2\), and \(-1\) otherwise, where \(t_i=\tanh(\beta_i J_i)\). This is local continuous-time heat-bath dynamics for the indicated Ising Hamiltonian, with a hub at inverse temperature zero and arbitrary strictly positive leaf inverse temperatures. A redraw may leave a spin unchanged. The finite chain is irreducible because all conditional refresh probabilities are strictly positive. Currents use the sign convention ``reservoir to system'', and the hub temperature contributes zero to bath entropy flow. No infinite-volume phase transition is asserted.

## Proof

**1. Full subset-moment hierarchy.** For any function \(f\) of the spins, let \(\mathcal L f\) be the continuous-time generator. The resampling rule gives the exact local identities
\[
\mathcal L_i\sigma_i=\ell_i(t_i C-\sigma_i),
\qquad \mathcal L_0 C=-cC.
\]
Here \(\mathcal L_i\) acts only at site \(i\). Apply \(\mathcal L\) to \(\prod_{j\in S}\sigma_j\) for a nonempty subset \(S\). In the stationary law,
\[
0=-L_S A_S+\sum_{i\in S}\ell_i t_i B_{S\setminus\{i\}}.
\]
Applying it instead to \(C\prod_{j\in S}\sigma_j\) gives
\[
0=-(c+L_S)B_S+\sum_{i\in S}\ell_i t_i A_{S\setminus\{i\}}.
\]
For the empty set, normalization gives \(A_\varnothing=1\), while the hub identity gives \(B_\varnothing=\mathbb EC=0\). Since all denominators are strictly positive and only proper subsets occur on the right, induction on subset cardinality proves the displayed complete recursion, without any assumptions of independent leaves. Global spin reversal consequently makes all odd-total-degree moments vanish.

**2. Exact distribution and complete reconstruction.** For each spin sign \(h\) and leaf-sign vector \(s\), its configuration indicator expands as
\[
\mathbf1_{\{C=h,\sigma=s\}}=
2^{-(n+1)}(1+hC)\prod_{i=1}^n(1+s_i\sigma_i).
\]
Take expectations and expand the product to get the stated Walsh inversion. Since the original finite process is irreducible and has a unique stationary law, the recursion and inversion are not merely formal: they are the exact nonnegative probabilities of that law. Calculation needs \(O(n2^n)\) rational arithmetic operations for the moments and, by fast Walsh transform, \(O(n2^n)\) more for all probabilities when the model parameters are rational. Bit complexity is not claimed to be bounded by this arithmetic-operation count.

**3. Exact correlations and heat currents.** Taking \(S=\{i\}\) gives \(B_{\{i\}}=\ell_i t_i/(c+\ell_i)\); taking \(S=\{i,j\}\) gives the displayed strictly positive leaf-pair correlation. Dividing that correlation by \(B_{\{i\}}B_{\{j\}}\) and simplifying gives the exact, temperature-independent amplification ratio. A leaf refresh changes the bond energy by average \(J_iC(\sigma_i-t_iC)\), so stationarity yields its reservoir-to-system current
\[
Q_i=J_i\ell_i\bigl(\mathbb E(C\sigma_i)-t_i\bigr)
=-J_i c\ell_i t_i/(c+\ell_i).
\]
The hub refresh, which replaces \(C\) by a mean-zero sign, changes the whole system energy by average \(\sum_i J_iC\sigma_i\). Its current is therefore \(Q_0=c\sum_iJ_i B_{\{i\}}=-\sum_iQ_i\). For independent thermal reservoirs the total stationary entropy production is \(-\beta_0 Q_0-\sum_i\beta_i Q_i\); here \(\beta_0=0\), giving the claimed strictly positive sum. Nothing about the other leaves appears in a fixed \(Q_i\), even though their equal-time correlations are generally nonzero.

**4. Equal-rate beta mixture and its limit.** Suppose \(\ell_i=\ell\). The autonomous stationary hub is a symmetric telegraph process with flip rate \(c/2\). In a stationary realization of its entire past, define its exponentially filtered mean
\[
Z=\ell\int_0^\infty e^{-\ell u}C(-u)\,du\in[-1,1].
\]
Conditional on this past, the leaf update clocks and draws are independent. For every \(i\), the conditional leaf spin mean is \(t_iZ\), so the conditional leaf law depends on the past only through \(Z\) and factorizes. The joint stationary process \((Z,C)\) has deterministic velocity \(\dot Z=\ell(C-Z)\) between hub flips. If its stationary sign-resolved densities are \(p_+(z)\) and \(p_-(z)\), the zero-total-probability-flux relation inside \((-1,1)\) gives
\[
(1-z)p_+(z)=(1+z)p_-(z).
\]
Thus \(p_\pm=(1\pm z)p/2\) for \(p=p_++p_-\). The sign-state stationary balance equation, with flip rate \(c/2\), reduces to
\[
(1-z^2)p'(z)=2(1-c/(2\ell))z p(z).
\]
Its normalized integrable solution is exactly \(p=p_\alpha\) with \(\alpha=c/(2\ell)>0\). It has no endpoint atoms because the telegraph process flips at positive rate; the solution is also the standard stationary beta law of an exponentially filtered two-state Markov process. Combining the hub conditional probability \((1+hz)/2\) and the independent leaf conditional factors proves the finite-size mixture formula. If all \(t_i=t\), conditional independent bounded leaf spins have mean \(tZ\), so their empirical mean converges in probability conditional on \(Z\) to \(tZ\) by variance at most \(1/n\). As \(\operatorname{Var}(Z)=1/(2\alpha+1)\), the asserted limit and variance follow. The shape statement follows directly from the exponent \(\alpha-1\).

## Verification

The standalone `verify_heterogeneous.py`, using only Python's standard library, reconstructs the \(2^{n+1}\)-state probabilities from the subset recurrence and independently checks the full spin-flip master equation with rational transition rates, normalization, strict positivity, pair-correlation identities and reservoir current balance. For 21 instances of star sizes \(1\) through \(7\) with three combinations of hub rates, heterogeneous leaf rates and temperature factors, all 1,524 configuration stationarity checks passed exactly. In a separate loop, beta-mixture moment identities were checked exactly through size \(8\) for two rate families. Run `python verify_heterogeneous.py`. These are finite-instance checks; the arbitrary-size theorem follows from the generator and mixture proofs above.

## Relationship to prior work

Schmüser and Schmittmann (arXiv:cond-mat/0206345; first public June 18, 2002) study the two-temperature Glauber Ising chain with alternating site temperatures and develop nonequilibrium stationary-state calculations; their lattice geometry and thermally active site dynamics do not provide this autonomous-hub, arbitrary-multibath, all-order star law. Cornu and Hilhorst (arXiv:1701.06164) derive exact heat-current fluctuations for Ising chains with two thermostats; their chain and two-thermostat geometry do not state the leaf-by-leaf current decoupling here. 

An especially close published result is *An exact triangular stationary-law recursion for noisy voters on a star* (2026), which gives all finite stationary moments for a **homogeneous-rate noisy voter** star where the hub also copies leaves. Its zero hub-copying specialization and a matching common noise rate cover **a restricted common-leaf-rate parameter subfamily** of the present model; that overlapping special case is not asserted as original. Crucially, it does not give the arbitrary independent hub rate and heterogeneous leaf temperatures and rates, the Ising multibath current formula, or the full class of parameter sets here. Cox, Peres and Steif (arXiv:1408.5122) likewise analyze a noisy-voter star with hub copying and study mixing rather than this autonomous-hub multibath law. The classical stationary beta law for filtered telegraph processes is established, and Caligiuri and Galla (arXiv:2305.19096) use related switching-environment beta/PDMP calculations; beta behavior alone is not claimed novel here. The originality claim is restricted to the **joint arbitrary-heterogeneity all-order stationary formula plus decoupled heat currents**. Such a formula may have an earlier equivalent statement in general Markov-modulated binary populations or other exact stochastic-process treatments; historical priority has not been conclusively settled.

## Limitations

The hub reservoir must refresh independently at infinite temperature; the formulas are not asserted when hub updates depend on the leaf magnetization, when direct leaf-leaf edges are added, or when update clocks are dependent. The exact beta mixture requires equal leaf update rates, though the finite subset recursion and current law do not. Finite positive leaf temperatures and positive couplings ensure strict current inequalities. The beta density and its shape transition are classical telegraph-filter facts, and the previously published uniform-noise voter-star subfamily is covered prior art. The complete stationary law is exact but has exponentially many outputs. There is no claim of a finite-temperature phase transition or a universal current-decoupling law beyond independently driven hubs. Independent historical-priority and mathematical verification have not been performed.

## References

1. F. Schmüser and B. Schmittmann, *Non-equilibrium stationary state of a two-temperature spin chain*, arXiv:cond-mat/0206345, first submitted 2002-06-18, https://arxiv.org/abs/cond-mat/0206345.
2. F. Cornu and H. J. Hilhorst, *Glauber's Ising chain between two thermostats*, arXiv:1701.06164, submitted 2017-01-22, https://arxiv.org/abs/1701.06164.
3. J. T. Cox, Y. Peres and J. E. Steif, *Cutoff for the noisy voter model*, arXiv:1408.5122, submitted 2014-08-21, https://arxiv.org/abs/1408.5122.
4. A. Caligiuri and T. Galla, *Noisy voter models in switching environments*, arXiv:2305.19096, submitted 2023-05-30, https://arxiv.org/abs/2305.19096.
5. *An exact triangular stationary-law recursion for noisy voters on a star* (published 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-an-exact-triangular-stationary-law-recursion-for-noisy-voters-on--30693f2b8577.
