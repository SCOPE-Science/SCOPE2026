# Lucas arithmetic and the first exponential short-return class in elementary Rule 110

## Finding
For every positive integer \(n\), let \(F_n\) be elementary binary cellular automaton Rule 110 on \(n\) indexed sites with periodic boundary conditions. Let \(a_t(n)=|\{x\in\{0,1\}^n:F_n^t(x)=x\}|\), with positive \(t\). Define the Lucas sequence by \(L_0=2\), \(L_1=1\), and \(L_{j+2}=L_{j+1}+L_j\).

**Theorem.** The complete counts through temporal return five are
\[
 a_1(n)=1,\qquad a_2(n)=a_4(n)=1+4\,\mathbf1_{4\mid n},\qquad
 a_3(n)=1+9\,\mathbf1_{9\mid n},
\]
and
\[
 a_5(n)=\begin{cases}
 1,&5\nmid n,\\
 1+5\bigl(2^m+2(-1)^m L_m\bigr),&n=5m.
 \end{cases}
\]
In particular, every nontrivial configuration fixed by the fifth iterate has **least temporal period five**, and the number of such temporal orbits on the labelled length-\(5m\) ring is exactly \(2^m+2(-1)^m L_m\). This number vanishes precisely for \(m=1,3\), and is positive for every other positive \(m\). Thus primitive five-cycles occur at exactly the lengths divisible by five other than lengths five and fifteen. Their labelled configuration population grows as \(5\cdot 2^{n/5}\) along multiples of five; through return times one to four, all nonzero-return populations remain bounded independently of \(n\).

Equivalently, the spatial dynamical zeta function of the set of configurations fixed by five temporal updates is the rational function
\[
 \exp\left(\sum_{n\ge1}\frac{a_5(n)z^n}{n}\right)
 =\frac{1}{(1-z)(1-2z^5)(1+z^5-z^{10})^2}.
\]
The restriction to *initially periodic states* is essential: this does not count eventual attractor basins.

## Assumptions and scope
A configuration is a binary word indexed by \(\mathbb Z/n\mathbb Z\), including the legitimate degenerate cases \(n=1,2\) where several neighborhood positions coincide. Site \(i\) updates using the Wolfram convention
\[
 f(a,b,c)=\bigl(110\mathbin{\mathrm{div}}2^{4a+2b+c}\bigr)\bmod 2,
 \quad (a,b,c)=(x_{i-1},x_i,x_{i+1}),
\]
for binary \(a,b,c\). Thus the truth-table outputs from neighborhoods \(111,110,101,100,011,010,001,000\) are \(0,1,1,0,1,1,1,0\), respectively. Each site updates simultaneously. Temporal period means its least strictly positive return time. Spatial rotations of an indexed word are **not** identified; rotations that happen to be the same word are still one configuration.

## Proof
**1. Finite-window reduction for all spatial lengths.** The result after \(t\) updates at a central site is determined by its radius-\(t\) block of \(2t+1\) bits. For each \(t=1,2,3,4,5\), create a directed graph \(G_t\) on all binary blocks of length \(2t\). An edge indexed by the block \(w_0\ldots w_{2t}\) goes from its first \(2t\) bits to its last \(2t\) bits if, and only if, applying the local three-bit Rule 110 map successively \(t\) times to the block produces exactly \(w_t\) at the center.

Every indexed length-\(n\) circular binary word defines an indexed closed walk of length \(n\) in this graph if and only if it returns after \(t\) updates. Conversely, a rooted closed walk is uniquely determined by its successive overlap bits and determines that indexed circular word. This bijection also holds when \(n\le 2t\): in a closed walk, the overlapping windows necessarily repeat symbols at the corresponding cyclic positions. Therefore, if \(A_t\) is the integer adjacency matrix, \(a_t(n)=\operatorname{tr}(A_t^n)\) for every \(n\ge1\).

**2. Exact finite graph certificate.** Reconstruct the entire graph deterministically by enumerating its \(2^{2t+1}\) possible local blocks, performing the prescribed \(t\) local updates, and retaining precisely those returning the central bit. Compute its strongly connected components. Only cyclic components contribute to traces of positive powers. The exhaustive exact-integer script `verify_graph.py` performs these operations and computes \(\det(I-zA_t)\) for the cyclic components from the first \(d\) closed-walk traces on each component of size \(d\). The Newton recurrence used is
\[
 c_0=1,\quad k c_k=-\sum_{j=1}^k c_{k-j}\operatorname{tr}(B^j)
 \qquad(1\le k\le d),
\]
where \(\det(I-zB)=\sum_{k=0}^d c_k z^k\). Every intermediate operation uses exact integers, including divisibility by \(k\). The complete graph sizes and certified determinant products are:

| \(t\) | graph vertices | retained edges | cyclic component sizes | \(\det(I-zA_t)\) |
| --- | ---: | ---: | --- | --- |
| 1 | 4 | 5 | 1 | \(1-z\) |
| 2 | 16 | 17 | 1, 4 | \((1-z)(1-z^4)\) |
| 3 | 64 | 66 | 1, 9 | \((1-z)(1-z^9)\) |
| 4 | 256 | 250 | 1, 4 | \((1-z)(1-z^4)\) |
| 5 | 1024 | 1042 | 1, 64 | \((1-z)(1-2z^5)(1+z^5-z^{10})^2\) |

