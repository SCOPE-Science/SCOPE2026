# A dominant NOR oscillator on every wheel: an exact parity-sensitive Lucas basin

## Finding
Let \(W_n=K_1\vee C_n\) be the labelled wheel with one hub and \(n\ge3\) rim vertices. In synchronous **open-neighborhood** binary NOR dynamics, each vertex becomes one precisely when all its neighbors are zero. The configurations with all vertices zero and all vertices one form a primitive two-cycle \(\mathcal O_n\). Its full attraction basin, including the two recurrent configurations, has cardinality
\[
\boxed{B_n=2^n+T_n,\qquad T_n=\begin{cases}L_n,&n\text{ odd},\\L_{n/2}^2,&n\text{ even},\end{cases}}
\]
where \(L_0=2\), \(L_1=1\) and \(L_{j+2}=L_{j+1}+L_j\) are the Lucas numbers. Equivalently, for even \(n\), \(T_n=L_n+2(-1)^{n/2}\). Every initial state enters a fixed point or a two-cycle after at most one update: \(F^3=F\); this bound is sharp for every \(n\ge3\). Since \(B_n>2^n\) out of \(2^{n+1}\) initial configurations, \(\mathcal O_n\) is the **unique largest attractor basin**. Under independent fair initial bits its probability is
\[
\boxed{\Pr(\mathcal O_n)=\tfrac12+\frac{T_n}{2^{n+1}}\longrightarrow\tfrac12\quad(n\to\infty).}
\]
The exact parity-sensitive correction is exponentially small, with leading base \((1+\sqrt5)/4\). For comparison, on the **bare rim** \(C_n\) with the identical NOR rule, the corresponding empty/full two-cycle has basin exactly \(T_n+1\) and probability \((T_n+1)/2^n\to0\). Thus adjoining one hub changes the probability of that natural oscillatory pattern from vanishing to asymptotically one-half.

## Assumptions and scope
The wheel means one vertex adjoining all vertices of the loopless, undirected cycle on \(n\) distinct rim vertices; thus \(W_3=K_4\). There are \(n+1\) labelled vertices and no self-neighbor inputs. Time is simultaneous and deterministic. A basin contains every initial configuration eventually visiting either point of the named periodic orbit. No basin-size assertion is made for any other individual orbit. The probability statement uses the uniform product measure on the \(2^{n+1}\) configurations.

## Proof
Write a state as \((h,x)\), with hub bit \(h\in\{0,1\}\) and rim word \(x=(x_i)_{i\in\mathbb Z/n\mathbb Z}\). Let \(\mathbf0\) and \(\mathbf1\) denote the constant rim words. Define the ring NOR map by
\[
g(x)_i=(1-x_{i-1})(1-x_{i+1}).
\]
The complete wheel rule is
\[
F(h,x)=\bigl(\mathbf1_{\{x=\mathbf0\}},\,(1-h)g(x)\bigr),
\]
where multiplication of a word by a bit is coordinatewise. Hence \(F(0,\mathbf0)=(1,\mathbf1)\), \(F(1,\mathbf1)=(0,\mathbf0)\), and \(F(1,\mathbf0)=(1,\mathbf0)\).

**The ring NOR identity.** A direct Boolean calculation gives
\[
g^2(x)_i=(x_{i-2}\lor x_i)(x_i\lor x_{i+2})=x_i\lor(x_{i-2}x_{i+2}).
\]
In particular \(g^2(x)\ge x\) coordinatewise. Furthermore, replacing a zero bit \(x_i\) by one under the last formula requires \(x_{i-2}=x_{i+2}=1\); therefore its two neighboring outputs \(g(x)_{i-1}\) and \(g(x)_{i+1}\) were already zero. Thus no output of \(g\) changes when the input is replaced by \(g^2(x)\), and \(g^3=g\). This argument works also at the short cyclic boundaries \(n=3,4\), where indices may coincide.

