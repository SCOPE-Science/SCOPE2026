# Singer-line and dyadic-depth classification of three-pinned cylinders for primitive linear cellular automata

## Finding

For any primitive irreducible binary local polynomial, the exact finite-time image index of *every* cylinder fixing three input sites is decided by two operations: comparison of the site residues on a multiplicative Singer cycle, and the dyadic orders of their pairwise distances. The greatest possible time until a triple becomes unrestricted has a sharp cutoff governed by the least span of a trinomial divisible by that polynomial.

Let \(D_n\) be the binary logarithm of the image index at time \(n\). For the conventions below, the complete formula is

\[
D_n=\begin{cases}
\mathbf1_{\{n\le H_-\}}+\mathbf1_{\{n\le H_+\}},&a\equiv b\equiv c\pmod q,\\
\mathbf1_{\{n\le H_{uv}\}},&\text{exactly }u,v\text{ share a residue mod }q,\\
\mathbf1_{\{n\le H_-\}},&\text{all residues distinct and }\alpha^a+\alpha^b+\alpha^c=0,\\
0,&\text{otherwise}.
\end{cases}
\]

In particular the index is always \(1\), \(2\), or \(4\), independent of the pinned bit assignment, and the all-equal-residue case has two strict successive drops. Define the natural trinomial-span invariant

\[
m(P)=\min\bigl\{v\ge2:\exists u\in\{1,\ldots,v-1\},\ P(z)\mid 1+z^u+z^v\bigr\}.
\]

Then \(d\le m(P)<2^d-1\), and for any integer \(L\ge2\), the sharp worst-case first time \(T_{\max}(L)\) at which a three-pin cylinder of span at most \(L\) has full image is

\[
T_{\max}(L)=\begin{cases}
1,&L<m(P),\\
1+2^{\lfloor\log_2(L/m(P))\rfloor},&L\ge m(P).
\end{cases}
\]

For the primitive cubic \(P(z)=1+z+z^3\), the Singer line is \(\{0,1,3\}\) modulo seven and \(m(P)=3\). Thus \(\{0,1,2\}\) is unrestricted already at time one, while \(\{0,1,3\}\) first becomes unrestricted at time two, and \(\{0,2,6\}\) at time three. For \(P(z)=1+z+z^2+z^3+z^5\) the corresponding least trinomial span is \(8\), witnessed by \(1+z^3+z^8\).

## Assumptions and scope

Work on the bilateral compact group \(X=(\mathbb F_2)^{\mathbb Z}\). Let \(P(z)=\sum_{j=0}^d p_jz^j\) be monic primitive irreducible of degree \(d\ge3\), so \(p_0=p_d=1\). The cellular automaton is \((F_Px)_i=\sum_{j=0}^d p_jx_{i+j}\pmod2\). Put \(q=2^d-1\); a root \(\alpha\in\mathbb F_{2^d}\) has multiplicative order \(q\). The condition \(\alpha^a+\alpha^b+\alpha^c=0\) does not depend on choosing another conjugate primitive root of \(P\).

Fix integers \(a<b<c\) (possibly negative) and any bits \(v_a,v_b,v_c\). The associated cylinder is \(C=\{x:x_a=v_a,\ x_b=v_b,\ x_c=v_c\}\). For positive integer \(n\), the image \(F_P^n(C)\) is closed, with finite group index interpreted as the index of the linear image \(F_P^n(H)\) for \(H=\{x:x_a=x_b=x_c=0\}\). Define \(H_{uv}=2^{\nu_2(v-u)}\), \(H_-=\min(H_{ab},H_{bc},H_{ac})\), and \(H_+=\max(H_{ab},H_{bc},H_{ac})\). The first full-reachability time of a cylinder is the least integer \(n\ge1\) with \(F_P^n(C)=X\), not the time-zero cylinder.

## Proof

**1. Dual image-index formula.** Identify finite binary characters of \(X\) with Laurent polynomials \(\mathbb F_2[z,z^{-1}]\): \(z^i\) evaluates the \(i\)-th coordinate. The dual of \(F_P\) multiplies by \(P(z)\). Since this Laurent ring is a domain, \(F_P\) is surjective. The annihilator of \(H\) is the three-dimensional subspace \(V=\operatorname{span}_{\mathbb F_2}\{z^a,z^b,z^c\}\). A character \(\chi\) annihilates \(F_P^n(H)\) precisely when \(P^n\chi\in V\); multiplication by \(P^n\) identifies the annihilator with \(V\cap(P^n)\). Consequently

\[
D_n=\dim_{\mathbb F_2}\bigl(V\cap P^n\mathbb F_2[z,z^{-1}]\bigr).
\]

Any assignment produces a translation of \(F_P^n(H)\), so the index does not depend on the three pinned bits. The seven nonzero elements of \(V\) are three monomials, three pair sums, and the triple sum.

**2. Roots and their exact multiplicities.** Monomials are units in the Laurent ring, so none is divisible by \(P\). For a pair \(u<v\), the polynomial \(z^u+z^v=z^u(1+z^{v-u})\) is divisible by \(P\) if and only if \(q\mid(v-u)\). Because \(q\) is odd, if \(v-u=2^s r\) with \(r\) odd and divisible by \(q\), then \(1+z^{v-u}=(1+z^r)^{2^s}\); the factor \(P\) occurs in \(1+z^r\) with multiplicity exactly one, since the derivative \(rz^{r-1}\) is a nonzero monomial in characteristic two. Thus the exact \(P\)-adic multiplicity of an eligible pair is \(H_{uv}=2^s\).

