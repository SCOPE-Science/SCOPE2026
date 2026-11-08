# Clique-parity bifurcation of reversible waves on dyadic cylinders

## Finding

Let \(r\geq3\), \(m\geq3\), \(q=2^f\) with \(f\geq1\), and \(G=C_{2^r}\square K_m\) with labelled vertices. Let \(A\) denote its loopless adjacency matrix over \(\mathbb F_q\), and let the reversible two-row update be
\[
T(u,v)=(Au+v,u),\qquad (u,v)\in\mathbb F_q^{V(G)}\times\mathbb F_q^{V(G)}.
\]
Write \(L=2^{r-1}\), \(h(t)=2^{\nu_2(t)}\), and \(p(X)=X^2+X+1\). The full \(\mathbb F_q[X]\)-module of the time-update is
\[
\begin{cases}
[\mathbb F_q[X]/(X+1)^{2L}]^{\oplus2}\;\oplus\;[\mathbb F_q[X]/p(X)^L]^{\oplus2(m-1)},&m\text{ odd},\\
[\mathbb F_q[X]/p(X)^L]^{\oplus2m},&m\text{ even}.
\end{cases}
\]
Here \(X\) acts as \(T\); the displayed expression remains valid whether or not \(p\) splits over \(\mathbb F_q\).

