# Critical source-pinned SIS occupation on a star: an exponential crossover constant

## Finding

Fix \(c>0\). On the star with a central vertex \(h\), one permanently infected leaf \(s\), and \(n\ge1\) ordinary leaves, run the continuous-time susceptible-infected-susceptible (contact) process with infection transmission rate \(\lambda_n=c/\sqrt n\) per infected-to-susceptible edge and recovery rate one at every nonpermanent infected vertex. Denote its unique stationary law by \(\pi_n\), the infection indicator of \(h\) by \(H_n\), and the number of infected ordinary leaves by \(K_n\).

**Theorem.** As \(n\to\infty\),
\[
\sqrt n\,\mathbb P_{\pi_n}(H_n=1)\longrightarrow\frac{e^{c^2}-1}{c},
\qquad
\mathbb E_{\pi_n}K_n\longrightarrow e^{c^2}-1.
\]
Both errors are \(O_c((\log n)^2/\sqrt n)\) after scaling the first observable as displayed. This specifies a natural inverse-square-root transmission window: the hub is infected with probability of order \(n^{-1/2}\), yet the expected number of infected nonpermanent leaves approaches a strictly positive nonlinear function of \(c\).

## Assumptions and scope

The permanent source \(s\) never recovers and has exactly one neighbor, \(h\). All arrows on distinct oriented graph edges are independent rate-\(\lambda_n\) Poisson processes; nonpermanent vertices recover at independent rate-one times. Only ordinary leaves are included in \(K_n\), not the source. The stationary chain on the hub and ordinary leaves is finite, irreducible and has a unique distribution. The limiting parameter \(c\) is fixed and strictly positive; the estimates are not uniform in an unbounded sequence of \(c\)'s. This theorem concerns a single forced leaf, not spontaneous infection at all vertices or the SIS chain conditioned on nonextinction.

## Proof

**1. The unforced star and its occupation potential.** Remove the permanent source and consider the ordinary contact process on the star with hub \(h\) and \(n\) leaves, starting with the hub infected and all leaves healthy, and stopping at the extinction time \(\tau_n\). Write \(X_t\in\{0,1\}\) for the hub indicator and \(L_t\) for the infected-leaf count, and put
\[
S_n=\int_0^{\tau_n}X_t\,dt,\qquad a=c^2,\qquad z=\lambda_n L_t.
\]
When the hub is healthy, infected leaves recover at total rate \(k\) and reinfect the hub at rate \(\lambda_n k\). When it is infected, it recovers at rate one, gives births to ordinary leaves at rate \(\lambda_n(n-k)\), and infected leaves recover at rate \(k\). These exhaust the transitions.

Define smooth functions on \([0,\infty)\) by
\[
v(z)=\int_0^1e^{t(a-z)}\,dt,\qquad
u_0(z)=\int_0^zv(y)\,dy,\qquad
u_1(z)=u_0(z)+v(z).
\]
Here \(u_0(0)=0\) and \(u_1(0)=(e^a-1)/a\). Direct differentiation and integration by parts give the **exact continuous equations**
\[
-z u_0'(z)+z\bigl(u_1(z)-u_0(z)\bigr)=0,
\]
\[
(a-z)u_1'(z)+u_0(z)-u_1(z)=-1.
\]
Indeed \(u_0'=v\), \(u_1'=\int_0^1(1-t)e^{t(a-z)}dt\), and the last identity follows by integrating the derivative of \((1-t)e^{t(a-z)}\) over \([0,1]\).

Let \(\mathcal L_n\) denote the exact generator of the unforced count process \((X_t,L_t)\). Taylor's theorem applied to \(u_x(\lambda_n k)\), using the rates above and \(n\lambda_n^2=a\), shows
\[
\sup_{x\in\{0,1\},\,0\le k\le n}\left|\mathcal L_n u_x(\lambda_n k)+x\right|\le C_c\lambda_n.
\]
This is a **uniform** estimate, including \(k=0,n\), not merely a bounded-\(k\) approximation. For clarity, the finite-generator error comes from the drift correction \(-\lambda_n z u_1'(z)\) and second-order finite differences; the quantities \(\sup_{z\ge0}z|u_1'(z)|\), \(\sup_{z\ge0}z|u_0''(z)|\), \(\sup_{z\ge0}(a+z)|u_1''(z)|\) are finite by their integral representations and the exponential factor \(e^{-tz}\). At the boundaries nonexistent transitions are simply omitted.

