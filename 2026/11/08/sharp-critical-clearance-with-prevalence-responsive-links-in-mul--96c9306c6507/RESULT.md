# Sharp critical clearance with prevalence-responsive links in multigroup SIS networks

## Finding

**Theorem (global critical profile for adaptive multigroup SIS).** Consider the finite-community deterministic system specified below, with irreducible transmission matrix and a strictly positive link-creation response at zero infection. At the exact threshold \(\mathcal R_0=1\), every solution with nonzero initial prevalence clears infection and restores every represented link density. Moreover, after normalization by the positive Perron right and left modes, it has an **initial-condition-independent, explicit inverse-time profile**:

\[
\lim_{t\to\infty}t\,y_i(t)=\frac{r_i}{\kappa},\qquad
\lim_{t\to\infty}t[1-z_{ij}(t)]=\frac{\gamma_{ij}}{\kappa}\quad(1\le i,j\le n),
\]

where \(\gamma_{ij}\ge0\), \(\kappa>0\), and their exact formulas appear below. In particular, first-order link-breaking sensitivity enters the leading infection-clearing amplitude, although the critical reproduction number itself does not depend on link-adaptation rates. If all link-breaking responses vanish to *second* order at the disease-free state, the leading infection-clearing coefficient agrees with the fixed-contact SIS model, regardless of their higher-order strength.

## Assumptions and scope

Fix an integer \(n\ge2\). For every \(1\le i,j\le n\), let \(\beta_{ij}\ge0\), \(\delta_i>0\), \(\zeta_{ij}\ge0\), and \(\xi_{ij}>0\). Require the nonnegative transmission matrix \(B=(\beta_{ij})\) to be irreducible. Let \(\phi_{ij},\psi_{ij}\) be nonnegative functions of the prevalence vector \(y\in[0,1]^n\), admitting \(C^2\) extensions to a neighborhood of the cube, with

\[
\phi_{ij}(0)=0,\qquad \psi_{ij}(0)>0.
\]

The model is

\[
\begin{aligned}
\dot y_i&=-\delta_i y_i+(1-y_i)\sum_{j=1}^n\beta_{ij}y_jz_{ij},\\
\dot z_{ij}&=-\zeta_{ij}z_{ij}\phi_{ij}(y)
                 +\xi_{ij}(1-z_{ij})\psi_{ij}(y).
\end{aligned}
\]

The scalar states \(0\le y_i,z_{ij}\le1\) are initial prevalence and the fraction of existing contacts. The responses may depend jointly on all communities, including the local and global awareness responses of the initiating multigroup aNIMFA model. No monotonicity of the responses is required beyond their stated nonnegativity. For links with \(\beta_{ij}=0\), the equation for \(z_{ij}\) may be retained; it does not influence disease transmission.

Write \(D=\operatorname{diag}(\delta_1,\ldots,\delta_n)\) and assume the *critical equality*

\[
\mathcal R_0=\rho(D^{-1}B)=1.
\]

Then \(A=B-D\) is irreducible Metzler, with simple spectral bound zero. Its strictly positive right and left zero eigenvectors \(r,l\) are uniquely normalized by

\[
Ar=0,\qquad l^{\mathsf T}A=0,\qquad
\sum_i r_i=1,\qquad l^{\mathsf T}r=1.
\]

Define the directional breaking sensitivity, link-deficiency coefficient, and population drift coefficient by

\[
\gamma_{ij}=
 \frac{\zeta_{ij}\,D\phi_{ij}(0)[r]}{\xi_{ij}\psi_{ij}(0)},
\qquad
\kappa=\sum_{i=1}^n l_i\left(\delta_i r_i^2+
           \sum_{j=1}^n\beta_{ij}r_j\gamma_{ij}\right).
\]

Because \(\phi_{ij}\) is nonnegative on the nonnegative orthant and zero at the origin, \(D\phi_{ij}(0)[r]\ge0\). Thus \(\gamma_{ij}\ge0\), and \(\kappa>0\) since \(l_i,\delta_i,r_i>0\). The theorem holds for **every** initial state in the closed feasible cube with \(y(0)\ne0\). If \(y(0)=0\), infection instead stays identically zero and link deficits decay exponentially; the inverse-time population profile is not asserted.

## Proof

**1. Feasibility, a decreasing Perron mass, and global extinction.** At \(y_i=0\), the prevalence derivative is nonnegative; at \(y_i=1\), it equals \(-\delta_i\). At \(z_{ij}=0\), the link derivative is \(\xi_{ij}\psi_{ij}(y)\ge0\); at \(z_{ij}=1\), it equals \(-\zeta_{ij}\phi_{ij}(y)\le0\). Hence the compact feasible cube is forward invariant and solutions exist globally.

Put \(v_{ij}=1-z_{ij}\) and \(W=l^{\mathsf T}y\). Using \(l^{\mathsf T}(B-D)=0\), exact differentiation gives the sign-definite identity

