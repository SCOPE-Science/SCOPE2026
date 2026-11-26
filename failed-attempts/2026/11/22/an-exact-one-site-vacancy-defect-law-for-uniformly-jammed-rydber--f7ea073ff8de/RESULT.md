# An exact one-site vacancy defect law for uniformly jammed Rydberg rings

## Finding
Fix a blockade radius \(b\in\mathbb N\), \(b\ge1\). On a labeled \(L\)-site ring, place excited atoms with at least \(b\) vacant sites between consecutive excited atoms, and require maximality: no other available site may be excited without violating the blockade. Let \(Z_{L,b}(y)\) be the excitation-fugacity partition function for the intact ring, with each configuration of \(n\) excited atoms weighted by \(y^n\), \(y>0\).

Make site \(0\) **inert**: it must remain unexcited and is exempt from the maximality requirement; all other sites must still be blocked or excited. Let \(Z^{\mathrm{inert}}_{L,b}(y)\) be the resulting partition function. Set
\[
G_b(z)=\sum_{d=b+1}^{2b+1}z^d,
\qquad yG_b(z_b(y))=1,
\qquad \rho_b(y)=\left(y\sum_{d=b+1}^{2b+1}d\,z_b(y)^d\right)^{-1}.
\]
The unique root \(z_b(y)\) lies in \((0,\infty)\), and \(\rho_b(y)\) is the intact-ring limiting mean excitation density. Then, for every fixed \(b\ge1\) and \(y>0\),
\[
\boxed{\lim_{L\to\infty}\frac{Z^{\mathrm{inert}}_{L,b}(y)}{Z_{L,b}(y)}
=1-\rho_b(y)+y\rho_b(y)z_b(y)^{2b+2}.}
\]

Every configuration counted only by the inert-ring ensemble contains **one and only one exceptional consecutive-atom gap** of length \(2b+2\) (rather than one of the normal lengths \(b+1,\ldots,2b+1\)); this exceptional gap has its unique unblocked site at \(0\). Consequently, the thermodynamic probability of such an exceptional gap in the inert ensemble is
\[
\boxed{P_b(y)=\frac{y\rho_b(y)z_b(y)^{2b+2}}
{1-\rho_b(y)+y\rho_b(y)z_b(y)^{2b+2}}.}
\]
At uniform weights \(y=1\), the sharp large-blockade law is
\[
\boxed{P_b(1)\sim\frac{(\log b)^2}{b^3}\quad(b\to\infty).}
\]
The order of limits is: first \(L\to\infty\) for fixed \(b\), and then \(b\to\infty\).

## Assumptions and scope
The ring has labeled sites \(\mathbb Z/L\mathbb Z\), with nearest-neighbor cyclic graph distance and blockade range \(b\). All weights are equilibrium weights **uniform among allowed jammed states at \(y=1\)**; no assertion about the distribution produced by random sequential adsorption is made. The defect is a missing or permanently inexcitable site that does not itself have to be blocked. All other physical sites obey the original exclusion and maximality constraints. For the exact finite-ring statements below assume \(L\ge4b+5\); the limits need only fixed \(b\) and sufficiently large \(L\). The statement is about a single inert site, not positive-density random disorder or interacting dynamical defects.

