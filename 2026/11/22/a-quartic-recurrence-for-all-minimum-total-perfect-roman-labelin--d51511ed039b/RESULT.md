# A quartic recurrence for all minimum total perfect Roman labelings of cycles

## Finding

For every integer \(n\ge3\), let \(C_n\) be the simple cycle on indexed vertices \(0,1,\ldots,n-1\). A **total perfect Roman dominating function** is a map \(f:V(C_n)\to\{0,1,2\}\) satisfying two local conditions: each vertex of value zero has **exactly one** neighbor of value two, and each vertex of positive value has a **positive** neighbor. Its weight is \(w(f)=\sum_v f(v)\).

The previously known minimum weight is \(\gamma^p_{tR}(C_n)=n\) [1]. Define \(a_n\) to be the number of functions of weight exactly \(n\). Then

\[
\boxed{\sum_{n\ge3}a_nx^n=\frac{7x^3+6x^4+3x^5+x^6}{1-x-2x^3-x^4}.}
\]

Consequently, \((a_3,a_4,a_5,a_6)=(7,13,16,31)\) and, for every \(n\ge7\),

\[
\boxed{a_n=a_{n-1}+2a_{n-3}+a_{n-4}.}
\]

An equivalent, nonnegative coefficient formula is

\[
\boxed{a_n=n[x^n]\log\frac1{1-x-2x^3-x^4}
=n\!\!\sum_{\substack{p,q,r\ge0\\p+3q+4r=n}}
\frac{2^q(p+q+r-1)!}{p!q!r!},\quad n\ge3.}
\]

The asymptotic is \(a_n\sim\lambda^n\), where \(\lambda=1.794309659412\ldots\) is the positive root of \(\lambda^4-\lambda^3-2\lambda-1=0\). Thus the number of optimal placements grows exponentially, even though the optimal cost is always exactly the number of cycle vertices. The first ten values, at lengths three through twelve, are \(7,13,16,31,64,109,187,346,628,1111\).

## Assumptions and scope

All graphs here are finite, simple, undirected and vertex-indexed. The cycle length is at least three. Adjacent indices are taken modulo \(n\). Rotations and reversals are **not** identified, and the three labels are distinct. All generating functions are formal power series in \(\mathbb Q[[x]]\); in particular, \(x\) is a formal marker of **cycle length**, not the weight of a labeling. No assertion is made about all nonminimum total perfect Roman functions.

## Proof

**1. Exact local rule.** For a triple of consecutive values \((a,b,c)\in\{0,1,2\}^3\), put
\[
\operatorname{ok}(a,b,c)\iff
\begin{cases}
\mathbf 1_{\{a=2\}}+\mathbf 1_{\{c=2\}}=1,&b=0,\\
(a>0)\text{ or }(c>0),&b>0.
\end{cases}
\]
A cyclic word is a total perfect Roman function if and only if its \(n\) centered triples satisfy this condition. This includes \(C_3\), for which the two neighbors of a vertex are distinct.

**2. An exact nonnegative reduced cost.** Use the nine ordered-pair states \((a,b)\in\{0,1,2\}^2\). There is a directed transition \((a,b)\to(b,c)\) when \(\operatorname{ok}(a,b,c)\). Assign the potential
\[
h(0,2)=-2,\qquad h(2,0)=0,\qquad h(a,b)=-1\ \text{for all other ordered pairs}.
\]
For every allowed transition define
\[
r(a,b,c)=b-1+h(a,b)-h(b,c).
\]
**Direct exact check:** there are twenty allowed triples, and for every one of them \(r(a,b,c)\) is a nonnegative integer. This finite lemma is checked from its full specified 27-triple domain by the standalone verifier; it can also be verified manually from the three cases \(b=0,1,2\). For a cyclic labeling, the sum of the potential differences is zero, so
\[
w(f)-n=\sum_{i=0}^{n-1}r\bigl(f(i-1),f(i),f(i+1)\bigr)\ge0.
\]
The all-one labeling is feasible and has weight \(n\). Hence the minimum is \(n\), independently recovering the known numerical value [1]. More importantly, a feasible labeling has weight \(n\) **if and only if** every one of its transitions has reduced cost zero.

**3. The critical transition graph.** List states in the order \(00,01,02,10,11,12,20,21,22\), where \(ab\) means \((a,b)\). The complete list of **zero-cost successors** is

```
00 -> 02
01 -> 11,12
02 -> 21,22
10 -> 02
11 -> 10,11,12
12 -> 20
20 -> 00,01
21 -> 10,11,12
22 -> 20
```

