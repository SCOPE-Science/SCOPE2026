# The complete characteristic-two cycle criterion for finite-field structure graphs

## Finding

Let \(m\ge1\) be an integer, set \(K=\mathbb F_{2^m}\), and consider the finite functional directed graph \(\Gamma(K)\) on \(K^2\), with its unique edge out of \((a,b)\) going to \(T(a,b)=(a+b,ab)\). Then \(\Gamma(K)\) has exactly \(2^m\) weakly connected components if and only if \(m\in\{1,2\}\). For every \(m\ge3\), it has strictly more than \(2^m\) components; equivalently, it has a nontrivial directed cycle. In fact:

1. If \(m\) has an odd divisor \(s>1\), the graph has a nontrivial directed cycle of even length arising from the linearized polynomial \(g(x)=x+x^2\) on \(\mathbb F_{2^s}\).
2. If \(4\mid m\), the graph contains the following explicit directed \(8\)-cycle over its subfield \(\mathbb F_{16}\):

\[
(14,11)\longrightarrow(5,8)\longrightarrow(13,14)\longrightarrow(3,10)\longrightarrow(9,13)\longrightarrow(4,15)\longrightarrow(11,9)\longrightarrow(2,12)\longrightarrow(14,11).
\]

Here the integers in this displayed cycle encode binary coefficients in the polynomial basis \(1,u,u^2,u^3\) of \(\mathbb F_2[u]/(u^4+u+1)\); for instance, \(14=u+u^2+u^3\), while \(11=1+u+u^3\). These two cases cover every \(m\ge3\).

## Assumptions and scope

The graph is a *functional* digraph: each ordered pair of field elements is a vertex and has one directed outgoing edge. Weak connectedness is connectedness after forgetting directions. No restriction to distinct coordinates or to units is made. The finite field is arbitrary of characteristic two, and the statement concerns existence of nontrivial cycles rather than a complete enumeration of their lengths or counts. All exponents and field operations are performed in \(K\).

## Proof

**Fixed points and components.** The equation \(T(a,b)=(a,b)\) implies \(b=0\), and conversely every \((a,0)\) is fixed. Thus there are exactly \(|K|=2^m\) fixed points. In any finite functional graph, each weak component contains exactly one directed cycle, so there are exactly \(2^m\) components if and only if there is no directed cycle of length larger than one.

**Two-step reduction valid in characteristic two.** For any commutative ring, direct multiplication yields
\[
T^2(-1,x)=(-1,x-x^2).
\]
In characteristic two, \(-1=1\), and hence
\[
T^2(1,x)=(1,g(x)),\qquad g(x)=x+x^2.
\]
Consequently, a nonzero periodic orbit of \(g\) of least period \(\ell>1\) produces a directed \(2\ell\)-cycle of \(T\). The intermediate states \(T(1,x)=(1+x,x)\) have first coordinate different from \(1\) whenever \(x\ne0\), so no shortening or collision occurs between the alternating states. The only fixed point of \(g\) in a field is \(0\), since \(g(x)=x\) implies \(x^2=0\).

**Degrees with an odd divisor.** Suppose \(s>1\) is odd and divides \(m\), and let \(L=\mathbb F_{2^s}\subset K\). Define the trace-zero subspace
\[
W=\{x\in L:\operatorname{Tr}_{L/\mathbb F_2}(x)=0\}.
\]
The field trace is nonzero because \(\operatorname{Tr}(1)=s\bmod2=1\), hence \(\dim_{\mathbb F_2}W=s-1\ge2\). The polynomial map \(g\) is \(\mathbb F_2\)-linear and maps \(W\) into itself, since \(\operatorname{Tr}(x^2)=\operatorname{Tr}(x)\). Its kernel on \(L\) is \(\{0,1\}\), but \(1\notin W\). Hence \(g|_W\) is injective, therefore bijective on the finite nonzero space \(W\). Every nonzero element of \(W\) lies on a \(g\)-cycle, whose length must exceed one because \(g\) has no nonzero fixed points. The two-step reduction gives a nontrivial \(T\)-cycle in \(K^2\).

