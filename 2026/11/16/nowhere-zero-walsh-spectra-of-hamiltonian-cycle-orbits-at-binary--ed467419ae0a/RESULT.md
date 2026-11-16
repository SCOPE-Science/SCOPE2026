# Nowhere-zero Walsh spectra of Hamiltonian-cycle orbits at binary-digit record orders

## Finding

Let \(n\ge 3\) and write \(G_n=\mathbb F_2^{E(K_n)}\), with one binary coordinate for every edge of the complete graph. Let \(\mathcal H_n\subset G_n\) be the incidence vectors of its *unoriented* Hamiltonian cycles. There are \(M_n=(n-1)!/2\) such cycles. For any edge subset \(A\subseteq E(K_n)\), its unnormalized Walsh coefficient is
\[
W_n(A)=\sum_{C\in\mathcal H_n}(-1)^{|C\cap A|}.
\]

**Theorem.** For every pair of integers \(k\ge1\), \(j\ge0\) satisfying \(n=(2^k-1)2^j\ge3\), and *every* edge subset \(A\),
\[
\boxed{W_n(A)\equiv M_n\pmod{2^{\nu_2(M_n)+1}}},
\qquad \nu_2(M_n)=n-2-s_2(n-1),
\]
where \(s_2(r)\) is the number of ones in the binary expansion of the nonnegative integer \(r\), and \(\nu_2\) is the two-adic valuation of a nonzero integer. In particular, every coefficient has exactly that two-adic valuation, and none vanish. Thus the unnormalized Walsh transform of \(\mathbf1_{\mathcal H_n}\) has full support, and convolution by \(\mathbf1_{\mathcal H_n}\) is an invertible linear operator on complex-valued functions on \(G_n\).

The admissible orders are precisely those for which \(s_2(n-1)\) is at least \(s_2(u)\) for every \(0\le u\le n-1\). They include \(3,4,6,7,8,12,14,15,16,24,28,30,31,32\), and infinitely many others.

**Motivated boundary.** A binary-digit hypothesis is substantive: at order \(5\), choosing a single negative edge produces \(W_5(A)=0\); at order \(9\), choosing as negative exactly the six edges induced by four designated vertices produces \(W_9(A)=0\). Hence no universal nonvanishing theorem holds for all orders.

## Assumptions and scope

All graph cycles are undirected, considered up to rotation and reversal. Every sign assignment on \(K_n\) is allowed. The transform is unnormalized: each coefficient is a signed integer count, and the Fourier transform convention is \(\widehat f(A)=\sum_{x\in G_n}f(x)(-1)^{A\cdot x}\). No assumption is made that the signed graph is balanced or that the cycle signs are individually constant. The infinite-parameter congruence is asserted for the indicated orders only; the boundary examples are exact statements at orders \(5\) and \(9\).

## Proof

**1. Signed subgraph expansion.** For a fixed edge subset \(A\), write \(N_n(F)\) for the number of undirected Hamiltonian cycles containing every edge of \(F\). Expanding the product of edge signs gives the finite integer identity
\[
W_n(A)=\sum_{F\subseteq A}(-2)^{|F|}N_n(F),
\qquad N_n(\varnothing)=M_n.
\]
This holds because \((-1)^{|A\cap C|}=\prod_{e\in A\cap C}(1-2)\).

**2. Cycle-extension count.** Suppose \(F\ne\varnothing\) has \(t=|F|\le n-3\). If \(F\) is contained in a Hamiltonian cycle, its non-isolated components are \(h\ge1\) vertex-disjoint paths. Contract each path to a block, leaving isolated vertices as singleton blocks. There are \(n-t\ge3\) blocks. The number of unoriented cyclic orderings of the blocks is \((n-t-1)!/2\), and each of the \(h\) nontrivial path blocks has two possible orientations. Consequently,
\[
N_n(F)=2^{h-1}(n-t-1)!.
\]
If \(F\) cannot extend to a Hamiltonian cycle, then \(N_n(F)=0\), and the following divisibility is automatic.

**3. Binary-digit divisibility.** Put \(m=n-1\). The parameter condition can be written \(n=2^r-2^j\), with \(r>j\ge0\); hence \(m=2^r-1-2^j\). Its \(r\)-bit representation has exactly one zero among the otherwise all-one digits, so \(s_2(m)=r-1\). Every \(0\le u\le m\) has at most \(r-1\) ones (the only \(r\)-one number below \(2^r\) is larger than \(m\)). Thus
\[
s_2(m-t)\le s_2(m)\qquad (0\le t\le m).
\]
Legendre's valuation identity gives \(\nu_2(a!)=a-s_2(a)\) for every nonnegative integer \(a\). If \(1\le t\le n-3\) and \(N_n(F)\ne0\), the path-extension count implies
\[
\begin{aligned}
\nu_2(2^tN_n(F))
&=t+h-1+\nu_2((m-t)!)\\
&=m-s_2(m-t)+h-1\\
&\ge m-s_2(m)=\nu_2(M_n)+1.
\end{aligned}
\]
For \(t\ge n-2=m-1\), the factor \(2^t\) alone is divisible by \(2^{m-s_2(m)}\), since \(s_2(m)\ge1\). Therefore every nonempty term in the subgraph expansion is divisible by \(2^{\nu_2(M_n)+1}\). Only the empty-set term remains, proving the congruence. Since \(M_n/2^{\nu_2(M_n)}\) is odd, the congruence forces \(\nu_2(W_n(A))=\nu_2(M_n)\) and \(W_n(A)\ne0\) for every \(A\).

