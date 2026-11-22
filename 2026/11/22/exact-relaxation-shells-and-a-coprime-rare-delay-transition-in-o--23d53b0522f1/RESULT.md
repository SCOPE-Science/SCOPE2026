# Exact relaxation shells and a coprime rare-delay transition in one-bridge conjunctive cycles

## Finding
Consider two directed cycles of lengths \(a,b\ge2\), with synchronous Boolean AND updates and one directed bridge from the first to the second. Let \(\tau\) be the first time a state enters a periodic orbit and let \(L=\operatorname{lcm}(a,b)\), \(g=\gcd(a,b)\), and \(\alpha=a/g\). The full joint **first-entry-time** distribution admits an explicit product of \(g\) finite sums, and the final \(b\) cumulative shells have a closed arithmetic product. In particular, among the \(2^{a+b}\) initial states,
\[
\boxed{\#\{\tau=L\}=2^{a+b-\alpha-1},\qquad \Pr_{\mathrm{uniform}}(\tau=L)=2^{-\alpha-1}.}
\]
The maximal convergence time is therefore exactly \(L\) for every pair of lengths. Equal lengths have a quarter of initial states attaining the final step, whereas consecutive lengths have exponentially rare maximal delay:
\[
\Pr(\tau=n)=\tfrac14\quad(a=b=n),\qquad
\Pr(\tau=n(n+1))=2^{-n-1}\quad(a=n,b=n+1).
\]
Thus the length of the worst transient and the frequency of its occurrence have dramatically different arithmetic behavior.

Write \(\mathcal A_u=\{k\in\{0,\dots,a-1\}:k\equiv u\pmod g\}\) and \(\mathcal B_u=\{j\in\{0,\dots,b-1\}:j+1\equiv u\pmod g\}\), for \(0\le u<g\). For \(j\in\mathcal B_u\) and \(t\ge0\), define
\[
 U_{j,t}=\{-s\pmod a:0\le s<t,\quad s\equiv b-1-j\pmod b\}.
\]
For a binary word \(w\in\{0,1\}^{\mathcal A_u}\), define \(R_u(w,t)\) as the number of \(j\in\mathcal B_u\) for which either every letter of \(w\) is one or some letter of \(w\) indexed by \(U_{j,t}\) is zero. Then the **exact cumulative distribution at every time** is
\[
\boxed{C_t:=\#\{\tau\le t\}=\prod_{u=0}^{g-1}\sum_{w\in\{0,1\}^{\mathcal A_u}}2^{R_u(w,t)}.}
\]
The individual shell sizes are \(N_0=C_0\) and \(N_t=C_t-C_{t-1}\) for \(t\ge1\). In particular, \(C_0=(2^\alpha-1+2^{b/g})^g\) and \(C_L=2^{a+b}\).

There is a simpler formula for all final \(b\) cumulative shells. For \(0\le r\le b\), let
\[
 c_{r,k}=\#\{0\le j<r:j+1\equiv k\pmod a\}.
\]
Then
\[
\boxed{C_{L-r}=2^b\prod_{u=0}^{g-1}
\left(2^\alpha-\alpha+\sum_{k\in\mathcal A_u}2^{-c_{r,k}}\right).}
\]
The product is an integer although fractional factors appear. This determines the late transient shells exactly for all pairs of cycle lengths, including non-coprime lengths.

## Assumptions and scope
The source bits are \(A_0,\dots,A_{a-1}\), the downstream bits are \(B_0,\dots,B_{b-1}\), and the simultaneous update is
\[
 A_i'=A_{i-1\bmod a},\quad
 B_0'=B_{b-1}\wedge A_0,\quad
 B_j'=B_{j-1}\ (1\le j<b).
\]
There is exactly one bridge, from \(A_0\) to \(B_0\), with no reverse connection or extra self-loops. The count refers to all labelled binary initial states. A state is *periodic* if some positive iterate returns to the same state; \(\tau\) is the smallest nonnegative iterate at which periodicity begins. The source cycle alone is reversible; downstream bits may be irreversibly erased. The theorem concerns transient-entry distributions, not just periodic-state populations.

## Proof
For a fixed initial source word \(A\), its bit at gate \(A_0\) at time \(s\) is \(A_{-s\bmod a}\). Initially downstream bit \(B_j\) moves around the downstream cycle without collision and meets the AND gate for the first time at \(s=b-1-j\), and thereafter every \(b\) steps. At such a crossing it is erased precisely if the source gate bit at that time is zero. Thus the first killing time of an initially active bit is
\[
 \delta_j(A)=1+\min\{s\ge0:s\equiv b-1-j\pmod b,\ A_{-s\bmod a}=0\},
\]
interpreted as infinity if the set is empty. During the first \(L\) steps the crossing times visit exactly the \(\alpha=a/g\) source positions in the residue class \(\mathcal A_{j+1\bmod g}\), once each. A downstream bit survives forever exactly if its entire source residue class is one. All other active downstream bits are erased by time \(L\).

The source word simply rotates, and the surviving downstream bits are also rotated. Because erasures of other bits never create ones, a state is periodic precisely when no active downstream bit has a future killing time. Before its last destined erasure the state cannot be periodic: periodicity would preserve the total number of downstream ones, which is strictly decreasing at the destined erasure. Therefore
\[
 \tau(A,B)=\max\{\delta_j(A):B_j=1,\ \delta_j(A)<\infty\},
\]
where the empty maximum is zero. This proves \(0\le\tau\le L\) without assuming that finite computational tests generalize.

For fixed \(A\), to have \(\tau\le t\), initial downstream bit \(B_j\) is free if it survives forever (all source positions in its residue class one), or if it would be erased by time \(t\) (at least one zero in \(U_{j,t}\)). Otherwise \(B_j\) must initially equal zero. Hence there are \(2^{\sum_u R_u(A|_{\mathcal A_u},t)}\) compatible downstream words. The condition depends separately on each residue class modulo \(g\); summing over all source words factorizes into the displayed formula for \(C_t\). At \(t=0\), source classes other than the all-one word force their respective downstream bits all zero, while an all-one class allows all \(b/g\) bits free. This yields \(C_0=(2^\alpha-1+2^{b/g})^g\). At \(t=L\), every initially active downstream bit either survives or has already been erased, proving \(C_L=2^{a+b}\).

For the last \(b\) steps, consider an initially active downstream bit that is destined to be erased. Its **last possible gate crossing** in the first \(L\) updates is at time \(s=L-1-j\), with source index \(-s\equiv j+1\pmod a\). For \(0\le r\le b\), a bit can be erased after time \(L-r\) only when \(j<r\) and when its source residue class has exactly **one zero**, at \(k\equiv j+1\pmod a\). Indeed a class with at least two zeros would have killed the bit at an earlier encounter, while an all-one class never kills it. If a residue class contains one zero at \(k\), there are exactly \(c_{r,k}\) corresponding downstream initial bits that must be absent in order that \(\tau\le L-r\). Thus the weighted sum over words within that class is \(2^{b/g}(2^\alpha-\alpha+\sum_{k\in\mathcal A_u}2^{-c_{r,k}})\); multiplying classes proves the second boxed formula.

Taking \(r=1\), exactly one source position \(k=1\pmod a\) incurs a half-weight instead of full weight. Thus \(C_L-C_{L-1}=2^{a+b-\alpha-1}\), strictly positive. This proves both sharpness and the terminal probability. The equal-size and consecutive-size consequences follow on substituting \(\alpha=1\) and \(\alpha=a\), respectively.

## Verification
`verification/check_shells.py` constructs the original synchronous map without using the product formula and exhaustively walks every initial state to find its actual first periodic entry time. Independently it evaluates the first-killing-time expression, the all-time product census, the full last-\(b\)-shell product and the terminal closed form for every pair \((a,b)\) with \(2\le a,b\le6\). It reports `BRUTE_SHELLS_OK 25`. The general proof is the explicit particle transport argument above; the finite tests detect indexing and arithmetic mistakes but do not replace the unrestricted proof. No external proof assistant or independent verification is claimed.

## Relationship to prior work
Colón-Reyes, Laubenbacher and Pareigis's early Boolean monomial dynamics work supplies a foundational graph/period framework. Jarrah, Laubenbacher and Veliz-Cuba's 2008 study examines connected conjunctive networks, including a two-cycle example and a \((4,6)\) periodic-orbit census; its periodic-point results and general transient bounds are not claimed as new here. Chen, Gao and Başar's explicit one-bridge *elementary digraph* formula (Lemma 8 in the later revision) already implies the eventual projection by time \(L\), so this upper bound and the eventual state description are expressly prior work. A related published two-bridge calculation counts recurrent states and basins by a gcd-sensitive transfer; it does not give these first-periodic-entry shells. The contribution here is the **complete time-resolved product distribution**, its simplified last-\(b\) tail, the universal sharpness and the arithmetic last-shell population. Related generic finite-state and Boolean-monomial methods make these formulas in principle computable, but the retrieved primary statements do not imply these exact shell formulas as stated without the new killing-time classification.

## Limitations
The two cycles must be connected by exactly one directed bridge and obey synchronous conjunctive updates; the formulas do not classify arbitrary strongly connected components, multi-bridge systems or arbitrary Boolean functions. The product for general \(t\) is a finite exact sum, not necessarily an elementary closed form. The terminal formula is a special simplification because only the final \(b\) opportunities are at issue. Originality is assessed against the accessible literature and search index, not independently certified; an unindexed explicit first-entry formula could change historical priority. No independent external audit has been performed.

## References
- J. Colón-Reyes, R. Laubenbacher, B. Pareigis, *Boolean Monomial Dynamical Systems*, first arXiv posting 2004-03-10, https://arxiv.org/abs/math/0403166.
- A. S. Jarrah, R. Laubenbacher, A. Veliz-Cuba, *The Dynamics of Conjunctive and Disjunctive Boolean Networks*, first arXiv posting 2008-05-02, https://arxiv.org/abs/0805.0275.
- X. Chen, J. Gao, T. Başar, *Asymptotic Behavior of Conjunctive Boolean Networks Over Weakly Connected Digraphs*, initially posted 2017-08-07, particularly Section IV-A and Lemma 8 in the later open revision, https://arxiv.org/abs/1708.01975.
