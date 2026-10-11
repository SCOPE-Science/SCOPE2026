# Finite-cylinder approximation makes Bernoulli Schreier fractional chromatic numbers right-c.e.

## Finding

Let \(\Gamma\) be a countably infinite group equipped with an effective presentation in which multiplication, inversion, and equality are decidable, let \(F\subseteq\Gamma\) be finite, and let \(G=G(\operatorname{Free}(2^\Gamma),F)\) be the Schreier graph of the free part of the Bernoulli shift. Fix a computable increasing exhaustion
\[
D_0\subseteq D_1\subseteq\cdots\subseteq \Gamma,\qquad \bigcup_sD_s=\Gamma .
\]
For finite \(D\subseteq\Gamma\), define
\[
\rho(D):=\max_{\Phi\subseteq 2^D}
\left\{\frac{|\Phi|}{2^{|D|}}:
I(D,\Phi)\text{ is independent}\right\},
\]
where
\[
I(D,\Phi):=\{x\in 2^\Gamma:x|_D\in\Phi\}.
\]
Then
\[
\rho(D_s)\nearrow \alpha_\beta(G)
\]
and hence
\[
\chi_B^*(G)=\frac{1}{\alpha_\beta(G)}
=\inf_s\frac{1}{\rho(D_s)},
\]
with the convention that stages with \(\rho(D_s)=0\) are ignored.

In particular, \(\chi_B^*(G)\) is a right-computably-enumerable real, uniformly from the effective presentation of \(\Gamma\) and the finite set \(F\). Equivalently, there is a computable nonincreasing sequence of rational numbers converging to \(\chi_B^*(G)\).

## Assumptions and scope

The Bernoulli shift is
\[
(\gamma\cdot x)(\delta)=x(\delta\gamma)
\]
on \(2^\Gamma\), with product measure \(\beta\). The graph \(G(\operatorname{Free}(2^\Gamma),F)\) joins \(x\) and \(y\) when \(y=\sigma\cdot x\) for some \(\sigma\in F\cup F^{-1}\), with loops discarded. Since \(\Gamma\) is countably infinite, the free part has \(\beta\)-measure \(1\).

The effectiveness assumption is intentionally modest: a computable presentation with decidable equality is enough. A finitely generated group with decidable word problem is a standard special case. No complexity bound is asserted for the finite maximizations defining \(\rho(D)\).

## Proof

Bernshteyn proves two facts used here. First,
\[
\chi_B^*(G)=\frac{1}{\alpha_\beta(G)}.
\]
Second, for every real \(a<\alpha_\beta(G)\), there is a clopen independent set \(I\subseteq 2^\Gamma\) with \(\beta(I)>a\). Every clopen subset of \(2^\Gamma\) depends on finitely many coordinates, so it has the form \(I(D,\Phi)\) for some finite \(D\subseteq\Gamma\) and \(\Phi\subseteq 2^D\).

It follows immediately that
\[
\sup_D\rho(D)=\alpha_\beta(G).
\]
Indeed, every \(I(D,\Phi)\) counted by \(\rho(D)\) is measurable and independent, so \(\rho(D)\leq\alpha_\beta(G)\). Conversely, given \(a<\alpha_\beta(G)\), Bernshteyn's clopen approximation lemma provides an independent cylinder \(I(D,\Phi)\) of measure greater than \(a\), so \(\rho(D)>a\).

If \(D\subseteq E\), an independent cylinder based on \(D\) can be rewritten on \(E\) by taking all extensions of its accepted \(D\)-patterns. Its measure is unchanged. Therefore
\[
\rho(D_s)\leq \rho(D_{s+1}).
\]
Because the exhaustion eventually contains the finite support of every clopen cylinder,
\[
\lim_s\rho(D_s)=\alpha_\beta(G).
\]
Taking reciprocals gives the displayed formula for \(\chi_B^*(G)\).

