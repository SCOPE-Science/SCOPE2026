# Two-scale Rayleigh-to-Gumbel spreading on \(K_{a,b}\) with finitely many hubs

## Finding
For each fixed integer \(a\ge 2\), consider continuous-time asynchronous push–pull broadcasting on \(K_{a,b}\), begun from exactly one informed vertex in the size-\(a\) part. Every vertex has an independent rate-one Poisson clock and calls a uniformly chosen neighbor, exchanging the rumour if either knows it. Let \(H_b(t)\) and \(L_b(t)\) count informed vertices in the parts of sizes \(a\) and \(b\); let \(C_b\) be the first time all vertices are informed. Define the accelerated process
\[
X_b(s)=\big(H_b(s/\sqrt b),\ L_b(s/\sqrt b)/\sqrt b\big),\qquad s\ge0.
\]
Then, as \(b\to\infty\), \(X_b\) converges in the Skorokhod \(J_1\) topology on each compact time interval to the piecewise-deterministic Markov process \(X=(H,Y)\) started at \((1,0)\), where
\[
Y(s)=\frac1a\int_0^s H(u)\,du,
\quad H:h\mapsto h+1\text{ at instantaneous rate }\frac{(a-h)Y(s)}a.
\]
The process reaches \(H=a\) at a finite time almost surely. Independently of the whole limiting early process, the centered completion time converges to a standard Gumbel random variable \(G\):
\[
\big(X_b,C_b-\log b\big)\ \Longrightarrow\ (X,G),\qquad
\Pr\{G\le x\}=\exp(-e^{-x}).
\]
If \(\tau_b\) denotes the first time a second hub becomes informed, then for every \(s\ge0\),
\[
\Pr\{\sqrt b\,\tau_b>s\}\longrightarrow
\exp\left(-\frac{a-1}{2a^2}s^2\right).
\]
The exact finite-\(b\) survival law is stated in the proof. In particular, for \(a=2\) the first-hub activation and final completion have asymptotically independent standard Rayleigh and standard Gumbel limits under the scalings \(\sqrt b\,\tau_b/2\) and \(C_b-\log b\).

## Assumptions and scope
The graph is a fixed unweighted complete bipartite graph \(K_{a,b}\). The integer \(a\ge2\) stays fixed while \(b\) tends to infinity through positive integers. Calls are independent Poisson rate-one processes and select a neighbor uniformly. The rumour persists after acquisition. Exactly one vertex of the size-\(a\) part is initially informed. Gumbel convergence concerns distribution, not expectation convergence. No assertion is made about growing \(a\), synchronous rounds, node failure, or weighted contacts.

## Proof
**1. Exact rate reduction and independent edge clocks.** Splitting each vertex's rate-one Poisson calls into independent directed-edge processes shows that each undirected edge carries an independent communication Poisson process of rate
\[
c_b=\frac1a+\frac1b.
\]
A crossing edge transmits whenever its ends have different information states. Thus \((H_b,L_b)\) is a finite pure-birth Markov chain with only the transitions
\[
(h,l)\longrightarrow(h,l+1)\text{ at rate }c_bh(b-l),\qquad
(h,l)\longrightarrow(h+1,l)\text{ at rate }c_b(a-h)l.
\]
These identities hold also on the boundary, where zero factors suppress impossible transitions.

**2. Early-scale generator convergence.** For a smooth function \(f(h,y)\) with compact support in its real coordinate, the accelerated chain has generator
\[
\begin{split}
\mathcal A_b f(h,y)={}&\sqrt b\,c_bh\left(1-\frac{y}{\sqrt b}\right)
\left[f(h,y+1/\sqrt b)-f(h,y)\right]\\
&+c_b(a-h)y\left[f(h+1,y)-f(h,y)\right].
\end{split}
\]
Its limit, uniformly on compact subsets of \(y\ge0\), is
\[
\mathcal A f(h,y)=\frac ha\partial_yf(h,y)+\frac{(a-h)y}{a}
\left[f(h+1,y)-f(h,y)\right].
\]
For completeness, on a compact accelerated interval \([0,S]\), the expected number of leaf infections is at most \(c_bab(S/\sqrt b)=O(\sqrt b)\), and the intensity for each hub birth is bounded on events with bounded scaled leaf counts. The leaf-coordinate martingale has predictable quadratic variation bounded by \(O(S/\sqrt b)\), and its drift differs uniformly on bounded sets from \(H/a\) by \(o(1)\). The hub-coordinate has at most \(a-1\) jumps; conditional on the leaf trajectory, its waiting times are governed by the integrated intensities displayed above. These observations give tightness, and every subsequential limit solves the \(\mathcal A\) martingale problem. It is unique by the explicit construction: between hub jumps \(Y\) grows at constant slope \(h/a\), and the next jump time has survival \(\exp[-\int (a-h)Y(u)/a\,du]\). Therefore \(X_b\Rightarrow X\) on each compact interval.

The limiting process satisfies \(Y(s)\ge s/a\). Whenever \(H<a\), its remaining jump rate is at least \(s/a^2\); hence the waiting time to the next jump is almost surely finite. With only \(a-1\) possible jumps, its all-hub time \(U\) is finite almost surely. By convergence of the non-simultaneous hub jumps, \(\sqrt b\,T_b^{\mathrm{hub}}\Rightarrow U\), where \(T_b^{\mathrm{hub}}\) is the first time every hub is informed. In particular \(T_b^{\mathrm{hub}}\to0\) in probability and \(L_b(T_b^{\mathrm{hub}})/b\to0\) in probability. For the latter, first restrict to \(T_b^{\mathrm{hub}}\le S/\sqrt b\), and use \(\mathbb E L_b(S/\sqrt b)=O(\sqrt b)\), then let \(S\to\infty\).

