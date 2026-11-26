# Exact odd-copy activation hierarchy for equally spaced passive qutrits

## Finding

Fix \(\epsilon>0\) and the nondegenerate three-level Hamiltonian \(H=\epsilon\operatorname{diag}(0,1,2)\). For every full-rank diagonal state \(\rho=\operatorname{diag}(p_0,p_1,p_2)\) with \(p_0\ge p_1\ge p_2>0\) and \(p_0+p_1+p_2=1\), and every integer \(N\ge1\), put \(r_N=N\) for odd \(N\) and \(r_N=N-1\) for even \(N\), and \(k_N=(r_N+1)/2\). Then the following are equivalent:

1. No cyclic unitary on the \(N\) independent copies extracts positive average work relative to \(H^{(N)}=\sum_{j=1}^{N}H_j\).
2. \(p_0^{k_N-1}p_2^{k_N}\le p_1^{r_N}\le p_0^{k_N}p_2^{k_N-1}\).
3. For \(u=\log(p_0/p_1)\) and \(v=\log(p_1/p_2)\), one has \(u+v\ge r_N|u-v|\).

In particular, \(2m\)-copy passivity is equivalent to \((2m-1)\)-copy passivity for every integer \(m\ge1\). If \(u=v\), the state is Gibbs (including the infinite-temperature case) and every tensor power is passive. Otherwise the **first** activating copy number is the odd integer

\[
N_{\min}=2\left\lfloor\frac{\max(u,v)}{|u-v|}\right\rfloor+1.
\]

This is an exact statewise threshold: all smaller powers are passive, and this power and every larger power are active. The use of a floor accounts for strict activation rather than equality at a transition boundary.

## Assumptions and scope

Passivity refers to arbitrary global cyclic unitaries on \(N\) initially independent copies, with no catalyst, bath, change of local Hamiltonian, or restriction to local operations. A state commuting with a finite Hamiltonian is passive exactly when every strictly higher-energy eigenvector has population no larger than any strictly lower-energy eigenvector; eigenvectors at equal energy need not have equal populations. Repeated populations are permitted; vanishing populations are excluded. Energies are expressed in units of \(\epsilon\), and logarithms are natural.

## Proof

An \(N\)-copy product eigenvector with \(\ell\) occupations of level \(1\) and \(m\) occupations of level \(2\), where \(\ell,m\ge0\) and \(\ell+m\le N\), has total energy \(E=\epsilon(\ell+2m)\) and population \(P=p_0^{N-\ell-m}p_1^\ell p_2^m\). Write \(t=E/\epsilon=\ell+2m\), \(u=\log(p_0/p_1)\), and \(v=\log(p_1/p_2)\). Exact rearrangement gives

\[
-\log P+N\log p_0
= u\ell+(u+v)m
=\tfrac12(u+v)t+\tfrac12(u-v)\ell.
\]

For two product words, let the subscript \(h\) label the strictly higher-energy word and \(l\) the lower one, and put \(d=t_h-t_l\ge1\) and \(\Delta\ell=\ell_h-\ell_l\). Their logarithmic population ordering is exactly

\[
-\log(P_h/P_l)=\tfrac12\bigl[(u+v)d+(u-v)\Delta\ell\bigr].
\]

Each word satisfies \(\ell\equiv t\pmod2\), hence \(\Delta\ell\equiv d\pmod2\). If \(d\) is odd, \(\Delta\ell\) is odd and its absolute value is at most the greatest odd integer not exceeding \(N\), namely \(r_N\). If \(d\) is even, \(\Delta\ell\) is even and has absolute value at most \(N\) for even \(N\), or at most \(N-1\) for odd \(N\); in either case this is at most \(2r_N\). Consequently \(u+v\ge r_N|u-v|\) implies \((u+v)d+(u-v)\Delta\ell\ge0\) for *every* higher/lower energy pair, separately for odd and even \(d\). The state is therefore passive under every global cyclic unitary.

Conversely, suppose \(u+v<r_N|u-v|\), write \(r_N=2k-1\), and first treat \(u>v\). Compare the \(r_N\)-symbol low-energy word containing only level \(1\) (energy \(r_N\epsilon\), population \(p_1^{r_N}\)) against the higher-energy word consisting of \(k-1\) zeros and \(k\) twos (energy \((r_N+1)\epsilon\), population \(p_0^{k-1}p_2^k\)). The strict inequality is equivalent to \((k-1)u>kv\), so the higher-energy word has strictly larger population. For \(v>u\), compare the lower-energy word with \(k\) zeros and \(k-1\) twos (energy \((r_N-1)\epsilon\), population \(p_0^kp_2^{k-1}\)) against the higher-energy word of \(r_N\) ones (energy \(r_N\epsilon\), population \(p_1^{r_N}\)). The strict inequality is then \((k-1)v>ku\), again giving an inversion. If \(N\) is even, append one zero symbol to each word, which preserves the energy gap and the strict population order. Exchanging these two levels lowers the mean energy. This proves necessity as well as sufficiency, including all equality boundaries.

