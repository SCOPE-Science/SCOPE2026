# A quadratic first-recurrence witness for rotor routing on sunlet graphs

## Finding

For every integer \(n\ge3\), on the sunlet \(S_n=C_n\odot K_1\) there is an explicit one-chip rotor-router initial condition whose **first entry into a recurrent state** occurs after exactly
\[
\tau_n=n^2-\left\lceil n/2\right\rceil
\]
individual rotor moves. Consequently the worst possible preperiod on \(S_n\) is \(\Omega(n^2)\); combined with the general \(O(|E|\operatorname{diam}S_n)\) rotor-router lock-in bound, it is \(\Theta(n^2)\). No assertion that \(\tau_n\) is the exact global maximum is made for all \(n\).

## Assumptions and scope

The undirected simple sunlet has rim vertices indexed \(i=0,\ldots,n-1\) cyclically and one distinct leaf \(i'\) adjacent to every rim vertex \(i\). A single chip starts at rim vertex \(0\). Each rim rotor has three positions in **cyclic order** \((i+1,i',i-1)\), with indices modulo \(n\), and each leaf rotor has its unique position pointing inward. At each discrete step, increment the chip vertex's rotor by one position in its local cyclic order, then move the chip along that newly selected outgoing arc. The state consists of the chip position and all rotor positions; the first recurrent-entry time is the first \(t\ge0\) for which the entire state at time \(t\) is on a periodic orbit.

Define \(c=\lceil n/2\rceil\) and initial rim rotor indices \(r_i\in\{0,1,2\}\) by \(r_c=1\), \(r_i=0\) for \(0\le i<c\), and \(r_i=2\) for \(c<i<n\). When \(n\) is odd replace \(r_0=0\) by \(r_0=2\). All leaf rotors point inward. These instructions completely define the claimed initial state and apply at \(n=3\) without any degeneracy.

## Proof

We prove the exact first hitting time of \(c\), then identify that hitting time with first recurrence. We use a rotor-stack firing certificate and prove its least-action property explicitly, rather than inferring an all-size result from finite simulation.

