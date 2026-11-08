# Exact arithmetic-progression structure of modular cubic graphs

## Finding
For every integer \(N\ge2\), write
\[
\Gamma_N=\{(x,x^3):x\in\mathbb Z/N\mathbb Z\}\subseteq(\mathbb Z/N\mathbb Z)^2.
\]
An ordered affine progression of length \(\ell\) has the form \(P_j=P_0+jV\) for all integer indices \(0\le j<\ell\). Distinctness means its points are pairwise distinct, rather than merely its step being nonzero.

For each prime power \(p^k\Vert N\), set \(\epsilon_p=v_p(6)\) (thus \(\epsilon_p=1\) for \(p=2,3\), and zero otherwise), and
\[
s_p=\max\!\left(0,\left\lceil\frac{k-\epsilon_p}{3}\right\rceil\right),\qquad L_N=\prod_{p^k\Vert N}p^{k-s_p}.
\]
**Maximum distinct length:** if \(L_N\ge4\), the greatest length of a pairwise-distinct affine progression lying in \(\Gamma_N\) and containing at least four terms is exactly \(L_N\). If \(L_N<4\), there is no such progression.

**Complete four-term count:** let \(A(N)\) be the number of ordered pairs of residues \((x,h)\) for which
\[
(x+jh,(x+jh)^3),\quad j=0,1,2,3,
\]
is an affine progression in the plane, with repeated points permitted. Then \(A(N)\) is multiplicative. Define \(T_p(0)=1\) and, for every \(k\ge1\),
\[
T_p(k)=p^{2k-\lceil k/2\rceil}+p^{k+\lceil k/2\rceil-1}-p^{k+\lceil k/3\rceil-1}.
\]
The exact local factors are
\[
A(p^k)=\begin{cases}T_p(k),&p\ge5,\\p^2T_p(k-1),&p=2\text{ or }3.\end{cases}
\]
The same two congruences characterize every ordered progression of length at least four, with or without repeated points. Consequently a valid four-term progression extends algebraically for every integer index and traverses precisely \(\operatorname{ord}(h)=N/\gcd(N,h)\) distinct points.

For orientation, \(L_5=1\) (no distinct four-term progression), whereas \(L_6=6\), \(L_8=4\), \(L_{25}=5\), and \(L_{125}=25\). Thus nontrivial long progressions can appear upon lifting from a prime field to its nonreduced residue rings.

## Assumptions and scope
All moduli are integers \(N\ge2\). The graph consists of residue pairs and its group law is componentwise addition. A progression is an **affine progression in the ambient additive group**, not merely a sequence whose first coordinates are in progression. A four-term progression counted in \(A(N)\) need not consist of distinct points. The maximal-length assertion concerns only progressions of at least four pairwise-distinct points, not the separate three-term problem. No assumption of squarefreeness or invertibility of \(6\) is made.

## Proof
**1. Affine progression criterion.** The first coordinates force any progression in the graph to be parametrized by \(x+jh\). Write \(f_j=(x+jh)^3\). Direct expansion gives
\[
f_{j+2}-2f_{j+1}+f_j=6h^2\bigl(x+(j+1)h\bigr).
\]
The two consecutive second differences at \(j=0\) and \(j=1\) vanish modulo \(N\) precisely if \(6h^2(x+h)\equiv6h^2(x+2h)\equiv0\pmod N\), equivalently
\[
N\mid6h^3,\qquad N\mid6h^2x.
\]
When they hold, every second difference, for every integer \(j\), is zero. Therefore these conditions are **both necessary and sufficient** for every length \(\ell\ge4\) and for indefinite algebraic extension. The first coordinate has exact additive period \(N/\gcd(N,h)\), so this is also the number of distinct points of the extended progression.

**2. Local valuation classification.** Work modulo \(p^k\). For any residue \(h\), let \(s=\min(k,v_p(h))\); for \(h=0\), put \(s=k\). Let \(\epsilon=v_p(6)\). The two conditions become
\[
3s+\epsilon\ge k,\qquad v_p(x)+2s+\epsilon\ge k,
\]
where the second condition is automatic when \(2s+\epsilon\ge k\). Thus any admissible step has \(s\ge s_p\), and a step with exactly \(s=s_p\) exists. Such a step has additive order \(p^{k-s_p}\). Choosing \(x=0\) satisfies the second condition for every step satisfying the first. The Chinese remainder theorem simultaneously attains all minimal valuations, and the order of a step modulo \(N\) is the product of its local prime-power orders. Hence its maximum is \(L_N\), attained at \(x=0\); the stated existence/nonexistence cutoff follows.

