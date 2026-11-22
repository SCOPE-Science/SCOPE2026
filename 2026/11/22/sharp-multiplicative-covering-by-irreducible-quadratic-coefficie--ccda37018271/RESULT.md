# Sharp multiplicative covering by irreducible quadratic coefficients at fixed nonsquare norm

## Finding

For every odd prime power \(q\) and every quadratic nonsquare \(c\in\mathbb F_q^\times\), define
\[
A_c=\{b\in\mathbb F_q^\times:X^2+bX+c\text{ is irreducible over }\mathbb F_q\}.
\]
The exact twofold multiplicative image is
\[
\boxed{A_c A_c=\begin{cases}\mathbb F_q^\times,&q\equiv3\pmod4,\\\mathbb F_q^\times\setminus\{4c,-4c\},&q\equiv1\pmod4.\end{cases}}
\]
Moreover, if \(q\equiv1\pmod4\), then \(A_c^3=\mathbb F_q^\times\) for \(q>5\), while \(|A_c^3|=2\) for \(q=5\). Thus the nonzero irreducibility-admissible linear coefficients form a two-step multiplicative covering set in one congruence class; in the other they miss exactly two prescribed products, and three steps are optimal except for the unique field of order five.

## Assumptions and scope

The field \(\mathbb F_q\) has odd order; no primality assumption on \(q\) is made. The fixed constant term \(c\) is a nonzero quadratic nonsquare. This includes every primitive element, since primitive elements are nonsquares in an odd-order finite field. The coefficients entering the product set are required to be nonzero, even when \(X^2+c\) itself is irreducible. Products \(A_c^j\) use exactly \(j\) factors and are taken in \(\mathbb F_q^\times\). The symbol \(\chi\) denotes the quadratic character, with \(\chi(0)=0\).

## Proof

**Step 1: character count.** Put \(d=4c\), a nonsquare, and \(\epsilon=\chi(-1)\). A monic quadratic \(X^2+bX+c\) is irreducible precisely when its discriminant \(b^2-d\) is a nonsquare. Because \(d\) is a nonsquare, this discriminant never vanishes. The classical identity \(\sum_{b\in\mathbb F_q}\chi(b^2-d)=-1\) implies that the number of such coefficients, allowing zero, is \((q+1)/2\). At zero the character is \(\chi(-d)=-\epsilon\). Consequently
\[
|A_c|=\begin{cases}(q+1)/2,&\epsilon=-1,\\(q-1)/2,&\epsilon=1.\end{cases}
\]
For completeness, the character-sum identity follows by counting pairs \((b,z)\) with \(z^2=b^2-d\): the nonzero-product equation \((b-z)(b+z)=d\) has exactly \(q-1\) solutions, so \(q+\sum_b\chi(b^2-d)=q-1\).

**Step 2: the case \(q\equiv3\pmod4\).** The multiplicative group has \(q-1\) elements, whereas \(|A_c|=(q+1)/2>(q-1)/2\). For each \(t\ne0\), the sets \(A_c\) and \(tA_c^{-1}\) must intersect by pigeonhole, yielding \(t\in A_cA_c\).

