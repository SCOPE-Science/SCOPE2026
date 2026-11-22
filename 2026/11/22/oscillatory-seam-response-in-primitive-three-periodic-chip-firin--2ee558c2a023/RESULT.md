# Oscillatory seam response in primitive three-periodic chip firing on cubic ladders

## Finding
For every integer \(n\ge3\), let \(P_n=C_n\square K_2\) be the labelled prism with two parallel cyclic rails and \(n\) rungs. Let \(M_n\) have the same labelled vertices and rung edges but replace the two closing rail edges with the crossed pair (the Möbius ladder). Under ordinary synchronous parallel chip firing, denote the number of **primitive temporal period-three orbits** on each graph by \(N_P(n)\) and \(N_M(n)\), counted once per temporal orbit and without identifying spatial symmetries.

Define the three integer monic polynomials
\[
\begin{aligned}
A(z)&=z^4+2z^3+12z^2+5z+1,\\
B(z)&=z^4+4z^3+6z^2+z+1,\\
C(z)&=z^5-6z^4+5z^3+z^2+6z-1.
\end{aligned}
\]
For any of these polynomials let \(S_A(n),S_B(n),S_C(n)\) be the sum of the \(n\)th powers of its complex roots with algebraic multiplicities, and put \(e_n=2\) if \(3\mid n\), and \(e_n=-1\) otherwise. The exact all-size orbit counts are
\[
\boxed{N_P(n)=\frac23\bigl(9+3e_n+2S_A(n)+2S_B(n)+S_C(n)\bigr),}
\]
\[
\boxed{N_M(n)=\frac23\bigl(-1+e_n-2S_A(n)+2S_B(n)+S_C(n)\bigr).}
\]
In particular, the signed effect of twisting one seam is exactly
\[
\boxed{N_P(n)-N_M(n)=\frac23\bigl(4S_A(n)+10+2e_n\bigr).}\tag{1}
\]
This difference has **infinitely many positive and infinitely many negative values**, a genuinely oscillatory dependence on circumference rather than a fixed parity rule. Both orbit counts have the same leading exponential growth,
\[
N_P(n)\sim N_M(n)\sim\frac23\rho^n,
\quad\rho=4.884782987\ldots,
\]
where \(\rho\) is the largest real root of \(C\). Meanwhile the difference has size \(O(R^n)\), where \(R=3.351537018\ldots\) is the largest root modulus of \(A\); thus the relative seam response is \(O((R/\rho)^n)\).

The first orbit-count pairs are

| Number of rungs | Prism | Möbius ladder |
|---:|---:|---:|
| 3 | 164 | 24 |
| 4 | 528 | 128 |
| 5 | 1,020 | 3,100 |
| 6 | 8,064 | 9,220 |
| 7 | 57,540 | 32,284 |
| 8 | 202,864 | 229,344 |

## Assumptions and scope
Each graph has vertices \((j,r)\), with \(j\in\{0,\ldots,n-1\}\) and \(r\in\{0,1\}\). The prism has the rung edges \((j,0)(j,1)\) and rail edges \((j,r)(j+1\bmod n,r)\). The Möbius variant has the same non-closing edges and the closing edges \((n-1,0)(0,1)\) and \((n-1,1)(0,0)\). For \(n\ge3\) these are connected simple cubic graphs.

A state is a vector of nonnegative integers \(x=(x_v)\). In one update, every vertex with at least three chips fires one chip to each neighbor simultaneously; the update is
\[
F_G(x)_v=x_v-3\mathbf1_{\{x_v\ge3\}}+\sum_{w\sim v}\mathbf1_{\{x_w\ge3\}}.
\]
A primitive temporal period-three orbit has three distinct states satisfying \(F_G^3(x)=x\), with each orbit counted once. Neither spatial automorphism equivalence nor conservation-total weighting is imposed. No claim is made about other periods, eventual basins, or transient times.

## Proof
**1. Firing-phase reduction.** Let \(G\) be any connected finite simple graph, with degrees \(d_v\), and suppose \(x\) has primitive period three. Write \(f_{v,t}\in\{0,1\}\) for whether vertex \(v\) fires at time \(t\in\{0,1,2\}\). Summing the three chip updates gives
\[
0=\sum_{w\sim v}q_w-d_vq_v,\qquad q_v=\sum_{t=0}^2f_{v,t}.
\]
The graph Laplacian has only constant functions in its kernel on a connected graph, so \(q_v=q\) is independent of \(v\). If \(q=0\) or \(q=3\), the update is stationary. The only possibilities for primitive three-cycles are therefore \(q=1\) and \(q=2\).

