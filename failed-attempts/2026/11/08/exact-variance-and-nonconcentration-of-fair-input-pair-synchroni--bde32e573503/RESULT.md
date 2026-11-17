# Exact variance and nonconcentration of fair-input pair synchronization in odd Černý automata

## Finding

For each odd integer \(n\ge3\), let \(\mathcal C_n\) have states \(\{0,\ldots,n-1\}\), a letter \(b\) acting by \(b(i)=i+1\pmod n\), and a letter \(a\) acting by \(a(0)=1\) and \(a(i)=i\) for \(i\ne0\). Every input letter is sampled independently and uniformly from \(\{a,b\}\). Define \(T_n\) to be the number of letters read before the images of the initially distinct states \(\{1,(n+1)/2\}\) first coincide. The clock starts at zero.

**Theorem.** For all these \(n\),
\[
\mathbb ET_n=\frac{(n-1)(2n^2-n-1)}2,
\qquad
\operatorname{Var}(T_n)=\frac{n(n-1)}6(4n^4-8n^3+3n^2+7n-14).
\]
The mean agrees with Gusev's previously established result; the variance is the new identity. Moreover,
\[
\lim_{n\to\infty\atop n\ \mathrm{odd}}\frac{\operatorname{Var}(T_n)}{(\mathbb ET_n)^2}=\frac23,
\qquad
T_n/\mathbb ET_n\not\longrightarrow1\quad\text{in probability}.
\]
Here and below the limit is through odd integers only.

## Assumptions and scope

The input letters are independent with \(\Pr(a)=\Pr(b)=1/2\); the theorem does not assert the same formula at other letter probabilities, for even \(n\), for a uniformly random initial pair, or for the time to synchronize *all* states. The automaton itself is fixed, not sampled randomly. A pair is regarded as merged once both images become equal, and it then remains merged. Every moment exists: a deterministic reset word has positive probability of occurring in each disjoint block of a fixed length, implying a geometric upper tail.

Write \(n=2m+1\), where \(m\ge1\). Each unordered distinct pair has one and only one representation \((i,\ell)\) standing for \(\{i,i+\ell\pmod n\}\), where \(0\le i<n\) and \(1\le\ell\le m\). Add an absorbing state \(\mathbf z\). The cycle letter sends \((i,\ell)\) to \((i+1\pmod n,\ell)\). The defect letter fixes the pair coordinate except for the transitions
\[
(0,1)\to\mathbf z,\quad (0,\ell)\to(1,\ell-1)\ (2\le\ell\le m),
\quad(n-\ell,\ell)\to(n-\ell,\ell+1)\ (1\le\ell<m),
\quad(m+1,m)\to(1,m).
\]
These identities follow directly by applying \(a\) to both states and taking the unique shorter oriented cyclic gap.

## Proof

**1. First-moment coordinates.** Let \(\mu_{i,\ell}\) denote expected remaining letters to absorption from the indicated pair, and define \(h_\ell=\mu_{1,\ell}\), \(e_\ell=\mu_{0,\ell}\), and \(h_0=0\). At every nonspecial state the defect letter is a self-loop, so the fair-letter first-step equation gives \(\mu_{i,\ell}=\mu_{i+1,\ell}+2\) (with a cyclic index where appropriate). At the special states it gives
\[
e_\ell=1+\tfrac12(h_{\ell-1}+h_\ell),\qquad
h_\ell=4m+\tfrac12(e_\ell+e_{\ell+1})\quad(1\le\ell<m),\qquad
h_m=6m+e_m.
\]
Consequently \(2h_\ell-h_{\ell-1}-h_{\ell+1}=16m+4\) for \(1\le\ell<m\), with \(h_m-h_{m-1}=12m+2\). The unique solution with \(h_0=0\) is
\[
h_\ell=(16m^2+8m)\ell-(8m+2)\ell^2,\qquad
h_m=8m^3+6m^2.
\]
In particular the displayed mean is recovered, as in [1]. The first moments at every pair-coordinate state are
\[
\mu_{0,\ell}=e_\ell,\quad
\mu_{i,\ell}=h_\ell-2(i-1)\quad(1\le i\le n-\ell),\quad
\mu_{i,\ell}=e_\ell+2(n-i)\quad(n-\ell+1\le i\le n-1).
\]
This formula will determine the inhomogeneous terms for the second moment.