The size-64 component for \(t=5\) has 74 internal directed edges. In particular its characteristic polynomial equals
\[
 \lambda^{39}(\lambda^5-2)(\lambda^{10}+\lambda^5-1)^2.
\]
The attached code recomputes the graph and every determinant coefficient from first principles: no numerically fitted recurrence or unverified large-\(n\) extrapolation is used. This exact finite certificate proves the determinant identity for all \(n\).

**3. Extract the all-length populations.** The formal identity
\[
 -\log\det(I-zA_t)=\sum_{n\ge1}\operatorname{tr}(A_t^n)\frac{z^n}{n}
\]
turns the first four determinant products into the stated small-return counts. For \(t=5\), put \(u=z^5\). Let \(\alpha,\beta\) be the roots of \(v^2+v-1=0\); thus \(\alpha+\beta=-1\) and \(\alpha\beta=-1\). Since \(1+u-u^2=(1-\alpha u)(1-\beta u)\), the nontrivial trace for \(n=5m\) equals \(5\cdot2^m+10(\alpha^m+\beta^m)\), vanishing for lengths not divisible by five. Because \(\alpha^m+\beta^m=(-1)^m L_m\), the claimed formula follows.

**4. Least period and sharp exclusions.** Since five is prime and the only fixed Rule 110 word is the all-zero word, subtracting one from \(a_5(n)\) counts exactly the least-period-five configurations. Dividing by five counts temporal orbits, since each primitive orbit has five distinct phases. For \(m=1,3\), the Lucas values give \(2^m=2L_m\), so there are no cycles. For even \(m\) the formula is positive. For odd \(m\ge5\), the base case \(m=5\) is \(2^5-2L_5=10>0\); the inequality \(L_{m+2}<3L_m\) for \(m\ge5\) preserves strict positivity upon increasing \(m\) by two, because \(2^{m+2}=4\cdot2^m\). This establishes exactly the asserted period-five circumference spectrum. The leading \(2^m\) term dominates \(L_m=O(\varphi^m)\), where \(\varphi=(1+\sqrt5)/2<2\).

## Verification
Run `python3 verify_graph.py > graph_output.json`. The self-check reconstructs graphs for all \(1\le t\le5\), their cyclic strongly connected components, and their complete integer determinant coefficients. It prints `"certificate": "PASS"` only after every expected identity and component-size assertion succeeds. It requires Python 3 and no third-party packages. For separate direct state-space enumeration run `c++ -std=c++17 -O2 verify_direct.cpp -o verify_direct && ./verify_direct > direct_output.txt`. The C++ code uses a different bit-parallel update and enumerates **all** \(2^n\) initial binary words for every \(1\le n\le20\), checking all five temporal return counts. The expected last line is `ALL_EXHAUSTIVE_CHECKS_PASS n=1..20`. The attached JSON and text files record actual outputs. These independent finite checks supplement, rather than replace, the all-size finite-graph proof.

## Relationship to prior work
The elementary cellular automaton formalism originates in Wolfram's 1983 work. Cook (2004) established universality of Rule 110 through a glider construction; that is a qualitatively different dynamical statement. Martínez, McIntosh, Seck Tuoh Mora and Chapa Vergara (2007) explicitly discuss extended de Bruijn diagrams and Rule 110 glider phases; the diagrammatic method is precedent and is not claimed to be new. Martínez, Adamatzky and McIntosh (2016) investigate computations on finite Rule 110 collider rings, but the inspected exposition addresses engineered glider interactions rather than an all-circumference fixed-fifth-iterate zeta or exact Lucas sequence. A distinct published published-finding corpus computation gives the spatial zeta of the **one-step image** of Rule 110, not the spatial zeta of configurations satisfying \(F_n^5(x)=x\). The complete all-size formulas, the fifteen-cell exception and the precise exponential onset are the claims being compared, not the previously established Rule 110 model or generic transfer-matrix technique.

## Limitations
The theorem counts **immediately** temporally returning configurations only, for return times through five. It does not enumerate all eventual basins or determine the full infinite temporal-period spectrum. The proof is a reproducible exact finite-state integer certificate, not a handwritten list of 1024 local transitions, and the certificate has not received an independent external audit. Although the literature comparison includes primary full texts and indexed searches, an unindexed older enumeration or inaccessible monograph could contain an equivalent five-return formula; historical priority is not definitively established.

## References
1. S. Wolfram, “Statistical mechanics of cellular automata,” *Reviews of Modern Physics* **55**, 601 (1983), DOI: 10.1103/RevModPhys.55.601 (public date 1983-07-01).
2. M. Cook, “Universality in Elementary Cellular Automata,” *Complex Systems* **15** (2004), DOI: 10.25088/ComplexSystems.15.1.1.
3. G. J. Martínez, H. V. McIntosh, J. C. Seck Tuoh Mora, S. V. Chapa Vergara, “Determining a regular language by glider-based structures called phases fi_1 in Rule 110,” arXiv:0706.3348 (2007).
4. G. J. Martínez, A. Adamatzky, H. V. McIntosh, “A Computation in a Cellular Automaton Collider Rule 110,” arXiv:1609.05240 (2016).