For \(q=1\), let \(s(v)\in\mathbb Z/3\mathbb Z\) be the unique firing time, and define
\[
a_v(s)=\#\{w\sim v:s(w)=s(v)-1\pmod3\}.
\]
At its own firing time, vertex \(v\) has \(d_v+u_v\) chips for an integer \(u_v\ge0\). At the two subsequent times it has \(u_v+b_{v,s(v)}\) and \(d_v+u_v-a_v(s)\) chips, where \(b_{v,j}\) is its number of neighbors of phase \(j\). Both are below threshold if and only if \(0\le u_v<a_v(s)\). These conditions are necessary and sufficient, make all chip counts nonnegative, and recover the original state after three updates. Hence for a fixed phase map \(s\), there are exactly \(\prod_va_v(s)\) states, with independent local height choices; zero factors correctly rule out inadmissible maps. Distinct choices give distinct states because the three actual firing patterns and firing-time heights recover \(s\) and \(u\).

The complement \(J(x)_v=2d_v-1-x_v\) is a bijection between primitive period-three states with firing frequency one-third and those with firing frequency two-thirds. It is well defined and nonnegative on these periodic states: every vertex has at least one waiting time, during which it holds at most \(d_v-1\) chips, and cannot exceed \(2d_v-1\) before or during its successive firing steps. The update identity \(F_G(Jx)=J(F_Gx)\) follows from \(\sum_{w\sim v}1=d_v\). Thus both activity classes contain the same number of periodic states, and each temporal orbit has three states. The orbit count is
\[
N_G=\frac23\sum_{s:V\to\mathbb Z/3\mathbb Z}\prod_{v\in V}a_v(s).\tag{2}
\]
This general phase-sum identity is background; the new calculation below evaluates the two seam closures and their signed difference.

