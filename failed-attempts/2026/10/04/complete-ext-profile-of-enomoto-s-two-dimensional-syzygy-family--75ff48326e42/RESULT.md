# Complete Ext profile of Enomoto's two-dimensional syzygy family
## Finding
Let \(k\) be an algebraically closed field, let \(q,\lambda,\mu\in k^\times\), and let \(\Lambda(q)\) and \(U_\lambda\) be the algebra and two-dimensional right module introduced by Enomoto. Then, for every integer \(r\ge 0\),

\[
\dim_k\operatorname{Ext}^{2r}_{\Lambda(q)}(U_\lambda,U_\mu)
=
\dim_k\operatorname{Ext}^{2r+1}_{\Lambda(q)}(U_\lambda,U_\mu)
=
\begin{cases}
1,&\mu=q^r\lambda,\\
0,&\mu\ne q^r\lambda.
\end{cases}
\]

Thus, when \(q\) has infinite multiplicative order, \(U_\lambda\) is a nonprojective nonperiodic module whose entire self-Ext algebra is

\[
\operatorname{Ext}^*_{\Lambda(q)}(U_\lambda,U_\lambda)
\cong k[\varepsilon]/(\varepsilon^2),
\qquad \deg\varepsilon=1.
\]

When \(q\) has finite multiplicative order \(m\), the module \(U_\lambda\) has exact period \(2m\), and its self-Ext groups are one-dimensional precisely in degrees congruent to \(0\) or \(1\pmod{2m}\).

## Assumptions and scope
The field \(k\) is algebraically closed, and \(q,\lambda,\mu\) are nonzero. Enomoto defines \(U_\lambda\) on one-dimensional spaces at vertices \(1\) and \(2\), with \(\alpha_1\) acting by multiplication by \(\lambda\), \(\beta_1\) acting by \(1\), and every other arrow acting by zero. The result concerns only this explicit family of modules over the explicit algebra \(\Lambda(q)\).

## Proof
Enomoto proves an exact minimal sequence

\[
0\longrightarrow U_{q\lambda}\longrightarrow P_2
\xrightarrow{\,h_\lambda\,}P_1
\longrightarrow U_\lambda\longrightarrow0,
\]

where \(h_\lambda\) is left multiplication by \(\alpha_1-\lambda\beta_1\), and identifies the second syzygy as \(\Omega^2(U_\lambda)\cong U_{q\lambda}\). Splicing this sequence with the corresponding sequence for \(U_{q\lambda}\), then iterating, gives a minimal projective resolution whose even projectives are \(P_1\) and whose odd projectives are \(P_2\). The differential \(P_2\to P_1\) in the block indexed by \(r\) is left multiplication by

\[
\alpha_1-q^r\lambda\beta_1.
\]

The intervening differential \(P_1\to P_2\) sends \(e_1\) to the element

\[
\beta_2\beta_3+q^{r+1}\lambda\alpha_2\alpha_3.
\]

Because \(U_\mu e_1\) and \(U_\mu e_2\) are each one-dimensional, both \(\operatorname{Hom}(P_1,U_\mu)\) and \(\operatorname{Hom}(P_2,U_\mu)\) identify with \(k\). Under these identifications, applying \(\operatorname{Hom}_{\Lambda(q)}(-,U_\mu)\) gives the cochain complex

\[
k\xrightarrow{\,\mu-\lambda\,}k\xrightarrow{0}k
\xrightarrow{\,\mu-q\lambda\,}k\xrightarrow{0}k
\xrightarrow{\,\mu-q^2\lambda\,}k\xrightarrow{0}\cdots .
\]

Indeed, on \(U_\mu\) one has \(u_1\alpha_1=\mu u_2\) and \(u_1\beta_1=u_2\), so the odd projective differential induces multiplication by \(\mu-q^r\lambda\). The other cochain differential is zero because every path of length two acts as zero on \(U_\mu\). Taking cohomology yields the displayed Ext formula.

For self-extensions, set \(\mu=\lambda\). If \(q\) has infinite order, the only nonzero self-Ext groups occur in degrees \(0\) and \(1\), so the positive-degree generator squares to zero for degree reasons. If \(q\) has finite order \(m\), Enomoto's formula \(\Omega^{2r}(U_\lambda)\cong U_{q^r\lambda}\) gives \(\Omega^{2m}(U_\lambda)\cong U_\lambda\). No smaller even period is possible because distinct parameters give zero Hom, and no odd syzygy can be isomorphic to \(U_\lambda\): every odd syzygy has dimension \(10\), whereas \(U_\lambda\) has dimension \(2\). Hence the exact period is \(2m\).

## Verification
The proof uses the actual minimal sequence and arrow actions displayed in Enomoto's Proposition 4.1 and the parameter-separation Lemma 4.2. The induced Hom-complex is computed directly from those maps. No finite experiment or extrapolation is used: the argument is symbolic for every permitted \(q,\lambda,\mu\).

A consistency check at degree zero reproduces Enomoto's Hom vanishing: \(\operatorname{Ext}^0(U_\lambda,U_\mu)=0\) when \(\lambda\ne\mu\). The finite-order conclusion also agrees with the general band-module mechanism in Erdmann's earlier work, where a multiplicative syzygy parameter that is a root of unity produces periodicity.

## Relationship to prior work
Enomoto proves \(\Omega^2(U_\lambda)\cong U_{q\lambda}\), its iteration, and Hom vanishing for distinct parameters in order to construct a nonperiodic module when \(q\) has infinite order. The inspected paper does not state the pairwise Ext groups or the resulting self-Ext algebra.

Erdmann's 2016 preprint on non-periodic bounded modules proves an analogous relation \(\Omega^2(M(\lambda))\cong M(v\lambda)\) for band modules over weakly symmetric special biserial algebras and observes the periodic root-of-unity case. That result motivates comparison but does not identify Enomoto's \(\Lambda(q)\)-modules or compute the Ext profile above. Erdmann's earlier Ext-finite classification is restricted to weakly symmetric indecomposable algebras with radical cube zero; Enomoto's algebra has nonzero paths of length greater than two, so that classification does not cover this setting.

## Limitations
This result does not classify all modules over \(\Lambda(q)\), does not determine the full Yoneda algebra between arbitrary modules, and does not make a new claim about bimodule periodicity of \(\Lambda(q)\). The originality comparison is limited by the possibility of unindexed or differently phrased literature, especially because the motivating preprint is recent.

## References
1. H. Enomoto, *A counterexample to the periodicity conjecture for finite-dimensional algebras*, arXiv:2609.09732v1, 2026.
2. K. Erdmann, *Algebras with non-periodic bounded modules*, arXiv:1601.07480v1; J. Algebra 475 (2017), 308–326.
3. K. Erdmann, *Ext-finite modules for weakly symmetric algebras with radical cube zero*, arXiv:1511.01418v1; J. Aust. Math. Soc. 103 (2017), 44–59.
