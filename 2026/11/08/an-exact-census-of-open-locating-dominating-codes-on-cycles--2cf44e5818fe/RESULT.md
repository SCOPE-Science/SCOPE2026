# An exact census of open locating-dominating codes on cycles

## Finding

For an integer \(n\ge3\), let \(C_n\) be the ordinary simple labelled cycle on \(\mathbb Z/n\mathbb Z\). An **open locating-dominating set** (OLD code) is a set \(S\subseteq V(C_n)\) for which every trace \(N(v)\cap S\) is nonempty and the \(n\) traces are pairwise different. Put
\[
P_n(z)=\sum_{S\text{ an OLD code of }C_n} z^{|S|}.
\]
Define, for \(m\ge3\), the explicit polynomial
\[
A_m(t)=1+\sum_{k=1}^{\lfloor m/3\rfloor}\frac{m}{k}\binom{m-2k-1}{k-1}t^k.
\]
Then the complete cardinality census is
\[
\boxed{P_n(z)=\begin{cases}
 z^n A_n(z^{-1}),&n\ge3\text{ odd},\\
 0,&n=4,\\
 z^n A_{n/2}(z^{-1})^2,&n\ge6\text{ even}.
\end{cases}}
\]
The expressions on the right are polynomials: multiplication by the displayed power of \(z\) cancels all negative exponents. Thus every individual coefficient is determined, with vertices labelled, not taken modulo rotations.

For every \(n\ge3\) other than \(n=4\), all cardinalities from the minimum to \(n\) occur. The exact minimum is
\[
\boxed{\gamma_{\mathrm{OLD}}(C_n)=\begin{cases}
 n-\lfloor n/3\rfloor,&n\text{ odd},\\
 n-2\lfloor n/6\rfloor,&n\text{ even},\ n\ge6.
\end{cases}}
\]
In particular, for \(n\ge5\), this is \(\lceil2n/3\rceil+1\) precisely when \(n\equiv4\pmod6\), and is \(\lceil2n/3\rceil\) otherwise. There is no OLD code for \(C_4\).

Put \(q=\lfloor n/3\rfloor\) for odd \(n\), or \(q=\lfloor n/6\rfloor\) for even \(n\). The number of minimum-cardinality OLD codes is \([t^q]A_n(t)\) for odd \(n\), and \(([t^q]A_{n/2}(t))^2\) for even \(n\). In particular, for odd \(n=3q,3q+1,3q+2\), respectively, these minimum counts are \(3\), \(n\), and \(n(q+1)/2\). These are counts of distinct labelled sets.

For example, \(P_7(z)=7z^5+7z^6+z^7\), \(P_{10}(z)=25z^8+10z^9+z^{10}\), and \(P_{13}(z)=13z^9+65z^{10}+52z^{11}+13z^{12}+z^{13}\). A nine-element OLD code of \(C_{13}\) is the complement of \(\{0,5,6,12\}\) in \(\mathbb Z/13\mathbb Z\). It directly contradicts the additional unit claimed for all \(n\equiv1\pmod3\) in Conjecture 1 of Raza (2021); indeed, the conjectured extra unit occurs only in the even subprogression \(n\equiv4\pmod6\), aside from the exceptional \(C_4\).

## Assumptions and scope

All graphs are finite, simple and undirected. \(C_n\) has vertices labelled by residues modulo \(n\), with \(N(i)=\{i-1,i+1\}\). The trace condition applies to **every** vertex, whether or not that vertex belongs to \(S\); this is different from locating-total domination that distinguishes only vertices outside a chosen set. For \(C_4\), opposite vertices have identical open neighborhoods, so no choice of \(S\) can distinguish them.

## Proof

**1. Forbidden omitted pairs.** Set \(Z=V(C_n)\setminus S\). For \(n\ge5\), each open neighborhood consists of two distinct vertices, and two distinct neighborhoods intersect nontrivially exactly when their centers differ by \(2\) or \(-2\) modulo \(n\). The same local argument holds for the triangle \(C_3\). Total domination is equivalent to forbidding both \(i-1\) and \(i+1\) from belonging to \(Z\), namely forbidding any omitted pair at cyclic displacement \(2\).

Under this domination condition, two different traces can coincide only if their underlying open neighborhoods overlap. For centers \(i\) and \(i+2\), the unique shared neighbor is \(i+1\), so the two nonempty traces are equal exactly when both other neighbors \(i-1\) and \(i+3\) are omitted. Those two omitted vertices have cyclic displacement \(4\). Conversely, an omitted pair at displacement \(4\), say \(i-1,i+3\), together with total domination forces \(i+1\in S\) and causes the two equal traces \(N(i)\cap S=N(i+2)\cap S=\{i+1\}\). Therefore, for every \(n\ge3\) other than \(4\),
\[
S\text{ is an OLD code}\quad\Longleftrightarrow\quad
Z\text{ contains no distinct pair at displacement }\pm2\text{ or }\pm4.
\]
(The triangle satisfies the same equivalence by direct inspection of its three neighborhoods.)

**2. The auxiliary cycle square.** Form the simple graph \(H_n\) on \(\mathbb Z/n\mathbb Z\), joining distinct vertices whenever their difference is \(\pm2\) or \(\pm4\). The displayed equivalence says that OLD codes are precisely complements of independent sets of \(H_n\). If \(n\) is odd, multiplication by \(2\), which is a bijection of the residue classes, identifies \(H_n\) with \(C_n^2\), the graph whose distinct vertices have cyclic distance at most two. If \(n=2m\ge6\), the even and odd residue classes do not interact, and dividing their labels by two identifies \(H_n\) with two disjoint copies of \(C_m^2\). This also includes \(m=3,4\), when \(C_m^2\) is complete.

