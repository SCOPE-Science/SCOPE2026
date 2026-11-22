# Prime-polynomial subgroups of every quadratic finite-field modulus: exact order profiles and a characteristic-parity transition

## Finding
Let \(q=p^r\) be any prime power, and let \(f(t)\in\mathbb F_q[t]\) be any monic polynomial of degree two. Use the **unique** reduced representative of degree less than two of each element of \(R_f=\mathbb F_q[t]/(f)\). A **prime-polynomial unit subgroup** is a subgroup \(H\le R_f^\times\) whose every element other than the identity has an irreducible reduced representative. The trivial subgroup is permitted.

**Theorem (complete order profile).** Such a subgroup is characterized by
\[
H\cap \mathbb F_q^\times=\{1\}.
\]
Precisely the following possibilities occur, and all listed subgroups qualify:

1. **Irreducible \(f\).** The ambient group is cyclic of order \(q^2-1\). For each positive divisor \(d\) of \(q+1\) coprime to \(q-1\), there is exactly one qualifying subgroup of order \(d\), with no others.
2. **Squarefree split \(f=(t-a)(t-b)\), \(a\ne b\).** For every \(d\mid(q-1)\), there are exactly \(d\) qualifying subgroups of order \(d\), all cyclic. Writing \(\mu_d\) for the unique subgroup of \(\mathbb F_q^\times\) of order \(d\), they are exactly the graphs \(\{(\phi(w),\phi(w)w):w\in\mu_d\}\) under evaluation at \(a,b\), with \(\phi:\mu_d\to\mathbb F_q^\times\) a homomorphism.
3. **Repeated-root \(f=(t-a)^2\).** For each \(0\le j\le r\), the qualifying subgroups of order \(p^j\) are exactly
\[
H_W=\{1+w(t-a):w\in W\},\qquad W\le_{\mathbb F_p}\mathbb F_q,\quad\dim_{\mathbb F_p}W=j.
\]
There are precisely the Gaussian-binomial number \({r\brack j}_p\) of them, all elementary abelian.

Consequently, counting pairs of a monic quadratic \(f\) and a qualifying subgroup \(H\) by their subgroup cardinality, the complete polynomial is
\[
\begin{aligned}
Z_q(z)&=\sum_{\deg f=2\atop f\text{ monic}}\ \sum_{H\text{ qualifying}}z^{|H|}\\
&=\frac{q(q-1)}2\sum_{\substack{d\mid(q+1)\\\gcd(d,q-1)=1}}z^d
 +\frac{q(q-1)}2\sum_{d\mid(q-1)}d\,z^d
 +q\sum_{j=0}^r{r\brack j}_p z^{p^j}.
\end{aligned}
\]
In particular, the largest attainable subgroup cardinality (as \(f\) varies) is
\[
\boxed{\max |H|=\begin{cases}q,&q\text{ odd},\\q+1,&q\text{ even}.\end{cases}}
\]
For odd \(q\), equality occurs for **exactly \(q\) pairs** \((f,H)\): one full principal-unit subgroup at each repeated-root quadratic. For even \(q\), equality occurs for **exactly \(q(q-1)/2\) pairs**: one order-\(q+1\) subgroup at each irreducible quadratic.

## Assumptions and scope
The field \(\mathbb F_q\) is arbitrary, including nonprime fields and characteristic two. The modulus is any monic quadratic, including reducible and non-squarefree polynomials. Irreducibility refers to nonconstant irreducible polynomials over \(\mathbb F_q\), **not** to irreducibility modulo \(f\). The canonical representative has degree strictly less than two and is not required to be monic. The identity is exempt from the irreducibility condition; constants other than one are not irreducible. The polynomial \(Z_q(z)\) counts *embedded subgroups*, not subgroup isomorphism classes, and counts different monic moduli separately.

## Proof
**1. Reduce the condition to scalar avoidance.** Every reduced nonzero representative has degree zero or one. Every degree-one polynomial over a field is irreducible, whereas every nonzero constant is a unit of degree zero and is not irreducible. A nonidentity element therefore violates the prime-polynomial condition if and only if it belongs to the embedded constant unit group \(\mathbb F_q^\times\). This proves \(H\cap\mathbb F_q^\times=\{1\}\).

**2. Irreducible modulus.** For irreducible \(f\), \(R_f\simeq\mathbb F_{q^2}\). Its multiplicative group is cyclic of order \((q-1)(q+1)\); \(\mathbb F_q^\times\) is its unique subgroup of order \(q-1\). The unique subgroup of order \(d\mid(q^2-1)\) intersects the constants in the unique subgroup of order \(\gcd(d,q-1)\). Thus it qualifies precisely when \(\gcd(d,q-1)=1\). This also forces \(d\mid(q+1)\): for each prime \(\ell\mid d\), it cannot divide \(q-1\), hence its full \(d\)-valuation is bounded by the valuation in \(q+1\). Conversely these two conditions suffice.

