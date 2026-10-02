# Multiset dimension three for a mod-four family of cylindrical graphs

## Result

Let \(P_m\) have vertices \(0,1,\ldots,m-1\), and let \(C_n\) have vertices in \(\mathbb Z_n\). For a vertex set \(W\), write the multiset code of \(v\) as the sorted list of distances from \(v\) to the vertices of \(W\).

**Theorem.** Let \(m\ge 3\) and let \(n\ge 6m\) satisfy
\[
n\equiv 2\pmod 4.
\]
Then
\[
\operatorname{md}(P_m\square C_n)=3.
\]
More explicitly, write \(n=2L\), so \(L\) is odd, and choose the odd integer \(a\) by
\[
a=\begin{cases}
2q+1,&L=6q+1,\\
2q+1,&L=6q+3,\\
2q+3,&L=6q+5.
\end{cases}
\]
Then
\[
W=\{(0,0),(0,a),(0,L)\}
\]
is a multiset-resolving set of \(P_m\square C_n\).

The new range is substantive: the previously published general three-landmark result for cylindrical graphs assumes \(n\ge 8m+1\). Thus the theorem resolves an infinite congruence class inside the previously open strip \(6m\le n\le 8m\).

## Antipodal three-landmark capacity on an even cycle

The proof rests on an exact collision calculation on \(C_{2L}\). Assume throughout this section that \(L\ge 7\) is odd and \(1\le a\le (L-1)/2\). Put
\[
B_a=\{0,a,L\}\subseteq V(C_{2L}).
\]
For \(x\in C_{2L}\), let
\[
s_a(x)=(d_1(x),d_2(x),d_3(x)),\qquad d_1(x)\le d_2(x)\le d_3(x),
\]
be the sorted distance triple from \(x\) to \(B_a\). Define
\[
\mu_a(x)=d_1(x),\qquad
h_a(x)=(d_2(x)-d_1(x),d_3(x)-d_1(x)).
\]
Thus \(h_a\) forgets only a common additive translation of the three entries.

**Lemma 1 (exact normalized collisions).** Every nonsingleton fibre of \(h_a\) has size two, and the fibres are exactly as follows.

1. If \(a\) is even, they are
   \[
   \left\{j,\ 2L+\frac a2-j\right\},
   \qquad a\le j\le L-\frac a2,
   \]
   and on every such pair the two values of \(\mu_a\) differ by exactly \(a/2\).
2. If \(a\) is odd and \(3a\le L\), there is exactly one nonsingleton fibre,
   \[
   \left\{\frac{L-a}{2},\frac{3L-a}{2}\right\},
   \]
   and its two \(\mu_a\)-values differ by exactly \(a\).
3. If \(a\) is odd and \(3a\ge L\), the nonsingleton fibres are
   \[
   \left\{j,\ 2L-\frac{L-a}{2}-j\right\},
   \qquad \frac{L-a}{2}\le j\le a,
   \]
   and on every such pair the two \(\mu_a\)-values differ by exactly \((L-a)/2\).

At \(3a=L\), the descriptions in (2) and (3) coincide in one pair.

### Proof of Lemma 1

On the first semicircle \(0\le x\le L\), sorting the three affine distance functions gives the following table. Endpoints that are half-integral simply contribute no integer vertex there.

| interval for \(x\) | \(h_a(x)\) | \(\mu_a(x)\) |
|---|---|---|
| \(0\le x\le a/2\) | \((a-2x,L-2x)\) | \(x\) |
| \(a/2\le x\le a\) | \((2x-a,L-a)\) | \(a-x\) |
| \(a\le x\le L/2\) | \((a,L+a-2x)\) | \(x-a\) |
| \(L/2\le x\le (L+a)/2\) | \((L+a-2x,a)\) | \(x-a\) |
| \((L+a)/2\le x\le L\) | \((2x-L-a,2x-L)\) | \(L-x\) |

For the second semicircle write \(x=2L-t\), with \(0\le t\le L\). Since the distance from \(2L-t\) to \(a\) is \(\min(t+a,2L-a-t)\), sorting gives

| interval for \(t\) | \(h_a(2L-t)\) | \(\mu_a(2L-t)\) |
|---|---|---|
| \(0\le t\le (L-a)/2\) | \((a,L-2t)\) | \(t\) |
| \((L-a)/2\le t\le L/2\) | \((L-2t,a)\) | \(t\) |
| \(L/2\le t\le L-a\) | \((2t-L,2t+a-L)\) | \(L-t\) |
| \(L-a\le t\le L-a/2\) | \((2t-L,L-a)\) | \(L-t\) |
| \(L-a/2\le t\le L\) | \((L-a,2t-L)\) | \(L-t\) |

Within either semicircle these affine pieces are injective and meet only at their common boundary vertex. Hence every collision between distinct vertices must occur between the two tables. Comparing the affine images leaves only the following possibilities.

- If \(a\) is even, the third, fourth and fifth rows of the first table meet respectively the first, second and third rows of the second table. In each case equality is equivalent to \(t=x-a/2\). Joining the three consecutive ranges gives
  \[
  a\le x\le L-a/2,
  \]
  hence the pairs in (1). Substitution in the two \(\mu_a\)-columns gives difference \(a/2\).
