# Binary parity dynamics on wheel graphs: a sharp two-adic transient law

## Finding

Let \(n\ge3\) and let the labelled simple wheel \(W_n=K_1\vee C_n\) have a hub and \(n\) rim vertices. At every synchronous step, each bit is replaced by the sum modulo two of all adjacent bits, with no self-input. Let \(F_n\) be this linear map, and let \(T(x)\) be the least \(t\ge0\) such that \(F_n^t(x)\) belongs to a temporal cycle.

**Odd–even dichotomy.** If \(n\) is odd, \(F_n\) is invertible: all \(2^{n+1}\) states have \(T=0\). If \(n\) is even, write \(v=2^{\nu_2(n)}\), the largest power of two dividing \(n\). There are exactly \(2^{n-v}\) recurrent states, and the exact rank sequence \(r_t=\operatorname{rank}_{\mathbb F_2}F_n^t\) is

\[
r_0=n+1,\qquad
\begin{array}{c|ccc}
& r_1&r_2&r_t\ (t\ge3)\\ \hline
v=2&n&n-1&n-2\\
v=4&n-2&n-3&n-4\\
v\ge8&n-2&n-4&n-\min(2t,v)
\end{array}.
\]

For even \(n\), the number of states with \(T\le t\) is **exactly**
\[
Q_t=2^{n-v+n+1-r_t}\qquad(t\ge0).
\]
In particular, the number entering a cycle for the first time at positive time \(t\) is \(Q_t-Q_{t-1}\). The largest possible first-entry time is
\[
D=\max\left(3,\frac v2\right).
\]
The fraction first entering at this final time is exactly \(1/2\) when \(v\in\{2,4\}\) and \(3/4\) when \(v\ge8\). In the special case that \(n\) is a power of two, the zero state is the **only** recurrent state, and the map is nilpotent with exact class \(D\). Conversely, for even \(n\) with a nontrivial odd factor, nonzero recurrent states exist.

## Assumptions and scope

A wheel means a hub adjacent to every vertex of an undirected simple cycle, with each rim vertex adjacent also to its two distinct cyclic neighbors. The condition \(n\ge3\) avoids the two-site rim multigraph ambiguity. All arithmetic is in \(\mathbb F_2\). A temporal cycle includes a fixed point. First-entry time is the first iterate **on** a cycle, rather than the first time a trajectory repeats a previous value. Every bit assignment is labelled by its fixed sites.

## Proof

Write a state as \((h,x)\), where \(h\in\mathbb F_2\) is the hub bit and \(x\) is a rim word. Identify the rim module with
\[
R=\mathbb F_2[z]/(z^n-1).
\]
Let \(H=1+z+\cdots+z^{n-1}\), let \(s(x)=x(1)\), and let \(L=z+z^{-1}=z^{-1}(z+1)^2\) in \(R\). The dynamics is precisely
\[
F_n(h,x)=\big(s(x),\,hH+Lx\big).
\]
These identities also fix all normalization and orientation choices.

**Odd rim.** Factor \(z^n-1=(z+1)P(z)\). Because \(n\) is odd, \(P(1)=1\), so the Chinese remainder decomposition splits \(R\) into a one-dimensional component at \(z=1\) and a complementary component on which \(L\) is invertible. The hub and the one-dimensional rim component exchange coordinates (since \(H(1)=1\)), while the complementary rim component evolves invertibly via \(L\). Thus \(F_n\) is invertible.

**Even rim.** Write \(n=vm\), with \(m\) odd and \(v=2^a\ge2\). Then \(z^n-1=(z^m-1)^v=(z+1)^vP(z)^v\), with \(P(1)=1\). Split the rim module into \(R_0=\mathbb F_2[u]/(u^v)\), where \(u=z+1\), and an invertible complement of dimension \(n-v\). In \(R_0\), multiplication by \(L\) is multiplication by a unit times \(u^2\), so \(\operatorname{rank}(L^t\vert_{R_0})=v-\min(2t,v)\). The hub input \(H\) lies in the top layer \(u^{v-1}R_0\) (up to a unit), and the sum functional \(s(x)\) reads the constant coefficient at \(u=0\).

