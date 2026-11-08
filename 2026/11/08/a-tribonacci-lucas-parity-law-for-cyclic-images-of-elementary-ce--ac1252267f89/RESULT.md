# A Tribonacci–Lucas parity law for cyclic images of elementary cellular automata

## Finding

For every integer \(n\ge1\), let \(a_n\) and \(b_n\) be the numbers of **distinct indexed cyclic binary outputs** after one simultaneous step of elementary cellular automata Rule 172 and Rule 184, respectively. The local functions are
\[
f_{172}(a,b,c)=\begin{cases}b&a=0,\\c&a=1,\end{cases}
\qquad
f_{184}(a,b,c)=\begin{cases}a&b=0,\\c&b=1.\end{cases}
\]
Define the Tribonacci–Lucas integers by \(L_0=3\), \(L_1=1\), \(L_2=3\) and \(L_{j+3}=L_{j+2}+L_{j+1}+L_j\) for all \(j\ge0\). Then **for every** \(n\ge1\),
\[
\boxed{a_n=L_n-(-1)^n,\qquad b_n=L_n+1.}
\]
In particular \(b_n-a_n=1+(-1)^n\): the two image cardinalities are equal for odd ring size, while Rule 172 has exactly two fewer reachable outputs for even ring size. The sets of outputs need not be the same; at length five, `11000` is produced by Rule 172 but not by Rule 184.

Equivalent ordinary generating functions are
\[
\sum_{n\ge1}a_nz^n=\frac{2z+2z^2+4z^3+2z^4}{1-2z^2-2z^3-z^4},\qquad
\sum_{n\ge1}b_nz^n=\frac{2z-4z^4}{1-2z+z^4}.
\]
The first twelve values of \(a_n\) are \(2,2,8,10,22,38,72,130,242,442,816,1498\). Let \(\lambda\) denote the unique real root greater than one of \(t^3-t^2-t-1\), numerically \(\lambda=1.839286755\ldots\). Then \(a_n=\lambda^n+O(1)\), and the one-step image information rate tends to \(\log_2\lambda=0.879146421\ldots\) bits per site.

## Assumptions and scope

A ring is an indexed vector \(x=(x_0,\ldots,x_{n-1})\in\{0,1\}^n\), with all subscripts taken modulo \(n\), including when \(n=1\) or \(n=2\). Every site updates simultaneously, and each distinct output vector is counted once, regardless of its number of predecessors. No quotient by cyclic rotation is taken. Only one update is counted.

## Proof

**1. Exact cyclic-image recognizer.** Let the four vertices be the ordered pairs \(00,01,10,11\). For each rule \(r\in\{172,184\}\) and output letter \(e\in\{0,1\}\), define a four-by-four Boolean relation \(B_{r,e}\): its entry from \(ab\) to \(bc\) is one exactly when \(f_r(a,b,c)=e\), and all other entries are zero. Regard each Boolean matrix as a sixteen-bit integer, enumerating its entries row-by-row. Boolean matrix multiplication uses OR for addition and AND for multiplication.

For any output \(y=y_0\cdots y_{n-1}\), a cyclic predecessor exists if and only if \(B_{r,y_0}\cdots B_{r,y_{n-1}}\) has a nonzero diagonal. Indeed, a closed labeled path spells exactly the overlapping cyclic triples of one indexed predecessor, and conversely every such predecessor supplies a closed labeled path. The statement remains valid for rings of sizes one and two, since a closed walk enforces repeated positions.

**2. Finite deterministic counting system.** Begin at the identity Boolean relation \(I\), and close the set of reachable Boolean relations under right multiplication by both \(B_{r,0}\) and \(B_{r,1}\). Each relation is a deterministic state; the two labeled transitions are counted separately even if they lead to the same state. Mark a relation accepting when it has a nonzero diagonal. With state order given by breadth-first insertion of the zero transition before the one transition, the exact numbers of reachable relation states are \(83\) for Rule 172 and \(34\) for Rule 184. Let \(T_r\) be the nonnegative integral transition matrix on these states, \(u_r\) the row vector with a one at the identity, and \(v_r\) the column indicator of accepting states. The cyclic-image count is precisely
\[
a_n=u_{172}T_{172}^{n}v_{172},\qquad b_n=u_{184}T_{184}^{n}v_{184}.
\]
The executable file `verify_relation.py` reconstructs **every state and transition** directly from the eight local triples; none are entered as unverified fixed tables.

