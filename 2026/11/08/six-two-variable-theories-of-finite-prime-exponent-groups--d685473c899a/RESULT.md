# Six two-variable theories of finite prime-exponent groups

## Finding

Let \(\mathcal K\) be the class of all **nontrivial finite groups of prime exponent**. Each group \(G\) is treated as a relational structure \((G;R,1)\), where \(1\) is a named identity and \(R(a,b,c)\) holds exactly when \(ab=c\). The symbol \(R\) is a relation, **not** a multiplication function. Write \(\mathrm{FO}^{k}\) for ordinary first-order logic with at most \(k\) reusable variable names, without counting quantifiers and with unrestricted quantifier depth.

**Classification theorem.** Exactly six distinct \(\mathrm{FO}^{2}\)-theories occur on \(\mathcal K\). Two structures from \(\mathcal K\) satisfy the same \(\mathrm{FO}^{2}\)-sentences precisely when they belong to the same row below:

| Class | Characterization |
| --- | --- |
| I | Exponent \(2\), order \(2\) |
| II | Exponent \(2\), order at least \(4\) |
| III | Exponent \(3\), order \(3\) |
| IV | Exponent \(3\), order at least \(9\) |
| V | Exponent \(5\), order \(5\) |
| VI | Exponent \(5\), order at least \(25\), **or any prime exponent \(p\ge7\)** |

The order conditions are exhaustive: a finite group of exponent \(p\), with \(p\) prime, has order a positive power of \(p\).

In particular, \(C_5\times C_5\), \(C_7\), and the nonabelian upper-unitriangular group \(\mathrm{UT}_3(\mathbb F_5)\) all satisfy the **same** counting-free \(\mathrm{FO}^{2}\) sentences. For every odd prime \(p\), \(\mathrm{UT}_3(\mathbb F_p)\equiv_{\mathrm{FO}^{2}} C_p^3\); a three-variable sentence distinguishes each nonabelian example from its abelian counterpart. Among structures in \(\mathcal K\), one-variable logic has exactly two theories, separated by whether the exponent is \(2\) or odd.

## Assumptions and scope

All groups are finite and nontrivial, and the exponent is prime, so every nonidentity element has order exactly that prime. No assumption of commutativity is made. The language consists only of equality, the identity constant, and one ternary graph-of-multiplication relation. Neither binary multiplication as a function nor inverse as a function is part of the language. This signature distinction is essential: a function term may expose arbitrarily many products without additional variable names.

A group in class VI with exponent \(5\) has order at least \(25\). The class VI assertion includes all finite groups of exponent \(p\ge7\), regardless of order or group structure. The statement is **not** an assertion of equivalence in counting logic, in unrestricted ordinary first-order logic, or in more expressive algebraic signatures.

## Proof

**1. Reduction of the atomic two-variable information.** Given assignments to \(x,y\), every atomic formula with terms chosen from \(x,y,1\) and relation \(R\) is equivalent, using the group laws, to a Boolean combination of equalities and the tests
\[
 x=1,\quad y=1,\quad x=y,\quad x^2=1,\quad y^2=1,\quad y=x^2,\quad x=y^2,\quad xy=1.
\]
For example, \(R(x,y,x)\) says \(y=1\), \(R(y,x,y)\) says \(x=1\), \(R(x,x,y)\) says \(y=x^2\), and \(R(x,y,1)\) says \(y=x^{-1}\). Crucially, no atom on these two variable names can compare \(xy\) with \(yx\) as two *distinct* third elements.

**2. Relative types and their availability.** Fix a nonidentity element \(a\) in a group of prime exponent \(p\). The complete atomic two-variable profile of a second element \(b\), relative to \(a\), is determined by whether \(b\) is \(1\), \(a\), \(a^2\), the unique square root \(a^{(p+1)/2}\) when \(p\) is odd, \(a^{-1}\), or none of these. Some types coincide at small primes:

- For \(p=2\), the identity is \(a^2\), the inverse is \(a\), no square root of \(a\) exists, and a different nonidentity \(b\) exists precisely if the group order exceeds \(2\).
- For \(p=3\), the square, square root, and inverse of \(a\) coincide. A further nonidentity \(b\) exists precisely if the group order exceeds \(3\).
- For \(p=5\), the four elements \(a,a^2,a^3,a^4\) are distinct and exhaust the nonidentity elements in \(\langle a\rangle\). An additional \(b\) exists exactly when the group order exceeds \(5\).
- For every prime \(p\ge7\), the four special nonidentity elements \(a,a^2,a^{(p+1)/2},a^{-1}\) are pairwise distinct, and at least one further element already lies in \(\langle a\rangle\).

Thus, for every possible choice of nonidentity anchor \(a\), the *set* of realizable atomic binary profiles depends solely on the six classes displayed in the theorem. It does not depend on the anchor, the multiplication of unrelated elements, or the order of the group beyond the indicated cutoffs. The identity anchor also has the same available profiles in any two groups of the same class.

**3. Permanent two-pebble strategy.** Consider two groups in the same row. Duplicator maintains equality of the full atomic diagrams of the currently occupied zero, one, or two pebble positions, including all occurrences of the named identity. If Spoiler moves one pebble, at most one old element remains fixed. The availability statement in step 2 supplies a response realizing exactly the requested atomic binary profile relative to the remaining anchor. The same statement applies with the two variable positions exchanged. Therefore the invariant persists after every move, without any upper bound on the number of rounds. The ordinary pebble-game characterization yields equivalence for **all** \(\mathrm{FO}^{2}\) sentences, of arbitrary quantifier depth.

