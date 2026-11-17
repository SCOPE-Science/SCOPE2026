# Hard-core classification of three-cycles in reversible second-order Rule 54

## Finding
For every integer \(n\ge3\), the binary second-order reversible extension of elementary Rule 54 on the labelled cycle of circumference \(n\) has an exactly classified temporal period-three sector. Except for the uniformly zero history, its three successive spatial rows form columns drawn from \(\{001,010,100,111\}\), where a non-\(111\) column cannot have another non-\(111\) column at cyclic spatial separation two. Conversely every such cyclic column word describes exactly one state fixed by the third iterate.

Write \(\mathcal H_n(w)=\sum_{z\in\operatorname{Fix}(R_n^3)}w^{d(z)}\), where \(d(z)\) is the number of columns other than \(000\) and \(111\) in the corresponding three-row temporal history. Put \(s_0(w)=2\), \(s_1(w)=1\), and \(s_m(w)=s_{m-1}(w)+3w\,s_{m-2}(w)\) for \(m\ge2\). Then the full weighted fixed-point polynomial is

\[
\mathcal H_n(w)=\begin{cases}
1+s_n(w),&n\text{ odd},\\
1+s_{n/2}(w)^2,&n\text{ even}.
\end{cases}
\]

Thus \(R_n\) has exactly two fixed states, its number of primitive temporal three-orbits is \((\mathcal H_n(1)-2)/3\), and its temporally three-periodic spatial entropy per site is \(\log((1+\sqrt{13})/2)\). This entropy refers exclusively to the configurations fixed by the third iterate, not to the full reversible state space.

## Assumptions and scope
Let \(\mathbb F_2=\{0,1\}\) with addition \(\oplus\), and let positions be \(i\in\mathbb Z/n\mathbb Z\), with \(n\ge3\). Define the synchronous elementary Rule 54 map by

\[
F_n(v)_i=v_i\oplus(v_{i-1}\lor v_{i+1}),
\]

where \(\lor\) is Boolean OR. It is the Wolfram rule with ordered neighborhood outputs \(00110110\) for inputs \(111,110,101,100,011,010,001,000\). The reversible two-row map is

\[
R_n(u,v)=(v,u\oplus F_n(v))
\qquad\text{on }(\mathbb F_2^n)^2.
\]

Its inverse is \(R_n^{-1}(a,b)=(b\oplus F_n(a),a)\); no asynchronous or staggered sublattice update is being used. For a third-iterate fixed state \((u,v)\), write \(x_0=u\), \(x_1=v\), \(x_2=u\oplus F_n(v)\) and \(x_{t+3}=x_t\). Its column at site \(i\) is \(c_i=(x_{0,i},x_{1,i},x_{2,i})\). A *defect* means a column equal to \(001\), \(010\), or \(100\); \(d\) is the number of such columns. Note that the cyclic sites are labelled: we do not quotient by spatial rotations.

## Proof
**1. A three-time parity identity.** The second-order update says

\[
x_{t+1,i}=x_{t-1,i}\oplus x_{t,i}\oplus(x_{t,i-1}\lor x_{t,i+1}).
\]

For a three-periodic temporal history, rearrangement gives, for each \(t\in\mathbb Z/3\mathbb Z\),

\[
p_i:=x_{0,i}\oplus x_{1,i}\oplus x_{2,i}
=x_{t,i-1}\lor x_{t,i+1}. \tag{1}
\]

If \(p_i=0\), then all three OR expressions on the right vanish. Both complete neighboring temporal columns are \(000\). This implies \(p_{i-1}=p_{i+1}=0\). Connectivity of the spatial cycle forces all columns to be \(000\). This gives the isolated uniform-zero history.

Otherwise \(p_i=1\) at every site, so every temporal column has odd Hamming weight: it is one of \(001\), \(010\), \(100\), or \(111\). Equation (1) holds for all three \(t\) precisely when each site has at least one neighboring \(111\) column: the OR of a \(111\) column with any other equals one in each time row, while two distinct or equal one-hot temporal columns cannot cover all three row positions. Hence two defects cannot stand at spatial distance two; equivalently, if \(c_i\) is a defect then \(c_{i-2}=c_{i+2}=111\). This condition is both necessary and sufficient, and reconstructing \((u,v)=(x_0,x_1)\) from the three-row history is injective. Indeed (1) implies the three second-order recurrence equations, so every admissible history defines a state in \(\operatorname{Fix}(R_n^3)\).

**2. Hard-core counting.** Choose the defect sites first, with no pair adjacent in the *step-two graph* that joins \(i\) to \(i+2\pmod n\). Each chosen site has exactly three independently selectable one-hot column colors. Unchosen sites have column \(111\). The zero history contributes a single additional configuration. If \(n\) is odd, the step-two graph is a single cycle of length \(n\); if \(n\) is even, it splits into two disjoint cycles of length \(n/2\). All these cycles have length at least two when \(n\ge3\).

For a cyclic hard-core graph of length \(m\ge2\), give every selected vertex weight \(3w\). Its independence polynomial equals

\[
\operatorname{tr}\begin{pmatrix}1&3w\\1&0\end{pmatrix}^{m}
=s_m(w).
\]

