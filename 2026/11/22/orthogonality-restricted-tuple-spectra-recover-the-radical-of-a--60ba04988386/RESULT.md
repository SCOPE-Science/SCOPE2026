# Orthogonality-restricted tuple spectra recover the radical of a finite symplectic parameter span

## Finding

Fix a prime power \(q\). Let \((V,\beta)\) be a countably infinite-dimensional nondegenerate alternating space over \(\mathbb F_q\), in the vector-space language with the finite field and the form named. Let \(A\) be a finite individually named parameter set, \(U=\langle A\rangle\), \(d=\dim U\), and \(\rho=\dim\operatorname{rad}(\beta|_U)\). For \(r\ge0\), let \(T_r^\perp(A)\) count complete types over \(A\) of ordered \(r\)-tuples with \(\beta(x_i,x_j)=0\) for all \(i,j\). Repetitions, zero coordinates, linear dependencies and coordinates in \(U\) are allowed.

Use \({n\brack k}_q\) for the Gaussian binomial coefficient (zero for \(k<0\) or \(k>n\)) and put \(m=(d-\rho)/2\). The number of totally isotropic \(t\)-subspaces of \(U\) is
\[
J_t(d,\rho;q)=\sum_{j=\max(0,t-m)}^{\min(t,\rho)}{\rho\brack j}_q q^{(t-j)(\rho-j)}\prod_{i=0}^{t-j-1}\frac{q^{2m-i}-q^i}{q^{t-j}-q^i}.
\]
Empty products are one and empty sums are zero. The spectrum is
\[
T_r^\perp(A)=\sum_{h=0}^{r}{r\brack h}_q\sum_{t=0}^{\min(h,d)}J_t(d,\rho;q)\left(\prod_{i=0}^{t-1}(q^h-q^i)\right)q^{(r-h)(d-t)}.
\]
In particular \(T_0^\perp=1\) and \(T_1^\perp=2q^d\). For \(d\ge1\),
\[
T_2^\perp=2q^{2d}-(q^d-q^\rho)(q^d-q^{d-1})+(q+1)\big[q^d+(q^d-1)q^{d-1}\big].
\]
For \(d=0\), the spectrum is \(T_r^\perp=\sum_{h=0}^r{r\brack h}_q\), so \(T_2^\perp=q+3\) (equal to five only for \(q=2\)). At fixed \(q\), the unary and binary counts determine \(d\) and \(\rho\), hence the abstract isometry class of \(U\) and all subsequent counts. Unary data alone are insufficient: two-dimensional parameter spaces over \(\mathbb F_2\) with zero form and with a nondegenerate alternating form both have unary count eight, but their orthogonal pair counts are respectively 62 and 56.

## Assumptions and scope

The ambient space has unbounded hyperbolic rank; the restriction to \(U\) may be degenerate. Orthogonality means vanishing of the form, including in characteristic two. Counts use ordered vector coordinates in the specified language, over the pointwise-named parameters. The reconstruction concerns the abstract alternating space \(U\); it does not recover the labelling or Gram matrix of the particular generators in \(A\).

## Proof

**Finite extension and orbit data.** Every finite alternating space embeds in a finite nondegenerate one: split off a nondegenerate summand and adjoin dual partners to a basis of the radical. Every finite subspace of \(V\) is also contained in a finite nondegenerate subspace of \(V\). For this, split the subspace as \(M\oplus R\) with \(M\) nondegenerate and \(R\) the radical. In \(M^\perp\), the pairing map to \(R^*\) is surjective by nondegeneracy and finite dimensionality of \(R\). The span of a basis of \(R\) and chosen dual partners is nondegenerate, regardless of the pairings among the partners. The finite-dimensional alternating Witt extension theorem applied in such an envelope extends an isometry between two finite subspaces of \(V\), and the extension acts as the identity on the envelope's orthogonal complement.

Write \(W=\mathbb F_q^r\) and let \(L:W\to V\) send the ordered standard basis to the tuple. The data determining the orbit under the pointwise stabilizer of \(U\) are:

1. the kernel \(H\) of \(W\xrightarrow{L}V\to V/U\);
2. the map \(a=L|_H:H\to U\);
3. the pairing with \(U\) of the images of a basis of a fixed complement \(W_0\) of \(H\) in \(W\).

Indeed the images from \(W_0\) are independent modulo \(U\); their mutual pairings are zero. The listed data determine the linear relations and all pairings in \(U+L(W)\), so equality of data gives an isometry fixing \(U\). Conversely all data are invariant. For realization, the image \(S=a(H)\) must be isotropic and the chosen functionals on \(U\) must vanish on \(S\). Any such data define an alternating form on the abstract sum \(U\oplus W_0\) with the given pairings across the summands and zero pairings within \(W_0\). Give \(W\) the map \(h+w_0\mapsto a(h)+w_0\). Embed this alternating space into a finite nondegenerate one and then into \(V\), and use Witt extension to align the embedded copy of \(U\) with the named one. This proves realizability without assumptions on the characteristic. There are finitely many complete diagrams of linear relations and pairings at fixed \(q,d,r\); each consistent such diagram in an elementary extension is realized by the same construction. Since realized tuples with the same diagram are conjugate, each diagram determines a complete type over \(A\).

