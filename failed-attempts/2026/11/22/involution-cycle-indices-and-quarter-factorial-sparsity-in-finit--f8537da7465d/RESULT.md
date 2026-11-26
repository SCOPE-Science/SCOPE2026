# Involution cycle indices and quarter-factorial sparsity in finite crown partial-automorphism monoids

## Finding

Let \(N\ge4\) be even. On \(\mathbb Z/N\mathbb Z\), give each even vertex the order relations placing it below its adjacent odd vertices, and no other strict comparisons. Let \(\mathcal I_N\) be the inverse monoid of all isomorphisms between induced subposets, with the empty map. A self-inverse element \(f=f^{-1}\) has the same domain and image, and consists of \(a(f)\) fixed points and \(b(f)\) transposed pairs on that domain. Define
\[
J_N(U,V)=\sum_{\substack{f\in\mathcal I_N\\f=f^{-1}}}U^{a(f)}V^{b(f)}.
\]

**Theorem.** The following completely explicit finite coefficient formula determines \(J_N(U,V)\), including every domain rank and every involution cycle type. Let \(\mathcal T_N\) contain types \(s\) (one vertex), \(e_\ell\) for even \(2\le\ell<N\), and \(o_{\ell,p}\) for odd \(3\le\ell<N\) and \(p\in\{0,1\}\). For positive \(\ell\), set \(\tau(1,p)=s\), \(\tau(\ell,p)=e_\ell\) for even \(\ell\), and \(\tau(\ell,p)=o_{\ell,p}\) for odd \(\ell\ge3\). Write \(L_t\) for the size of type \(t\), and \(h_t=2\) for an odd type, \(h_t=1\) otherwise. Define
\[
B_t(U,V)=\begin{cases}
U^{L_t}+UV^{(L_t-1)/2},&h_t=2,\\
U^{L_t},&h_t=1,
\end{cases}
\]
and for every nonnegative integer \(c\),
\[
W_{t,c}(U,V)=\sum_{j=0}^{\lfloor c/2\rfloor}
\frac{c!\,h_t^j}{2^jj!(c-2j)!}V^{jL_t}B_t(U,V)^{c-2j}.
\]
Form the two-by-two matrix of formal power series \(T(z,\mathbf X)\), indexed by \(p,q\in\{0,1\}\),
\[
T_{pq}(z,\mathbf X)=\sum_{\ell,g\ge1}
\mathbf1_{\{q\equiv p+\ell+g\pmod2\}}
 z^{\ell+g}X_{\tau(\ell,p)},
\]
truncating all series after degree \(N\). For a finite exponent vector \(\mathbf c=(c_t)\), put
\[
A_N(\mathbf c)=[\mathbf X^{\mathbf c}]
\frac N2[z^N]\sum_{r=1}^{\lfloor N/2\rfloor}
\frac1r\operatorname{tr}\big(T(z,\mathbf X)^r\big).
\]
Then, with \(m=N/2\),
\[
\boxed{J_N(U,V)=1+U^N+mU^2V^{(N-2)/2}
+\mathbf1_{\{2\mid m\}}V^{N/2}
+\sum_{\mathbf c:A_N(\mathbf c)>0}
 A_N(\mathbf c)\prod_{t\in\mathcal T_N}W_{t,c_t}(U,V).}
\]
The rank polynomial is \(J_N(Z,Z^2)\). Its rank-zero, rank-one, rank-two, corank-one, and full-rank coefficients are, respectively,
\[
1,\qquad N,\qquad N(N-2),\qquad 2N,\qquad
m+1+\mathbf1_{\{2\mid m\}}.
\]
For \(N\ge6\), the corank-two coefficient is
\[
\boxed{[Z^{N-2}]J_N(Z,Z^2)=
\begin{cases}
N(5m-7)/2,&m\text{ odd},\\
N(5m/2-3),&m\text{ even}.
\end{cases}}
\]
At \(N=4\), that coefficient is \(8\).

**Sharp asymptotic.** If \(H_N=J_N(1,1)\) is the total number of self-inverse elements, then, along even \(N\to\infty\),
\[
\boxed{\log H_N=\tfrac14N\log N+O(N).}
\]
In particular, since \(\log|\mathcal I_N|=\frac12N\log N+O(N)\),
\[
\boxed{\log\frac{H_N}{|\mathcal I_N|}=-\tfrac14N\log N+O(N).}
\]
Thus self-inverse partial automorphisms are rare on a superexponential scale even though every induced antichain contributes a large involution family.