**4. Intrinsic binary-digit characterization.** The stated parameter family achieves \(s_2(m)=\max_{0\le u\le m}s_2(u)\). Conversely, if \(m\) has \(r\) binary digits, then \(2^{r-1}-1<m\) has \(r-1\) ones unless \(m=1\). Therefore the maximum condition forces \(m\) to have either all \(r\) bits equal to one or exactly one zero. In the first case \(n=2^r\); in the second \(m=2^r-1-2^j\), so \(n=2^r-2^j=(2^{r-j}-1)2^j\). Both cases lie in the given family. This characterization includes the permitted small cases.

**5. Boundary examples.** At \(n=5\), six of the twelve Hamiltonian cycles contain a fixed edge, and six do not; their signed sum is zero. At \(n=9\), give negative sign to exactly the six edges of a fixed four-vertex clique and positive sign to every other edge. The numbers of the \(20{,}160\) unoriented Hamiltonian cycles using exactly \(0,1,2,3\) negative edges are respectively \(1{,}440,8{,}640,8{,}640,1{,}440\). The alternating sum is zero. These finite identities are also certified in the standalone checker, using separate direct cycle enumeration and signed dynamic programming.

**6. Fourier corollary.** Under the stated Walsh convention, convolution by \(\mathbf1_{\mathcal H_n}\) is diagonalized by the group characters, with eigenvalues exactly \(W_n(A)\). Every eigenvalue is nonzero, so the convolution operator is invertible. This uses no analytic limiting argument.

## Verification

Run `python3 check_hamilton.py` with a standard Python 3 interpreter. It checks complete exact-integer Walsh transforms on vertex-switching quotients for all \(3\le n\le8\), including the claimed valuation and support for the qualifying sizes. For \(n\le7\), an independent Held–Karp signed-cycle recurrence agrees on random signings. Additional exact signed-recurrence checks cover qualifying sizes \(12,14,15,16\). It independently verifies the two boundary counterexamples and tests the binary-digit characterization through \(n=160\).

The computation prints `BINARY_HAMILTONIAN_2ADIC_CHECKS_PASS` only after all assertions succeed. Finite tests do not establish the all-orders theorem; the subgraph expansion and valuation argument above do.

## Relationship to prior work

Gimbel (2004) characterizes edge labels for which every Hamiltonian cycle has the *same* aggregate label. In contrast, the present theorem allows arbitrary labels and proves a noncancellation congruence for the *sum* of cycle signs. Staples (2014) gives Hamiltonian-cycle enumeration formulas involving determinants and permanents, without a universal two-adic nonvanishing law in the inspected main theorem. Yan (2025) characterizes when signed complete graphs have Hamiltonian cycles of both signs; that existence dichotomy does not determine their difference in number. The order-five and order-nine zero examples exhibit why sign-existence alone cannot imply the present congruence. Standard Fourier theory supplies diagonalization, but not the new arithmetic divisibility. These sources are mathematical context, not evidence of absolute historical priority.

## Limitations

The theorem does not assert nonvanishing at every positive integer order, nor does it classify the full distributions of Walsh coefficients or their sharp projection norms. The two finite boundary examples do not establish failure at *every* excluded order. Independent mathematical validation and exhaustive historical-priority review have not been performed. Published literature may contain an equivalent formulation not found in the comparisons described here.

## References

- J. Gimbel, *Abelian Group Labels on Hamiltonian Cycles*, Journal of Combinatorial Mathematics and Combinatorial Computing **51** (2004), 3–32. Published 2004-11-30. https://combinatorialpress.com/jcmcc-articles/volume-051/abelian-group-labels-on-hamiltonian-cycles/ . Full text: https://combinatorialpress.com/article/jcmcc/Volume%20051/vol-051-paper%201.pdf .
- G. S. Staples, *Graph-induced operators: Hamiltonian cycle enumeration via fermion-zeon convolution*, arXiv:1408.1036 (initial 2014-08-05; accessible v2 2015-01-18). https://arxiv.org/pdf/1408.1036 .
- X. Yan, *Hamiltonian Cycles in Signed and Multisigned Complete Graphs*, arXiv:2502.10612 (2025-02-15). https://arxiv.org/pdf/2502.10612 .
- R. de Wolf, *A Brief Introduction to Fourier Analysis on the Boolean Cube*, Theory of Computing Graduate Surveys **1** (2008). https://theoryofcomputing.org/articles/gs001/gs001.pdf .