It remains to verify effectiveness. For fixed finite \(D\) and \(\Phi\subseteq2^D\), independence is decidable by a finite consistency check. For \(\sigma\in F\) and \(p,q\in\Phi\), the cylinders \(C_p\) and \(\sigma C_q\) intersect exactly when the two finite assignments
\[
x(d)=p(d)\quad(d\in D)
\]
and
\[
x(e\sigma^{-1})=q(e)\quad(e\in D)
\]
agree wherever their coordinate sets overlap. Decidable equality in \(\Gamma\) makes this a finite decidable test. Hence one can enumerate all \(\Phi\subseteq2^D\) and compute \(\rho(D)\) exactly as a rational number.

The maximum degree of \(G\) is at most \(2|F|\), so the standard finite-degree Borel coloring bound gives
\[
\chi_B^*(G)\leq 2|F|+1.
\]
Thus
\[
u_s:=\min\!\left(2|F|+1,\,
\begin{cases}
1/\rho(D_s),&\rho(D_s)>0,\\
2|F|+1,&\rho(D_s)=0
\end{cases}\right)
\]
is a computable nonincreasing rational sequence converging to \(\chi_B^*(G)\). This is exactly right-computable enumerability.

## Verification

The accompanying script `artifacts/verify.py` independently constructs the finite cylinder-conflict problem for \(\Gamma=\mathbb Z\) and \(F=\{1\}\). For consecutive supports of lengths \(1,\ldots,6\), it computes exact maximum accepted-pattern counts
\[
0,1,2,6,12,27,
\]
hence densities
\[
0,\frac14,\frac14,\frac38,\frac38,\frac{27}{64}.
\]
It also checks that the densities are nondecreasing and that every accepted family is genuinely shift-independent by direct finite assignment consistency. These finite checks illustrate the effective stage computation; they are not used as evidence for the infinite convergence theorem, which is proved above from the clopen approximation lemma.

## Relationship to prior work

Bernshteyn's Theorem 1.1 identifies the Borel fractional chromatic number of a Bernoulli Schreier graph with the reciprocal of its measurable independence number, and Lemma 2.2 proves approximation of that independence number by clopen independent sets. The same proof explicitly represents a clopen independent set by a finite coordinate set \(D\) and a family \(\Phi\subseteq2^D\).

The present observation extracts the effective consequence of those ingredients: after choosing a computable exhaustion of a group with decidable equality, the infinite Borel invariant is the limit of an explicit monotone sequence of finite rational optimization problems, and therefore is right-c.e. Searches for this computability formulation, including the phrases "right-c.e. Borel fractional chromatic number", "computable Borel fractional chromatic number", and "finite cylinder approximation Bernoulli Schreier", did not locate a prior statement.

Meehan introduced and studied fractional Borel chromatic numbers before Bernshteyn's result, but the inspected thesis material concerns definable fractional coloring itself rather than this one-sided computability consequence.

## Limitations

No polynomial-time or primitive-recursive complexity bound is claimed for computing \(\rho(D)\); the naive search over all \(\Phi\subseteq2^D\) is doubly exponential in \(|D|\). The theorem gives only right-c.e. computability. It does not show that \(\chi_B^*(G)\) is computable, algebraic, or left-c.e., and it does not address groups whose equality problem is undecidable in the chosen presentation.

The countably infinite hypothesis is used so that the Bernoulli shift is free almost everywhere, as in the cited theorem. The argument concerns the free-part Schreier graph of the Bernoulli \(2\)-shift and does not automatically transfer to arbitrary graphings.

## References

Anton Bernshteyn, *Borel fractional colorings of Schreier graphs*, Annales Henri Lebesgue 5 (2022), 1151–1160, DOI 10.5802/ahl.145, arXiv:2105.11557. First public arXiv version: 2021-05-24.

Connor G. W. Meehan, *Definable Combinatorics of Graphs and Equivalence Relations*, Ph.D. thesis, California Institute of Technology, 2018, DOI 10.7907/45E4-MC27.