**2. Uniform extinction moments.** At \(\lambda_n=c/\sqrt n\), the unforced process satisfies, uniformly over **every** initial state,
\[
\mathbb E\tau_n\le C_c\log(n+2),\qquad
\mathbb E\tau_n^2\le C_c(\log(n+2))^2.
\]
Here is a block proof. Dominate each ordinary leaf by an independent two-state birth/death process with its hub kept infected. Starting from any state, after \(2\log n\) time units the expected number of infected leaves is at most \(c\sqrt n+1\). Markov's inequality therefore gives probability bounded away from zero of having at most \(C_c\sqrt n\) infected leaves. In the next unit time interval the total potential hub-to-leaf births are dominated by a rate-\(n\lambda_n=c\sqrt n\) Poisson process. With another uniformly positive probability this leaves at most \(C_c\sqrt n\) infected leaves. Independently, a hub recovery mark appears during that interval with fixed positive probability, and suppressing all leaf-to-hub infection arrows until the interval ends has probability at least \(e^{-C_c\lambda_n\sqrt n}>0\). Thus with probability bounded below independently of the initial configuration the hub ends this interval healthy, with at most \(C_c\sqrt n\) infected leaves. While the hub remains healthy, every infected leaf has an independent recovery clock of rate one, and the total leaf-to-hub reinfection rate is \(\lambda_n k\) at leaf count \(k\). Consequently the probability that all these leaves recover before any hub reinfection is exactly \((1+\lambda_n)^{-k}\ge e^{-C'_c}>0\); conditional on that event their extinction time is a sum of exponentials of rates \(j(1+\lambda_n)\), \(1\le j\le k\), so with probability bounded away from zero it is at most \(2\log n\). Combining events yields a constant \(p_c>0\) probability of extinction during a block of at most \(5\log n\), from every starting state. Iterating blocks by the Markov property bounds the extinction time by a geometric number of such blocks, proving both moment estimates for all sufficiently large \(n\); finitely many small \(n\) are absorbed into the constants.

Dynkin's formula for the bounded finite-state potential \(u_{X_t}(\lambda_n L_t)\), stopped at extinction where \(u_0(0)=0\), now gives
\[
\mathbb E S_n=u_1(0)+O_c\bigl(\lambda_n\mathbb E\tau_n\bigr)
=\frac{e^{c^2}-1}{c^2}+O_c\left(\frac{\log n}{\sqrt n}\right).
\]

**3. Stationary dual representation.** In the Harris graphical construction, trace the infection state of the hub backward from stationarity. Without arrows from the forced source, the ancestor set evolves exactly as the unforced contact process started from the hub, until extinction. Source-to-hub arrows form an independent Poisson process of rate \(\lambda_n\); a source arrow hits the backward ancestors exactly when the hub is an ancestor. Thus, conditional on the unforced ancestral occupation time \(S_n\), the probability of at least one effective arrow is \(1-e^{-\lambda_n S_n}\). This proves the exact identity
\[
p_n:=\pi_n(H_n=1)=\mathbb E\bigl[1-e^{-\lambda_n S_n}\bigr].
\]
The elementary inequality \(0\le y-(1-e^{-y})\le y^2/2\) and \(S_n\le\tau_n\) show
\[
0\le\lambda_n\mathbb ES_n-p_n\le\frac{\lambda_n^2}2\mathbb E\tau_n^2
=O_c\!\left(\frac{(\log n)^2}{n}\right).
\]
Inserting the occupation asymptotic gives
\[
p_n=\frac{c}{\sqrt n}\frac{e^{c^2}-1}{c^2}+O_c\!\left(\frac{(\log n)^2}{n}\right),
\]
which proves the first claimed limit and its error.