The trace sequence satisfies the displayed recurrence and initial values. Multiplication across two disjoint cycles and addition of the all-zero history establish the theorem. In particular the coefficient of \(w^0\) is two: the only fixed states are the all-zero and all-one pairs. Because period divides three for every state in the counted set, every other such state has least temporal period three, and division by three counts temporal orbits.

**3. Growth rate.** At \(w=1\), the eigenvalues of the two-state matrix are \(\lambda_\pm=(1\pm\sqrt{13})/2\), with \(\lvert\lambda_-\rvert<\lambda_+\). For odd \(n\), \(s_n(1)\sim\lambda_+^n\). For even \(n\), \(s_{n/2}(1)^2\sim\lambda_+^n\). Therefore the growth rate per site is \(\lambda_+\), giving entropy \(\log\lambda_+\). The finite-ring enumeration is exact for every \(n\ge3\), not inferred from that asymptotic.

## Verification
The package includes `verify_direct.py`, which evolves every one of the \(2^{2n}\) initial pairs under the original Rule 54 definition for each \(3\le n\le10\), and checks the entire defect-count polynomial against a separate enumeration of cyclic hard-core selections. The recorded output is `direct.out`.

Independently, `verify_transfer.py` evaluates all \(8^3\) neighboring temporal-column triples against the local rule truth table, builds the 64-vertex directed temporal-history graph, and checks its cyclic strongly connected components and graph traces for \(1\le n\le24\). Its 112 directed edges have a one-vertex zero-history recurrent component and a sixteen-vertex odd-parity recurrent component. The recorded output is `transfer.out`. Both scripts require only Python 3 standard-library modules and were executed successfully from their package contents.

For example the numbers of pairs fixed by the third iterate are \(11,50,62,101,338,962,1811,3722\) for circumferences \(3,4,5,6,7,8,9,10\), respectively; subtracting two and dividing by three gives \(3,16,20,33,112,320,603,1240\) primitive three-orbits. Finite checks corroborate, but do not replace, the all-size proof above.

## Relationship to prior work
Wolfram [1] explicitly defines the elementary Rule 54 Boolean update and separately introduces the reversible second-order prescription \(x_{t+1}=F(x_t)\oplus x_{t-1}\). Toffoli and Margolus [2] present the general arbitrary-rule reversible second-order construction; Vlasov [3] studies its generalizations. Those developments establish the setting but, in the inspected material, do not state the three-time parity classification or this weighted independent-set formula.

An important naming ambiguity is Buča, Klobas and Prosen's *reversible Rule 54* (RCA54) [5]. It is a staggered sublattice dynamics with the local relation \(s_{x}^{t+1}=\chi(s_{x-1}^{t},s_x^{t-1},s_{x+1}^{t})\) only on alternating space-time sites. Our map instead updates both stored rows on every site each step and explicitly uses the *present center* as well as the previous center. The finite-state maps, configurations being counted, and update conventions are thus different; the RCA54 transport/time-state results in the inspected sections do not directly imply this theorem. The comprehensive glider/tiling study of Martínez, Adamatzky and McIntosh [4] likewise studies the ordinary synchronous one-row Rule 54, not the reversible two-register map. Existing published one-step image results for ordinary synchronous Rule 54 similarly count different objects. This is a mathematical statement comparison, not an assertion that similar titles cannot hide equivalent facts.

## Limitations
Only the sector fixed by the third iterate is classified. No claim is made about all higher temporal periods, generic orbit statistics, thermal equilibrium of the full reversible dynamics, or equivalence to staggered RCA54. The historical originality assessment is conditional on the accessible literature and indexed research records; an unindexed older result could still overlap. There has been no independent mathematical audit.

## References
1. S. Wolfram, “Statistical mechanics of cellular automata,” *Reviews of Modern Physics* **55** (1983), 601–644, published 1983-07-01, DOI https://doi.org/10.1103/RevModPhys.55.601 ; full author's text https://content.wolfram.com/sw-publications/2020/08/statistical-mechanics-cellular-automata.pdf ; especially the Rule 54 Boolean rule and second-order construction.
2. T. Toffoli and N. Margolus, “Invertible cellular automata: A review,” *Physica D* **45** (1990), 229–253, full text https://people.csail.mit.edu/nhm/ica.pdf ; especially section 5.4.
3. A. Yu. Vlasov, “On generalization of reversible second-order cellular automata,” arXiv:1311.4297, first posted 2013-11-18, https://arxiv.org/abs/1311.4297 .
4. G. J. Martínez, A. Adamatzky, H. V. McIntosh, “Complete Characterization of Structure of Rule 54,” *Complex Systems* **23** (2014), 259–293, arXiv:1410.3096, https://arxiv.org/abs/1410.3096 ; the glider classification concerns synchronous one-row Rule 54.
5. B. Buča, K. Klobas, T. Prosen, “Rule 54: Exactly solvable model of nonequilibrium statistical mechanics,” arXiv:2103.16543, first posted 2021-03-30, https://arxiv.org/abs/2103.16543 ; especially section 2 and section 7.
