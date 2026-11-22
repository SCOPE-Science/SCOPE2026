# Logarithmic inverse-branch frequency drift for Fibonacci-driven Rule 150

## Finding
Let \(\tau(0)=01\) and \(\tau(1)=0\), and let \(y\) be the one-sided Fibonacci fixed point beginning with \(0\). For each initial pair \(s\in\{00,01,10,11\}\), the one-sided sequence \(x^{(s)}\) is uniquely defined by \((x^{(s)}_0,x^{(s)}_1)=s\) and the three-input parity relation
\[
y_i=x^{(s)}_i\oplus x^{(s)}_{i+1}\oplus x^{(s)}_{i+2}\quad(i\ge0),
\]
where \(\oplus\) is addition modulo two. Put \(N_k=|\tau^{16k}(0)|=F_{16k+2}\), with \(F_0=0,F_1=1\), and let \(C_s(k)\) count \(0\le i<N_k\) for which \((x^{(s)}_i,x^{(s)}_{i+1})=(0,0)\). Define \(D_s(k)=4C_s(k)-N_k\).

**Exact theorem.** For all integers \(k\ge0\), in the order \(s=00,01,10,11\), the initial discrepancy vectors are
\[
(D_s(0))_s=(3,-1,-1,-1),\quad (D_s(1))_s=(0,-4,20,-16),\quad (D_s(2))_s=(9,5,17,-31).
\]
They obey the all-level laws
\[
(D_s(k+3)-D_s(k))_s=(0,0,24,-24).
\]
Consequently the four branches have frequency \(C_s(k)/N_k\to 1/4\), yet the biases have different orders: the first two remain bounded, while
\[
C_{10}(k)-\frac{N_k}{4}=\frac{\log N_k}{8\log\varphi}+O(1),\qquad
C_{11}(k)-\frac{N_k}{4}=-\frac{\log N_k}{8\log\varphi}+O(1),
\]
where \(\varphi=(1+\sqrt5)/2\). The constants and the mod-three oscillations are exact, not estimates from sample lengths.

## Assumptions and scope
These statements concern the specified Fibonacci fixed point, precisely the four specified initial pairs, and the canonical prefix lengths \(N_k\). The counted pair starts at \(i\) in the *preimage*, and the last counted pair uses coordinates \(x_{N_k},x_{N_k+1}\), which exist uniquely by the recurrence. A claim of bounded discrepancy at every arbitrary prefix length or for arbitrary base sequences is not made. This is a statement about one-step inverse branches of the binary linear cellular automaton Rule 150, not the temporal orbit of that automaton.

## Proof
Encode each predecessor pair \((a,b)\) as the state \(s=2a+b\) in \(\{0,1,2,3\}\). On reading the output symbol \(d\in\{0,1\}\), update
\[
P_d(2a+b)=2b+(a\oplus b\oplus d).
\]
The old state is exactly the pair \((x_i,x_{i+1})\) at the output position \(i\). Thus the number of old states equal to zero is precisely \(C_s(k)\).

Let \(W_a=\tau^{16}(a)\). Their lengths are \(|W_0|=2584\) and \(|W_1|=1597\). Direct composition of the four-state permutations gives the *two finite identities* \(P_{W_0}=P_0\) and \(P_{W_1}=P_1\), where \(P_w\) means read the letters of \(w\) left to right. (Both identities are reconstructed and checked by `verify_matrix.py`.) Define the substitution on eight decorated letters \((a,s)\) by replacing \((a,s)\) with the successive decorated letters \((W_a[j],s_j)\), where \(s_0=s\) and \(s_{j+1}=P_{W_a[j]}(s_j)\). Since the final state equals \(P_a(s)\), this substitution composes correctly under repeated application. By induction its \(k\)-fold iterate of \((0,s)\) records exactly all old states while processing \(\tau^{16k}(0)\).

