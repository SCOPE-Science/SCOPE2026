# Four two-variable theories of prime cyclic groups in relational addition

## Finding

For each prime \(p\), let
\[
\mathcal G_p=(\mathbb Z/p\mathbb Z;R,0),\qquad
R(a,b,c)\ \Longleftrightarrow\ a+b=c\pmod p.
\]
The language contains equality, the ternary relation \(R\), and the constant \(0\), but **no addition or inverse function symbol**. All equivalences below concern counting-free first-order logic with at most the specified number of reusable variable names, at unrestricted quantifier depth.

**Theorem.** On the family \(\{\mathcal G_p:p\text{ prime}\}\):

1. There are exactly two \(\mathrm{FO}^{1}\)-theories: \(p=2\) and all odd primes together.
2. There are exactly four \(\mathrm{FO}^{2}\)-theories, represented by \(p=2\), \(p=3\), \(p=5\), and one shared theory for **all primes \(p\ge7\)**. In particular, \(\mathcal G_7\equiv_{\mathrm{FO}^{2}}\mathcal G_{11}\), and the same holds for every pair of primes at least seven.
3. Every pair of distinct primes is distinguished by a sentence in \(\mathrm{FO}^{3}\). Hence every prime is a separate theory at each variable width \(k\ge3\).

The least variable width defining \(\mathcal G_p\) **relative to this family** is one for \(p=2\), two for \(p=3,5\), and three for each prime \(p\ge7\).

## Assumptions and scope

Prime parameters are positive rational primes, including \(2\). Structures are finite nonempty cyclic groups of order \(p\) in the indicated **relational** signature. A variable name may be reused under nested quantifiers. The language contains no counting quantifiers or infinitary connectives. The conclusion does not assert equivalence with nonprime cyclic groups or with arbitrary finite abelian groups.

## Proof

### Atomic information involving at most two variable names

Write \(x,y\) for the two possible variable names, with \(0\) additionally available as a constant. Every atom involving \(R\) and terms chosen among \(0,x,y\), along with all equalities between such terms, is determined by the following tests:
\[
\begin{gathered}
x=0,\quad y=0,\quad x=y,\\
2x=0,\quad 2y=0,\quad
2x=y,\quad 2y=x,\quad x+y=0.
\end{gathered}
\]
This follows by inspecting all substitutions into the three argument positions of \(R\); there are only \(3^3\) choices, and commutativity reduces them to the displayed equations. Thus no additional atomic relation involving the two variable names is overlooked.

When \(p\ge7\) and \(x\ne0\), the possible atomic profiles of a second point \(y\), relative to \(x\), are precisely
\[
y=0,\qquad y=x,\qquad y=2x,\qquad
y=\tfrac12 x,\qquad y=-x,\qquad
\text{or none of these five cases}.
\]
The first five choices are distinct for every prime \(p\ge7\), and the last choice is available because \(p-5\ge2\). When \(x=0\), only \(y=0\) and \(y\ne0\) occur. These possibilities, and the complete atomic profiles they determine, are independent of the prime as soon as \(p\ge7\).

### Permanent two-pebble equivalence

Fix two primes \(p,q\ge7\). Duplicator maintains the invariant that the current pebbled pairs have identical atomic profiles, including their relationships to the named zero. When one pebble stays at a nonzero element, Spoiler's replacement for the other pebble is in exactly one of the six classes displayed above. Duplicator chooses an element of the same class relative to the fixed corresponding pebble in the other group. When the fixed pebble is zero, the two-class description suffices. If no pebble is fixed, Duplicator matches zero to zero and nonzero to nonzero.

Every response preserves all atomic formulas on the pebbled tuple. The response options remain available **after every move**, so this is a strategy for arbitrarily many rounds. By the standard pebble-game characterization, \(\mathcal G_p\equiv_{\mathrm{FO}^{2}}\mathcal G_q\) for all primes \(p,q\ge7\).

### Sharp formulas for the exceptional primes

All following sentences use only the variable names \(x,y\), in addition to the constant \(0\). Let
\[
\alpha:=\exists x\,(x\ne0\land R(x,x,0)),
\]
\[
\beta:=\exists x\exists y\,
(x\ne0\land R(x,x,y)\land R(x,y,0)),
\]
and
\[
\begin{split}
\gamma:=\exists x\exists y\,(&x\ne0\land y\ne0\land y\ne x\\
&\land\neg R(x,x,y)\land\neg R(y,y,x)\land\neg R(x,y,0)).
\end{split}
\]
For prime \(p\), the sentence \(\alpha\) holds exactly at \(p=2\), because it asserts the existence of a nonzero element of order two. The sentence \(\beta\) holds exactly at \(p=3\), because \(y=2x\) and \(x+y=0\) force \(3x=0\). Finally, \(\gamma\) holds exactly when \(p\ge7\): for each nonzero \(x\), it requests a nonzero \(y\) outside the four choices \(x,2x,\tfrac12 x,-x\). For \(p=5\) those four elements exhaust the nonzero group, whereas every \(p\ge7\) supplies another element. The smaller primes also fail \(\gamma\).