**3. Local counting.** For \(s<k\), the number of residues \(h\bmod p^k\) with valuation exactly \(s\) is \((p-1)p^{k-s-1}\). Each has precisely \(p^{\min(k,2s+\epsilon)}\) admissible values of \(x\), since the solutions of \(p^k\mid6h^2x\) form the annihilator of \(6h^2\). The zero step contributes \(p^k\). Consequently the exact count is
\[
A(p^k)=p^k+\sum_{s=s_p}^{k-1}(p-1)p^{k-s-1+\min(k,2s+\epsilon)}.
\]
For \(p\ge5\) set \(r=\lceil k/2\rceil\), \(u=\lceil k/3\rceil\). Contributions from steps divisible by \(p^r\), including zero, total \(p^{2k-r}\). The remaining range \(u\le s<r\) contributes
\[
(p-1)p^{k-1}\sum_{s=u}^{r-1}p^s=p^{k+r-1}-p^{k+u-1}.
\]
This proves \(A(p^k)=T_p(k)\). If \(p=2\) or \(3\), then \(6=p\,u\) with \(u\) a \(p\)-adic unit, and both constraints modulo \(p^k\) depend only on \((x,h)\bmod p^{k-1}\). Every solution modulo \(p^{k-1}\) has exactly \(p^2\) lifts, proving \(A(p^k)=p^2T_p(k-1)\). Finally, the conditions factor coordinatewise over the Chinese remainder theorem, establishing \(A(N)=\prod_{p^k\Vert N}A(p^k)\).

## Verification
Execute the standalone script `python3 verify.py` with Python 3 (standard library only). It exhaustively compares both congruences with actual four-point affine progressions and the prime-power product formulas for each \(1\le N\le90\). It tests extensions to nine points for \(N\le30\), verifies the maximum order of admissible steps for \(1\le N\le90\), and cross-checks independent finite valuation sums at six primes through exponent eight. No floating-point arithmetic or external data is used. The proof above establishes the unrestricted statements; these finite checks are not a replacement for the proof.

## Relationship to prior work
Cook and Magyar (2010, arXiv:1011.5302) prove existence and abundance theorems for arithmetic progressions with homogeneous-polynomial restrictions on the **difference** in vector spaces over finite fields. Their Theorem 1 imposes \(\ell\le d<p\) and a singular-locus condition; it neither counts four-term progressions *inside* the one-dimensional cubic graph over arbitrary \(\mathbb Z/N\mathbb Z\) nor determines maximal distinct length. The graph here is highly sparse and prime-power nilpotent effects are central.

Vinh (2017, *Ars Combinatoria* 132, 137--145) studies existence of three-term progressions in product sets of finite fields and rings, using product-graph spectra; its main theorems do not address four-term progressions in the cubic polynomial graph or the local counts. Covert, Iosevich and Pakianathan (2011/2012, arXiv:1105.5373) study distances and dot products in finite prime-power rings, a related setting but a different configuration family. No inspected statement establishes the exact formulas above; a historical formulation elsewhere is possible.

## Limitations
The count includes repeated-point four-term progressions; the maximal-length statement separately imposes pairwise distinctness. The theorem classifies lengths four and higher, not three-term progression counts or maximal three-term configurations. It treats the specific cubic graph, not general polynomial graphs. Elementary finite-difference and valuation methods make an independent rediscovery plausible; the historical novelty assessment is necessarily qualified.

## References
1. B. Cook and Á. Magyar, *On restricted arithmetic progressions over finite fields*, arXiv:1011.5302v1 (first public 2010-11-24), full text at https://arxiv.org/html/1011.5302v3.
2. L. A. Vinh, *On 3-term arithmetic progressions in product sets over finite rings via spectra of graphs*, Ars Combinatoria **132** (2017), 137--145, https://combinatorialpress.com/article/ars/Volume%20132/volume-132-paper-12.pdf.
3. D. Covert, A. Iosevich, and J. Pakianathan, *Geometric configurations in the ring of integers modulo \(p^\ell\)*, arXiv:1105.5373 (2011), https://arxiv.org/abs/1105.5373.