**3. Exact finite certificates and infinite extension.** Write
\[
q_{172}(t)=t^4-2t^2-2t-1,\qquad q_{184}(t)=t^4-2t^3+1.
\]
Exact integer arithmetic from the stated constructions gives
\[
u_{172}T_{172}^{j}q_{172}(T_{172})v_{172}=0\quad(1\le j\le83),\]
and
\[
u_{184}T_{184}^{j}q_{184}(T_{184})v_{184}=0\quad(1\le j\le34).
\]
All \(117\) scalar equalities are regenerated and asserted by `verify_relation.py`. By Cayley–Hamilton, for an \(s\)-state matrix the row vectors \(uT^{s+1},uT^{s+2},\ldots\) lie in the span of \(uT,uT^2,\ldots,uT^s\). Consequently the displayed equalities hold for **all** \(j\ge1\), not only those checked. They imply the all-length recurrences
\[
a_{n+4}=2a_{n+2}+2a_{n+1}+a_n,\qquad
b_{n+4}=2b_{n+3}-b_n\quad(n\ge1).
\]
Direct evaluation of the same finite matrices yields \((a_1,a_2,a_3,a_4)=(2,2,8,10)\) and \((b_1,b_2,b_3,b_4)=(2,4,8,12)\). Their generating functions are therefore the two rational expressions in the Finding section. Elementary polynomial reduction gives
\[
\sum_{n\ge1}b_nz^n-\sum_{n\ge1}a_nz^n=\frac{2z^2}{1-z^2}.
\]
Finally, if \(L_n\) is the sum of the \(n\)th powers of the three roots of \(t^3-t^2-t-1\), it obeys the stated Tribonacci–Lucas initial conditions and recurrence, and
\[
\sum_{n\ge1}L_nz^n=\frac{z+2z^2+3z^3}{1-z-z^2-z^3}.
\]
Adding \(z/(1+z)\) gives the generating function for \(a_n\), while adding \(z/(1-z)\) gives the one for \(b_n\). This establishes the boxed formula. The dominant root \(\lambda\) is strictly larger in modulus than the other roots, which have modulus below one. The asymptotic claim follows.

## Verification

Execute `python3 verify_relation.py` to regenerate the Boolean relations, the \(83\)- and \(34\)-state graphs, all exact recurrence checks, and the initial image counts. Execute `python3 direct_check.py` for an independent exhaustive image-set enumeration for **all** binary indexed cyclic inputs at every length from one through sixteen, for both rules. Both checks use the Python standard library and were executed successfully. The exact finite certificate supports the infinite proof through Cayley–Hamilton; the direct enumeration is an independent finite cross-check, not an infinite proof.

## Relationship to prior work

Fukś's 2009/2010 work on Rule 172 gives a selective-copier formulation and exact preimage-tree counts for short blocks and Bernoulli probabilities, rather than counts of **distinct full cyclic outputs for every ring length**. His subsequent full treatment of Rule 172 develops a closed-form Cauchy solution and its temporal dynamics, not the present parity relation between two rules. General discussions of Garden-of-Eden configurations and finite-ring orphan tables address related reachability, but finite entries alone do not establish this identity for arbitrary length. A previously established Rule-184 output count was included in the comparison; independently deriving both recurrences above avoids assuming it as a proof of the Rule-172 result. The new assertion is the Rule-172 all-length count and its exact cross-rule parity law, not a new result about the existence of finite automaton image recognizers.

## Limitations

The theorem treats exactly one simultaneous update on indexed binary cyclic rings, not multistep images, basins, preimage multiplicities, or rotation classes. The parity equality is of **cardinalities**, not a conjugacy or equality of the two output languages. Historical completeness of the literature search is not proved; results on complete Garden-of-Eden structures and unindexed finite-ring enumeration remain possible priority risks. No independent external mathematical audit is asserted.

## References

- H. Fukś, *Probabilistic initial value problem for cellular automaton rule 172*, DMTCS proceedings (online publication page dated 2009-12-31; open preprint arXiv:1007.1026, 2010), https://arxiv.org/abs/1007.1026 ; https://doi.org/10.46298/dmtcs.2761.
- H. Fukś, *Explicit solution of the Cauchy problem for cellular automaton rule 172*, Journal of Cellular Automata 12 (2017), 423–444; accessible preprint arXiv:2002.09362, https://arxiv.org/abs/2002.09362.
- *Gardens of Eden*, Elementary CA Zoo, https://cellular.solves.ca/gardens-of-eden (finite-ring census and recognition method).
- E. J. Powley and S. Stepney, *Counting preimages of homogeneous configurations in 1-dimensional cellular automata*, Journal of Cellular Automata 5 (2010), 353–381 (related inverse-fiber problem).