## Proof
Write \(e=2b+2\), and let \([z^L]\) denote a formal-series coefficient. On the intact ring, consecutive occupied sites have clockwise separations precisely in \(\{b+1,\ldots,2b+1\}\): the lower bound is the blockade rule, and a larger separation leaves an unblocked vacant site. Conversely, the stated range guarantees maximality. For any integer \(n\ge1\), the number of labeled intact configurations with \(n\) excitations is exactly
\[
B_{L,b,n}=\frac{L}{n}[z^L]G_b(z)^n.
\]
Indeed, choose a distinguished occupied site (\(L\) choices), choose the successive \(n\) clockwise gaps, and divide by the \(n\) possible distinguished atoms in each configuration. Thus
\[
Z_{L,b}(y)=\sum_{n\ge1}B_{L,b,n}y^n,
\qquad \sum_{L\ge1} Z_{L,b}(y)z^L=\frac{zyG_b'(z)}{1-yG_b(z)}.
\]

If a valid inert-ring configuration would also be jammed on the original intact ring, its site \(0\) is simply unoccupied. Translation invariance makes the number of such \(n\)-excitation configurations exactly \((1-n/L)B_{L,b,n}\). Otherwise \(0\) is the *only* unblocked site of the intact ring. A separating gap of \(e=2b+2\) must therefore have endpoints at sites \(-(b+1)\) and \(b+1\), with its unique unblocked center at \(0\); all remaining gaps are ordinary. Conversely, any such anchored exceptional gap and ordinary gaps give one valid inert-only configuration. The number of the latter with \(n\ge2\) excited sites is exactly
\[
E_{L,b,n}=[z^{L-e}]G_b(z)^{n-1}.
\]
This proves the finite-size identity
\[
\boxed{Z^{\mathrm{inert}}_{L,b}(y)=Z_{L,b}(y)-\frac{y}{L}\partial_y Z_{L,b}(y)
+\sum_{n\ge2}y^n[z^{L-e}]G_b(z)^{n-1}.}
\]
The generating function of the last sum, after summing over \(L\), is
\[
\sum_{L\ge1} E_{L,b}(y)z^L
=\frac{y^2z^eG_b(z)}{1-yG_b(z)}.
\]
For fixed \(y>0\), \(yG_b(z)\) has a unique positive root \(z_b(y)\); all other zeros of \(1-yG_b(z)\) have strictly larger modulus. This follows by the strict triangle inequality because the permitted gap lengths include consecutive integers, so their gcd is one. Both rational generating functions have a simple dominant pole at this root. Coefficient extraction therefore gives
\[
Z_{L,b}(y)\sim z_b(y)^{-L},\qquad
E_{L,b}(y)\sim y\rho_b(y)z_b(y)^e z_b(y)^{-L}.
\]
Analyticity of the dominant root for \(y>0\) also gives \(L^{-1}y\partial_y\log Z_{L,b}(y)\to\rho_b(y)\), because differentiating \(yG_b(z_b(y))=1\) yields \(-y\partial_y\log z_b(y)=\rho_b(y)\). Dividing the finite-size identity by \(Z_{L,b}(y)\) proves the first boxed formula. The extra-gap probability is the ratio of the \(E\) contribution to the total inert partition function, proving the second.

For the large-blockade law set \(B=b+1\) and \(z_b(1)=e^{-u_B/B}\). The root equation becomes exactly
\[
1-e^{-u_B/B}=e^{-u_B}(1-e^{-u_B}).
\]
It implies \(u_B\to\infty\), \(u_B/B\to0\), and \(u_Be^{u_B}/B\to1\). In particular \(u_B\sim\log B\). In the intact gap distribution with masses \(z_b(1)^d\), \(d=B,\ldots,2B-1\), the excess gap over \(B\) has mean \(O(B/u_B)\); hence \(\rho_b(1)\sim1/B\). Moreover \(z_b(1)^{2B}=e^{-2u_B}\sim u_B^2/B^2\). Substituting into the exact expression for \(P_b(1)\), whose denominator tends to one, gives \(P_b(1)\sim u_B^2/B^3\sim(\log b)^2/b^3\).

## Verification
The complete standard-library checker in `checker.py` exhaustively enumerates allowed states for \(16\) finite-ring/blockade pairs with \(b=1,2,3\), compares cardinality by excitation count with the explicit cyclic-composition and pinned-defect formulas, and checks several fugacities. It reports \(1194\) successful assertions. The same checker numerically evaluates the positive root and defect-event probability over additional blockade values. The finite exhaustive checks support the exact counting lemma but do not substitute for the analytic dominant-pole and large-blockade arguments. Run `python checker.py` from a directory containing the supplied file.

## Relationship to prior work
Došlić, Puljiz, Šebek and Žubrinić, *Complexity Function of Jammed Configurations of Rydberg Atoms*, arXiv:2302.08791 (first public 2023-02-17), give the intact-chain equilibrium enumeration and configurational entropy. Krapivsky and Luck, *A renewal approach to configurational entropy in one dimension*, arXiv:2302.08852 (first public 2023-02-17), develop the intact-model renewal generating functions and high-blockade asymptotics. Luck, *On the structure factor of jammed particle configurations on the one-dimensional lattice*, arXiv:2311.14393 (first public 2023-11-24), derives intact-ensemble local observables and correlations. These established bulk roots, densities, and methods are used here as known background. The assessed additional statement concerns **the explicitly broken maximality constraint at one prescribed site**, the newly permitted pinned oversized-gap sector, its exact finite-ring and thermodynamic partition ratios, and the rare-defect \((\log b)^2/b^3\) law. It is not a claim that the intact renewal formulas or bulk density are new.

## Limitations
The geometric gap classification is exact for sufficiently large finite rings and the stated order of limits, but physical realizations with thermal fluctuations, coherent Rydberg dynamics, or a defect affecting blockade interactions in a different way are outside the model. This is an equilibrium maximal-configuration ensemble, not a kinetic jamming prediction. Although the primary inspected literature does not state the pinned-inert-site partition ratio, an implicit earlier one-site-defect transfer-matrix formula could cover it; independent publication-priority assessment has not been performed. The \(b\)-asymptotic is not uniform in ring size.

## References
- T. Došlić, M. Puljiz, S. Šebek, J. Žubrinić, *Complexity Function of Jammed Configurations of Rydberg Atoms* (2023), https://arxiv.org/abs/2302.08791.
- P. L. Krapivsky, J. M. Luck, *A renewal approach to configurational entropy in one dimension* (2023), https://arxiv.org/abs/2302.08852.
- J.-M. Luck, *On the structure factor of jammed particle configurations on the one-dimensional lattice* (2023), https://arxiv.org/abs/2311.14393.
