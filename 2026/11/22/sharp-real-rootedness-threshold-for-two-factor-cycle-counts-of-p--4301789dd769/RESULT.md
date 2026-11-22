# Sharp real-rootedness threshold for two-factor cycle counts of prism graphs

## Finding

Let \(Y_n=C_n\square K_2\) be the simple prism on \(2n\) labelled vertices, for every integer \(n\ge3\). Define its cycle-count polynomial
\[
F_n(z)=\sum_{H\text{ spanning two-factor of }Y_n}z^{\kappa(H)},
\]
where \(\kappa(H)\) denotes the number of connected cycles of \(H\), and let \(M_n(z)=\sum_{k\ge0}m_{n,k}z^k\) be the ordinary matching polynomial by cardinality (not the alternating-sign matching polynomial) of the base cycle \(C_n\). Then
\[
\boxed{F_n(z)=M_n(z)-1+z^2+2\mathbf1_{2\mid n}z,\qquad
m_{n,k}=\frac{n}{n-k}\binom{n-k}{k}\quad(0\le k\le\lfloor n/2\rfloor).}
\]
In particular, \(F_n\) has only real zeros **if and only if** \(3\le n\le7\); for every \(n\ge8\), it has at least one nonreal conjugate pair. This is a uniform, sharp real-rootedness boundary across the entire prism family. The polynomial counts each undirected spanning two-factor exactly once, independent of orientations or labelled traversals.

The known scalar counting consequences follow: the total number of two-factors equals \(L_n+2\mathbf1_{2\mid n}\), where \(L_n\) is the ordinary Lucas number; the number of Hamiltonian two-factors is \(n+2\mathbf1_{2\mid n}\). These total and Hamiltonian counts are included as consistency checks, not novelty claims.

## Assumptions and scope

The graph is the simple Cartesian product of a length-\(n\) cycle, \(n\ge3\), and a single edge. All vertices and graph edges are distinguishable, and a two-factor means a spanning two-regular **edge subset**, so its components are undirected cycles. Cubicity implies that complementation maps two-factors bijectively to perfect matchings. The variable \(z\) records the number of components of the two-factor; it does **not** record the size of a matching, except under the explicit correspondence established below.

## Proof

**Classification of perfect matchings.** Name the two rim vertices over each cycle position \(i\) by \((i,0)\) and \((i,1)\). If a perfect matching contains any vertical rung, then removing all matched rungs leaves a disjoint union of paths along the two rims. Each path is of even order and has a unique perfect matching. Hence the horizontal edges of the matching occur in identical pairs, one on each rim, at a matching \(A\subseteq E(C_n)\). Conversely, any matching \(A\) of the base cycle yields a unique perfect matching: take both horizontal copies of every edge of \(A\) and all vertical rungs at vertices not incident to \(A\). This description also includes the all-rung perfect matching when \(A=\varnothing\) and both in-phase all-horizontal matchings when \(n\) is even and \(A\) is perfect. The only omitted possibilities are, for even \(n\), the two all-horizontal matchings using opposite alternating phases on the two rims. There are no omitted matchings for odd \(n\).

**Cycle components of the complement.** For each nonempty base matching \(A\), the graph obtained by deleting the edges of \(A\) from \(C_n\) consists of exactly \(|A|\) disjoint paths. In the complementary two-factor, each such rim path has two copies, joined at their endpoints by the vertical rungs, so these form exactly \(|A|\) cycles. For \(A=\varnothing\), the complement comprises the two intact rims and therefore has two cycles. Each of the two exceptional opposite-phase all-horizontal perfect matchings (possible only for even \(n\)) has a connected Hamiltonian complement. These mutually exhaustive cases give the boxed identity without duplications.

**Cycle-matching coefficients.** For \(1\le k\le\lfloor n/2\rfloor\), a size-\(k\) matching on the labelled cycle is a cyclic choice of \(k\) mutually nonadjacent edges. The usual gap count, or rotation double counting, gives \(m_{n,k}=\frac{n}{n-k}\binom{n-k}{k}\); also \(m_{n,0}=1\).