Because \(s(H)=n\bmod2=0\), \(LH=0\), and \(s(Lx)=0\), direct substitution gives
\[
F_n^2(h,x)=\big(0,\,s(x)H+L^2x\big),\qquad
F_n^t(h,x)=\big(0,L^tx\big)\ (t\ge3).
\]
Consequently the rank for \(t\ge3\) is \(n-\min(2t,v)\). At \(t=2\), the extra vector \(H\) is outside \(\operatorname{im}L^2\) when \(v=2,4\), but belongs to it for \(v\ge8\). Thus \(r_2=n-\min(4,v)+\mathbf1_{v\le4}\). At \(t=1\), the exceptional case \(v=2\) has a two-dimensional image in the three-dimensional hub-plus-local module, whereas for \(v\ge4\), the extra hub-output is already recovered from the \(u^2\) coefficient of \(Lx\), and \(H\in\operatorname{im}L\); the local image has dimension \(v-2\). Adding the invertible complement yields the stated \(r_1\).

The stable image \(P=\bigcap_{t\ge0}\operatorname{im}F_n^t\) has dimension \(n-v\) for even \(n\), and \(F_n\) restricts to an invertible map of \(P\). In any finite linear map \(F\), the states periodic by step \(t\) form \(F^{-t}(P)\). Since \(P\subseteq\operatorname{im}F^t\), the dimension of this preimage is \(\dim P+\operatorname{nullity}F^t\). This gives \(Q_t=2^{n-v+n+1-r_t}\). The ranks stabilize first at \(D=3\) for \(v=2,4\), and at \(D=v/2\) for \(v\ge8\), with a strict rank drop at the preceding step. The final-time fractions follow by evaluating \(1-Q_{D-1}/2^{n+1}\).

## Verification

Two standalone, standard-library-only Python programs are included. `verify_wheel.py` independently constructs wheel adjacency matrices and performs exact binary Gaussian elimination for \(3\le n\le32\), comparing all computed rank powers with the theorem. It separately checks first-entry histograms by exhaustive finite-state iteration for selected small graphs. `verify_direct_wheel.py` computes the local XOR rule directly from neighbor lists and enumerates all \(2^{n+1}\) initial states for every \(3\le n\le11\), comparing actual first-entry times with the closed formulas. Both programs terminate successfully with their captured outputs. Such finite checks do not replace the all-size algebraic proof.

For example, the exact histograms \((\#\{T=t\})_t\) are \((1,7,8,16)\) at \(n=4\), \((16,16,32,64)\) at \(n=6\), and \((1,7,24,96,384)\) at \(n=8\).

## Relationship to prior work

Additive cellular automata have long been studied through polynomial and algebraic descriptions, including Ward (2000), which focuses on shift-commuting dynamics over infinite sequences and periodic-point statistics. The present wheel map introduces one global hub coordinate, so it is not a translation-invariant one-dimensional rule. Gadouleau and Richard (2015) study which interaction digraphs **admit some** nilpotent Boolean network; their wheel in Theorem 4 has directed outward spokes, and their existence bound does not classify the **fixed**, undirected, XOR adjacency update here. These are methodological and thematic predecessors, not a proof of this exact rank and transient census. Recent work on affine automata and graph-parity Lyapunov spectra treats real-valued spectral growth, rather than the finite-field nilpotent primary part computed here. Complete-multipartite parity networks and distance-two Boolean-cube networks have different adjacency modules; their classifications do not imply the wheel calculation.

## Limitations

The result counts first periodic-entry times but does not classify least lengths of the nontrivial temporal cycles on the stable image. This is a self-review only, not independent validation. Historical priority remains qualified: an equivalent wheel-specific finite-field computation may be present in less-indexed graph-dynamics literature, and one recent preprint was accessible only through its abstract during comparison.

## References

1. M. Gadouleau and A. Richard, *Simple dynamics on graphs*, arXiv:1503.04688 (first public version 2015-03-16), section on wheels and Boolean nilpotence. https://arxiv.org/abs/1503.04688
2. T. B. Ward, *Additive Cellular Automata and Volume Growth*, *Entropy* 2 (2000), 142–167, DOI 10.3390/e2030142. https://doi.org/10.3390/e2030142
3. M. Rollier and J. M. Baetens, *Exact Lyapunov spectra of affine cellular automata and the parity rule on networks*, arXiv:2606.14521 (2026), abstract consulted; full text not assessed. https://arxiv.org/abs/2606.14521