**2. Second-moment first-step equation.** Set \(M_{i,\ell}=\mathbb E_{(i,\ell)}T^2\), \(H_\ell=M_{1,\ell}\), \(E_\ell=M_{0,\ell}\), and \(H_0=0\). Write \(r_{i,\ell}=4\mu_{i,\ell}-2\). Since \(T=1+T'\), the mean first-step identity implies at every transient pair
\[
2M_{i,\ell}=M_{a(i,\ell)}+M_{b(i,\ell)}+r_{i,\ell},
\]
where absorption contributes zero. Along each nonspecial arc this reduces to \(M_{i,\ell}=M_{i+1,\ell}+r_{i,\ell}\).

For \(1\le\ell\le m\) let \(L_\ell=2m-\ell\), and define the arc sums and special-state increments
\[
\begin{aligned}
A_\ell&=\sum_{i=1}^{n-\ell-1}r_{i,\ell}
=L_\ell(4h_\ell-2)-4L_\ell(L_\ell-1),\\
B_\ell&=\sum_{i=n-\ell+1}^{n-1}r_{i,\ell}
=(\ell-1)(4e_\ell-2)+4\ell(\ell-1),\\
u_\ell&=r_{n-\ell,\ell}=4(h_\ell-2L_\ell)-2,\\
v_\ell&=r_{0,\ell}=4e_\ell-2.
\end{aligned}
\]
An empty sum is zero. Thus \(M_{n-\ell,\ell}=H_\ell-A_\ell\) and \(M_{n-\ell+1,\ell}=E_\ell+B_\ell\). The special state at \(i=0\) gives \(2E_\ell=H_{\ell-1}+H_\ell+v_\ell\). For \(\ell<m\), the special state at \(i=n-\ell\) gives
\[
2(H_\ell-A_\ell)=E_\ell+B_\ell+E_{\ell+1}+B_{\ell+1}+u_\ell.
\]
Eliminating the \(E\)-terms yields
\[
2H_\ell-H_{\ell-1}-H_{\ell+1}=F_\ell
:=4A_\ell+2(B_\ell+B_{\ell+1}+u_\ell)+v_\ell+v_{\ell+1},\quad 1\le\ell<m.
\]
The top-row special transition at \((m+1,m)\) instead yields
\[
H_m-H_{m-1}=F_*
:=4A_m+2B_m+2u_m+v_m.
\]
These recurrences also hold when \(m=1\): the interior range is simply empty.

**3. Telescoping and exact polynomial.** Substituting the explicit first moments into the preceding quantities and collecting terms gives
\[
\begin{aligned}
F_\ell={}&-4(64\ell^2m^2+32\ell^2m+4\ell^2
-128\ell m^3-96\ell m^2+4\ell-4m+1),\\
F_*={}&2(96m^4+88m^3-16m^2+2m-1).
\end{aligned}
\]
The difference recurrences, \(H_0=0\), and the top boundary condition telescope to the exact identity
\[
H_m=mF_*+\sum_{\ell=1}^{m-1}\ell F_\ell
=\frac{2m}{3}(160m^5+240m^4+98m^3+16m^2-3m-4).
\]
Subtract \(h_m^2=(8m^3+6m^2)^2\). After factorization,
\[
\operatorname{Var}(T_n)
=\frac{2m(2m+1)}3(32m^4+32m^3+6m^2+5m-4)
=\frac{n(n-1)}6(4n^4-8n^3+3n^2+7n-14).
\]
This proves the first assertion for every odd \(n\ge3\); no interpolation or finite computation is used as an infinite proof.

**4. Nonconcentration.** The polynomial formulas show \(\mathbb ET_n\sim n^3\) and \(\operatorname{Var}(T_n)\sim\tfrac23 n^6\). A positive limiting coefficient of variation alone would not establish nonconvergence in probability, so we also establish uniform integrability. From the explicit first moments, \(h_\ell\le h_m\), \(e_\ell\le h_m+1\), and all transient pair means are bounded by \(h_m+1+2n=O(n^3)\). Let \(R_n\) be the maximum of those means. Markov's inequality followed by the Markov property yields \(\Pr(T_n>2k\lceil R_n\rceil)\le2^{-k}\) for all positive integers \(k\). It follows that \(\sup_{n\ \mathrm{odd}}\mathbb E[(T_n/n^3)^4]<\infty\). Therefore \((T_n/n^3)^2\) is uniformly integrable. If \(T_n/\mathbb ET_n\to1\) in probability, then \(T_n/n^3\to1\) in probability, forcing \(\mathbb E[(T_n/n^3-1)^2]\to0\), contrary to the positive variance limit \(2/3\). Thus synchronization fails to concentrate on its mean scale.

## Verification

The included `verify_moments.py` requires Python 3.10 or later and SymPy. Run `python verify_moments.py` from the directory containing the file. It independently verifies the symbolic moment summation and constructs the **unordered-pair** absorbing Markov chain directly from the two letters, without using the proof's reduced coordinates. It solves rational linear systems for \(n=3,5,7,9,11\), obtaining respectively \((\mathbb ET_n,\operatorname{Var}T_n)=(14,142),(88,5320),(270,49294),(608,248448),(1150,886270)\). These finite checks detect possible indexing and algebra errors but are not the basis of the theorem for arbitrary \(n\).

## Relationship to prior work

Gusev [1], Theorem 3.1, derives the mean for the odd Černý pair for general Bernoulli input; its fair-letter specialization is the mean displayed here. We do not claim that mean as novel. Gusev's inspected primary text does not provide the absorption-time variance or a nonconcentration theorem. Gonze and Jungers [2] study a different synchronizing-probability function (an optimization/game quantity) and deterministic triple-rendezvous time; these do not imply the fair-input pair first-passage second moment. The current contribution is the exact all-odd-size variance identity and consequent nonconcentration argument.

## Limitations

The formula is restricted to fair iid letters, an odd number of states, and the specified initial pair, not full-state synchronization. The result determines the first two moments and nonconcentration, but not the limiting distribution or higher moment asymptotics. The literature comparison supports originality to the extent of the inspected sources; an unindexed equivalent result remains a possible historical-priority risk. Independent mathematical validation has not been performed.

## References

[1] V. V. Gusev, *Synchronizing automata with random inputs*, 2014 preprint, first public version 27 April 2014. https://arxiv.org/abs/1404.6731. Section 3, Theorem 3.1 and its proof.

[2] F. Gonze and R. M. Jungers, *On the synchronizing probability function and the triple rendezvous time for synchronizing automata*, 2014 preprint, first public version 15 October 2014. https://arxiv.org/abs/1410.4034.
