# Exact cyclic binary trigram-profile capacity and its rational generating function

## Finding
For each integer \(n\ge3\), let \(S(w)\) be the eight-count vector of the cyclic length-three factors, with multiplicity, of an indexed word \(w\in\{0,1\}^n\). Write \(T_n\) for the number of distinct such vectors. Then
\[
\sum_{n\ge1}T_nz^n=\frac{2z}{1-z}+\frac{z^2}{1-z^2}+\frac{2z^3}{(1-z)(1-z^2)(1-z^3)}+\frac{z^4(1+z^3)}{(1-z)^2(1-z^2)(1-z^3)(1-z^4)}.
\]
The initial counts at lengths three through twelve are
\[
(T_3,\ldots,T_{12})=(4,6,8,13,18,27,38,53,72,98).
\]
Furthermore, \(T_n=n^4/288+O(n^3)\). An injective code under this exact cyclic-read observation has at most \(T_n\) members, and selecting one word for each observed vector attains \(T_n\).

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\), all input words are indexed (rotations may denote different inputs), and each of the \(n\) cyclic windows of length three is counted even when positions wrap around. The observation discards the window order but retains its eight labeled multiplicities. The finding concerns the number of *distinct observations*, not the number of circular necklaces or the sizes of individual observation fibers. The displayed series has a well-defined extension to \(n=1,2\), although the principal statement is for \(n\ge3\).

## Proof
**Step 1: flow coordinates and realizability.** Use the binary order-two de Bruijn multigraph, whose vertices are `00`, `01`, `10`, `11` and whose directed edges are labeled `000`, `001`, `010`, `011`, `100`, `101`, `110`, `111`. The edge from a labeled three-word joins its first two symbols to its last two. A cyclic input produces one edge per starting position, hence balanced in/out degree at all four vertices. Consequently any observed vector is necessarily of the form
\[
(m_{000},m_{001},m_{010},m_{011},m_{100},m_{101},m_{110},m_{111})
=(a,b,c,d,b,c+d-b,d,h),
\]
where \(a,b,c,d,h\ge0\), \(c+d\ge b\), and
\[
a+h+b+2c+3d=n.\]
Conversely, these nonnegative multiplicities arise from one cyclic word if and only if their positive-edge support is weakly connected after isolated vertices are removed. Indeed, a nonempty finite directed balanced multigraph has an Euler circuit using all its edges exactly when its positive-edge support is weakly connected. Reading the successive appended edge symbols around that circuit produces the requisite cyclic binary word. This criterion is essential: balance alone permits disconnected directed loops with no single cyclic realization.

**Step 2: complete, disjoint connected-support classification.** There are five regimes:

1. \(b>0,d>0\): the edges `001`, `100`, `011`, `110` already connect all four vertices; any \(c\ge\max(0,b-d)\) and any \(a,h\ge0\) work.
2. \(b>0,d=0\): feasibility requires \(c\ge b\), \(h=0\), and arbitrary \(a\ge0\). Any \(h>0\) would create an isolated `11` loop.
3. \(b=0,d>0\): feasibility requires \(a=0\), arbitrary \(c,h\ge0\). Any \(a>0\) would create an isolated `00` loop.
4. \(b=d=0,c>0\): the only connected realization has \(a=h=0\), giving \(n=2c\) and the alternating cycle.
5. \(b=c=d=0\): precisely one of \(a,h\) is positive, giving two constant-word vectors for every positive \(n\).

The cases exhaust all possibilities because positive `001` and `011` edges determine whether the common directed core connects vertices `00` and `11`; when neither is present, the only possible non-loop core is the `01`–`10` two-cycle.

**Step 3: generating functions.** Every case is counted by its distinct integer parameters, not by its possibly many Eulerian word realizations. Case 5 contributes \(2z/(1-z)\); case 4 contributes \(z^2/(1-z^2)\). Cases 2 and 3 contribute equal series \(z^3/((1-z)(1-z^2)(1-z^3))\): in case 2 write \(c=b+s\) with \(b\ge1,s\ge0\), and in case 3 count \(d\ge1,c,h\ge0\).

