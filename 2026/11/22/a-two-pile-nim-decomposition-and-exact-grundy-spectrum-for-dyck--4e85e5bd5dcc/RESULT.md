# A two-pile Nim decomposition and exact Grundy spectrum for Dyck-end word subtraction

## Finding

Fix the alphabet \(\Sigma=\{a,b\}\) and let \(\mathcal D\) be the language of Dyck words (including the empty word), with \(a\) as an opening and \(b\) as a closing parenthesis. Consider the impartial normal-play game on all finite words: a move deletes **either** a nonempty Dyck prefix **or** a nonempty Dyck suffix. The game has the following complete solution.

A *primitive Dyck word* is a nonempty Dyck word with no proper nonempty Dyck prefix. Every Dyck word uniquely factors into primitive Dyck words. If \(w\in\mathcal D\) has \(k\) primitive components, then its Sprague–Grundy value is \(G(w)=k\). Every \(w\notin\mathcal D\) has a unique factorization

\[
w=u\,c\,v,
\]

where \(u\) is its longest Dyck prefix, \(v\) is its longest Dyck suffix, and \(c\ne\varepsilon\) has neither a nonempty Dyck prefix nor a nonempty Dyck suffix. If \(u\) and \(v\) have \(k\) and \(\ell\) primitive components, respectively, then

\[
\boxed{G(w)=k\mathbin{\mathrm{xor}}\ell.}
\]

Consequently the losing positions are exactly the empty word together with the non-Dyck words whose longest Dyck prefix and suffix contain equally many primitive components. The losing-position language is not regular.

Write

\[
p(z)=\frac{1-\sqrt{1-4z^2}}2,\qquad
q(z)=\frac{(1-p(z))^2}{1-2z}-(1-p(z)).
\]

For each fixed integer \(g\ge0\), let \(M\) be the smallest power of two strictly greater than \(g\); let \(A_{n,g}\) count length-\(n\) binary words with Grundy value \(g\). The complete exact length distribution at that value is the algebraic series

\[
\boxed{\sum_{n\ge0} A_{n,g}z^n
=p(z)^g+q(z)\frac{\displaystyle\sum_{r=0}^{M-1}p(z)^{r+(r\mathbin{\mathrm{xor}}g)}}{1-p(z)^{2M}}.}
\]

In particular, the number \(L_n=A_{n,0}\) of losing positions satisfies

\[
\boxed{\sum_{n\ge0} L_n z^n
=\frac{1-2zp(z)}{(1-2z)(1+p(z))}.}
\]

For a uniformly random word \(W_n\in\Sigma^n\), \(G(W_n)\) converges in distribution to \(K\mathbin{\mathrm{xor}}J\), where \(K,J\) are independent and have \(\Pr(K=k)=\Pr(J=k)=2^{-k-1}\) for \(k\ge0\). Thus

\[
\boxed{\lim_{n\to\infty}\Pr(G(W_n)=0)=\frac13},
\]

and, more precisely,

\[
\Pr(G(W_n)=0)=\frac13+\frac{4\sqrt2}{9\sqrt{\pi n}}+O(n^{-1}).
\]

The limiting masses at values \(0,1,2,3\) are respectively \(1/3,4/15,8/51,32/255\).

## Assumptions and scope

A Dyck word has equally many \(a\)'s and \(b\)'s, and in every prefix the excess of \(a\)'s over \(b\)'s is nonnegative. Both end-removal move sets are precisely \(\mathcal D\setminus\{\varepsilon\}\); no other removal is allowed. The game uses normal play, not misère play. The empty word is terminal. Words are finite, the alphabet consists of exactly one parenthesis type, and all positions of all lengths are included. A nonempty Dyck prefix or suffix is allowed to equal the whole word. All generating functions are ordinary formal power series in length, using \(z\) per letter; exponents \(k,\ell,g,r\) are nonnegative integers.

## Proof

