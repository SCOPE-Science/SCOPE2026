# Cubic collapse of digit-frequency fluctuations in Fibonacci finite-type covers

## Finding
Let \(f=010010100100101\cdots\) be the fixed point of \(0\mapsto01,\ 1\mapsto0\). Let \(X\subseteq\{0,1\}^{\mathbb Z}\) be its two-sided factor subshift, and let \(X^{(m)}\) be the canonical finite-type cover allowing exactly the length-\(m\) factors of \(f\). Write \(F_0=0,F_1=1,F_{k+1}=F_k+F_{k-1}\). For every \(k\ge5\), put
\[
 p=F_{k-1},\quad q=F_k,\quad a=F_{k-3},\quad b=F_{k-2}.
\]
The finite-type cover \(X^{(q)}\) is topologically mixing. For the digit-one potential \(\psi(x)=x_0\), its exact pressure \(P_k(t)\), for every real \(t\), is the unique real solution of
\[
 e^{at-pP_k(t)}+e^{bt-qP_k(t)}=1.\tag{1}
\]
Let \(\mu_k\) be its unique maximal-entropy (Parry) measure, and define the asymptotic digit-count variance
\[
 \sigma_k^2=\lim_{N\to\infty}\frac1N\operatorname{Var}_{\mu_k}\left(\sum_{j=0}^{N-1}x_j\right).
\]
If \(h_k=P_k(0)\), \(u_k=e^{-ph_k}\), and \(v_k=e^{-qh_k}\), then \(u_k+v_k=1\) and
\[
 \boxed{\sigma_k^2=\frac{u_kv_k}{(pu_k+qv_k)^3}>0.}\tag{2}
\]
Set \(\varphi=(1+\sqrt5)/2\), \(r=\varphi^{-1}\), and let \(c>0\) solve \(e^{-rc}+e^{-c}=1\). Writing \(U=e^{-rc}\), \(V=e^{-c}\), define
\[
 C=\frac{UV}{(rU+V)^3}=0.5174960277197655\ldots .
\]
Then the sharp cubic fluctuation law is
\[
 \boxed{\lim_{k\to\infty}F_k^3\sigma_k^2=C.}\tag{3}
\]
In fact, because \(X^{(m)}\) is constant for every integer \(F_k\le m<F_{k+1}\), the complete set of subsequential limits of \(m^3\sigma^2(X^{(m)})\) as \(m\to\infty\) is
\[
 \boxed{[C,\varphi^3C]=[0.5174960277\ldots,2.1921483515\ldots].}\tag{4}
\]
Here \(\sigma^2(X^{(m)})\) is the same per-time digit-count variance computed under that cover's unique maximal-entropy measure. For each fixed cover, standard finite-state central-limit theory gives a nondegenerate Gaussian central limit theorem with the variance in (2). The limits in (3)–(4) vary the cover *after* taking the long-time variance limit.

## Assumptions and scope
All shifts are two-sided, over the binary alphabet. Pressure uses natural logarithms and sums of the observable \(x_0\) (not entropy of the limiting zero-entropy system). The cover index \(m\) means the length of permitted words, not the number of graph vertices. The theorem concerns the equilibrium measure at *zero field* and the second derivative of the *field-dependent* pressure; it makes no uniform-in-\(k\) central-limit assertion. The first admissible index \(k=5\) gives cover length \(5\), return-loop data \((p,a)=(3,1)\) and \((q,b)=(5,2)\).

## Proof
**1. Exact finite-type presentation.** The length-\(m\) Rauzy graph has vertices the length-\((m-1)\) factors and one directed edge for each length-\(m\) factor, labeled by the last digit. The corresponding edge shift presents \(X^{(m)}\). Fibonacci Sturmian languages are recurrent and have exactly one right-special and one left-special factor at each length. In particular, there is exactly one branching vertex in the Rauzy graph; every other vertex has one outgoing edge. Strong connectivity implies that every directed simple cycle passes through the branching vertex: any cycle avoiding it would be a closed outgoing component.

The Fibonacci bispecial indices and the two first-return loops of lengths \(F_{k-1}\) and \(F_k\) at order \(F_k-2\) are established in Bruin–Leplaideur, Section 2.1–2.2 and Proposition 2.2, with the continued-fraction graph discussion. Taking its directed line graph gives the graph at order \(F_k-1\), without changing the return-loop lengths or label sums: an edge becomes a vertex and a return path retains exactly the cyclic word of edge labels. Thus at cover length \(F_k\) there are exactly two simple cycles of lengths \(p,q\) and no vertex-disjoint simple cycles.

The labels of the two loops are cyclic conjugates of the two successive finite Fibonacci words of lengths \(F_{k-1}\) and \(F_k\). This follows from the substitution return-word decomposition at the special factor; equivalently one may read the two return words from the Fibonacci substitution towers in Bruin–Leplaideur, Lemma 2.3 and its surrounding graph construction. Their numbers of ones are \(a=F_{k-3}\) and \(b=F_{k-2}\), respectively: under \(0\mapsto01,\ 1\mapsto0\), word lengths and one-counts obey the same Fibonacci recursion with initial pairs \((1,0)\), \((2,1)\). These structural facts are existing Fibonacci combinatorics, not a claimed discovery. The graph is strongly connected, and its loop lengths \(p,q\) are coprime, so it is primitive, hence the cover is mixing with a unique Parry measure.

