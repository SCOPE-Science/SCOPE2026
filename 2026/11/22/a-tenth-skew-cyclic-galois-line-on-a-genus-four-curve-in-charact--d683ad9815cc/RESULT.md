# A tenth skew cyclic Galois line on a genus-four curve in characteristic five

## Finding

The smooth canonical curve \(C\subset\mathbb P^3_{\mathbb F_5}\) given by
\[
XY-Z^2=0,\qquad X^3+Y^3+W^3=0
\]
has **at least ten distinct geometric skew cyclic Galois lines**. Besides the nine distinct lines whose defining equations and deck transformations occur in the characteristic-zero computation of Komeda and Takahashi, there is an additional \(\mathbb F_5\)-rational skew line
\[
L:\qquad X+Z=0,\qquad Y-Z=0.
\]
Projection from this line induces a degree-six geometrically cyclic Galois function-field extension. The characteristic-zero upper bound of nine for this configuration therefore does not persist unchanged in characteristic five.

## Assumptions and scope

The ground field is \(k=\mathbb F_5\), with \(\omega\in\mathbb F_{25}\) a primitive cube root of unity. The word *cyclic Galois line* means a projective line disjoint from the canonical curve whose induced projection induces a cyclic Galois extension of degree six **over an algebraic closure**. It does not assert that the projection is cyclic Galois over \(\mathbb F_5\). The theorem asserts a lower bound, not an exact total count of all Galois lines.

## Proof

The quadric is parametrized by \(X=S^2,Y=T^2,Z=ST\). Substitution gives the smooth cyclic triple cover
\[
W^3=-(S^6+T^6).
\]
In characteristic five, the binary sextic has six distinct roots because \(5\nmid6\). Its triple cover of \(\mathbb P^1\) is smooth of genus four by Riemann–Hurwitz. The displayed intersection is its canonical model, hence it is a smooth complete intersection of degrees two and three.

Define a linear substitution over \(\mathbb F_{25}\):
\[
\sigma(X,Y,Z,W)=
(2X+2Y+4Z,\ 2X+2Y+Z,\ 2X+3Y,\ \omega W).
\]
Write \(Q=XY-Z^2\) and \(F=X^3+Y^3+W^3\). Direct expansion modulo five gives
\[
Q\circ\sigma=Q,\qquad F\circ\sigma=F+3(X+Y)Q.
\]
Therefore \(\sigma\) restricts to an automorphism of \(C\). Its three-by-three block squares to the identity in characteristic five but is not the identity; its fourth-coordinate multiplier has order three. Thus \(\sigma\) has order six. For the two linear forms \(\ell_1=X+Z\) and \(\ell_2=Y-Z\), direct matrix multiplication yields
\[
\ell_i\circ\sigma=-\ell_i\quad(i=1,2).
\]
Consequently the rational function \(\ell_1/\ell_2\), defining projection from \(L\), is fixed by the order-six group.

The line is skew: on \(L\), set \(X=-Z\), \(Y=Z\). Then \(Q=-2Z^2\) and \(F=W^3\). Over characteristic five the only common affine solution is the zero vector, so \(L\cap C=\varnothing\). Projection from a skew line of a degree-six projective curve has degree six. It is therefore precisely the cyclic order-six Galois quotient.

The nine previously exhibited geometric skew lines are given by the following pairs of linear equations, where \(\omega\) is a primitive third root of unity:

\[
\begin{array}{ll}
X=Y=0;&X+Y=Z=0;\\
X+\omega Y=Z=0;&X+\omega^2Y=Z=0;\\
X-Y=Z=0;&X-\omega Y=Z=0;\\
X-\omega^2Y=Z=0;&X=W=0;\\
Y=W=0.&
\end{array}
\]
Their integral cyclotomic matrix certificates, reproduced in `verify.py`, remain valid in characteristic five and prove degree-six skew cyclic projections there. They are pairwise distinct after reduction: the seventh-root issues do not arise, \(\omega\ne\omega^2\), and all required nonzero skew-intersection coefficients remain nonzero in characteristic five. The new line \(L\) belongs to none of these nine because its direction has all three of \(X,Y,Z\) nonzero and it does not impose \(W=0\). Thus at least ten distinct lines exist.

## Verification

Running `python verify.py` uses exact polynomial arithmetic over \(\mathbb Z[\omega]\) for the original cyclic-line certificates and reduction modulo five for the new automorphism. It checks the quadric and cubic identities, exact order six, invariance of the projection coordinates, skewness, and distinctness from the nine displayed lines. It produces the confirmation `CHAR5 EXTRA SKEW CYCLIC GALOIS CENTER VERIFIED`. The proof of smoothness and the degree-six argument are mathematical, not inferred from enumeration.

## Relationship to prior work

Komeda and Takahashi's 2023 work classifies nine skew cyclic order-six Galois lines on the displayed canonical curve **in characteristic zero** and provides their defining equations. Those nine are prior art, not new. The additional characteristic-five line and the resulting failure of the characteristic-zero nine-line upper bound under reduction are the present assertion. Published calculations of Weil polynomials for the diagonal genus-four family address a different arithmetic invariant.

## Limitations

No claim is made about the *exact* number of skew Galois lines in characteristic five, their complete orbit structure, or their ground-field Galois property. The extra generator requires \(\omega\in\mathbb F_{25}\). Earlier literature may contain a positive-characteristic classification not located in the inspected sources; this remains a priority risk. The proof concerns this concrete curve in characteristic five and not all genus-four curves.

## References

Komeda, J. and Takahashi, T., *Galois lines for a canonical curve of genus 4, II: Skew cyclic lines*, 2023, DOI: 10.4171/RSMUP/141. In particular the two nine-line configurations and the defining equations in the source's classification.
