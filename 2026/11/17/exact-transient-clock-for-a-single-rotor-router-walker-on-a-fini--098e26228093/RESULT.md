# Exact transient clock for a single rotor-router walker on a finite cycle

## Finding

Let a single rotor-router walker move on the labelled, undirected cycle \(C_n\), with \(n\ge3\). Each vertex carries a left/right rotor. At each discrete step the walker flips the rotor at its current vertex, then follows the new direction to the neighboring vertex. Write \(\tau\) for the first time the complete walker-plus-rotor state becomes periodic (the **preperiod**, not the vertex-cover time).

Every initial state admits the exact statewise formula in the next section. In particular,
\[
\max\tau=\frac{(n-1)(n-2)}2,
\qquad \#\{\text{initial states attaining this maximum}\}=2n.
\]
If the initial walker position and all \(n\) rotor bits are independent and uniform, then
\[
\mathbb E\tau=\frac{n^2-5n+8}{4}-2^{1-n},
\qquad
\Pr\left\{\tau=\frac{(n-1)(n-2)}2\right\}=2^{1-n}.
\]
The finite-state dynamical system has \(2n^2\) recurrent states, forming \(n\) orbits of length \(2n\). The recurrence count is consistent with the established unicycle theorem; the contribution here is the exact preperiod, its sharp extremizers, and its mean.

## Assumptions and scope

Number vertices cyclically by \(0,1,\ldots,n-1\) and regard \(n\ge3\) as a simple cycle (so the left and right neighbors are distinct). Encode a clockwise rotor by \(1\) and an anticlockwise rotor by \(0\). Let \(p\) be the initial walker vertex and \(k\) the total number of clockwise rotors. Define the conserved cyclic offset
\[
c\equiv p-k\pmod n
\]
and read the initial rotor word from vertex \(c\): \(b_j=1\) if and only if the rotor at \(c+j\pmod n\) is clockwise, for \(0\le j<n\). Let
\[
S=\sum_{j=0}^{n-1}j b_j,\qquad k=\sum_{j=0}^{n-1}b_j.
\]
Define \(r=\max(\{0\}\cup\{j:1\le j<n,\ b_j=1\})\) and \(\ell=\min(\{n\}\cup\{j:1\le j<n,\ b_j=0\})\). Then, without exceptions at the all-zero and all-one rotor words,
\[
\boxed{\displaystyle
\tau(p,b)=\begin{cases}
2S-k^2-r,&b_0=0,\\
2S-k^2+\ell,&b_0=1.
\end{cases}}
\]
The sentinel definitions \(r=0\) and \(\ell=n\) make both constant-word preperiods zero. This counts individual, indexed full states, not states modulo translation or rotational equivalence. The result is for **rotate-before-move** dynamics, not a rotor update after movement, and not a multiwalker system.

## Proof

**1. Conservation and reduction to a binary map.** A flip of a left rotor changes its bit from \(0\) to \(1\), raises \(k\) by one, and moves \(p\) clockwise by one. A flip of a right rotor changes its bit from \(1\) to \(0\), lowers \(k\) by one, and moves \(p\) anticlockwise by one. Hence \(c=p-k\pmod n\) is invariant. In \(c\)-relative coordinates the walker is at index \(k\pmod n\) and the entire step consists of flipping \(b_{k\bmod n}\). Thus each of the \(n\) offset classes is isomorphic to the same binary-word map.

**2. Explicit recurrent cycle.** For \(0\le j\le n\), let \(A_j\) be the word consisting of \(j\) ones followed by \(n-j\) zeros. For \(0\le j<n\), let \(B_j\) be a zero, then \(j\) ones, then \(n-1-j\) zeros. Apart from \(A_0=B_0\), these are distinct. Their transitions are
\[
A_0\to A_1\to\cdots\to A_n\to B_{n-1}\to B_{n-2}\to\cdots\to B_1\to B_0=A_0.
\]
They therefore form a single length-\(2n\) recurrent orbit in each offset class.