**Degrees divisible by four.** Take \(L=\mathbb F_2[u]/(u^4+u+1)\), a field of order \(16\). The polynomial \(u^4+u+1\) has neither a root in \(\mathbb F_2\) nor a factor \(u^2+u+1\), the only monic irreducible quadratic over \(\mathbb F_2\); thus it is irreducible. Encode \(a_0+a_1u+a_2u^2+a_3u^3\) by \(\sum_{i=0}^3a_i2^i\). Binary XOR gives field addition, while multiplication is reduction modulo \(u^4+u+1\). Eight successive exact multiplications verify the displayed cycle; its eight vertices are distinct. If \(4\mid m\), the standard subfield criterion embeds \(L\) into \(K\), preserving the cycle.

**Exhaustion of degrees.** Every integer \(m\ge3\) is either divisible by four or has an odd divisor larger than one: if \(4\nmid m\), write \(m=2^r s\) with \(r\in\{0,1\}\) and \(s\) odd; \(m\ge3\) then forces \(s>1\).

**Exceptional fields.** In \(\mathbb F_4\), write \(\mathbb F_4^\times=\{1,\omega,\omega^2\}\), with \(\omega^2+\omega+1=0\). If \(ab=0\), then \(T(a,b)\) is fixed. If \(a=b\), then \(T(a,b)=(0,a^2)\) and \(T^2(a,b)=(a^2,0)\) is fixed. In the remaining case, \(a,b\) are distinct nonzero elements. For \(\{a,b\}=\{\omega,\omega^2\}\), \(T(a,b)=(1,1)\), which reaches \((1,0)\) in two further steps. For either of the two remaining unordered pairs \(\{1,\omega\}\) or \(\{1,\omega^2\}\), one has \(T^2(a,b)=(1,1)\), which reaches \((1,0)\) in two more steps. Therefore every trajectory over \(\mathbb F_4\) reaches a fixed point in at most four steps. The subfield \(\mathbb F_2\) inherits the same property. Neither field has a nontrivial cycle. Together the cases prove the theorem. \(\square\)

## Verification

The standalone script `verify_structure_graph.py` checks the eight-cycle in \(\mathbb F_{16}\), tests irreducibility of its listed binary field moduli, enumerates complete functional-graph cycles over \(\mathbb F_{2^m}\) for \(1\le m\le8\), and verifies sample \(g\)-cycle reductions for degrees \(3,5,6,7\). It returns `STRUCTURE_GRAPH_VERIFY_OK` on success. The infinite-degree conclusion follows from the subfield/trace proof, **not** from finite enumeration. Only the eight-cycle certificate and two tiny exceptional cases are finite calculations in the proof.

## Relationship to prior work

Chernev and Chernev (2026, Definition 3.1, Hypothesis 6.1, Section 6) formulate this same structure graph and establish the characteristic-two cases through finite calculations. Their Lemma 5.1 gives the two-step identity for \(g(x)=x-x^2\), and their paper already certifies a cycle over \(\mathbb F_{16}\). The novelty asserted here is the *all-extension-degree criterion* using the odd-degree trace-zero subspace, together with a concise fully explicit cycle for the degrees divisible by four. The result resolves the characteristic-two portion of their finite-field cycle-existence hypothesis; it **does not** resolve their remaining exceptional odd-prime case or the corresponding full finite-ring classification.

Lipkovski (2012, 2017) introduced and studied the graph, its fixed points, necessary cycle conditions, and finite examples. These contributions are prior work; neither cited treatment gives the universal characteristic-two extension-degree criterion.

## Limitations

The argument establishes only the existence or nonexistence of a nontrivial directed cycle, not the number of all cycles, possible exact lengths, or their basin sizes in general. In particular the general odd-divisor construction does not specify one uniform cycle length. The condition says nothing about nonfields of characteristic two or about odd-characteristic fields. Historical originality may depend on further hard-to-index publications; the finite examples and the two-step identity are explicitly not claimed as new.

## References

1. A. M. Chernev and N. A. Chernev, *On the Connected Components of Structure Graphs of Associative Rings*, arXiv:2611.07521v1, first public 2026-11-05. https://arxiv.org/abs/2611.07521
2. A. T. Lipkovski, *Digraphs associated with finite rings*, Publications de l'Institut Mathématique 92(106) (2012), 35–41. https://doi.org/10.2298/PIM1206035L
3. A. T. Lipkovski, *Structure Graphs of Rings: Definitions and First Results*, Journal of Mathematical Sciences 225 (2017), 658–665. https://doi.org/10.1007/s10958-017-3484-3
4. H. Daoub, O. Shafah and A. T. Lipkovski, *An Association between Digraphs and Rings*, Filomat 36 (2022), 715–720. https://doi.org/10.2298/FIL2203715D