**4. Separation of the six classes.** Define the following sentences, using only the variable names \(x,y\):
\[
\begin{aligned}
\alpha &:= \exists x\,[x\ne1\wedge R(x,x,1)],\\
\beta &:= \exists x\exists y\,[x\ne1\wedge y\ne1\wedge x\ne y],\\
\gamma &:= \exists x\exists y\,[x\ne1\wedge R(x,x,y)\wedge R(x,y,1)],\\
\delta &:= \exists x\exists y\,[x\ne1\wedge y\ne1\wedge x\ne y\wedge
 \neg R(x,x,y)\wedge\neg R(y,y,x)\wedge\neg R(x,y,1)].
\end{aligned}
\]
Their truth vectors in the six classes, listed as \((\alpha,\beta,\gamma,\delta)\) with true encoded by \(1\), are
\[
(1,0,0,0),\ (1,1,0,1),\ (0,1,1,0),\ (0,1,1,1),\ (0,1,0,0),\ (0,1,0,1).
\]
All six vectors differ, establishing the converse. In the one-variable language, the only nonidentity atomic distinction is whether its square is the identity; hence the two one-variable classes are exactly even-prime versus odd-prime exponent.

**5. Sharp noncommutativity example.** For odd prime \(p\), take \(H_p=\mathrm{UT}_3(\mathbb F_p)\) represented by triples with multiplication
\[
(a,b,c)(a',b',c')=(a+a',\ b+b',\ c+c'+ab').
\]
The group has order \(p^3\), exponent \(p\), and is nonabelian, while \(C_p^3\) is abelian of the same order and exponent. Both lie in the same two-variable class. The three-variable sentence
\[
\exists x\exists y\exists z\,[R(x,y,z)\wedge\neg R(y,x,z)]
\]
is true in \(H_p\) and false in \(C_p^3\). This proves that **three variables are the least width witnessing noncommutativity for this pair** in the stated relational language.

## Verification

Two Python programs, using only the standard library, are included. Run `python3 verify_prime_exponent.py` and `python3 verify_pebble_bisimulation.py` in the directory containing both programs. The first independently enumerates all two-variable atomic multiplication relations and the four distinguishing sentences on eleven concrete sample groups, including three nonabelian unitriangular groups. The second constructs the exact sets of atomic two-pebble pair profiles reachable by replacing either pebble and checks their closure, with all ordered pairs and all legal replacement targets included. Both programs are deterministic; their recorded stdout is supplied in adjacent files `check_profiles.txt` and `check_bisimulation.txt`.

The finite enumeration is **not** used to extrapolate to infinitely many groups. The general result follows from the algebraic reduction and permanent strategy above; the programs check their premises and small/nonabelian boundary cases independently.

## Relationship to prior work

Gomaa's 2007 dissertation studies finite abelian groups and develops relational-group pebble games; its Chapter 3, especially Sections 3.5–3.9, derives variable and quantifier-depth bounds, and discusses dihedral groups and the general finite-group problem. The exact six-theory classification across **all** prime-exponent groups, its merger of large exponent-five groups with every exponent-at-least-seven group, and the nonabelian examples were not found in the inspected material.

Brachter and Schweitzer, *On the Weisfeiler-Leman Dimension of Finite Groups*, provide an explicit ternary relational multiplication version and compare group WL versions, but their results involve **counting logics and bijective pebble games**, which can distinguish groups by order. Their results do not directly establish the uncounted, two-variable collapse here. The restricted four-class behavior for prime-order cyclic groups is a genuine special case of this six-class classification, not its converse: cyclic groups alone do not determine the classes containing nonabelian groups or the additional elementary-abelian cases.

A specialized earlier analysis of the same uncounted two-variable group fragment could nevertheless subsume this theorem; the comparisons listed are not a proof of priority.

## Limitations

No claim is made for the trivial group, for groups with composite exponent, for function-symbol multiplication, for counting quantifiers, or for \(\mathrm{FO}^{k}\) at \(k\ge3\) beyond the stated noncommutativity separator. The executable checks are finite and do not certify the unrestricted logical result independently. Historical-priority assessment relies on the accessible literature cited below; the full 2010 journal adaptation of the 2007 dissertation was not inspected.

## References

1. W. Gomaa, *Model Theory and Complexity Theory*, PhD dissertation, University of Maryland, public repository record dated 2007-07-06, https://hdl.handle.net/1903/7227. Relevant: Chapter 3, Sections 3.5–3.9. Full lawful text: https://api.drum.lib.umd.edu/server/api/core/bitstreams/5a564fe0-5c19-4da2-8ce0-2cc76964e427/content.
2. W. Gomaa, *Descriptive Complexity of Finite Abelian Groups*, International Journal of Algebra and Computation 20 (2010), 1087–1116, https://doi.org/10.1142/S0218196710006047. Abstract checked; full journal text not inspected.
3. J. Brachter and P. Schweitzer, *On the Weisfeiler-Leman Dimension of Finite Groups*, arXiv:2003.13745, first public 2020-03-30, https://arxiv.org/pdf/2003.13745. Relevant: Sections 2.3 and 3.1–3.4; the inspected full text is version 2, dated November 2021.
