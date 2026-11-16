# Sharp polyspectral order and minimal entry design on two Fourier cosets

## Finding
Let \(G\) be a finite abelian group, \(\Gamma=\widehat G\), and \(H<\Gamma\) a subgroup of size \(h\). Choose \(a\in\Gamma\setminus H\) whose class has order \(q\ge3\) in \(\Gamma/H\). Let \(S=H\cup(a+H)\). For complex signals \(f:G\to\mathbb C\) with \(\widehat f(\xi)\ne0\) exactly when \(\xi\in S\), define the order-\(r\) mixed polyspectrum by
\[
P_r^f(\xi_1,\ldots,\xi_{r-1})=\widehat f(\xi_1)\cdots\widehat f(\xi_{r-1})\overline{\widehat f(\xi_1+\cdots+\xi_{r-1})},\quad r\ge2.
\]
Then:

**(i) Sharp order.** Full power spectrum and all mixed polyspectra of orders \(3,\ldots,q\) leave a circle of non-translation phase ambiguities. Precisely, for any second signal \(g\) with identical data through order \(q\), its nonzero Fourier ratio has the form
\[
\rho(h')=\chi(h'),\qquad\rho(a+h')=\alpha\chi(h')\quad(h'\in H),
\]
with \(\chi\in\widehat H\) and arbitrary \(\alpha\in\mathbb T\). Equal data through order \(q+1\) force \(\alpha^q=\chi(qa)\), and therefore \(g\) is a translate of \(f\). The order \(q+1\) is optimal.

**(ii) Sharp individual-entry count.** Once all Fourier magnitudes are known, exactly \(2h\) selected nonzero mixed-polyspectrum entries suffice to determine every such signal up to translation. One explicit choice has \(2h-1\) cubic entries and the single \(q+1\)-st-order entry \(P_{q+1}^f(a,\ldots,a)\). No fixed selection of fewer than \(2h\) individual entries, of any orders, recovers every signal in this class up to translation.

Both results hold for all finite abelian \(G\), all allowed \(H\), and every set of nonzero Fourier amplitudes on \(S\), without genericity or reality assumptions.

## Assumptions and scope
The Fourier transform is \(\widehat f(\xi)=\sum_{x\in G}f(x)\overline{\xi(x)}\). Group laws in \(\Gamma\) are written additively and \(\mathbb T=\{z\in\mathbb C:|z|=1\}\). The character \(\chi:H\to\mathbb T\) is multiplicative with respect to addition. A translation \(f(x-t)\) multiplies \(\widehat f(\xi)\) by \(\overline{\xi(t)}\); all such Fourier ratios are restrictions of characters of \(\Gamma\), and conversely every character on a subgroup of \(\Gamma\) extends to \(\Gamma\) and comes from a translation in \(G\).

A mixed polyspectrum is the Fourier transform, with the stated conventions and a known nonzero normalization, of the mixed spatial correlation \(\sum_{x\in G}f(x+t_1)\cdots f(x+t_{r-1})\overline{f(x)}\). This is distinct from the holomorphic autocorrelation \(\sum_x\prod_j f(x+t_j)\). Its individual entries need not be real. Because \(0\in H\), all designated entries below are nonzero for every admissible signal.

## Proof
**Phase equations.** Equal power spectra imply common Fourier support and unit-modulus ratios \(\rho(\xi)=\widehat g(\xi)/\widehat f(\xi)\) for \(\xi\in S\). Equality of a nonzero \(P_r\) entry is equivalent to
\[
\rho(\xi_1)\cdots\rho(\xi_{r-1})=\rho(\xi_1+\cdots+\xi_{r-1}).\tag{1}
\]
The cubic equality at \((0,0)\) gives \(\rho(0)=1\). Cubic entries at \((h_1,h_2)\), with \(h_i\in H\), give \(\rho(h_1+h_2)=\rho(h_1)\rho(h_2)\), so \(\rho|_H=\chi\in\widehat H\). Cubic entries at \((a+h_1,h_2)\) give \(\rho(a+h)=\alpha\chi(h)\), where \(\alpha=\rho(a)\). Conversely all nonzero polyspectral entries of order at most \(q\) satisfy (1) for every such pair \((\chi,\alpha)\). Indeed if \(t\) inputs lie in \(a+H\), the sum lies in \(S\) only if \(t\equiv0\) or \(1\pmod q\). Since \(0\le t\le r-1\le q-1\), necessarily \(t=0\) or \(1\), for which the phase factors match. (Entries with summed frequency outside \(S\) vanish for both signals.)

At order \(q+1\), the tuple of \(q\) copies of \(a\) has sum \(qa\in H\); (1) becomes \(\alpha^q=\chi(qa)\). This equation is exactly the compatibility condition for a character of \(\langle H,a\rangle\) extending \(\chi\) and sending \(a\) to \(\alpha\). Since every character of a subgroup of a finite abelian group extends to the full group, this is a translation ratio. Every other valid \(P_{q+1}\) entry is then automatically preserved. Choosing \(\chi=1\) and \(\alpha\in\mathbb T\) with \(\alpha^q\ne1\) proves nonuniqueness modulo translations at all lower orders. This proves (i).

**Explicit sparse measurement selection.** Fix an invariant-factor decomposition \(H=C_{n_1}\oplus\cdots\oplus C_{n_d}\), with \(n_j\ge2\) and generators \(e_j\). The trivial group has \(d=0\). Represent each \(h'\in H\) by canonical coordinates \(0\le k_j<n_j\). For every nonzero \(h'\), choose the first \(j\) with \(k_j>0\), and set \(p(h')=h'-e_j\). Let \(E=\{e_1,\ldots,e_d\}\). Select the following nonzero polyspectral entries:

1. \(P_3(0,0)\), one entry.
2. \(P_3(p(h'),e_j)\) for \(h'\in H\setminus(\{0\}\cup E)\), where \(j\) is chosen from its canonical coordinates, altogether \(h-1-d\) entries.
3. \(P_3((n_j-1)e_j,e_j)\) for each \(j\), altogether \(d\) entries.
4. \(P_3(a+p(h'),e_j)\) for every \(h'\in H\setminus\{0\}\), altogether \(h-1\) entries.
5. \(P_{q+1}(a,\ldots,a)\) with exactly \(q\) arguments, one entry.

There are exactly \(1+(h-1-d)+d+(h-1)+1=2h\) entries (for \(h=1\), only the first and last). Recursion along \(p(h')\) forces \(\rho(h')=\prod_j\rho(e_j)^{k_j}\), and the cyclic closure entries force \(\rho(e_j)^{n_j}=1\). Thus \(\rho|_H\) is a character. The cross-coset recursion forces \(\rho(a+h')=\rho(a)\rho(h')\); the final entry imposes \(\rho(a)^q=\rho(qa)\). Hence the listed entries separate every signal from all non-translates.

**Optimality of the entry count.** For any fixed nonzero Fourier magnitudes, the unconstrained phases form a torus \(\mathbb T^{2h}\), with coordinates indexed by \(S\). Every individual nonzero polyspectral entry evaluates a character of this torus, i.e. an integral monomial in its coordinates. For \(m<2h\) selected entries, the group homomorphism \(\mathbb T^{2h}\to\mathbb T^m\) defined by their phase monomials has a positive-dimensional identity-component kernel, because its integer exponent matrix has rank at most \(m\). A positive-dimensional torus cannot consist of finitely many translations, so at least two non-translate signals have the same magnitudes and selected polyspectra. Entries that vanish identically contribute no constraint. Thus no \(m<2h\) measurements can suffice. This proves (ii).

## Verification
A standalone exact-integer program, `check_coset_polyspectra.py`, constructs the exponent matrix of the stated entries in cyclic extensions \(\Gamma=C_{hq}\), \(H=\langle q\rangle\), and split extensions \(\Gamma=H\oplus C_q\), including noncyclic \(H\). It checks that the selected matrix is square of dimension \(2h\), has determinant magnitude \(qh\), and has Smith invariant factors \((1,\ldots,1,qh)\) in the cyclic cases. These finite examples test implementation and normalization; the all-group theorem is proved by the preceding character argument, not numerical extrapolation. Use `python check_coset_polyspectra.py` with SymPy installed.

## Relationship to prior work
Higher-order autocorrelation reconstruction on finite abelian groups is studied by Agulnick and Busick-Warner (2026). Their stated order bounds concern holomorphic products of shifted signals and may impose different reality or rationality assumptions. Babanskyy (2026) develops zero-sum phase lattices and local separating degrees, principally for holomorphic autocorrelations on cyclic Fourier supports. Schefler, Zhao and Zhong (2025/2026) develop general minimal separating sets of polynomial invariant monomials. These provide significant conceptual antecedents to the integral phase-relation method. The present result specifically establishes the complete sharp mixed-polyspectral phase fiber, its order \(q+1\) cutoff and an explicit exactly \(2h\)-entry sharp design for an arbitrary finite abelian two-coset support, with arbitrary nonzero complex amplitudes. General invariant-lattice criteria should not be mistaken for an assertion that this explicit support classification and minimum-sample construction was previously absent in all literature.

## Limitations
The support must be exactly two cosets with all Fourier coefficients nonzero, and the quotient order must be at least three. The theorem is for conjugate mixed polyspectra and does not automatically transfer to holomorphic autocorrelations or power-only phase retrieval. Observations are assumed exact, with no conditioning, noise or robustness estimate. The minimum count concerns fixed individual nonzero polyspectral entries after the entire power spectrum is known; it is not a lower bound on total scalar measurements including magnitudes. Novelty relative to older group-invariant and higher-correlation literature remains subject to independent specialist verification; no independent audit was undertaken.

## References
- A. Agulnick and T. Busick-Warner, *Higher-Order Autocorrelations on Finite Abelian Groups*, arXiv:2604.13310v1, first public April 14, 2026, https://arxiv.org/html/2604.13310v1.
- O. Babanskyy, *Autocorrelation Phase Lattices on Cyclic Groups: Unit Supports, 2pq Orbit Profiles, and Binary Reconstruction*, first public November 10, 2026, https://hub.valency.io/works/W_bent7gm9.
- B. Schefler, K. Zhao and Q. Zhong, *On separating sets of polynomial invariants of finite abelian group actions*, arXiv:2509.16097, initial version September 19, 2025, https://arxiv.org/html/2509.16097.
