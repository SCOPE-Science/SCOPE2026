# Characteristic-three fifth-jet conjugacy spectra and the first order-nine Nottingham stratum

## Finding
Let \(q=3^e\), where \(e\ge1\), and let \(G=\operatorname{Aut}_{\mathbb F_q}(\mathbb F_q[t]/(t^6))\) be the coefficient-field-fixing automorphism group. Every element is uniquely a substitution
\[
f(t)=at+bt^2+ct^3+dt^4+ut^5\pmod{t^6},\qquad a\ne0.
\]
Write \(h=q-1\), \(g=\gcd(4,h)\in\{2,4\}\), and \(\delta=1\) if \(g=4\), otherwise \(\delta=0\). In each row of the table, the second entry is the **number of conjugacy classes** and the third is their **common class size**. If distinct rows have the same size their multiplicities are combined.

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
| every remaining \(a\ne1\) | \(1\) | \(q^4\) |

There are exactly two multipliers of order four if \(e\) is even, and none if \(e\) is odd. The final row excludes \(1,-1\), and those two roots. Hence \(|G|=hq^4\), and
\[
\boxed{k(G)=\begin{cases}6q+4,&e\text{ odd},\\6q+16,&e\text{ even}.\end{cases}}
\]
The ordered commuting-pair count is \(hq^4 k(G)\), and the commuting probability is \(k(G)/(hq^4)\).

For its multiplier-one subgroup \(U\), the precise first order-nine stratum is
\[
\boxed{\{f\in U:\operatorname{ord}(f)=9\}=\{f:b\ne0,\ c\ne b^2\},\qquad |\{f\in U:\operatorname{ord}(f)=9\}|=q^2(q-1)^2.}
\]
Exactly \(q-1\) full-\(G\) conjugacy classes consist of order-nine elements. The proportion of such elements in \(U\) is \((1-1/q)^2\), tending to one as \(e\to\infty\).

## Assumptions and scope
The field is of characteristic exactly three and may be any extension of \(\mathbb F_3\). Conjugation occurs in the full finite group \(G\), not just its normal Nottingham subgroup \(U\) of substitutions with linear coefficient one. Multipliers lie in \(\mathbb F_q^\times\), not in the automorphism group of the coefficient field. Each row is indexed by the actual multiplier of an element; multiple distinct order-four multipliers are separate cases. The classical quotient \(U\) and the full torus extension are distinct conjugacy problems.

## Proof
**1. Filtration and multiplier action.** For \(1\le j\le4\), let \(U_j\) be the substitutions \(t+\sum_{i\ge j+1}x_i t^i\pmod{t^6}\), with \(U_5=1\). The filtration has one additive factor \(U_j/U_{j+1}\cong(k,+)\) per index \(j\). The linear substitution \(t\mapsto \lambda t\) acts on factor \(j\) with weight \(\lambda^j\) or its inverse, depending on conjugation convention; they have the same stabilizers. Thus \(G=U\rtimes k^\times\), \(|U|=q^4\).

**2. Multiplier-one classes.** For two substitutions in \(U\), write their coefficients as \((b,c,d,u)\) and \((v,w,z,s)\), respectively. Direct expansion of the difference of their compositions modulo \(t^6\) yields the only nontrivial coefficient equations
\[
v(c-b^2)+b(v^2-w)=0,\qquad b(cv-vw+z)-dv=0.
\]
If \(b\ne0\), the variables \(w,z\) are uniquely determined by \(v\), while \(s\) is free. The centralizer in \(U\) therefore has \(q^2\) elements and the \(U\)-class size is \(q^2\). The coefficients \(b,c\) are invariant under conjugation in \(U\), and there are exactly \(q^2\) choices of the remaining pair \((d,u)\); hence each \((b,c)\), \(b\ne0\), is one \(U\)-orbit. The multiplier torus scales \((b,c)\) with weights \((1,2)\), leaving exactly \(q\) orbits, indexed by \(c/b^2\). Their full-\(G\) class sizes are \(q^2h\).

If \(b=0,c\ne0\), the equations force \(v=0\) and leave \(w,z,s\) free, so every \(U\)-class has size \(q\). Direct conjugation takes the pair \((d,u)\) to \((d-cv,u+dv+cv^2)\), where \(v\in k\); the expression \(I=u-d^2/c\) is invariant (because \(2=-1\) in characteristic three). Thus the \(U\)-classes are indexed exactly by \((c,I)\), with \(c\ne0\). Torus weights are \((2,4)\), producing \(2q\) full classes of size \(qh/2\).

If \(b=c=0,d\ne0\), the second equation forces \(v=0\), so one \(U\)-orbit has all \(q\) values of \(u\) for each fixed \(d\). The torus scales \(d\) by the third power. Since \(\gcd(3,q-1)=1\), these give one full class of size \(qh\). If \(b=c=d=0\), all \(q\) elements \(t+ut^5\) are central in \(U\), while the torus scales \(u\) by fourth powers: the identity is a singleton, and \(g\) further classes have size \(h/g\). These cases exhaust the multiplier-one coset and contribute \(3q+2+g\) classes.

