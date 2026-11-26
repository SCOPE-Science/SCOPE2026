# Complete temporal-two ring zeta classification for elementary cellular automata

## Finding

Let \(F_r\) be elementary cellular automaton (ECA) rule \(r\), for each Wolfram rule \(0\le r\le255\). On the cyclic binary ring of length \(n\ge1\), let \(a_{r,n}\) count configurations fixed after one update, and \(b_{r,n}\) count configurations fixed after two updates. The number of configurations with **exact temporal period two** is \(b_{r,n}-a_{r,n}\), so the number of two-point temporal orbits is \((b_{r,n}-a_{r,n})/2\).

For every rule and every positive ring length, there are explicitly computable integer polynomials \(D_r(z)\) and \(E_r(z)\), of degrees at most four and sixteen, respectively, each with constant coefficient one, such that
\[
\exp\!\left(\sum_{n\ge1}\frac{a_{r,n}}n z^n\right)=\frac1{D_r(z)},\qquad
\exp\!\left(\sum_{n\ge1}\frac{b_{r,n}}n z^n\right)=\frac1{E_r(z)}.
\]
In particular the spatial exponential generating function of exact temporal-two configurations is rational:
\[
\exp\!\left(\sum_{n\ge1}\frac{b_{r,n}-a_{r,n}}n z^n\right)=\frac{D_r(z)}{E_r(z)}.
\]
An exhaustive exact-integer classification of all \(256\) rules gives **51 distinct ordered polynomial pairs** \((D_r,E_r)\), **40 distinct** \(E_r\), and **25 distinct reduced rational functions** \(D_r/E_r\). Exactly **107** ECA rules have no genuine temporal two-cycle on any finite cyclic ring; the other **149** all have one on a ring of length at most six. This length-six bound is **optimal**, being first attained by twelve rules. The full first-witness distribution over the 256 rules is:

| Least cyclic ring length exhibiting an exact temporal two-cycle | Number of ECA rules |
| --- | ---: |
| 1 | 64 |
| 2 | 48 |
| 3 | 6 |
| 4 | 17 |
| 5 | 2 |
| 6 | 12 |
| None, at any length | 107 |

The three accompanying complete CSV files give every rule's denominators, rational-function class, and least witness length, as well as the class memberships.

## Assumptions and scope

The local rule is the binary map \(f_r:\{0,1\}^3\to\{0,1\}\), specified by the Wolfram convention that \(f_r(\ell,m,u)\) is bit number \(4\ell+2m+u\) of \(r\), where bit zero is the least significant bit. The cyclic map on \(\{0,1\}^n\) is \(F_{r,n}(x)_i=f_r(x_{i-1},x_i,x_{i+1})\), with every index modulo \(n\). Repeated indices for \(n=1,2\) are intentional. All formal power series and polynomial equalities are over the rationals (with integer coefficients wherever stated). Distinct spatial rotations of a configuration are counted as distinct labeled ring configurations; temporal two-orbits are unordered pairs \(\{x,F_{r,n}(x)\}\), with no additional quotient by spatial rotation.

## Proof

**1. Exact finite-state trace model.** For each \(k\in\{1,2\}\), define an integer adjacency matrix \(M_{r,k}\) indexed by all \(2k\)-bit words \(u=(u_0,\ldots,u_{2k-1})\). For each appended bit \(t\in\{0,1\}\) form the \((2k+1)\)-bit word \(w=(u_0,\ldots,u_{2k-1},t)\), and let \(v=(u_1,\ldots,u_{2k-1},t)\). Include one directed edge \(u\to v\) when applying the ECA rule locally \(k\) successive times to \(w\) produces \(w_k\) at its center. Sum edge multiplicities to define the matrix entry (parallel edges are retained where present). As paths advance, the overlapping words enforce consistency, so closed directed paths of length \(n\) are in bijection with cyclic length-\(n\) binary configurations satisfying \(F_{r,n}^k(x)=x\), including for \(n<2k+1\). Hence
\[
\operatorname{tr}(M_{r,1}^n)=a_{r,n},\qquad
\operatorname{tr}(M_{r,2}^n)=b_{r,n}\quad(n\ge1).
\]

**2. Rational spatial zeta functions.** For any finite square matrix \(M\), the formal logarithmic determinant identity
\[
-\log\det(I-zM)=\sum_{n\ge1}\operatorname{tr}(M^n)z^n/n
\]
proves the displayed zeta identities with \(D_r(z)=\det(I-zM_{r,1})\) and \(E_r(z)=\det(I-zM_{r,2})\). Taking their quotient gives the exact temporal-two zeta function. Since \(F_{r,n}^2(x)=x\) partitions its fixed configurations into disjoint orbits of size one and two, the actual number of prime-two temporal orbits is one half of the difference of traces.