Therefore \(\alpha\), \(\beta\), and \(\gamma\), together with Boolean combinations, separate all four classes. The previous pebble strategy shows that no further \(\mathrm{FO}^{2}\) classes occur.

### One variable

With just \(x\) and the constant \(0\), all atomic information about a nonzero element is identical among odd prime cyclic groups: \(2x\ne0\), while \(x=0\) is false. Thus matching zero with zero and any nonzero element with any nonzero element is a permanent one-pebble strategy between odd primes. The sentence \(\alpha\) above uses only \(x\) and separates \(p=2\) from odd primes. This proves exactly two \(\mathrm{FO}^{1}\) theories.

### Three variables distinguish every prime

For each positive integer \(n\), let \(D_n(x,y)\) be a formula expressing \(y=nx\). Begin with \(D_1(x,y)\) equal to \(x=y\). Inductively set
\[
D_{n+1}(x,y):=\exists z\,
\bigl(R(z,x,y)\land D_n(x,z)\bigr).
\]
In each recursive use of \(D_n(x,z)\), the internal bound variable names are alternated between \(y\) and \(z\); no fourth name is introduced, and \(x\) remains free. The recursion has the indicated semantics by induction: \(z=nx\) and \(z+x=y\) exactly when \(y=(n+1)x\).

For a prime \(r\ge2\), form the sentence
\[
\theta_r:=\exists x\,\bigl(x\ne0\land
\exists y\,[R(y,x,0)\land D_{r-1}(x,y)]\bigr).
\]
It uses only \(x,y,z\), and says that a nonzero element satisfies \(rx=0\). In \(\mathcal G_p\), this holds if and only if \(p=r\), since both are prime. Hence every two different prime cyclic groups are \(\mathrm{FO}^{3}\)-distinguishable, proving the final part of the theorem.

## Verification

The standalone checker `verify_prime_logic.py` enumerates all \(3^3\) ternary atomic substitutions, forms atomic two-pebble profiles, and computes both possible one-pebble replacement-profile sets for every ordered pair in each of fourteen prime groups through order \(43\). It verifies that these replacement sets are constant within each profile and match between prime groups exactly in the predicted four classes. It also evaluates explicit separating patterns and three-variable recursive formula abstract-syntax trees for the first seven primes.

Run with an ordinary Python 3 interpreter:

```bash
python3 verify_prime_logic.py
```

The recorded output is in `verification_output.txt`. Finite computation checks only the specified instances. The unrestricted-depth theorem is established by the permanent strategy and the formulas proved above.

## Relationship to prior work

Gomaa's 2007 dissertation, *Model Theory and Complexity Theory*, Section 3.3 defines exactly the ternary relation and named identity used here, and Section 3.5 studies finite-variable pebble games and gives a five-pebble upper bound for distinguishing prime cyclic groups. The present claim is the exact, **unrestricted-depth one-/two-/three-variable classification within the prime-order subfamily**; that bound does not imply the collapse of all primes at least seven at width two.

Grohe and Otto (2012) develop general pebble-game equivalences and boolean-semiring methods, but do not give the stated prime-cyclic classification. Bova and Martin (2015) study first-order model checking on finite abelian groups in the **functional** signature with addition and inverse; its source language is richer, so bounded-variable results there do not directly imply a bounded-variable classification in the ternary relational signature. Related published work on quantifier-rank bounds for prime cyclic groups addresses a distinct resource and does not, in its accessible summary, state this complete two-variable partition.

## Limitations

The result does not classify composite cyclic orders, all groups, counting logic, or languages containing addition as a function symbol. The same-model correctness and originality assessments are not independent certification; the historical-priority search cannot exclude an unidentified stronger finite-variable composition theorem. The complete mathematical argument, including all quantifiers and signature restrictions, appears above.

## References

1. W. Gomaa, *Model Theory and Complexity Theory*, University of Maryland dissertation, 2007, Section 3.3 and Section 3.5, https://drum.lib.umd.edu/items/b8c06e8c-d2da-4d80-923e-0bd02e2a8440.
2. W. Gomaa, *Descriptive Complexity of Finite Abelian Groups*, International Journal of Algebra and Computation 20 (2010), 1087–1116, DOI: 10.1142/S0218196710006047 (abstract inspected; journal full text not established as read).
3. M. Grohe and M. Otto, *Pebble Games and Linear Equations*, CSL 2012, DOI: 10.4230/LIPIcs.CSL.2012.289.
4. S. Bova and B. Martin, *First-Order Queries on Finite Abelian Groups*, CSL 2015, DOI: 10.4230/LIPIcs.CSL.2015.41.