\[
\boxed{
\dot W=-\sum_i l_i y_i(By)_i
       -\sum_{i,j}l_i(1-y_i)\beta_{ij}y_jv_{ij}\le0.}
\]

It follows that \(W(t)\) has a nonnegative limit. To identify the largest invariant subset of \(\{\dot W=0\}\), take any nonzero prevalence vector and let \(S\) be its positive support. If all groups have positive prevalence, the first sum is positive because \(B\) is irreducible. If \(S\) is a proper nonempty subset, irreducibility supplies a directed transmission edge from a currently positive group \(j\in S\) to a zero-prevalence group \(i\notin S\). The equality \(\dot W=0\) forces \(v_{ij}=0\) on every such edge. Therefore the corresponding zero-prevalence coordinate satisfies \(\dot y_i=\sum_j\beta_{ij}y_jz_{ij}>0\). Once a coordinate is positive, it cannot return to zero at a finite future time, because \(\dot y_i\ge-\delta_i y_i\). An entire trajectory trapped in \(\{\dot W=0\}\) would therefore enlarge its positive support along outgoing edges until every group were positive, a contradiction. The only invariant subset has \(y=0\). LaSalle's invariance principle gives \(y(t)\to0\). Each link then satisfies an asymptotically stable scalar restoration equation, because \(\zeta_{ij}\phi_{ij}(y(t))\to0\) and \(\xi_{ij}\psi_{ij}(y(t))\to\xi_{ij}\psi_{ij}(0)>0\), so \(v_{ij}(t)\to0\).

**2. The slow Perron direction.** For a nonzero initial prevalence, \(W(t)>0\) at every finite time: the prevalence equations imply \(\dot W\ge-CW\) for a finite constant on the cube. The exact derivative above and positivity of \(l\) yield

\[
\frac{\dot W}{W}=O(W+\|v\|)\longrightarrow0,
\]

