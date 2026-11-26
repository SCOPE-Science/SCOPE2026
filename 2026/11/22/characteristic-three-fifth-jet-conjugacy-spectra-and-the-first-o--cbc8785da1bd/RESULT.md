# Full conjugacy spectrum of fifth-jet automorphisms in characteristic three

## Finding
Let \(q=3^e\) with \(e\ge1\), let \(k=\mathbb F_q\), and let \(G=\operatorname{Aut}_k(k[t]/(t^6))\). The coefficient-field-fixing automorphisms are the substitutions
\[
f(t)=at+bt^2+ct^3+dt^4+ut^5\pmod {t^6},\qquad a\in k^\times.
\]
Put \(h=q-1\) and \(g=\gcd(4,h)\). Each row below gives the number of conjugacy classes and their common size, for the specified actual multiplier \(a\). Multiplicities add when class sizes coincide.

| Multiplier | Number of classes | Size of each class |
|---|---:|---:|
| \(a=1\) | \(1\) | \(1\) |
| \(a=1\) | \(g\) | \(h/g\) |
| \(a=1\) | \(1\) | \(qh\) |
| \(a=1\) | \(2q\) | \(qh/2\) |
| \(a=1\) | \(q\) | \(q^2h\) |
| \(a=-1\) | \(1\) | \(q^2\) |
| \(a=-1\) | \(g\) | \(q^2h/g\) |
| \(a=-1\) | \(2q\) | \(q^2h/2\) |
| each multiplier of order four | \(1\) | \(q^3\) |
| each multiplier of order four | \(g\) | \(q^3h/g\) |
| each remaining multiplier | \(1\) | \(q^4\) |

There are two order-four multipliers when \(e\) is even and none otherwise. The total class number is \(6q+4\) for odd \(e\) and \(6q+16\) for even \(e\). The group has order \(hq^4\); hence there are \(hq^4k(G)\) ordered commuting pairs and the commuting probability is \(k(G)/(hq^4)\).

As an application of the class table, combining it with the classical first-iterate criterion identifies exactly \(q-1\) full-\(G\) classes of elements of order nine, each of size \(q^2h\). In the multiplier-one subgroup \(U\), the classical condition reduces modulo \(t^6\) to \(b\ne0,\ c\ne b^2\). There are \(q^2(q-1)^2\) such elements by direct coefficient counting, a proportion \((1-1/q)^2\) of \(U\). The iterate criterion and this elementary element count are not asserted as separate new results.

## Assumptions and scope
All counts are over finite fields of characteristic three, and conjugation is in the full group \(G\), not just \(U\) or its prime-field version. Field-semilinear substitutions and longer truncations are outside the classification. The order-nine statement concerns orders **in the finite quotient**, not torsion of an arbitrary infinite power series lifting one of its elements.

## Proof
The multiplier map has kernel \(U\) and is split by the linear substitutions \(t\mapsto\lambda t\). Filter \(U\) by \(U_j=\{f\equiv t\pmod{t^{j+1}}\}\) for \(1\le j\le5\). Its four consecutive quotients are additive copies of \(k\), and conjugation by a linear substitution acts degree by degree with weight \(\lambda^j\) (or all inverse weights, according to convention). In particular the factor \(j\) is central in \(U/U_{j+1}\).

### Multiplier one
For two elements of \(U\) with coefficient tuples \((b,c,d,u),(v,w,z,s)\), commutation reduces by expansion to
\[
v(c-b^2)+b(v^2-w)=0,\qquad b(cv-vw+z)-dv=0.
\]
In particular the group law in degrees two and three is commutative. For \(b\ne0\), after choosing \(v,s\) the equations determine \(w,z\) uniquely. The \(U\)-class size is \(q^2\); since the pair \((b,c)\) is invariant and there are exactly \(q^2\) choices of \((d,u)\), this completely determines a \(U\)-class. The linear multipliers act on \((b,c)\) with weights \((1,2)\), giving a free orbit of length \(h\) for each value of \(c/b^2\). These are the \(q\) classes of size \(q^2h\).

If \(b=0,c\ne0\), the equations force \(v=0\) in the centralizer, giving \(U\)-class size \(q\). A conjugating element with first nonlinear coefficient \(v\) takes \((d,u)\) to \((d-cv,u+dv+cv^2)\) in one of the two conventions. The invariants are \(c\) and \(I=u-d^2/c\), since \(2=-1\) in \(k\); they describe the classes because each such fiber has \(q\) points. Their weights under the torus are \((2,4)\), with stabilizer of order two because \(c\ne0\). This gives \(2q\) classes of size \(qh/2\). If \(b=c=0,d\ne0\), the second centralizer equation forces \(v=0\), and the class of size \(q\) contains all \(u\) for fixed \(d\), as \(d\) is invariant at the leading grade. Cubes act transitively on \(d\ne0\) because \(\gcd(3,h)=1\), giving one class of size \(qh\). Finally \(b=c=d=0\) is central in \(U\); the fourth-power scaling of \(u\) gives the identity singleton and \(g\) classes of size \(h/g\).