The triple \(z^a+z^b+z^c\) is divisible by \(P\) exactly when \(\alpha^a+\alpha^b+\alpha^c=0\). A triple with two equal residues cannot have zero evaluation; with all three equal, its evaluation is the nonzero common power. Thus eligible triples have three distinct residues. If \(u=b-a\), \(v=c-a\), and \(s=\min\{\nu_2(u),\nu_2(v)\}\), remove the monomial factor \(z^a\) and use

\[
1+z^u+z^v=\bigl(1+z^{u/2^s}+z^{v/2^s}\bigr)^{2^s}.
\]

At least one of the reduced exponents is odd. The derivative of the parenthesized polynomial is nonzero at \(\alpha\): if exactly one exponent is odd, it is a monomial; if both are odd, its vanishing would imply \(\alpha^{u/2^s}=\alpha^{v/2^s}\), contradicting the distinct original residues, because the power \(2^s\) is invertible modulo odd \(q\). Therefore the eligible triple has exact multiplicity \(2^s=H_-\), since \(\nu_2(c-b)=\nu_2(v-u)\) is no smaller than \(s\).

**3. Ranks of the relation subspaces.** When all residues coincide, the three pair sums are precisely the three nonzero elements of the two-dimensional even-parity subspace of \(V\). The three corresponding valuations have exactly two equal minimal values and one strictly larger value (the two-adic ultrametric property). For \(n\le H_-\), all three pairs survive, giving dimension two. For \(H_-<n\le H_+\), exactly the unique longest-lived pair survives, giving dimension one, and thereafter no relation survives. When exactly two residues coincide, the unique eligible pair spans the relation subspace until its multiplicity threshold. When all residues differ, no pair survives; the triple alone survives up to \(H_-\) precisely on a Singer line. This proves all cases of the index formula.

**4. Existence of the sharp span parameter.** Because \(\alpha\) generates \(\mathbb F_{2^d}^{\times}\), the nonzero element \(1+\alpha\) equals \(\alpha^v\) for some \(2\le v\le q-1\). Therefore \(P\mid 1+z+z^v\); this proves \(m(P)<q\). Irreducibility implies \(m(P)\ge d\). For a three-site relation with exact multiplicity \(h=2^s\), if it is a pair, its gap is a multiple of \(q h\), and hence its span is at least \(m(P)h\). If it is a triple, divide the two site differences from \(a\) by \(h\): the displayed Frobenius identity and the fact that field squaring is an automorphism show that the reduced trinomial remains divisible by \(P\); its span is at least \(m(P)\). Thus every nonzero image obstruction surviving through time \(n\) requires original span at least \(m(P)\) times its dyadic survival depth. If \(L<m(P)\), every cylinder becomes unrestricted after a single update. Otherwise the longest possible survival depth is at most the largest power of two not exceeding \(L/m(P)\).

Choose \(u<m(P)\) attaining the minimum in the definition of \(m(P)\). The trinomial \(1+z^u+z^{m(P)}\) has no common factor \(2\) in its two positive exponents, since dividing both by two would yield, by Frobenius, a shorter divisible trinomial. Its exact multiplicity is therefore one, by Step 2. For \(h=2^{\lfloor\log_2(L/m(P))\rfloor}\), the scaled triple \(\{0,hu,hm(P)\}\) spans at most \(L\) and has a relation of exact multiplicity \(h\). Hence its first full-reachability time is \(h+1\), attaining the upper bound.

## Verification

The standalone Python-standard-library checker `check_singer.py` independently computes the predicted dyadic/Singer index, the number of divisible character polynomials among the seven nonzero three-site masks, and the nullity of the coordinate evaluation map on the recurrence kernel of \(P^n\). The three methods agree in 207,628 exact comparisons for the primitive polynomials \(1+z+z^3\) and \(1+z+z^2+z^3+z^5\). For both, it additionally checks the sharp span cutoff for every integer \(2\le L\le32\), with exact witnesses. To reproduce from the package, run `python3 check_singer.py`. Computation checks finitely many degrees, locations and times; the universal theorem is established by the preceding proof.

## Relationship to prior work

Castronuovo, Dennunzio, Kari and Margara [1] investigate group cellular automata through topological entropy, one-sided space-time traces, duality and characteristic polynomials. The present work studies a different invariant: exact finite-time spatial images of three-site cylinders, including an explicit global worst-case cutoff. Dennunzio, Formenti, Grinberg and Margara [2] establish qualitative transitivity and ergodicity statements for additive cellular automata, including a cylinder-return characterization (their Lemma 18). These qualitative statements do not give the three-site image index or the Singer-line/dyadic filtration. Elementary finite-field facts about primitive polynomials and the binary projective Singer line are used as standard input; novelty is not asserted for those facts alone. A dedicated historical priority comparison remains appropriate.

## Limitations

The result is restricted to primitive irreducible local polynomials over \(\mathbb F_2\) and three pinned sites. It does not classify reducible polynomials, arbitrary higher-cardinality patterns, temporal observation traces, or finite cyclic lattices. Computing \(m(P)\) may itself require arithmetic work for large degrees. The exact analytic theorem does not rely on the finite checker; no independent mathematical audit has been performed. The comparison with earlier literature does not establish an exhaustive historical-priority claim.

## References

1. N. Castronuovo, A. Dennunzio, J. Kari and L. Margara, *Topological Entropy of Group Cellular Automata is Effectively Computable*, arXiv:2611.16746, first public version 12 November 2026. https://arxiv.org/abs/2611.16746
2. A. Dennunzio, E. Formenti, D. Grinberg and L. Margara, *Additive Cellular Automata Over Finite Abelian Groups: Topological and Measure Theoretic Properties*, MFCS 2019, Article 68, DOI:10.4230/LIPIcs.MFCS.2019.68. https://drops.dagstuhl.de/storage/00lipics/lipics-vol138-mfcs2019/LIPIcs.MFCS.2019.68/LIPIcs.MFCS.2019.68.pdf