Consequently the exact number \(F(t)=\#\operatorname{Fix}(T^t)\) of paired-row configurations fixed at any positive time \(t\) is
\[
F(t)=\begin{cases}
q^{\,2\min(h(t),2L)+4(m-1)\mathbf 1_{3\mid t}\min(h(t),L)},&m\text{ odd},\\
q^{\,4m\mathbf1_{3\mid t}\min(h(t),L)},&m\text{ even}.
\end{cases}
\]
The exact permutation order of \(T\) is \(3\cdot2^r\) for odd \(m\), but \(3\cdot2^{r-1}\) for even \(m\). All states are periodic at time zero. The complete set of occurring least periods is
\[
\begin{cases}
\{1\}\cup\{2^j:1\leq j\leq r\}\cup\{3\cdot2^j:0\leq j\leq r\},&m\text{ odd},\\
\{1\}\cup\{3\cdot2^j:0\leq j\leq r-1\},&m\text{ even}.
\end{cases}
\]
Every listed period actually occurs. If \(P(d)\) counts states of least period \(d\), the exact count at every divisor \(d\) of the displayed order is
\[
P(d)=\sum_{e\mid d}\mu(d/e)F(e),
\]
and the number of distinct temporal orbits of that period is \(P(d)/d\). The state and orbit counts do not quotient by graph automorphisms or swap the two labelled temporal rows.

## Assumptions and scope

The cycle has length at least eight; this restriction removes the four-cycle specialization, which is also a Cartesian product of two edges and is covered by a known Hamming-graph wave calculation. The clique has at least three vertices. Graphs are undirected, simple, and labelled, and every neighbor is counted once. The field is any finite field of characteristic two, not just the binary field. Only the linear neighbor-sum reversible update displayed above is treated. An earlier first-order parity-update law, even on the same graph, is a different dynamical system.

## Proof

**Step 1: the dyadic cycle adjacency.** Put \(n=2^r=2L\). On the cyclic coordinate, let \(S\) denote translation by one step. The cycle-adjacency map is \(B=S+S^{-1}\). Identify the cyclic regular module with
\[
R=\mathbb F_q[x,x^{-1}]/(x^n-1)\cong\mathbb F_q[y]/(y^n),\qquad y=x+1.
\]
The second isomorphism uses \(x^n-1=(x+1)^n\) in characteristic two. Multiplication by \(B\) becomes multiplication by \(y^2/(1+y)\), where the denominator is a unit. For each \(j\geq0\),
\[
\dim\ker(B^j)=\min(2j,n).
\]
Therefore \(B\) has precisely two nilpotent Jordan blocks, each of length \(L\):
\[
B\sim J_L(0)^{\oplus2}.
\]
This is a statement about all powers, not merely the characteristic polynomial.

**Step 2: the clique parity split.** Let \(E\) be the \(m\times m\) all-ones matrix. Clique adjacency is \(C=I+E\) in characteristic two. Since \(E^2=mE\), if \(m\) is odd then \(C^2=C\). Its zero eigenspace has dimension one, and its unit eigenspace dimension \(m-1\). The Cartesian graph adjacency \(A=B\otimes I+I\otimes C\) therefore has
\[
A\sim J_L(0)^{\oplus2}\oplus J_L(1)^{\oplus2(m-1)}
\]
for odd \(m\).

If \(m\) is even then \(E^2=0\) and \(\operatorname{rank}E=1\). Thus \(C\) consists of one \(J_2(1)\) and \(m-2\) copies of \(J_1(1)\). It remains to handle the tensor Kronecker sum of \(J_L(0)\) and \(J_2(0)\). It acts as multiplication by \(a+b\) on
\[
\mathbb F_q[a,b]/(a^L,b^2).
\]
With \(c=a+b\), the power-of-two identity gives \(c^L=a^L+b^L=0\), because \(L\geq4\) and \(b^2=0\). The inverse substitution \(a=c+b\) identifies this algebra with \(\mathbb F_q[c,b]/(c^L,b^2)\), a free module of rank two over \(\mathbb F_q[c]/c^L\). Consequently the Kronecker sum has exactly two Jordan blocks of length \(L\). Counting the two original cycle blocks and all clique blocks yields
\[
A\sim J_L(1)^{\oplus2m}
\]
for even \(m\). This explains why changing the parity of the clique removes the adjacency eigenvalue zero without increasing the nilpotent block length.

**Step 3: lifting a Jordan block to a reversible wave block.** On an adjacency Jordan block \(J_L(\beta)\), with \(\beta\in\{0,1\}\), represent its nilpotent parameter by \(a\) with \(a^L=0\). If \(X\) denotes the time-update, its defining relation is
\[
X^2+(\beta+a)X+1=0.
\]
The constant term ensures that \(X\) is invertible, so
\[
a=X^{-1}(X^2+\beta X+1).
\]
Eliminating \(a\) proves an isomorphism of \(2L\)-dimensional modules
\[
\mathbb F_q[a,X]/(a^L,X^2+(\beta+a)X+1)
\cong\mathbb F_q[X]/(X^2+\beta X+1)^L.
\]
This is an exact cyclic-module calculation. For \(\beta=0\) the polynomial is \((X+1)^2\); for \(\beta=1\) it is \(p(X)\). Combining this with Step 2 gives the module decomposition in the finding. It is valid even if \(p\) factors over the chosen extension field.

**Step 4: every fixed space.** For a cyclic \(\mathbb F_q[X]\)-module \(\mathbb F_q[X]/g(X)\), the kernel of multiplication by \(X^t-1\) has dimension \(\deg\gcd(g(X),X^t-1)\). Writing \(t=2^s w\) with \(w\) odd, characteristic two gives
\[
X^t-1=(X^w-1)^{2^s}.
\]
The polynomial \(X+1\) divides \(X^w-1\) exactly once; the two distinct primitive cube roots are roots of \(X^w-1\) exactly when \(3\mid w\), equivalently \(3\mid t\). Hence the kernel dimensions for each \((X+1)^{2L}\) and each \(p(X)^L\) block are respectively
\[
\min(h(t),2L),\qquad 2\mathbf1_{3\mid t}\min(h(t),L).
\]
Multiplying by the block multiplicities proves \(F(t)\) over every finite characteristic-two field.

**Step 5: exact order, support, and orbit counts.** A module \(\mathbb F_q[X]/(X+1)^{2L}\) has order \(2L\), while a \(p(X)^L\) module has order \(3L\). Both follow from the root orders and the highest Jordan lengths (since \(L\) is a power of two). Their least common multiple is \(6L\) in the odd-clique case and \(3L\) in the even-clique case. These are \(3\cdot2^r\) and \(3\cdot2^{r-1}\).

For odd \(m\), put \(U_j=q^{2\min(2^j,2L)}\) and \(W_j=q^{4(m-1)\min(2^j,L)}\). Then \(F(2^j)=U_j\) and \(F(3\cdot2^j)=U_jW_j\). For \(1\leq j\leq r\), \(U_j>U_{j-1}\), \(W_j\geq W_{j-1}>1\), and
\[
P(3\cdot2^j)=(U_j-U_{j-1})(W_j-1)+U_{j-1}(W_j-W_{j-1})>0.
\]
Also \(P(2^j)=U_j-U_{j-1}>0\) and \(P(3)=U_0(W_0-1)>0\). For even \(m\), \(F(2^j)=1\) for every \(j\), and \(F(3\cdot2^j)=q^{4m\min(2^j,L)}\) increases strictly for \(0\leq j\leq r-1\). Thus all listed primitive periods occur, and no other ones can occur because every period divides the exact global order. Möbius inversion of the fixed-point populations proves the formula for \(P(d)\); every primitive orbit has exactly \(d\) states. This completes the proof.

## Verification

Run `python3 verify_algebra.py` and `python3 verify_direct.py` with the Python 3 standard library. Exact binary matrix arithmetic (not floating point) checks the asserted time orders and fixed-space dimensions for \(r=3,4,5\) and \(m=3,4,5\), using 438 time-rank comparisons and explicitly verifying the prime-factor minimality of each asserted order. Direct neighbor-by-neighbor evolution enumerates all 65,536 paired states on the small eight-vertex boundary example \(C_4\square K_2\), and separately tests 60,000 deterministic pseudorandom states on four graphs within the theorem's domain. The boundary example is a regression check, not a newly claimed result. Recorded standard output is in `verify_algebra.out` and `verify_direct.out`.

For \(r=3\), \(q=2\) and odd \(m=3\), the numbers fixed at times \(1,2,3,4,6,8,12,24\) are respectively \(4,16,1024,256,1048576,65536,1099511627776,281474976710656\). For even \(m=4\), the global order is twelve, and the fixed populations at times \(1,3,6,12\) are \(1,65536,4294967296,18446744073709551616\). The examples illustrate the parity change in the least common temporal clock.

## Relationship to prior work

Macfarlane (2004) constructs first-order matrix equivalents for linear reversible second-order cellular automata and computes single-seed spacetime weights for three one-dimensional rules. Vlasov (2013) describes a general reversible two-state history construction. These works supply general reversible cellular-automaton context, not the clique-cylinder adjacency module or its full labelled finite-state orbit census. Tadaki (1994) gives the closest explicit prior dyadic-cycle calculation: one-dimensional first-order rule-90 and rule-150 dynamics, including nilpotence of rule 90 at powers of two. This establishes neither the additional clique module nor the reversible two-row temporal orbit census. Earlier first-order cylindrical-cellular-automaton counting methods and more recent Kronecker-sum matrix analyses concern related but different dynamics.

Related existing wave calculations cover pure dyadic Cartesian tori and mixed-parity products of complete graphs. Neither includes \(C_{2^r}\square K_m\) with \(r\geq3\): the first lacks a clique factor and the second contains no cycle of length at least eight as a Cartesian prime factor. The excluded \(r=2\) case can overlap with the Hamming product \(C_4=K_2\square K_2\). The present claim concerns the exact module, parity-dependent global period, all fixed populations, and complete primitive-period support for the stated family; generic reversibility and the use of Kronecker sums are not claimed to be new.

## Limitations

The theorem is restricted to characteristics two, a clique cross-section, and power-of-two cycle lengths at least eight. It does not classify non-dyadic cycles, nonlinear rules, transients of first-order automata, spatial-symmetry quotient orbits, or dynamics over odd-characteristic fields. Binary finite tests support, but do not substitute for, the unrestricted symbolic proof. The possibility of unindexed prior work involving the same cyclic modules remains an originality risk; no independent scientific audit is claimed.

## References

1. S. Tadaki, *Periodicity of cylindrical linear cellular automata*, arXiv:patt-sol/9412003v1, first submitted 1994-12-15. https://arxiv.org/abs/patt-sol/9412003
2. A. J. Macfarlane, *Linear reversible second-order cellular automata and their first-order matrix equivalents*, Journal of Physics A: Mathematical and General **37** (2004), 10791–10814, DOI: 10.1088/0305-4470/37/45/006. Public release dated 2004-10-28.
3. A. Yu. Vlasov, *On generalization of reversible second-order cellular automata*, arXiv:1311.4297v1, submitted 2013-11-18. https://arxiv.org/abs/1311.4297
4. E. Jen, *Cylindrical cellular automata*, Communications in Mathematical Physics **118** (1988), 569–590, DOI: 10.1007/BF01221109. Earlier general counting context; only month-level public date was located.
5. C.-H. Chang, Y.-C. Yang, F. Şah, *Reversibility of linear cellular automata with intermediate boundary condition*, AIMS Mathematics **9** (2024), 7645–7661, DOI: 10.3934/math.2024371. Relevant first-order Kronecker-sum context, not a source-date anchor.