**Counting the data.** With \(h=\dim H\), there are \({r\brack h}_q\) choices for \(H\). For a chosen isotropic \(S\subset U\) of dimension \(t\), there are \(\prod_{i=0}^{t-1}(q^h-q^i)\) surjections \(H\to S\). The \(r-h\) pairing functionals on \(U\) vanishing on \(S\) contribute \(q^{(r-h)(d-t)}\). This gives the stated sum over \(h,t\).

To evaluate \(J_t\), let \(R\) be the radical of \(U\), and put \(j=\dim(S\cap R)\). Select \(S\cap R\) in \({\rho\brack j}_q\) ways. The image in the nondegenerate quotient \(U/R\) is isotropic of dimension \(s=t-j\); the lifts for a given image and intersection are parametrized by linear maps to \(R/(S\cap R)\), giving \(q^{s(\rho-j)}\) choices. The number of ordered independent mutually orthogonal \(s\)-frames in the quotient is \(\prod_{i=0}^{s-1}(q^{2m-i}-q^i)\): at stage \(i\) select a vector in the perpendicular of the span but not in the span itself. Dividing by the number of ordered bases of an \(s\)-space gives the product in \(J_t\). The bounds on \(j\) follow from \(0\le s\le m\) and \(0\le j\le\min(t,\rho)\).

**Low arities and recovery.** For one coordinate, the \(q^d\) vectors in \(U\) each give a type and the nonzero quotient case gives one type per pairing functional, another \(q^d\). For an orthogonal ordered pair and \(d\ge1\), quotient rank two contributes \(q^{2d}\) choices of two functionals. Rank zero contributes \(q^\rho q^d+(q^d-q^\rho)q^{d-1}\) pairs inside \(U\), because a vector in the radical has \(q^d\) possible partners and every other vector has \(q^{d-1}\). Rank one gives \(q+1\) kernel lines. For each line, a chosen generator may map to zero (contributing \(q^d\) functionals) or to one of \(q^d-1\) nonzero vectors (contributing \(q^{d-1}\) functionals each). Adding the three contributions gives the binary formula. For \(d=0\), all choices after \(H\) are unique, so the binary count is the number of subspaces of \(\mathbb F_q^2\): the zero space, \(q+1\) lines and the full space. At fixed \(q\), \(T_1^\perp\) determines \(d\); \(\rho=0\) when \(d=0\), and otherwise the coefficient of \(q^\rho\) in the binary count is \(q^d-q^{d-1}>0\). The rank and radical dimensions classify finite alternating forms over a fixed field, proving recovery and the claimed sharpness example.

## Verification

The recorded outputs for `verify.cpp` and `verify_general.py` give finite checks using explicit finite symplectic spaces and isotropic image strata, respectively. They cover selected bases over \(\mathbb F_2\) and \(\mathbb F_3\), with the latter program comparing the all-arity expression through arity four in its test cases. The empty-base binary count is independently obtainable by enumerating the linear relation subspaces of \(\mathbb F_q^2\) as above; for example it is six over \(\mathbb F_3\). The general theorem rests on the finite extension and counting arguments, not on extrapolation from the finite tests.

## Relationship to prior work and limitations

The proof uses familiar alternating Witt extension and the symplectic count of isotropic frames. Barbina's Theorem 3.3.4 gives the finite-subspace extension background for countable symplectic spaces. Liu's work on finite singular-symplectic subspace orbits concerns a related enumeration problem. Unrestricted alternating tuple-orbit formulas without a named base instead vary the form on the tuple span. Here the new-vector form is fixed to zero, the named base is fixed pointwise, and the interaction between a tuple and that base is counted explicitly. It is this interaction that allows the radical dimension to be recovered from the first two counts. The result does not apply to arbitrary reducts or recover the marked parameter structure, and it does not assert historical priority for the standard ingredients.

## References

- Silvia Barbina, *Automorphism groups of omega-categorical structures*, University of Leeds thesis, 2004, §3.3. https://silviabarbina.github.io/tutto.pdf
- Xuemei Liu, *Lattices Generated by Two Orbits of Subspaces under Finite Singular Symplectic Groups*, 2013. https://doi.org/10.1155/2013/732808
- *Exact product tuple-orbit profiles for homogeneous finite-field bilinear spaces*, mathematical record, 2026, record ID `ee908111b8bd`.