**2. Marked renewal equation.** Weight each edge labeled one by \(e^t\) and each edge labeled zero by one. Because every simple cycle passes through the same branching vertex, the directed cycle expansion of the weighted adjacency determinant has only the two nonempty terms
\[
 \det(I-zA_t)=1-z^pe^{at}-z^qe^{bt}.\tag{5}
\]
In particular its positive Perron eigenvalue \(e^{P_k(t)}\) is determined by (1), and uniqueness follows from strict monotonicity of the left side in \(P_k(t)\). This holds for all real \(t\), rather than merely a Taylor approximation.

**3. Exact fluctuation coefficient.** Implicit differentiation at \(t=0\) gives
\[
 P'_k(0)=\frac{au_k+bv_k}{pu_k+qv_k},\qquad
 P''_k(0)=\frac{u_k(a-pP'_k(0))^2+v_k(b-qP'_k(0))^2}{pu_k+qv_k}.
\]
Write \(D=pu_k+qv_k\). Since \(u_k+v_k=1\), the numerator in the second formula reduces to \(u_kv_k(aq-bp)^2/D^2\). Cassini's Fibonacci identity yields \(|aq-bp|=|F_{k-3}F_k-F_{k-2}F_{k-1}|=1\), proving (2). For a primitive finite graph and a locally constant potential, \(P''_k(0)\) equals the limiting variance per time under the Parry measure (it is also the renewal-reward variance for the two return loops). Its strict positivity proves the fixed-cover central limit theorem is nondegenerate.

**4. Cubic scale and full phase interval.** The entropy equation at zero field reads \(u_k+v_k=1\). With \(r_k=p/q\to r\) and \(c_k=qh_k\), it becomes \(e^{-r_kc_k}+e^{-c_k}=1\). Continuity and strict monotonicity imply \(c_k\to c\), \(u_k\to U\), and \(v_k\to V\). Multiplying (2) by \(q^3\) proves (3).

The minimal forbidden factors of the Fibonacci word have exactly one new length at every \(F_k\) and none between consecutive Fibonacci lengths (Amaral, Section 2, citing classical bispecial combinatorics). Therefore the allowed-word SFT does not change for \(F_k\le m<F_{k+1}\). Hence its digit-variance is also constant throughout that interval. Since \(m/F_k\) fills in the entire asymptotic interval \([1,\varphi]\), and \(F_k^3\sigma_k^2\to C\), the full accumulation interval is precisely (4). This establishes every intermediate limit, not only its endpoints.

## Verification
The standalone standard-library checker `verify_fibonacci_variance.py` was executed against the embedded source. It constructs finite Fibonacci prefixes and all distinct length-\(F_k\) factors for \(5\le k\le12\); computes all first-return cycles through the unique branching vertex and their digit counts; independently verifies Cassini's determinant and the two formulations of renewal variance; and checks the pressure's second derivative by symmetric finite differences at three small graph sizes. Eight finite cycle enumerations, three second-derivative comparisons, and the limiting constant passed. The program checks finite instances and is **not** an infinite proof; the all-index Rauzy structure and plateau facts are justified by the cited mathematical results and the analytic argument above. Reproduce with `python3 verify_fibonacci_variance.py`.

## Relationship to prior work
Coles–Cyr–Kra–Pavlov introduced entropy/period stability questions for canonical SFT covers, but not digit-count fluctuation constants for Fibonacci covers. Amaral studied the Fibonacci forbidden-factor hierarchy and its topological entropy staircase, including low-index eigenvalues; his work does not supply a marked pressure or a digit-variance hierarchy. Bruin–Leplaideur proved the Fibonacci bispecial Rauzy graph structure and substitution count identities used in Step 1. The published result *A Fibonacci entropy staircase and its full scaled accumulation interval* gives the **unmarked** two-loop entropy equation and exact cover plateaus; that covers the zero-field specialization \(t=0\) of (1), but states neither the field-dependent equation nor the second derivative (2), its cubic decay (3), or the full scaled variance interval (4). General finite-state pressure/CLT theory explains the variance derivative but does not determine this graph-specific sharp exponent and constant without the marked return analysis. The contribution here is exactly that quantitative fluctuation classification, not a claim of new Fibonacci graph or entropy facts.

## Limitations
This theorem concerns the canonical Fibonacci finite-type covers, not arbitrary Sturmian slopes or the limiting minimal Fibonacci subshift's Birkhoff central-limit behavior. The limit order matters: the observation time first tends to infinity with the cover fixed. The two-loop graph and return words are classical; novelty and mathematical value lie in the explicit **marked** pressure and the cubic variance and accumulation laws. Unindexed historical thermodynamic computations of Fibonacci Markov approximants remain a priority risk; independent external validation has not been performed.

## References
[1] Marcelo Maciel Amaral, *A Hierarchy of Fibonacci Forbidden-Word Hamiltonians: From the Golden Chain to the Plastic Chain and Aperiodic Order*, arXiv:2511.10672v1, first publicly submitted 2025-11-09, https://arxiv.org/pdf/2511.10672; Sections 2–4.

[2] Solly Coles, Van Cyr, Bryna Kra, Ronnie Pavlov, *Stable Covers of Subshifts*, arXiv:2602.04097v1, first publicly submitted 2026-02-04, https://cs.du.edu/~rpavlov/SCVCBKRPstable.pdf; Sections 1–2.

[3] Henk Bruin, Renaud Leplaideur, *Renormalization, Freezing Phase Transitions and Fibonacci Quasicrystals*, arXiv:1309.7934v1, 2013, https://arxiv.org/pdf/1309.7934; Section 2, Proposition 2.2, Lemma 2.3.

[4] *A Fibonacci entropy staircase and its full scaled accumulation interval*, published-finding corpus mathematical research record (2026-10-11), identifier be7c0c99809f. The underlying graph identities are credited to [3].