**3. Split squarefree modulus.** Evaluation gives \(R_f^\times\simeq\mathbb F_q^\times\times\mathbb F_q^\times\) and identifies the constants with the diagonal. The change of coordinates \((u,v)\mapsto (u,v/u)\) identifies the diagonal with \(\mathbb F_q^\times\times\{1\}\). Therefore projection of a qualifying \(H\) to the second factor has trivial kernel and identifies \(H\) with a subgroup \(K\le\mathbb F_q^\times\). Since \(\mathbb F_q^\times\) is cyclic, for every \(d\mid(q-1)\) its unique order-\(d\) subgroup is \(K=\mu_d\). Every complement to the first factor above \(K\) is the graph of a homomorphism \(\phi:K\to\mathbb F_q^\times\), yielding exactly \(\gcd(d,q-1)=d\) distinct graphs. Returning to evaluation coordinates gives the displayed formula. No other subgroup can qualify.

**4. Repeated root.** Let \(\varepsilon=t-a\pmod f\), so \(\varepsilon^2=0\). A unit is uniquely \(c(1+u\varepsilon)\) with \(c\in\mathbb F_q^\times\), \(u\in\mathbb F_q\); multiplication identifies \(R_f^\times\simeq\mathbb F_q^\times\times(\mathbb F_q,+)\). Scalar avoidance makes the projection of \(H\) to the additive factor injective. If its image is \(W\le(\mathbb F_q,+)\), then \(H\) is the graph of a homomorphism \(W\to\mathbb F_q^\times\). The additive factor is a \(p\)-group and the multiplicative factor has order \(q-1\), which is coprime to \(p\), so every such homomorphism is trivial. Hence \(H=1+W\varepsilon\). The additive subgroups are exactly \(\mathbb F_p\)-linear subspaces, with \({r\brack j}_p=\prod_{i=0}^{j-1}(p^{r-i}-1)/(p^{j-i}-1)\) of dimension \(j\), proving the third profile.

**5. Aggregate and extremal counts.** The numbers of monic irreducible, squarefree split, and repeated-root quadratics are, respectively, \(q(q-1)/2\), \(q(q-1)/2\), and \(q\), by counting unordered pairs of distinct roots, repeated roots, and the remaining monic quadratics. Multiplying the three order profiles by these counts proves \(Z_q(z)\). If \(q\) is even, \(\gcd(q+1,q-1)=1\), giving the unique order-\(q+1\) subgroup in every irreducible case; split and repeated cases have order at most \(q-1\) and \(q\). If \(q\) is odd, the admissible divisors of \(q+1\) must be odd, and are therefore at most \((q+1)/2<q\). Split orders are at most \(q-1\); the repeated-root full unipotent subgroup has order \(q\) and is unique at each repeated-root quadratic. All asserted strict maxima and equality multiplicities follow, including the edge case \(q=2\).

## Verification
A standalone standard-library checker `verify.py` independently constructs finite fields, enumerates all units of every inspected quadratic quotient, generates **all** of their subgroups by closure, filters out subgroups containing nonidentity scalars, and compares the full subgroup-order histogram against the theorem. It checked all monic quadratic moduli over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7\), and one modulus of each factorization type over \(\mathbb F_8\) and \(\mathbb F_9\): 109 quadratic cases. The checker verifies no conjectural infinite conclusion by enumeration; the proof above applies to every prime power.

Reproduce with `python3 verify.py` (standard library only); successful output ends in `PASS: 109 polynomial cases; every subgroup independently enumerated`.

## Relationship to prior work
Trey Li, *Groups of Prime Units*, arXiv:2611.01793v1 (first publicly posted 2026-11-01), Question 6.6, asks about polynomial-ring analogues over finite fields. It gives no all-quadratic subgroup classification. A published result entitled *Complete prime-polynomial unit groups over finite fields* proves a classification of **whole unit groups** with the prime-polynomial property, over \(\mathbb F_2\), but its limitations explicitly leave **proper prime-polynomial subgroups** unclassified. The present result counts precisely such embedded subgroups for every quadratic modulus and all finite fields, which is not implied by the earlier full-group classification. The special \(q=2\) whole-group cases and standard cyclic-group/CRT facts are not claimed as new. The claim is the exact all-quadratic, order-resolved subgroup profile and extremal characteristic transition, not a new general subgroup theorem.

## Limitations
No claim is made for moduli of degree three or greater, or for canonical representative conventions other than reduction to degree less than the modulus. The proof uses standard descriptions of finite-field unit groups and elementary finite-abelian subgroup theory. Although the indicated closest primary literature and indexed results were inspected for implication, an unindexed equivalent treatment of degree-two polynomial-unit subgroups remains possible. 
## References
1. Trey Li, *Groups of Prime Units*, arXiv:2611.01793v1 (first posted 2026-11-01), especially Question 6.6. https://arxiv.org/html/2611.01793v1
2. *Complete prime-polynomial unit groups over finite fields*, publicly indexed mathematical finding (2026-11-08), especially theorem and limitations. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-complete-prime-polynomial-unit-groups-over-finite-fields--6f138ca9083c/RESULT.md
3. Standard finite field facts: cyclicity of \(\mathbb F_q^\times\), Chinese remaindering for coprime polynomial factors, and Gaussian binomial counts of finite vector subspaces.
