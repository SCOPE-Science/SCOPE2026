# Exact three-rate excitation census on open square ladders

## Finding
For each integer \(n\ge2\), let \(L_n=P_n\square K_2\), with labelled upper vertices \(u_1,\dots,u_n\) and lower vertices \(v_1,\dots,v_n\); horizontal neighbors have successive indices and each \(u_i\) is adjacent to \(v_i\). Start synchronous three-state cyclic cellular automaton (CCA) or three-state threshold-one Greenberg–Hastings (GHM) dynamics from an arbitrary labelled initial coloring with states \(\{0,1,2\}\).

Let \(\alpha_C\) be the eventual mean number of CCA increments per time step at a fixed vertex, and \(\alpha_G\) the eventual mean number of GHM transitions \(0\to1\) per time step at a fixed vertex. Both limits exist, are independent of the chosen vertex, and obey
\[
\alpha_C=3\alpha_G,\qquad \alpha_C\in\{0,3/4,1\}.
\]
All three rates occur for \(n\ge3\); for \(n=2\), rate \(1\) does not occur.

Define integer sequences \(Z_n\) and \(Q_n\) by
\[
Z_1=9,\quad Z_2=57,\quad Z_n=7Z_{n-1}-4Z_{n-2}\quad(n\ge3),
\]
\[
Q_1=9,\quad Q_2=81,\quad Q_3=723,\quad Q_n=9Q_{n-1}-Q_{n-2}+3Q_{n-3}\quad(n\ge4).
\]
Among the \(3^{2n}=9^n\) labelled initial colorings, exactly \(Z_n\) have rate \(0\), exactly \(Q_n-Z_n\) have CCA rate \(3/4\), and exactly \(9^n-Q_n\) have CCA rate \(1\). The respective GHM rates are \(0,1/4,1/3\).

In particular, for uniformly independent initial colors, the maximal activity becomes overwhelmingly likely: \(\Pr(\alpha_C=1)=1-Q_n/9^n\to1\) exponentially. The exponential base for \(Q_n\) is the unique positive root \(\rho=8.92561986\ldots\) of \(\rho^3-9\rho^2+\rho-3=0\), which is strictly less than \(9\). The zero-rate count has base \((7+\sqrt{33})/2=6.37228132\ldots\).

## Assumptions and scope
CCA advances \(x_i\mapsto x_i+1\pmod3\) precisely when some neighbor currently has successor color \(x_i+1\pmod3\), otherwise retaining its color. GHM advances states \(1\mapsto2\mapsto0\) automatically and advances \(0\mapsto1\) precisely upon contact with a neighbor in state \(1\). All vertices update simultaneously. No randomness in updating is assumed; probabilities concern the uniform initial coloring only. The graph is finite, connected, simple, open at both ends, and contains exactly \(n-1\) square faces.

For any ordered edge \((a,b)\), let \(d_C(a,b)\in\{-1,0,1\}\) be the signed representative of \(x_b-x_a\pmod3\). The circulation around the \(i\)-th square, oriented \(u_i,u_{i+1},v_{i+1},v_i,u_i\), is \(3c_i\), where \(c_i\in\{-1,0,1\}\). Reversing the square orientation negates \(c_i\).

## Proof
**1. Cycle-rate reduction.** The finite-graph activity theorem of Gravner, Lyu and Sivakoff [1, Theorem 3] says that the eventual excitation rate equals the largest signed cycle circulation divided by cycle length, or zero if all circulations vanish. It applies separately to CCA and GHM. Let \(d_G\) be the GHM signed edge form: it is \(+1\) on an edge oriented from \(0\) to \(1\), \(-1\) on the reverse orientation, and zero otherwise. For the function \(f(0)=0,\ f(1)=-2,\ f(2)=-1\), a direct six-case check gives \(d_C(a,b)-3d_G(a,b)=f(x_b)-f(x_a)\). Therefore every closed-cycle CCA circulation is exactly three times its GHM circulation. The two activities on the same initial coloring have the claimed ratio, and the synchronizing sets coincide.

**2. Two-square witness criterion.** Every simple cycle of an open ladder is the boundary of \(k\ge1\) consecutive squares, has \(2(k+1)\) edges and signed circulation \(3\sum_{i=j}^{j+k-1}c_i\). Suppose two adjacent face charges both equal \(+1\), or both equal \(-1\). Their two-square rectangle has circulation magnitude \(6\) and length \(6\), so the maximal CCA activity is \(1\), its possible absolute upper bound. Conversely, suppose there is no adjacent pair of equal nonzero signs. For either chosen orientation, among any \(k\) consecutive face charges there are at most \(\lceil k/2\rceil\) positive entries, hence its signed mean does not exceed
\[
\frac{3\lceil k/2\rceil}{2(k+1)}\le\frac34.
\]
If some face charge is nonzero, its square already achieves \(3/4\). If all charges vanish, all cycles have zero circulation and the dynamics synchronize. Thus the three activity events are characterized exactly by: all \(c_i=0\); some \(c_i\ne0\) but no adjacent equal nonzero signs; and at least one adjacent equal nonzero pair.