**1. Nonoverlap and uniqueness of the core.** Define the balance path \(h_0=0\) and \(h_i=\#_a(w_1\cdots w_i)-\#_b(w_1\cdots w_i)\). Suppose a Dyck prefix ends at position \(i\) and a Dyck suffix starts just after position \(j\), where \(j\le i\). Put \(H=h_{|w|}\). We have \(h_j=H\), since the suffix is balanced, and \(h_i=0\). Because the prefix is Dyck, \(h_j\ge0\); because the suffix is Dyck, \(h_i\ge H\). Hence \(0\le H\le0\). The prefix stays above height zero until \(i\), and the suffix stays above height zero from \(j\) through the end. Thus the entire word is Dyck. Contrapositively, if \(w\notin\mathcal D\), its longest Dyck prefix and suffix are disjoint. Between them lies a nonempty core \(c\). If \(c\) had a nonempty Dyck prefix, it would extend the chosen longest prefix; if it had a nonempty Dyck suffix, it would extend the chosen longest suffix. Conversely, for any nonempty core without either such end and any Dyck words \(u,v\), no Dyck prefix of \(ucv\) can extend past \(u\): if the prefix of \(cv\) reached zero while respecting nonnegative balances, then \(c\) would itself admit a Dyck prefix (or, if \(c\) stayed strictly positive, appending Dyck \(v\) could not bring it back to zero). The symmetric argument holds at the right end. Hence \(ucv\) is non-Dyck, and \(u,c,v\) is a unique, unrestricted combinatorial decomposition.

**2. Game isomorphism.** For a non-Dyck word, every removable Dyck prefix is a concatenation of the first \(j\) primitive components of \(u\), with \(1\le j\le k\); every removable Dyck suffix is a concatenation of the last \(j\) components of \(v\), with \(1\le j\le\ell\). After either move, the core and opposite end are unchanged, and maximality of the surviving Dyck ends persists by the uniqueness result. Therefore the option graph of \(w\) is isomorphic to the disjunctive sum of two ordinary Nim heaps of sizes \(k\) and \(\ell\). Its Grundy value is their bitwise exclusive-or. If the word itself is Dyck, every legal removal takes one or more complete primitive components from one end; the possible remaining component counts are exactly \(0,\ldots,k-1\), proving \(G(w)=\operatorname{mex}\{0,\ldots,k-1\}=k\). For \(k=0\), the empty word has value zero.

**3. Exact counting.** Let \(P\) denote the language of nonempty primitive Dyck words. A primitive is \(aDb\) with \(D\in\mathcal D\), so its generating series is \(p=z^2/(1-p)\), yielding \(p(z)=(1-\sqrt{1-4z^2})/2\). The Dyck language \(\mathcal D=P^*\) has series \(1/(1-p)\). Let \(q\) enumerate the nonempty cores from step 1. The unique disjoint decomposition of all words into \(\mathcal D\) and \(\mathcal D\,C\,\mathcal D\) gives

\[
\frac1{1-2z}=\frac1{1-p}+\frac{q}{(1-p)^2},
\]

which proves the stated expression for \(q\). Words with \(k,\ell\) end components have series \(q p^{k+\ell}\), while Dyck words with \(g\) components have series \(p^g\). For the fixed nimber \(g\), choose a power of two \(M>g\). The solutions of \(k\mathbin{\mathrm{xor}}\ell=g\) are exactly

\[
k=tM+r,\qquad \ell=tM+(r\mathbin{\mathrm{xor}}g),\quad t\ge0,\ 0\le r<M.
\]

This partitions all pairs because exclusive-or by \(g\) leaves all binary digits at positions at least \(\log_2 M\) unchanged. Summing \(q p^{k+\ell}\) gives the claimed finite-numerator series for each \(g\). For \(g=0\), the sum is \(1/(1-p^2)\); algebra gives \(1+q/(1-p^2)=(1-2zp)/((1-2z)(1+p))\).

**4. Nonregularity.** Intersect the losing-position language with the regular language \((ab)^*b(ab)^*\). A word \((ab)^k b(ab)^\ell\) has longest Dyck prefix \((ab)^k\) and longest Dyck suffix \((ab)^\ell\); its isolated core is \(b\). Therefore the intersection is exactly \(\{(ab)^k b(ab)^k:k\ge0\}\), which is not regular by the pumping lemma. Hence the full losing language is not regular.

**5. Random limit and correction.** At the dominant positive singularity \(z=1/2\), \(p(z)\to1/2\) and

\[
q(z)p(z)^{k+\ell}\sim\frac{2^{-k-\ell-2}}{1-2z}
\]

for each fixed \(k,\ell\). The other singularity at \(z=-1/2\) is of weaker square-root type. Coefficient transfer implies that the probability of a length-\(n\) non-Dyck word with exactly \(k,\ell\) end components tends to \(2^{-k-\ell-2}\). These probabilities sum to one, yielding convergence of the joint end counts to independent geometric variables and hence the asserted xor limit. For the loss probability, put \(\epsilon=1-2z\); then

\[
\frac{1-2zp(z)}{(1-2z)(1+p(z))}
=\frac1{3\epsilon}+\frac{4\sqrt2}{9}\epsilon^{-1/2}+O(1)
\]

as \(z\to1/2\) in a slit neighborhood. Standard square-root coefficient transfer, including the smaller singular contribution from \(z=-1/2\), gives the stated \(n^{-1/2}\) correction with an \(O(n^{-1})\) remainder. The first four limit masses follow by summing the geometric weights over the finite xor residue blocks in the formula from step 3.

## Verification

The package includes two independent Python 3 scripts. Run `python3 verify_game.py` and `python3 verify_series.py` in the same directory. The first uses an independent recursive mex definition and checks all \(262143\) words through length \(17\) against the end-component formula, including the separation of the nonempty core. The second uses an independently implemented recursive mex and formal power-series arithmetic: it matches all Grundy coefficients against direct enumeration through length \(14\), proves sum-to-total coefficient checks through length \(60\), and checks sixteen finite XOR-block identities. The output from their current replay is saved as `verification_output.txt`. These finite checks corroborate, but do not replace, the all-length proof above.

## Relationship to prior work

Inoue and Inazu, *Word Subtraction Games*, arXiv:2611.09157v1 (first public version November 6, 2026), define two-sided prefix/suffix removal in Section 5.1 and analyze the Timber and End-Nim examples. Their Dyck language appears as the losing language for the **different** rule permitting removal of a prefix ending in \(a\) or suffix beginning in \(b\). It does not give the same-context-free-language end-removal game, the two-pile decomposition, exact Grundy spectrum, or asymptotic law proved here.

Albert and Nowakowski, *The Game of End-Nim* (2001), study reduction of the two end piles in a sequence of heaps. That game may expose new piles and has different move dynamics; the present Dyck-core is invariant under play and gives a separate two-heap structure. Established Catalan enumeration, primitive excursions, and the standard xor law for impartial sums are used as ingredients, not claimed as new.

## Limitations

The game is fixed to the one-type Dyck language on two symbols with identical legal prefix and suffix sets. The result does not classify arbitrary context-free move languages or end-removal rules. The random limit is for uniform fixed-length binary words, not Dyck-conditioned words. The probability correction is asymptotic rather than a simple formula for every finite \(n\). Equivalence to an unindexed earlier specialization has not been conclusively excluded. No independent mathematical audit has been performed.

## References

1. Y. Inoue and H. Inazu, *Word Subtraction Games*, arXiv:2611.09157v1, November 6, 2026. https://arxiv.org/html/2611.09157v1
2. M. H. Albert and R. J. Nowakowski, *The Game of End-Nim*, Electronic Journal of Combinatorics 8(2), R1 (2001). https://doi.org/10.37236/1600
3. G. Cairns and N. B. Ho, *Some Remarks on End-Nim*, International Journal of Combinatorics 2011, 824742 (2011). https://doi.org/10.1155/2011/824742