For case 1 split \(b\le d\) and \(b>d\). If \(b\le d\), write \(d=b+t\), \(b\ge1,t\ge0\), and the length is \(4b+3t+2c+a+h\), producing
\[
\frac{z^4}{(1-z)^2(1-z^2)(1-z^3)(1-z^4)}.
\]
If \(b>d\), write \(b=d+1+t\), \(c=1+t+s\) with \(d\ge1,t,s\ge0\). The length is \(4d+3+3t+2s+a+h\), producing the same rational denominator with numerator \(z^7\). Summing all five disjoint contributions proves the displayed identity.

**Step 4: asymptotic and code optimum.** The final rational summand has a pole of order five at \(z=1\) with leading coefficient \(1/12\); the other terms have poles of order at most three there, and all other root-of-unity poles are lower order. Therefore the coefficient of \(z^n\) is \(\tfrac1{12}\binom{n+4}{4}+O(n^3)=n^4/288+O(n^3)\). For any decoder observing only \(S(w)\), at most one codeword may be taken from each spectrum class. Taking one representative from every class achieves exactly \(T_n\).

## Verification
Run `python3 verify.py` with Python 3 standard library only. It independently compares all five case-count sums with the rational coefficients at orders three through eighty, explicitly tests positive-support graph connectivity at orders three through twenty-two, and enumerates all binary input words at orders three through sixteen. The expected terminal marker is `VERIFY_OK`. Optionally compile `crosscheck.cpp` using `c++ -O3 -std=c++17 -o checker crosscheck.cpp` and run `./checker`; this independent implementation enumerates every input at lengths three through twenty-one and reports `CROSSCHECK_OK`. The included `counts.csv` lists coefficients for lengths three through fifty. These tests support the all-order symbolic proof; they do not by themselves prove it.

## Relationship to prior work
Jacquet, Knessl, and Szpankowski establish an integral representation and asymptotic count for balanced frequency matrices of first-order Markov types on a complete alphabet graph, and remark that their techniques extend to higher order. This supplies a broad enumeration framework, but not the evaluated generating function above for the *sparse four-vertex binary de Bruijn graph with connected positive support*. Arbitrary balanced vectors need not be realizable by one circular sequence. Karhumäki, Puzynina, Rao, and Whiteland investigate linear \(k\)-abelian classes and exact sizes of their individual fibers; they do not state this binary cyclic count. The published linear binary three-abelian class series OEIS A289657 differs because end boundaries and all shorter factors are included. Bresler, Bresler, and Tse analyze uniqueness of genome assembly from sequence reads, rather than counting the number of attainable full cyclic trigram profiles. The contribution here is the explicit all-order circular spectrum enumerator, with exact finite-block capacity and a connected-support classification; historical priority is not independently certified.

## Limitations
The theorem is for binary cyclic order-three *multiplicity* spectra. It does not give fiber-size distributions, classify all optimal codebooks beyond the one-per-fiber construction, establish analogous expressions for nonbinary alphabets or other read lengths, or address noisy sampling. The full-text search cannot rule out an unpublished or unindexed equivalent formula. The general Markov-type framework is a substantial antecedent and leaves a residual special-case-priority risk.

## References
- P. Jacquet, C. Knessl, and W. Szpankowski, "Counting Markov Types," *Discrete Mathematics & Theoretical Computer Science*, AofA proceedings, 2010; earliest public source listing dated 2009-12-31. DOI: https://doi.org/10.46298/dmtcs.2768 . Full text: https://dmtcs.episciences.org/en/articles/2768/download .
- J. Karhumäki, S. Puzynina, M. Rao, and M. A. Whiteland, "On cardinalities of k-abelian equivalence classes," first posted 2016-05-11. https://arxiv.org/abs/1605.03319 .
- G. Bresler, M. Bresler, and D. Tse, "Optimal Assembly for High Throughput Shotgun Sequencing," first posted 2013-01-01. https://arxiv.org/abs/1301.0068 .
- OEIS A289657, "Number of 3-abelian equivalence classes of words of length n over a binary alphabet," https://oeis.org/A289657 (linear rather than cyclic counts).
