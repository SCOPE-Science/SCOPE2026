# An energy-resolved frozen-state zeta for two-row Q2R

## Finding

Consider the reversible Q2R Ising update on a labelled \(2\times n\) square-lattice torus for every **even** integer \(n\ge4\). At each full step, sites of one checkerboard color flip their spins if exactly two of their four directed neighbors have value one, followed by the same rule on the other color. Because the vertical circumference is two, the north and south neighbors are the same site but count **twice**, as dictated by the four-direction torus rule.

Let \(E(x)\) be the number of disagreeing nearest-neighbor bonds, with these vertical bonds counted with multiplicity two, and define the energy-resolved frozen-state polynomial
\[
Z_n(u)=\sum_{x:F_n(x)=x}u^{E(x)}.
\]
For formal variables \(z,u\), set \(D(z,u)=(1-u^4z^2)A(z,u)B(z,u)C(z,u)\), where
\[
\begin{aligned}
A(z,u)&=1-z+(u^2+u^4)z^2+u^4z^3+u^6z^4,\\
B(z,u)&=1+u^4z+(u^4+u^6)z^2-u^8z^3+u^{10}z^4,\\
C(z,u)&=1-(1+u^4)z-(u^2+u^6)z^2\\
&\quad+(-u^4+2u^6-u^8)z^3+(u^6+u^{10})z^4\\
&\quad+2u^{10}z^5-u^{12}z^6.
\end{aligned}
\]
Then **the complete energy distribution at every permitted circumference** is
\[
\boxed{Z_n(u)=[z^n]\left(-z\frac{\partial}{\partial z}\log D(z,u)\right),\qquad n\ge4\text{ even}.}
\]
Equivalently, the coefficient is determined by a sixteen-state transfer and the displayed explicit polynomial, with no finite-size cutoff.

Write \(L_0=2\), \(L_1=1\), \(L_{k+2}=L_{k+1}+L_k\) for Lucas numbers and \(\varphi=(1+\sqrt5)/2\). The exact unweighted count and its entropy are
\[
\boxed{Z_n(1)=L_{2n}+4L_n\cos(n\pi/3)+4+2\cos(2n\pi/3)},
\qquad \lim_{\substack{n\to\infty\\2\mid n}}\frac{\log Z_n(1)}{2n}=\log\varphi.
\]
The complete energy population has an exact mirror symmetry:
\[
\boxed{Z_n(u)=u^{4n}Z_n(u^{-1}).}
\]
In particular, under the uniform distribution over frozen configurations, the mean number of disagreeing bonds is exactly \(2n\), half of all \(4n\) counted bonds, at **every** even circumference.

## Assumptions and scope

Spins belong to \(\{0,1\}\), and row indices are modulo two while column indices are modulo \(n\). There are four incident lattice directions per site, with the two vertical directions counted separately. This is a periodic **multigraph**, not the cubic simple prism \(C_n\square K_2\). Even circumference is essential because the alternating checkerboard color must be globally well-defined. A full time step first updates all sites with \(r+i\) even and then all sites with \(r+i\) odd. Configurations are counted with their labelled sites, without rotation, reflection or spin-reversal quotient. The polynomial uses disagreeing-bond count, not the negative-sign Ising Hamiltonian. No assertion is made for odd circumferences.

## Proof

**The frozen-state criterion.** A full checkerboard step can fix a state only if the first half-step changes no even-colored site, because the second half-step never changes one. In that case the odd-colored sites see the original configuration, so the second half-step also changes no site precisely when no odd site has two one-valued neighbors. Thus a configuration is frozen if and only if **no site has exactly two one-valued neighbors**, counted with directional multiplicities.

**The exact transfer.** Denote the four possible column words by \(\mathcal A=\{0,1\}^2\) and use the sixteen pair-states \((a,b)\in\mathcal A^2\). For \(a,b,c\in\mathcal A\), the two neighborhood counts in central column \(b\) are \(a_0+c_0+2b_1\) and \(a_1+c_1+2b_0\). Define the weighted matrix
\[
T(u)_{(a,b),(b',c)}=\mathbf1_{\{b=b'\}}\prod_{r=0}^1\mathbf1_{\{a_r+c_r+2b_{1-r}\ne2\}}\;u^{e(b,c)},
\quad e(b,c)=2\mathbf1_{\{b_0\ne b_1\}}+\sum_{r=0}^1\mathbf1_{\{b_r\ne c_r\}}.
\]
It has sixteen vertices and exactly 36 allowed directed transitions. Every labelled cyclic word of \(n\) columns yields exactly one length-\(n\) closed transfer walk, and vice versa. Its local transitions enforce the frozen criterion. Summing \(e(b,c)\) around the walk gives precisely the full disagreeing-bond number \(E(x)\). Therefore \(Z_n(u)=\operatorname{tr}(T(u)^n)\) for all permitted \(n\).

**Exact characteristic identity.** Finite symbolic integer-polynomial elimination gives
\[
\det(yI-T(u))=y^{16}D(y^{-1},u).
\]
The accompanying `verify_transfer.py` constructs all sixteen transfer states from the displayed local condition, computes its symbolic characteristic polynomial by exact arithmetic, and compares it coefficient-by-coefficient with this identity, thus certifying every coefficient of the displayed determinant. For any finite matrix, \(\sum_{n\ge1}\operatorname{tr}(T^n)z^n=-z\partial_z\log\det(I-zT)\) as an identity of formal power series. This proves the energy-resolved formula at arbitrary even circumference.

