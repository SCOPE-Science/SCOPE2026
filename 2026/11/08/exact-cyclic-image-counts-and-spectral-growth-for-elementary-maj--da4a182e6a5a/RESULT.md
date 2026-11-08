# Exact cyclic image counts and spectral growth for elementary majority cellular automaton Rule 232

## Finding

For each integer \(n\ge1\), let \(F_n:\{0,1\}^n\to\{0,1\}^n\) be the simultaneous update on *indexed cyclic configurations*
\[
(F_n(x))_i=\mathbf1\{x_{i-1}+x_i+x_{i+1}\ge2\},\qquad i\in\mathbb Z/n\mathbb Z.
\]
Indices are interpreted modulo \(n\), including repeated neighbor positions for \(n=1,2\). Put \(a_n=|\operatorname{im}F_n|\). Define
\[
D(z)=(1+z^3-z^5)(1-2z+z^3-z^5).
\]
Then, as a formal power series over the rational numbers,
\[
\boxed{\sum_{n\ge1}a_n z^n=-\frac{zD'(z)}{D(z)}.}
\]
Equivalently, if \(\alpha_1,\ldots,\alpha_5\) are the complex roots, with multiplicity, of \(X^5+X^2-1\) and \(\beta_1,\ldots,\beta_5\) those of \(X^5-2X^4+X^2-1\), then
\[
\boxed{a_n=\sum_{j=1}^5(\alpha_j^n+\beta_j^n)\qquad(n\ge1).}
\]
The first values are \(2,4,2,8,22,34,58,96,182,334,596,1046\). The unique root \(\lambda\in(1.78,1.79)\) of \(X^5-2X^4+X^2-1\) is larger in modulus than all nine other roots. Consequently,
\[
a_n=\lambda^n+O(1.5^n),\qquad \lambda=1.784598933\ldots,
\]
and the exponential information rate of the one-step output set is \(\log_2\lambda=0.835599882\ldots\) bits per cell. These are *one-step image counts*, not counts of fixed points, attractors, or time-periodic orbits.

## Assumptions and scope

The alphabet is binary; configurations are ordered and individually indexed, so spatial rotations are **not** identified. The update is exactly the usual elementary majority rule (Wolfram Rule 232), with periodic boundary conditions. For \(n=1\) and \(n=2\), the three local inputs are the values at the residues \(i-1,i,i+1\) even when residues repeat. No probabilistic initial-state assumption is used. Formal generating functions are expanded at \(z=0\).

## Proof

**1. A closed-path representation.** Number the pairs \(00,01,10,11\) by \(0,1,2,3\). For each output letter \(b\in\{0,1\}\), define a \(4\times4\) Boolean matrix \(M_b\). Its entry \(((a,c),(c,d))\) is one precisely when the input triple \((a,c,d)\) has majority \(b\), and all other entries vanish. Rows and columns are ordered by the pair numbers. Thus the matrices, in row-major bit encoding with bit \(4i+j\) for entry \((i,j)\), are \(M_0=323\) and \(M_1=49792\). Boolean multiplication uses disjunction for addition and conjunction for multiplication.

For any indexed cyclic output word \(y_0\cdots y_{n-1}\), a cyclic input predecessor exists if and only if \(M_{y_0}M_{y_1}\cdots M_{y_{n-1}}\) has a nonzero diagonal entry. Indeed, a diagonal closed path of length \(n\) in the pair de Bruijn graph gives compatible cyclic input triples, and conversely. This equivalence also handles \(n=1,2\): the closed-path condition enforces the repeated cyclic indices.

**2. A finite deterministic exact-count certificate.** Let \(I\) be the Boolean identity relation and \(\mathcal S\) the least set of Boolean \(4\times4\) relations containing \(I\) and closed under right multiplication by \(M_0,M_1\). An exhaustive breadth-first closure, constructed from these two matrices in `verify_transfer.py` (without importing any state table), gives exactly \(120\) distinct relations. Number them by breadth-first discovery starting from \(I\). Define \(T\) as the integer \(120\times120\) transition-count matrix: \(T_{s,t}\) is the number of letters \(b\in\{0,1\}\) for which \(sM_b=t\). Let \(u\) be the row vector supported at the identity state \(s=0\), and \(f\) the column vector with \(f_s=1\) exactly when relation \(s\) has a nonzero diagonal. In total, \(75\) states have this property. Determinism and the preceding closed-path equivalence give
\[
 a_n=uT^nf\quad(n\ge1).
\]

The same finite closure verifies the **integer vector identity**
\[
\bigl(T^{10}-2T^9+2T^7-2T^6-2T^5+3T^4-2T^2+I\bigr)f=-9e_0,
\]
where \(e_0\) is the column unit vector at the identity state. No transition leads *into* that state, so \(Te_0=0\). Thus after multiplication by \(uT^n\) the displayed identity gives, for every \(n\ge1\),
\[
 a_{n+10}-2a_{n+9}+2a_{n+7}-2a_{n+6}-2a_{n+5}
 +3a_{n+4}-2a_{n+2}+a_n=0.
\]
The certificate independently returns the exact initial values
\[
(a_1,\ldots,a_{10})=(2,4,2,8,22,34,58,96,182,334).
\]
The script specifies every finite operation, checks the exact state count, the complete vector identity (not just ten output values), and the lack of transitions into the identity state. The finite identity therefore proves the stated *infinite* recurrence rather than extrapolating finite enumeration.

**3. Generating function and spectral form.** Direct polynomial multiplication yields
\[
D(z)=1-2z+2z^3-2z^4-2z^5+3z^6-2z^8+z^{10}.
\]
The recurrence in Step 2, together with its ten initial values, uniquely fixes the formal series \(\sum_{n\ge1}a_nz^n\). Those ten initial values are precisely the first ten coefficients of \(-zD'(z)/D(z)\), and the latter series satisfies the same recurrence for all terms from index eleven. Hence the generating-function identity is exact. Factoring \(D(z)\) into reciprocal quintics and taking the logarithmic derivative proves the stated ten-root formula by the formal identity \(-z\frac{d}{dz}\log(1-\gamma z)=\sum_{n\ge1}\gamma^n z^n\).

**4. Dominant root.** The polynomial \(q(X)=X^5-2X^4+X^2-1\) has a real root \(\lambda\in(1.78,1.79)\) by direct substitution; its derivative is positive for \(X\ge1.5\), so it is the only real root in that region. Divide by \(X-\lambda\):
\[
q(X)/(X-\lambda)=X^4+(\lambda-2)X^3+\lambda(\lambda-2)X^2+
[1+\lambda^2(\lambda-2)]X+\lambda[1+\lambda^2(\lambda-2)].
\]
For \(1.78<\lambda<1.79\), the absolute values of these four lower-degree coefficients are bounded respectively by \(0.22,0.394,0.33,0.6\). On \(|X|=1.5\), their total contribution is less than \(0.22(1.5)^3+0.394(1.5)^2+0.33(1.5)+0.563<2.8<(1.5)^4\). Rouché's theorem therefore puts all four other roots of \(q\) inside \(|X|<1.5\). If \(X^5+X^2-1=0\) and \(|X|\ge1.5\), then \(|X|^5\le1+|X|^2\), a contradiction; all five roots of that factor also lie inside \(|X|<1.5\). The root-power formula now gives \(a_n=\lambda^n+O(1.5^n)\) and the information-rate conclusion.

## Verification

The standalone file `verify_transfer.py` builds all states, validates exactly \(120\) reachable relations and \(75\) accepting relations, and checks the degree-ten vector-polynomial identity with integer arithmetic. The standalone file `verify_direct.py` independently applies the three-bit majority rule to all binary cyclic inputs through length \(16\) and compares all distinct outputs to the formal-series recurrence. Both scripts use only the Python standard library and were run from their final artifact paths. Their successful results are recorded in `VERIFICATION.md`. The direct checks validate finite instances but are not used to infer the all-length theorem; the finite algebraic identity is the step proving the recurrence for arbitrary \(n\).

## Relationship to prior work

Wolfram (1983) treats elementary cellular automata. Jen (1989, Section 4, Case e, and its Appendix) derives detailed **preimage multiplicities for an arbitrary specified output string** under Rule 232. This is closely related, but it does not state the exact number of *distinct indexed cyclic outputs summed over all words of each length* or the two-quintic logarithmic-derivative expression. Jen (1988) addresses **time-periodic attractors and fixed points on cylinders**, not all one-step image words. Li (1987) studies the regular-language **spatial spectra of attractors**; it is a different observational set. A published online cellular-automaton census tabulates finite-length orphan counts for the elementary rules, including information about forward enumeration, but a finite census is not the all-length formula. The distinction between counting closed de Bruijn paths with multiplicity and counting distinct cycle labels is essential here: Boolean relations remove duplicate predecessors before counting outputs.

## Limitations

The theorem counts indexed one-step image words on binary rings. It does not describe the distribution of inverse-fiber sizes, the asymptotic attractor set, multistep images, or nonperiodic input boundaries. The two programs constitute reproducible finite exact certificates and cross-checks, not independent human validation. The accessible text of Jen (1988) was restricted to the abstract, leaving a limited historical-priority risk for any unpublished results on one-step images, although the published abstract describes different invariants. The earlier finite census covers numerical lengths without the proved general formula. There is no claim of priority beyond the consulted sources.

## References

1. S. Wolfram, "Statistical mechanics of cellular automata", *Reviews of Modern Physics* 55 (1983), 601–644, https://doi.org/10.1103/RevModPhys.55.601 . Published 1983-07-01.
2. E. Jen, "Enumeration of preimages in cellular automata", *Complex Systems* 3 (1989), 421–456, https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf , especially pp. 441–442 on Rule 232.
3. E. Jen, "Cylindrical cellular automata", *Communications in Mathematical Physics* 118 (1988), 569–590, https://doi.org/10.1007/BF01221109 .
4. W. Li, "Power spectra of regular languages and cellular automata", *Complex Systems* 1 (1987), 107–130, https://wpmedia.wolfram.com/uploads/sites/13/2018/02/01-1-8.pdf .
5. *Elementary CA Zoo*, "Gardens of Eden", https://cellular.solves.ca/gardens-of-eden , consulted 2026-11-04; finite cyclic orphan census rather than an all-length theorem.