### The other multipliers
Let \(\ell_a(t)=at\) for \(a\ne1\). Each \(U\)-orbit in \(U\ell_a\) meets \(U^{\ell_a}\ell_a\): for a degree \(j+1\) with \(a^j\ne1\), conjugation by a suitable element of \(U_j\) removes that coefficient in the \(U\)-factor, leaving earlier degrees unchanged. This works because the change on \(U_j/U_{j+1}\) is multiplication by \(1-a^j\) up to convention, and the fixed subgroup is exactly the subgroup with all nonfixed degrees zero. Now for \(v\in U^{\ell_a}\) the prime-to-three part of \(v\ell_a\) is \(\ell_a\), since \(v\) has three-power order and commutes with \(\ell_a\). Any element of \(U\) taking one such representative to another must therefore centralize \(\ell_a\). In the cases at hand \(U^{\ell_a}\) is abelian. Thus the distinct representatives are the distinct \(v\)'s; each has \(U\)-class size \(q^4/|U^{\ell_a}|\). Full classes then come from the remaining torus action on these representatives.

For \(a=-1\), the fixed subgroup consists of \(t+ct^3+ut^5\) and is abelian (the possible cross term has factor three). The torus acts with weights \((2,4)\), and the three cases \((c,u)=(0,0)\), \(c=0,u\ne0\), and \(c\ne0\) give the three rows for \(-1\). If \(a\) has order four, the fixed subgroup is \(t+ut^5\); its zero orbit and its fourth-power cosets give the two rows. All other nonidentity multipliers have trivial fixed subgroup. Fourth roots of unity occur in number \(\gcd(4,3^e-1)\), so summing the rows gives the two claimed class numbers. In the sum of centralizer sizes over all elements, each class contributes \(|G|\), giving the ordered commuting-pair count.

### Application to the order-nine classes
Rivera-Letelier's normalized first-iterate formula gives, at characteristic three, the coefficient \(1-c\) for \(b=1\). In arbitrary characteristic-three fields the coefficient identity here reads
\[
f^{\circ3}(t)=t+b^2(b^2-c)t^5\pmod {t^6}\qquad (f\in U).
\]
For a direct truncated check, the second iterate has tuple \((B,C,D,U')=(-b,-c-b^2,-d+b^3-bc,-u-b^2c)\) in degrees two through five. Substituting that tuple into \(f\) kills degrees two through four and yields \(b^4-b^2c\) in degree five. This also covers \(b=0\); when nonzero, a pure degree-five jet has order three. In the full-\(G\) class family indexed by \(c/b^2\), every index except one therefore gives an order-nine class. All order-nine elements are in \(U\), since the multiplier group has order prime to three.

## Verification
The bundled `verify.py` in the source package specifies a direct exhaustive composition test of all \(162\) group elements and \(26{,}244\) ordered pairs at \(q=3\), with \(3{,}564\) commuting pairs, and the order criterion for all multiplier-one elements. At \(q=9\) it uses exact extension-field arithmetic and checks centralizer equations for \(52\) representatives, not all ordered pairs. The original captured output is `verification_output.txt`; replay from the source package with `python verify.py` in Python 3. Uniformity is by the proof, not by either finite check.

## Relationship to prior work and limitations
- P. P. Pálfy, *The number of conjugacy classes in some quotients of the Nottingham group*, Proc. Edinburgh Math. Soc. **41** (1998), 369–384, DOI `10.1017/S0013091500019714`, includes class-number information for the prime-field quotient \(U\) studied here. J. Sangroniz, *Conjugacy classes and characters in some quotients of the Nottingham group*, J. Algebra **211** (1999), 26–41, is also relevant to unipotent quotients. Neither the calculation of the prime-field unipotent class number nor application of a torus orbit count as a general technique is claimed as an original contribution.
- J. Rivera-Letelier, *Dynamique des fonctions rationnelles sur des corps locaux*, Astérisque **287** (2003), p. 191, Example 3.19, gives the normalized first-iterate coefficient. Kallal and Kirkpatrick, *Ramification of Wild Automorphisms of Laurent Series Fields*, arXiv:1611.01077, Theorem 1.6 and Proposition 3.9, give the relevant arbitrary-field order-of-first-ramification criterion and coefficient calculation. These results supply the iterate threshold, not the full multiplier-resolved conjugacy analysis. Classifications of torsion of formal series (e.g. S. Jean, *Conjugacy classes of series in positive characteristic and Witt vectors*, J. Théor. Nombres Bordeaux **21** (2009), 263–284, Theorem 5.6) concern infinite formal series rather than the whole finite group considered here.
- The earlier *Conjugacy and centralizer spectra of finite fourth-order substitution groups* gives the analogous full-group kind of spectrum at shorter truncation and characteristic at least five. *Automorphism-orbit spectra of subalgebras in length-six truncated polynomial rings* studies the action on subalgebras, not conjugation of group elements. The claim here is the all-\(q\) multiplier-resolved finite class table in characteristic three, including its parity change, with the exact order-nine full-class count as a consequence. There is no assertion of global priority or of the absence of an implicit broader classification.