where \(\|v\|\) denotes any fixed finite-dimensional norm. In particular, \(W\) decays subexponentially: for every \(\varepsilon>0\), eventually \(-\varepsilon\le(\log W)'\le0\). For each fixed \(s\ge0\), the ratio \(W(t-s)/W(t)\to1\), and for large \(t\) it is bounded by \(e^{\varepsilon s}\).

Expand the prevalence equation as \(\dot y=Ay+R(y,v)\), where

\[
R_i(y,v)=-y_i(By)_i-(1-y_i)\sum_j\beta_{ij}y_jv_{ij}.
\]

Since all components of \(y\) are bounded by a constant times \(W\), one has \(\|R(y(t),v(t))\|=O(W^2+W\|v\|)=o(W)\). Let \(P=r l^{\mathsf T}\) be the spectral projection onto the zero eigenvalue of \(A\) and \(Q=I-P\). Irreducibility of \(A\) gives an exponential semigroup bound \(\|e^{At}Q\|\le C e^{-at}\) for some \(a>0\). Variation of constants, division by \(W(t)\), and the preceding subexponential-ratio bound show that both the decaying initial term and the convolution of \(o(W)\) with this stable semigroup are \(o(W(t))\). Thus

\[
\frac{y(t)}{W(t)}\longrightarrow r.
\]

**3. Each link relaxes to the slow mode.** The exact link-deficit equation is

\[
\dot v_{ij}=\zeta_{ij}(1-v_{ij})\phi_{ij}(y)
                -\xi_{ij}v_{ij}\psi_{ij}(y).
\]

Taylor expansion at the zero-prevalence state gives

\[
\dot v_{ij}=-\lambda_{ij}v_{ij}+
 \zeta_{ij}D\phi_{ij}(0)[y]
 +O(W^2+Wv_{ij}),
\qquad\lambda_{ij}=\xi_{ij}\psi_{ij}(0)>0.
\]

The last error is \(o(W)\) because \(W,v\to0\). By step 2 the forcing is \(\zeta_{ij}D\phi_{ij}(0)[r]W(t)+o(W(t))\). Applying variation of constants and the same exponential-kernel/slow-ratio comparison yields

\[
\frac{v_{ij}(t)}{W(t)}\longrightarrow
 \frac{\zeta_{ij}D\phi_{ij}(0)[r]}{\lambda_{ij}}=\gamma_{ij}.
\]

This conclusion also covers vanishing derivatives and zero breaking rates, when the limit is zero.

**4. Exact inverse-time amplitude.** Substitute the ratios from steps 2 and 3 into the exact expression for \(\dot W\). Because \((Br)_i=\delta_i r_i\),

\[
\frac{\dot W(t)}{W(t)^2}\longrightarrow
 -\sum_i l_i\left(r_i(Br)_i+\sum_j\beta_{ij}r_j\gamma_{ij}\right)
 =-\kappa.
\]

Consequently \(\frac{\mathrm d}{\mathrm dt}(1/W(t))\to\kappa>0\), so \(1/[tW(t)]\to\kappa\). Combining this with \(y/W\to r\) and \(v/W\to\gamma\) proves both asserted limits for every admissible nonzero initial prevalence. No numerical enumeration or center-manifold assumption is used. \(\square\)

**Corollary (response-order barrier).** If \(D\phi_{ij}(0)[r]=0\) on every active transmission edge, then \(\kappa=\sum_i l_i\delta_i r_i^2\) and \(t y_i(t)\to r_i/\kappa\), exactly as in the critical fixed-contact SIS network. Linear and higher-order response mechanisms can therefore have identical reproduction thresholds but different critical decay amplitudes; breaking that is only quadratic or higher order in low prevalence does not change the first asymptotic coefficient.

## Verification

Take two communities with unit recovery, symmetric transmission rates

\[
B=\begin{pmatrix}1/4&3/4\\3/4&1/4\end{pmatrix},\quad
\xi_{ij}=1,\quad\psi_{ij}(y)=1,
\]

and breaking only on cross-community links, at rate \(\zeta_{12}=\zeta_{21}=c\ge0\). Use \(\phi_{12}(y)=\phi_{21}(y)=(y_1+y_2)/2\), with zero breaking responses on self-links. The Perron modes are \(r=(1/2,1/2)^{\mathsf T}\), \(l=(1,1)^{\mathsf T}\), and the exact coefficients reduce to

\[
\gamma_{12}=\gamma_{21}=c/2,\quad
\kappa=(4+3c)/8,\quad
\lim t y_i=\frac4{4+3c},\quad
\lim t(1-z_{12})=\lim t(1-z_{21})=\frac{4c}{4+3c}.
\]

At \(c=2\), the limits are \(2/5\) for each prevalence and \(4/5\) for each cross-link deficit. In contrast, replacing the breaking responses by \(((y_1+y_2)/2)^2\) with the same \(c=2\) yields the static-network limit \(\lim t y_i=1\) and \(\lim t(1-z_{12})=0\). The standalone `verify.py` establishes the algebraic coefficients exactly, and provides optional high-accuracy numerical checks to time \(10^5\) for each response order. Its printed `VERIFY_OK` is a computational replay indicator, not a substitute for the all-time proof.

## Relationship to prior work

Achterberg, Sensi, and Sottile (arXiv:2407.17639, initially public July 24, 2024) introduce the heterogeneous multigroup aNIMFA system and obtain the reproduction number. Their Theorem 2 proves disease-free global stability under a **strict** threshold \(\mathcal R_0<1\); sections 3–5 discuss supercritical equilibria and examples of oscillation. The critical equality, the nonlinear universal amplitude, and linked contact-deficit profile above do not follow from their strict-threshold argument. Their 2023 predecessor treats a single adaptive community with a planar system. Standard static SIS criticality yields a related inverse-time epidemic rate but has no state-dependent link-repair dynamics or the term \(\sum_{ij}l_i\beta_{ij}r_j\gamma_{ij}\). A previously documented one-community critical feedback law also does not determine the heterogeneous left/right Perron-weighted coupling stated here. Other adaptive-network and multi-group epidemic literature treats related thresholds or near-critical topology, without an identified implication covering this full statement in the inspected evidence. See the accompanying scientific review for specific comparisons and access limits.

## Limitations

The conclusion is for a finite-dimensional deterministic compartmental ODE, not a stochastic individual contact network. It requires irreducible \(B\), strictly positive recovery and link-restoration response at zero prevalence, and \(\phi_{ij}(0)=0\). It applies at the exact equality \(\mathcal R_0=1\) and does not classify supercritical attractors, bistability, or transient waves. Its limits are first-order asymptotic statements; no uniform error estimate over parameters or initial conditions is claimed. Bibliographic comparisons cannot logically establish absolute priority, and independently reproduced proofs or external audit remain outstanding.

## References

1. M. A. Achterberg, M. Sensi, S. Sottile, *A minimal model for multigroup adaptive SIS epidemics*, arXiv:2407.17639 (v1, 2024-07-24; inspected full-text v3 dated 2025-01-30), https://arxiv.org/abs/2407.17639 and https://arxiv.org/html/2407.17639v3 .
2. M. A. Achterberg, M. Sensi, *A minimal model for adaptive SIS epidemics*, Nonlinear Dynamics 111 (2023), 12657–12670, https://doi.org/10.1007/s11071-023-08498-4 .
3. L. Horstmeyer, C. Kuehn, S. Thurner, *Network topology near criticality in adaptive epidemics*, Physical Review E 98 (2018), 042313, https://doi.org/10.1103/PhysRevE.98.042313 .
4. M. A. Achterberg, J. L. A. Dubbeldam, C. J. Stam, P. Van Mieghem, *Classification of link-breaking and link-creation updating rules in susceptible-infected-susceptible epidemics on adaptive networks*, Physical Review E 101 (2020), 052302, https://doi.org/10.1103/PhysRevE.101.052302 .
5. T. Gross, C. J. Dommar D’Lima, B. Blasius, *Epidemic dynamics on an adaptive network*, Physical Review Letters 96 (2006), 208701, https://doi.org/10.1103/PhysRevLett.96.208701 .
