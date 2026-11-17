# A sharp forty-nine-site gap and two entropy scales in Rule 126 periodic dynamics

## Finding

For every integer \(n\geq3\), let \(F_n\) be the synchronous elementary cellular automaton Rule 126 on indexed binary configurations of the cyclic ring \(\mathbb Z/n\mathbb Z\). Let \(C_2(n)\) and \(C_4(n)\) be the numbers of distinct orbits of **least temporal period exactly two and exactly four**, respectively, without identifying spatial rotations.

Put
\[
P_2(z)=1-z^4-2z^5-z^6,\qquad P_4(z)=1-z^{10}-2z^{11}-z^{12},
\]
and define integer sequences \(b_n,d_n\) by formal power series
\[
\sum_{n\ge1}b_nz^n=-\frac{zP_2'(z)}{P_2(z)},\qquad
\sum_{n\ge1}d_nz^n=-\frac{zP_4'(z)}{P_4(z)}.
\]
Then, for **every** \(n\ge3\),
\[
\boxed{C_2(n)=b_n/2,\qquad C_4(n)=d_n/2.}
\]
In particular, four-cycles exist exactly when \(n\) is a sum (with repetitions) of \(10,11,12\). Thus the **largest circumference without a primitive temporal four-cycle is \(49\)**, and every \(n\ge50\) admits one. At smaller sizes, the allowed lengths are exactly the union of intervals \([10k,12k]\) over positive integers \(k\).

Two distinct spatial exponential scales occur:
\[
C_2(n)\sim \tfrac12\rho^n,\qquad C_4(n)\sim\tfrac12\sigma^n,
\]
where \(\rho=1.324717957244746\ldots\) is the positive root of \(\rho^3-\rho-1=0\), whereas \(\sigma=1.134724138401519\ldots\) is the positive root of \(\sigma^6-\sigma-1=0\). Hence the primitive-four population grows exponentially but at a strictly smaller rate than the primitive-two population.

The exact fixed-point identities, useful for comparison with transfer matrices, are
\[
\#\operatorname{Fix}(F_n)=1,\quad
\#\operatorname{Fix}(F_n^2)=1+b_n,\quad
\#\operatorname{Fix}(F_n^4)=1+b_n+2d_n.
\]
The spatial dynamical zeta function on the temporal-four fixed subshift is consequently \(\big((1-z)P_2(z)P_4(z)^2\big)^{-1}\). The latter zeta concerns spatial translation on the fixed set of \(F^4\), not all temporal recurrence.

## Assumptions and scope

The neighborhood convention is \(f(a,b,c)=1\) if and only if the integer \(a+b+c\) is either one or two, otherwise zero. This corresponds to Wolfram code \(126\), whose transition row is `01111110` on neighborhoods ordered from `111` down to `000`. Each spatial position carries one bit and every update is simultaneous; indices are read modulo \(n\). The period of an orbit is its least positive **temporal** return time, not a return modulo spatial translation. States are labelled, so distinct cyclic rotations count separately as states and orbits unless temporal updates actually identify them. Only temporal periods one, two, and four are classified here; no assertion is made about all other temporal periods or transient basins.

## Proof

**1. Space–time transfer construction.** For a chosen height \(h\in\{1,2,4\}\), encode each temporal column as an integer \(a\) between \(0\) and \(2^h-1\), whose bit \(i\) is the cell value at time \(i\) modulo \(h\). Form a directed graph \(G_h\) on column-pair vertices \((a,b)\). There is an edge from \((a,b)\) to \((b,c)\) precisely when
\[
  f(a_i,b_i,c_i)=b_{i+1\bmod h}\qquad (0\le i<h).
\]
Any length-\(n\) closed directed walk in this graph records a cyclic space–time array of height \(h\) satisfying the local rule. Its initial row is an indexed configuration fixed by \(F_n^h\). Conversely, every such initial row generates exactly one such array and one closed walk with spatial origin fixed. This bijection holds for all \(n\ge3\), without requiring an approximation by large rings. Consequently
\[
\#\operatorname{Fix}(F_n^h)=\operatorname{tr}(A_h^n),
\]
where \(A_h\) is the integer adjacency matrix of \(G_h\).

**2. Complete finite component certificate.** Constructing all edges with the explicit eight-case local rule, and computing all directed strongly connected components that contain cycles, gives the following complete table. All components not listed are acyclic and contribute zero to traces of positive powers.

| Height | Cyclic component sizes | Elementary directed cycle lengths, with multiplicity |
|---|---|---|
| \(1\) | \(1\) | \(1\) |
| \(2\) | \(6,1\) | \(4,5,5,6\); \(1\) |
| \(4\) | \(12,12,6,1\) | \(10,11,11,12\) in each size-twelve component; \(4,5,5,6\); \(1\) |

This table is a finite, reproducible certificate, not a numerical inference from large \(n\): `verification/transfer_check.py` constructs the entire graph for each listed height by direct integer operations, enumerates every cyclic strongly connected component by Tarjan's algorithm, and enumerates **every elementary cycle** in each component by a depth-first search rooted at the smallest vertex of the cycle. It checks the component sizes, their complete cycle-length multisets, and the existence of a vertex common to every elementary cycle of each component. Its independent adjacency-power trace calculation agrees with the stated formulas at circumferences three through twelve. All assumptions, loops and boundary conditions are in that standalone script; there is no external data file.

**3. Determinants and traces.** For a finite directed component in which all elementary cycles meet at a common vertex, no two elementary cycles are vertex-disjoint. The elementary-cycle determinant expansion thus gives \(\det(I-zA)=1-\sum_Cz^{|C|}\), where the sum ranges over all its elementary cycles. Applying the exact table, the cyclic components at height two contribute \(1-z\) and \(P_2(z)\). At height four they contribute \(1-z\), \(P_2(z)\), and two copies of \(P_4(z)\). All acyclic components contribute determinant one. Hence
\[
\det(I-zA_1)=1-z,\quad
\det(I-zA_2)=(1-z)P_2(z),\quad
\det(I-zA_4)=(1-z)P_2(z)P_4(z)^2.
\]
For every finite matrix over the integers, the formal identity
\[
\sum_{n\ge1}\operatorname{tr}(A^n)z^n=-z\frac{d}{dz}\log\det(I-zA)
\]
holds as an identity of formal power series. The three displayed fixed-point counts follow for all \(n\ge3\). The height-one transfer graph has only the all-zero self-loop among its directed cycles. It follows that the all-zero configuration is the only temporal fixed state of Rule 126 at every circumference.  Subtracting the fixed configurations from the two-step fixed set gives \(2C_2(n)=b_n\); subtracting the two-step fixed set from the four-step fixed set gives \(4C_4(n)=2d_n\).

**4. Sharp existence threshold.** The coefficient \(d_n\) is positive if and only if the length-\(n\) spatial trace in either size-twelve component is positive, which holds exactly when \(n\) is a nonnegative combination of elementary-cycle lengths \(10,11,12\) with positive total. Because these cycles all pass through one vertex, any concatenation gives a closed walk, and any closed walk decomposes into elementary cycles. A sum of \(k\) terms, each one of \(10,11,12\), gives every integer in \([10k,12k]\). The intervals for \(k\ge5\) meet or overlap, so every integer from fifty onward occurs; forty-nine is not in the union. This proves both the precise semigroup condition and the largest excluded circumference.

**5. Growth rates.** The characteristic polynomials of the nontrivial components are \(\lambda^6-(\lambda+1)^2\) and \(\lambda^{12}-(\lambda+1)^2\). They factor as \((\lambda^3-\lambda-1)(\lambda^3+\lambda+1)\) and \((\lambda^6-\lambda-1)(\lambda^6+\lambda+1)\), respectively. Both corresponding adjacency components are strongly connected and aperiodic (their simple cycle lengths have greatest common divisor one). Thus Perron–Frobenius yields a unique simple dominant positive eigenvalue, respectively \(\rho\) and \(\sigma\); all other eigenvalues in that component have strictly smaller modulus. Each component's trace is therefore its dominant root raised to \(n\), plus an exponentially smaller term. The two size-twelve components contribute equally. Dividing trace counts by temporal orbit size proves the asymptotic formulas with leading coefficient one-half. Since \(\rho^3=\rho+1\), one has \(\rho^6=(\rho+1)^2>\rho+1\); monotonicity of \(x^6-x-1\) for \(x\ge1\) gives \(\sigma<\rho\).

## Verification

Both supplied programs require no external scientific data. From the package root, run `python3 verification/transfer_check.py` and compile `g++ -O3 -std=c++17 verification/direct_check.cpp -o /tmp/rule126_direct_check`, followed by `/tmp/rule126_direct_check`. The first checks the complete recurrent component structure for heights one, two, three and four, all elementary cycles and common-vertex conditions, direct matrix traces through circumference twelve, and the all-size renewal coefficient formula and semigroup bounds. The second independently enumerates all \(2^n\) configurations for every circumference three through twenty, applying the rule directly and comparing exact two-step and four-step return counts against the transfer formula. Recorded successful outputs appear in `verification/transfer_output.txt` and `verification/direct_output.txt`. The finite all-height transfer graph certificate establishes the theorem for all lengths; bounded brute-force agreement is a cross-check, not an infinite proof.

## Relationship to prior work

Martínez, Adamatzky, Seck-Tuoh-Mora and Alonso-Sanz analyze Rule 126 with mean-field, finite-ring attractors through length eighteen, and extended de Bruijn diagrams including selected two-generation traveling patterns. These methods and finite examples are acknowledged; their inspected discussion does not state the exact all-circumference primitive temporal four-cycle counts, the sharp last absent circumference forty-nine, or the two exponential temporal-period scales. McIntosh's earlier Rule 126 treatment in *Linear Cellular Automata* develops predecessor and subset diagrams; its inspected sections address ancestor counts rather than these temporal-return populations. A published exact Rule 18 **two-cycle** formula has the same polynomial \(P_2\), but concerns a different local rule and only height two; that coincidence does not yield the Rule 126 height-four graph decomposition or its semigroup threshold. Separate published Rule 126 results on one-step image sizes and preimage multiplicities calculate different inverse-image invariants, which do not determine fixed points of four iterates.

## Limitations

This theorem does not classify Rule 126's eventual periods other than one, two and four, its complete long-term recurrent set, or the sizes of attraction basins. The entropy comparison concerns spatial growth of two precisely specified temporal orbit populations, not Kolmogorov–Sinai entropy of the full time dynamical system. Historical priority is not established absolutely; older diagrams might encode related count information without a published formula. The finite graph certificate is directly executable and the claimed orbit counts do not depend on unavailable external computations.

## References

1. G. J. Martínez, A. Adamatzky, J. C. Seck-Tuoh-Mora and R. Alonso-Sanz, *How to Make Dull Cellular Automata Complex by Adding Memory: Rule 126 Case Study*, Complexity **15** (2010), 34–49, https://doi.org/10.1002/cplx.20311 ; open author preprint https://arxiv.org/abs/1212.0124 (posted 2012-12-01).
2. H. V. McIntosh, *Linear Cellular Automata*, Chapter 8, especially §§8.7–8.8 on the Rule 126 subset diagram, https://delta.cs.cinvestav.mx/~mcintosh/cellularautomata/Papers_files/lcau.pdf .
3. *Exact temporal-two orbit census and spatial zeta for elementary cellular automaton 18*, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-temporal-two-orbit-census-and-spatial-zeta-for-elementary--752b17859ec3 .
4. *Perron–Lucas and Fibonacci laws for periodic images of elementary Rule 126*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-perron-lucas-and-fibonacci-laws-for-periodic-images-of-elementar--f92703bac447 .
5. E. W. Weisstein, *Rule 126*, MathWorld, https://mathworld.wolfram.com/Rule126.html .