## Assumptions and scope

The crown has even size \(N\ge4\) and alternating height-two order. A partial automorphism is an induced-poset **isomorphism**, not merely an order-preserving injection. Self-inverse means equality with the inverse partial bijection (including all partial identities), not exact order two in the group of units. The formal sums have finite support after truncation at degree \(N\); no infinite formal computation is required. The cycle variables count moved vertices only in the domain: omitted vertices contribute neither a fixed point nor a transposition. The asymptotic is along even \(N\) only.

## Proof

**1. Domains and components.** A partial bijection equals its inverse precisely when its domain equals its image \(S\) and its restriction to \(S\) is an involutive automorphism of the induced poset. For a proper nonempty \(S\), its induced comparability graph consists of the clockwise runs of selected vertices separated by at least one omitted vertex. An isolated vertex is one poset type. An even-length alternating path has trivial automorphism group and its two starting parities yield isomorphic ordered paths via reversal *between* the two paths. An odd-length path of length at least three has two nonisomorphic height types (endpoints both minimal or both maximal), and each has precisely the identity and internal reversal as automorphisms. These are exactly the types \(t\) and group orders \(h_t\) above. Every automorphism of \(S\) permutes components within each type.

**2. Involution factors.** On \(c\) identical components of type \(t\), an involution must induce a matching with \(j\) exchanged component pairs and \(c-2j\) fixed components. There are \(c!/(2^j j!(c-2j)!)\) matchings, and for each exchanged pair \(h_t\) choices of isomorphism one way (the return map is forced), giving \(jL_t\) point transpositions. A fixed component permits its identity and, only in odd length at least three, its reflection with one fixed vertex and \((L_t-1)/2\) transpositions. These alternatives are encoded by \(B_t\). Therefore its contribution is exactly \(W_{t,c}\). Components of different types cannot mix and their factors multiply.

**3. Cyclic run count.** A proper nonempty subset with \(r\) runs has clockwise run lengths \(\ell_i\ge1\) and intervening gap lengths \(g_i\ge1\), satisfying \(\sum_i(\ell_i+g_i)=N\). Mark a run. There are \(N/2\) possible starting vertices of each parity, and the next start parity is shifted by \(\ell_i+g_i\) modulo two. Exactly these data are recorded in \([z^N]\operatorname{tr}(T^r)\), with the parity closed around the circle. Dividing by \(r\) removes the run mark. Consequently \(A_N(\mathbf c)\) is the **integer number** of labeled subsets whose induced components have multiplicity vector \(\mathbf c\). Combining this with step 2 gives the sum for all proper nonempty domains. There is one empty partial map. The full crown has a parity-preserving dihedral group of order \(N=2m\) (\(m\) rotations, \(m\) reflections); its involutions consist of the identity, \(m\) reflections each fixing two vertices, and, when \(m\) is even, the fixed-point-free half-turn. Their contributions are exactly the remaining displayed terms.

**4. Boundary coefficients.** There is one partial identity on each one-point domain. On a two-point domain, a comparable pair permits only the identity, whereas an incomparable pair permits both the identity and transposition. As there are \(N\) comparable pairs, the rank-two total is \(N+2(\binom N2-N)=N(N-2)\). Removing one vertex leaves an odd-length fence, with precisely two automorphisms (identity and reversal), so corank one has \(2N\) involutions. For corank two, delete a pair of vertices with smaller clockwise separation \(d\le m\). There are \(N\) such pairs for \(d<m\) and \(m\) for \(d=m\). At \(d=1\) the surviving even-length path has one automorphism; at \(d=2\) there is a singleton and a long odd path, giving two involutions (when \(N\ge6\)); for odd \(3\le d<m\) the two even-length paths give one; for even \(4\le d<m\) the two distinct odd-length paths allow four independent internal reversals. At \(d=m\), both paths have length \(m-1\) and may be exchanged: their involution count is two if \(m\) is odd, and six if \(m\ge4\) is even. Summing these separated cases yields the stated parity formula. Directly at \(N=4\), the rank-two count above is eight.