**3. A fixed-representative lemma for other multipliers.** Fix \(a\in k^\times\setminus\{1\}\), and let \(\tau_a\) be conjugation by the linear substitution \(t\mapsto at\) on \(U\). In the coset \(U\tau_a\), every \(U\)-conjugacy orbit meets the fixed subgroup \(U^{\tau_a}\). Indeed, eliminate each nonfixed degree-\(j+1\) coefficient successively by conjugation in \(U_j\); whenever \(a^j\ne1\), the change is multiplication by the invertible scalar \(1-a^j\). The remaining coefficients are precisely the resonant fixed degrees, because the fixed-point equation for \(\tau_a\) is coefficientwise. Moreover, if two fixed representatives \(v\tau_a,w\tau_a\) are conjugate by \(x\in U\), their equality \(xv\tau_a=w\tau_a x\) implies inductively that every nonfixed coefficient of \(x\) vanishes: at the lowest nonfixed degree, the commutator terms of already fixed lower degrees cannot contribute there. Thus \(x\in U^{\tau_a}\). In each case below this fixed subgroup is abelian, hence \(v=w\). The same filtration induction shows its centralizer in \(U\) has order \(|U^{\tau_a}|\). Thus a fixed representative has a \(U\)-orbit of size \(q^4/|U^{\tau_a}|\), and the full conjugacy classes are exactly the residual torus orbits on \(U^{\tau_a}\).

For \(a=-1\), the fixed subgroup is the two-parameter group of odd substitutions \(t+ct^3+ut^5\). It is abelian, because the possible cross term \(3cc't^5\) vanishes in characteristic three. Torus weights on \((c,u)\) are \((2,4)\). The zero pair gives one class of size \(q^2\); \(c=0,u\ne0\) gives \(g\) classes of size \(q^2h/g\); \(c\ne0\) gives \(2q\) classes of size \(q^2h/2\).

If \(a\) has order four, the fixed subgroup is the one-dimensional additive group \(t+ut^5\). Its zero element gives one class of size \(q^3\), and the nonzero fourth-power cosets give \(g\) classes of size \(q^3h/g\). For all other \(a\ne1\), the fixed subgroup is trivial, so the entire multiplier fiber is one class of size \(q^4\). These are the remaining table rows. Summing the rows gives \(6q+4\) when \(g=2\) and \(6q+16\) when \(g=4\). The class-count identity for ordered commuting pairs yields the stated probability.

**4. The order-nine threshold.** For \(f=t+bt^2+ct^3+dt^4+ut^5\), direct triple composition in characteristic three gives
\[
f^{\circ3}(t)=t+b^2(b^2-c)t^5\pmod{t^6}.
\]
Every substitution \(t+\alpha t^5\) has cube equal to the identity modulo \(t^6\). Thus \(f\) has order nine precisely when \(b\ne0,c\ne b^2\). The free coefficients \(d,u\) supply \(q^2(q-1)^2\) elements. Within the \(b\ne0\) classes from Step 2 the invariant \(c/b^2\) ranges over \(k\); exactly one value yields order three, and the other \(q-1\) values yield order nine.

## Verification
The standalone `verify.py` uses exact finite arithmetic with no external packages. Over \(\mathbb F_3\), it enumerates all \(162\) group elements and all \(26,244\) ordered pairs directly by truncated composition, recovers the complete multiplier-resolved class-size table, checks \(3,564\) commuting ordered pairs, and verifies the order-nine criterion on every unipotent element. Over \(\mathbb F_9=\mathbb F_3[i]\) with \(i^2=-1\), it checks \(52\) representatives through independently implemented coefficient-by-coefficient centralizer equations, covering multiplier types and sample resonant strata; the predicted group class count is \(70\). Run `python verify.py` from a Python 3 environment. These are finite tests only; uniform conclusions rely on the proof.

## Relationship to prior work
Pálfy's *The number of conjugacy classes in some quotients of the Nottingham group* computes class numbers and centralizers in **unipotent Nottingham quotients**, not the full torus extension above; its theorem covers the prime-field quotient size relevant to the unipotent part, so no unconditional novelty is claimed for that part. The separate previous result *Conjugacy and centralizer spectra of finite fourth-order substitution groups* covers full substitutions only modulo \(t^5\) and in characteristic at least five. A published study of subalgebra orbits in \(k[t]/(t^6)\) concerns the action on subalgebras, not conjugation on \(G\) itself. The contribution here is the full characteristic-three multiplier-resolved fifth-jet conjugacy classification, including the extension-degree parity jump, together with its exact order-nine strata.

## Limitations
The theorem does not cover other characteristics, field-semilinear substitutions, or longer truncations. The full-group conjugacy problem may be implicitly encompassed by general solvable algebraic-group or filtered-group orbit theory; explicit universal priority is not asserted. Only the finite fields of orders three and nine were computationally checked. The archived Nottingham literature proves unipotent results and is not displaced by the present classification.

## References
1. P. P. Pálfy, *The number of conjugacy classes in some quotients of the Nottingham group*, *Proc. Edinburgh Math. Soc.* **41** (1998), 369–384, DOI:10.1017/S0013091500019714. Its publicly verified online release is dated 2009-01-20, and its full mathematical text was inspected.
2. J. Sangroniz, *Conjugacy classes and characters in some quotients of the Nottingham group*, *Journal of Algebra* **211** (1999), 26–41, DOI:10.1006/jabr.1998.7588.
3. *Conjugacy and centralizer spectra of finite fourth-order substitution groups*, public published-finding corpus record 2026-10-25, identifier `21c11f1d-c6ee-4d6a-b885-f124f6655cd6`.
4. *Automorphism-orbit spectra of subalgebras in length-six truncated polynomial rings*, public published-finding corpus record 2026-10-13, public path `2026/10/13/SCOPE-automorphism-orbit-spectra-of-subalgebras-in-length-six-truncate--64aff8a15920`.