**Step 3: two explicit obstructions when \(q\equiv1\pmod4\).** Now \(\chi(-d)=-1\), and \(|A_c|=(q-1)/2\). For \(t=\pm d\), any \(b\ne0\) and \(b'=t/b\) obey
\[
(b')^2-d=-\frac{d}{b^2}(b^2-d).
\]
The multiplier \(-d/b^2\) is a nonsquare. Thus the two discriminants have opposite quadratic characters, and \(t\notin A_cA_c\). The elements \(d\) and \(-d\) are distinct because the characteristic is odd.

**Step 4: no other obstruction.** Fix \(t\in\mathbb F_q^\times\) with \(t\ne\pm d\) and suppose \(t\notin A_cA_c\). The disjoint sets \(A_c\) and \(tA_c^{-1}\) both have size \((q-1)/2\), hence partition \(\mathbb F_q^\times\). Since neither discriminant vanishes, for every \(x\ne0\) the characters \(\chi(x^2-d)\) and \(\chi((t/x)^2-d)\) are opposite. Accordingly
\[
\chi((x^2-d)(t^2-dx^2))=-1\qquad(x\ne0).
\]
The same identity holds at \(x=0\), because \(\chi(-dt^2)=-1\). The smooth projective curve
\[
\mathcal C_t:\quad y^2=(x^2-d)(t^2-dx^2)
\]
therefore has no affine rational points. Its defining quartic has four distinct roots over an algebraic closure: \(d\ne0\), \(t\ne0\), and \(t^2\ne d^2\). Hence \(\mathcal C_t\) is a smooth genus-one curve. Its leading coefficient \(-d\) is a nonsquare, so its two geometric points at infinity are not rational over \(\mathbb F_q\). Thus \(\#\mathcal C_t(\mathbb F_q)=0\), contradicting the Hasse–Weil bound
\[
\#\mathcal C_t(\mathbb F_q)\ge q+1-2\sqrt q=(\sqrt q-1)^2>0.
\]
The bound is valid for any smooth projective genus-one curve over a finite field, regardless of whether a rational base point has previously been chosen. This proves the twofold formula for every odd prime power, including small fields.

**Step 5: sharp threefold covering.** In the case \(q\equiv1\pmod4\), Step 4 shows \(|A_c^2|=q-3\) and Step 1 shows \(|A_c|=(q-1)/2\). If \(q>5\), then \(q-3+(q-1)/2>q-1\), so \(A_c^2\cap tA_c^{-1}\ne\varnothing\) for every \(t\ne0\). Hence \(A_c^3=\mathbb F_q^\times\). For \(q=5\) the set \(A_c\) contains two opposite elements, so its third power contains exactly two elements. This also proves minimality of three factors when \(q\equiv1\pmod4\) and \(q>5\).

## Verification

Run `python3 VERIFY.py` with Python 3 and the standard library. The checker directly constructs coefficient sets and their twofold and threefold products, comparing them with the exact predicted images for 44 prime fields and five quadratic extension fields of orders \(9,25,49,121,169\). It tests 411 distinct nonsquare constants. The recorded result was `VERIFY_OK field_cases= 49 nonsquare_constants= 411`. This is finite corroboration, not a substitute for the genus-one argument, which establishes the theorem for all odd prime powers.

## Relationship to prior work

Zhu and Wu (2026) investigate primitive quadratic polynomials \(X^2+bX+c\) with a fixed primitive constant and derive coefficientwise criteria and counts. That work motivates studying the multiplicative structure of the admissible coefficient set, but a count of admissible coefficients does not imply its exact twofold products. Earlier work on irreducible even quartic trinomials establishes simultaneous irreducibility at prescribed ratios of *constant terms*, governed by elliptic curves; it does not determine products of linear coefficients for a fixed quadratic constant. Related counts for paired compositional quartics concern a different family. The present argument uses classical discriminant identities and Hasse–Weil, but the structural image classification is the claimed new part.

## Limitations

The hypothesis that \(c\) is a nonsquare is essential to the argument and the stated formula. Zero coefficients are omitted from products. Characteristic two and higher-degree irreducible-polynomial families are not classified. The exact product images are established mathematically; no statement about multiplicative independence, primitive polynomial frequency, or factorization algorithms follows. The possibility of implicit coverage in older general finite-field character-set or sum-product literature remains a scientific priority risk. Independent validation has not been performed.

## References

1. Li Zhu and Hongfeng Wu, *The Optimal Coefficients-Based Criterion for Primitive Quadratic Polynomials over Finite Fields*, arXiv:2608.01327v1, first public 2026-08-02. https://arxiv.org/abs/2608.01327
2. Classical quadratic discriminant criterion, quadratic character sum for a nonzero quadratic shift, and Hasse–Weil bound for smooth genus-one curves over finite fields (standard results used with all relevant normalizations specified in the proof).