**3. Every other state reaches that cycle and its entry time is explicit.** First suppose \(b_0=0\) and the word is not all zero. Let \(r\ge1\) be its rightmost one. Before entering the displayed orbit, the bit at \(r\) cannot be flipped: as long as it remains one, all ones lie among positions \(1,\ldots,r\), so if the weight reaches \(r\), the word must be exactly \(B_r\), already recurrent. Consequently, while not recurrent, the weight lies between \(1\) and \(r-1\), the active bit lies strictly before \(r\), and \(b_0\) remains zero. Define the nonnegative displacement
\[
E_B=S-\frac{k(k+1)}2\ge0.
\]
An upward weight step \(k\to k+1\) decreases \(E_B\) by exactly one, while a downward step leaves it unchanged. In any stretch without an upward step, the weight strictly decreases; it cannot reach zero with the preserved one at \(r\). Therefore upward steps recur until \(E_B=0\), which means the ones occupy precisely \(1,\ldots,k\). Preservation of the rightmost one forces \(k=r\), so the first recurrent state is \(B_r\). There have been exactly \(E_B\) upward steps and \(E_B+k-r\) downward steps, giving
\[
\tau=2E_B+k-r=2S-k^2-r.
\]

Now suppose \(b_0=1\) and the word is not all one. Let \(\ell\ge1\) be its leftmost zero. Until entering the recurrent set, that zero cannot flip: all earlier bits are ones, so a weight of \(\ell\) implies the word is \(A_\ell\). Thus the active bit has index greater than \(\ell\) and the weight remains below \(n\). Define
\[
E_A=S-\frac{k(k-1)}2\ge0.
\]
Each downward weight step decreases \(E_A\) by exactly one, while each upward step leaves it unchanged. An endless stretch of upward steps would force weight \(n\), contradicting the preserved zero at \(\ell\). Hence \(E_A\) reaches zero and the first recurrent word is \(A_\ell\). There have been \(E_A\) downward steps and \(E_A+\ell-k\) upward steps, proving
\[
\tau=2E_A+\ell-k=2S-k^2+\ell.
\]
The constant words lie on the explicit recurrent orbit already. Hence these are the complete recurrent states and the preperiod formula holds for every initial state.

**4. Sharp maximum and complete extremizers.** In the \(b_0=0\) branch fix the weight \(k\ge1\) and rightmost one \(r\). The index sum \(S\) is largest, uniquely, when the ones occupy \(r-k+1,\ldots,r\). Thus
\[
\tau\le(2k-1)(r-k)\le(2k-1)(n-1-k).
\]
The integer expression on the right is uniquely maximized over \(1\le k<n\) at \(k=\lfloor n/2\rfloor\), with value \((n-1)(n-2)/2\). Its unique maximizing word in this branch is \(0^{n-k}1^k\).

In the \(b_0=1\) branch fix the number \(q=n-k\ge1\) of zeros and their leftmost index \(\ell\). Minimizing their index sum places them consecutively at \(\ell,\ldots,\ell+q-1\). Substitution in the exact clock gives
\[
\tau\le(2q-1)(k-\ell)\le(2q-1)(n-q-1).
\]
Equality at the global maximum requires \(q=\lfloor n/2\rfloor\), \(\ell=1\), with the unique word \(1\,0^q1^{n-q-1}\). Thus each offset class contains exactly two maximizers. Since the \(n\) offset classes partition the \(n2^n\) labelled full states, there are exactly \(2n\) maximizers and their proportion is \(2^{1-n}\).