There are sixteen such directed edges. Write \(Z\) for their nine-by-nine zero-one adjacency matrix, indexed in the displayed order. This successor list is an explicit, reproducible complete specification of \(Z\). Its determinant, by ordinary integer polynomial expansion or exact Newton identities, is
\[
\det(I-xZ)=1-x-2x^3-x^4.
\]
The standalone verifier reconstructs the matrix and checks all ten determinant coefficients exactly, including the five zero high-degree coefficients.

**4. Cyclic enumeration.** For \(n\ge3\), each labelled cyclic word of length \(n\) determines a unique length-\(n\) closed walk in the ordered-pair automaton, with initial state \((f(0),f(1))\); conversely every such closed walk determines exactly that labelled word. The zero-reduced-cost condition proved above gives
\[
a_n=\operatorname{tr}(Z^n),\qquad n\ge3.
\]
Use the formal trace–determinant identity
\[
-\log\det(I-xZ)=\sum_{n\ge1}\frac{\operatorname{tr}(Z^n)}n x^n.
\]
With the displayed determinant, this gives the logarithmic coefficient formula. The formal trace values at indices one and two are both one; they are closed automaton walks rather than the simple cycles considered here. Subtracting \(x+x^2\) from the full trace series yields
\[
\sum_{n\ge3}a_nx^n
=\frac{x+6x^3+4x^4}{1-x-2x^3-x^4}-x-x^2
=\frac{7x^3+6x^4+3x^5+x^6}{1-x-2x^3-x^4}.
\]
Expanding \(\log(1/(1-U))=\sum_{m\ge1}U^m/m\), with \(U=x+2x^3+x^4\), and using multinomial coefficients gives the positive factorial sum. The denominator gives the recurrence, valid from \(n\ge7\), with four initial values as stated.

**5. Growth.** Let \(\lambda_j\) be the four roots, with multiplicities, of \(t^4-t^3-2t-1=0\). The trace–determinant identity shows \(a_n=\sum_{j=1}^4\lambda_j^n\) for every \(n\ge3\). The polynomial has one positive real root \(\lambda=1.794309659412\ldots\); its remaining roots are approximately \(-0.439087115146\) and \(-0.177611272133\pm1.112527792130i\), all of smaller absolute value. Therefore \(a_n=\lambda^n+O(\mu^n)\) for any \(\mu\) strictly between the second-largest root modulus and \(\lambda\). In particular \(a_n\sim\lambda^n\), with leading constant exactly one.

## Verification

Run `python3 verify.py` (Python 3, standard library only). The checker independently evaluates all twenty legal local triples and their reduced costs, constructs the zero-edge graph, calculates the determinant by exact integer Newton identities, compares the formula with direct enumeration of **all** \(3^n\) labelings for every \(3\le n\le12\), and checks the recurrence through index sixty. It finishes with `VERIFY_OK`. Brute-force checks do not constitute the infinite proof; the potential lemma and trace identity above do.

## Relationship to prior work

Almulhim [1, Definition 1 and Theorem 3] introduced total perfect Roman domination and explicitly proved the scalar equality \(\gamma^p_{tR}(C_n)=n\). That exact minimum **is not new**. The accessible full text does not state the all-orders count, this nine-state optimum criterion, or the rational minimum-labeling enumerator.

Related published results on open two-row ladders [2] give minimum total perfect Roman function counts for \(P_2\square P_n\), not for simple cycles. Other cycle enumerations [3,4] treat pointwise-minimal ordinary Roman functions or independent Roman functions; both impose logically different conditions and have different sequences. In particular, the values \(7,13,16,31\) cannot be obtained merely by specializing the weight polynomial of minimal ordinary Roman functions [3]. The new claim is precisely the complete minimum-function count for **total perfect Roman domination on cycles**, not a general definition, an existing scalar optimum or a relabeled previously proved formula.

## Limitations

This theorem enumerates only optimum-weight functions on labelled simple cycles. It does not enumerate higher-weight functions, classify equivalence classes under dihedral symmetry, or extend to paths, prisms or other graph families. Targeted literature and mathematical-record searches do not rule out obscure or unindexed equivalents. Independent mathematical review has not been performed.

## References

[1] A. Almulhim, *Total Perfect Roman Domination*, Symmetry **15** (2023), 1676, first published August 31, 2023, DOI 10.3390/sym15091676. Full text: https://www.mdpi.com/2073-8994/15/9/1676.

[2] *Exact total perfect Roman domination and minimum-function multiplicities on ladder graphs*, publicly accessible research result, 2026: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-total-perfect-roman-domination-and-minimum-function-multip--b1badea27fb1.

[3] *Exact weight census of pointwise-minimal Roman domination on cycles*, publicly accessible research result, 2026: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-weight-census-of-pointwise-minimal-roman-domination-on-cyc--ca1e0cc36d93.

[4] *Independent Roman weight enumerator of cycles*, publicly accessible research result, 2026: https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-independent-roman-weight-enumerator-of-cycles--46324718e498.