Put \(u_c=u_{c'}=0\). For each other rim vertex \(i\), define a proposed number \(u_i\) of firings of \(i\), and \(u_{i'}\) of the leaf \(i'\), as follows:

* For \(1\le i<c\), let \(d=c-i\) and put \((u_i,u_{i'})=(3d-1,d)\).
* For \(c<i<n\), let \(d=i-c\) and put \((u_i,u_{i'})=(3d,d)\).
* If \(n=2m\) is even, let \((u_0,u_{0'})=(3m-1,m)\). If \(n=2m+1\) is odd, let \((u_0,u_{0'})=(3m,m)\).

A firing of \(i\) follows the next arc in its three-arc rotor stack. If its initial rotor is zero and it fires \(3d-1\) times, its outgoing arc counts in order (clockwise, leaf, counterclockwise) are \((d-1,d,d)\). If its initial rotor is two and it fires \(3d\) times, all three outgoing counts equal \(d\). Each leaf fires exactly the number of times it receives a chip. These arc-count formulas and the cyclic boundary edge \((n-1,0)\) show the exact conservation identity, for **every** vertex \(v\),
\[
\mathbf 1_{v=0}+\sum_w N_{w\to v}(u_w)-u_v=\mathbf 1_{v=c},
\]
where \(N_{w\to v}(u_w)\) is the number of uses of \(w\to v\) among the first \(u_w\) firings in the prescribed local rotor stack. In particular the proposed final chip configuration has one chip at \(c\) and no chips elsewhere. Every rim rotor except at \(c\) now points counterclockwise, while \(c\) still points to \(c'\). The terminal rotor arrows therefore have just one directed cycle, the two-cycle \(c\leftrightarrow c'\); every other arrow eventually reaches this cycle.

For completeness, this legal firing schedule is unique. Stop the actual chip walk on its **first** arrival at \(c\) and write \(v_x\) for its number of firings at vertex \(x\). Suppose the actual schedule would make an \((u_x+1)\)-st firing at some vertex \(x\) while all other actual firing counts are at most their prescribed \(u_y\). The prescribed vector already leaves zero chips at \(x\), and the actual walk has fired \(x\) exactly \(u_x\) times with no more incoming firings from any other vertex; hence the actual chip cannot be at \(x\). This contradiction, starting with the first excess firing, proves \(v_x\le u_x\) for all \(x\). Both schedules leave the same single chip at \(c\). If \(S=\{x:v_x<u_x\}\) were nonempty, subtraction of chip-conservation equations across \(S\) implies that **no** excess firing from \(S\) sends a chip outside \(S\), since vertices outside \(S\) have no excess firings. At every \(x\in S\), the last excess firing follows the **final** prescribed rotor arrow of \(x\), so this arrow remains inside \(S\). A finite nonempty rotor-closed set contains a directed cycle, contradicting the already established fact that all prescribed terminal rotor arrows outside \(c\) lead toward \(c\). Thus \(v=u\).

Summing these firing counts gives, for \(n=2m\), the total \(4m^2-m\), and for \(n=2m+1\), the total \(4m^2+3m\). Both equal \(n^2-\lceil n/2\rceil\). Therefore the first visit to \(c\) occurs at exactly that update.

A finite strongly connected Eulerian digraph's one-chip rotor-router state is recurrent precisely if its rotor arrows have exactly one directed cycle and that cycle contains the chip (the rotor-router unicycle criterion). Until the visit to \(c\), the rotor at \(c\) is unchanged and still points to \(c'\), which points back to \(c\); the chip is not on this cycle, so no earlier state is recurrent. At arrival the terminal arrows have the unique cycle \(c\leftrightarrow c'\) containing the chip, hence the state is recurrent. This establishes the claimed **first** recurrence time.

Finally, \(|E(S_n)|=2n\) and \(\operatorname{diam}(S_n)=\lfloor n/2\rfloor+2\). The general rotor-router lock-in bound of order \(|E|\operatorname{diam}\) is \(O(n^2)\); our explicit entry time is \(\Omega(n^2)\). The growth order of the global worst-case time on this family is therefore quadratic. This does not establish the exact global maximum.

## Verification

Run `python verify.py` with Python 3 and no third-party modules. The program (a) independently verifies every candidate stack-count conservation identity, final arrow condition and time for \(3\le n\le500\); (b) directly iterates the microscopic chip walk for \(3\le n\le60\); and (c) exhausts the \(3^n\) choices of all rim rotors for \(3\le n\le8\), with the chip at zero, as a *finite* supplemental extremality check. The proof, not this finite computation, establishes the formula for all sizes.

## Relationship to prior work

Holroyd–Levine–Mészáros–Peres–Propp–Wilson give the rotor-router unicycle criterion and general rotor-routing theory. Lock-in and rotor-router exploration papers establish general convergence and other-graph bounds. None of the inspected full-text discussions yields this specified sunlet-rotor initialization, its exact \(n^2-\lceil n/2\rceil\) first-recurrence time, or the rotor-stack conservation witness. Rotor investigations on bare cycles, bare paths, and tree spiders do not directly cover a cycle with one private pendant at **every** vertex. Published search and existing related summaries have been compared by mathematical implication rather than title alone.

## Limitations

The result is **one explicit all-size lower-bound family**, not an exact all-initial-conditions extremal theorem. Finite checks through eight rim vertices happen to find this value maximal for those sizes, but no corresponding claim is made for larger sizes. The asymptotic \(O(n^2)\) upper bound invokes established general rotor-router theory. Historical priority is conditional on the literature inspected; undiscovered equivalent rotor-stack examples remain possible. No independent mathematical audit has been performed.

## References

1. Holroyd, Levine, Mészáros, Peres, Propp and Wilson, *Chip-Firing and Rotor-Routing on Directed Graphs*, arXiv:0801.3306, first public version 2008-01-22. https://arxiv.org/abs/0801.3306
2. Chalopin et al., *Lock-in Problem for Parallel Rotor-router Walks*, arXiv:1407.3200, first public version 2014-07-10. https://arxiv.org/abs/1407.3200
3. Menc, Pająk and Uznański, *Time and Space Optimality of Rotor-router Graph Exploration*, arXiv:1502.05545, first public version 2015-02-19. https://arxiv.org/abs/1502.05545