**Basin characterization.** Every state with hub one and nonzero rim word maps immediately to \((0,\mathbf0)\); there are \(2^n-1\) such states. The state \((0,\mathbf0)\) is itself in \(\mathcal O_n\). For a state \((0,x)\) with \(x\ne\mathbf0\), its next state is \((0,g(x))\). If \(g(x)=\mathbf0\), it joins \(\mathcal O_n\). If \(g(x)\ne\mathbf0\), then \(g^2(x)\ge x\ne\mathbf0\) and \(g^3(x)=g(x)\); so all subsequent rim states are nonzero and the hub stays zero forever. Such a state cannot enter \(\mathcal O_n\). Consequently
\[
\lvert\operatorname{Basin}(\mathcal O_n)\rvert=(2^n-1)+1+\#\{x:g(x)=\mathbf0\}=2^n+T_n.
\]
On the bare cycle, the same \(g^3=g\) identity shows that a state is in the basin of \(\mathbf0\leftrightarrow\mathbf1\) precisely when its first image is \(\mathbf0\) or \(\mathbf1\). There are \(T_n\) inputs of the first type and exactly one of the second type (\(x=\mathbf0\)), giving the comparison basin \(T_n+1\). This also proves every wheel state reaches an eventual periodic orbit within one update: if \(h=1\), one of the displayed fixed/recurrent states is reached; if \(h=0\) and \(x\ne\mathbf0\) with \(g(x)\ne\mathbf0\), the ring identity \(g^3=g\) makes \((0,g(x))\) two-periodic (possibly fixed). Thus \(F^3=F\). The bound one is attained, for example by \((1,\mathbf1)\) with one rim bit toggled to zero: it maps to \((0,\mathbf0)\) but is not itself recurrent.

**Counting the special basin.** The condition \(g(x)=\mathbf0\) says: for every rim vertex at least one of its two rim neighbors has bit one. These are exactly the total dominating subsets of \(C_n\), or equivalently words with no pair of zero bits at cyclic distance two. The distance-two edges form one cyclic component of length \(n\) when \(n\) is odd, and two disjoint cyclic components of length \(n/2\) when \(n\) is even. On a cyclic component of length \(m\ge2\), allowed binary words have no adjacent zeros and are counted by
\[
\operatorname{tr}\left(\begin{pmatrix}0&1\\1&1\end{pmatrix}^m\right)=L_m.
\]
This gives the stated odd/even expressions for \(T_n\); the standard Lucas doubling identity \(L_{2m}=L_m^2-2(-1)^m\) gives the equivalent mod-four correction. Because \(T_n>0\), the basin is strictly more than half the state space and hence larger than any other basin, with no need to classify those other basins. Finally \(L_m=\varphi^m+(-\varphi^{-1})^m\) for \(\varphi=(1+\sqrt5)/2<2\), proving convergence of the probability and the decay rate.

## Verification
Two independent, dependency-free Python 3 checkers are included. `verify_bruteforce.py` constructs adjacency masks and exhaustively verifies all \(2^{n+1}\) states for each \(3\le n\le13\), confirming \(F^3=F\), the designated orbit, the basin, and the Lucas formula. `verify_transfer.py` independently computes transfer-matrix traces through length 60 and directly enumerates valid cyclic words through length 18; it also checks the Lucas doubling identity. Run `python verify_bruteforce.py` and `python verify_transfer.py` from the directory containing those files. Finite tests corroborate the separate all-length proof and do not themselves establish it.

## Relationship to prior work
The published odd-cycle Rule-5 predecessor classification already evaluates the **bare** odd-cycle empty/full basin and its Lucas preimage count; those ingredients are explicitly credited. The new effect concerns the quantitatively different **wheel** basin, including even circumferences and its hub-induced asymptotic half-space dominance. Boolean AND-NOT fixed-point theory relates fixed states to maximal independent sets (Veliz-Cuba and Laubenbacher, 2011), while the more general AND-OR-NOT work of Aracena, Richard and Salinas (2014) develops extremal fixed-point bounds. Their stated fixed-point targets do not imply an exact attraction basin for a specified wheel two-cycle. The general antitone-map identity and elementary Lucas enumeration are classical ingredients, not claimed new. The contribution claimed here is their exact combination into a dominant-basin law, with an explicit parity/mod-four correction and one-update complete relaxation for this natural hub-and-cycle family. Related published analyses of NOR dynamics on different graphs do not present this exact wheel basin in the material inspected.

## Limitations
Originality is based on accessible literature, stated-result comparisons, and searched records; an unindexed earlier wheel-specific formula may exist. One historical fixed-point paper was inspected only via its public abstract and references because full text was not openly accessible. Independent external validation has not been performed. No assertion is made about full attractor counts or all other basins.

## References
- *Fibonacci fibers and the uniquely dominant Lucas basin for odd-ring Rule 5*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-fibonacci-fibers-and-the-uniquely-dominant-lucas-basin-for-odd-r--9b825fd6faf8.
- A. Veliz-Cuba and R. Laubenbacher, *On the computation of fixed points in Boolean networks*, publicly published 2011-10-15, https://doi.org/10.1007/s12190-011-0517-9.
- J. Aracena, A. Richard and L. Salinas, *Maximum number of fixed points in AND–OR–NOT networks*, Journal of Computer and System Sciences 80 (2014), https://doi.org/10.1016/j.jcss.2014.04.025.
- *Wheel graph*, graph definition and nomenclature, https://en.wikipedia.org/wiki/Wheel_graph.