Expanding \(r_N=2k-1\) in the two-sided slope inequality gives \(ku\ge(k-1)v\) and \(kv\ge(k-1)u\), equivalent by exponentiation to the displayed population sandwich. Since \(r_{2m}=r_{2m-1}\), successive odd and even powers share a passivity boundary. For \(u\ne v\), the first violating odd \(r\) obeys \(r>(u+v)/|u-v|=2\max(u,v)/|u-v|-1\), giving the stated \(N_{\min}\) formula. Adding identical level-zero symbols to an inverted word pair propagates nonpassivity to all larger tensor powers. Finally, \(u=v\) is equivalent to \(p_1^2=p_0p_2\), so \(p_j\) are normalized Gibbs weights and every power is passive.

## Verification

The dependency-free standalone program `verify.py` checks the analytic criterion by exact integer arithmetic without logarithmic rounding. For each \(N\), it enumerates all occupation-count vectors and tests every pair at strictly different energies. The script reports `VERIFY_OK exact_count_vector_cases=1430 activation_onsets=3,5,7,9 witness_5=(64,32)`. In particular it checks all weakly descending positive integer population triples with entries at most \(9\) for copy numbers \(1\) to \(8\), plus ten additional triples through \(N=11\). The universal statement above is proved by the parity argument, not inferred from these finite tests.

A concrete threshold example is \((p_0,p_1,p_2)=(8,2,1)/11\). The first activated power is \(N=5\); at that power the energies of the words \(11111\) and \(00222\) are \(5\epsilon\) and \(6\epsilon\), whereas their populations are \(32/11^5\) and \(64/11^5\). Their transposition extracts the positive work \(32\epsilon/11^5\). The power \(N=4\) remains passive, including its equality boundary.

## Relationship to prior work

Skrzypczyk, Silva, and Brunner [1] prove complete passivity from common virtual temperature and provide in their section IV, equation (9), a **sufficient finite-copy activation construction** using two virtual temperatures. Applying that construction to the neighboring qutrit transitions yields a relevant activation witness and can give a matching upper bound for this special Hamiltonian. The result here does not claim the virtual-temperature mechanism as new. Its additional content is a converse **for every** higher/lower product-energy pair, the exact if-and-only-if population wedge for each finite tensor power, and the equality-sensitive odd/even hierarchy.

Perarnau-Llobet and coauthors [2] study energy/entropy extremizers among passive states rather than a statewise minimal activation index. Salvia and Giovannetti [3] derive general energy bounds for \(N\)-passive states, often under the additional structurally-stable hypothesis. Structural stability is not assumed here and must not be conflated with ordinary passivity. A later pedagogical account [4] supplies exact three-copy and five-copy illustrative inversions but not the arbitrary-\(N\) if-and-only-if classification.

## Limitations

The classification requires exactly equidistant three-level energies, strictly positive diagonal populations initially nonincreasing with energy, and unconstrained joint cyclic unitaries on independent copies. It does not characterize higher-dimensional systems, nonequidistant spectra, coherences, rank-deficient boundary states, catalyst-assisted work extraction, thermal operations, or the global maximum of extractable work. A permutation of two word states supplies a strictly positive work witness, not necessarily the optimal work yield. Related results may express the finite-copy criterion through alternate thermomajorization or lattice-order language; literature comparison is not a proof of absolute novelty.

## References

[1] P. Skrzypczyk, R. Silva, N. Brunner, *A short note on passivity, complete passivity and virtual temperatures*, arXiv:1412.5485 (first public 2014-12-17), especially section IV equation (9) and Appendix A. https://arxiv.org/abs/1412.5485

[2] M. Perarnau-Llobet et al., *Most energetic passive states*, arXiv:1502.07311 (first public 2015-02-25). https://arxiv.org/abs/1502.07311

[3] R. Salvia, V. Giovannetti, *Energy upper bound for structurally stable N-passive states*, arXiv:1912.02099 (first public 2019-12-02). https://arxiv.org/abs/1912.02099

[4] *Complete Passivity, KMS Structure, and Resource Conversion*, QFT.org, section “Exact activation in three truncated oscillator copies”. https://qft.org/quantum-information/energy-entropy-localization/complete-passivity-kms-resource-conversion/