**3. Labelled independence polynomial.** An independent set of \(k\ge1\) vertices in \(C_m^2\) has cyclic gaps of length at least three between successive selected vertices. Starting from a distinguished chosen vertex, the \(k\) ordered gaps sum to \(m\) and each is at least three. By stars-and-bars their number is \(\binom{m-2k-1}{k-1}\). There are \(m\) possible initial labels, and every actual independent set of size \(k\) was counted exactly \(k\) times through the distinguished vertex. Thus its number is \(\frac m k\binom{m-2k-1}{k-1}\), and no such independent set exists for \(k>\lfloor m/3\rfloor\). The empty independent set contributes one. This proves the expression for \(A_m\) and, by the graph decompositions in Step 2, the formulas for \(P_n\).

**4. Minimum, multiplicities, and absence of gaps.** The largest independent set in \(C_m^2\) has size \(\lfloor m/3\rfloor\), attained by the gap construction. Under disjoint union, independence numbers add. Taking complements gives the minimum OLD cardinality displayed in the finding. Every subset of an independent set remains independent; therefore every omission cardinality from zero to the relevant maximum occurs, proving the full contiguous support in the allowed cases. The minimum coefficient formulas are the leading terms of the explicitly counted independence polynomials. The three odd residue-case expressions follow by substituting \(m=3q,3q+1,3q+2\) into the binomial coefficient. Finally, comparing the two minimum expressions with \(\lceil 2n/3\rceil\) yields the asserted modulo-six correction. The explicit \(C_{13}\) set is valid by the forbidden-pair condition.

## Verification

The standalone standard-library program `verify.py` directly checks the OLD definition from open neighborhoods on every selected subset of each cycle \(C_n\), \(3\le n\le17\), and compares it independently to the forbidden-pair characterization and exact coefficient formula. It also independently computes independence-polynomial coefficients using the weighted trace of a four-state cyclic transfer matrix for all lengths \(3\le m\le90\), checks the full support and minimum formula through \(n=250\), and verifies the explicit nine-vertex \(C_{13}\) example. Run with `python3 verify.py`. The recorded output is:

`VERIFY_OK cycles=3..17 masks=262136 OLD_sets=2083 transfer_cycle_squares=3..90 size_support=3..250 C13_witness=PASS`

Finite verification supports the proof but is not a proof for unbounded cycle lengths. The unrestricted result follows from the four mathematical steps above.

## Relationship to prior work

Argiroffo, Bianchi, Lucarini and Wagler (2019), Lemma 2.3, give the scalar claim \(\gamma_{\mathrm{OLD}}(C_n)=\lceil2n/3\rceil\) for cycles; their proposed pattern does not always separate vertices, as Raza subsequently noted for \(C_{13}\). Raza (2021), Section 2 and Conjecture 1, proposes an extra unit whenever \(n\equiv1\pmod3\). The present result retains the earlier known lower bound but establishes the complete corrected minimum and the exact numbers **at all sizes**, including the minimum. It explains why the correction actually depends on parity as well as the residue modulo three. It does not claim that general graph-independent-set counting or the classical cyclic gap formula itself is novel.

Seo and Slater (2010) introduced the OLD notion; Chellali, Rad, Seo and Slater (2014) studied general OLD properties; Givens, Yu and Kincaid studied a distinct circulant with edges of displacements one and three, and separately a mixed-weight model on cycles. These do not supply the displayed complete ordinary-cycle polynomial in the inspected treatments. Definitions using only vertices **outside** a code, or using **closed** neighborhoods, are not equivalent to the OLD property here.

## Limitations

This is a cycle-specific, unweighted, labelled enumeration. It does not solve the corresponding polynomial for arbitrary circulant graphs, weighted OLD codes, or higher-degree graphs. The ordinary cycle-square independence formula is a standard counting ingredient; the claim of originality lies in its exact application to OLD-code constraints, the bivariate parity factorization, exact multiplicities and the corrected published conjecture. No independent mathematical audit has been performed, and a previously unlocated equivalent result may exist.

## References

1. G. R. Argiroffo, S. M. Bianchi, Y. P. Lucarini, A. K. Wagler, *The Identifying Code, the Locating-dominating, the Open Locating-dominating and the Locating Total-dominating Problems Under Some Graph Operations*, Electronic Notes in Theoretical Computer Science **346** (2019), 135–145. DOI: 10.1016/j.entcs.2019.08.013. Especially Lemma 2.3 and Table 2.
2. H. Raza, *Computing Open Locating-Dominating Number of Some Rotationally-Symmetric Graphs*, Mathematics **9** (2021), article 1415, first published 18 June 2021. DOI: 10.3390/math9121415. Especially Section 2, Table 2, Conjecture 1.
3. S. J. Seo, P. J. Slater, *Open neighborhood locating-dominating sets*, Australasian Journal of Combinatorics **46** (2010), 109–120.
4. M. Chellali, N. J. Rad, S. J. Seo, P. J. Slater, *On open neighborhood locating-dominating in graphs*, Electronic Journal of Graph Theory and Applications **2** (2014), 87–98. DOI: 10.5614/ejgta.2014.2.2.1.
5. R. M. Givens, G. Yu, R. K. Kincaid, *Open locating-dominating sets in circulant graphs*, Discussiones Mathematicae Graph Theory **42** (2022), 47–62. DOI: 10.7151/dmgt.2235. The studied graph is the circulant with differences one and three, plus a mixed-weight setting on cycles.