**4. Ordinary-leaf balance.** Applying stationary generator balance to the observable \(K_n\) yields exactly
\[
\mathbb E_{\pi_n}K_n=\lambda_n\,\mathbb E_{\pi_n}\bigl[H_n(n-K_n)\bigr].
\]
In particular \(0\le\mathbb E K_n\le n\lambda_n p_n=O_c(1)\), and \(0\le\lambda_n\mathbb E[H_nK_n]\le\lambda_n\mathbb E K_n=O_c(n^{-1/2})\). Hence
\[
\mathbb E K_n=n\lambda_n p_n+O_c(n^{-1/2})=e^{c^2}-1+O_c\!\left(\frac{(\log n)^2}{\sqrt n}\right),
\]
completing the proof.

## Verification

A standalone verifier in `verify.py` builds exact labeled-state Markov generators and the independent permutation-symmetric count generators for several small star sizes and rational transmission rates. It compares all count-state probabilities, the exact hub dual-hit formula, leaf-moment stationarity, and unforced hub-occupation linear systems. Independent banded and sparse solvers test larger finite sizes at several critical-window couplings; numerical tests evaluate the limiting Poisson equations and the finite-generator residual. Execute `python verify.py` with Python 3 and the available NumPy, SciPy, and SymPy libraries. The reported successful replay contains 268 assertions. Those checks corroborate the derivation but are not used to infer the infinite-size theorem from finite data. The displayed proof supplies the extinction and generator estimates that justify the limit.

## Relationship to prior work

Cator and Van Mieghem study ordinary star SIS dynamics using two distinct nonextinction regularizations (spontaneous infection at all vertices and suppressed final recovery) and determine a threshold of order \(\sqrt{\log n/n}\); neither regularization fixes **one peripheral** infected source. Cai, Wu and Holme explicitly simulate a star with one permanently infected leaf in Appendix B, at fixed rate and size, and replace measured distributions by averages in an approximation; that section does not give the inverse-square-root stationary law or its exact exponential prefactor. Huang and Durrett study unforced contact-process extinction and metastable survival on stars, rather than the stationary density induced by a pinned peripheral vertex. Schwartz and Stone provide a general exact-state star SIS analysis; only its abstract was available for comparison, so possible indirect coverage remains an unresolved historical-priority risk. The result also follows neither from a graph's adjacency spectral radius alone nor from the first-order mean-field threshold: it uses an occupation-time dual and uniformly controlled excursions.

## Limitations

The result concerns the finite, exactly defined CTMC, fixed \(c>0\), one permanently infected leaf, and all-leaf homogeneous rates. It does not prove a limiting distribution for \(K_n\), any uniform statement when \(c\to\infty\), a threshold for a contact process with no permanent source, or a general-graph theorem. The literature comparison is provisional rather than a claim of complete historical priority: the Schwartz–Stone full text was inaccessible, and semantic database searches cannot certify uniqueness. Independent scientific verification has not been performed.

## References

1. E. Cator and P. Van Mieghem, *Susceptible-infected-susceptible epidemics on the complete graph and the star graph: Exact analysis*, Physical Review E 87, 012811 (2013), https://doi.org/10.1103/PhysRevE.87.012811. First public date verified as 2013-01-23.
2. C.-R. Cai, Z.-X. Wu, and P. Holme, *Multistage onset of epidemics in heterogeneous networks*, arXiv:2103.05881 (2021), https://arxiv.org/abs/2103.05881, especially Appendix B and Figure B1.
3. X. Huang and R. Durrett, *The Contact Process on Random Graphs and Galton-Watson Trees*, arXiv:1810.06040 (2018), https://arxiv.org/abs/1810.06040, particularly the star-graph discussion.
4. N. Schwartz and L. Stone, *Exact epidemic analysis for the star topology*, Physical Review E 87, 042815 (2013), https://doi.org/10.1103/PhysRevE.87.042815 (abstract consulted; full text unavailable).