**2. The explicit width-two transfer.** Encode each rung phase by \(c=(c_0,c_1)\in\mathcal C=(\mathbb Z/3\mathbb Z)^2\), with nine choices. For three consecutive rung phases \(p,q,r\) put
\[
\begin{split}
U(p,q,r)&=[p_0=q_0-1]+[r_0=q_0-1]+[q_1=q_0-1],\\
V(p,q,r)&=[p_1=q_1-1]+[r_1=q_1-1]+[q_0=q_1-1],\\
w(p,q,r)&=U(p,q,r)V(p,q,r),
\end{split}
\]
where equalities are modulo three and brackets are their zero-one indicators. Index an integer matrix \(T\) by \(\mathcal C^2\) (81 ordered adjacent-rung pairs), with
\[
T_{(p,q),(q',r)}=\begin{cases}w(p,q,r),&q'=q,\\0,&q'\ne q.\end{cases}
\]
Let \(S\) simultaneously exchange the top and bottom labels within both rungs of every pair state. This is an involution commuting with \(T\). A closed length-\(n\) walk through \(T\) records every rung and contributes exactly the product of predecessor-neighbor counts in (2); a walk closing after the row exchange records the Möbius seam. Therefore
\[
N_P(n)=\tfrac23\operatorname{tr}(T^n),\qquad
N_M(n)=\tfrac23\operatorname{tr}(T^nS),\qquad(n\ge3).\tag{3}
\]

**3. Exact symmetry-sector characteristic polynomials.** The \(+1\) and \(-1\) eigenspaces of \(S\) over the rationals have dimensions 45 and 36, since the row exchange fixes nine pair states and swaps the other 72 in 36 pairs. A basis of the positive sector uses fixed basis vectors and sums of swapped basis vectors; the negative sector uses their differences. Substituting the 81 explicitly defined entries of \(T\) and taking integer determinants gives
\[
\begin{aligned}
\chi_+(z)&=z^{24}(z-1)^4(z^2+z+1)^2 B(z)^2 C(z),\\
\chi_-(z)&=z^{21}(z-1)^5(z^2+z+1) A(z)^2.
\end{aligned}\tag{4}
\]
The self-contained `verify_transfer.py` constructs the 81 entries, both rational symmetry bases, and both exact characteristic polynomials; it verifies the displayed identities directly rather than relying on an extrapolated numerical recurrence. For positive powers, eigenvalue power sums determine traces even if the operator is not diagonalizable. Letting \(e_n=\omega^n+\omega^{2n}\), for either nontrivial cube root \(\omega\), equation (4) gives
\[
\begin{aligned}
\operatorname{tr}(T^n|_+)&=4+2e_n+2S_B(n)+S_C(n),\\
\operatorname{tr}(T^n|_-)&=5+e_n+2S_A(n).
\end{aligned}
\]
Their sum and difference in (3) prove both exact counts and equation (1).

**4. Exponential seam screening and infinitely many sign reversals.** The real polynomial \(A(z)=(z^2+z)^2+(11z^2+5z+1)\) is strictly positive on the real line. Its roots therefore form two complex-conjugate pairs. Their moduli are \(R\) and \(1/R\), because the constant coefficient is one. They cannot all lie on the unit circle: in that event the real monic polynomial with constant term one would be reciprocal, but its cubic and linear coefficients differ (two versus five). Thus \(R>1\). Write one root of modulus \(R\) as \(Re^{i\theta}\) with \(0<\theta<\pi\). Then
\[
S_A(n)=2R^n\cos(n\theta)+O(R^{-n}).
\]
Whether \(\theta/(2\pi)\) is rational or irrational, \(\cos(n\theta)\) takes values bounded away from zero on both the positive and negative sides along infinitely many integers \(n\). As \(e_n\) is bounded, equation (1) consequently changes sign infinitely often.

For the growth assertion, the largest positive root \(\rho\) of \(C\) lies in the rational interval \((4.88,4.89)\). The other positive roots lie in \((0.15,0.17)\) and \((1.73,1.74)\), verified by opposite endpoint signs; Descartes' rule of signs allows at most three positive roots, and \(C(-x)<0\) for all \(x\ge0\), so these are all real roots. The complex conjugate pair has modulus below one by the product of all five roots. Every root of \(A\) has modulus below \(4.8\), since on and outside that radius the leading fourth power exceeds the sum of absolute values of all other terms. Every root of \(B\) has modulus below three: \(B(z)=(z+1)^4-3z\), while \((|z|-1)^4>3|z|\) for \(|z|\ge3\). Thus the unique largest modulus among the eigenvalues in (4) is \(\rho\), appearing once in each complete count with coefficient \(2/3\). This proves the leading asymptotics and the exponentially decreasing relative difference. The root values are reported as approximations, not as exact certificates.

## Verification
Run `python3 verify_transfer.py` with SymPy to reconstruct and test the 45- and 36-dimensional exact determinant factors, the row-swap commutation, Newton power sums, trace closures and root-sign brackets. Run `python3 verify_direct.py` with the Python standard library to independently reconstruct each graph, enumerate all \(3^{2n}\) firing-phase maps for \(n=3,4,5\) on both seam types, and test all \(6^6=46,656\) chip states on each six-vertex graph by three direct updates. Its bounded box is exhaustive for primitive period-three states because the preceding proof gives \(0\le x_v\le2d_v-1=5\) at every periodic vertex. Both programs have been executed and their exact output is included in `verification_output.txt`. Finite enumeration is corroboration; equations (2)–(4) establish the full infinite result.

## Relationship to prior work
Jiang–Scully–Zhang (2012) develop general periodic firing-pattern restrictions, and Jiang (2010) treats possible periods for complete multipartite graphs. Neither inspected primary result counts primitive three-orbits in both cubic seam closures. A previously available arbitrary-graph period-three **phase-sum** formula (the unweighted specialization of a chip-mass polynomial) is exactly the background identity (2), and is explicitly acknowledged; it does not provide the sector determinants (4), closed root-power orbit counts, or the infinite sign-reversal theorem. Another published result counts primitive two-orbits on exactly the same prism and Möbius graph families and finds a strict alternating parity law; the present claim is about period **three**, whose twist difference is instead governed by a complex-root quartic and reverses infinitely often without the period-two parity rule. A three-color Greenberg–Hastings seam theorem concerns different deterministic dynamics with a zero-one predecessor-existence predicate, rather than the multiplicative predecessor-degree weights of chip firing. Its characteristic factors and populations do not imply those here.

## Limitations
The results concern only configurations already in primitive temporal three-cycles. Other recurrent periods, transients, attraction basins, spatial orbit quotients and total-chip refinements are not classified. The exact characteristic polynomials are finite integer calculations and are independently reproducible from the transfer definition, but the work has not received independent external mathematical audit. Published and indexed-literature inspection cannot rule out every unindexed equivalent enumeration or stronger theorem.

## References
- T.-Y. Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, arXiv:1003.0943 (public 2010-03-04), https://arxiv.org/abs/1003.0943.
- T.-Y. Jiang, Z. Scully, and Y. X. Zhang, *Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game*, arXiv:1211.6786 (public 2012-11-29), https://arxiv.org/abs/1211.6786; SIAM Journal on Discrete Mathematics 29 (2015), 615–630.
- *Two contiguous chip-energy bands and an exact three-cycle census on connected graphs*, publicly available research statement, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-two-contiguous-chip-energy-bands-and-an-exact-three-cycle-census--99e5dddcdc6e.
- *A parity-reversing twist law for period-two chip-firing orbits on cubic ladders*, publicly available research statement, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-parity-reversing-twist-law-for-period-two-chip-firing-orbits-o--3e46c74462fe.
- *Exponential seam screening for three-color excitable waves on cubic ladders*, publicly available research statement, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exponential-seam-screening-for-three-color-excitable-waves-on-cu--b0ea4c831bc4.