**3. Exact three-state transfer for face charges.** Represent the difference between the lower and upper color at column \(i\) by \(r_i\in\{-1,0,1\}\). For a transition between consecutive columns, take the upper horizontal increment \(t\in\{-1,0,1\}\), and write \([a]_3\) for its representative in that set. The lower horizontal increment is \(s=[t+r_{i+1}-r_i]_3\). The face charge is
\[
c_i=\frac{t+r_{i+1}-s-r_i}{3}.
\]
Each initial upper color has three choices; each successive \(t\) fixes the new upper color. Ordering the rung differences as \((-1,0,1)\), define the integer matrices \(T_{\sigma}\), where entry \((r,r')\) counts the choices of \(t\) producing face charge \(\sigma\). The full matrices are
\[
T_{-1}=\begin{pmatrix}0&0&0\\1&0&0\\2&1&0\end{pmatrix},\quad
T_0=\begin{pmatrix}3&2&1\\2&3&2\\1&2&3\end{pmatrix},\quad
T_{+1}=\begin{pmatrix}0&1&2\\0&0&1\\0&0&0\end{pmatrix}.
\]
With \(\mathbf1_d\) the all-ones column vector of length \(d\), the zero-rate count is exactly
\[
Z_n=3\mathbf1_3^{\mathsf T}T_0^{n-1}\mathbf1_3.
\]
Exact inversion of this explicit \(3\times3\) matrix yields
\[
\sum_{n\ge1}Z_nz^{n-1}=3\mathbf1_3^{\mathsf T}(I_3-zT_0)^{-1}\mathbf1_3
=\frac{3(3-2z)}{1-7z+4z^2},
\]
which establishes the stated recurrence and initial values.

**4. Excluding adjacent equal nonzero face charges.** Define a \(9\times9\) matrix \(B\), whose rows and columns are indexed by pairs \((r,\sigma)\in\{-1,0,1\}^2\). The row represents the present rung difference and previous face charge, and the column the next rung difference and new face charge. Set
\[
B_{(r,\sigma),(r',\tau)}=
\begin{cases}
(T_\tau)_{r,r'},&\sigma\ne\tau\text{ or }\tau=0,\\
0,&\sigma=\tau\in\{-1,1\}.
\end{cases}
\]
Let \(u\) be the row vector with entry \(1\) at \((r,0)\) for each \(r\) and zero elsewhere. By direct path counting, \(Q_n=3uB^{n-1}\mathbf1_9\). A finite exact matrix inversion gives
\[
\sum_{n\ge1}Q_nz^{n-1}=3u(I_9-zB)^{-1}\mathbf1_9
=\frac{3(3+z^2)}{1-9z+z^2-3z^3}.
\]
The three-term recurrence and its initial values follow. The matrices and both rational-function identities are reproduced in the standalone exact symbolic checker; a separate integer checker also generates both sequences via independently coded transitions. Combining with Step 2 proves all three exact population formulas.

**5. Occurrence and asymptotics.** A single nonzero square exists already for \(n=2\), while two adjacent equally signed nonzero squares first occur when \(n=3\), in six colorings. Extending any such coloring to additional columns preserves the rate-one witness. The displayed generating functions give \(Q_n\sim C\rho^{n}\) for some \(C>0\), with the unique real root \(\rho\in(8,9)\) of the stated cubic (the other roots have modulus below \(1\)); \(Z_n\) has the stated smaller leading root. Hence the exact phase probabilities have the asserted limits. No primitive-period or entry-time distribution is needed or asserted.

## Verification
The three accompanying programs are `verify_transfer.py`, `verify_symbolic.py`, and `verify_dynamics.py`. Run with Python 3.10 or later; the symbolic check additionally requires SymPy 1.12 or later.

`verify_transfer.py` evaluates the integral transfer recurrences through \(n=30\) and independently enumerates all \(597{,}861\) labelled colorings at \(2\le n\le6\). `verify_symbolic.py` constructs all \(T_\sigma\), the \(9\times9\) transfer matrix, and verifies both rational generating-function identities by exact symbolic simplification. `verify_dynamics.py` simulates both original synchronous update rules until recurrence for all \(66{,}420\) labelled initial colorings at \(2\le n\le5\); it checks rate equality at every vertex, phase values, and the exact populations. Captured program output is included separately. The finite checks corroborate, but do not substitute for, the all-size proof.

For \(n=2,3,4,5,6\), the respective triples \((\#0,\#3/4,\#1)\) are \((57,24,0)\), \((363,360,6)\), \((2313,4140,108)\), \((14739,42858,1452)\), and \((93921,420168,17352)\).

## Relationship to prior work
The finite-graph cycle-mean activity characterization is exactly [1, Theorem 3] and is **not** a new theorem here. [2] independently treats arbitrary finite-graph GHM activity via maximum cycle density; its general principle also does not evaluate this labelled open-ladder population. An existing calculation of the number of *initially primitive period-three* GHM states on open ladders answers a different question: the present census classifies **all initial configurations by eventual mean excitation**, including those with transients and with other eventual periods. Neither that restricted calculation nor the general cycle theorems yields the displayed two rational population generating functions without a ladder-specific transfer argument. No claim of an exhaustive global literature search or historical priority is made.

## Limitations
The exact activity classes and the populations of their **initial** colorings are established; neither time to enter the eventual behavior nor numbers of distinct eventual temporal orbits at each period are counted. A max-rate configuration may have a transient and is not necessarily initially period three. The asymptotic statement assumes uniform independent initial colors. Equivalent enumerations in less-indexed work cannot be excluded. Independent external validation has not been performed.

## References
[1] J. Gravner, H. Lyu, D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (first posted 2016-10-24), Theorem 3 and its proof. https://arxiv.org/abs/1610.07320

[2] N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, Complex Systems 27 (2018), 101–126, DOI 10.25088/ComplexSystems.27.2.101, Sections 6–7. https://doi.org/10.25088/ComplexSystems.27.2.101
