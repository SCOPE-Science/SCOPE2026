# An exact idempotent–isometry commuting-pair census for a finite chain

## Finding

For each integer \(n\ge 2\), let \(D_n\) be the inverse monoid of distance-preserving partial injections of the chain \([n]\), including the empty map. Its idempotents \(E_n\) are the partial identities. Let \(T_n\) be the number of ordered commuting pairs with first factor in \(E_n\) and second factor in \(D_n\), including pairs whose second factor is also idempotent. Write
\[
H_{n,\ell}=2^{n-\ell}10^{\lfloor\ell/2\rfloor}4^{\ell\bmod2}.
\]
Then
\[
\boxed{T_n=4^n+4\cdot3^n+H_{n,n}+2\sum_{\ell=1}^{n-1}H_{n,\ell}-(5n+3)2^n-n(n-1)2^{n-1}.}
\]
The factor \(10\) counts the compatible restrictions and idempotent labels on an exchanged pair of a reflection. Both arrows of that pair may be present, a possibility absent for order-decreasing maps and not represented by the translation-forest calculation. The statistic \(T_n\) sums the sizes of the idempotent centralizers of all partial isometries; subtracting \(4^n\) gives exactly the incidence count with an idempotent in the first position and a nonidempotent in the second.

## Assumptions and scope

Equality is equality of partial maps, including equality of their domains. Composition convention does not affect commutation. Use coordinates \(0,\ldots,n-1\) for the proof. A map of rank at least two extends uniquely to a translation \(p_k(i)=i+k\), \(-n+1\le k\le n-1\), or a reflection \(r_c(i)=c-i\), \(0\le c\le 2n-2\). Indeed, two domain points determine the sign and offset from their two images; distances to the two distinct image points determine the image of any further point uniquely. The available domain of a model consists of coordinates whose images stay in the chain. A rank-one map has one model of each type and the empty map has every model. No claim is made here about the count of commuting pairs having no idempotent factor.

## Proof

**Idempotents and the weight of a fixed map.** An idempotent partial injection \(f\) must fix every point in its domain: idempotence gives \(f(f(i))=f(i)\) with both \(i\) and \(f(i)\) in the domain, and injectivity gives \(f(i)=i\). For \(A\subseteq[n]\), the partial identity \(e_A\) commutes with \(f\) exactly when \(\mathbf1_A(i)=\mathbf1_A(f(i))\) for every \(i\in\operatorname{dom}f\). This is equality of the two product domains, after which the maps have the same values. Let \(G_f\) be the undirected graph on all \(n\) coordinates formed by the moved arrows of \(f\), forgetting direction and ignoring repeated edges. The membership bits of \(A\) may be chosen independently across components of \(G_f\), including isolated points, giving weight \(2^{c(G_f)}\).

**Translations.** A nonzero shift with \(\ell=n-|k|\) available positions offers a forest of possible edges along chains with step \(|k|\). Choosing \(j\) available positions selects \(j\) distinct forest edges and gives weight \(2^{n-j}\). Thus summing over restrictions gives \(2^{n-\ell}3^\ell\). The zero shift contributes \(4^n\) because each of its \(2^n\) restrictions is an idempotent. There are two nonzero shifts for each \(1\le\ell<n\), so the model sum for translations is
\[
4^n+2\sum_{\ell=1}^{n-1}2^{n-\ell}3^\ell=4^n+4\cdot3^n-6\cdot 2^n.
\]

**Reflections.** For \(r_c\), the available interval has length \(\ell=n-|c-(n-1)|\). The reflection preserves this interval and decomposes it into \(\lfloor\ell/2\rfloor\) exchanged pairs and, if \(\ell\) is odd, one fixed point. On an exchanged pair the possible domain choices are neither endpoint, just the first, just the second, or both. The first choice allows four labelings by membership in \(A\); each other choice imposes equality of the two bits and allows two. The joint count is therefore \(4+2+2+2=10\). A fixed point gives four choices for its two bits (domain and \(A\)); a coordinate outside the interval gives two choices for membership in \(A\). These choices factor across orbits, giving \(H_{n,\ell}\). Exactly one reflection has \(\ell=n\) and two have each \(1\le\ell<n\), yielding the reflection sum in the formula.

**Model overlaps.** There are \(4n-2\) models, so the empty map was counted \(4n-3\) extra times, each with weight \(2^n\). Rank-one maps were each counted one extra time. There are \(n\) fixed rank-one maps of weight \(2^n\), and \(n(n-1)\) moved rank-one maps of weight \(2^{n-1}\). There are no further overlaps. Subtracting these extra weights from the two model sums proves the formula. In particular at \(n=2\) it gives \(22\), including the \(16\) pairs of idempotents.

## Verification

The accompanying `check_commutation.py` enumerates distinct partial isometries and compares both composition orders as partial maps for \(2\le n\le7\). The recorded `check_output.txt` includes the mixed counts \(22,116,520,2188,8556,32812\). The same checker also reports the total number of commuting pairs in this small range; those totals are not asserted as an all-size formula. The argument above proves the incidence census for every \(n\ge2\).

## Relationship to prior work and limitations

Kehinde and Umar (arXiv:1101.0049v1, Theorem 3.16) give the previously known cardinality \(|D_n|=6\cdot2^n-n^2-4n-5\). The signed-translation result *Exponential convergence to one-ninth commutativity for finite-chain partial translations* (Resultary `015301143d17`) has a rank-refined translation incidence count and excludes reflections. The parity-sensitive order-decreasing spectrum (Resultary `e6b2ccea87b9`) includes reflections under a different domain condition: a reflected two-point orbit cannot contribute the upward arrow there. Its rank spectrum does not give the two-arrow choice counted here.

*Idempotent concentration and a one-thirty-sixth commuting law for chain partial isometries* (Resultary [`f54b34cb7503`](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-idempotent-concentration-and-a-one-thirty-sixth-commuting-law-fo--f54b34cb7503/RESULT.md)) treats the same full monoid, and gives the \(1/36\) limit and exponential dominance of idempotent–idempotent pairs. That concentration result is not a novelty claim here. Its proof uses reflected two-cycles for independent probabilistic obstructions, as opposed to summing the full incidence weight of the restrictions on each reflected orbit. The precise novelty claim is the exact incidence census and its reflection factor. Historical priority beyond the compared sources is not asserted.