- If \(a\) is odd, the preceding equations would require a half-integral shift and therefore give no integer collision. The second row of the first table can meet the fourth row of the second table exactly when \(3a\ge L\); equality is \(t=x+(L-a)/2\), which yields the interval \((L-a)/2\le x\le a\) and the pairs in (3), with \(\mu_a\)-difference \((L-a)/2\).
- The only remaining cross-table intersection is between the third row of the first table and the third row of the second table. It forces
  \[
  x=\frac{L-a}{2},\qquad t=\frac{L+a}{2},
  \]
  and is present exactly when \(3a\le L\). It gives the pair in (2), whose \(\mu_a\)-difference is \(a\).

The coordinate ranges in the tables rule out every other cross-table intersection. This proves the classification. \(\square\)

Define the **translation separation**
\[
\tau(L,a)=\min\{|\mu_a(x)-\mu_a(y)|:x\ne y,\ h_a(x)=h_a(y)\}.
\]
Lemma 1 gives the exact formula
\[
\tau(L,a)=
\begin{cases}
a/2,&a\text{ even},\\
\min\{a,(L-a)/2\},&a\text{ odd}.
\end{cases}
\]
Consequently
\[
\max_{1\le a\le (L-1)/2}\tau(L,a)=\left\lfloor\frac L3\right\rfloor.
\]
Indeed, the displayed choices of odd \(a\) for \(L\bmod 6\) attain \(\lfloor L/3\rfloor\), while \(\min\{a,(L-a)/2\}\le L/3\) for odd \(a\), and \(a/2<L/3\) for even \(a\le(L-1)/2\).

This also has an exact interpretation: among boundary triples of the form \(B_a=\{0,a,L\}\), the largest path order \(r\) for which their lifts to layer zero resolve \(P_r\square C_{2L}\) is precisely \(\lfloor L/3\rfloor\).

## Lifting from the cycle to the cylinder

**Lemma 2 (vertical-lift criterion).** Let \(W_a=\{(0,0),(0,a),(0,L)\}\). Then \(W_a\) resolves \(P_m\square C_{2L}\) if and only if
\[
|\mu_a(x)-\mu_a(y)|\ge m
\]
for every distinct \(x,y\) with \(h_a(x)=h_a(y)\).

**Proof.** For a cylinder vertex \((i,x)\), every landmark lies in layer zero, so its sorted distance triple is
\[
s_a(x)+i(1,1,1).
\]
If two such triples are equal, subtracting their minima shows that the corresponding normalized codes \(h_a\) are equal. Conversely, if \(h_a(x)=h_a(y)\), then
\[
s_a(y)=s_a(x)+(\mu_a(y)-\mu_a(x))(1,1,1).
\]
Rows \(i,j\in\{0,\ldots,m-1\}\) can cancel this translation exactly if and only if
\(|\mu_a(x)-\mu_a(y)|\le m-1\). This proves the criterion. \(\square\)

## Proof of the theorem

Write \(n=2L\). The congruence \(n\equiv2\pmod4\) makes \(L\) odd, and \(n\ge6m\) gives \(L\ge3m\). For the displayed choice of \(a\), the capacity calculation gives
\[
\tau(L,a)=\left\lfloor\frac L3\right\rfloor\ge m.
\]
Lemma 2 therefore shows that \(W\) is a three-vertex multiset-resolving set. Thus \(\operatorname{md}(P_m\square C_n)\le3\).

The graph \(P_m\square C_n\) is connected and is not a path. A standard foundational result for multiset dimension states that no connected graph has multiset dimension two and that a nontrivial connected graph has multiset dimension one exactly when it is a path. Hence \(\operatorname{md}(P_m\square C_n)\ge3\), proving equality. \(\square\)

## Verification evidence

The proof above is general and does not depend on computation. The accompanying checker directly evaluates the cycle distance triples and the lifted cylinder codes. It reproduces the collision classification for every odd \(7\le L\le301\) and every admissible \(a\), and verifies the stated construction for \(3\le m\le40\) across a finite band of admissible circumferences beginning at \(6m\). No discrepancy was found in those checks.

## Context and limitations

Marcelo, Tolentino, Garciano and Buot proved in 2025 that every cylindrical graph has finite multiset dimension and that
\[
\operatorname{md}(P_m\square C_n)=3\qquad(n\ge8m+1),
\]
while explicitly leaving the remaining cases open. The present theorem lowers the sufficient circumference coefficient from eight to six on the congruence class \(n\equiv2\pmod4\), and the antipodal-capacity calculation explains why this particular boundary construction reaches the constant six.

The theorem does **not** determine the remaining congruence classes, does not settle \(n<6m\), and does not claim that \(6m\) is the optimal threshold among arbitrary three-landmark configurations. The exact capacity statement applies only to the antipodal boundary family \(\{(0,0),(0,a),(0,n/2)\}\).

## References

1. R. M. Marcelo, M. A. C. Tolentino, A. D. Garciano, and J. C. Buot, “On multiset dimension of cylindrical graphs,” *Journal of Combinatorial Mathematics and Combinatorial Computing* 126 (2025), 225–240. DOI: https://doi.org/10.61091/jcmcc126-15
2. R. Simanjuntak, T. Vetrík, and P. B. Mulia, “The multiset dimension of graphs,” arXiv:1711.00225. https://arxiv.org/abs/1711.00225
3. M. Farhan, S. Klavžar, D. Kuziak, and I. G. Yero, “Multiset resolvability parameters in graphs: A survey with new results and open problems,” arXiv:2607.10311. https://arxiv.org/abs/2607.10311