**3. Complete finite census with exact identities.** Both matrices have dimensions four and sixteen. For any \(m\times m\) integer matrix \(M\), let \(t_j=\operatorname{tr}(M^j)\), let \(c_0=1\), and recursively define
\[
 c_k=-\frac1k\sum_{j=1}^k c_{k-j}t_j\quad(1\le k\le m).
\]
Newton's identities prove \(\det(I-zM)=\sum_{k=0}^m c_kz^k\), so the recurrence generates the entire polynomial *exactly* after finitely many integer matrix multiplications. The supplied generator constructs both matrices independently from every one of the 256 possible truth tables, reduces each polynomial quotient over \(\mathbb Q[z]\), and groups equal full polynomial pairs and equal reduced ratios. The accompanying tables are the full, explicitly checkable result of those finite operations: 51 pairs, 40 second-iterate denominators, and 25 reduced ratios. This is an exhaustive census because each of the 256 eight-bit truth tables is processed and exact finite polynomial comparison is decisive; there is no asymptotic extrapolation from ring lengths.

**4. All-length absence and the optimal six-site witness.** The formal logarithm is invertible for series with constant term one. Consequently \(D_r=E_r\) if and only if \(a_{r,n}=b_{r,n}\) for *every* positive \(n\). The exact table contains 107 rules with this polynomial identity. For each of the other 149 rules, the tables and integer trace evaluations exhibit a strict inequality \(b_{r,n}>a_{r,n}\) at a specific \(n\le6\), as reported by the first-witness column. Exhaustively checking all earlier \(n\) establishes minimality for each. Twelve explicit tabulated rules first witness the strict inequality at \(n=6\), so no smaller universal detection bound is possible. These finite claims follow by exhaustive arithmetic over exactly the 256 ECA rules; the all-length conclusion follows *only* through the proved determinant identity.

## Verification

All evidence is standalone. Running `python3 build_tables.py` in this directory regenerates `eca2_rules.csv`, `eca2_classes.csv`, and `eca2_ratio_classes.csv` from integer matrices. Running `python3 verify.py` then independently rebuilds all matrices and all denominators, verifies all 256 tabulated identities, checks exact reduced rational-function classes, tests the ring-length-six witness cutoff, and compares traces with direct enumeration of all binary cyclic configurations for every length from one through eight. Expected final message:

```text
VERIFY_OK rules=256 pair_types=51 second_fixed_zeta_types=40 exact_two_zeta_types=25 temporally_two_rules=149 max_witness_ring=6
```

The full infinite-ring claims rely on the symbolic trace/determinant proof, not on testing finitely many cyclic rings. The finite 256-rule census is complete and exactly reproducible from the supplied source and all 256 table rows.

## Relationship to prior work

Zhu and Richard's 2026 study examines Koopman spectra of finite-periodic ECA realizations and motivates an exact all-rule dynamical invariant. The publicly accessible abstract states an all-ECA spectral classification; its detailed full text was not available for comparison, so **whether it independently contains some exact count tables is unresolved**. The 2021 analysis of Taga and collaborators studies Koopman spectra for all ECA on a fixed ring of 13 sites, not this variable-ring exact spatial zeta census; their 2023 paper studies reconstruction of Koopman eigenvalues. Classical ECA phenomenological classifications likewise distinguish transient dynamics or symmetry classes, rather than the 256-rule set of rational temporal-two spatial zeta functions. A separate earlier Rule 18-specific exact-two enumeration is a strict special case of the present full ECA table and is not claimed as novel separately. The de Bruijn transfer-matrix and determinant tools are established methods and are not claimed as new. The novelty assessed here is the **complete exact classification, reduction to 25 rational types, and sharp all-rule six-site detection bound**.

## Limitations

This is a theorem about exact temporal period two on *finite cyclic rings*, uniformly in ring length; it does not describe higher temporal periods, limiting state distributions, or infinite-lattice orbits. All 256 numerical class and cutoff assertions depend on the inspectable, deterministic exact integer computation; no separate human mathematical audit is claimed. The uninspected full text of Zhu and Richard (2026), and possibly older databases of ECA periodic dynamics under different terminology, pose residual bibliographic priority risks. Arithmetic reproducibility does not eliminate that literature risk.

## References

- Q. Zhu and S. Richard, *Elementary cellular automata: spectral properties of Koopman operator for finite periodic realizations* (2026), arXiv:2610.10967, first posted October 7, 2026. https://arxiv.org/abs/2610.10967
- K. Taga et al., *Koopman spectral analysis of elementary cellular automata* (2021), arXiv:2106.01118. https://arxiv.org/abs/2106.01118
- K. Taga et al., *Dynamic mode decomposition for Koopman spectral analysis of elementary cellular automata* (2023), arXiv:2312.01690. https://arxiv.org/abs/2312.01690