**5. Asymptotics.** Set \(m=N/2\), and let \(I_m\) be the number of involutions of the symmetric group \(S_m\). One parity class of the crown is an antichain of \(m\) vertices, so \(H_N\ge I_m\). An induced proper subset has at most \(m\) runs; with \(r\le m\) components, every involution chooses an involutive permutation of those components and, for each fixed component or paired component, at most two internal isomorphism choices. Therefore there are at most \(2^r I_r\le2^m I_m\) involutions per domain. Summing over the \(2^N\) possible domains (and including the full group) gives \(H_N\le2^{N+m}I_m+N\). The standard involution sum \(I_m=\sum_{j=0}^{\lfloor m/2\rfloor}m!/[2^jj!(m-2j)!]\) has logarithm \(\frac12m\log m+O(m)\): a term with \(j=\lfloor m/2\rfloor\) supplies the lower bound, while its exponential generating function \(\exp(z+z^2/2)\) at \(z=\sqrt m\) gives the upper bound. Hence \(\log H_N=\frac14N\log N+O(N)\). For the whole monoid, the \(m!\) permutations of an induced antichain provide a lower bound; every proper domain has at most \(m\) components and hence at most \(2^m m!\) poset isomorphisms to any given image, of which there are fewer than \(4^N\) domain-image pairs. Thus \(\log|\mathcal I_N|=\frac12N\log N+O(N)\), and subtracting establishes the proportion exponent.

## Verification

Run `python3 checker.py` with the Python standard library. The checker uses positive cyclic run-gap compositions and separately enumerates all proper nonempty binary subsets to compare the *entire* component-type coefficient dictionary for \(N=4,6,8,10,12\). It then constructs the involution polynomial and independently enumerates all involutive permutations of every selected domain, testing every ordered comparability, for \(N=4,6,8\). The exact rank totals are \(25,103,507,2629,14373\) at \(N=4,6,8,10,12\), respectively. It checks the low-, high-, and corank-two formulas. The finite checks are not a proof for unbounded \(N\); the preceding combinatorial argument supplies that proof. The limiting logarithmic coefficient follows from explicit factorial bounds, not numerical extrapolation.

## Relationship to prior work

Dimitrova and Koppitz's 2022 crown paper characterizes the same inverse monoid and proves its **minimum generating-set rank**; it does not enumerate self-inverse maps or their cycles. A 2026 public theorem, *Rank polynomial and half-factorial growth of finite crown partial-automorphism monoids*, already gives the cyclic run/gap coefficient \(A_N(\mathbf c)\) and the size of the full monoid. Both are explicitly used here, not reclaimed. A public *Cycle-type enumeration of self-inverse partial automorphisms of finite fences* already establishes the same wreath-involution factor for **linear fences**. The present claim is confined to **cyclic crowns**, including the full-dihedral-domain correction, the explicit corank-two parity law, and the sharp quarter-factorial asymptotic for self-inverse elements. These require a new crown-specific synthesis and proof; routine wreath-product enumeration itself is not claimed as new. The published involution polynomial for restrictions of global dihedral permutations concerns a strictly smaller inverse submonoid, since general crown partial automorphisms can permute separate nonadjacent path components independently.

## Limitations

The transfer formula uses existing component-classification machinery; it is not a new general wreath-product theory. The bounds determine a sharp logarithmic growth exponent, not a multiplicative asymptotic constant or local limit law. Exact computed cases cover \(N\le12\) for transfer coefficients and \(N\le8\) for direct involution maps, not all sizes. A combined or alternative presentation of the existing fence-involution and crown-rank results may make parts of this calculation routine; historical priority for the specific crown asymptotic and parity coefficient remains provisional. No independent mathematical audit has been performed.

## References

1. I. Dimitrova and J. Koppitz, *The rank of the inverse semigroup of all partial automorphisms on a finite crown*, arXiv:2204.13961, first posted 2022-04-29, https://arxiv.org/abs/2204.13961.
2. *Rank polynomial and half-factorial growth of finite crown partial-automorphism monoids*, publicly accessible mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-rank-polynomial-and-half-factorial-growth-of-finite-crown-partia--5cf963fdeacf.
3. *Cycle-type enumeration of self-inverse partial automorphisms of finite fences*, publicly accessible mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-cycle-type-enumeration-of-self-inverse-partial-automorphisms-of--2b5b0d3783a1.
4. *The domain-rank involution polynomial of the dihedral inverse monoid*, publicly accessible mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-domain-rank-involution-polynomial-of-the-dihedral-inverse-mo--8670f30aedd1.
