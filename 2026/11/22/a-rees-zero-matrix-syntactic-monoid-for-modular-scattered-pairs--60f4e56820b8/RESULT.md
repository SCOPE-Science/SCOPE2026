# A Rees zero-matrix syntactic monoid for modular scattered pairs with forbidden adjacent ones

## Finding

For every integer \(m\ge2\), define the binary language
\[
L_m=\{w\in\{0,1\}^{*}:\text{the contiguous factor }11\text{ does not occur in }w,\; \binom{w}{01}\equiv0\pmod m\},
\]
where \(\binom{w}{01}\) counts pairs of indices \(i<j\) with \(w_i=0\) and \(w_j=1\); the empty word belongs to \(L_m\). Its syntactic monoid is the external-identity adjunction of the completely zero-simple Rees matrix semigroup
\[
M^0(H_m;\{0,1\},\{0,1\};P),\qquad P=\begin{pmatrix}e&e\\e&\mathbf0\end{pmatrix},
\]
where \(\mathbf0\) denotes a new absorbing zero, \(e=(0,0,0)\), and \(H_m\) is the finite Heisenberg group with carrier \((\mathbb Z/m\mathbb Z)^3\) and multiplication
\[
(z,o,p)\cdot(z',o',p')=(z+z',\ o+o',\ p+p'+zo')\pmod m.
\]
The rows of \(P\) index the last bit of the left factor and the columns index the first bit of the right factor. In particular,
\[
\boxed{|\operatorname{Synt}(L_m)|=4m^3+2.}
\]
For each \(m\ge2\), the nonzero maximal subgroups of the nonidentity ideal are isomorphic to the nonabelian class-two group \(H_m\).

## Assumptions and scope

All words are finite and binary, all counts are of **scattered** (not necessarily consecutive) occurrences, and \(m\) is an arbitrary fixed integer at least two. The forbidden factor `11` is **contiguous**. Two words are syntactically equivalent precisely when they have the same membership under all two-sided contexts \(x(\cdot)y\), with \(x,y\in\{0,1\}^*\). We classify this two-sided syntactic congruence, not merely the right residuals or the state count of a deterministic acceptor. The Rees-semigroup identity is an externally adjoined identity distinct from each internal group identity \(e\).

## Proof

**Step 1: Signature and homomorphism.** For a nonempty word \(w\) avoiding `11`, let \(f(w),\ell(w)\in\{0,1\}\) be its first and last symbols, and let
\[
z(w)=|w|_0\bmod m,\quad o(w)=|w|_1\bmod m,\quad p(w)=\binom{w}{01}\bmod m.
\]
Set \(\sigma(w)=(f(w),z(w),o(w),p(w),\ell(w))\). Map the empty word to \(\mathbf1\), a separate identity; map any word containing `11` to \(\mathbf0\). For two valid nonempty words \(u,v\), the concatenation is invalid exactly when \(\ell(u)=f(v)=1\). Otherwise
\[
p(uv)=p(u)+p(v)+z(u)o(v)\pmod m
\]
and the first and last bits are \(f(u)\) and \(\ell(v)\). Thus \(\sigma\) is a homomorphism onto a submonoid of the displayed identity-adjoined Rees matrix semigroup, with multiplication
\[
(f,h,\ell)(f',h',\ell')=\begin{cases}(f,hh',\ell')&P_{\ell,f'}=e,\\\mathbf0&P_{\ell,f'}=\mathbf0.\end{cases}
\]
The semigroup zero is reached by `11`.

**Step 2: Every nonzero group signature with either boundary occurs.** Fix first bit \(f\), last bit \(\ell\), and arbitrary residues \((z,o,p)\in H_m\). Choose an integer \(O\ge3\) congruent to \(o\pmod m\). For a valid word with exactly \(O\) ones, let \(g_i\) denote its number of zeros between the \(i\)-th and \((i+1)\)-st one, with \(g_0\) preceding the first one and \(g_O\) following the last. The constraints are
\[
g_i\ge1\ (1\le i\le O-1),\quad
(g_0=0\text{ if }f=1;\ g_0\ge1\text{ if }f=0),\quad
(g_O=0\text{ if }\ell=1;\ g_O\ge1\text{ if }\ell=0),
\]
and
\[
|w|_0=\sum_{i=0}^{O}g_i,\qquad\binom{w}{01}=\sum_{i=0}^{O-1}(O-i)g_i.
\]
Choose a sufficiently large integer \(Z\equiv z\pmod m\) so that, after satisfying the minimum gaps, at least \(m-1\) additional zeros remain. There are always two consecutive *allowed* gap coordinates: choose \((g_{O-1},g_O)\) when \(\ell=0\); otherwise choose \((g_0,g_1)\) when \(f=0\); otherwise choose \((g_1,g_2)\) (possible since \(O\ge3\)). Their coefficients in the scattered-pair sum differ by one. Place exactly \(m-1\) of the additional zeros in these two gaps, with \(t\) of them in the first and \(m-1-t\) in the second, and place all remaining excess zeros at a fixed allowed gap independently of \(t\). As \(t\) runs from zero to \(m-1\), the pair-count residues run through every element of \(\mathbb Z/m\mathbb Z\). Thus the target \(p\) is realized with the prescribed first and last bits and \((z,o)\). Surjectivity follows: all \(4m^3\) nonzero normal forms, the identity and the absorbing zero occur.

**Step 3: Every two distinct normal forms are syntactically separable.** An absorbing-zero word is rejected after every two-sided context. Every valid nonzero word can be made accepted in some two-sided context: surround it with valid words whose chosen first and last symbols make both joins legal, then select the right context's \(p\)-coordinate so that the total scattered-pair residue is zero. This uses Step 2.

For valid nonempty words with **different first bits**, choose a left context ending in `1` and a right context starting in `0`. The word beginning in `1` is rejected because a crossing `11` appears, whereas for the word beginning in `0` the group coordinate of the right context can be chosen to force acceptance. For **different last bits**, use a left context ending in `0` and a right context starting in `1` and make the word ending in `0` accepted. In both cases the opposite word crosses a forbidden `11` boundary.

Now suppose two distinct normal forms have the same first and last bits and group coordinates \((z,o,p)\ne(z',o',p')\). Select left context \(x\) ending in `0` and right context \(y\) starting in `0`; both joins are therefore legal. Their resulting pair-count difference is
\[
\Delta=p-p'+z(x)(o-o')+(z-z')o(y)\pmod m.
\]
If \(p-p'\ne0\), set \(z(x)=o(y)=0\). Otherwise, if \(o-o'\ne0\), set \(z(x)=1,o(y)=0\). Otherwise set \(z(x)=0,o(y)=1\). In each case \(\Delta\ne0\pmod m\). Step 2 allows all chosen context group coordinates; adjust \(p(y)\) to accept the first word while rejecting the second. Notice that no division in \(\mathbb Z/m\mathbb Z\) is used, so the argument includes composite moduli.

It remains to distinguish the empty word \(\varepsilon\), mapped to \(\mathbf1\), from a nonempty valid word \(w\). If \(f(w)=1\), choose a left context ending in `1` and right context beginning in `0`: \(xwy\) is invalid but \(xy\) is valid, and its pair residue can be made zero. If \(f(w)=0,\ell(w)=1\), use \(x\) ending in `0` and \(y\) beginning in `1`, again making \(xy\) accepted while \(xwy\) contains `11`. If \(f(w)=\ell(w)=0\), use \(x\) ending in `1` and \(y\) beginning in `1`: \(xy\) is invalid, while \(xwy\) is valid and can be made accepted. Thus identity is not syntactically equivalent to any other normal form.

**Step 4: Exactness of the quotient.** Step 1 shows equal normal forms have identical behavior in every two-sided context, and Steps 2–3 show all normal forms are attained and pairwise distinguishable. The kernel of \(\sigma\) is therefore the syntactic congruence. There are \(4|H_m|=4m^3\) nonzero forms, one absorbing zero and one external identity. The matrix \(P\) has no all-zero row or column, so its Rees semigroup ideal is completely zero-simple. Finally, exchanging the group elements \((1,0,0)\) and \((0,1,0)\) changes the third coordinate by one, proving noncommutativity for every \(m\ge2\).

## Verification

The standalone `check_rees.py` builds, for each modulus \(m\in\{2,3,4,5,6,7\}\), a completely independent modular counting DFA, enumerates its entire transition monoid by breadth-first traversal, and compares each transformation with its signature under multiplication. It obtains exactly 34, 110, 258, 502, 866 and 1374 transformations, respectively, agreeing with \(4m^3+2\). All 8191 words of lengths zero through twelve are also checked against a direct quadratic-time scattered-pair count for each of the six moduli (49,146 word/modulus tests). The derived automata have respectively 9, 19, 33, 51, 73 and 99 states including the sink. The exhaustive finite checks support, but cannot replace, the general proof. To reproduce: `python3 check_rees.py` using Python 3 without third-party dependencies.

## Relationship to prior work

Lejeune, Rigo and Rosenfeld (2020) relate unrestricted \(2\)-binomial word equivalence to free class-two nilpotent groups; their studied quotients retain **integer** scattered-subsequence statistics and do not impose `11`-avoidance or identify the syntactic monoid of a modular residue language. The current proof uses a finite modular Heisenberg group in a **Rees zero-matrix extension** with one boundary-forbidden sandwich entry, and proves a two-sided syntactic equality rather than recognition by some finite monoid. Adámek, Milius and Urbat (2018) provide general syntactic congruence theory, not this exact family. Bourne and Ruškuc (2016) study **contiguous** factor-counting languages and Rees zero-matrix semigroups **over abelian groups**, with different aims (generalized star height), rather than this scattered-pair nonabelian syntactic classification. Search comparisons did not identify a theorem implying the displayed formula; this is a best-knowledge literature assessment, not a proof of historical uniqueness.

## Limitations

This result concerns syntactic **monoid size and structure**; it does not assert a novel exact minimum number of states for a DFA, a noise-tolerant decoder, nor the same formula for any other forbidden factor, longer scattered pattern, or different acceptance residue. The finite experiment covers only six moduli. Published equivalences not captured by accessible indexed sources may exist. Independent expert validation has not been performed.

## References

1. Marie Lejeune, Michel Rigo, Matthieu Rosenfeld, *On the binomial equivalence classes of finite words*, arXiv:2001.11732, first public 31 January 2020. https://arxiv.org/abs/2001.11732
2. Jiří Adámek, Stefan Milius, Henning Urbat, *A Categorical Approach to Syntactic Monoids*, arXiv:1804.03011 (2018). https://arxiv.org/abs/1804.03011
3. Tom Bourne, Nik Ruškuc, *On the star-height of factor counting languages and their relationship to Rees zero-matrix semigroups*, arXiv:1603.06236 (2016). https://arxiv.org/abs/1603.06236