At \(u=1\) the full characteristic polynomial factors as
\[
(y-1)^2(y+1)^2(y^2-3y+1)(y^2+y+1)
(y^4-y^3+2y^2+y+1)(y^4+y^3+2y^2-y+1).
\]
The quadratic \(y^2-3y+1\) has roots \(\varphi^2\) and \(\varphi^{-2}\). The two quartics have roots \(\pm\varphi\exp(\pm i\pi/3)\) and \(\pm\varphi^{-1}\exp(\pm2i\pi/3)\), with appropriate independent signs. For even \(n\), these quartic roots contribute \(4L_n\cos(n\pi/3)\); the two unit-sign factors contribute four and the cubic-root factor contributes \(2\cos(2n\pi/3)\). This proves the Lucas formula. Since \(\varphi^{2n}\) strictly dominates all remaining exponential bases along even \(n\), the entropy claim follows directly.

**Exact energy duality.** For even \(n\), define a checkerboard gauge map \((Gx)_{r,i}=x_{r,i}\mathbin{\mathrm{xor}}((r+i)\bmod2)\). Every neighbor of a vertex has the opposite checkerboard parity. Hence this map either complements all four neighbor bits or none, preserving the condition of having exactly two one-valued neighbors. Thus it bijects frozen configurations. Every lattice bond has endpoints of opposite parity, so this map switches agreement and disagreement on every one of the \(4n\) bonds. Consequently \(E(Gx)=4n-E(x)\). Summing monomials over the involution proves the reciprocal polynomial identity and the exact mean-energy statement.

## Verification

Run `python3 verify_transfer.py` with SymPy 1.13.1 for the transfer matrix, exact characteristic identity, unweighted Lucas checks at even circumferences four through twelve, and weighted energy histograms at circumferences four and six. Separately compile `verify_direct.cpp` with `g++ -O2 -std=c++17 verify_direct.cpp -o direct` and run `./direct`. This second program evolves the original checkerboard automaton phase by phase, independently of the transfer construction, for **all** \(2^{2n}\) initial states at even circumferences four, six, eight and ten, and computes the full bond-energy histograms. The recorded outputs are provided as `verify_transfer.out` and `verify_direct.out`. Both programs were executed from the packaged source before inclusion; all assertions passed. The finite tests corroborate the theorem but are not the proof at arbitrary \(n\); the exact transfer identity and checkerboard involution supply that proof.

For example, at circumference four, the energy coefficients at \(E=0,4,8,12,16\) are respectively \(2,4,24,4,2\). At circumference six the total is 400; at eight it is 2,116; at ten it is 14,884; and at twelve it is 104,976.

## Relationship to prior work

Vichniac's 1984 work established reversible cellular-automaton simulation of Ising dynamics. Kari and Taati's 2015 open-access treatment specifies the two-color Q2R update, its reversibility and energy conservation, but does not provide this narrow-torus frozen-energy polynomial. Shukla's 2005 full text treats voter and zero-temperature Glauber dynamics on a **three-neighbor simple ladder**, rather than Q2R on the four-direction toroidal quotient with doubled vertical bonds. Banks and Djirar's 1992 report states a general graph method for cellular-automaton fixed points, not an inspected instance of this explicit polynomial.

The published result *Critical-field entropy spikes for one-spin metastability on cyclic Ising ladders* concerns an **antiferromagnetic homogeneous cubic simple prism** and weak single-spin stability in varying external fields. Its full statement and proof were compared: it neither treats the fourth neighbor arising from a duplicated vertical bond nor imposes the Q2R no-zero-local-field criterion, so its exact counts do not imply the present polynomial. The transfer-matrix method and the bipartite gauge principle are standard ingredients, not claimed as independent inventions. The contribution asserted here is the explicit full energy-resolved finite-strip law and its exact frozen-state consequences for the defined Q2R quotient.

## Limitations

The statement concerns **fixed** configurations only; Q2R is reversible and has many nonstationary periodic orbits, none of which are enumerated. It does not treat odd horizontal circumference, any taller strip, stochastic Glauber dynamics, or typical approach to statistical equilibrium. The multigraph convention for the two-row torus is essential. The original Vichniac article's full text could not be inspected, so older unseen enumerations remain a historical-priority risk. The formula has not undergone independent mathematical review.

## References

1. G. Y. Vichniac, *Simulating physics with cellular automata*, Physica D 10 (1984), 96–115, DOI: https://doi.org/10.1016/0167-2789(84)90253-7.
2. J. Kari and S. Taati, *Statistical Mechanics of Surjective Cellular Automata*, arXiv:1311.2319, v1 publicly posted 2013-11-10; Journal of Statistical Physics 160 (2015), 1198–1243, especially introduction and Example 9. https://doi.org/10.1007/s10955-015-1281-2.
3. P. Shukla, *Voter Dynamics on an Ising Ladder: Coarsening and Persistence*, first posted 2005-01-31, arXiv:cond-mat/0501754. https://arxiv.org/html/cond-mat/0501754v2.
4. S. P. Banks and S. Djirar, *Fixed Points and Shift Cycles in Cellular Automata*, Sheffield ACSE Research Report 459 (1992). https://eprints.whiterose.ac.uk/id/eprint/79286/.
5. *Critical-field entropy spikes for one-spin metastability on cyclic Ising ladders*, publicly available mathematical result, 2026. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-critical-field-entropy-spikes-for-one-spin-metastability-on-cycl--def1265feda1/RESULT.md.