In the ordered decorated alphabet
\[
(0,00),(0,01),(0,10),(0,11),(1,00),(1,01),(1,10),(1,11),
\]
let \(M\) be the integer incidence matrix of this substitution, with output-letter counts in rows and input-letter types in columns. Its eight columns are constructed directly from the above words and permutations in `verify_matrix.py` (no guessed floating-point coefficients). Set
\[
R=(3,-1,-1,-1,3,-1,-1,-1),\quad V=(0,0,24,-24,24,-24,0,0).
\]
Finite integer matrix multiplication verifies the critical identities
\[
R(M^3-I)=V,\qquad VM=V.
\]
Writing \(e_s\) for the coordinate column of the decorated letter \((0,s)\), the count identity is \(D_s(k)=RM^ke_s\). Therefore, for every \(k\ge0\),
\[
D_s(k+3)-D_s(k)=R(M^3-I)M^ke_s=VM^ke_s=Ve_s.
\]
Reading the first four entries of \(V\) gives the recurrence. Direct integer multiplication of \(R,RM,RM^2\) gives the three displayed initial vectors. Finally \(N_k=F_{16k+2}\sim \varphi^{16k+2}/\sqrt5\), and a recurrence increment of \(\pm24\) every three steps translates to a count increment of \(\pm6\) every three steps. This proves the logarithmic coefficient and bounded residual oscillations.

## Verification
Run `python3 verify_matrix.py` to reconstruct the two length-\(2584\)/\(1597\) block permutations, all eight integer matrix columns, all first-three discrepancy vectors, and the two exact matrix identities. Run `python3 verify_direct.py` as an independently coded check of the four inverse branches by scanning output prefixes of lengths \(1\), \(2584\), and \(5702887\), corresponding to substitution depths \(0\), \(16\), and \(32\). Both scripts use only Python's standard library. These finite checks provide a complete finite certificate for the unbounded claim through the proven decorated-substitution induction; the direct finite scan alone would not prove an all-level identity.

## Relationship to prior work
Kang and Jäger (2026, arXiv:2609.01140, first public September 1, 2026) develop inverse branches and permutation skew products for general permutative block codes, and prove strict ergodicity for Fibonacci lifts under their family \(h_{\kappa,\ell}(a_0,\ldots,a_{\ell-1})=a_{\ell-1}-a_0\). Their general theory motivates the finite-permutation construction, but their displayed family has two active endpoint inputs, whereas the present map has three active input bits. Their qualitative inverse-branch and ergodicity statements do not state the precise four-branch logarithmic bias or the period-three recurrence here. The known observation that minimal permutative finite lifts of linearly recurrent bases remain uniquely ergodic likewise does not determine these finite-scale coefficients.

Claussen's 2008 paper on Rule 150 and Fibonacci iterations concerns *time evolution* from a single occupied initial site, using a Fibonacci-type recursion for the aggregate temporal activity. Its observed space-time activity is not the pair-state frequency of a one-step inverse branch of a Fibonacci output sequence. The familiar Fibonacci substitution and finite-state skew-product methods are not claimed as new; the new quantitative assertion is the exact bias law and its sharp contrast among the four inverse branches.

## Limitations
The theorem does not assert uniform bounded discrepancy at arbitrary prefix lengths, mixing, independent validation, or a complete description of the invariant measures of the full two-sided inverse-image subshift. Priority cannot be considered independently established; other unindexed specialized results on substitution cocycles and exact digit statistics remain a possible overlap risk. The computations and proof have only received internal mathematical verification, not an independent audit.

## References
- Z. Kang and T. Jäger, *Permutative lifts of strictly ergodic subshifts*, arXiv:2609.01140v2 (2026), especially Proposition 1.1 and Theorems 1.3 and 1.6. First publicly submitted September 1, 2026. https://arxiv.org/html/2609.01140v2
- J. C. Claussen, *Time evolution of the rule 150 cellular automaton activity from a Fibonacci iteration*, Journal of Mathematical Physics 49, 062701 (2008), DOI:10.1063/1.2939398. Open-access author copy: https://publications.aston.ac.uk/id/eprint/37635/1/Time_evolution_of_the_rule.pdf