**3. Exact first extra-hub law.** Until a second hub is informed, each leaf has an independent first communication time \(E\sim\mathrm{Exp}(c_b)\) with the initially informed hub. Thereafter that leaf contacts any of the \(a-1\) uninformed hubs after an independent \(F\sim\mathrm{Exp}((a-1)c_b)\). The b independent two-edge candidates yield
\[
\Pr(\tau_b>t)=
\begin{cases}
\left[e^{-c_bt}(1+c_bt)\right]^b,&a=2,\\[2pt]
\left[\dfrac{(a-1)e^{-c_bt}-e^{-(a-1)c_bt}}{a-2}\right]^b,&a>2.
\end{cases}
\]
For small \(t\), \(\Pr(E+F\le t)=\tfrac12(a-1)c_b^2t^2+O(t^3)\). Setting \(t=s/\sqrt b\) and using \(c_b\to1/a\) proves the displayed Rayleigh survival limit. For \(a=2\), use \(t=2s/\sqrt b\) to obtain standard Rayleigh survival \(e^{-s^2/2}\).

**4. Late independent Gumbel.** After the stopping time \(T_b^{\mathrm{hub}}\), all hubs are informed. Each of the remaining \(R_b=b-L_b(T_b^{\mathrm{hub}})\) uninformed leaves then becomes informed at independent exponential rate \(a c_b=1+a/b\), by independent edge-clock increments. Consequently, conditionally on the history up to this stopping time,
\[
C_b\ \overset d=\ T_b^{\mathrm{hub}}+\max_{1\le j\le R_b}Z_j,
\quad Z_j\stackrel{\mathrm{iid}}\sim\mathrm{Exp}(1+a/b).
\]
Since \(T_b^{\mathrm{hub}}=o_{\mathbb P}(1)\) and \(R_b/b\to1\) in probability, for each real \(x\) the corresponding conditional completion CDF at \(\log b+x\) converges in probability to \(\exp(-e^{-x})\). Thus the Gumbel variable is asymptotically independent of all early hub activation times. To extend independence to the entire early path on \([0,S]\), replace the conditioning time by \(T_b^{\mathrm{hub}}\vee S/\sqrt b\), which is also \(o_{\mathbb P}(1)\) and leaves \(b-o_{\mathbb P}(b)\) susceptible leaves. The path \(X_b\) on \([0,S]\) is measurable at that time and the same conditional CDF argument applies. Joint finite-window convergence and consistency over \(S\) prove the asserted functional joint limit. \(\square\)

## Verification
The standalone `verify.py` uses the exact rational first-step recursions independently in a count-state chain and the full labeled informed-subset chain for \(a=2,3,4\) and \(b=2,3,4,5,6\). It also compares the exact \(a=2\) first-extra-hub mean computed by integrating its survival law with a separate first-step recursion for \(b=1,\ldots,14\), and compares analytic survival functions with numerical integration of the killed generator for 48 parameter/time triples. Finally it checks the convergence trend for the Rayleigh survival at one scaled time. These finite calculations test the exact rate model and finite law, but do not by themselves prove the asymptotic results; those rely on the preceding generator and conditional-extreme-value argument. Run with `python verify.py` using Python, NumPy, and SciPy.

## Relationship to prior work
Acan, Collevecchio, Mehrabian and Wormald (first preprint 2014) develop the asynchronous push–pull model, universal bounds and star examples. Pourmiri and Mans (first publicly available arXiv preprint May 16, 2020) give cut-rate and dynamic-network bounds, including explicit complete-bipartite substructures, but not fixed-width \(K_{a,b}\) two-scale distributional limits. Aalto and Leskelä (2014 preprint) prove initial/final extreme-value decompositions for directed transmission in homogeneously mixing transmitter/receiver populations with many transmitters, a different interaction structure; their assumptions do not imply the fixed-number-of-hubs model here. Doerr and Kostrygin (2023) study round-based protocols in fully connected networks, not these asynchronous bipartite distributions. The contribution assessed here is the fixed-\(a\) early PDMP, exact first-hub survival and the joint independent late Gumbel, not the general edge-clock representation or generic extreme-value theorem. This comparison is not a proof of absolute historical novelty.

## Limitations
The result is restricted to fixed \(a\) and initial infection of one hub. It makes no claim for growing \(a\), source infection in the large part, other communication mechanisms, finite-size optimality or convergence of mean completion times. The comparison with previous literature is limited to the identified sources; an overlooked specialization or independently derived formula remains possible. Independent mathematical validation has not been conducted.

## References
1. A. Pourmiri and B. Mans, *Tight Analysis of Asynchronous Rumor Spreading in Dynamic Networks*, arXiv:2005.07859, first version 2020-05-16, https://arxiv.org/abs/2005.07859.
2. H. Acan, A. Collevecchio, A. Mehrabian and N. Wormald, *On the push&pull protocol for rumour spreading*, arXiv:1411.0948, first version 2014-11-04, https://arxiv.org/abs/1411.0948.
3. P. Aalto and L. Leskelä, *Information spreading in a large population of active transmitters and passive receivers*, arXiv:1412.7563, first version 2014-12-23, https://arxiv.org/abs/1412.7563.
4. B. Doerr and A. Kostrygin, *Randomized Rumor Spreading Revisited (Long Version)*, arXiv:2303.11150, first version 2023-03-20, https://arxiv.org/abs/2303.11150.