**5. Exact uniform mean.** In each offset class a uniform full state induces a uniform binary word. Reflection followed by complementation, \(b_j\mapsto1-b_{(-j)\bmod n}\), conjugates the binary map and interchanges the two \(b_0\) branches, so their mean preperiods coincide. Condition on \(b_0=0\); the remaining \(M=n-1\) bits are independent fair bits. Writing \(r=0\) for the empty set, the statewise formula yields \(\tau=2S-k^2-r\), with
\[
\mathbb E S=\frac{M(M+1)}4,\quad
\mathbb E k^2=\frac{M(M+1)}4,\quad
\mathbb E r=M-1+2^{-M}.
\]
The last identity follows from \(\mathbb E r=\sum_{j=1}^M\Pr(r\ge j)\). Hence
\[
\mathbb E\tau=\frac{M(M+1)}4-M+1-2^{-M}
=\frac{n^2-5n+8}{4}-2^{1-n}.
\]

## Verification

Two independent finite tests accompany this proof. `check_functional_graph.py` constructs the full state-transition functional graph, strips all noncyclic states by indegree peeling, computes their exact distance to a cycle and compares it with the closed formula for every state at \(3\le n\le14\). `check_direct.cpp` implements the original rotor update separately, checks the unicycle criterion before every predicted entry and at the predicted entry, and exhausts \(3\le n\le13\). Their recorded outputs are in `functional_graph_output.txt` and `direct_output.txt`. These finite computations are consistency checks; the all-\(n\) conclusion follows from the preceding proof, not extrapolation.

## Relationship to prior work

Priezzhev's original self-directing-walk paper and Priezzhev–Dhar–Dhar–Krishnamurthy establish the rotor mechanism and recurrent/Eulerian behavior. Holroyd–Levine–Mészáros–Peres–Propp–Wilson give the general unicycle criterion on strongly connected digraphs, and Pham gives general orbit-size information. Klasing–Kosowski–Pająk–Sauerwald examine cover time and asymptotic rotor exploration on rings. Those results explain eventual recurrence but do not, by their stated conclusions, give the initial-state-dependent preperiod, its exact worst-case population or its uniform mean. Cover time, Euler-tour period and first entry to a recurrent full state are distinct quantities.

## Limitations

The proof concerns one walker on an undirected simple ring with exactly two alternating rotor directions and a uniform distribution only for the stated mean. It makes no multiwalker claim, does not give vertex-cover-time statistics, and does not establish priority against inaccessible or unindexed archival sources. The 2003 original graph-patrolling paper was available as bibliographic metadata and an abstract but not inspected in full; the earlier 2002 technical-report version was also not accessible in full. Independent mathematical evaluation has not been performed.

## References

1. V. B. Priezzhev, *Self-organized criticality in self-directing walks*, arXiv:cond-mat/9605094 (first submitted 1996-05-15), https://arxiv.org/abs/cond-mat/9605094.
2. V. B. Priezzhev, D. Dhar, A. Dhar, S. Krishnamurthy, *Eulerian Walkers as a Model of Self-Organized Criticality*, arXiv:cond-mat/9611019 (first submitted 1996-11-04), https://arxiv.org/abs/cond-mat/9611019.
3. V. Yanovski, I. A. Wagner, A. M. Bruckstein, *A Distributed Ant Algorithm for Efficiently Patrolling a Network*, Algorithmica 37 (2003), 165–186, https://doi.org/10.1007/s00453-003-1030-9.
4. A. E. Holroyd et al., *Chip-Firing and Rotor-Routing on Directed Graphs*, arXiv:0801.3306 (first submitted 2008-01-22), https://arxiv.org/abs/0801.3306.
5. T. V. Pham, *Orbits of rotor-router operation and stationary distribution of random walks on directed graphs*, arXiv:1403.5875 (first submitted 2014-03-24), https://arxiv.org/abs/1403.5875.
6. R. Klasing, A. Kosowski, D. Pająk, T. Sauerwald, *The multi-agent rotor-router on the ring: a deterministic alternative to parallel random walks*, Distributed Computing (first published online 2016-09-17), https://doi.org/10.1007/s00446-016-0282-y.