**The threshold.** Put \(m=\lfloor n/2\rfloor\). For \(n\ge8\), the positive-coefficient polynomial \(F_n(z)/z\) has degree \(d=m-1\ge3\). Its first three coefficients are
\[
a=n+2\mathbf1_{2\mid n},\qquad
b=\frac{n(n-3)}2+1,\qquad
c=\frac{n(n-4)(n-5)}6.
\]
If every zero were real, they would all be strictly negative because all coefficients are positive, and Newton's inequalities would require
\[
\left(\frac b d\right)^2\ge\frac{ac}{\binom d2},\qquad\text{equivalently}\qquad (d-1)b^2\ge2dac.
\]
In fact, with \(\Delta=2dac-(d-1)b^2\), direct algebra yields
\[
3\Delta=(m-2)(m-1)(4m^3-55m+3)\quad\text{when }n=2m,
\]
and
\[
3\Delta=(m-2)(4m^4-12m^3-15m^2+14m+6)\quad\text{when }n=2m+1.
\]
For every integer \(m\ge4\), the first expression is positive because \(4m^3-55m+3=m(4m^2-55)+3>0\); the second is positive because its quartic factor equals \(m^2(4m^2-12m-15)+14m+6>0\), and \(4m^2-12m-15\ge1\) on \(m\ge4\). This contradicts Newton's necessary inequality, proving nonreal zeros for **all** \(n\ge8\).

For the remaining \(3\le n\le7\), direct coefficient formulas give
\[
\begin{aligned}
F_3(z)&=z(z+3),&F_4(z)&=3z(z+2),\\
F_5(z)&=z(6z+5),&F_6(z)&=2z(z+1)(z+4),\\
F_7(z)&=z(7z^2+15z+7).
\end{aligned}
\]
The last quadratic has discriminant \(15^2-4\cdot7\cdot7=29>0\); both roots are negative. This completes the sharp classification.

## Verification

A standalone standard-library Python program, `prism_twofactor_verify.py`, enumerates all perfect matchings of the labelled prisms for \(3\le n\le14\), counts connected components directly in each complementary two-factor, and compares every coefficient against both the claimed closed form and an independent brute-force matching enumeration on \(C_n\). It additionally checks the exact Newton-defect expressions for \(4\le m\le200\) and verifies the low-order boundary polynomials. All checks pass. These finite tests support, but do not replace, the complete proof for arbitrary \(n\).

The identity yields the known total factor count \(F_n(1)=L_n+2\mathbf1_{2\mid n}\), consistent with the earlier total perfect-matching census. It also gives the known Hamiltonian coefficient \([z]F_n=n+2\mathbf1_{2\mid n}\), whose directed double appears in a standard sequence database.

## Relationship to prior work

Cao, Lu and Zhao (first posted 2026-07-22, arXiv:2607.20157) study matching and two-factor packing existence for percolated vertex-transitive host graphs. Their work motivates a closer look at the components of two-factors in a sparse vertex-transitive family; it does not give the present component-count polynomial or its zero geometry. The earlier paper of Lekshmi and West (arXiv:2003.09602) already gives the **total number** of perfect matchings of prism graphs. That scalar enumeration is fully credited here and follows by setting \(z=1\). The known undirected Hamiltonian count also agrees with OEIS A124349 after dividing the recorded directed count by two. Neither the scalar total nor the Hamiltonian count, by itself, determines the distribution or the real-zero threshold. Searches of published mathematical records for equivalent prism two-factor cycle-count distributions, polynomial transforms, and real-rootedness boundaries revealed no directly covering claim. Historical uniqueness is not established by search alone.

The phrase *two-factor polynomial* is used for a different invariant in Baldridge, Lowrance and McCarty (2020); the polynomial here is specifically the ordinary generating function by the number of connected components of spanning two-factors.

## Limitations

This statement is for the simple circular prism \(C_n\square K_2\), not Möbius ladders, arbitrary cubic graphs, random regular graphs, or percolated prisms. Non-real-rootedness does not imply failure of coefficient log-concavity. The older full text of arXiv:2003.09602 was not obtainable through the accessible open-text links during this comparison; its abstract and stated scalar theorem were checked, so unseen refinements in its proof remain a specific historical-priority risk. No independent expert or external audit of this theorem is claimed.

## References

1. M. Cao, M. Lu, X. Zhao, *Matchings and Near-Optimal 2-Factor Packings in Percolated Vertex-Transitive Graphs*, arXiv:2607.20157, first public 2026-07-22, https://arxiv.org/abs/2607.20157.
2. R. S. Lekshmi, D. B. West, *The Number of Perfect Matchings in Möbius Ladders and Prisms*, arXiv:2003.09602, first public 2020-03-21, https://arxiv.org/abs/2003.09602.
3. OEIS A124349, *Numbers of directed Hamiltonian cycles on the n-prism graph*, https://oeis.org/A124349.
4. S. Baldridge, A. M. Lowrance, B. McCarty, *The 2-Factor Polynomial Detects Even Perfect Matchings*, Electron. J. Combin. 27 (2020), P2.27, https://doi.org/10.37236/9214.
